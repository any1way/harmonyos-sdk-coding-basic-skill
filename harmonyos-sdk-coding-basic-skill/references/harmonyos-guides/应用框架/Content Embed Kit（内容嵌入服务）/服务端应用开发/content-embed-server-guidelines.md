---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/content-embed-server-guidelines
title: 服务端应用开发
breadcrumb: 指南 > 应用框架 > Content Embed Kit（内容嵌入服务） > 服务端应用开发
category: harmonyos-guides
scraped_at: 2026-06-01T11:10:31+08:00
doc_updated_at: 2026-04-30
content_hash: sha256:f8aca3a753a59457cea9ebde9c8fe767810b531f55da8f401b6ce17dd8bea25b
---
## 场景介绍

[OH\_ContentEmbed](<../../../../harmonyos-references/Content Embed Kit（内容嵌入服务）/C API/模块/ContentEmbed/capi-contentembed.md>)内容嵌入模块提供对象编辑框架与技术，支持应用间文档嵌入与协同编辑。

OE服务端应用使用[OE Extension框架](<../../../../harmonyos-references/Content Embed Kit（内容嵌入服务）/C API/头文件/content_embed_extension.h/capi-content-embed-extension-h.md>)提供的接口，向客户端应用提供特定格式文档的嵌入与编辑能力。

## 约束限制

