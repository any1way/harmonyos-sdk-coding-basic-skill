---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/use-jsvm-process
title: 使用JSVM-API实现JS与C/C++语言交互开发流程
breadcrumb: 指南 > NDK开发 > 代码开发 > 使用JSVM-API实现JS与C/C++语言交互 > 使用JSVM-API实现JS与C/C++语言交互开发流程
category: harmonyos-guides
scraped_at: 2026-06-01T15:15:51+08:00
doc_updated_at: 2026-05-26
content_hash: sha256:f11714001657646db7bb4c9c392567b1dba822f5e3d09348063dc8817f4bcda0
---
使用JSVM-API实现跨语言交互，首先需按其机制注册和加载模块。

* ArkTS/JS侧：实现C++方法的调用。代码比较简单，import一个对应的so库后，即可调用C++方法。
* Native侧：.cpp文件，实现模块的注册。需要提供注册lib库的名称，并在注册回调方法中定义接口的映射关系，即Native方法及对应的JS/ArkTS接口名称等。

此处以在ArkTS/JS侧和Native侧实现RunTest()接口实现跨语言交互为例，展示使用JSVM-API进行跨语言交互的流程。

## 创建Native C++工程

具体见[创建NDK工程](../../../创建NDK工程/create-with-ndk.md)

## Native侧方法的实现

