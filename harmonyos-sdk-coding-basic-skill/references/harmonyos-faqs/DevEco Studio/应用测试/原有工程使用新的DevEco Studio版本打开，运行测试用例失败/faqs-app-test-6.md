---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-test-6
title: 原有工程使用新的DevEco Studio版本打开，运行测试用例失败
breadcrumb: FAQ > DevEco Studio > 应用测试 > 原有工程使用新的DevEco Studio版本打开，运行测试用例失败
category: harmonyos-faqs
scraped_at: 2026-06-12T10:45:38+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:fdfb32c2344ab35a417260eb82b28c5b17840bde69da1be59ea8c08edf23d297
---

**问题现象**

如果工程是在DevEco Studio 3.1.0.400之前版本创建的，升级DevEco Studio至3.1.0.400及以上版本后，原有工程运行测试用例会失败，并提示“A page configured in 'test\_pages.json' must have one and only one '@Entry' decorator”。

**图1**   
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/41/v3/suCgr3_1QImrw6J-GIjJPw/zh-cn_image_0000002229604113.png?HW-CC-KV=V1&HW-CC-Date=20260612T024537Z&HW-CC-Expire=86400&HW-CC-Sign=559F7FC753F4542EA35F943AFD259802ABC1D23333DAC9B21EA73418B88CBB9E "点击放大")

**解决措施**

将TestRunner、TestAbility目录改为小写testrunner、testability，再次运行测试用例。

**图2**   
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/45/v3/LMLT-klYS_SudbTyP_0C3Q/zh-cn_image_0000002194158732.png?HW-CC-KV=V1&HW-CC-Date=20260612T024537Z&HW-CC-Expire=86400&HW-CC-Sign=A03672334636DB6D97904134320CD653C31BA8B3A5328D85FC9A4108DBE04109 "点击放大")
