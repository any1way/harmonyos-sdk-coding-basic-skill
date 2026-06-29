---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-task-visualization
title: 任务可视化与执行
breadcrumb: 指南 > 构建应用 > 任务可视化与执行
category: harmonyos-guides
scraped_at: 2026-06-11T15:31:05+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:6639a887f29d2ae3c5a04c9bf176d2ea1f18086177ad48861391f8197b104313
---
从DevEco Studio 6.1.0 Beta1版本开始，Hvigor提供任务可视化窗口，用于展示工程和各个模块常用的构建任务，便于快速执行。

1. 点击编辑窗口右侧工具栏的**Hvigor**，或者菜单栏**View > Tool Windows >** **Hvigor**，打开任务可视化窗口，会显示当前product和构建模式下的任务，切换product和构建模式时会同步工程，同步成功后会刷新任务列表。
   * Tasks：工程级的任务。
   * Run Configurations：Run/Debug Configurations窗口中的任务。
   * 其他目录：模块级的任务，如entry。

   其中工程级和模块级的任务，build和help目录下是Hvigor的默认任务，other目录下是开发者[自定义的任务](../扩展构建能力/开发Hvigor任务/ide-hvigor-task.md)。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7d/v3/hh26-4J-RcGHnOyGA8UVkA/zh-cn_image_0000002602066327.png?HW-CC-KV=V1&HW-CC-Date=20260611T073104Z&HW-CC-Expire=86400&HW-CC-Sign=55680E45ADE7D906AD34B82FC8E9D0FC5F728A17B0EC96ED2EFBB14197678E2A)
2. 可以通过鼠标双击、鼠标右键或Enter键快速执行一个选中的任务，也可以点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/98/v3/EfdazvFYSxKPsVX4tMpecw/zh-cn_image_0000002571546846.png?HW-CC-KV=V1&HW-CC-Date=20260611T073104Z&HW-CC-Expire=86400&HW-CC-Sign=CCCDDD439E083501FC32098D719ED417C866ADCD4913ECE428F29025F7DAF259)打开Run Anything窗口，搜索任务并双击执行。