参考[使用Node-API实现跨语言交互开发流程](../../使用Node-API实现ArkTSJS与CC++语言交互/使用Node-API实现跨语言交互开发流程/use-napi-process.md#native侧方法的实现)，以下代码提供了“使用JSVM-API实现JS与C/C++语言交互开发流程”Native侧方法实现的一个demo。

* 在index.d.ts文件中，提供JS侧的接口方法。

  ```
  1. export const runTest: () => void;
  ```

  [Index.d.ts](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkTS/JSVMAPI/JsvmProcess/entry/src/main/cpp/types/libentry/Index.d.ts#L16-L18)
* 在oh-package.json5文件中将index.d.ts与cpp文件关联起来。

  ```
  1. {
  2. "name": "libentry.so",
  3. "types": "./index.d.ts",
  4. "version": "",
  5. "description": "Please describe the basic information."
  6. }
  ```
* 在CMakeLists.txt文件中配置CMake打包参数。

  ```
  1. # entry/src/main/cpp/CMakeLists.txt
  2. cmake_minimum_required(VERSION 3.4.1)
  3. project(JSVMDemo)

  5. set(NATIVERENDER_ROOT_PATH ${CMAKE_CURRENT_SOURCE_DIR})
  6. # 日志打印配置
  7. add_definitions( "-DLOG_DOMAIN=0xd0d0" )
  8. add_definitions( "-DLOG_TAG=\"testTag\"" )
  9. include_directories(${NATIVERENDER_ROOT_PATH}
  10. ${NATIVERENDER_ROOT_PATH}/include)

  12. # 添加名为entry的库
  13. add_library(entry SHARED hello.cpp)
  14. # 构建此可执行文件需要链接的库
  15. target_link_libraries(entry PUBLIC libace_napi.z.so libjsvm.so libhilog_ndk.z.so)
  ```
* 新建entry/src/main/cpp/hello.cpp，实现Native侧的runTest接口。具体代码如下：

  ```
  1. #include "napi/native_api.h"
  2. #include "hilog/log.h"
  3. #include "ark_runtime/jsvm.h"

  5. #define LOG_DOMAIN 0x3200
  6. #define LOG_TAG "APP"

  8. static int g_aa = 0;

  10. #define CHECK_RET(theCall)                                                                                             \
  11. do {                                                                                                               \
  12. JSVM_Status cond = theCall;                                                                                    \
  13. if ((cond) != JSVM_OK) {                                                                                       \
  14. const JSVM_ExtendedErrorInfo *info;                                                                        \
  15. OH_JSVM_GetLastErrorInfo(env, &info);                                                                      \
  16. OH_LOG_ERROR(LOG_APP, "jsvm fail file: %{public}s line: %{public}d ret = %{public}d message = %{public}s", \
  17. __FILE__, __LINE__, cond, info != nullptr ? info->errorMessage : "");                         \
  18. return -1;                                                                                                 \
  19. }                                                                                                              \
  20. } while (0)

  22. #define CHECK(theCall)                                                                                                 \
  23. do {                                                                                                               \
  24. JSVM_Status cond = theCall;                                                                                    \
  25. if ((cond) != JSVM_OK) {                                                                                       \
  26. OH_LOG_ERROR(LOG_APP, "jsvm fail file: %{public}s line: %{public}d ret = %{public}d", __FILE__, __LINE__,  \
  27. cond);                                                                                        \
  28. return -1;                                                                                                 \
  29. }                                                                                                              \
  30. } while (0)

  32. // 用于调用theCall并检查其返回值是否为JSVM_OK。
  33. // 如果不是，则调用OH_JSVM_GetLastErrorInfo处理错误并返回retVal。
  34. #define JSVM_CALL_BASE(env, theCall, retVal)                                                                           \
  35. do {                                                                                                               \
  36. JSVM_Status cond = theCall;                                                                                    \
  37. if (cond != JSVM_OK) {                                                                                         \
  38. const JSVM_ExtendedErrorInfo *info;                                                                        \
  39. OH_JSVM_GetLastErrorInfo(env, &info);                                                                      \
  40. OH_LOG_ERROR(LOG_APP, "jsvm fail file: %{public}s line: %{public}d ret = %{public}d message = %{public}s", \
  41. __FILE__, __LINE__, cond, info != nullptr ? info->errorMessage : "");                         \
  42. return retVal;                                                                                             \
  43. }                                                                                                              \
  44. } while (0)

  46. // JSVM_CALL_BASE的简化版本，返回nullptr
  47. #define JSVM_CALL(theCall) JSVM_CALL_BASE(env, theCall, nullptr)

  49. // OH_JSVM_StrictEquals的样例方法
  50. static JSVM_Value IsStrictEquals(JSVM_Env env, JSVM_CallbackInfo info)
  51. {
  52. // 接受两个入参
  53. size_t argc = 2;
  54. JSVM_Value args[2] = {nullptr};
  55. JSVM_CALL(OH_JSVM_GetCbInfo(env, info, &argc, args, nullptr, nullptr));
  56. // 调用OH_JSVM_StrictEquals接口判断给定的两个JavaScript value是否严格相等
  57. bool result = false;
  58. JSVM_Status status = OH_JSVM_StrictEquals(env, args[0], args[1], &result);
  59. if (status != JSVM_OK) {
  60. OH_LOG_ERROR(LOG_APP, "JSVM OH_JSVM_StrictEquals: failed");
  61. } else {
  62. OH_LOG_INFO(LOG_APP, "JSVM OH_JSVM_StrictEquals: success: %{public}d", result);
  63. }
  64. JSVM_Value isStrictEqual;
  65. JSVM_CALL(OH_JSVM_GetBoolean(env, result, &isStrictEqual));
  66. return isStrictEqual;
  67. }
  68. // IsStrictEquals注册回调
  69. static JSVM_CallbackStruct param[] = {
  70. {.data = nullptr, .callback = IsStrictEquals},
  71. };
  72. static JSVM_CallbackStruct *method = param;
  73. // IsStrictEquals方法别名，供JS调用
  74. static JSVM_PropertyDescriptor descriptor[] = {
  75. {"isStrictEquals", nullptr, method++, nullptr, nullptr, nullptr, JSVM_DEFAULT},
  76. };
  77. // 样例测试js
  78. const char *SRC_CALL_NATIVE = R"JS(    let data = '123';
  79. let value = 123;
  80. isStrictEquals(data, value);)JS";

  82. static int32_t TestJSVM()
  83. {
  84. JSVM_InitOptions initOptions = {0};
  85. JSVM_VM vm;
  86. JSVM_Env env = nullptr;
  87. JSVM_VMScope vmScope;
  88. JSVM_EnvScope envScope;
  89. JSVM_HandleScope handleScope;
  90. JSVM_Value result;
  91. // 初始化JavaScript引擎实例
  92. if (g_aa == 0) {
  93. g_aa++;
  94. CHECK(OH_JSVM_Init(&initOptions));
  95. }
  96. // 创建JSVM环境
  97. CHECK(OH_JSVM_CreateVM(nullptr, &vm));
  98. CHECK(OH_JSVM_OpenVMScope(vm, &vmScope));
  99. CHECK(OH_JSVM_CreateEnv(vm, sizeof(descriptor) / sizeof(descriptor[0]), descriptor, &env));
  100. CHECK_RET(OH_JSVM_OpenEnvScope(env, &envScope));
  101. CHECK_RET(OH_JSVM_OpenHandleScope(env, &handleScope));

  103. // 通过script调用测试函数
  104. JSVM_Script script;
  105. JSVM_Value jsSrc;
  106. CHECK_RET(OH_JSVM_CreateStringUtf8(env, SRC_CALL_NATIVE, JSVM_AUTO_LENGTH, &jsSrc));
  107. CHECK_RET(OH_JSVM_CompileScript(env, jsSrc, nullptr, 0, true, nullptr, &script));
  108. CHECK_RET(OH_JSVM_RunScript(env, script, &result));

  110. // 销毁JSVM环境
  111. CHECK_RET(OH_JSVM_CloseHandleScope(env, handleScope));
  112. CHECK_RET(OH_JSVM_CloseEnvScope(env, envScope));
  113. CHECK(OH_JSVM_DestroyEnv(env));
  114. CHECK(OH_JSVM_CloseVMScope(vm, vmScope));
  115. CHECK(OH_JSVM_DestroyVM(vm));
  116. return 0;
  117. }

  119. static napi_value RunTest(napi_env env, napi_callback_info info)
  120. {
  121. TestJSVM();
  122. return nullptr;
  123. }

  125. // 模块注册信息，供arkts侧调用
  126. EXTERN_C_START
  127. static napi_value Init(napi_env env, napi_value exports)
  128. {
  129. napi_property_descriptor desc[] = {{"runTest", nullptr, RunTest, nullptr, nullptr, nullptr, napi_default, nullptr}};
  130. napi_define_properties(env, exports, sizeof(desc) / sizeof(desc[0]), desc);
  131. return exports;
  132. }
  133. EXTERN_C_END

  135. static napi_module demoModule = {
  136. .nm_version = 1,
  137. .nm_flags = 0,
  138. .nm_filename = nullptr,
  139. .nm_register_func = Init,
  140. .nm_modname = "entry",
  141. .nm_priv = ((void *)0),
  142. .reserved = {0},
  143. };

  145. extern "C" __attribute__((constructor)) void RegisterEntryModule(void) { napi_module_register(&demoModule); }
  ```

  [hello.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkTS/JSVMAPI/JsvmProcess/entry/src/main/cpp/hello.cpp#L16-L162)

## ArkTS侧调用C/C++方法实现

```
1. import napitest from 'libentry.so';

3. @Entry
4. @Component
5. struct Index {
6. @State message: string = 'Hello World';

8. build() {
9. Row() {
10. Column() {
11. Text(this.message)
12. .fontSize(50)
13. .fontWeight(FontWeight.Bold)
14. .onClick(() => {
15. try {
16. napitest.runTest();
17. this.message = 'success';
18. } catch (error) {
19. console.error('An error occurred: ', error);
20. this.message = 'fail';
21. }
22. })
23. }
24. .width('100%')
25. }
26. .height('100%')
27. }
28. }
```

[Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkTS/JSVMAPI/JsvmProcess/entry/src/main/ets/pages/Index.ets#L16-L45)

预期输出结果

```
1. JSVM OH_JSVM_StrictEquals: success: 0
```
