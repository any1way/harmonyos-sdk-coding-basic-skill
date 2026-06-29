---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-test-3
title: 运行测试用例时，结果树始终处于加载状态
breadcrumb: FAQ > DevEco Studio > 应用测试 > 运行测试用例时，结果树始终处于加载状态
category: harmonyos-faqs
scraped_at: 2026-06-12T10:45:32+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:8d9849399c339b216c199a15bdcaa79b797e74a3f5cbd05798fecf1fa8e5ccc9
---

**问题现象**

如果多个模块（如entry和feature模块）同时依赖HSP，在设备上先运行entry和HSP模块，再执行feature模块下的测试用例时，任务结果树会一直处于加载状态，无法正常完成。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/43/v3/d-m36MH5T9KibjfSDZHOfA/zh-cn_image_0000002229758525.png?HW-CC-KV=V1&HW-CC-Date=20260612T024531Z&HW-CC-Expire=86400&HW-CC-Sign=DF3710273687559CD1DD1C4A20A6D3A582C479B8D91B689CC40D709D687FD1AF)

**解决措施**

1. 打开非entry模块的ohosTest/ets/testrunner/OpenHarmonyTestRunner.ts文件。
2. 在lMonitor与want中分别增加moduleName字段，该字段用于指定当前模块的名称（即该模块下的module.json5文件中module字段下name的值）。示例代码如下：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/53/v3/ppMolzfMSZWxGF3orEdpWQ/zh-cn_image_0000002194158652.png?HW-CC-KV=V1&HW-CC-Date=20260612T024531Z&HW-CC-Expire=86400&HW-CC-Sign=5C5492FAE136C50EE9AA7E1BF1318CBAA871BA81CF191F87711CCC7E95662C60)
