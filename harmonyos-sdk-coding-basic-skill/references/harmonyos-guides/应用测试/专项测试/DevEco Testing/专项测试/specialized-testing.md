---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/specialized-testing
title: 专项测试
breadcrumb: 指南 > 应用测试 > 专项测试 > DevEco Testing > 专项测试
category: harmonyos-guides
scraped_at: 2026-06-11T15:32:58+08:00
doc_updated_at: 2026-04-28
content_hash: sha256:f0ed48f8dee0392c72c0b1909a1a0caa9ee1cfc36d556ec125e0785fcb2e5fa4
---
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c8/v3/Y1g35nk4R0KStk7-pQ01TA/zh-cn_image_0000002503713790.png?HW-CC-KV=V1&HW-CC-Date=20260611T073255Z&HW-CC-Expire=86400&HW-CC-Sign=CC7A84263ED8568232391460BE7D3CACACF361607CE56E199E31DE4742FD9F0B "点击放大")

## 性能基础质量测试

**性能基础质量测试：**基于应用性能测试标准，提供了一套包含智能遍历算法和性能指标分析的解决方案，用于评估应用性能。该测试服务通过模拟用户操作行为，对应用进行长时间、高频次的页面遍历，实时采集性能数据，并生成全面、专业的测试报告。

应用的设计、开发及测试过程中推荐参考[应用性能体验建议](../../../../应用体验建议/应用性能体验建议/performance-experience-suggestions.md)。

**服务使用场景：**

用户在进行整包性能评估测试时，可以使用本服务通过指定应用启动次数与遍历操作时长，对应用进行性能测试。

**检测能力**：

性能基础质量测试提供了响应时延、完成时延、卡顿、音视频和黑白块五大类性能指标的检测能力，具体如下：

|  |  |  |  |
| --- | --- | --- | --- |
| **指标类型** | **指标名称** | **单位** | **指标说明** |
| 响应时延 | 点击响应时延 | 毫秒 | 时间起点：点击离手；  时间终点：界面发生变化。 |
| 响应时延 | 滑动响应时延 | 毫秒 | 时间起点：手指滑动；  时间终点：界面发生变化。 |
| 完成时延 | 加载完成时延 | 毫秒 | 时间起点：应用首页铺满全屏；  时间终点：应用首页所有占位符加载完成。 |
| 完成时延 | 点击完成时延 | 毫秒 | 时间起点：点击离手；  时间终点：转场页面所有占位符加载完成。 |
| 卡顿 | 最大丢帧 | 次 | 动效时间内，连续丢失的最大帧数。 |
| 卡顿 | 卡顿率 | 毫秒/秒 | 动效时间内，累计丢帧时间/动效时长。 |
| 音视频 | 起播时延 | 毫秒 | 时间起点：点击或滑动离手；  时间终点：视频播放首帧。 |
| 音视频 | 视频卡顿 | 次 | 视频播放过程中的卡顿情况，卡顿时长大于100ms视为1次卡顿。 |
| 黑白块 | 启动白屏时长 | 毫秒 | 时间起点：启动动效开始；  时间终点：启动过程中白屏消失。 |
| 黑白块 | 滑动占位符加载指数 | 毫秒/秒 | 页面滑动过程中占位符存在的累计时间。 |

**创建任务**

打开DevEco Testing客户端-专项测试-性能基础质量测试卡片，在任务创建界面按需配置任务参数，点击创建任务后开始测试。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8/v3/92aeY_1URQ-ADrXrlWBpjw/zh-cn_image_0000002524503459.png?HW-CC-KV=V1&HW-CC-Date=20260611T073255Z&HW-CC-Expire=86400&HW-CC-Sign=0E3E54B1D79D3D0CA4498F2B5C417D9D30D4FEC72DAB2CA914892DA47A8646A9 "点击放大")

性能基础质量测试支持选择已安装的应用，或选择待测应用的安装包后进行测试。

说明

应用支持情况说明：

* 冷启动测试：支持所有应用。
* 应用内操作测试：遍历目前主要支持以下应用类型：
  + ArkUI原生控件（含ReactNative框架开发）应用。
  + 使用Flutter3.7.12及之后版本开发的应用。
  + 除以上支持的应用类型，其他三方自研框架的自定义控件暂不支持。

（1）已安装的应用

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0/v3/dZYhi-jaSgCSIxi6kJbQoA/zh-cn_image_0000002492343774.png?HW-CC-KV=V1&HW-CC-Date=20260611T073255Z&HW-CC-Expire=86400&HW-CC-Sign=C9956C400FB79499B9F02BF560FE01E268FF7739BE0FA58E4F726D2BBE1C7E95 "点击放大")

（2）安装新的应用

点击按钮，在弹窗中选择应用安装包，支持.hap、.zip格式安装包。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b8/v3/h_--FWghSRqAp4sAfJYznw/zh-cn_image_0000002524623413.png?HW-CC-KV=V1&HW-CC-Date=20260611T073255Z&HW-CC-Expire=86400&HW-CC-Sign=CE0804CD5DAEFFF2F5370BDE0DAC967E833C62D4F4744B8BF928D853EF28ED1B "点击放大")

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/63/v3/HmeTDHiHSsafE2CI8SriUw/zh-cn_image_0000002492343792.png?HW-CC-KV=V1&HW-CC-Date=20260611T073255Z&HW-CC-Expire=86400&HW-CC-Sign=7B9DD9D2F7E6EDA19372BC8AD36F39F22D9D175D90F37DB2AB4991E50DAFE714 "点击放大")

**启动测试次数**

执行冷启动操作的次数，自动化测试过程中会重复执行应用冷启动和退出操作，用来评估应用启动的性能。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8f/v3/uSangE4KQVSrPjES2adYRQ/zh-cn_image_0000002492503686.png?HW-CC-KV=V1&HW-CC-Date=20260611T073255Z&HW-CC-Expire=86400&HW-CC-Sign=8C3AEC8EC27C20431EB949C4C789025FAEFDD125858F88EAF1F89F7510988121)

**遍历时长**

应用内点击、滑动等操作的总执行时长，用户可根据需求自定义遍历时长，默认为1小时，最大支持120分钟。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/44/v3/aX-wdV6iTvKEwECMLjmRZA/zh-cn_image_0000002524503423.png?HW-CC-KV=V1&HW-CC-Date=20260611T073255Z&HW-CC-Expire=86400&HW-CC-Sign=250963CCF0CAA5357B70B0C1B1C54E9CC17C625AF422B356F362C21BB4853CA8 "点击放大")

