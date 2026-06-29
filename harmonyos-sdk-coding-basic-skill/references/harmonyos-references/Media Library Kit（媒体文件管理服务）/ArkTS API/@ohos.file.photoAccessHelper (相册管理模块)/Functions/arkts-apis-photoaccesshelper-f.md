---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-photoaccesshelper-f
title: Functions
breadcrumb: API参考 > 媒体 > Media Library Kit（媒体文件管理服务） > ArkTS API > @ohos.file.photoAccessHelper (相册管理模块) > Functions
category: harmonyos-references
scraped_at: 2026-06-01T16:25:42+08:00
doc_updated_at: 2026-05-26
content_hash: sha256:cf9b5cadd200e5edac5c8b1037dbcf31ec605b0af8d53a7e35c00334ac9ef496
---
说明

本模块首批接口从API version 10开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { photoAccessHelper } from '@kit.MediaLibraryKit';
```

## photoAccessHelper.getPhotoAccessHelper

PhonePC/2in1TabletTVWearable

getPhotoAccessHelper(context: Context): PhotoAccessHelper

获取相册管理模块的实例，用于访问和修改相册中的媒体文件。

**模型约束**： 此接口仅可在Stage模型下使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [Context](<../../../../Ability Kit（程序框架服务）/ArkTS API/接口依赖的元素及定义/application/Context (Stage模型的上下文基类)/js-apis-inner-application-context.md>) | 是 | 传入Ability实例的上下文。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [PhotoAccessHelper](<../Interface (PhotoAccessHelper)/arkts-apis-photo_93807367.md>) | 相册管理模块的实例。 |

**错误码：**

接口抛出错误码的详细介绍请参见[通用错误码](../../../../通用错误码/errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```
1. // 此处获取的phAccessHelper实例为全局对象，后续使用到phAccessHelper的地方默认为使用此处获取的对象，如未添加此段代码报phAccessHelper未定义的错误请自行添加。
2. // 请在组件内获取context，确保this.getUIContext().getHostContext()返回结果为UIAbilityContext
3. import { common } from '@kit.AbilityKit';

5. @Entry
6. @Component
7. struct Index {
8. build() {
9. Row() {
10. Button("example").onClick(async () => {
11. let context: Context = this.getUIContext().getHostContext() as common.UIAbilityContext;
12. let phAccessHelper = photoAccessHelper.getPhotoAccessHelper(context);
13. }).width('100%')
14. }
15. .height('90%')
16. }
17. }
```
