---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/use-jsvm-create-snapshot
title: 使用JSVM-API接口进行虚拟机快照相关开发
breadcrumb: 指南 > NDK开发 > 代码开发 > 使用JSVM-API实现JS与C/C++语言交互 > JSVM-API使用指导 > 使用JSVM-API接口进行虚拟机快照相关开发
category: harmonyos-guides
scraped_at: 2026-06-01T15:15:57+08:00
doc_updated_at: 2026-05-26
content_hash: sha256:ddaa4687a3e648f980f08e573fd149cee32f26e1fc5f4eb1a64d30f137749456
---

## 简介

JavaScript虚拟机（JSVM）的快照创建功能，将当前运行时的JavaScript程序状态保存为一个快照文件，这个快照文件包含了当前的堆内存、执行上下文、函数闭包等信息。

## 基本概念

* **虚拟机启动快照**：虚拟机在某个特定时间点的状态快照，包含了当前虚拟机的所有内部状态和数据。通过创建一个启动快照，可以在之后的时间点恢复虚拟机到相同的状态。

创建和使用虚拟机启动快照可以简化一些复杂的编程任务，提高JSVM中虚拟机的管理和维护效率，增强程序的灵活性和稳定性。

## 接口说明

| 接口 | 功能说明 |
| --- | --- |
| OH\_JSVM\_CreateSnapshot | 用于创建虚拟机的启动快照 |
| OH\_JSVM\_CreateEnvFromSnapshot | 基于虚拟机的起始快照，创建一个新的环境 |

## 使用示例

### OH\_JSVM\_CreateSnapshot & OH\_JSVM\_CreateEnvFromSnapshot

用于创建和使用虚拟机的启动快照。

cpp部分代码：

**注意事项**: 需要在OH\_JSVM\_Init的时候，将JSVM对外部的依赖注册到initOptions.externalReferences中。

