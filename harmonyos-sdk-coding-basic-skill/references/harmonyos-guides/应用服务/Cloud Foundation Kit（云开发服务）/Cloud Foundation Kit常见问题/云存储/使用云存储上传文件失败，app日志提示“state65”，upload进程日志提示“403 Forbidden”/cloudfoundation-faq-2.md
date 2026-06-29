---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cloudfoundation-faq-2
title: 使用云存储上传文件失败，app日志提示“"state":65”，upload进程日志提示“403 Forbidden”
breadcrumb: 指南 > 应用服务 > Cloud Foundation Kit（云开发服务） > Cloud Foundation Kit常见问题 > 云存储 > 使用云存储上传文件失败，app日志提示“"state":65”，upload进程日志提示“403 Forbidden”
category: harmonyos-guides
scraped_at: 2026-06-11T15:06:18+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:631da4ef551d9590ff6217e09de1f8ddd7c9a458b597ff63e5103ee7339bcc70
---
**问题现象**

使用云存储上传文件失败，出现如下错误提示：

* app日志提示“"state":65”

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b9/v3/jUEhgVDYQZy1NRN8689L4w/zh-cn_image_0000002622698875.png?HW-CC-KV=V1&HW-CC-Date=20260611T070617Z&HW-CC-Expire=86400&HW-CC-Sign=55CB55DACCA6DCC81C27685640B5B1F6F04E4C7C95ADFAEE1D32CE2EAFF4DB2A)
* upload进程的日志提示“403 Forbidden”（通过设置“No filters”模式、过滤“C01C50”关键字查找）

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5b/v3/5BHfhtWETIO5wVFpzsMQBw/zh-cn_image_0000002592219314.png?HW-CC-KV=V1&HW-CC-Date=20260611T070617Z&HW-CC-Expire=86400&HW-CC-Sign=A5A3CB5A251638FD01B8CC815E6B5963434E1FE540ACA0DC82C5B40A9A5F7DEF)

**解决措施**

出现此问题，可按照如下步骤排查和解决：

1. 请确认应用的签名方式正确。当前Cloud Foundation Kit支持[关联注册应用进行自动签名](../../../../../编写与调试应用/配置调试签名/ide-signing.md#section20943184413328)和[手动签名](../../../../../编写与调试应用/配置调试签名/ide-signing.md#section297715173233)两种方式。
2. 请确认已通过[AuthProvider](<../../../../../../harmonyos-references/Cloud Foundation Kit（云开发服务）/ArkTS API/cloudCommon (公共模块)/cloudfoundation-cloudcommon.md#authprovider>)获取用户凭据。未配置用户凭据的情况下，服务端会返回“403 Forbidden”错误。
