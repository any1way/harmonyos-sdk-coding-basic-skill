---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-local-file-manager-1
title: 如何使用Zip模块解压项目目录rawfile中的文件至应用的沙箱目录中
breadcrumb: FAQ > 应用框架开发 > 本地数据和文件 > 本地文件管理 > 如何使用Zip模块解压项目目录rawfile中的文件至应用的沙箱目录中
category: harmonyos-faqs
scraped_at: 2026-06-12T10:34:48+08:00
doc_updated_at: 2026-04-27
content_hash: sha256:b61bb5ecb2a5180ddf66fd1c6dbe7c2a6f50226025f04e47c634cdd96fd1ac5b
---
1. 使用getRawFileContent接口获取 rawfile 中的文件内容，以字节数组形式返回。
2. 通过context对象获取应用的沙箱目录。
3. 使用file.write接口将rawfile的字节数组写入沙箱目录。
4. 使用zlib.decompressfile接口解压保存在沙箱目录中的文件。

注意：由于RawFile目录受系统保护，直接使用fileio.copyFile可能导致权限错误，请使用本文描述的字节流方式操作。

**参考链接**

[getRawFileContent接口](<../../../../../harmonyos-references/Localization Kit（本地化开发服务）/ArkTS API/@ohos.resourceManager (资源管理)/js-apis-resource-manager.md#getrawfilecontent9>)，[获取应用沙箱目录](<../../../../../harmonyos-references/Core File Kit（文件基础服务）/ArkTS API/@ohos.file.fs (文件管理)/js-apis-file-fs.md#使用说明>)，[fileIo.write接口](<../../../../../harmonyos-references/Core File Kit（文件基础服务）/ArkTS API/@ohos.file.fs (文件管理)/js-apis-file-fs.md#fileiowrite>)，[zlib.decompressFile接口](<../../../../../harmonyos-references/基础功能/Basic Services Kit（基础服务）/ArkTS API/数据文件处理/@ohos.zlib (Zip模块)/js-apis-zlib.md#zlibdecompressfile9>)
