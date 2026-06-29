---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/native-httpinterceptor-guidelines
title: 使用HTTP全局拦截器 (C/C++)
breadcrumb: 指南 > 系统 > 网络 > Network Kit（网络服务） > 访问网络 > 使用HTTP全局拦截器 (C/C++)
category: harmonyos-guides
scraped_at: 2026-06-11T14:48:12+08:00
doc_updated_at: 2026-05-26
content_hash: sha256:27dfdd0f209d5b6a0613c3fc1b1a441e0569ceb02a77b64e08eb88fda7406f90
---
## 场景介绍

从API version 24开始，通过HTTP全局拦截器，开发者可以监控HTTP流量，实现日志记录功能。

## 接口说明

HTTP全局拦截器常用接口如下表所示，详细的接口说明请参考[http\_interceptor.h](<../../../../../../harmonyos-references/网络/Network Kit（网络服务）/C API/头文件/http_interceptor.h/capi-net-http-interceptor-h.md>)。

| 接口名 | 描述 |
| --- | --- |
| OH\_Http\_AddReadOnlyInterceptor(struct OH\_Http\_Interceptor \*interceptor) | 添加一个HTTP全局只读拦截器。 |
| OH\_Http\_RemoveInterceptor(struct OH\_Http\_Interceptor \*interceptor) | 删除指定的HTTP全局拦截器。 |
| OH\_Http\_RemoveAllInterceptors(int32\_t groupId) | 删除指定组ID的所有HTTP全局拦截器。 |
| OH\_Http\_StartAllInterceptors(int32\_t groupId) | 启用指定组ID的所有HTTP全局拦截器。 |
| OH\_Http\_StopAllInterceptors(int32\_t groupId) | 停用指定组ID的所有HTTP全局拦截器。 |

## 开发步骤

使用本文档涉及接口创建并使用HTTP全局拦截器时，需先创建Native C++工程，在源文件中封装相关接口，然后在ArkTS层调用封装好的接口，使用hilog或console.info等方法将日志打印到控制台或生成设备日志。

本文以添加HTTP全局只读响应拦截器、启用/停用拦截器、删除拦截器为例，提供具体的开发指导。

### 添加开发依赖

**添加动态链接库**

CMakeLists.txt中添加以下lib:

```
1. libace_napi.z.so
2. libhttp_interceptor.so
```

**头文件**

```
1. #include "napi/native_api.h"
2. #include "network/netstack/http_interceptor.h"
3. #include "network/netstack/http_interceptor_type.h"
```

### 构建工程

