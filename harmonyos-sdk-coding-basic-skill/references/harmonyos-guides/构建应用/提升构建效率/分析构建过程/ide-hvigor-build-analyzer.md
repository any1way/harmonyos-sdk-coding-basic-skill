---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hvigor-build-analyzer
title: 分析构建过程
breadcrumb: 指南 > 构建应用 > 提升构建效率 > 分析构建过程
category: harmonyos-guides
scraped_at: 2026-06-11T15:30:48+08:00
doc_updated_at: 2026-04-30
content_hash: sha256:b530b83e722b72e108dcb8fc7f5f7cc25cb698bd5dc870447cf5d6ccb7361d06
---
Build Analyzer可以展示编译构建过程的重要信息，开发者能够通过Build Analyzer的可视化分析来排查构建过程中的性能和内存问题。

## 进入Build Analyzer

Build Analyzer会在每次构建应用时默认生成一份报告，并在Build Analyzer窗口进行展示。

可以在构建完成后通过以下方式打开Build Analyzer窗口：

* 点击菜单栏**Build > Build Analyzer**进行查看。
* 在Build窗口中的Build Output页签，点击左侧边栏![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c6/v3/WcdHzXouQBmmHBZCUoC5_Q/zh-cn_image_0000002571546450.png?HW-CC-KV=V1&HW-CC-Date=20260611T073047Z&HW-CC-Expire=86400&HW-CC-Sign=358E728263FC9B9EC3F5E16A7B67353AC7C0AD2F04717B955E6381B4A6DD4600)，打开Build Analyzer页签。
* 构建成功且使用构建分析能力时，在Build窗口Build Output页签下的日志下方点击链接，跳转至Build Analyzer页签。

## 查看构建历史记录

Build Analyzer左侧的Build History窗口中按时间顺序显示构建历史记录，包括本工程的构建历史数据和[导入的日志数据](ide-hvigor-build-analyzer.md#section26761217305)。点击构建历史记录可以显示对应概览和可视化图谱界面。

说明

本工程的构建历史数据保存在./hvigor/report目录下，超过10条记录后，最久的历史数据将会被自动清理。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6d/v3/n35J74BsSfWA0s0EoS8vyg/zh-cn_image_0000002571386810.png?HW-CC-KV=V1&HW-CC-Date=20260611T073047Z&HW-CC-Expire=86400&HW-CC-Sign=47EFC2248059649749A677429E12109535050AA09AAB738EFB9943843FD30C65)

## 查看构建任务时间图谱

完成构建后首次打开Build Analyzer 时，窗口会显示构建分析概览，如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/11/v3/skO0fOf0Ry6LdxKJciaS4Q/zh-cn_image_0000002602065931.png?HW-CC-KV=V1&HW-CC-Date=20260611T073047Z&HW-CC-Expire=86400&HW-CC-Sign=DDD9F343B32382734DBD2EC1080CF5A466AA7D1A1A8CE8C4C01D9FE621F52A57)

如需查看构建任务时间图谱，请从下拉菜单中点击Tasks，默认进入时间图谱界面。该界面会分块显示构建历史记录、构建任务时长图谱、构建日志以及对应的日志详情信息，如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3f/v3/9x8_nxl3QXSRrSOXV6uQuQ/zh-cn_image_0000002571386812.png?HW-CC-KV=V1&HW-CC-Date=20260611T073047Z&HW-CC-Expire=86400&HW-CC-Sign=E7AC2A5D0565D6910F52612F4D5BF526358F5FAEDFB53A1CBE9D0855841BC36F)

图谱中的构建任务展示按照各个任务总时长占比，以相对长度进行展示。可以对时间块进行缩小放大，查看具体的任务名称及耗时信息。

图谱中构建子任务默认是折叠的，可点击Build TimeLine的节点信息，展开查看子任务的构建时长图谱。

图谱与日志信息是联动的，可点击图谱中的任务信息，即可联动对应的日志以及日志详情；相同的，点击日志时，也可联动对应的上方图谱信息。

说明

Build Analyzer不会全部显示构建操作中的所有任务，而是重点显示决定构建总时长的任务。

图谱下方日志模块，展示每次构建的所有日志信息，并按日志级别（Info、Debug、Warn、Error）进行区分，并提供日志搜索功能。

点击日志，可与上方图谱和右侧Details模块，进行联动显示。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0c/v3/dwSnlbnTR06-ZQbYzGQsQA/zh-cn_image_0000002602065933.png?HW-CC-KV=V1&HW-CC-Date=20260611T073047Z&HW-CC-Expire=86400&HW-CC-Sign=2799E1E3A166EF65FF7BF1D03AACBE476991D453C49F0746572897C5AFEFA689)

## 查看构建任务占比图谱

