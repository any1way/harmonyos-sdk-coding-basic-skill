---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/remote-communication-pre-connect
title: 通过预建连接提升HTTP传输性能
breadcrumb: 指南 > 系统 > 网络 > Remote Communication Kit（远场通信服务） > 提升HTTP传输性能 > 通过预建连接提升HTTP传输性能
category: harmonyos-guides
scraped_at: 2026-06-01T11:21:17+08:00
doc_updated_at: 2026-04-30
content_hash: sha256:95d2d7a29f1fd41f416478fcfe60607a579fec57368ca2d6eea389e56db04fd5
---
## 概述

从6.1.1(24)版本开始，新增支持预建连接功能。

发起一次HTTP/HTTPS请求一般需要先和目标服务器完成TCP握手和TLS握手（仅HTTPS）。后续请求如果能够复用已完成握手的连接，则可以直接收发数据，从而节省握手的耗时。Remote Communication Kit支持HTTP预建连接的能力。应用可以发起一次不进行数据传输的请求，使后续请求不再需要建立连接。

需要满足以下条件才能复用连接：

* 使用同一个session
* 访问同一个域名
* 网络状态未改变（未发生切换网络、网络关闭等情况）

## 约束与限制

通过预建连接提升HTTP传输性能，支持Phone、PC/2in1、Tablet、Wearable和TV设备。

## 使用预建连接能力（ArkTS）

```
1. import { rcp } from '@kit.RemoteCommunicationKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. export async function startConnectionOnlyByRequest() {
5. const session = rcp.createSession();
6. const request = new rcp.Request('https://example.com', 'GET');
7. request.connectOnly = true;

9. const response = await session.fetch(request);
10. console.info(`Request succeeded, statusCode is ${response.statusCode}`);

12. // 此session可用于发起后续请求
13. }
```

注意