**高级配置**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1f/v3/HkFS0zVTQFixgcoC1e0x0g/zh-cn_image_0000002524503461.png?HW-CC-KV=V1&HW-CC-Date=20260611T073255Z&HW-CC-Expire=86400&HW-CC-Sign=5963F5886049693E6D56706C8C53228790A13D887F246C10F88A1471EFEFBCBA)

**检测标准**

检测基于用户体验分为三个标准，分别为：

* 极优体验：操作体验快速、流畅，发现更多的性能体验问题（磁盘空间占用会增加)，可选项。
* 较好体验：操作体验良好，发现可感知的性能体验问题，默认选项。
* 一般体验：操作体验较差，发现感知明显的性能体验问题，需重点关注，默认选项。

**指标监控**

自动化遍历执行过程中，被测设备的系统资源指标项采集，当前支持采集CPU、内存、温度、网络、GPU、存储和电量，固定采集CPU和内存，用户自行选择是否采集其他指标项。

**其他配置**

* 后台负载测试：开启后会在自动化遍历结束后，让应用进入后台，采集应用在后台状态下的CPU负载和内存占用，默认采集。
* 保存全部数据：开启后会保存自动化测试过程中产生的所有视频、trace、图片等数据，关闭后只保存影响体验操作的步骤数据。
* 生成IDE分析文件**：**开启后会将报告中的性能问题压缩打包，压缩包可导入 DevEco Studio 的体检工具，进行问题诊断并给出修改建议。

**测试执行**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b6/v3/6P4CZU_8TtSmvtv7fcOWfA/zh-cn_image_0000002535546833.png?HW-CC-KV=V1&HW-CC-Date=20260611T073255Z&HW-CC-Expire=86400&HW-CC-Sign=FF0DA51040F4FC5456F953B6F026CF96EF0124F2F91742FB9B0CB947702A6F02 "点击放大")

**①：**实时显示任务的整体进度。

**②/③****：**实时显示每个用例的执行状态和分析状态。

**④：**实时打印任务执行时的日志。

**查看报告**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/eb/v3/IeknnBnBTlu9gfeDnRqIiw/zh-cn_image_0000002492343780.png?HW-CC-KV=V1&HW-CC-Date=20260611T073255Z&HW-CC-Expire=86400&HW-CC-Sign=035026F8BAAAE58320F22C0A0AA6C85DDCFAF92C593E31512613EC158286D616 "点击放大")

**基础信息**

* 任务数据：任务名称、开始时间、持续时间、执行人。
* 应用数据：应用包名、应用版本、API版本。
* 备注：备注信息支持自定义修改。
* 环境参数：支持查看任务下发的参数以及被测设备的详细信息。
* 执行日志：支持查看任务执行过程中的日志，支持日志级别的筛选。
* 打开目录：点击打开任务数据文件夹。

**整体评估**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/17/v3/3M_dtMhASWGeffWJQOfpNw/zh-cn_image_0000002524503443.png?HW-CC-KV=V1&HW-CC-Date=20260611T073255Z&HW-CC-Expire=86400&HW-CC-Sign=783C238A9E6AC73102D8391E10C04F40ABA50622F8B940F4706D98F9C3430A97 "点击放大")

整体评估报告部分会展示本次的测试结论，包括如下部分：

* 测试结论：描述本次测试的结论，包括遍历时长、执行操作次数、发现问题数。
* 报告对比：一键跳转到性能测试报告对比工具，从概览、指标达标率等多维度进行报告对比。
* 性能报告自动分析：一键跳转到性能报告自动分析服务，对该报告中发现的问题进行自动分析。
* 导出IDE体检文件：支持生成体检文件导入到DevEco Studio中进行问题分析定位。详细操作指导请查看[导入DevEco Testing的检测报告进行诊断](<../../../../编写与调试应用/开发自测试/应用与元服务体检/导入DevEco Testing的检测报告进行诊断/ide-app-analyzer-testing.md>)。
* 问题分布环形图：呈现本次任务发现的总问题数以及各指标性能问题的分布情况。
* 操作类型和问题表单：统计遍历过程中，启动、点击、滑动、观看的操作次数，以及对应指标发现的问题数。
* 一般体验：为了帮助提前识别可能影响应用日常使用的性能体验问题，将所有体验问题进行过滤，聚焦于明显影响用户体验的严重问题，问题数会比所有体验问题少。
* 较好体验和极优体验：为了追求极致性能体验，这两种体验问题的标准比一般体验的标准更严格，上报的问题也会更多，用户可以根据实际情况解决问题。

整体评估表格中的红色数字表示当前体验标准下的问题次数，支持点击查看问题步骤列表。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e0/v3/WUVnzc70SEuhK1802ozgfA/zh-cn_image_0000002492503740.png?HW-CC-KV=V1&HW-CC-Date=20260611T073255Z&HW-CC-Expire=86400&HW-CC-Sign=2127B8716BB11EFD3B5A0868B29441472D5932B8C1DF67E9D9A70788AED16890 "点击放大")

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/82/v3/p1FdbDPPRX-uqDpBtFh3PA/zh-cn_image_0000002492343768.png?HW-CC-KV=V1&HW-CC-Date=20260611T073255Z&HW-CC-Expire=86400&HW-CC-Sign=FFB988187A34C12B87A20D7FFF35980D34A9A2C301E5BF2768E82EA18825CAC7 "点击放大")

* 维测数据：点击打开按钮，自动打开该操作的数据文件夹，汇总当前操作的trace、视频、图片等维测数据，协助用户进行问题定位。
* 查看详情：点击展开按钮，呈现该操作的帧图片集，点击视频时间数字，能直接定位到具体的图片。

**遍历统计**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b0/v3/3qf4uQywRHqzTREUoRt36Q/zh-cn_image_0000002492503764.png?HW-CC-KV=V1&HW-CC-Date=20260611T073255Z&HW-CC-Expire=86400&HW-CC-Sign=35285F81C42E7C5FA23E212206F0A99FB5665063BDF48806B6F49A75F51B698C "点击放大")

**遍历统计会展示应用遍历过程中的操作步骤信息，包括如下信息：**

