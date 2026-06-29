---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-parallel-concurrency-analysis
title: 并行并发：Concurrency分析
breadcrumb: 指南 > 优化应用性能 > 并行并发：Concurrency分析
category: harmonyos-guides
scraped_at: 2026-06-11T15:31:46+08:00
doc_updated_at: 2026-04-30
content_hash: sha256:1f53be2ebfa66fdc330618dc8124908445fe5d023f2e48985d03a9659c1d1412
---
任务池（TaskPool）（详细信息请参考[@ohos.taskpool（启动任务池）](<../../../harmonyos-references/ArkTS（方舟编程语言）/ArkTS API/@ohos.taskpool (启动任务池)/js-apis-taskpool.md>)）是为应用程序提供一个多线程的运行环境，降低整体资源的消耗和提高系统的整体性能，且您无需关心线程实例的生命周期。您可以使用任务池API创建后台任务（Task），并对所创建的任务进行如任务执行、任务取消的操作。

DevEco Profiler提供的Concurrency场景分析能力，帮助开发者针对并行并发场景，录制并行并发关键数据，分析Task的生命周期、吞吐量、耗时等性能问题。Concurrency模板支持展示ArkTS异步接口、NAPI异步接口、TaskPool、FFRT并发模型相关信息，并集成ArkTS Callstack、Callstack、Process信息，支持用户从Task生命周期关联到具体调用栈信息，方便用户定位并行并发性能问题。

## 查看Task统计信息

1. 选择展开某个泳道，可以用options下拉框筛选不同进程。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/96/v3/MrGU6kqeRR-tkkpXcrznOw/zh-cn_image_0000002602186545.png?HW-CC-KV=V1&HW-CC-Date=20260611T073145Z&HW-CC-Expire=86400&HW-CC-Sign=4ACDF3BEB03D397F3563D689D38B09F3C87756CC25A11C12049594D6A658025D "点击放大")
2. 框选子泳道中某段时间范围，详情区会出现该时段内，泳道对应执行状态下，并行并发任务的统计信息。
3. 点击Task Name的跳转按钮可跳转到对应的Task泳道。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7a/v3/Bf_K1bYZT9GGYP0RAQmHbQ/zh-cn_image_0000002571547004.png?HW-CC-KV=V1&HW-CC-Date=20260611T073145Z&HW-CC-Expire=86400&HW-CC-Sign=D4AD501AEB8272929D04D7FBCDF1FCA4BA3C2022D2E7031A547481808B2BA958 "点击放大")

## 查看某一个Task的所有状态

1. 选择展开某个泳道，可以用options下拉框筛选不同进程。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cf/v3/0TrYygKwSwas5cG_nJsBDg/zh-cn_image_0000002571387362.png?HW-CC-KV=V1&HW-CC-Date=20260611T073145Z&HW-CC-Expire=86400&HW-CC-Sign=CD3E043A2920C0F5470816B204B3FE74012D71963512108271B2BD50C1DC4DA2)
2. 框选子泳道中某段时间范围，可以看到该Task在框选时间范围内的任务状态。
3. 点击Task Name的跳转按钮可跳转到对应线程的泳道，可查看在该Task执行时间范围内，trace文件的打点信息，反映的是线程该时段内的函数执行情况。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/58/v3/J9rcsbT4T0WBVDlACLej0A/zh-cn_image_0000002571387364.png?HW-CC-KV=V1&HW-CC-Date=20260611T073145Z&HW-CC-Expire=86400&HW-CC-Sign=7520EC45ADC4FB609E7B22D7FD3CBF2B1B6D8D4C9D6F68F055061AB3DDE684BF "点击放大")
4. 展开Async ArkTS泳道，可单独查看ArkTS异步调用任务详情。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7b/v3/G1fsRDGjQamGGObggpHicQ/zh-cn_image_0000002602186543.png?HW-CC-KV=V1&HW-CC-Date=20260611T073145Z&HW-CC-Expire=86400&HW-CC-Sign=E5EC17CECBB4B1B0A350F3C7DF6EB26624F1B73A5D0BBBAC945C1C4CE276B890 "点击放大")
5. 展开Async NAPI泳道，单独查看NAPI异步调用任务详情。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ac/v3/rc2m5GiPROacek5h6l6T6Q/zh-cn_image_0000002571547006.png?HW-CC-KV=V1&HW-CC-Date=20260611T073145Z&HW-CC-Expire=86400&HW-CC-Sign=03EBB5FCAE4EEF68DEC807D49E4C0A91CF284AC63383EC998F87BF660FC6826D "点击放大")

## 查看Task的某个状态

点击Task子泳道的某个执行节点，Details详情区里会出现task在该状态下的详细信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/72/v3/GwHGgzEMQzKBYRfTFSDyXw/zh-cn_image_0000002571387366.png?HW-CC-KV=V1&HW-CC-Date=20260611T073145Z&HW-CC-Expire=86400&HW-CC-Sign=D39F185DCA6B8EC187E58DA4EB6192FD2FFB8F255FE603630A1995C94BA81418 "点击放大")
