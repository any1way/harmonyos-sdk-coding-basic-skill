---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/filemanagerservice-getfileicon
title: 获取文件图标
breadcrumb: 指南 > 应用服务 > File Manager Service Kit（文件管理服务） > 获取文件图标
category: harmonyos-guides
scraped_at: 2026-06-01T15:03:26+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:83ae55cc5290d7f9856ef81cc566093ef5fa13f5166ad85cc16eb0d2710f8c12
---
## 场景介绍

根据文件类型获取对应的文件图标。

## 接口说明

| 接口名 | 描述 |
| --- | --- |
| function [getFileIconSync](<../../../../harmonyos-references/File Manager Service Kit（文件管理服务）/ArkTS API/fileManagerService/filemanagerservice-arkts-filemanagerservice.md#filemanagerservicegetfileiconsync>)(fileType: string): string | Resource | 根据文件类型获取文件图标。 |
| function [getFileIcon](<../../../../harmonyos-references/File Manager Service Kit（文件管理服务）/ArkTS API/fileManagerService/filemanagerservice-arkts-filemanagerservice.md#filemanagerservicegetfileicon>)(fileType: string): Promise<string | Resource> | 根据文件类型获取文件图标。使用Promise异步回调。 |

## 示例代码

1.导入文件管理服务模块及相关模块

```
1. import { fileManagerService } from '@kit.FileManagerServiceKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { uniformTypeDescriptor } from '@kit.ArkData';
```

2.申请权限。使用获取文件图标接口时，需要在module.json5中声明申请接口所需的权限：ohos.permission.GET\_FILE\_ICON。具体指导可见[声明权限](../../../系统/安全/程序访问控制/应用权限管控/申请应用权限/声明权限/declare-permissions.md)。

3.获取文件图标

```
1. @Entry
2. @Component
3. struct Index {
4. @State fileIcon: string | Resource = '';

6. private getFileIconByFileExtension(filenameExtension: string): void {
7. try {
8. let typeId: string = uniformTypeDescriptor.getUniformDataTypeByFilenameExtension(filenameExtension);
9. this.fileIcon = fileManagerService.getFileIconSync(typeId);
10. } catch (error) {
11. let err: BusinessError = error as BusinessError;
12. console.error('getFileIconByFileExtension failed with err: ' + JSON.stringify(err));
13. }
14. }

16. build() {
17. RelativeContainer() {
18. Column() {
19. Image(this.fileIcon)
20. .height(88)
21. .border({ width: 1, radius: 6 })
22. Button('Update FileIcon')
23. .onClick(() => {
24. // 以txt格式为例
25. this.getFileIconByFileExtension('.txt');
26. })
27. }
28. }
29. .height('100%')
30. .width('100%')
31. }
32. }
```