1. 在源文件中编写调用该API的代码，实现HTTP全局拦截器的处理函数和相关操作。

   ```
   1. #include "napi/native_api.h"
   2. #include "network/netstack/http_interceptor.h"
   3. #include "network/netstack/http_interceptor_type.h"
   4. #include "hilog/log.h"

   6. #include <cstring>

   8. #undef LOG_DOMAIN
   9. #undef LOG_TAG
   10. #define LOG_DOMAIN 0x3200 // 全局domain宏，标识业务领域
   11. #define LOG_TAG "HttpInterceptorDemo"  // 全局tag宏，标识模块日志tag

   13. // 全局拦截器实例
   14. static OH_Http_Interceptor g_responseInterceptor = {
   15. .groupId = 1,
   16. .stage = OH_STAGE_RESPONSE,
   17. .type = OH_TYPE_READ_ONLY,
   18. .enabled = 1,
   19. .handler = nullptr,
   20. };

   22. // 日志打印辅助函数
   23. void LogHeader(OH_Http_Interceptor_Headers *headers)
   24. {
   25. OH_LOG_INFO(LOG_APP, "---------------------header begin---------------------");
   26. while (headers != nullptr) {
   27. if (headers->data != nullptr) {
   28. OH_LOG_INFO(LOG_APP, "%{public}s", headers->data);
   29. }
   30. headers = headers->next;
   31. }
   32. OH_LOG_INFO(LOG_APP, "---------------------header end---------------------");
   33. }

   35. // 打印响应信息
   36. void PrintResponseInfo(OH_Http_Interceptor_Response *response)
   37. {
   38. OH_LOG_INFO(LOG_APP, "-----PrintResponseInfo Begin-----");
   39. if (response != nullptr) {
   40. OH_LOG_INFO(LOG_APP, "responseCode = %{public}d", response->responseCode);
   41. if (response->body.buffer != nullptr) {
   42. OH_LOG_INFO(LOG_APP, "body = %{public}s", response->body.buffer);
   43. }
   44. if (response->headers != nullptr) {
   45. LogHeader(response->headers);
   46. }

   48. OH_LOG_INFO(LOG_APP, "dns: %{public}lf", response->performanceTiming.dnsTiming);
   49. OH_LOG_INFO(LOG_APP, "tcp: %{public}lf", response->performanceTiming.tcpTiming);
   50. OH_LOG_INFO(LOG_APP, "tls: %{public}lf", response->performanceTiming.tlsTiming);
   51. OH_LOG_INFO(LOG_APP, "snd: %{public}lf", response->performanceTiming.firstSendTiming);
   52. OH_LOG_INFO(LOG_APP, "rcv: %{public}lf", response->performanceTiming.firstReceiveTiming);
   53. OH_LOG_INFO(LOG_APP, "tot: %{public}lf", response->performanceTiming.totalFinishTiming);
   54. OH_LOG_INFO(LOG_APP, "rdr: %{public}lf", response->performanceTiming.redirectTiming);
   55. OH_LOG_INFO(LOG_APP, "-----PrintResponseInfo End-----");
   56. }
   57. }

   59. // 响应拦截器处理函数
   60. OH_Interceptor_Result ResponseInterceptorHandler(
   61. OH_Http_Interceptor_Request *request,
   62. OH_Http_Interceptor_Response *response,
   63. int32_t *isModified)
   64. {
   65. (void)request;
   66. (void)isModified;

   68. if (response != nullptr) {
   69. OH_LOG_INFO(LOG_APP, "---Response Interceptor Handler---");
   70. PrintResponseInfo(response);
   71. }
   72. return OH_CONTINUE;
   73. }

   75. // 添加只读响应拦截器
   76. static napi_value AddResponseInterceptor(napi_env env, napi_callback_info info)
   77. {
   78. napi_value result;

   80. // 设置拦截器处理函数
   81. g_responseInterceptor.handler = ResponseInterceptorHandler;

   83. // 添加拦截器
   84. int ret = OH_Http_AddReadOnlyInterceptor(&g_responseInterceptor);

   86. OH_LOG_INFO(LOG_APP, "AddResponseInterceptor ret: %{public}d", ret);
   87. napi_create_int32(env, ret, &result);
   88. return result;
   89. }

   91. // 移除拦截器
   92. static napi_value RemoveInterceptor(napi_env env, napi_callback_info info)
   93. {
   94. napi_value result;

   96. // 移除拦截器
   97. int ret = OH_Http_RemoveInterceptor(&g_responseInterceptor);

   99. OH_LOG_INFO(LOG_APP, "RemoveInterceptor ret: %{public}d", ret);
   100. napi_create_int32(env, ret, &result);
   101. return result;
   102. }

   104. // 启用指定组的所有拦截器
   105. static napi_value StartInterceptors(napi_env env, napi_callback_info info)
   106. {
   107. napi_value result;

   109. // 启用组ID为1的所有拦截器
   110. int ret = OH_Http_StartAllInterceptors(1);

   112. OH_LOG_INFO(LOG_APP, "StartInterceptors ret: %{public}d", ret);
   113. napi_create_int32(env, ret, &result);
   114. return result;
   115. }

   117. // 停用指定组的所有拦截器
   118. static napi_value StopInterceptors(napi_env env, napi_callback_info info)
   119. {
   120. napi_value result;

   122. // 停用组ID为1的所有拦截器
   123. int ret = OH_Http_StopAllInterceptors(1);

   125. OH_LOG_INFO(LOG_APP, "StopInterceptors ret: %{public}d", ret);
   126. napi_create_int32(env, ret, &result);
   127. return result;
   128. }

   130. // 删除指定组的所有拦截器
   131. static napi_value RemoveAllInterceptors(napi_env env, napi_callback_info info)
   132. {
   133. napi_value result;

   135. // 删除组ID为1的所有拦截器
   136. int ret = OH_Http_RemoveAllInterceptors(1);

   138. OH_LOG_INFO(LOG_APP, "RemoveAllInterceptors ret: %{public}d", ret);
   139. napi_create_int32(env, ret, &result);
   140. return result;
   141. }
   ```

   [napi\_init.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/NetWork_Kit/NetWorkKit_Datatransmission/HTTP_interceptor_C/entry/src/main/cpp/napi_init.cpp#L16-L158)

   上述代码实现了一个HTTP全局只读响应拦截器，用于监控HTTP响应。在响应拦截器处理函数中，会打印响应的状态码、响应体、响应头以及性能指标等信息。
2. 初始化并导出通过N-API封装的napi\_value类型对象，通过外部函数接口将函数提供给JavaScript调用。

   ```
   1. EXTERN_C_START
   2. static napi_value Init(napi_env env, napi_value exports)
   3. {
   4. napi_property_descriptor desc[] = {
   5. {"AddResponseInterceptor", nullptr, AddResponseInterceptor, nullptr, nullptr, nullptr, napi_default, nullptr},
   6. {"RemoveInterceptor", nullptr, RemoveInterceptor, nullptr, nullptr, nullptr, napi_default, nullptr},
   7. {"StartInterceptors", nullptr, StartInterceptors, nullptr, nullptr, nullptr, napi_default, nullptr},
   8. {"StopInterceptors", nullptr, StopInterceptors, nullptr, nullptr, nullptr, napi_default, nullptr},
   9. {"RemoveAllInterceptors", nullptr, RemoveAllInterceptors, nullptr, nullptr, nullptr, napi_default, nullptr},
   10. };
   11. napi_define_properties(env, exports, sizeof(desc) / sizeof(desc[0]), desc);
   12. return exports;
   13. }
   14. EXTERN_C_END
   ```

   [napi\_init.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/NetWork_Kit/NetWorkKit_Datatransmission/HTTP_interceptor_C/entry/src/main/cpp/napi_init.cpp#L160-L175)
3. 将上一步中初始化成功的对象通过RegisterEntryModule函数，使用napi\_module\_register函数将模块注册到Node.js中。

   ```
   1. static napi_module demoModule = {
   2. .nm_version = 1,
   3. .nm_flags = 0,
   4. .nm_filename = nullptr,
   5. .nm_register_func = Init,
   6. .nm_modname = "entry",
   7. .nm_priv = ((void *)0),
   8. .reserved = {0},
   9. };

   11. extern "C" __attribute__((constructor)) void RegisterEntryModule(void)
   12. {
   13. napi_module_register(&demoModule);
   14. }
   ```

   [napi\_init.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/NetWork_Kit/NetWorkKit_Datatransmission/HTTP_interceptor_C/entry/src/main/cpp/napi_init.cpp#L177-L192)
4. 在工程的Index.d.ts文件中定义函数的类型。

   ```
   1. export const AddResponseInterceptor: () => number;
   2. export const RemoveInterceptor: () => number;
   3. export const StartInterceptors: () => number;
   4. export const StopInterceptors: () => number;
   5. export const RemoveAllInterceptors: () => number;
   ```

   [Index.d.ts](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/NetWork_Kit/NetWorkKit_Datatransmission/HTTP_interceptor_C/entry/src/main/cpp/types/libentry/Index.d.ts#L15-L21)
5. 在Index.ets文件中对上述封装好的接口进行调用。

   ```
   1. import { hilog } from '@kit.PerformanceAnalysisKit';
   2. import httpInterceptor from 'libentry.so';
   3. import { http } from '@kit.NetworkKit';

   5. const LOG_TAG: string = 'HttpInterceptorDemo';
   6. const HTTP_URL_BAIDU: string = "http://www.baidu.com";

   8. @Entry
   9. @Component
   10. struct Index {
   11. @State message: string = 'HTTP Interceptor Demo';

   13. build() {
   14. Navigation() {
   15. Column() {
   16. Text(this.message)
   17. .fontSize(20)
   18. .margin({ bottom: 20 })

   20. Column({
   21. space: 12
   22. }) {
   23. Button('Add Response Interceptor')
   24. .id('AddInterceptor')
   25. .onClick(() => {
   26. let ret = httpInterceptor.AddResponseInterceptor();
   27. hilog.info(0x0000, LOG_TAG, `AddResponseInterceptor ret: ${ret}`);
   28. })

   30. Button('Start Interceptors')
   31. .id('StartInterceptors')
   32. .onClick(() => {
   33. let ret = httpInterceptor.StartInterceptors();
   34. hilog.info(0x0000, LOG_TAG, `StartInterceptors ret: ${ret}`);
   35. })

   37. Button('Send HTTP Request')
   38. .id('networkRequest')
   39. .onClick(() => {
   40. let httpRequest: http.HttpRequest = http.createHttp();
   41. let options: http.HttpRequestOptions = {
   42. method: http.RequestMethod.POST,
   43. };
   44. httpRequest.request(HTTP_URL_BAIDU, options, (err: BusinessError, res: http.HttpResponse) => {
   45. if (err) {
   46. hilog.info(0x0000, LOG_TAG, `request fail, error code: ${err.code}, msg: ${err.message}`);
   47. httpRequest.destroy();
   48. } else {
   49. hilog.info(0x0000, LOG_TAG, `res:${JSON.stringify(res)}`);
   50. httpRequest.destroy();
   51. }
   52. });
   53. })

   55. Button('Stop Interceptors')
   56. .id('StopInterceptors')
   57. .onClick(() => {
   58. let ret = httpInterceptor.StopInterceptors();
   59. hilog.info(0x0000, LOG_TAG, `StopInterceptors ret: ${ret}`);
   60. })

   62. Button('Remove Interceptor')
   63. .id('RemoveInterceptor')
   64. .onClick(() => {
   65. let ret = httpInterceptor.RemoveInterceptor();
   66. hilog.info(0x0000, LOG_TAG, `RemoveInterceptor ret: ${ret}`);
   67. })

   69. Button('Remove All Interceptors')
   70. .id('RemoveAllInterceptors')
   71. .onClick(() => {
   72. let ret = httpInterceptor.RemoveAllInterceptors();
   73. hilog.info(0x0000, LOG_TAG, `RemoveAllInterceptors ret: ${ret}`);
   74. })
   75. }
   76. }
   77. .padding(20)
   78. }
   79. }
   80. }
   ```

   [Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/NetWork_Kit/NetWorkKit_Datatransmission/HTTP_interceptor_C/entry/src/main/ets/pages/Index.ets#L16-L97)
6. 配置CMakeLists.txt，本模块需要用到的共享库是libhttp\_interceptor.so，在工程自动生成的CMakeLists.txt中的target\_link\_libraries中添加此共享库。

   注意：如图所示，在add\_library中的entry是工程自动生成的module name，若要做修改，需和步骤 3 中.nm\_modname保持一致。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/64/v3/v9bXf-dFStqtjFyvPXx5gg/zh-cn_image_0000002592378782.png?HW-CC-KV=V1&HW-CC-Date=20260611T064811Z&HW-CC-Expire=86400&HW-CC-Sign=9F9F588BD9EC062308BF6906B5F600F1ACF25C48621AF22C449CC928FC31A4CE)
7. 调用HTTP全局拦截器C API接口要求应用拥有ohos.permission.INTERNET权限，在module.json5中的requestPermissions项添加该权限。

完成上述步骤后，工程搭建已全部完成，后续可连接设备运行工程并查看日志。

## 测试步骤

1. 连接设备，使用DevEco Studio打开搭建好的工程。
2. 运行工程，设备上会弹出以下图片所示界面。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8d/v3/ymPYcX3AS-yqN3yisTvY_A/zh-cn_image_0000002622858289.png?HW-CC-KV=V1&HW-CC-Date=20260611T064811Z&HW-CC-Expire=86400&HW-CC-Sign=C97A4D9C8A20710EE4EE5DFAB5DFB9CDB286CCD24473AF22DFE6FE6E95A1CA95)

* 点击Add Response Interceptor按钮，添加一个HTTP全局只读响应拦截器。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d1/v3/DLgZ0YLhQMq2LzJks-Zy5A/zh-cn_image_0000002622698411.png?HW-CC-KV=V1&HW-CC-Date=20260611T064811Z&HW-CC-Expire=86400&HW-CC-Sign=2AF0BF6A490AB6A0D572F09AEC6F817F5AD0A338B9D6608FE8EC147F9E7BE9C9)

* 点击Start Interceptors按钮，启用组ID为1的所有拦截器。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/94/v3/o4F3-o3RSu6z2TLzHyVk2w/zh-cn_image_0000002592218850.png?HW-CC-KV=V1&HW-CC-Date=20260611T064811Z&HW-CC-Expire=86400&HW-CC-Sign=C091FBD6690C023C913E6A6F449FBBDA81AF4B5132D267A3A584082F43D66A36)

* 点击Send HTTP Request按钮，拦截器会捕获响应并打印相关信息到日志。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4a/v3/0TMF6LkETYOrsUFAvK7mDQ/zh-cn_image_0000002592378784.png?HW-CC-KV=V1&HW-CC-Date=20260611T064811Z&HW-CC-Expire=86400&HW-CC-Sign=B232E039FD1450A8ADD5AC00C3F9010CEC7472F5053C3B26A144268BE64AB537)