当[Request](<../../../../../../harmonyos-references/网络/Remote Communication Kit（远场通信服务）/ArkTS API/rcp（数据请求）/remote-communication-rcp.md#request>)的connectOnly属性被设置为true时，即使已有连接，此请求也一定会建立一条新的连接。

## 使用预建连接能力（C++）

```
1. #include "RemoteCommunicationKit/rcp.h"
2. #include <stdio.h>
3. #include <thread>

5. void DataRequestCallback(void *userContext, Rcp_Response *response, uint32_t errCode) {
6. printf("DataRequest callback, errCode: %u\n", errCode);
7. if (response != nullptr) {
8. printf("Data request succeeded, status code: %d\n", response->statusCode);
9. response->destroyResponse(response);
10. }
11. }

13. void dataTransRequest() {
14. uint32_t errCode = 0;
15. // 创建session
16. Rcp_Session *session = HMS_Rcp_CreateSession(nullptr, &errCode);
17. printf("create session end: %d\n", errCode);
18. const char *kHttpServerAddress = "https://example.com";
19. Rcp_Request *dataRequest = HMS_Rcp_CreateRequest(kHttpServerAddress);
20. dataRequest->method = RCP_METHOD_GET;

22. // 设置本次请求仅建立连接。
23. errCode = HMS_Rcp_SetRequestConnectOnly(dataRequest, true);

25. Rcp_ResponseCallbackObject callback = {DataRequestCallback, nullptr};

27. errCode = HMS_Rcp_Fetch(session, dataRequest, &callback);
28. printf("session fetch end: %d\n", errCode);

30. // 等待结果，仅是等待异步调用完成，开发者可根据自己实际场景处理回调。
31. std::this_thread::sleep_for(std::chrono::milliseconds(1000 * 1000 * 3));

33. // 请求完成后，清理request
34. HMS_Rcp_DestroyRequest(dataRequest);

36. // 此session在被close前可用于发起后续请求
37. errCode = HMS_Rcp_CloseSession(&session);
38. printf("HMS_Rcp_CloseSession end errCode: %d\n", errCode);
39. }
```

注意

请求被设置为仅建立连接后，即使已有连接，此请求也一定会建立一条新的连接。

只有通过[HMS\_Rcp\_Fetch](<../../../../../../harmonyos-references/网络/Remote Communication Kit（远场通信服务）/C API/模块/RemoteCommunication/remote-communication-overview.md#hms_rcp_fetch>)接口发起的请求可以复用已有的连接；通过[HMS\_Rcp\_FetchSync](<../../../../../../harmonyos-references/网络/Remote Communication Kit（远场通信服务）/C API/模块/RemoteCommunication/remote-communication-overview.md#hms_rcp_fetchsync>)接口发起的请求不支持连接复用。

## 通过DefaultSession使用连接复用能力

不同的session之间不支持连接复用。可以通过默认session在同一个session上方便地发起请求。通过[getDefaultSession](<../../../../../../harmonyos-references/网络/Remote Communication Kit（远场通信服务）/ArkTS API/rcp（数据请求）/remote-communication-rcp.md#getdefaultsession>)（ArkTS）和[HMS\_Rcp\_GetDefaultSession](<../../../../../../harmonyos-references/网络/Remote Communication Kit（远场通信服务）/C API/模块/RemoteCommunication/remote-communication-overview.md#hms_rcp_getdefaultsession>)（C API）获得的默认session在系统内实际上是同一个session。

**ArkTS：**

```
1. import { rcp } from '@kit.RemoteCommunicationKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. export async function startConnectionOnlyByRequest() {
5. const defaultSession = rcp.getDefaultSession();
6. const request = new rcp.Request('https://example.com', 'GET');
7. request.connectOnly = true;

9. const response = await defaultSession.fetch(request);
10. console.info(`Request succeeded, statusCode is ${response.statusCode}`);

12. // 可以在默认session上发起后续请求
13. }
```

**C++：**

```
1. #include <stdio.h>
2. #include <thread>
3. #include "RemoteCommunicationKit/rcp.h"

5. Rcp_Session *defaultSession = nullptr;

7. void DataRequestCallback(void *userContext, Rcp_Response *response, uint32_t errCode) {
8. printf("DataRequest callback, errCode: %u\n", errCode);
9. if (response != nullptr) {
10. printf("Data request succeeded, status code: %d\n", response->statusCode);
11. response->destroyResponse(response);
12. }
13. }

15. void dataTransRequest() {
16. uint32_t errCode = 0;
17. // 获得默认session
18. errCode = HMS_Rcp_GetDefaultSession(&defaultSession);

20. printf("create session end: %d\n", errCode);
21. const char *kHttpServerAddress = "https://example.com";
22. Rcp_Request *dataRequest = HMS_Rcp_CreateRequest(kHttpServerAddress);
23. dataRequest->method = RCP_METHOD_GET;

25. Rcp_ResponseCallbackObject callback = {DataRequestCallback, nullptr};
26. errCode = HMS_Rcp_Fetch(defaultSession, dataRequest, &callback);
27. printf("defaultSession fetch end: %d\n", errCode);
28. // 等待结果，仅是等待异步调用完成，开发者可根据自己实际场景处理回调。
29. std::this_thread::sleep_for(std::chrono::milliseconds(1000 * 1000 * 3));
30. // 清理request
31. HMS_Rcp_DestroyRequest(dataRequest);

33. // 可以在默认session上发起后续请求

35. // 当不再需要默认session时，使用HMS_Rcp_CloseSession释放对默认session的强引用
36. errCode = HMS_Rcp_CloseSession(&defaultSession);
37. printf("HMS_Rcp_CloseSession end errCode: %d\n", errCode);
38. }
```

注意

系统内会自动维护一个默认session。应用的默认session会持有对系统内默认session的引用。当应用所有的默认session被回收后，系统内默认session将被关闭。

当应用再次获取默认session时，系统内会创建一个新的默认session。新创建的默认session无法复用之前的连接。如果需要默认session长期保持连接，应用应长期持有至少一个默认session对象。
