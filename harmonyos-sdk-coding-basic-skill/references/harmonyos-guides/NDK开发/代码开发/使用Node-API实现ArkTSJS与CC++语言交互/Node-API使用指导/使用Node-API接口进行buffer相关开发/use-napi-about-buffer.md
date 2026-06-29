---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/use-napi-about-buffer
title: 使用Node-API接口进行buffer相关开发
breadcrumb: 指南 > NDK开发 > 代码开发 > 使用Node-API实现ArkTS/JS与C/C++语言交互 > Node-API使用指导 > 使用Node-API接口进行buffer相关开发
category: harmonyos-guides
scraped_at: 2026-06-01T15:15:09+08:00
doc_updated_at: 2026-05-28
content_hash: sha256:dd30b8a7ce7c46cca794b528285a27f8bd3f648e38dddbabd3c0f0dcab95f8a9
---
## 简介

在ArkTS中，Buffer是一种用于处理二进制数据的数据类型。

## 基本概念

使用Node-API接口进行buffer相关开发时，可以通过Buffer对象实现ArkTS代码与Node-API模块之间的二进制数据交互，包括创建、操作Buffer对象，以处理I/O、网络传输等场景中的二进制数据。

* **Buffer对象**：用于表示一段二进制数据的对象。
* **外部Buffer**：在Node-API模块中创建的Buffer，可以与现有的数据关联起来而不需要复制数据到新的Buffer中。

## 场景和功能使用

以下这些接口用于有效地与ArkTS层进行交互，这使Node-API模块能够更好地处理ArkTS层的二进制数据，比如处理文件I/O、网络传输等操作：

| 接口 | 描述 |
| --- | --- |
| napi\_create\_buffer | 用于创建并获取一个指定大小的ArkTS Buffer。 |
| napi\_create\_buffer\_copy | 用于创建并获取一个指定大小的ArkTS Buffer，并以给定的入参数据对buffer的缓冲区进行初始化。 |
| napi\_create\_external\_buffer | 用于创建并获取一个指定大小的ArkTS Buffer，并以给定数据进行初始化，该接口可为Buffer附带额外数据。 |
| napi\_get\_buffer\_info | 获取ArkTS Buffer底层数据缓冲区及其长度。 |
| napi\_is\_buffer | 判断给定ArkTS value是否为Buffer对象。 |
| napi\_create\_external\_arraybuffer | 用于分配一个附加有外部数据的ArkTS ArrayBuffer。外部ArrayBuffer是一个特殊类型的ArrayBuffer，它持有对外部数据的引用而不实际拥有数据存储。 |

## 使用示例

Node-API接口开发流程参考[使用Node-API实现跨语言交互开发流程](../../使用Node-API实现跨语言交互开发流程/use-napi-process.md)，本文仅对接口对应C++及ArkTS相关代码进行展示。

### napi\_create\_buffer

此接口用于创建Buffer对象。Buffer对象是用于在Node-API模块中操作二进制数据的一种特殊类型。

cpp部分代码

```
1. // napi_create_buffer
2. static napi_value CreateBuffer(napi_env env, napi_callback_info info)
3. {
4. std::string str("CreateBuffer");
5. void *bufferPtr = nullptr;
6. size_t bufferSize = str.size();
7. napi_value buffer = nullptr;
8. // 调用napi_create_buffer接口创建并获取一个指定大小的ArkTS Buffer
9. napi_status status = napi_create_buffer(env, bufferSize + 1, &bufferPtr, &buffer);
10. if (status != napi_ok) {
11. OH_LOG_ERROR(LOG_APP, "napi_create_buffer failed");
12. return nullptr;
13. }
14. // 将字符串str的值复制到buffer的内存中
15. strcpy((char *)bufferPtr, str.data());
16. return buffer;
17. }
```

