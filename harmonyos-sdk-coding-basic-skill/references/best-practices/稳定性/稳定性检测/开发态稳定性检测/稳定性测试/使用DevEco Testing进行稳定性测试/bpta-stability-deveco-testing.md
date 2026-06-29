---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-stability-deveco-testing
title: 使用DevEco Testing进行稳定性测试
breadcrumb: 最佳实践 > 稳定性 > 稳定性检测 > 开发态稳定性检测 > 稳定性测试 > 使用DevEco Testing进行稳定性测试
category: best-practices
scraped_at: 2026-06-12T10:17:31+08:00
doc_updated_at: 2026-03-12
content_hash: sha256:efa3a5e46e65784ead791d9011f0466ba794bbfe658406d0d27eb99fdf120832
---
本文介绍DevEco Testing为HarmonyOS NEXT应用开发者提供的稳定性测试服务，涵盖稳定性基础质量测试和应用探索测试。稳定性基础质量测试依据HarmonyOS NEXT稳定性测试建议，提供应用稳定性基础检测能力，帮助开发者快速上手稳定性测试。应用探索测试采用基于专家经验的智能遍历方法，驱动测试高效执行，构建应用专属测试模型，帮助开发者有效识别应用故障。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dd/v3/4-BZ254NTDyMNSOAdoiZog/zh-cn_image_0000002441736772.png?HW-CC-KV=V1&HW-CC-Date=20260612T021730Z&HW-CC-Expire=86400&HW-CC-Sign=D8D409EAF51F693E6B1A83525CDA7FDCDD713B2B8FC66BDBA98758EDFDDA89CE)

## 稳定性基础质量测试

**稳定性基础质量测试：**根据应用稳定性建议，检测应用运行过程中是否存在应用崩溃、资源过载、内存泄漏等异常情况。

**创建任务**

进入DevEco Testing客户端，在左侧菜单栏选择“稳定性基础质量测试”，点击“稳定性基础质量测试”服务卡片，即进入任务创建界面。按需配置任务参数，点击创建任务即开始测试。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/25/v3/HYXhAbErQZ6eyaK9O9f6Yg/zh-cn_image_0000002475040597.png?HW-CC-KV=V1&HW-CC-Date=20260612T021730Z&HW-CC-Expire=86400&HW-CC-Sign=BE214AD2BD3C0902A719EA7CA5BD55A0D21078496003A3E2563DBFE797B8730A)

任务名称：用于标识任务，工具会根据时间生成默认任务名，支持自定义修改。

备注信息：按需填写任务备注信息，便于快速筛选报告。

测试设备：选择一个待测设备和待测应用。系统版本支持 HarmonyOS 6.0 及以上版本。

选择应用：可选择测试设备上已安装的应用；或安装新的应用，即在测试设备上安装新的应用包。

是否卸载应用：选择卸载应用后，测试时会进行卸载无残留检测，测试任务结束后将自动卸载被测应用。

是否开启多线程检测：打开后，系统支持检测应用多线程安全问题（例如：多个线程并发写入操作）。

是否开启[MemDebug](../../地址越界类问题检测/使用HWASan检测内存错误/bpta-stability-hwasan-detection.md#section10791454125320)模式：打开开关以后，会打开被测应用的内存越界检测开关，可以辅助发现和定位内存越界类问题。

说明

**稳定性基础质量测试最佳测试时长建议设置为8****小时。**

**测试执行**

创建任务后，将会跳转到执行页，进入测试环境初始化阶段。待测试环境初始化完成，待测应用被启动。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/65/v3/vpyTHaIeRFK9ZHmOslJULQ/zh-cn_image_0000002475126385.png?HW-CC-KV=V1&HW-CC-Date=20260612T021730Z&HW-CC-Expire=86400&HW-CC-Sign=4725F34E7B70078ABCE1F46C1BB9FDD2F32AA034110FE3DE6AA020C7E640C6C0)

测试过程中，在测试页面可以看到测试进度、检测状态、实时投屏及执行日志。

**查看报告**

测试完成后，自动生成测试报告。报告包含任务信息、结果统计、检测规则。

任务信息中，可查看当前应用信息、任务执行时长及详细的环境参数（配置信息及环境信息），点击打开目录按钮支持导出 HTML 的报告文件。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1e/v3/ynkjketPQRiA7rrhsuTvkQ/zh-cn_image_0000002475127285.png?HW-CC-KV=V1&HW-CC-Date=20260612T021730Z&HW-CC-Expire=86400&HW-CC-Sign=A3F6443F36722B1FD35E6206FE1A317F0CE1B9CCA81E0BF770B104C9F90106C4)

测试概览中，包含结果统计及检测规则，可直观查看本次任务中，测试项检测结果。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/56/v3/c92sTGZpTKGs255OROqLyw/zh-cn_image_0000002441728014.png?HW-CC-KV=V1&HW-CC-Date=20260612T021730Z&HW-CC-Expire=86400&HW-CC-Sign=FE244A8B32CD9FD997E2232032581ECE0EF950328296A86D0722143F5C34E591)检测不通过或检测异常的规则项，点击查看详情即可查看异常问题详情，包含检测项概览、测试截图、问题列表。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6f/v3/dpGnBLDDQjCD7PqRKHO5vQ/zh-cn_image_0000002475048409.png?HW-CC-KV=V1&HW-CC-Date=20260612T021730Z&HW-CC-Expire=86400&HW-CC-Sign=721E201998903E2E82570D6F1D7C21430F93A1C036A02D96CE4C89C6D3831BA1)点击查看按钮，支持查看测试过程中的日志，用户可结合问题描述及日志详情进一步分析。

说明

更多测试服务详情，请前往DevEco Testing客户端->专项测试->稳定性基础质量测试->任务创建页->测试指南中查询。

更多应用稳定性体验优化建议及问题定位，请查阅：[应用稳定性体验建议](../../../../../../harmonyos-guides/应用体验建议/应用稳定性体验建议/experience-suggestions-stability.md) 及 [CppCrash问题定位](https://developer.huawei.com/consumer/cn/doc/architecture-guides/common-v1_26-ts_c25-0000002324993158)

## 其他专项测试

请参考：[专项测试](<../../../../../../harmonyos-guides/应用测试/专项测试/DevEco Testing/专项测试/specialized-testing.md>)。

## 探索测试

请参考：[应用探索测试](<../../../../../../harmonyos-guides/应用测试/专项测试/DevEco Testing/探索测试/exploratory-testing.md#section12324184817324>)。
