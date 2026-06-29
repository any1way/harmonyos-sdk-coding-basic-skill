---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/scenario-fusion-faq-3
title: 剪贴板粘贴框遮挡智能填充选择框
breadcrumb: 指南 > 应用服务 > Scenario Fusion Kit（融合场景服务） > Scenario Fusion Kit常见问题 > 剪贴板粘贴框遮挡智能填充选择框
category: harmonyos-guides
scraped_at: 2026-06-11T15:14:30+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:a99ba61fcb078b2d71b39bea127b2e2990e0769efbd021005a63af9e836df305
---

**现象描述**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d1/v3/PMjG0m_KSO-Aj03WcSaJVQ/zh-cn_image_0000002592219596.jpg?HW-CC-KV=V1&HW-CC-Date=20260611T071429Z&HW-CC-Expire=86400&HW-CC-Sign=3D11D1ACA1FB7F6129408E3AF83188E6DA37BC6E67828669522DDCD649A94CFF)

**解决措施**

在代码文件中设置.selectionMenuHidden(true)，使剪贴板粘贴框隐藏。

```
1. Row() {
2. Text('收货人：').textAlign(TextAlign.End).width('25%')
3. TextInput().width('75%').contentType(ContentType.PERSON_FULL_NAME).selectionMenuHidden(true)
4. }
```
