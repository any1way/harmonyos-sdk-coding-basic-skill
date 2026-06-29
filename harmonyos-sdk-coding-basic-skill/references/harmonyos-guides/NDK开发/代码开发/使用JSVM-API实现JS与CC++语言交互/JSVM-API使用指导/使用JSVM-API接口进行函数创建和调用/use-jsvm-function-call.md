---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/use-jsvm-function-call
title: 使用JSVM-API接口进行函数创建和调用
breadcrumb: 指南 > NDK开发 > 代码开发 > 使用JSVM-API实现JS与C/C++语言交互 > JSVM-API使用指导 > 使用JSVM-API接口进行函数创建和调用
category: harmonyos-guides
scraped_at: 2026-06-01T15:16:00+08:00
doc_updated_at: 2026-05-26
content_hash: sha256:aa12bf9061ce83a3f6f56a6204f9fecfc375b45d227755b8788cf87c51a7e46b
---
## 简介

函数调用允许开发者从JSVM模块中调用JavaScript函数，并传参，或者直接在JSVM模块中创建一个JavaScript函数。

## 基本概念

函数是一种重要的编程概念，用于执行特定任务，提升代码可读性与复用性，简化复杂操作，并实现代码的模块化和结构化，便于理解、维护和扩展。

## 接口说明

| 接口 | 功能说明 |
| --- | --- |
| OH\_JSVM\_GetCbInfo | 从给定的callback info中获取有关调用的详细信息，如参数和this指针。 |
| OH\_JSVM\_CallFunction | 在C/C++侧调用JavaScript方法。 |
| OH\_JSVM\_IsFunction | 判断对象是否为函数对象。 |
| OH\_JSVM\_CreateFunction | 用于创建JavaScript函数,用于从JavaScript环境中调用C/C++代码中的函数, 需要设置到一个JavaScript对象中才可以进行调用。 |

## 使用示例

JSVM-API接口开发流程参考[使用JSVM-API实现JS与C/C++语言交互开发流程](../../使用JSVM-API实现JS与CC++语言交互开发流程/use-jsvm-process.md)，本文仅对接口对应C++相关代码进行展示。

### OH\_JSVM function整合测试

cpp测试全量代码，入口为TEST\_FUNC