* 遍历时长：用户在任务创建时指定的遍历时间。
* 启动次数：用户在任务创建时指定的启动测试次数。
* 点击次数：应用遍历过程中，点击操作的总次数。
* 滑动次数：应用遍历过程中，滑动操作的总次数。
* 观看视频：应用遍历过程中，观看视频操作的总次数。
* 图片列表：展示遍历的操作过程。

**资源数据**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f1/v3/5IE65YqwQKiQCSCyZkeadQ/zh-cn_image_0000002492503770.png?HW-CC-KV=V1&HW-CC-Date=20260611T073255Z&HW-CC-Expire=86400&HW-CC-Sign=CC8EB91DF07F8BA4A834366DBFE752922BAF616AB63D7CF866D562C1EBBA2F58 "点击放大")

资源数据报告部分呈现的是应用在遍历过程中的资源占用情况。

* CPU和内存占用是默认采集，GPU、网络、电量和温度为可选项，可在任务创建页面“高级配置”中勾选。
* 后台CPU和内存的测试需要在任务创建页面打开“后台负载测试”开关，检测应用在后台时，CPU和内存资源的占用情况。
* 峰值步骤：展示当前系统资源指标的最大值，点击可跳转至对应的步骤详情。

**操作详情**

操作详情展示遍历测试过程中的操作步骤信息，整体呈现内容如下所示：

* 应用启动测试：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/95/v3/0IfQljy0TEqNvhcYzfjSvg/zh-cn_image_0000002503552638.png?HW-CC-KV=V1&HW-CC-Date=20260611T073255Z&HW-CC-Expire=86400&HW-CC-Sign=D9729206E278462ED9CA89FACBF1C2F652D4E95BD7A0BBCE6605E0EA1D551721 "点击放大")

展示应用启动测试的步骤信息，包括操作前后截图、测试数据以及维测数据。

操作前&操作后：展示该步骤操作前后的设备截图。

指标项：展示应用启动过程的指标检测结果信息，如果测试值超标，字体标红显示，支持点击查看问题详情。若不涉及，则显示”-”。

维测数据：点击打开按钮，自动打开该操作的数据文件夹，汇总当前操作的trace、视频、图片等维测数据，协助用户进行问题定位。若该步骤所有测试数据都达到标准，则不展示打开按钮。

* 应用内遍历测试：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1/v3/FCBhqpF_QPCJXeKJSs0yLw/zh-cn_image_0000002503712596.png?HW-CC-KV=V1&HW-CC-Date=20260611T073255Z&HW-CC-Expire=86400&HW-CC-Sign=CCD100CDA62C9B0851120EED51A8615CD30C4194B5F165D7E2BC14B3CCCAB152 "点击放大")

展示应用内进行遍历操作的步骤信息，包括操作前后截图、测试数据以及维测数据。

操作前&操作后：展示该步骤操作前后的设备截图。

指标项：展示应用启动过程的指标检测结果信息，如果测试值超标，字体标红显示，支持点击查看问题详情。若不涉及，则显示”-”。

维测数据：点击打开按钮，自动打开该操作的数据文件夹，汇总当前操作的trace、视频、图片等维测数据，协助用户进行问题定位。若该步骤所有测试数据都达到标准，则不展示打开按钮。

* **异常指标信息查看：**

对于超标的检测结果，可以通过点击超标项，查看该步骤的详细信息，展示内容如下图所示（以响应时延为例）。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/82/v3/WYlwnpX-To2kt2uoaJgghQ/zh-cn_image_0000002492343720.png?HW-CC-KV=V1&HW-CC-Date=20260611T073255Z&HW-CC-Expire=86400&HW-CC-Sign=5ABE206368F92EA449E277369C9057A7545421D75D820FB092A853008A87E2D9 "点击放大")

测试值：表示该步骤的响应时延测试值。

开始时间：表示用户从122这一帧开始操作。

结束时间：表示应用UI在255这一帧开始响应。

图片组：逐帧展示该步骤的操作视频。

**问题定位定界**

**维测数据**

点击打开按钮跳转到问题步骤对应的资源文件目录。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6d/v3/JUy_gtPyRDS4UCXdj6IgbQ/zh-cn_image_0000002524623399.png?HW-CC-KV=V1&HW-CC-Date=20260611T073255Z&HW-CC-Expire=86400&HW-CC-Sign=A4207CDCEC66C52E6E6DF02262EF9A8C82ABA7B1ED9A03ABB3444B6C52FEE644 "点击放大")

用户可查看步骤执行全过程的图片和视频，如下所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/07/v3/iYmr_aHTTqOF8WCPPZnUDw/zh-cn_image_0000002492503752.png?HW-CC-KV=V1&HW-CC-Date=20260611T073255Z&HW-CC-Expire=86400&HW-CC-Sign=82373952AD52A98E0097468560FBE20D9CFEA60F81D367B5FBAA3B4B94EE6325 "点击放大")

**perfdata数据**

可使用[DevEco Studio](https://developer.huawei.com/consumer/cn/download/deveco-studio) 5.0.3.300及以上版本中的场景化调优工具DevEco Profiler打开及查看该文件，内含步骤执行过程中的trace打点和调用栈信息，也可使用压缩软件解压为单个的trace文件和调用栈文件，解压后的文件可使用[SmartPerf](https://gitcode.com/openharmony/developtools_smartperf_host)工具打开。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/38/v3/o8M804HxSyGbETYn30CGGQ/zh-cn_image_0000002492343718.png?HW-CC-KV=V1&HW-CC-Date=20260611T073255Z&HW-CC-Expire=86400&HW-CC-Sign=FE006C3F6417F5A86B35F1DFE7E4D2B10B729ADDAB811186B4903750F6C7C8BD "点击放大")

说明

更多测试服务详情，请前往DevEco Testing客户端->专项测试->性能基础质量测试->任务创建页->测试指南中查询。

更多应用性能优化建议及问题定位，请查阅：[应用性能体验建议](../../../../应用体验建议/应用性能体验建议/performance-experience-suggestions.md) 及 [最佳实践-性能-性能场景优化案例](../../../../../best-practices/性能/性能场景优化案例/bpta-scenario-performance-optimization.md)。

## 场景化性能测试

**服务说明**

场景化性能测试服务提供了一套包含自动化脚本执行和性能指标分析的解决方案，涵盖响应时延、完成时延、卡顿、音视频和黑白块五大类性能指标的检测。

应用的设计、开发及测试过程中推荐参考[应用性能体验建议](../../../../应用体验建议/应用性能体验建议/概述/performance-overview.md)。

**服务使用场景**

支持一键式测试应用的关键场景和核心路径的性能体验。通过任务报告，用户可查看关键场景上的多维度性能指标表现，精准识别性能体验问题。

注意

**场景化性能测试的性能指标检测能力****与性能基础质量测试一致；详情请查看[性能基础质量测试](specialized-testing.md#section12324184817324)。**

**脚本写作**

请参考[自定义性能脚本测试（基于Python)](../../../单元测试和UI测试/自定义性能脚本测试（基于Python）/hypium-perf-python-guidelines.md)。

**任务创建：**

打开DevEco Testing客户端-专项测试-场景化性能测试卡片，在任务创建界面按需配置任务参数，点击创建任务后开始测试。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cf/v3/29KYjc4cSfGztMPIrUPAAg/zh-cn_image_0000002492352024.png?HW-CC-KV=V1&HW-CC-Date=20260611T073255Z&HW-CC-Expire=86400&HW-CC-Sign=FF2FFFF4BD93343C27E3CE1262CD868F1AA7670575B1A485EFF5EE6B6F472957 "点击放大")

