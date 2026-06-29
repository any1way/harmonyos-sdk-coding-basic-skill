---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/content-embed-client-guidelines
title: 客户端应用开发
breadcrumb: 指南 > 应用框架 > Content Embed Kit（内容嵌入服务） > 客户端应用开发
category: harmonyos-guides
scraped_at: 2026-06-01T11:10:32+08:00
doc_updated_at: 2026-04-30
content_hash: sha256:17f3198d0a4f79955e67079bb4de005d0c236febc7e4dd44a4a368c9e140d98b
---
## 场景介绍

[OH\_ContentEmbed](<../../../../harmonyos-references/Content Embed Kit（内容嵌入服务）/C API/模块/ContentEmbed/capi-contentembed.md>)内容嵌入模块提供对象编辑框架与技术，支持应用间文档嵌入与协同编辑。

OE客户端应用指嵌入其它文档的应用，通过调用[OE框架层接口](<../../../../harmonyos-references/Content Embed Kit（内容嵌入服务）/C API/头文件/content_embed_proxy.h/capi-content-embed-proxy-h.md>)实现嵌入外部文档、展示文档快照，以及按需启动OE服务端应用编辑文档的功能。

典型应用场景包括：

* 在CAD文档中嵌入Excel表格，通过点击嵌入对象启动Excel应用进行编辑。
* 在文档编辑器中嵌入图片、表格等多种格式的文档。
* 在笔记应用中嵌入其他应用的文档，实现跨应用协作。

## 约束限制

