---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-app-analyzer-testing
title: 导入DevEco Testing的检测报告进行诊断
breadcrumb: 指南 > 编写与调试应用 > 开发自测试 > 应用与元服务体检 > 导入DevEco Testing的检测报告进行诊断
category: harmonyos-guides
scraped_at: 2026-06-11T15:30:04+08:00
doc_updated_at: 2026-04-30
content_hash: sha256:9c879cc4a11f329d603046713c1ebc4af44be9bba296e921933e24e2886ce312
---
从DevEco Studio 6.0.0 Beta3版本开始，支持在DevEco Testing中进行性能相关测试生成检测报告后，导入到AppAnalyzer进行诊断和分析，获得可能的故障原因并生成体检报告。

## 前置操作

体检前，请先在DevEco Testing中测试并导出检测报告，具体操作方式请参考[性能基础质量测试](<../../../../应用测试/专项测试/DevEco Testing/专项测试/specialized-testing.md#section12324184817324>)或[场景化性能测试](<../../../../应用测试/专项测试/DevEco Testing/专项测试/specialized-testing.md#section8642101711299>)。

## 进行体检

说明

由于DevEco Testing和AppAnalyzer在检测能力、检测方法以及场景识别上存在差异，所以通过DevEco Testing检测并导入AppAnalyzer诊断和直接通过AppAnalyzer检测并诊断，检测和诊断结果会出现不一致的情况。

### DevEco Studio 6.0.1 Beta1及以上版本

1. 点击菜单栏**Tools >** **AppAnalyzer**，打开AppAnalyzer页面，点击底部**体检历史**按钮，点击右上角的**导入报告**按钮，根据界面提示，确保即将导入的检测报告满足相关要求。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e7/v3/_qnDuKPYTEmOYbRotciLrg/zh-cn_image_0000002602066197.png?HW-CC-KV=V1&HW-CC-Date=20260611T073003Z&HW-CC-Expire=86400&HW-CC-Sign=B23132A39465159A2433A5B2B26D3CCD932B89E55E4E4343A2829A6BCF5EC1C5)
2. 选择从DevEco Testing导出的报告（zip文件），点击**OK**后，等待AppAnalyzer导入数据并对问题进行诊断分析。AppAnalyzer仅支持对DevEco Testing中的部分指标进行诊断，具体请参考[检测指标](ide-app-analyzer-testing.md#section16156317171913)。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/92/v3/TVT8PDgVTLS2taJUjdnGPw/zh-cn_image_0000002571387084.png?HW-CC-KV=V1&HW-CC-Date=20260611T073003Z&HW-CC-Expire=86400&HW-CC-Sign=1A60B30DFC8AA756924F66D52B8F5E4CC4F9E1F3F7A73EAB439C615070E87D70)
3. 诊断完成后，查看测试报告如下。
   * **源文件、调优文件（包含trace文件和调用栈文件）或snapshot文件、时间戳等**：点击源文件可跳转到问题源码，点击调优文件或snapshot文件支持直接拉起性能分析工具Profiler并导入性能检测的问题数据进行调优分析，点击时间戳可以打开Profiler并定位到问题发生的时间范围。
   * **分析文档**：点击链接可跳转至官网文档，参考文档对检测出来的问题进行分析。
   * **优化建议**：针对可能的故障原因，给出对应的最佳实践，点击链接可跳转至官网文档。

   从DevEco Studio 6.0.2 Beta1版本开始，如果在体检中遇到问题，可点击报告右上角的**User Feedback**向我们反馈。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2d/v3/Aq15M5-FT3KBryc4ReAQpw/zh-cn_image_0000002571387082.png?HW-CC-KV=V1&HW-CC-Date=20260611T073003Z&HW-CC-Expire=86400&HW-CC-Sign=044633D2E14A62B9885D99E381A3D24B25486B9CF2D80C12983462A892E2F050)

