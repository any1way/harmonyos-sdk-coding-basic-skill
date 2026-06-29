---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-139
title: 编译报错“Method setProperty validate failed in hvigorfile.ts”
breadcrumb: FAQ > DevEco Studio > 编译构建 > 编译报错“Method setProperty validate failed in hvigorfile.ts”
category: harmonyos-faqs
scraped_at: 2026-06-12T10:43:00+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:bc64aa2dbfe03dec8edbf633ab7a2c2368cb75856ccb564ad5e5bd5b529ee94d
---

**错误描述**

setProperty方法在hvigorfile.ts中校验失败。

**可能****原因**

在hvigorfile.ts中使用setProperty方法时，传入的参数未通过 Schema 校验。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ec/v3/My66B7J0SciNRDwDQ-ztlg/zh-cn_image_0000002194318124.png?HW-CC-KV=V1&HW-CC-Date=20260612T024259Z&HW-CC-Expire=86400&HW-CC-Sign=5B87563426B621FF72718A53BBEFADD119CB5D3E20A99D4869570FF1661700A0)

**解决措施**

请根据报错提示信息，修改hvigorfile.ts文件中的配置字段。