```
1. #include "napi/native_api.h"
2. #include "ark_runtime/jsvm.h"
3. #include <hilog/log.h>
4. #include <fstream>

6. #define LOG_DOMAIN 0x0202
7. #define LOG_TAG "TEST_TAG"

9. static int g_aa = 0;

11. #define CHECK_RET(theCall)                                                                           \
12. do {                                                                                             \
13. JSVM_Status cond = theCall;                                                                  \
14. if ((cond) != JSVM_OK) {                                                                     \
15. const JSVM_ExtendedErrorInfo *info;                                                      \
16. OH_JSVM_GetLastErrorInfo(env, &info);                                                    \
17. OH_LOG_ERROR(LOG_APP,                                                                    \
18. "jsvm fail file: %{public}s line: %{public}d ret = %{public}d message = %{public}s", \
19. __FILE__,                                                                            \
20. __LINE__,                                                                            \
21. cond,                                                                                \
22. info != nullptr ? info->errorMessage : "");                                          \
23. return -1;                                                                               \
24. }                                                                                            \
25. } while (0)

27. #define CHECK(theCall)                                                                                              \
28. do {                                                                                                            \
29. JSVM_Status cond = theCall;                                                                                 \
30. if ((cond) != JSVM_OK) {                                                                                    \
31. OH_LOG_ERROR(                                                                                           \
32. LOG_APP, "jsvm fail file: %{public}s line: %{public}d ret = %{public}d", __FILE__, __LINE__, cond); \
33. return -1;                                                                                              \
34. }                                                                                                           \
35. } while (0)

37. // 用于调用theCall并检查其返回值是否为JSVM_OK。
38. // 如果不是，则调用GET_AND_THROW_LAST_ERROR处理错误并返回retVal。
39. #define JSVM_CALL_BASE(env, theCall, retVal)                                                         \
40. do {                                                                                             \
41. JSVM_Status cond = theCall;                                                                  \
42. if (cond != JSVM_OK) {                                                                       \
43. const JSVM_ExtendedErrorInfo *info;                                                      \
44. OH_JSVM_GetLastErrorInfo(env, &info);                                                    \
45. OH_LOG_ERROR(LOG_APP,                                                                    \
46. "jsvm fail file: %{public}s line: %{public}d ret = %{public}d message = %{public}s", \
47. __FILE__,                                                                            \
48. __LINE__,                                                                            \
49. cond,                                                                                \
50. info != nullptr ? info->errorMessage : "");                                          \
51. return retVal;                                                                           \
52. }                                                                                            \
53. } while (0)

55. // JSVM_CALL_BASE的简化版本，返回nullptr
56. #define JSVM_CALL(theCall) JSVM_CALL_BASE(env, theCall, nullptr)

58. static const int MAX_BUFFER_SIZE = 128;
59. // CreateHelloString()函数需绑定到JSVM虚拟机, 用于OH_JSVM_CreateSnapshot虚拟机快照的正常创建
60. static JSVM_Value CreateHelloString(JSVM_Env env, JSVM_CallbackInfo info)
61. {
62. JSVM_Value outPut;
63. OH_JSVM_CreateStringUtf8(env, "Hello world!", JSVM_AUTO_LENGTH, &outPut);
64. return outPut;
65. }
66. // 提供外部引用的方式以便JavaScript环境可以调用绑定的函数
67. static JSVM_CallbackStruct helloCb = {CreateHelloString, nullptr};

69. static intptr_t g_externals[] = {
70. (intptr_t)&helloCb,
71. 0,
72. };

74. static JSVM_Value RunVMScript(JSVM_Env env, std::string &src)
75. {
76. // 打开handleScope作用域
77. JSVM_HandleScope handleScope;
78. OH_JSVM_OpenHandleScope(env, &handleScope);
79. JSVM_Value jsStr = nullptr;
80. OH_JSVM_CreateStringUtf8(env, src.c_str(), src.size(), &jsStr);
81. // 编译JavaScript代码
82. JSVM_Script script;
83. OH_JSVM_CompileScript(env, jsStr, nullptr, 0, true, nullptr, &script);
84. // 执行JavaScript代码
85. JSVM_Value result = nullptr;
86. OH_JSVM_RunScript(env, script, &result);
87. // 关闭handleScope作用域
88. OH_JSVM_CloseHandleScope(env, handleScope);
89. return result;
90. }
91. // OH_JSVM_CreateSnapshot的样例方法
92. static void CreateVMSnapshot()
93. {
94. // 创建JavaScript虚拟机实例,打开虚拟机作用域
95. JSVM_VM vm;
96. JSVM_CreateVMOptions vmOptions;
97. memset(&vmOptions, 0, sizeof(vmOptions));
98. // isForSnapshotting设置该虚拟机是否用于创建快照
99. vmOptions.isForSnapshotting = true;
100. OH_JSVM_CreateVM(&vmOptions, &vm);
101. JSVM_VMScope vmScope;
102. OH_JSVM_OpenVMScope(vm, &vmScope);
103. // 创建JavaScript环境,打开环境作用域
104. JSVM_Env env;
105. // 将native函数注册成JavaScript可调用的方法
106. JSVM_PropertyDescriptor descriptor[] = {
107. {"createHelloString", nullptr, &helloCb, nullptr, nullptr, nullptr, JSVM_DEFAULT},
108. };
109. OH_JSVM_CreateEnv(vm, 1, descriptor, &env);
110. JSVM_EnvScope envScope;
111. OH_JSVM_OpenEnvScope(env, &envScope);
112. // 使用OH_JSVM_CreateSnapshot创建虚拟机的启动快照
113. const char *blobData = nullptr;
114. size_t blobSize = 0;
115. JSVM_Env envs[1] = {env};
116. OH_JSVM_CreateSnapshot(vm, 1, envs, &blobData, &blobSize);
117. // 将snapshot保存到文件中
118. // 保存快照数据，/data/storage/el2/base/files/test_blob.bin为沙箱路径
119. // 以包名为com.example.jsvm为例，实际文件会保存到/data/app/el2/100/base/com.example.jsvm/files/test_blob.bin
120. std::ofstream file("/data/storage/el2/base/files/test_blob.bin",
121. std::ios::out | std::ios::binary | std::ios::trunc);
122. file.write(blobData, blobSize);
123. file.close();
124. // 关闭并销毁环境和虚拟机
125. OH_JSVM_CloseEnvScope(env, envScope);
126. OH_JSVM_DestroyEnv(env);
127. OH_JSVM_CloseVMScope(vm, vmScope);
128. OH_JSVM_DestroyVM(vm);
129. }

131. static void RunVMSnapshot()
132. {
133. // blobData的生命周期不能短于vm的生命周期
134. // 从文件中读取snapshot
135. std::vector<char> blobData;
136. std::ifstream file("/data/storage/el2/base/files/test_blob.bin", std::ios::in | std::ios::binary | std::ios::ate);
137. size_t blobSize = file.tellg();
138. blobData.resize(blobSize);
139. file.seekg(0, std::ios::beg);
140. file.read(blobData.data(), blobSize);
141. file.close();
142. OH_LOG_INFO(LOG_APP, "Test JSVM RunVMSnapshot read file blobSize = : %{public}ld", blobSize);
143. // 使用快照数据创建虚拟机实例
144. JSVM_VM vm;
145. JSVM_CreateVMOptions vmOptions;
146. memset(&vmOptions, 0, sizeof(vmOptions));
147. vmOptions.snapshotBlobData = blobData.data();
148. vmOptions.snapshotBlobSize = blobSize;
149. OH_JSVM_CreateVM(&vmOptions, &vm);
150. JSVM_VMScope vmScope;
151. OH_JSVM_OpenVMScope(vm, &vmScope);
152. // 从快照中创建环境env
153. JSVM_Env env;
154. OH_JSVM_CreateEnvFromSnapshot(vm, 0, &env);
155. JSVM_EnvScope envScope;
156. OH_JSVM_OpenEnvScope(env, &envScope);
157. // 执行js脚本，快照记录的env中定义了createHelloString()
158. std::string src = "createHelloString()";
159. JSVM_Value result = RunVMScript(env, src);
160. // 环境关闭前检查脚本运行结果
161. char str[MAX_BUFFER_SIZE];
162. OH_JSVM_GetValueStringUtf8(env, result, str, MAX_BUFFER_SIZE, nullptr);
163. if (strcmp(str, "Hello world!") != 0) {
164. OH_LOG_ERROR(LOG_APP, "jsvm fail file: %{public}s line: %{public}d", __FILE__, __LINE__);
165. }
166. // 关闭并销毁环境和虚拟机
167. OH_JSVM_CloseEnvScope(env, envScope);
168. OH_JSVM_DestroyEnv(env);
169. OH_JSVM_CloseVMScope(vm, vmScope);
170. OH_JSVM_DestroyVM(vm);
171. return;
172. }

174. static JSVM_Value AdjustExternalMemory(JSVM_Env env, JSVM_CallbackInfo info)
175. {
176. // 在创建虚拟机快照时，如果存在对外部的依赖，需要在OH_JSVM_Init时，将外部依赖注册到initOptions.externalReferences中
177. // 创建虚拟机快照并将快照保存到文件中
178. CreateVMSnapshot();
179. // snapshot可以记录下特定的js执行环境，可以跨进程通过snapshot快速还原出js执行上下文环境
180. RunVMSnapshot();
181. JSVM_Value result = nullptr;
182. OH_JSVM_CreateInt32(env, 0, &result);
183. return result;
184. }

186. static JSVM_CallbackStruct param[] = {
187. {.data = nullptr, .callback = AdjustExternalMemory},
188. };
189. static JSVM_CallbackStruct *method = param;
190. // AdjustExternalMemory方法别名，供JS调用
191. static JSVM_PropertyDescriptor descriptor[] = {
192. {"adjustExternalMemory", nullptr, method, nullptr, nullptr, nullptr, JSVM_DEFAULT},
193. };

195. // 样例测试JS
196. const char *SRC_CALL_NATIVE = R"JS(adjustExternalMemory();)JS";

198. static int32_t TestJSVM()
199. {
200. JSVM_InitOptions initOptions = {0};
201. JSVM_VM vm;
202. JSVM_Env env = nullptr;
203. JSVM_VMScope vmScope;
204. JSVM_EnvScope envScope;
205. JSVM_HandleScope handleScope;
206. JSVM_Value result;
207. // 初始化JavaScript引擎实例
208. if (g_aa == 0) {
209. g_aa++;
210. initOptions.externalReferences = g_externals;
211. int argc = 0;
212. char **argv = nullptr;
213. initOptions.argc = &argc;
214. initOptions.argv = argv;
215. CHECK(OH_JSVM_Init(&initOptions));
216. }
217. // 创建JSVM环境
218. CHECK(OH_JSVM_CreateVM(nullptr, &vm));
219. CHECK(OH_JSVM_OpenVMScope(vm, &vmScope));
220. CHECK(OH_JSVM_CreateEnv(vm, sizeof(descriptor) / sizeof(descriptor[0]), descriptor, &env));
221. CHECK_RET(OH_JSVM_OpenEnvScope(env, &envScope));
222. CHECK_RET(OH_JSVM_OpenHandleScope(env, &handleScope));

224. // 通过script调用测试函数
225. JSVM_Script script;
226. JSVM_Value jsSrc;
227. CHECK_RET(OH_JSVM_CreateStringUtf8(env, SRC_CALL_NATIVE, JSVM_AUTO_LENGTH, &jsSrc));
228. CHECK_RET(OH_JSVM_CompileScript(env, jsSrc, nullptr, 0, true, nullptr, &script));
229. CHECK_RET(OH_JSVM_RunScript(env, script, &result));

231. // 销毁JSVM环境
232. CHECK_RET(OH_JSVM_CloseHandleScope(env, handleScope));
233. CHECK_RET(OH_JSVM_CloseEnvScope(env, envScope));
234. CHECK(OH_JSVM_DestroyEnv(env));
235. CHECK(OH_JSVM_CloseVMScope(vm, vmScope));
236. CHECK(OH_JSVM_DestroyVM(vm));
237. return 0;
238. }

240. static napi_value RunTest(napi_env env, napi_callback_info info)
241. {
242. TestJSVM();
243. return nullptr;
244. }

246. EXTERN_C_START
247. static napi_value Init(napi_env env, napi_value exports)
248. {
249. OH_LOG_INFO(LOG_APP, "JSVM Init");
250. napi_property_descriptor desc[] = {
251. {"runTest", nullptr, RunTest, nullptr, nullptr, nullptr, napi_default, nullptr},
252. };

254. napi_define_properties(env, exports, sizeof(desc) / sizeof(desc[0]), desc);
255. return exports;
256. }
257. EXTERN_C_END

259. static napi_module demoModule = {
260. .nm_version = 1,
261. .nm_flags = 0,
262. .nm_filename = nullptr,
263. .nm_register_func = Init,
264. .nm_modname = "createsnapshot",
265. .nm_priv = ((void *)0),
266. .reserved = {0},
267. };

269. extern "C" __attribute__((constructor)) void RegisterEntryModule(void) { napi_module_register(&demoModule); }
```

[hello.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkTS/JSVMAPI/JsvmUsageGuide/UsageInstructionsOne/createsnapshot/src/main/cpp/hello.cpp#L16-L286)

ArkTS侧示例代码：

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
15. // runtest
16. napitest.runTest();
17. })
18. }
19. .width('100%')
20. }
21. .height('100%')
22. }
23. }
```

执行结果

在LOG中输出：

```
1. Test JSVM RunVMSnapshot read file blobSize = : 300064
```

多次点击屏幕,LOG中输出:

```
1. Test JSVM RunVMSnapshot read file blobSize = : 300176
2. Test JSVM RunVMSnapshot read file blobSize = : 300064
3. Test JSVM RunVMSnapshot read file blobSize = : 300160
4. Test JSVM RunVMSnapshot read file blobSize = : 300032
5. Test JSVM RunVMSnapshot read file blobSize = : 300176
6. Test JSVM RunVMSnapshot read file blobSize = : 300048
```

上述执行结果是因为在读取快照文件时，blobSize 的值来源于快照文件的大小（通过 file.tellg() 获取）。快照文件的大小直接决定了 blobSize 的值，所以会输出不同的值。