* 点击Stop Interceptors按钮，停用组ID为1的所有拦截器。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f3/v3/qog3jwqQSKmVdQuKZ1FQQg/zh-cn_image_0000002622858291.png?HW-CC-KV=V1&HW-CC-Date=20260611T064811Z&HW-CC-Expire=86400&HW-CC-Sign=F8DA3EA6FDFB4E850539DA4B15782CF9B34D71CCD52581F70B1E07DE05929BE7)

* 点击Remove Interceptor按钮，移除之前添加的拦截器。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2b/v3/GYMYu5-xRM6ZJIpldTD-hw/zh-cn_image_0000002622698413.png?HW-CC-KV=V1&HW-CC-Date=20260611T064811Z&HW-CC-Expire=86400&HW-CC-Sign=2F89E536BC8C4CED6D58EBB7E98983FA8A7109DA1E1CA8E936B4DBB3D448CDC6)

* 点击Remove All Interceptors按钮，删除组ID为1的所有拦截器。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/72/v3/Ve7PFhSiQSaNqP86QvuvGg/zh-cn_image_0000002592218852.png?HW-CC-KV=V1&HW-CC-Date=20260611T064811Z&HW-CC-Expire=86400&HW-CC-Sign=7EAE9F3DD51B0B55169592734491F60F79AE69EBEFB501B10381C6738205785E)