在使用接口前，需先确认设备具备SystemCapability.ContentEmbed.ObjectEditor系统能力，判断方式请参阅[查询指定的系统能力是否被支持](<../../../../harmonyos-references/C API/模块/Init/init.md#caniuse>)。并申请ohos.permission.REGISTER\_OBJECTEDITOR\_EXTENSION权限，配置方式请参阅[声明权限](../../../系统/安全/程序访问控制/应用权限管控/申请应用权限/声明权限/declare-permissions.md)。

## 接口说明

常用接口如下表所示。更多API说明请参考[OH\_ContentEmbed](<../../../../harmonyos-references/Content Embed Kit（内容嵌入服务）/C API/模块/ContentEmbed/capi-contentembed.md>)。

**表1** 服务端主要接口

| 接口名称 | 功能描述 |
| --- | --- |
| OH\_ContentEmbed\_Extension\_GetExtensionInstance | 从ExtensionAbility基类实例中获取对应的[OE Extension](<../Content Embed Kit术语/content-embed-kit-terminology.md#oe-extension>)实例。 |
| OH\_ContentEmbed\_Extension\_GetContentEmbedContext | 从OE Extension实例中获取其对应的OE Extension上下文对象。 |
| OH\_ContentEmbed\_Extension\_GetContext | 从OE Extension上下文中获取AbilityRuntime上下文。 |
| OH\_ContentEmbed\_Extension\_RegisterOnCreateFunc | 注册OE Extension实例创建时的生命周期函数。 |
| OH\_ContentEmbed\_Extension\_RegisterOnDestroyFunc | 注册OE Extension实例销毁时的生命周期函数。 |
| OH\_ContentEmbed\_Extension\_RegisterOnObjectAttachFunc | 注册[客户端OE对象](<../Content Embed Kit术语/content-embed-kit-terminology.md#客户端oe对象>)连接时的回调函数。 |
| OH\_ContentEmbed\_Extension\_RegisterOnObjectDetachFunc | 取消注册客户端OE对象连接时的回调函数。 |
| OH\_ContentEmbed\_Extension\_RegisterOnWriteToDataStreamFunc | 注册[服务端OE对象](<../Content Embed Kit术语/content-embed-kit-terminology.md#服务端oe对象>)写入[OE文档](<../Content Embed Kit术语/content-embed-kit-terminology.md#oe文档>)数据流时的回调函数。 |
| OH\_ContentEmbed\_Extension\_RegisterOnGetSnapshotFunc | 注册客户端OE对象请求获取OE文档快照时的回调函数。 |
| OH\_ContentEmbed\_Extension\_RegisterOnDoEditFunc | 注册客户端OE对象请求编辑OE文档时的回调函数。 |
| OH\_ContentEmbed\_Extension\_RegisterOnGetEditStatusFunc | 注册客户端OE对象请求OE文档编辑状态时的回调函数。 |
| OH\_ContentEmbed\_Extension\_RegisterOnGetCapabilityFunc | 注册客户端OE对象查询OE Extension实例支持能力时的回调函数。 |
| OH\_ContentEmbed\_Extension\_GetContentEmbedDocument | 获取服务端OE对象关联的OE文档实例。 |
| OH\_ContentEmbed\_Extension\_CallbackToOnUpdate | 触发客户端OE对象注册的OE文档更新回调函数。 |
| OH\_ContentEmbed\_Extension\_CallbackToOnError | 触发客户端OE对象注册的OE文档错误回调函数。 |
| OH\_ContentEmbed\_Extension\_CallbackToOnEditingFinished | 触发客户端OE对象注册的OE文档编辑完成回调函数。 |
| OH\_ContentEmbed\_Extension\_CallbackToOnExtensionStopped | 触发OE Extension关联的所有客户端OE对象注册的OE Extension停止时的回调函数。 |
| OH\_ContentEmbed\_Extension\_SetSnapshot | 设置客户端OE对象关联的OE文档快照图像。 |
| OH\_ContentEmbed\_Extension\_ContextStartSelfUIAbility | 通过OE Extension上下文启动自身的UIAbility。 |

## 开发步骤

以下演示使用Native API开发OE服务端应用的完整流程，演示了OE服务端注册Extension组件回调，响应客户端请求，返回OE文档快照和启动UIAbility编辑OE文档。

### OE服务端配置OE ExtensionAbility

从API version 24版本开始，在module.json5文件的extensionAbilities标签中配置OE ExtensionAbility，示例如下：

```
1. "extensionAbilities": [
2. {
3. "name": "OEExtAbility",
4. "srcEntry": "libentry.so",
5. "type": "contentEmbed",
6. "exported": true,
7. "metadata": [
8. {
9. "name": "content_embed_config",
10. "resource": "$profile:content_embed_config"
11. }
12. ]
13. }
14. ]
```

配置说明：

* name：Extension组件的名称。
* srcEntry：Extension组件的入口库文件路径。
* type：必须设置为"contentEmbed"。
* exported：必须设置为true，表示对外暴露。
* [metadata](../../../基础入门/开发基础知识/应用配置文件（Stage模型）/module.json5配置文件/module-configuration-file.md#metadata标签)：元数据信息"metadata"新增一个"name"为"content\_embed\_config"的数据项，"resource"为OE Extension配置文件的资源索引。

开发者需要新增一个二级配置json文件，用于配置OE Extension信息。例如将"resource"配置成"$profile:content\_embed\_config"，表示指向resources/base/profile/content\_embed\_config.json配置文件。json文件示例如下：

```
1. {
2. "content_embed_config": [
3. {
4. "oeid": "E0A8B74A-445B-4D7A-8B05-07B5509B50D8",
5. "file_exts": ".doc|.docx",
6. "icon": "$media:app_logo",
7. "name": "$string:name",
8. "description": "$string:description"
9. }
10. ]
11. }
```

配置说明：

* oeid：OE文档的系统可识别标识符，用于定位支持该OE文档的OE服务端应用。
  + 如果OE服务端应用在其它操作系统上也有相同功能，建议复用已在其它系统中使用的ID；
  + 如果OE服务端应用该功能仅在HarmonyOS系统上提供，则建议使用系统自带的“终端”工具，通过uuidgen命令生成新的ID。
* file\_exts：支持的文件扩展名，如".doc"、".docx"等，如果支持多个文件后缀，使用"|"进行隔开。
* icon：OE文档查询显示图标，取值为图标资源文件的索引。
* name：OE文档查询显示名称，要求采用该名称的资源索引，以支持多语言。
* description：OE文档查询显示描述，要求采用该名称的资源索引，以支持多语言。

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
9. # ability
10. libability_runtime.so
11. # want
12. libability_base_want.so
13. # fileuri
14. libohfileuri.so
15. # libimage_source
16. libimage_source.so
```

### 导入头文件

```
1. #include <cstdint>
2. #include <fstream>
3. #include <hilog/log.h>
4. #include <AbilityKit/ability_base/want.h>
5. #include <AbilityKit/ability_runtime/application_context.h>
6. #include <ContentEmbedKit/content_embed/content_embed_document.h>
7. #include <ContentEmbedKit/content_embed/content_embed_extension.h>
8. #include <filemanagement/file_uri/oh_file_uri.h>
9. #include <multimedia/image_framework/image/image_source_native.h>
```

### 定义全局变量

```
1. static ContentEmbed_ExtensionInstanceHandle g_instance = nullptr;
```

### 注册Extension回调函数

当OE服务端应用的OE Extension被系统启动以响应OE客户端请求时，首先执行[OH\_AbilityRuntime\_OnNativeExtensionCreate](<../../../../harmonyos-references/Ability Kit（程序框架服务）/C API/头文件/extension_ability.h/capi-extension-ability-h.md#oh_abilityruntime_onnativeextensioncreate>)函数，需在该函数中注册OE Extension回调，以响应客户端请求。

```
1. extern "C" void OH_AbilityRuntime_OnNativeExtensionCreate(AbilityRuntime_ExtensionInstance *instance, const char *abilityName) {
2. if (instance == nullptr) {
3. OH_LOG_ERROR(LOG_APP, "instance is null");
4. return;
5. }

7. ContentEmbed_ExtensionInstanceHandle ceExtensionInstance;
8. // 获取OE Extension实例
9. ContentEmbed_ErrorCode ret = OH_ContentEmbed_Extension_GetExtensionInstance(instance, &ceExtensionInstance);
10. if (ret != CE_ERR_OK) {
11. OH_LOG_ERROR(LOG_APP, "OH_ContentEmbed_Extension_GetExtensionInstance failed, errCode: %{public}d.", ret);
12. return;
13. }
14. // 给全局变量赋值
15. g_instance = ceExtensionInstance;
16. // 注册OE Extension创建函数回调
17. ret = OH_ContentEmbed_Extension_RegisterOnCreateFunc(ceExtensionInstance, NativeOnCreate);
18. if (ret != CE_ERR_OK) {
19. OH_LOG_ERROR(LOG_APP, "OH_ContentEmbed_Extension_RegisterOnCreateFunc failed, errCode: %{public}d.", ret);
20. return;
21. }
22. // 注册OE Extension销毁函数回调
23. ret = OH_ContentEmbed_Extension_RegisterOnDestroyFunc(ceExtensionInstance, NativeOnDestroy);
24. if (ret != CE_ERR_OK) {
25. OH_LOG_ERROR(LOG_APP, "OH_ContentEmbed_Extension_RegisterOnDestroyFunc failed, errCode: %{public}d.", ret);
26. return;
27. }
28. // 注册服务端OE对象绑定回调
29. ret = OH_ContentEmbed_Extension_RegisterOnObjectAttachFunc(ceExtensionInstance, RegisterOnObjectAttachFunc);
30. if (ret != CE_ERR_OK) {
31. OH_LOG_ERROR(LOG_APP, "OH_ContentEmbed_Extension_RegisterOnObjectAttachFunc failed, errCode: %{public}d.", ret);
32. return;
33. }
34. // 注册服务端OE对象解绑回调
35. ret = OH_ContentEmbed_Extension_RegisterOnObjectDetachFunc(ceExtensionInstance, RegisterOnObjectDetachFunc);
36. if (ret != CE_ERR_OK) {
37. OH_LOG_ERROR(LOG_APP, "OH_ContentEmbed_Extension_RegisterOnObjectDetachFunc failed, errCode: %{public}d.", ret);
38. return;
39. }
40. }
```

### 实现创建和销毁生命周期回调函数

```
1. static void NativeOnCreate(ContentEmbed_ExtensionInstanceHandle instance, AbilityBase_Want *want)
2. {
3. OH_LOG_INFO(LOG_APP, "enter NativeOnCreate");
4. }

6. static void NativeOnDestroy(ContentEmbed_ExtensionInstanceHandle instance)
7. {
8. OH_LOG_INFO(LOG_APP, "enter NativeOnDestroy");
9. }
```

### 实现服务端OE对象绑定和解绑的回调函数

当OE客户端调用[OH\_ContentEmbed\_Proxy\_StartWork](<../../../../harmonyos-references/Content Embed Kit（内容嵌入服务）/C API/头文件/content_embed_proxy.h/capi-content-embed-proxy-h.md#oh_contentembed_proxy_startwork>)函数将客户端OE对象与服务端OE对象绑定时，系统会触发OE服务端的RegisterOnObjectAttachFunc回调。在此回调中，OE服务端需调用服务端OE对象的注册函数以响应OE客户端的请求。

当OE客户端调用[OH\_ContentEmbed\_Proxy\_StopWork](<../../../../harmonyos-references/Content Embed Kit（内容嵌入服务）/C API/头文件/content_embed_proxy.h/capi-content-embed-proxy-h.md#oh_contentembed_proxy_stopwork>)函数将客户端OE对象与服务端OE对象解除绑定时，系统会触发OE服务端的RegisterOnObjectDetachFunc回调，在该回调后服务端OE对象将失效。

```
1. static void RegisterOnObjectAttachFunc(ContentEmbed_ExtensionInstanceHandle instance, ContentEmbed_ObjectHandle object)
2. {
3. ContentEmbed_ErrorCode ret = CE_ERR_OK;
4. // 当OE文档是通过文件创建的时候执行该回调函数
5. ret = OH_ContentEmbed_Extension_RegisterOnWriteToDataStreamFunc(object, NativeOnWriteToDataStream);
6. if (ret != CE_ERR_OK) {
7. OH_LOG_ERROR(LOG_APP, "OH_ContentEmbed_Extension_RegisterOnWriteToDataStreamFunc failed, errCode: %{public}d.", ret);
8. return;
9. }
10. // 获取当前OE Extension的能力
11. ret = OH_ContentEmbed_Extension_RegisterOnGetCapabilityFunc(object, NativeOnGetCapability);
12. if (ret != CE_ERR_OK) {
13. OH_LOG_ERROR(LOG_APP, "OH_ContentEmbed_Extension_RegisterOnGetCapabilityFunc failed, errCode: %{public}d.", ret);
14. return;
15. }
16. // OE文档触发编辑操作
17. ret = OH_ContentEmbed_Extension_RegisterOnDoEditFunc(object, NativeOnDoEdit);
18. if (ret != CE_ERR_OK) {
19. OH_LOG_ERROR(LOG_APP, "OH_ContentEmbed_Extension_RegisterOnDoEditFunc failed, errCode: %{public}d.", ret);
20. return;
21. }
22. // OE文档请求获取快照
23. ret = OH_ContentEmbed_Extension_RegisterOnGetSnapshotFunc(object, NativeOnGetSnapshot);
24. if (ret != CE_ERR_OK) {
25. OH_LOG_ERROR(LOG_APP, "OH_ContentEmbed_Extension_RegisterOnGetSnapshotFunc failed, errCode: %{public}d.", ret);
26. return;
27. }
28. // OE文档查询当前编辑状态
29. ret = OH_ContentEmbed_Extension_RegisterOnGetEditStatusFunc(object, NativeOnGetEditStatusFunc);
30. if (ret != CE_ERR_OK) {
31. OH_LOG_ERROR(LOG_APP, "OH_ContentEmbed_Extension_RegisterOnGetEditStatusFunc failed, errCode: %{public}d.", ret);
32. return;
33. }
34. }

36. static void RegisterOnObjectDetachFunc(ContentEmbed_ExtensionInstanceHandle instance, ContentEmbed_ObjectHandle object)
37. {
38. OH_LOG_INFO(LOG_APP, "enter RegisterOnObjectDetachFunc");
39. }
```

### 实现获取OE文档快照

当OE客户端通过新建对象类型或已存在文件来嵌入OE对象时，OE对象在OE客户端界面中可能呈现为文档快照（Snapshot），当OE Extension被启动后，OE客户端会通过[OH\_ContentEmbed\_Proxy\_GetSnapshot](<../../../../harmonyos-references/Content Embed Kit（内容嵌入服务）/C API/头文件/content_embed_proxy.h/capi-content-embed-proxy-h.md#oh_contentembed_proxy_getsnapshot>)获取文档快照，此时会触发OE服务端的NativeOnGetSnapshot回调，在该回调中OE服务端应用需调用[OH\_ContentEmbed\_Extension\_SetSnapshot](<../../../../harmonyos-references/Content Embed Kit（内容嵌入服务）/C API/头文件/content_embed_extension.h/capi-content-embed-extension-h.md#oh_contentembed_extension_setsnapshot>)设置OE文档快照。

```
1. static void NativeOnGetSnapshot(ContentEmbed_ObjectHandle object)
2. {
3. // 当前OE文档快照路径
4. std::string path = "/data/storage/el2/base/haps/entry/temp/snapshot_demo.png";
5. // 判断当前是否有UI生成的缩略图
6. FILE *srcFile = fopen(path.c_str(), "rb");
7. if (!srcFile) {
8. OH_LOG_ERROR(LOG_APP, "文件打开失败");
9. return;
10. }
11. int fd = fileno(srcFile);
12. // 创建ImageSource实例。
13. OH_ImageSourceNative *source = nullptr;
14. Image_ErrorCode errCode = OH_ImageSourceNative_CreateFromFd(fd, &source);
15. if (errCode != IMAGE_SUCCESS) {
16. OH_LOG_ERROR(LOG_APP, "OH_ImageSourceNative_CreateFromFd failed, errCode: %{public}d.", errCode);
17. return;
18. }
19. // 通过图片解码参数创建PixelMap对象。
20. OH_DecodingOptions *ops = nullptr;
21. OH_DecodingOptions_Create(&ops);
22. // 设置为AUTO会根据图片资源格式解码，如果图片资源为HDR资源则会解码为HDR的pixelmap。
23. OH_DecodingOptions_SetDesiredDynamicRange(ops, IMAGE_DYNAMIC_RANGE_AUTO);
24. OH_PixelmapNative *resPixMap = nullptr;

26. // ops参数支持传入nullptr, 当不需要设置解码参数时，不用创建。
27. errCode = OH_ImageSourceNative_CreatePixelmap(source, ops, &resPixMap);
28. OH_DecodingOptions_Release(ops);
29. if (errCode != IMAGE_SUCCESS) {
30. OH_LOG_ERROR(LOG_APP, "OH_ImageSourceNative_CreatePixelmap failed, errCode: %{public}d.", errCode);
31. return;
32. }
33. // 设置快照
34. ContentEmbed_ErrorCode ret = OH_ContentEmbed_Extension_SetSnapshot(object, resPixMap);
35. // 释放ImageSource实例。
36. OH_ImageSourceNative_Release(source);
37. }
```

### 实现编辑OE文档

当OE Extension被启动后，OE客户端会通过[OH\_ContentEmbed\_Proxy\_DoEdit](<../../../../harmonyos-references/Content Embed Kit（内容嵌入服务）/C API/头文件/content_embed_proxy.h/capi-content-embed-proxy-h.md#oh_contentembed_proxy_doedit>)通知OE服务端编辑OE文档，此时会触发OE服务端的NativeOnDoEdit回调，在该回调中OE服务端应用需调用[OH\_ContentEmbed\_Extension\_ContextStartSelfUIAbility](<../../../../harmonyos-references/Content Embed Kit（内容嵌入服务）/C API/头文件/content_embed_extension.h/capi-content-embed-extension-h.md#oh_contentembed_extension_contextstartselfuiability>)或[OH\_ContentEmbed\_Extension\_ContextStartSelfUIAbilityWithStartOptions](<../../../../harmonyos-references/Content Embed Kit（内容嵌入服务）/C API/头文件/content_embed_extension.h/capi-content-embed-extension-h.md#oh_contentembed_extension_contextstartselfuiabilitywithstartoptions>)启动OE服务端应用的UIAbility编辑文档。

```
1. static void NativeOnDoEdit(ContentEmbed_ObjectHandle object)
2. {
3. ContentEmbed_ErrorCode ret = CE_ERR_OK;
4. ContentEmbed_Document* ceDocument;
5. // 获取当前OE文档
6. ret = OH_ContentEmbed_Extension_GetContentEmbedDocument(object, &ceDocument);
7. if (ret != CE_ERR_OK) {
8. OH_LOG_ERROR(LOG_APP, "OH_ContentEmbed_Extension_GetContentEmbedDocument failed, errCode: %{public}d.", ret);
9. return;
10. }
11. // 获取当前上下文实例
12. ContentEmbed_ExtensionContextHandle context;
13. ret = OH_ContentEmbed_Extension_GetContentEmbedContext(g_instance, &context);
14. if (ret != CE_ERR_OK) {
15. OH_LOG_ERROR(LOG_APP, "OH_ContentEmbed_Extension_GetContentEmbedContext failed, errCode: %{public}d.", ret);
16. return;
17. }
18. // 需要启动的UIAbility的信息
19. char* bundleName = "com.example.oeserverdemo"; // 服务端应用的包名
20. char* moduleName = "entry";
21. char* abilityName = "EntryAbility";
22. // 创建Want对象
23. AbilityBase_Element element = {
24. .bundleName = bundleName,
25. .moduleName = moduleName,
26. .abilityName = abilityName,
27. };
28. AbilityBase_Want* want = OH_AbilityBase_CreateWant(element);
29. // 获取OE文档的RootStorage
30. ContentEmbed_Storage *rootStorage = nullptr;
31. ret = OH_ContentEmbed_Document_GetRootStorage(ceDocument, &rootStorage);
32. if (ret != CE_ERR_OK) {
33. OH_LOG_ERROR(LOG_APP, "OH_ContentEmbed_Document_GetRootStorage failed, errCode: %{public}d.", ret);
34. return;
35. }
36. // 判断document中是否有指定stream
37. ContentEmbed_Stream *childStream;
38. char* fileType = "aaa";
39. ret = OH_ContentEmbed_Storage_GetStream(rootStorage, fileType, &childStream);
40. if (ret == CE_ERR_OK) {
41. size_t bufferSize;
42. // 获取OE文档流的大小
43. ret = OH_ContentEmbed_Stream_GetSize(childStream, &bufferSize);
44. if (ret != CE_ERR_OK) {
45. OH_LOG_ERROR(LOG_APP, "OH_ContentEmbed_Stream_GetSize failed, errCode: %{public}d.", ret);
46. return;
47. }
48. // Read之前需要将流位置重置
49. ret = OH_ContentEmbed_Stream_Seek(childStream, 0);
50. if (ret != CE_ERR_OK) {
51. OH_LOG_ERROR(LOG_APP, "OH_ContentEmbed_Stream_Seek failed, errCode: %{public}d.", ret);
52. return;
53. }
54. unsigned char *buffer;
55. size_t num = 0;
56. // 读取流数据
57. ret = OH_ContentEmbed_Stream_Read(childStream, &buffer, bufferSize, &num);
58. if (ret != CE_ERR_OK) {
59. OH_LOG_ERROR(LOG_APP, "OH_ContentEmbed_Stream_Read failed, errCode: %{public}d.", ret);
60. return;
61. }
62. std::string tempPath = "/data/storage/el2/base/cache/temp_demo.aaa";
63. // 创建输出文件流对象，并以二进制模式打开文件
64. std::ofstream outputFile(tempPath, std::ios::out | std::ios::binary);
65. // 检查文件是否成功打开
66. if (outputFile.is_open()) {
67. // 将缓冲区内容写入文件
68. outputFile.write(reinterpret_cast<const char*>(buffer), bufferSize);
69. // 关闭文件（析构函数会自动调用，但显式关闭是好习惯）
70. outputFile.close();
71. OH_LOG_INFO(LOG_APP, "数据写入成功.");
72. } else {
73. OH_LOG_INFO(LOG_APP, "无法打开文件.");
74. }
75. char* tempFileUri;
76. OH_FileUri_GetUriFromPath(tempPath.c_str(), tempPath.size(), &tempFileUri);
77. // 设置文件路径
78. OH_AbilityBase_SetWantUri(want, tempFileUri);
79. }
80. // 启动UIAbility 对文档进行编辑操作
81. ret = OH_ContentEmbed_Extension_ContextStartSelfUIAbility(context, want);
82. if (ret != CE_ERR_OK) {
83. OH_LOG_ERROR(LOG_APP, "OH_ContentEmbed_Extension_ContextStartSelfUIAbility failed, errCode: %{public}d.", ret);
84. return;
85. }
86. }
```

### 实现获取OE Extension能力

当OE Extension被启动后，OE客户端会通过[OH\_ContentEmbed\_Proxy\_GetCapability](<../../../../harmonyos-references/Content Embed Kit（内容嵌入服务）/C API/头文件/content_embed_proxy.h/capi-content-embed-proxy-h.md#oh_contentembed_proxy_getcapability>)获取OE服务端具备的能力，此时会触发OE服务端的NativeOnGetCapability回调，在该回调中OE服务端应用通过给bitmask属性赋值，通知OE客户端自身具备的能力。

```
1. static void NativeOnGetCapability(ContentEmbed_ObjectHandle object, uint32_t *bitmask)
2. {
3. if (!bitmask) {
4. OH_LOG_ERROR(LOG_APP, "bitmask is null");
5. return;
6. }
7. *bitmask = CE_CAPABILITY_SUPPORT_SNAPSHOT | CE_CAPABILITY_SUPPORT_DO_EDIT;
8. }
```

### 实现查询OE文档编辑状态

当OE Extension被启动后，OE客户端会通过[OH\_ContentEmbed\_Proxy\_GetEditStatus](<../../../../harmonyos-references/Content Embed Kit（内容嵌入服务）/C API/头文件/content_embed_proxy.h/capi-content-embed-proxy-h.md#oh_contentembed_proxy_geteditstatus>)获取OE文档编辑状态，此时会触发OE服务端的NativeOnGetEditStatusFunc回调，在该回调中OE服务端应用通知OE客户端文档编辑状态。

```
1. static void NativeOnGetEditStatusFunc(ContentEmbed_ObjectHandle object, bool *isEditing, bool *isModified)
2. {
3. if (!isEditing || !isModified) {
4. OH_LOG_ERROR(LOG_APP, "param is null");
5. return;
6. }
7. // 若文档未处于编辑态
8. *isEditing = false;
9. *isModified = false;
10. }
```

### 实现OE文档写流操作

当OE客户端通过已存在文件来嵌入OE对象且OE Extension被启动后，此时会触发OE服务端的NativeOnWriteToDataStream回调，在该回调中OE服务端需往OE文档中写入数据。

```
1. static void NativeOnWriteToDataStream(ContentEmbed_ObjectHandle object)
2. {
3. ContentEmbed_ErrorCode ret = CE_ERR_OK;
4. ContentEmbed_Document* ceDocument = nullptr;
5. // 获取OE文档
6. ret = OH_ContentEmbed_Extension_GetContentEmbedDocument(object, &ceDocument);
7. if (ret != CE_ERR_OK) {
8. OH_LOG_INFO(LOG_APP, "OH_ContentEmbed_Extension_GetContentEmbedDocument ret: %{public}d", ret);
9. return;
10. }
11. // 获取Root Storage
12. ContentEmbed_Storage *rootStorage = nullptr;
13. ret = OH_ContentEmbed_Document_GetRootStorage(ceDocument, &rootStorage);
14. if (ret != CE_ERR_OK) {
15. OH_LOG_INFO(LOG_APP, "OH_ContentEmbed_Document_GetRootStorage ret: %{public}d", ret);
16. return;
17. }

19. ContentEmbed_Stream *destStream;
20. char* fileType = "aaa";
21. // 获取名字为aaa的流
22. ret = OH_ContentEmbed_Storage_GetStream(rootStorage, fileType, &destStream);
23. if (ret != CE_ERR_OK) {
24. // 获取失败创建名字为aaa的流
25. ret = OH_ContentEmbed_Storage_CreateStream(rootStorage, fileType, &destStream);
26. }
27. // 获取本地文件路径
28. char nativeFilePath[MAX_PATH_LENGTH];
29. ret = OH_ContentEmbed_Document_GetNativeFilePath(ceDocument, nativeFilePath);
30. if (ret != CE_ERR_OK) {
31. OH_LOG_INFO(LOG_APP, "OH_ContentEmbed_Document_GetNativeFilePath ret: %{public}d", ret);
32. return;
33. }

35. std::string srcStreamPath = std::string(nativeFilePath);
36. std::ifstream oriFile(srcStreamPath, std::ios::binary);
37. if (!oriFile) {
38. OH_LOG_ERROR(LOG_APP, "File not found");
39. return;
40. }
41. oriFile.seekg(0, std::ios::end);
42. size_t oriFileSize = oriFile.tellg();
43. oriFile.seekg(0, std::ios::beg);
44. std::vector<unsigned char> buffer(oriFileSize);
45. oriFile.read(reinterpret_cast<char*>(buffer.data()), oriFileSize);
46. size_t num = 0;
47. // 往OE文档写数据
48. ret = OH_ContentEmbed_Stream_Write(destStream, buffer.data(), oriFileSize, &num);
49. if (ret != CE_ERR_OK) {
50. OH_LOG_INFO(LOG_APP, "OH_ContentEmbed_Stream_Write ret: %{public}d", ret);
51. return;
52. }
53. // 刷新OE文档
54. ret = OH_ContentEmbed_Document_Flush(ceDocument);
55. if (ret != CE_ERR_OK) {
56. OH_LOG_INFO(LOG_APP, "OH_ContentEmbed_Document_Flush ret: %{public}d", ret);
57. return;
58. }
59. }
```
