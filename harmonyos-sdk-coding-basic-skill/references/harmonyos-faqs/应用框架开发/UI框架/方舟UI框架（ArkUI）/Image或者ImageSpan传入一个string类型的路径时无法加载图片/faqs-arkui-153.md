---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-153
title: Image或者ImageSpan传入一个string类型的路径时无法加载图片
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > Image或者ImageSpan传入一个string类型的路径时无法加载图片
category: harmonyos-faqs
scraped_at: 2026-06-12T10:28:14+08:00
doc_updated_at: 2026-06-05
content_hash: sha256:7f00f735ddef865745cb3bf5e6563d751088026b9cde55aefab8dcdd83086c45
---
**解决措施**

string类型的路径图片无法加载的可能情况以及对应的解决方案如下：

1. 使用的网络图片的路径

   确保网络图片路径可用，并且申请了ohos.permission.INTERNET权限，具体申请方式请参考[声明权限](../../../../../harmonyos-guides/系统/安全/程序访问控制/应用权限管控/申请应用权限/声明权限/declare-permissions.md)。
2. 使用沙箱路径或媒体库路径

   支持file://路径前缀的字符串，应用沙箱URI：file://<bundleName>/<sandboxPath>。应用沙箱路径URI构造可参考[constructor](<../../../../../harmonyos-references/Core File Kit（文件基础服务）/ArkTS API/@ohos.file.fileuri (文件URI)/js-apis-file-fileuri.md#constructor10>)。沙箱路径需要使用[fileUri.getUriFromPath(path)](<../../../../../harmonyos-references/Core File Kit（文件基础服务）/ArkTS API/@ohos.file.fileuri (文件URI)/js-apis-file-fileuri.md#fileurigeturifrompath>)方法将路径转换为应用沙箱URI，然后传入显示。同时需要保证目录包路径下的文件有可读权限。
3. 使用base64字符串

   需要注意路径格式，路径格式为data:image/[png|jpeg|bmp|webp|heif];base64,[base64 data]，其中[base64 data]为Base64字符串数据。

**参考链接：**

[加载图片资源](<../../../../../harmonyos-guides/应用框架/ArkUI（方舟UI框架）/UI开发 (ArkTS声明式开发范式)/媒体展示/显示图片 (Image)/arkts-graphics-display.md#加载图片资源>)
