---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-159
title: 编译报错“The reason attribute are mandatory for user_grant permissions.”
breadcrumb: FAQ > DevEco Studio > 编译构建 > 编译报错“The reason attribute are mandatory for user_grant permissions.”
category: harmonyos-faqs
scraped_at: 2026-06-12T10:43:20+08:00
doc_updated_at: 2026-05-15
content_hash: sha256:4e9aca709e9cbf77526a579d10f9fa566d195d0b3ca63204c32f260a3460ce4e
---

**错误描述**

针对Har和Hsp模块，配置user\_grant权限时必须包含reason属性。

**可能原因**

在module.json5文件中配置user\_grant类型的权限时，必须包含reason属性。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c7/v3/RyiE2jPyRNWUj7oo6NBdoQ/zh-cn_image_0000002229758313.png?HW-CC-KV=V1&HW-CC-Date=20260612T024318Z&HW-CC-Expire=86400&HW-CC-Sign=7FF5EF80262F4F785614C73C2A958C37BD56DF7EF7C1F32B8478AD95D31AB214)

**解决措施**

hap模块的module.json5文件中添加reason和usedScene字段。

在module.json5文件的requestPermissions中添加reason字段，用于har/hsp模块。

示例：

```
1. "requestPermissions": [
2. {
3. "name": "ohos.permission.READ_IMAGEVIDEO",
4. "usedScene": {
5. "abilities": [
6. "FormAbility"
7. ]
8. },
9. "reason":"$string:location_permission_reason"
10. }
11. ]
```