**配置项说明**

**执行轮次**

用例可重复执行多轮提升测试结果的可靠性，最多测试10轮。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e5/v3/JcZeSH_gR666vGbeNbn1rg/zh-cn_image_0000002524511721.png?HW-CC-KV=V1&HW-CC-Date=20260611T073255Z&HW-CC-Expire=86400&HW-CC-Sign=EE18E82D9A964CED2E3AB5AAAFF83FEA66EF45B53346CE1E25CF01315AC2F93E)

**用例工程路径**

存放自动化用例的工程路径。

如果已有用例脚本，可点击创建工程模板，将脚本文件存放到工程根目录的testcases目录下，用例工程路径请选择工程根目录。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/98/v3/B0npeeXaSRCK3x39pSj7zw/zh-cn_image_0000002492511990.png?HW-CC-KV=V1&HW-CC-Date=20260611T073255Z&HW-CC-Expire=86400&HW-CC-Sign=3923566A45213EE8A8728C492912624235E3225F9214E34FCE77AA4D7955D721)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d0/v3/C_CcBtICTZeTNTjoASREdg/zh-cn_image_0000002524631695.png?HW-CC-KV=V1&HW-CC-Date=20260611T073255Z&HW-CC-Expire=86400&HW-CC-Sign=73737B04D7EF155B4DD44BC77562A275C5404B19FBF89819229CB95F0CCC3E02)

**高级配置**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/14/v3/9oNgOmpqSyyx4Yap9qvvlA/zh-cn_image_0000002492352026.png?HW-CC-KV=V1&HW-CC-Date=20260611T073255Z&HW-CC-Expire=86400&HW-CC-Sign=05538162E4A5DEAD9001BF32E34E7947019A6C689FC6398E6847579AFA2C4C93 "点击放大")

**检测标准、****指标监控**

与性能基础质量测试一致，可点击[性能基础质量测试](specialized-testing.md#section12324184817324)查看。

**其他配置**

保存全部数据：开启后会保存自动化测试过程中产生的所有视频、trace、图片等数据，关闭后只保存影响体验操作的步骤数据。

生成IDE分析文件：开启后会将报告中的性能问题压缩打包，压缩包可导入 DevEco Studio 的体检工具，进行问题诊断并给出修改建议。

**任务执行**

所有用例按照顺序和轮次依次执行，并行分析；任务完成后，会自动生成报告页面。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7f/v3/JuLUpHxXSIutkYjZfVFlgQ/zh-cn_image_0000002524511723.png?HW-CC-KV=V1&HW-CC-Date=20260611T073255Z&HW-CC-Expire=86400&HW-CC-Sign=E398AD653D753AA93CDA932A00E4DF1B38E8C9CAFD709ED0EDED299D7690A6AC "点击放大")

①：实时显示任务的整体进度。

②/③：实时显示每个用例的执行状态和分析状态。

④：实时打印任务执行时的日志。

**查看报告**

测试完成后，自动生成测试报告。报告包含基础信息、整体评估、资源数据、用例详情等。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3e/v3/xt7PEu9mSXuDya51ExCx2w/zh-cn_image_0000002492511992.png?HW-CC-KV=V1&HW-CC-Date=20260611T073255Z&HW-CC-Expire=86400&HW-CC-Sign=3D9844A4A43C814D3D4C85192D39947D06E3EC2A9479CC438CA262C734719A34 "点击放大")

**基础信息**

任务信息：任务名称、工程路径、开始时间、持续时间、执行人。

备注：备注信息支持自定义修改。

环境参数：支持查看任务下发的参数以及被测设备的详细信息。

执行日志：支持查看任务执行过程中的日志，支持日志级别的筛选。

打开目录：点击打开任务数据文件夹。

**整体评估**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/61/v3/8eaW6lvJS3eZbmn5V7Qm7g/zh-cn_image_0000002524631697.png?HW-CC-KV=V1&HW-CC-Date=20260611T073255Z&HW-CC-Expire=86400&HW-CC-Sign=2A1FE8495D51FDFD0087CABFB9C7FE6930AE5F266930FC59DD8839236493AB7B "点击放大")

整体评估包括如下部分：

* 测试结论：描述本次测试的结论，包括执行用例个数、轮数、操作次数及发现问题数。
* 报告对比：一键跳转到报告对比工具，从概览、指标优劣化、用例对比详情等多维度进行报告对比。
* 性能报告自动分析：一键跳转到性能报告自动分析服务，对该报告中发现的问题进行自动分析。
* 导出IDE体检文件：支持生成体检文件导入到DevEco Studio中进行问题分析定位。详细操作指导请查看[导入DevEco Testing的检测报告进行诊断](<../../../../编写与调试应用/开发自测试/应用与元服务体检/导入DevEco Testing的检测报告进行诊断/ide-app-analyzer-testing.md>)。
* 问题分布环形图：呈现本次任务发现的总问题数以及各指标性能问题的分布情况。
* 用户场景和问题分布表单：执行状态表示用例场景多轮执行的状态，用例场景展示的是脚本中定义的场景用例名称，后面几列为对应指标发现的问题数。
* 一般体验：为了帮助提前识别可能影响应用日常使用的性能体验问题，将所有体验问题进行过滤，聚焦于明显影响用户体验的严重问题，问题数会比所有体验问题少。
* 较好体验和极优体验：为了追求极致性能体验，这两种体验问题的标准比一般体验的标准更严格，上报的问题也会更多，用户可以根据实际情况对应用进行优化。