如需查看决定构建时长的任务的占比细分数据，请点击概览页面上的**Common views into this build**下方链接 ，您也可以从下拉菜单中选择**Tasks**并确认您要的任务分组类别。任务以模块、业务类别、Target以及同一模块下的Target、同一模块下的业务类别和同一Target下的业务类别进行分组。图表中任务按照时间占比从大到小排列，点击子任务可详细了解其执行情况。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/11/v3/a5k36G0PTPuzCeYAygOolw/zh-cn_image_0000002571386816.png?HW-CC-KV=V1&HW-CC-Date=20260611T073047Z&HW-CC-Expire=86400&HW-CC-Sign=23C2AEEC4A2C0418E07447283161E27F9B282AD744B33733E6A4C8BB6B835DF3)

说明

1. 由于并行线程的存在，分类任务计算时间可能会比实际总时间长；

2. 饼图中Configuration代表未记录的任务占比。

## 查看构建过程内存消耗曲线图

如果要分析构建过程的内存消耗情况，需要先[设置构建分析模式为Advanced](ide-hvigor-build-analyzer.md#section207890565217)，启用内存监测，构建后会生成内存消耗曲线图。从DevEco Studio 5.1.1 Beta1版本开始支持。

点击概览页面上**Common views into this build**下方的链接**Memory Usage During Build**，也可以从下拉菜单中选择**Tasks**和**Memory Usage**分组，查看内存消耗曲线图。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4c/v3/m3SnY_RDRmiloceuuJF4CQ/zh-cn_image_0000002602185981.png?HW-CC-KV=V1&HW-CC-Date=20260611T073047Z&HW-CC-Expire=86400&HW-CC-Sign=FBFDF82376654D1D69D8D993E3F6BE7FD23DBE928C1D03F58659F91443758DFE)

## 导出日志

如需查看本次构建日志，您可以点击导出按钮进行日志导出。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2d/v3/6TFnl3wwR3-uaiEbthdQ6g/zh-cn_image_0000002602185977.png?HW-CC-KV=V1&HW-CC-Date=20260611T073047Z&HW-CC-Expire=86400&HW-CC-Sign=D67252DEFC13B3FC2138167F7E7D73BC8DFC1E597D513953D521B88D376BBA66)

导出内容有：

* 分析统计本次构建的html文件。
* 记录构建日志的build.log文件。
* 记录构建daemon日志的daemon.log文件。
* 记录构建任务耗时的report.json文件。
* 记录构建过程内存消耗的report-monitor.json文件。

## 导入日志

如需查看历史或其他工程的构建日志，您可以点击导入按钮导入report.json文件，导入的文件保存在工程./hvigor/report/upload目录下，导入后可在Build Analyzer左侧的Build History窗口中查看。upload目录下最多保存10条记录，超过10条记录后，最久的历史数据将会被自动清理。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/82/v3/QpqIaYgvR0O2_hrrlWHcmA/zh-cn_image_0000002602185985.png?HW-CC-KV=V1&HW-CC-Date=20260611T073047Z&HW-CC-Expire=86400&HW-CC-Sign=FECA2387D13CB970BD45FCC395A5353F3AFBF0385AB84FC93A2F4DE8E92E30BA)

## 设置构建分析模式

进入**File > Settings**（macOS为**DevEco Studio > Preferences/Settings**） **> Build, Execution, Deployment > Build Tools > Hvigor**下，查看**Use build analysis mode**选项：

* 勾选此项：
  + 模式选择为Normal，即为普通模式（默认选项），记录简单打点数据进行分析。
  + 模式选择为Advanced，即为高级模式，记录详细打点数据进行分析（此模式下，建议搭配使用node 18版本）。
  + 模式选择为Ultrafine，即超精细化模式，与Advanced模式相比，在ArkTS编译阶段记录更详细的打点数据，但开启后可能导致编译构建时间更长。从DevEco Studio 6.0.0 Beta1版本开始支持。
* 取消勾选，即为不记录该次构建数据，不进行分析。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b4/v3/HbO5JmVBR_-KqLgnjJWRZw/zh-cn_image_0000002571386818.png?HW-CC-KV=V1&HW-CC-Date=20260611T073047Z&HW-CC-Expire=86400&HW-CC-Sign=BCFF5132FEE955FDC5EE1EB9F7158DD08BB9ADDE4B621C24C8D7FD2885A63A72)

## 生成构建可视化html文件

* 通过命令行方式生成构建可视化html文件。如生成HAP模块的构建可视化html文件，命令如下：

  ```
  1. hvigorw assembleHap --analyze=normal --config properties.hvigor.analyzeHtml=true
  ```

* 通过[hvigor-config.json5](../../配置文件/hvigor-config.json5文件/ide-hvigor-set-options.md)配置文件中properties.hvigor.analyzeHtml字段生成构建可视化html文件：

  ```
  1. {
  2. "modelVersion": "6.1.1",
  3. "dependencies": {
  4. },
  5. "execution": {
  6. },
  7. "logging": {
  8. },
  9. "debugging": {
  10. },
  11. "nodeOptions": {
  12. },
  13. "properties": {
  14. "hvigor.analyzeHtml": true  // 生成构建可视化html文件
  15. }
  16. }
  ```

  再执行构建，例如执行以下命令：

  ```
  1. hvigorw assembleHap --analyze=normal
  ```

执行以上命令后，在工程的.hvigor/report目录下生成对应的html文件，该文件可直接在浏览器中打开。
