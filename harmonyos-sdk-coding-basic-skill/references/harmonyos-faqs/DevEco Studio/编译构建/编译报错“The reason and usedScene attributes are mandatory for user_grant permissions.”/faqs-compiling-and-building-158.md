---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-158
title: 编译报错“The reason and usedScene attributes are mandatory for user_grant permissions.”
breadcrumb: FAQ > DevEco Studio > 编译构建 > 编译报错“The reason and usedScene attributes are mandatory for user_grant permissions.”
category: harmonyos-faqs
scraped_at: 2026-06-12T10:43:18+08:00
doc_updated_at: 2026-05-15
content_hash: sha256:6119f270ae62619c48c6490886c27a10710f75548180fe245cb482f14437a00a
---

**错误描述**

针对Hap模块，配置user\_grant权限时必须包含reason和usedScene属性。

**可能原因**

在module.json5文件中配置user\_grant类型的权限时，必须包含reason和usedScene属性。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/88/v3/oXsogVZHRUetwgmuwIHIxA/zh-cn_image_0000002194158708.png?HW-CC-KV=V1&HW-CC-Date=20260612T024317Z&HW-CC-Expire=86400&HW-CC-Sign=DCB1269D67A911BDAF3D7C61B15A7F060ED7463B77818CA1330388122CB9B027)

**解决措施**

对于Hap模块，在module.json5文件的requestPermissions中添加reason和usedScene字段。

对于Har/Hsp模块，在module.json5文件的requestPermissions中添加reason字段。

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