**执行状态共有如下几种：**

* 成功：用例所有轮次均执行成功。
* 部分成功：用例部分轮次执行成功，部分轮次失败或者未执行。
* 失败：用例无成功执行轮次。
* 未执行：用例未执行。

整体评估表格中的红色数字是当前体验标准下的问题次数，支持点击查看问题步骤列表：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a0/v3/GTEB4KJNTM-3r_SyqD6fkQ/zh-cn_image_0000002492352028.png?HW-CC-KV=V1&HW-CC-Date=20260611T073255Z&HW-CC-Expire=86400&HW-CC-Sign=34D671464C0877D2FD0EB658F8558FCB42016CF214B1BB96DB68C96A6806172C)

展开后呈现问题的详细信息：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/85/v3/Rrhm-050Th6D_9kfbD5MVg/zh-cn_image_0000002524511725.png?HW-CC-KV=V1&HW-CC-Date=20260611T073255Z&HW-CC-Expire=86400&HW-CC-Sign=DF21667F843D3ADF71E84199077F3B016FE75D24A97012B5172684D1AECB538B "点击放大")

维测数据：点击打开按钮，自动打开该操作的数据文件夹，汇总当前操作的trace、视频、图片等维测数据，协助用户进行问题定位。

查看详情：点击展开按钮，呈现该操作的帧图片集，点击视频时间数字，能直接定位到具体的图片。

**资源数据**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a5/v3/Eh952N1aT62bQgeoSTUEpg/zh-cn_image_0000002492511994.png?HW-CC-KV=V1&HW-CC-Date=20260611T073255Z&HW-CC-Expire=86400&HW-CC-Sign=CE7DA1C194ADBB38FB8FB323523CFE808216CB6984A002395E173F216515BDD1 "点击放大")

资源数据报告部分呈现的是应用在遍历过程中的资源占用情况。

* CPU和内存占用是默认采集，GPU、网络、电量和温度为可选项，可在任务创建页面“高级配置”中勾选。
* 峰值步骤：展示的是当前系统资源指标的最大值，点击可跳转至对应的步骤详情。

**用例详情**

用例详情会展示用例的执行轮次和执行步骤的信息，整体呈现内容如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/67/v3/MXLDT3IzQauBmHip3RZDkw/zh-cn_image_0000002524631699.png?HW-CC-KV=V1&HW-CC-Date=20260611T073255Z&HW-CC-Expire=86400&HW-CC-Sign=295BA90C9056BA5F6BA569C7008B61A5CBF4228095C6D8DAB6E28B9E8A0417F6 "点击放大")

OH\_XXXX：代表用例名称，由脚本进行指定。

用例资源数据： 统计该用例在执行过程中采集到的CPU，内存等资源数据，并针对改用例进行数据汇总计算。

测试步骤：展示用例的步骤信息，默认展示该步骤在多轮测试中的测试数据，对于超过标准的测试值，数据标红显示，支持点击查看问题详情。对于该操作不涉及的指标，显示“-”。

点击步骤左侧的箭头，展开该步骤的详细轮次信息，如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c4/v3/4ksXGDzWQ32_TH9NzYyF-w/zh-cn_image_0000002492352030.png?HW-CC-KV=V1&HW-CC-Date=20260611T073255Z&HW-CC-Expire=86400&HW-CC-Sign=56427E86E65AC3856AAC3A1598F0B41E19490B731F76E0347133164DFCC02971 "点击放大")

操作前&操作后：展示该步骤操作前后的信息，用户可以通过前后截图了解操作的场景。

指标项：展示每轮的指标检测结果信息，如果测试值超标，字体标红显示，支持点击查看问题详情。若不涉及，则显示“-”。

维测数据：点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f2/v3/wTKaNEIVTXmU6ArcRHqslg/zh-cn_image_0000002524511727.png?HW-CC-KV=V1&HW-CC-Date=20260611T073255Z&HW-CC-Expire=86400&HW-CC-Sign=F68CA59411B14EA188C019E4F02D30F4DE522CCBD6EED8E5EF166E4BBD7A25AC) 按钮，自动打开该操作的数据文件夹，汇总当前操作的trace、视频、图片等维测数据，协助用户进行问题定位。若该步骤所有测试数据都达到标准，则不会出现该按钮。

对于超标的检测结果，可以通过点击超标项，查看该步骤的详细信息，展示内容如下图所示（以滑动占位符加载指数详情为例）：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d/v3/O3MWjk0TQH-EWZlzTHHBeQ/zh-cn_image_0000002492511996.png?HW-CC-KV=V1&HW-CC-Date=20260611T073255Z&HW-CC-Expire=86400&HW-CC-Sign=BB343ABFD1A704166F1EF7770F114A99BD874859A7BB435DF670043ED17EEA83 "点击放大")

开始时间：从3299这一帧开始，页面中出现占位符。

结束时间：在3465这一帧，占位符全部都加载完成。

图片组：逐帧展示该步骤的操作视频。

**问题定位定界**

**维测数据**

点击打开按钮可以跳转到问题步骤对应的资源文件目录。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/58/v3/Y7PJFwl3TKe2a6gl-PtnJw/zh-cn_image_0000002524631701.png?HW-CC-KV=V1&HW-CC-Date=20260611T073255Z&HW-CC-Expire=86400&HW-CC-Sign=1192C5D22420AE992DF65D5C655B136028ACDA1C6783A6BADAD54466F1EF5BF3 "点击放大")

测试步骤执行全过程的图片和视频如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b6/v3/i4RbuXjeRr-098_mo0XGtQ/zh-cn_image_0000002492352032.png?HW-CC-KV=V1&HW-CC-Date=20260611T073255Z&HW-CC-Expire=86400&HW-CC-Sign=2661E021BD20CE54A17315241FBC5B4AD7EFB5A5038E47B67E3BD9ED35C1E534 "点击放大")

**perfdata****数据**