### DevEco Studio 6.0.1 Beta1以下版本

1. 点击菜单栏**Tools >** **AppAnalyzer**，打开AppAnalyzer页面，点击底部**历史记录**按钮，进入历史记录页面。
2. 点击右上角的**检测报告导入**按钮，首次测试时，请根据AppAnalyzer的指引，下载Python及三方库，并根据界面提示，确保即将导入的检测报告满足相关要求。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/df/v3/VDzUnCs3ROaa0kGdSZmgFQ/zh-cn_image_0000002602066199.png?HW-CC-KV=V1&HW-CC-Date=20260611T073003Z&HW-CC-Expire=86400&HW-CC-Sign=7D2FECE1CE97F2BC07674E926FF41C10F5115DFBFCF5541F5B4B18346AFED3AE)
3. 选择从DevEco Testing导出的报告（zip文件），点击**确认**后，等待AppAnalyzer导入数据并对问题进行诊断分析。AppAnalyzer仅支持对DevEco Testing中的部分指标进行诊断，具体请参考[检测指标](ide-app-analyzer-testing.md#section16156317171913)。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2f/v3/pdxPw-jMRSSyTHtmdtaqkA/zh-cn_image_0000002602186257.png?HW-CC-KV=V1&HW-CC-Date=20260611T073003Z&HW-CC-Expire=86400&HW-CC-Sign=B45D829B3D9310047A1527D57C2DF436BBC634F2BBC4709E7C33C96A6C2723B9)
4. 诊断完成后，查看测试结果如下。
   * 测试报告：测试结果的汇总信息，点击**详情链接**可跳转到对应场景的详情报告。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/46/v3/dgS7tDVcT46JGJ6zIdRRUA/zh-cn_image_0000002602186251.png?HW-CC-KV=V1&HW-CC-Date=20260611T073003Z&HW-CC-Expire=86400&HW-CC-Sign=E609091F8824336C9855F21B1A01E5B64CC59D0BDD943B0C6615B74F565125D2)
   * 详情报告：给出详细的测试结果、可能的故障原因和对应的优化建议。
     + **开始/结束页面、时间戳、调优文件（包含trace文件和调用栈文件）或snapshot文件等**：点击开始/结束页面可跳转到问题源码，点击时间戳可以打开性能分析工具Profiler并定位到问题发生的时间范围，点击调优文件或snapshot文件支持直接拉起Profiler并导入性能检测的问题数据进行调优分析。
     + **分析文档**：点击链接可跳转至官网文档，参考文档对检测出来的问题进行分析。
     + **优化建议**：针对可能的故障原因，给出对应的最佳实践，点击链接可跳转至官网文档。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c7/v3/vzn9NvFoTHiRQ0Q7cXnNgw/zh-cn_image_0000002571546722.png?HW-CC-KV=V1&HW-CC-Date=20260611T073003Z&HW-CC-Expire=86400&HW-CC-Sign=2C6A53B8BFD6BD9DFC1A55D08E7324A67DDF32A325ACE6800849BC93BDC820F4)

   说明

   由于DevEco Testing和AppAnalyzer在检测能力、检测方法以及场景识别上存在差异，所以通过DevEco Testing检测并导入AppAnalyzer诊断和直接通过AppAnalyzer检测并诊断，检测和诊断结果会出现不一致的情况。

## 检测指标

AppAnalyzer会将DevEco Testing测试用例的操作归类为以下场景，仅支持对部分指标进行诊断，具体如下。

| 场景 | 检测指标 |
| --- | --- |
| 页面间转场 | 点击响应时延 |
| 点击完成时延 |
| 转场卡顿率 |
| 页面滑动 | 滑动响应时延 |
| 滑动卡顿率 |
| 冷启动 | 完成时延 |
| 页面内转场 | 滑动响应时延 |
| 点击响应时延 |
| 点击完成时延 |
| 滑动卡顿率 |
| 起播时延 |
