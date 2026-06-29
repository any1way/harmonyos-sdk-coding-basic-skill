---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/filemanagerservice-deletetotrash
title: 删除文件到回收站
breadcrumb: 指南 > 应用服务 > File Manager Service Kit（文件管理服务） > 删除文件到回收站
category: harmonyos-guides
scraped_at: 2026-06-01T15:03:25+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:ccd17c6fcb708c8ca82054186a560d61d87060803f05d521bbd8a36aa149fea5
---
## 场景介绍

删除公共目录的文件到回收站。

## 接口说明

| 接口名 | 描述 |
| --- | --- |
| [deleteToTrash](<../../../../harmonyos-references/File Manager Service Kit（文件管理服务）/ArkTS API/fileManagerService/filemanagerservice-arkts-filemanagerservice.md#filemanagerservicedeletetotrash>)(uri: string): Promise<string> | 删除指定文件到回收站，并返回文件删除到回收站后的uri。使用Promise异步回调。 |

## 示例代码

1.导入文件管理服务模块及相关模块

```
1. import { fileManagerService } from '@kit.FileManagerServiceKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
```

2.删除指定文件到回收站

```
1. async function deleteFile() {
2. // 以内置存储目录为例
3. // 示例代码targetUri表示Download目录下文件
4. // 开发者应根据自己实际获取的uri进行开发，并确保对该文件有读写权限
5. let targetUri: string = "file://docs/storage/Users/currentUser/Download/1.txt";
6. try {
7. let trashUri: string = await fileManagerService.deleteToTrash(targetUri);
8. console.info("trashUri: " + trashUri);
9. } catch (err) {
10. let error: BusinessError = err as BusinessError;
11. console.error("delete failed, errCode:" + error.code + ", errMessage:" + error.message);
12. }
13. }
```