可使用[DevEco Studio](https://developer.huawei.com/consumer/cn/download/deveco-studio) 5.0.3.300及以上版本中的场景化调优工具DevEco Profiler打开及查看该文件，内含步骤执行过程中的trace打点和调用栈信息，也可使用压缩软件解压为单个的trace文件和调用栈文件，解压后的文件可使用[SmartPerf](https://gitcode.com/openharmony/developtools_smartperf_host)工具打开。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2/v3/DujPrNPsQOOD6Cyx-3ZBhg/zh-cn_image_0000002524511729.png?HW-CC-KV=V1&HW-CC-Date=20260611T073255Z&HW-CC-Expire=86400&HW-CC-Sign=EF73EF9FCBA567201580B520B177BF031D5D63B10BE64F93B9F5AB91238EC6BA "点击放大")

说明

更多场景化性能测试报告解读及常见问题，请前往DevEco Testing客户端->专项测试->场景化性能测试->任务创建页->测试指南中查询。

更多应用性能优化建议及问题定位，请查阅：[应用性能体验建议](../../../../应用体验建议/应用性能体验建议/performance-experience-suggestions.md) 及 [最佳实践-性能-性能场景优化案例](../../../../../best-practices/性能/性能场景优化案例/bpta-scenario-performance-optimization.md)。

## 稳定性基础质量测试

**稳定性基础质量测试：**根据应用稳定性建议，检测应用运行过程中是否存在应用崩溃、资源过载、内存泄漏等异常情况。

**创建任务**

进入DevEco Testing客户端，在左侧菜单栏选择“专项测试”，点击“稳定性基础质量测试”服务卡片，即进入任务创建界面。用户按需配置任务参数，点击创建任务即开始测试。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3b/v3/CsqnjX9ERxeWnJRicCEjCg/zh-cn_image_0000002538034024.png?HW-CC-KV=V1&HW-CC-Date=20260611T073255Z&HW-CC-Expire=86400&HW-CC-Sign=FDC9BD5E261069D03EE787A1DD4AA51EAECC1655B6A00B7F201FF72EE3883B6D "点击放大")

任务名称：用于标识任务，工具会根据时间生成默认任务名，支持自定义修改。

备注信息：按需填写任务备注信息，便于快速筛选报告。

测试设备：选择一个待测设备和待测应用。系统版本支持 HarmonyOS 5.0及以上版本。

选择应用：可选择测试设备上已安装的应用；或安装新的应用，即在测试设备上安装新的应用包。

是否卸载应用：选择卸载应用后，测试时会进行卸载无残留检测，测试任务结束后将自动卸载被测应用。

是否开启多线程检测：打开后，系统支持检测应用多线程安全问题（例如：多个线程并发写入操作）。

是否开启[MemDebug](../../../../../best-practices/稳定性/稳定性检测/开发态稳定性检测/地址越界类问题检测/使用HWASan检测内存错误/bpta-stability-hwasan-detection.md#section10791454125320)模式：打开开关以后，会打开被测应用的内存越界检测开关，可以辅助发现和定位内存越界类问题。

说明

**稳定性基础质量测试最佳测试时长建议设置为8****小时**。

**控件黑名单**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e1/v3/Oc393zdWS5KQmgfk-gFn3w/zh-cn_image_0000002538194210.png?HW-CC-KV=V1&HW-CC-Date=20260611T073255Z&HW-CC-Expire=86400&HW-CC-Sign=C5316176A1AB0D0FEFF2DFE845A772D97D21CDD2B5ED9A13581E66B2A9ABAE36 "点击放大")

控件黑名单通过指定控件的关键字（控件感知语义或layout中控件text属性值）和控件Xpath进行正则匹配识别黑名单控件；黑名单控件在遍历中不会进行操作；屏蔽的黑名单控件在遍历过程中会在应用页面中置灰。

1、关键字：可以填写页面内可交互控件选框中的关键字，例如“购物车”、“我的订单”等。

2、XPath：可以通过Uiviewer工具或已有的遍历图谱文件获取控件的XPath。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/13/v3/p3xSBRttQu2Qna_0Po9xQQ/zh-cn_image_0000002568914377.png?HW-CC-KV=V1&HW-CC-Date=20260611T073255Z&HW-CC-Expire=86400&HW-CC-Sign=3EF74838A3DBC6BCCC9D92E3C724454EBB0BF059F80B41612687625456E69E67 "点击放大")

说明

**1、关于控件黑名单中“XPath”信息也可以通过探索测试报告中的遍历地图获取**：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b9/v3/tnqioOCfRI2VUUYrBCPgog/zh-cn_image_0000002569034393.png?HW-CC-KV=V1&HW-CC-Date=20260611T073255Z&HW-CC-Expire=86400&HW-CC-Sign=DEF773AD4CA62C90096624429CEB6C3497DC946BD8A633E5B99ADB0EDBB8260A "点击放大")

点击遍历地图中的关联线条；即可在右侧查看该跳转事件详情。

**测试执行**

创建任务后，将会跳转到执行页，进入测试环境初始化阶段。待测试环境初始化完成，待测应用被启动。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/42/v3/PHQuDhtFQOWnD28aomBZiw/zh-cn_image_0000002524503425.png?HW-CC-KV=V1&HW-CC-Date=20260611T073255Z&HW-CC-Expire=86400&HW-CC-Sign=B5E2D0ECD34246C07F706584580E24A1A751D52274FEF81FEF6C7007ACCBFA21 "点击放大")

测试过程中，在测试页面可以看到测试进度、检测状态、实时投屏及执行日志。

**查看报告**

测试完成后，自动生成测试报告。报告包含任务信息、结果统计、检测规则。

任务信息中，可查看当前应用信息、任务执行时长及详细的环境参数（配置信息及环境信息），点击打开目录按钮支持导出 html 的报告文件。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0c/v3/-5lhQ8FDQey9zHgeyoeE4A/zh-cn_image_0000002524503497.png?HW-CC-KV=V1&HW-CC-Date=20260611T073255Z&HW-CC-Expire=86400&HW-CC-Sign=D7208ED2343412C13C09A30BF737775B405C2C48D8C7F7C271A46811636A56B3 "点击放大")

测试概览中，包含结果统计及检测规则，可直观查看本次任务中，测试项检测结果。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1a/v3/KGZjun4kQ_CcPU8yt99lEw/zh-cn_image_0000002492503702.png?HW-CC-KV=V1&HW-CC-Date=20260611T073255Z&HW-CC-Expire=86400&HW-CC-Sign=34E9731F7D319C6EB6DEADD9DA1EB6CFA0333538302BB58C9486DEF5A7474C10 "点击放大")