在使用接口前，需先确认设备具备SystemCapability.ContentEmbed.ObjectEditor系统能力，判断方式请参阅[查询指定的系统能力是否被支持](<../../../../harmonyos-references/C API/模块/Init/init.md#caniuse>)。并申请ohos.permission.CONNECT\_OBJECTEDITOR\_EXTENSION权限，配置方式请参阅[声明权限](../../../系统/安全/程序访问控制/应用权限管控/申请应用权限/声明权限/declare-permissions.md)。

## 接口说明

常用接口如下表所示。更多API说明请参考[OH\_ContentEmbed](<../../../../harmonyos-references/Content Embed Kit（内容嵌入服务）/C API/模块/ContentEmbed/capi-contentembed.md>)。

**表1** 客户端主要接口

| 接口名称 | 功能描述 |
| --- | --- |
| OH\_ContentEmbed\_CreateDocumentByFile | 通过被嵌入文档路径创建[OE文档](<../Content Embed Kit术语/content-embed-kit-terminology.md#oe文档>)。 |
| OH\_ContentEmbed\_CreateDocumentByOEId | 通过[OEID](<../Content Embed Kit术语/content-embed-kit-terminology.md#oeid>)创建OE文档。 |
| OH\_ContentEmbed\_LoadDocumentFromFile | 通过已存在的[OE格式文件](<../Content Embed Kit术语/content-embed-kit-terminology.md#oe格式文件>)加载OE文档。 |
| OH\_ContentEmbed\_CreateExtensionProxy | 创建[客户端OE对象](<../Content Embed Kit术语/content-embed-kit-terminology.md#客户端oe对象>)。 |
| OH\_ContentEmbed\_DestroyExtensionProxy | 销毁客户端OE对象，释放相关资源。 |
| OH\_ContentEmbed\_Proxy\_RegisterOnUpdateFunc | 向客户端OE对象注册OE文档更新时的回调函数。 |
| OH\_ContentEmbed\_Proxy\_RegisterOnErrorFunc | 向客户端OE对象注册OE文档触发错误时的回调函数。 |
| OH\_ContentEmbed\_Proxy\_RegisterOnEditingFinishedFunc | 向客户端OE对象注册OE文档编辑完成时的回调函数。 |
| OH\_ContentEmbed\_Proxy\_RegisterOnExtensionStoppedFunc | 向客户端OE对象注册[OE Extension](<../Content Embed Kit术语/content-embed-kit-terminology.md#oe-extension>)停止时的回调函数。 |
| OH\_ContentEmbed\_Proxy\_StartWork | 客户端通过客户端OE对象与Object Editor服务跨进程通信，启动OE Extension组件，并创建服务端OE对象。 |
| OH\_ContentEmbed\_Proxy\_StopWork | 客户端通过客户端OE对象与Object Editor服务跨进程通信，销毁服务端OE对象，释放资源。 |
| OH\_ContentEmbed\_Proxy\_GetSnapshot | 从客户端OE对象获取当前OE文档的快照图像，用于预览或缩略图显示。 |
| OH\_ContentEmbed\_Proxy\_DoEdit | 客户端通过客户端OE对象与OE Extension组件跨进程通信，通知服务端启动UIAbility编辑OE文档。 |
| OH\_ContentEmbed\_Proxy\_GetDocument | 从客户端OE对象获取其关联的OE文档对象。 |
| OH\_ContentEmbed\_Document\_Read | 从OE文档中读取OE格式文件数据，存入buffer。 |
| OH\_ContentEmbed\_DestroyDocument | 销毁OE文档对象，释放资源。 |

## 开发步骤

以下演示使用Native API开发OE客户端应用的完整流程。

### 添加动态链接库

CMakeLists.txt中添加以下lib。

```
1. # content embed
2. libcontent_embed_ndk.so
3. # hilog
4. libhilog_ndk.z.so
5. # ace
6. libace_napi.z.so
7. # piexlmap
8. libpixelmap.so
```

### 引用头文件

```
1. #include <string>
2. #include <ContentEmbedKit/content_embed/content_embed_common.h>
3. #include <ContentEmbedKit/content_embed/content_embed_document.h>
4. #include <ContentEmbedKit/content_embed/content_embed_proxy.h>
5. #include <hilog/log.h>
6. #include <multimedia/image_framework/image/pixelmap_native.h>
```

### 查询当前设备支持的可嵌入文档信息

查询当前设备在指定语言下支持的所有可嵌入文档的信息。

```
1. void QueryAllFormat(const std::string &locale)
2. {
3. ContentEmbed_Info* contentEmbedInfo = nullptr;
4. // 创建ContentEmbedInfo
5. ContentEmbed_ErrorCode errCode = OH_ContentEmbed_CreateContentEmbedInfo(&contentEmbedInfo);
6. if (errCode != CE_ERR_OK) {
7. OH_LOG_ERROR(LOG_APP, "OH_ContentEmbed_CreateContentEmbedInfo failed, errCode: %{public}d.", errCode);
8. return;
9. }
10. // 获取locale语言的ContentEmbedInfo信息
11. errCode = OH_ContentEmbed_GetContentEmbedInfo(locale.c_str(), contentEmbedInfo);
12. if (errCode != CE_ERR_OK) {
13. OH_LOG_ERROR(LOG_APP, "OH_ContentEmbed_GetContentEmbedInfo failed, errCode: %{public}d.", errCode);
14. // 查询失败销毁ContentEmbedInfo对象
15. OH_ContentEmbed_DestroyContentEmbedInfo(contentEmbedInfo);
16. return;
17. }
18. uint32_t count = 0;
19. // 获取ContentEmbedInfo对象Format对象数量
20. errCode = OH_ContentEmbed_GetFormatCountFromInfo(contentEmbedInfo, &count);
21. if (errCode != CE_ERR_OK) {
22. OH_LOG_ERROR(LOG_APP, "OH_ContentEmbed_GetFormatCountFromInfo failed, errCode: %{public}d.", errCode);
23. // 查询失败销毁ContentEmbedInfo对象
24. OH_ContentEmbed_DestroyContentEmbedInfo(contentEmbedInfo);
25. return;
26. }
27. for (int i = 0; i < count; i++) {
28. ContentEmbed_Format* ceFormat = nullptr;
29. // 从ContentEmbedInfo对象获取索引为i的ContentEmbed_Format信息
30. errCode = OH_ContentEmbed_GetFormatFromInfo(contentEmbedInfo, i, &ceFormat);
31. if (errCode != CE_ERR_OK) {
32. OH_LOG_ERROR(LOG_APP, "OH_ContentEmbed_GetFormatFromInfo failed, errCode: %{public}d.", errCode);
33. continue;
34. }
35. char oeid[MAX_OEID_LENGTH];
36. // 获取OEID
37. errCode = OH_ContentEmbed_GetOEidFromFormat(ceFormat, oeid);
38. if (errCode != CE_ERR_OK) {
39. OH_LOG_ERROR(LOG_APP, "OH_ContentEmbed_GetOEidFromFormat failed, errCode: %{public}d.", errCode);
40. continue;
41. }
42. char name[MAX_NAME_LENGTH];
43. char description[MAX_DESCRIPTION_LENGTH];
44. // 获取名称和描述
45. errCode = OH_ContentEmbed_GetNameAndDescriptionFromFormat(ceFormat, name, description);
46. if (errCode != CE_ERR_OK) {
47. OH_LOG_ERROR(LOG_APP, "OH_ContentEmbed_GetNameAndDescriptionFromFormat failed, errCode: %{public}d.", errCode);
48. continue;
49. }
50. OH_PixelmapNative* pixelMap = nullptr;
51. // 获取图标
52. errCode = OH_ContentEmbed_GetIconFromFormat(ceFormat, &pixelMap);
53. if (errCode != CE_ERR_OK) {
54. OH_LOG_ERROR(LOG_APP, "OH_ContentEmbed_GetIconFromFormat failed, errCode: %{public}d.", errCode);
55. continue;
56. }
57. unsigned int count = 0;
58. // 获取文件后缀
59. char **fileNameExtensions = OH_ContentEmbed_GetFileNameExtensionsFromFormat(ceFormat, &count);
60. if (fileNameExtensions == nullptr) {
61. OH_LOG_ERROR(LOG_APP, "OH_ContentEmbed_GetFileNameExtensionsFromFormat failed");
62. continue;
63. }
64. }
65. // 销毁ContentEmbedInfo对象
66. OH_ContentEmbed_DestroyContentEmbedInfo(contentEmbedInfo);
67. }
```

### 查询OEID对应的格式信息

```
1. void QueryFormatByOEid(const std::string &oeid, const std::string &locale)
2. {
3. ContentEmbed_Format* ceFormat = nullptr;
4. // 创建ContentEmbed_Format
5. ContentEmbed_ErrorCode errCode = OH_ContentEmbed_CreateContentEmbedFormat(&ceFormat);
6. if (errCode != CE_ERR_OK) {
7. OH_LOG_ERROR(LOG_APP, "OH_ContentEmbed_CreateContentEmbedFormat failed, errCode: %{public}d.", errCode);
8. return;
9. }
10. errCode = OH_ContentEmbed_GetContentEmbedFormatByOEidAndLocale(oeid.c_str(), locale.c_str(), ceFormat);
11. if (errCode != CE_ERR_OK) {
12. OH_LOG_ERROR(LOG_APP, "OH_ContentEmbed_GetContentEmbedFormatByOEidAndLocale failed, errCode: %{public}d.", errCode);
13. // 查询失败销毁ContentEmbed_Format对象
14. OH_ContentEmbed_DestroyContentEmbedFormat(ceFormat);
15. }
16. char name[MAX_NAME_LENGTH];
17. char description[MAX_DESCRIPTION_LENGTH];
18. // 获取名称和描述
19. errCode = OH_ContentEmbed_GetNameAndDescriptionFromFormat(ceFormat, name, description);
20. if (errCode != CE_ERR_OK) {
21. OH_LOG_ERROR(LOG_APP, "OH_ContentEmbed_GetNameAndDescriptionFromFormat failed, errCode: %{public}d.", errCode);
22. return;
23. }
24. OH_PixelmapNative* pixelMap = nullptr;
25. // 获取图标
26. errCode = OH_ContentEmbed_GetIconFromFormat(ceFormat, &pixelMap);
27. if (errCode != CE_ERR_OK) {
28. OH_LOG_ERROR(LOG_APP, "OH_ContentEmbed_GetIconFromFormat failed, errCode: %{public}d.", errCode);
29. return;
30. }
31. unsigned int count = 0;
32. // 获取文件后缀
33. char **fileNameExtensions = OH_ContentEmbed_GetFileNameExtensionsFromFormat(ceFormat, &count);
34. if (fileNameExtensions == nullptr) {
35. OH_LOG_ERROR(LOG_APP, "OH_ContentEmbed_GetFileNameExtensionsFromFormat failed");
36. return;
37. }
38. }
```

### 创建OE文档

1. 基于OEID创建OE文档

   ```
   1. void CreateDocumentByOEid(const std::string &oeid)
   2. {
   3. ContentEmbed_Document* ceDocument = nullptr;
   4. // 基于OEID创建OE文件
   5. ContentEmbed_ErrorCode errCode = OH_ContentEmbed_CreateDocumentByOEid(oeid.c_str(), &ceDocument);
   6. }
   ```
2. 基于文件创建OE文档

   ```
   1. void CreateDocumentByFile(std::string filePath)
   2. {
   3. // 基于文件创建OE文档
   4. ContentEmbed_Document *ceDocument = nullptr;
   5. // 是否以链接形式创建OE文档，当isLinking为true时，表示以链接方式创建OE文档；当isLinking为false时，表示以嵌入方式创建OE文档。
   6. bool isLinking = false;
   7. ContentEmbed_ErrorCode ret = OH_ContentEmbed_CreateDocumentByFile(filePath.c_str(), filePath.size(), isLinking, &ceDocument);
   8. }
   ```
3. 基于[OE格式文件](<../Content Embed Kit术语/content-embed-kit-terminology.md#oe格式文件>)加载OE文档，当OE格式文件为数据流存储时需先落盘至本地再使用此接口。

   ```
   1. void LoadDocumentFromFile(std::string oeFormatFilePath)
   2. {
   3. ContentEmbed_Document *ceDocument = nullptr;
   4. // 基于OE格式文件
   5. ContentEmbed_ErrorCode ret = OH_ContentEmbed_LoadDocumentFromFile(oeFormatFilePath.c_str(), oeFormatFilePath.size(), &ceDocument);
   6. }
   ```

### 创建客户端OE对象

基于OE文档和当前上下文实例创建客户端OE对象，实现OE文档与客户端OE对象的关联，并用于与服务端通信。

```
1. void ClientCallBack_OnUpdateFunc(ContentEmbed_ExtensionProxy *proxy)
2. {
3. OH_LOG_INFO(LOG_APP, "Enter ClientCallBack_OnUpdateFunc");
4. // 将OE文档数据写入客户端应用文档
5. ContentEmbed_Document *document = nullptr;
6. ContentEmbed_ErrorCode errCode = OH_ContentEmbed_Proxy_GetDocument(proxy, &document);
7. if (errCode != CE_ERR_OK) {
8. OH_LOG_ERROR(LOG_APP, "OH_ContentEmbed_Proxy_GetDocument failed, errCode: %{public}d.", errCode);
9. return;
10. }
11. bool isLinking = false;
12. ContentEmbed_ErrorCode ret = OH_ContentEmbed_Document_IsLinking(document, &isLinking);
13. OH_LOG_INFO(LOG_APP, "ret: %{public}d, isLinking: %{public}d", ret, isLinking);
14. if (ret == CE_ERR_OK && isLinking) {
15. OH_LOG_INFO(LOG_APP, "linking document, No need to save to the sandbox");
16. return;
17. }
18. const size_t CHUNK_SIZE = 4096; // 分块大小
19. uint8_t *buffer = new (std::nothrow) uint8_t[CHUNK_SIZE + 1];
20. if (!buffer)
21. return;
22. size_t offset = 0;
23. size_t actualRead = 0;
24. do {
25. // 读取OE文档内容
26. ret = OH_ContentEmbed_Document_Read(buffer, CHUNK_SIZE, document, offset, &actualRead);

28. if (ret != CE_ERR_OK || actualRead == 0)
29. break;

31. // 自行处理buffer数据流
32. // ...
33. offset += actualRead;
34. } while (true);

36. delete[] buffer;
37. }

39. void ClientCallBack_OnErrorFunc(ContentEmbed_ExtensionProxy *proxy, ContentEmbed_ErrorCode error)
40. {
41. OH_LOG_INFO(LOG_APP, "Enter ClientCallBack_OnErrorFunc, error: %{public}d", error);
42. }

44. void ClientCallBack_OnEditingFinishedFunc(ContentEmbed_ExtensionProxy *proxy, bool dataModified)
45. {
46. OH_LOG_INFO(LOG_APP, "Enter ClientCallBack_OnEditingFinishedFunc, dataModified: %{public}d", dataModified);
47. // 建议此时销毁OE文档和客户端OE对象，释放资源。
48. ContentEmbed_Document *document = nullptr;
49. ContentEmbed_ErrorCode errCode = OH_ContentEmbed_Proxy_GetDocument(proxy, &document);
50. if (errCode != CE_ERR_OK) {
51. OH_LOG_ERROR(LOG_APP, "OH_ContentEmbed_Proxy_GetDocument failed, errCode: %{public}d.", errCode);
52. return;
53. }
54. // 销毁OE文档
55. OH_ContentEmbed_DestroyDocument(document);
56. // 销毁客户端OE对象
57. OH_ContentEmbed_DestroyExtensionProxy(proxy);
58. }

60. void ClientCallBack_OnExtensionStoppedFunc(ContentEmbed_ExtensionProxy *proxy)
61. {
62. OH_LOG_INFO(LOG_APP, "Enter ClientCallBack_OnExtensionStoppedFunc");
63. }

65. // contextPtr: 当前上下文实例
66. // oeDocument: OE文档
67. void CreateProxy(void* contextPtr, ContentEmbed_Document *oeDocument)
68. {
69. ContentEmbed_ExtensionProxy* proxy;
70. // 创建客户端OE对象
71. ContentEmbed_ErrorCode errCode = OH_ContentEmbed_CreateExtensionProxy(oeDocument, &proxy, contextPtr);
72. if (errCode != CE_ERR_OK) {
73. OH_LOG_ERROR(LOG_APP, "OH_ContentEmbed_CreateExtensionProxy failed, errCode: %{public}d.", errCode);
74. return;
75. }
76. // 注册回调：注册文档更新、错误、编辑结束等回调函数，回调函数注册顺序无要求，但不能遗漏。
77. // 注册OE文档更新回调
78. errCode = OH_ContentEmbed_Proxy_RegisterOnUpdateFunc(proxy, ClientCallBack_OnUpdateFunc);
79. if (errCode != CE_ERR_OK) {
80. OH_LOG_ERROR(LOG_APP, "OH_ContentEmbed_Proxy_RegisterOnUpdateFunc failed, errCode: %{public}d.", errCode);
81. return;
82. }
83. // 注册OE文档发生错误回调
84. errCode = OH_ContentEmbed_Proxy_RegisterOnErrorFunc(proxy, ClientCallBack_OnErrorFunc);
85. if (errCode != CE_ERR_OK) {
86. OH_LOG_ERROR(LOG_APP, "OH_ContentEmbed_Proxy_RegisterOnErrorFunc failed, errCode: %{public}d.", errCode);
87. return;
88. }
89. // 注册OE文档编辑结束回调
90. errCode = OH_ContentEmbed_Proxy_RegisterOnEditingFinishedFunc(proxy, ClientCallBack_OnEditingFinishedFunc);
91. if (errCode != CE_ERR_OK) {
92. OH_LOG_ERROR(LOG_APP, "OH_ContentEmbed_Proxy_RegisterOnEditingFinishedFunc failed, errCode: %{public}d.", errCode);
93. return;
94. }
95. // 注册Extension实例关闭回调
96. errCode = OH_ContentEmbed_Proxy_RegisterOnExtensionStoppedFunc(proxy, ClientCallBack_OnExtensionStoppedFunc);
97. if (errCode != CE_ERR_OK) {
98. OH_LOG_ERROR(LOG_APP, "OH_ContentEmbed_Proxy_RegisterOnExtensionStoppedFunc failed, errCode: %{public}d.", errCode);
99. return;
100. }
101. }
```

获取当前上下文实例。

```
1. // 获取UIAbility Context
2. let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
3. // 调用Native接口，将Context传到C++侧处理
4. nativeModule.receiveContext(context);
```

```
1. static napi_value ReceiveContext(napi_env env, napi_callback_info info) {
2. size_t argc = 1;
3. napi_value argv[2] = {nullptr};
4. napi_get_cb_info(env, info, &argc, argv, nullptr, nullptr);

6. // 获取ArkTS传递的UIAbilityContext对象
7. napi_value contextObj = argv[0];
8. void* contextPtr = nullptr;
9. napi_ref tmp = nullptr;
10. // 创建强引用，引用计数+1，防止ArkTS垃圾回收把这个Context回收掉
11. napi_create_reference(env, contextObj, 1, &tmp);
12. // 把ArkTS对象解包为C++指针
13. napi_status status = napi_unwrap(env, contextObj, &contextPtr);

15. if (status != napi_ok || contextPtr == nullptr) {
16. // 错误处理
17. napi_throw_error(env, nullptr, "Failed to unwrap context");
18. return nullptr;
19. }
20. // 记录contextPtr，后续使用
21. // ...
22. return nullptr;
23. }

25. // napi注册
26. EXTERN_C_START
27. static napi_value Init(napi_env env, napi_value exports) {
28. napi_property_descriptor desc[] = {
29. {"receiveContext", nullptr, ReceiveContext, nullptr, nullptr, nullptr, napi_default, nullptr},
30. };
31. napi_define_properties(env, exports, sizeof(desc) / sizeof(desc[0]), desc);
32. return exports;
33. }
34. EXTERN_C_END
```

### 实现客户端OE对象和OE Extension交互

1. 启动OE Extension：启动OE Extension组件。
2. 查询OE Extension组件能力。
3. 编辑文档：通知OE服务端启动UIAbility编辑文档。
4. 查询OE文档编辑状态。
5. 获取OE文档快照。

```
1. void HandleProxy(ContentEmbed_ExtensionProxy* proxy)
2. {
3. ContentEmbed_ErrorCode errCode = CE_ERR_OK;
4. // 启动OE Extension组件
5. errCode = OH_ContentEmbed_Proxy_StartWork(proxy);
6. if (errCode != CE_ERR_OK) {
7. OH_LOG_ERROR(LOG_APP, "OH_ContentEmbed_Proxy_StartWork failed, errCode: %{public}d.", errCode);
8. return;
9. }
10. uint32_t bitmask = 0;
11. // 查询OE Extension组件能力
12. errCode = OH_ContentEmbed_Proxy_GetCapability(proxy, &bitmask);
13. if (errCode != CE_ERR_OK) {
14. OH_LOG_ERROR(LOG_APP, "OH_ContentEmbed_Proxy_GetCapability failed, errCode: %{public}d.", errCode);
15. return;
16. }
17. if ((bitmask & CE_CAPABILITY_SUPPORT_DO_EDIT) != 0) {
18. // 服务端支持编辑能力时，通知OE服务端编辑OE文档
19. errCode = OH_ContentEmbed_Proxy_DoEdit(proxy);
20. if (errCode != CE_ERR_OK) {
21. OH_LOG_ERROR(LOG_APP, "OH_ContentEmbed_Proxy_DoEdit failed, errCode: %{public}d.", errCode);
22. return;
23. }
24. }
25. // 主动查询OE文档的编辑状态
26. bool isEditing = false;
27. bool isModified = false;
28. // 查询被嵌入文档编辑状态
29. errCode = OH_ContentEmbed_Proxy_GetEditStatus(proxy, &isEditing, &isModified);
30. if ((bitmask & CE_CAPABILITY_SUPPORT_SNAPSHOT) != 0) {
31. // 服务端支持获取OE快照能力时，从OE服务端获取OE文档快照
32. OH_PixelmapNative* pixelMap;
33. // 获取OE文档快照
34. errCode = OH_ContentEmbed_Proxy_GetSnapshot(proxy, &pixelMap);
35. }
36. // 当proxy不需要和服务端交互时
37. OH_ContentEmbed_Proxy_StopWork(proxy);
38. }
```
