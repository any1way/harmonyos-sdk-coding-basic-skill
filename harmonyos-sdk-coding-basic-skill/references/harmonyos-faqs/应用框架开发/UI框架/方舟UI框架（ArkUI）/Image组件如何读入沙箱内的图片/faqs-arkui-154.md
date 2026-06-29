---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-154
title: Image组件如何读入沙箱内的图片
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > Image组件如何读入沙箱内的图片
category: harmonyos-faqs
scraped_at: 2026-06-12T10:28:16+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:77a07471d03236ae40c7f394a89122278d0471cd84c80d6370c5cb754f3be6b1
---
Image组件不能直接传入应用沙箱路径，需要传入应用沙箱URI。

1. 参考fileUri模块示例代码，获取文件的沙箱路径。
2. 然后调用fileUri.getUriFromPath方法将沙箱路径转化为沙箱URI，传入之后即可正常显示沙箱图片。

**参考链接**

[@ohos.file.fileuri (文件URI)](<../../../../../harmonyos-references/Core File Kit（文件基础服务）/ArkTS API/@ohos.file.fileuri (文件URI)/js-apis-file-fileuri.md>)