检测不通过或检测异常的规则项，点击查看详情即可查看异常问题详情，包含检测项概览、测试截图、问题列表。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e2/v3/8AOyM0-oSrK6cCm1fo-EVQ/zh-cn_image_0000002492503694.png?HW-CC-KV=V1&HW-CC-Date=20260611T073255Z&HW-CC-Expire=86400&HW-CC-Sign=5812900906FABF3AFEFAE052A872FCB18B499354B368D408EE16A621EF18CDC2 "点击放大")

点击查看按钮，支持查看测试过程中的日志，用户可结合问题描述及日志详情进一步分析。

说明

更多测试服务详情，请前往DevEco Testing客户端->专项测试->稳定性基础质量测试->任务创建页->测试指南中查询。

更多应用稳定性体验优化建议及问题定位，请查阅：[应用稳定性体验建议](../../../../应用体验建议/应用稳定性体验建议/experience-suggestions-stability.md) 及 [CppCrash故障定位指导](https://developer.huawei.com/consumer/cn/doc/architecture-guides/common-v1_26-ts_c25-0000002324993158)

## 性能指标监控测试

**性能指标监控测试：**为用户提供指定业务场景性能测试能力，选择待测应用后手动操作应用，输出测试过程中应用和整机的性能指标数据。

**任务创建**

打开DevEco Testing客户端-专项测试-性能指标监控测试卡片，在任务创建界面按需配置任务参数，点击创建任务后开始测试。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/89/v3/Py8kxRWjQp6pmDsdp4P-Ig/zh-cn_image_0000002524623373.png?HW-CC-KV=V1&HW-CC-Date=20260611T073255Z&HW-CC-Expire=86400&HW-CC-Sign=0BD660976B04B92E6C92C913EB6E7A6C9396CEA7FD86CCD5AFBA413235DCEE4C)

任务名称：用于标识任务，根据时间生成默认任务名，支持自定义任务名称。

备注信息：按需填写任务备注信息，便于快速筛选报告。

测试设备：选择待测设备，待测设备的系统版本建议使用 HarmonyOS 5.0及以上版本。

选择应用：选择已安装在测试设备上的应用或安装新的应用。

指标监控：固定采集CPU和内存，用户自行选择是否采集其他指标项。

参数配置完成后，点击创建任务按钮开始测试。

**测试执行**

创建任务后，跳转到执行页，执行测试环境初始化操作。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0b/v3/gzf17TUxTAKuxnVYkV1Q_Q/zh-cn_image_0000002492503718.png?HW-CC-KV=V1&HW-CC-Date=20260611T073255Z&HW-CC-Expire=86400&HW-CC-Sign=87789BC461F8BA4B7DDE3601E3ECADCEA929D8CA58137B5FA4CC1FBC1BADE250 "点击放大")

等待测试环境初始化完成后，待测应用启动，自动跳转至监控页面，并启动监控，在手工测试场景准备好后，点击右上角的开始图标按钮，出现“开始采集”标识线，开始统计分析数据。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/36/v3/UnRfIQwkSRiOWflx5E5N3w/zh-cn_image_0000002524503453.png?HW-CC-KV=V1&HW-CC-Date=20260611T073255Z&HW-CC-Expire=86400&HW-CC-Sign=5AAB81FF8A6CD15CD345D2D09C3C1C15D3A2DDA4B6416CD35024F501786061AF "点击放大")

开始采集后，点击开始图标右侧的“记录”图标，可标识场景，并提示“场景开始”。待测场景结束后，再次点击，完成标识场景。概览中单独计算被标识的场景数据。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/18/v3/YQrWB42HSUu_aii0pk9T5w/zh-cn_image_0000002524503491.png?HW-CC-KV=V1&HW-CC-Date=20260611T073255Z&HW-CC-Expire=86400&HW-CC-Sign=0972E52F7D30A00B3C5B6E488E6471AC01E356152E7CCF8B071D92A106109A94 "点击放大")

在测试过程中，可随时点击“采集 trace”按钮，采集连续30 秒的 trace 信息，单次任务只保留最近10 个 trace 文件。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/51/v3/0OLmZAvsQkePOcxf0R3F6g/zh-cn_image_0000002524503479.jpg?HW-CC-KV=V1&HW-CC-Date=20260611T073255Z&HW-CC-Expire=86400&HW-CC-Sign=554B8BB7ED6E8822FA738DC3C71F8E1533A14189D94A46F4C2A0DB35C428520F "点击放大")

结束采集。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/14/v3/VkXkLk1qRyaZ1R0tjsvIKw/zh-cn_image_0000002492503708.jpg?HW-CC-KV=V1&HW-CC-Date=20260611T073255Z&HW-CC-Expire=86400&HW-CC-Sign=FA37DBF815BF8799C26B12E5EE30E5E40DF9ED0BE57142A437BD1D926CC2A075 "点击放大")

**查看报告**

测试报告包括：基本信息、环境参数、执行日志，打开目录及指标数据。

指标数据：包括 FPS、设备 CPU/GPU 的频率、负载监控等信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6c/v3/mJKdIwfbQkqOjwFxLWOOWA/zh-cn_image_0000002524503401.png?HW-CC-KV=V1&HW-CC-Date=20260611T073255Z&HW-CC-Expire=86400&HW-CC-Sign=4591CBC3A38549F0F80D9C90EAD18763DFBDB3FD711347A88954CDBE2A09A46E "点击放大")

指标数据介绍：

FPS：应用界面每秒刷新次数。

帧间隔：两帧画面刷新时间的间隔。帧间隔应保持稳定，并与应用帧率负相关。当帧间隔过大时， 设备会出现卡顿现象。

CPU 频率：各个 CPU 核心的实时频率。在 ARM 架构下，相同规格的核心实时频率一致（即大、中、小核分别具有不同的实时频率，但相同的核心的实时频率一致）。

内存占用：应用及整机的各个内存指标测试数据。

GPU 频率：GPU 核心的实时频率。

GPU 负载：GPU 的当前负载。

温度：设备的壳温，前壳温，后壳温，soc 温度。

网络速率：应用测试过程中的网络上下行速率。

