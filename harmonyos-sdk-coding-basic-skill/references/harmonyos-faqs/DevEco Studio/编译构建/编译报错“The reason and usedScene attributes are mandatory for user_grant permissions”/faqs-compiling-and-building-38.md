---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-38
title: 编译报错“The reason and usedScene attributes are mandatory for user_grant permissions”
breadcrumb: FAQ > DevEco Studio > 编译构建 > 编译报错“The reason and usedScene attributes are mandatory for user_grant permissions”
category: harmonyos-faqs
scraped_at: 2026-06-12T10:41:30+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:e9af4e3e258fb0a3fff17303281ff2f01d0cfb7f254b199854fd3d838597e1b4
---

**问题现象**

DevEco Studio编译失败，提示“The reason and usedScene attributes are mandatory for user\_grant permissions”。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/53/v3/f0e7wO8hRtyqs3bUB7DVLg/zh-cn_image_0000002194158568.png?HW-CC-KV=V1&HW-CC-Date=20260612T024129Z&HW-CC-Expire=86400&HW-CC-Sign=B5976D9D971F8EB5BC9C5930E59C4E2F0487B80B7F4FEE719DB7EB701A124D99 "点击放大")

**问题原因**

从DevEco Studio NEXT Developer Preview 2版本开始，新增规则：APP包中，所有entry和feature hap的module下的requestPermissions权限清单必须指定（可以为空，若非空则name必填；user\_grant权限则必填reason和usedScene字段）。

**解决措施**

进入对应module.json5文件中，补齐requestPermissions字段下的reason和usedScene字段。如以下示例：

```
1. "requestPermissions": [
2. {
3. "name": "ohos.permission.READ_IMAGEVIDEO",
4. "reason": "$string:module_desc",
5. "usedScene": {
6. "abilities": [
7. "EntryAbility"
8. ],
9. "when": "inuse"
10. }
11. }
12. ],
```

[module.json5](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/CompilingAndBuilding/entry/src/main/module.json5#L56-L67)