```
1. #include "napi/native_api.h"
2. #include "hilog/log.h"
3. #include "ark_runtime/jsvm.h"

5. #define LOG_DOMAIN 0x3200
6. #define LOG_TAG "APP"

8. #define CHECK_RET(cond)                                                                                                \
9. if ((cond)) {                                                                                                      \
10. const JSVM_ExtendedErrorInfo *info;                                                                            \
11. OH_JSVM_GetLastErrorInfo(env, &info);                                                                          \
12. OH_LOG_ERROR(LOG_APP, "jsvm fail file: %{public}s line: %{public}d ret = %{public}d message = %{public}s",     \
13. __FILE__, __LINE__, cond, info != nullptr ? info->errorMessage : "");                             \
14. return -1;                                                                                                     \
15. }

17. #define CHECK(cond)                                                                                                    \
18. if (!(cond)) {                                                                                                     \
19. OH_LOG_ERROR(LOG_APP, "jsvm fail file: %{public}s line: %{public}d ret = %{public}d", __FILE__, __LINE__,      \
20. cond);                                                                                            \
21. return -1;                                                                                                     \
22. }

24. JSVM_Value NativeCreateFunctionTest(JSVM_Env env, JSVM_CallbackInfo info)
25. {
26. void *data;
27. size_t argc = 1;
28. JSVM_Value argv[1] = {nullptr};
29. JSVM_Value thisArg;
30. // 获取callback 参数信息
31. JSVM_Status ret = OH_JSVM_GetCbInfo(env, info, &argc, &argv[0], &thisArg, &data);
32. if (ret != JSVM_OK) {
33. const JSVM_ExtendedErrorInfo *info;
34. OH_JSVM_GetLastErrorInfo(env, &info);
35. OH_LOG_ERROR(LOG_APP, "jsvm fail file: %{public}s line: %{public}d ret = %{public}d message = %{public}s",
36. __FILE__, __LINE__, ret, info != nullptr ? info->errorMessage : "");
37. return nullptr;
38. }
39. const int maxMessageLength = 256;
40. char message[256];
41. OH_JSVM_GetValueStringLatin1(env, argv[0], message, maxMessageLength, nullptr);
42. if (data == nullptr) {
43. OH_LOG_ERROR(LOG_APP, "jsvm: %{public}s; callback data null", message);
44. } else {
45. OH_LOG_INFO(LOG_APP, "jsvm: %{public}s; %{public}s", message, (char *)data);
46. }
47. return nullptr;
48. }

50. static int32_t TEST_FUNC()
51. {
52. JSVM_InitOptions initOptions{};
53. JSVM_VM vm;
54. JSVM_Env env = nullptr;
55. JSVM_VMScope vmScope;
56. JSVM_EnvScope envScope;
57. JSVM_HandleScope handleScope;
58. JSVM_Value result;
59. static bool isVMInit = false;
60. if (!isVMInit) {
61. isVMInit = true;
62. // 单个进程只需初始化一次
63. OH_JSVM_Init(&initOptions);
64. }
65. CHECK_RET(OH_JSVM_CreateVM(nullptr, &vm));
66. CHECK_RET(OH_JSVM_OpenVMScope(vm, &vmScope));
67. CHECK_RET(OH_JSVM_CreateEnv(vm, 0, nullptr, &env));
68. CHECK_RET(OH_JSVM_OpenEnvScope(env, &envScope));
69. CHECK_RET(OH_JSVM_OpenHandleScope(env, &handleScope));

71. // 创建并检查函数
72. char hello[] = "Hello World!";
73. JSVM_CallbackStruct cb = {NativeCreateFunctionTest, (void *)hello};
74. JSVM_Value func;
75. CHECK_RET(OH_JSVM_CreateFunction(env, "", JSVM_AUTO_LENGTH, &cb, &func));
76. bool isFunction = false;
77. CHECK_RET(OH_JSVM_IsFunction(env, func, &isFunction));
78. CHECK(isFunction);

80. // 将函数设置到全局对象中
81. JSVM_Value global;
82. CHECK_RET(OH_JSVM_GetGlobal(env, &global));
83. JSVM_Value key;
84. CHECK_RET(OH_JSVM_CreateStringUtf8(env, "NativeFunc", JSVM_AUTO_LENGTH, &key));
85. CHECK_RET(OH_JSVM_SetProperty(env, global, key, func));

87. // 通过call 接口调用函数
88. JSVM_Value argv[1] = {nullptr};
89. OH_JSVM_CreateStringUtf8(env, "jsvm api call function", JSVM_AUTO_LENGTH, &argv[0]);
90. CHECK_RET(OH_JSVM_CallFunction(env, global, func, 1, argv, &result));

92. // 通过script调用函数
93. JSVM_Script script;
94. JSVM_Value jsSrc;
95. const char *srcCallNative = R"JS(NativeFunc('js source call function');)JS";
96. CHECK_RET(OH_JSVM_CreateStringUtf8(env, srcCallNative, JSVM_AUTO_LENGTH, &jsSrc));
97. CHECK_RET(OH_JSVM_CompileScript(env, jsSrc, nullptr, 0, true, nullptr, &script));
98. CHECK_RET(OH_JSVM_RunScript(env, script, &result));

100. CHECK_RET(OH_JSVM_CloseHandleScope(env, handleScope));
101. CHECK_RET(OH_JSVM_CloseEnvScope(env, envScope));
102. CHECK_RET(OH_JSVM_DestroyEnv(env));
103. CHECK_RET(OH_JSVM_CloseVMScope(vm, vmScope));
104. CHECK_RET(OH_JSVM_DestroyVM(vm));
105. return 0;
106. }
```

[hello.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkTS/JSVMAPI/JsvmUsageGuide/UsageInstructionsOne/functioncall/src/main/cpp/hello.cpp#L16-L123)

预期输出结果：

```
1. jsvm: jsvm api call function; Hello World!
2. jsvm: js source call function; Hello World!
```