Trace：可以通过报告底部的"打开Trace文件"按钮跳转到trace文件目录。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1/v3/yFz3dqIoTsy-O-XEkiVG6Q/zh-cn_image_0000002492503700.png?HW-CC-KV=V1&HW-CC-Date=20260611T073255Z&HW-CC-Expire=86400&HW-CC-Sign=7D190C4414D1E045753A6FF46D7CBB1B20EB6704BAB211335CBC15F65F859036 "点击放大")

说明

更多测试服务详情，请前往DevEco Testing客户端->专项测试->性能指标监控测试->任务创建页->测试指南中查询。

## UX基础质量测试

**UX基础质量测试：**根据应用UX建议，验证应用在基础体验、系统特性适配、控件布局等方面是否合理。

测试完成后，自动生成测试报告。UX基础质量测试报告如下：

报告包含任务信息、执行结果、检测规则。支持查看当前应用信息、任务执行时长，及详细的环境参数（配置信息及环境信息），支持导出 html 的报告文件。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d3/v3/EGAHmE3AQ-u4BV8vd-NPEQ/zh-cn_image_0000002524503465.png?HW-CC-KV=V1&HW-CC-Date=20260611T073255Z&HW-CC-Expire=86400&HW-CC-Sign=AC6638D67CE01F1E26DCFF99F5E04830D353824E882D8C8E3099D89E0F55A2D1 "点击放大")

对于检测不通过及检测异常的规则项，点击查看详情即可查看异常问题详情，包含检测项概览、测试截图、问题列表。对于异常问题，可根据测试截图、问题描述，针对性优化异常问题。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/84/v3/aWapHue4QbmLh7NgYCcbeg/zh-cn_image_0000002524503505.png?HW-CC-KV=V1&HW-CC-Date=20260611T073255Z&HW-CC-Expire=86400&HW-CC-Sign=EC8DF7003AB41D66C695A850B5A9EB4A9CD2C4751CB6062E98FFD8BFC76F7235 "点击放大")

说明

更多检测规则详情，请前往DevEco Testing客户端 ->专项测试 ->UX基础质量测试 ->任务创建页-测试指南中查询。

## 安全基础质量测试

**安全基础质量测试：**根据应用安全测试建议，评估应用基础安全，如组件安全、存储安全、配置安全、签名安全等。

测试完成后，会自动生成测试报告。报告包含任务信息、执行结果、问题统计、检测规则。任务信息中，可查看当前应用信息、任务执行时长以及详细的环境参数（配置信息及环境信息），支持导出 html 的报告文件。

安全基础质量测试报告如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b7/v3/lExVZumARryYYH2hprxcrQ/zh-cn_image_0000002492352192.png?HW-CC-KV=V1&HW-CC-Date=20260611T073255Z&HW-CC-Expire=86400&HW-CC-Sign=FE4A340E57CC6F94564E32EB7137D54CF1B6475D30B6D90BC0F04E0F37EBA03B "点击放大")

在测试报告中，包含执行结果、问题统计及检测规则。用户可直观查看本次任务中的测试项检测结果。

对于检测不通过的规则项，点击查看详情即可查看异常问题详情，包含执行设备信息、执行过程信息和问题列表；问题列表中有序号、问题描述和修复指南。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/32/v3/D-BBuQ4UQJWfN6tdW1sAcg/zh-cn_image_0000002524511907.png?HW-CC-KV=V1&HW-CC-Date=20260611T073255Z&HW-CC-Expire=86400&HW-CC-Sign=E24E4CF39B117C688C1556FF8A7B96E731BA4DCDE875E96586125D946FF8F232 "点击放大")

说明

更多测试服务详情，请前往DevEco Testing客户端->专项测试->安全基础质量测试->任务创建页->测试指南中查询。

## 功能体验基础质量测试

**功能体验基础质量测试：**根据应用功能体验建议，检测应用在当前系统、设备及升级场景下运行是否存在兼容性问题。

测试完成后，自动生成测试报告。报告包含任务信息、执行结果、问题统计、检测规则。支持查看当前应用信息、任务执行时长及详细的环境参数，点击打开目录按钮可导出 html 格式报告。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9c/v3/d9AStg6aQf-9u4vErWrX4Q/zh-cn_image_0000002492343802.png?HW-CC-KV=V1&HW-CC-Date=20260611T073255Z&HW-CC-Expire=86400&HW-CC-Sign=2031D38BACD89CBC6A0BFE5C120E61CC1B9BF256965B06628676DDFAB589E8EE "点击放大")

检测不通过的规则项，点击查看按钮查看问题详情，包含执行设备信息、执行过程信息、测试截图、问题列表等。![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b6/v3/JLycZ--FT0izWbO-McXzGw/zh-cn_image_0000002524623463.png?HW-CC-KV=V1&HW-CC-Date=20260611T073255Z&HW-CC-Expire=86400&HW-CC-Sign=8A01630A91B756A2C62AF747F9411F5B798113EFD9B9DFDAD12B28A1A047FB55 "点击放大")

说明

了解更多测试服务详情，请前往DevEco Testing客户端->专项测试->功能体验基础质量测试->任务创建页->测试指南中查询。

## 功耗基础质量测试

**功耗基础质量测试：**根据应用功耗建议，检测应用在运行时是否出现系统资源异常占用的情况。

测试完成后，自动生成测试报告。报告包含任务信息、执行结果、问题统计、检测规则。支持查看当前应用信息、任务执行时长及详细的环境参数，支持导出 html 格式报告。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/aa/v3/4axnhDpZRqC-oC_YPtmECQ/zh-cn_image_0000002524623477.png?HW-CC-KV=V1&HW-CC-Date=20260611T073255Z&HW-CC-Expire=86400&HW-CC-Sign=4F9D833F3B7FF645F63DDAD05790F78DEB3B92F1053CE800F249711D2AE84247 "点击放大")

检测不通过的规则项，点击查看按钮查看问题详情，包含执行设备信息、执行过程信息、测试截图、问题列表等。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/91/v3/U2Aa4ck7S1iTf2uTmtrulg/zh-cn_image_0000002524623445.png?HW-CC-KV=V1&HW-CC-Date=20260611T073255Z&HW-CC-Expire=86400&HW-CC-Sign=9E65D7D151777834A40B7AF8BF2C202F17876EC882EEDA28CEFEE2D53FB3B198 "点击放大")

说明

了解更多测试服务详情，请前往DevEco Testing客户端->专项测试->功耗基础质量测试->任务创建页->测试指南中查询。