[napi\_init.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkTS/NodeAPI/NodeAPIUse/NodeAPIBuffer/entry/src/main/cpp/napi_init.cpp#L22-L40)

接口声明

```
1. export const createBuffer: () => string; // napi_create_buffer
```

[Index.d.ts](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkTS/NodeAPI/NodeAPIUse/NodeAPIBuffer/entry/src/main/cpp/types/libentry/Index.d.ts#L16-L18)

ArkTS侧示例代码

```
1. // napi_create_buffer
2. try {
3. hilog.info(0x0000, 'testTag', 'Test Node-API napi_create_buffer: %{public}s',
4. testNapi.createBuffer().toString());
5. // ...
6. } catch (error) {
7. hilog.error(0x0000, 'testTag', 'Test Node-API napi_create_buffer error');
8. // ...
9. }
```

[Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkTS/NodeAPI/NodeAPIUse/NodeAPIBuffer/entry/src/main/ets/pages/Index.ets#L54-L68)

### napi\_create\_buffer\_copy

本接口是Node-API中用于创建并复制数据到Buffer对象的函数。它可以在Node-API模块中创建一个新的Buffer对象，并将指定的数据复制到该Buffer对象中。

cpp部分代码

```
1. // napi_create_buffer_copy
2. static napi_value CreateBufferCopy(napi_env env, napi_callback_info info)
3. {
4. // 要copy的内容
5. char str[] = "CreateBufferCopy";
6. napi_value buffer = nullptr;
7. // 调用napi_create_buffer_copy接口创建buffer并将str的内容copy到buffer
8. void* resultData = nullptr;
9. napi_status status = napi_create_buffer_copy(env, sizeof(str), str, &resultData, &buffer);
10. if (status != napi_ok) {
11. OH_LOG_ERROR(LOG_APP, "napi_create_buffer_copy failed");
12. return nullptr;
13. }
14. if (resultData != nullptr) {
15. OH_LOG_INFO(LOG_APP, "Node-API resultData is : %{public}s.", reinterpret_cast <const char*>(resultData));
16. } else {
17. OH_LOG_INFO(LOG_APP, "Node-API resultData is nullptr.");
18. }
19. return buffer;
20. }
```

[napi\_init.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkTS/NodeAPI/NodeAPIUse/NodeAPIBuffer/entry/src/main/cpp/napi_init.cpp#L42-L63)

接口声明

```
1. export const createBufferCopy: () => string; // napi_create_buffer_copy
```

[Index.d.ts](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkTS/NodeAPI/NodeAPIUse/NodeAPIBuffer/entry/src/main/cpp/types/libentry/Index.d.ts#L20-L22)

ArkTS侧示例代码

```
1. // napi_create_buffer_copy
2. try {
3. hilog.info(0x0000, 'testTag', 'Test Node-API napi_create_buffer_copy: %{public}s',
4. testNapi.createBufferCopy().toString());
5. // ...
6. } catch (error) {
7. hilog.error(0x0000, 'testTag', 'Test Node-API napi_create_buffer_copy error');
8. // ...
9. }
```

[Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkTS/NodeAPI/NodeAPIUse/NodeAPIBuffer/entry/src/main/ets/pages/Index.ets#L70-L84)

### napi\_create\_external\_buffer

当希望在ArkTS中使用现有的Node-API模块内存块，而不需要额外的拷贝时，可以使用napi\_create\_external\_buffer。这将允许ArkTS层直接访问并操作该内存，避免额外的内存分配和拷贝操作。

cpp部分代码

```
1. // 回调函数，用于释放内存
2. void FinalizeCallback(napi_env env, void *data, void *hint)
3. {
4. if (data == nullptr) {
5. return;
6. }
7. free(data);
8. data = nullptr;
9. }

11. // napi_create_external_buffer
12. static napi_value CreateExternalBuffer(napi_env env, napi_callback_info info)
13. {
14. // 创建一个字符串
15. std::string str("CreateExternalBuffer");
16. // 在堆上分配内存，大小为字符串的长度
17. void* data = malloc(str.size() + 1);
18. if (data == nullptr) {
19. OH_LOG_ERROR(LOG_APP, "malloc failed");
20. return nullptr;
21. }
22. memset(data, 0, str.size() + 1);
23. // 将字符串复制到分配的内存中
24. strcpy(static_cast<char *>(data), str.data());
25. // 使用napi_create_external_buffer接口创建并获取一个指定大小buffer
26. napi_value buffer = nullptr;
27. napi_status status = napi_create_external_buffer(env, str.size(), data, FinalizeCallback, nullptr, &buffer);
28. if (status != napi_ok) {
29. free(data);
30. OH_LOG_ERROR(LOG_APP, "napi_create_external_buffer failed");
31. return nullptr;
32. }
33. return buffer;
34. }
```

[napi\_init.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkTS/NodeAPI/NodeAPIUse/NodeAPIBuffer/entry/src/main/cpp/napi_init.cpp#L65-L100)

接口声明

```
1. export const createExternalBuffer: () => string; // napi_create_external_buffer
```

[Index.d.ts](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkTS/NodeAPI/NodeAPIUse/NodeAPIBuffer/entry/src/main/cpp/types/libentry/Index.d.ts#L24-L26)

ArkTS侧示例代码

```
1. // napi_create_external_buffer
2. try {
3. hilog.info(0x0000, 'testTag', 'Test Node-API napi_create_external_buffer: %{public}s',
4. testNapi.createExternalBuffer()
5. .toString());
6. // ...
7. } catch (error) {
8. hilog.error(0x0000, 'testTag', 'Test Node-API napi_create_external_buffer error');
9. // ...
10. }
```

[Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkTS/NodeAPI/NodeAPIUse/NodeAPIBuffer/entry/src/main/ets/pages/Index.ets#L86-L101)

### napi\_get\_buffer\_info

在ArkTS中需要对Buffer对象中的数据执行特定的操作时，可以使用此接口来获取指向数据的指针和数据长度。这样可以在Node-API模块直接对数据进行操作，而无需进行数据的拷贝。

cpp部分代码

```
1. // napi_get_buffer_info
2. static napi_value GetBufferInfo(napi_env env, napi_callback_info info)
3. {
4. // 创建一个字符串
5. std::string str("GetBufferInfo");
6. napi_value buffer = nullptr;
7. void *bufferPtr = nullptr;
8. size_t bufferSize = str.size();
9. napi_status status = napi_create_buffer(env, bufferSize + 1, &bufferPtr, &buffer);
10. if (status != napi_ok) {
11. OH_LOG_ERROR(LOG_APP, "napi_create_buffer failed");
12. return nullptr;
13. }
14. strcpy((char *)bufferPtr, str.data());

16. // 获取Buffer的信息
17. void *tmpBufferPtr = nullptr;
18. size_t bufferLength = 0;
19. napi_get_buffer_info(env, buffer, &tmpBufferPtr, &bufferLength);

21. // 创建一个新的ArkTS字符串来保存Buffer的内容并返出去
22. if (bufferLength == 0 || ((char*)tmpBufferPtr)[bufferLength - 1] != '\0') {
23. OH_LOG_ERROR(LOG_APP, "Buffer is not null-terminated");
24. return nullptr;
25. }
26. napi_value returnValue = nullptr;
27. napi_create_string_utf8(env, (char*)tmpBufferPtr, bufferLength, &returnValue);
28. return returnValue;
29. }
```

[napi\_init.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkTS/NodeAPI/NodeAPIUse/NodeAPIBuffer/entry/src/main/cpp/napi_init.cpp#L102-L132)

接口声明

```
1. export const getBufferInfo: () => string; // napi_get_buffer_info
```

[Index.d.ts](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkTS/NodeAPI/NodeAPIUse/NodeAPIBuffer/entry/src/main/cpp/types/libentry/Index.d.ts#L28-L30)

ArkTS侧示例代码

```
1. // napi_get_buffer_info
2. try {
3. hilog.info(0x0000, 'testTag', 'Test Node-API napi_get_buffer_info: %{public}s',
4. testNapi.getBufferInfo().toString());
5. // ...
6. } catch (error) {
7. hilog.error(0x0000, 'testTag', 'Test Node-API napi_get_buffer_info error');
8. // ...
9. }
```

[Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkTS/NodeAPI/NodeAPIUse/NodeAPIBuffer/entry/src/main/ets/pages/Index.ets#L103-L117)

### napi\_is\_buffer

判断给定ArkTS value是否为Buffer对象。

cpp部分代码

```
1. // napi_is_buffer
2. static napi_value IsBuffer(napi_env env, napi_callback_info info)
3. {
4. // 创建一个Buffer对象
5. std::string str = "buffer";
6. napi_value buffer = nullptr;
7. void *bufferPtr = nullptr;
8. napi_create_buffer(env, str.size(), &bufferPtr, &buffer);

10. // 调用napi_is_buffer接口判断创建的对象是否为buffer
11. bool result = false;
12. napi_is_buffer(env, buffer, &result);
13. // 将结果返回出去
14. napi_value returnValue = nullptr;
15. napi_get_boolean(env, result, &returnValue);
16. return returnValue;
17. }
```

[napi\_init.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkTS/NodeAPI/NodeAPIUse/NodeAPIBuffer/entry/src/main/cpp/napi_init.cpp#L134-L152)

接口声明

```
1. export const isBuffer: () => boolean; // napi_is_buffer
```

[Index.d.ts](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkTS/NodeAPI/NodeAPIUse/NodeAPIBuffer/entry/src/main/cpp/types/libentry/Index.d.ts#L32-L34)

ArkTS侧示例代码

```
1. // napi_is_buffer
2. try {
3. hilog.info(0x0000, 'testTag', 'Test Node-API napi_is_buffer: %{public}s',
4. JSON.stringify(testNapi.isBuffer()));
5. // ...
6. } catch (error) {
7. hilog.info(0x0000, 'testTag', 'Test Node-API napi_is_buffer error');
8. // ...
9. }
```

[Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkTS/NodeAPI/NodeAPIUse/NodeAPIBuffer/entry/src/main/ets/pages/Index.ets#L119-L133)

### napi\_create\_external\_arraybuffer

分配一个附加有外部数据的ArkTS ArrayBuffer。

cpp部分代码

```
1. static constexpr int INT_ARG_5 = 5; // 入参索引

3. typedef struct {
4. uint8_t *data;
5. size_t length;
6. } BufferData;

8. void FinalizeCallback1(napi_env env, void *finalizeData, void *finalizeHint)
9. {
10. // 获取终结时的数据
11. BufferData *bufferData = static_cast<BufferData *>(finalizeHint);

13. // 执行清理操作，比如释放资源
14. delete[] bufferData->data;
15. delete bufferData;
16. }

18. // napi_create_external_arraybuffer
19. napi_value CreateExternalArraybuffer(napi_env env, napi_callback_info info)
20. {
21. // 创建一个有五个元素的C++数组
22. uint8_t *dataArray = new uint8_t[5]{1, 2, 3, 4, 5};
23. napi_value externalBuffer = nullptr;
24. BufferData *bufferData = new BufferData{dataArray, 5};

26. // 使用napi_create_external_arraybuffer创建一个外部Array Buffer对象，并指定终结回调函数
27. napi_status status =
28. napi_create_external_arraybuffer(env, dataArray, INT_ARG_5, FinalizeCallback1, bufferData, &externalBuffer);
29. if (status != napi_ok) {
30. // 处理错误
31. delete[] dataArray;
32. delete bufferData;
33. napi_throw_error(env, nullptr, "Node-API napi_create_external_arraybuffer fail");
34. return nullptr;
35. }
36. napi_value outputArray;
37. // 使用napi_create_typedarray创建一个Array对象，并将externalBuffer对象作为参数传入
38. status = napi_create_typedarray(env, napi_int8_array, INT_ARG_5, externalBuffer, 0, &outputArray);
39. if (status != napi_ok) {
40. // 处理错误
41. napi_throw_error(env, nullptr, "Node-API napi_create_typedarray fail");
42. return nullptr;
43. }
44. return outputArray;
45. }
```

[napi\_init.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkTS/NodeAPI/NodeAPIUse/NodeAPIBuffer/entry/src/main/cpp/napi_init.cpp#L154-L198)

接口声明

```
1. export const createExternalArraybuffer: () => ArrayBuffer | undefined; // napi_create_external_arraybuffer
```

[Index.d.ts](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkTS/NodeAPI/NodeAPIUse/NodeAPIBuffer/entry/src/main/cpp/types/libentry/Index.d.ts#L36-L38)

ArkTS侧示例代码

```
1. // napi_create_external_arraybuffer
2. hilog.info(0x0000, 'testTag', 'Node-API createExternalArraybuffer: %{public}s',
3. JSON.stringify(testNapi.createExternalArraybuffer()));
```

[Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkTS/NodeAPI/NodeAPIUse/NodeAPIBuffer/entry/src/main/ets/pages/Index.ets#L135-L139)

以上代码如果要在native cpp中打印日志，需在CMakeLists.txt文件中添加以下配置信息（并添加头文件：#include "hilog/log.h"）：

```
1. // CMakeLists.txt
2. add_definitions( "-DLOG_DOMAIN=0xd0d0" )
3. add_definitions( "-DLOG_TAG=\"testTag\"" )
4. target_link_libraries(entry PUBLIC libace_napi.z.so libhilog_ndk.z.so)
```
