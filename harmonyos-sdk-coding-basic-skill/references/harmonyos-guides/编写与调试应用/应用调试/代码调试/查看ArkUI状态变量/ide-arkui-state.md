---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-arkui-state
title: 查看ArkUI状态变量
breadcrumb: 指南 > 编写与调试应用 > 应用调试 > 代码调试 > 查看ArkUI状态变量
category: harmonyos-guides
scraped_at: 2026-06-11T15:29:20+08:00
doc_updated_at: 2026-06-10
content_hash: sha256:5b52fadb36f9b3873e65cf75eccce973962ac94f99994ea7082d393b906ffa4c
---

从DevEco Studio 6.0.2 Beta1版本开始，支持在调试时查看ArkUI状态变量的实时变化情况。

在调试窗口中，点击**Layout Settings**![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/be/v3/ivWLwQdWSWWlTLf8z2u4bw/zh-cn_image_0000002571386866.png?HW-CC-KV=V1&HW-CC-Date=20260611T072919Z&HW-CC-Expire=86400&HW-CC-Sign=ABEEDFB55094C86AB590D407186A428CFE1179BBC0A64E151C4088FFF5665E64)，勾选**ArkUI State**，打开ArkUI状态变量面板。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/49/v3/gfCPEIZ1RzWVrAsEeXz5EQ/zh-cn_image_0000002602186035.png?HW-CC-KV=V1&HW-CC-Date=20260611T072919Z&HW-CC-Expire=86400&HW-CC-Sign=80C232B0939239AA65B5A61A07C89FAEF5A26F5BADE8780AC95D2EF6A1F3F916)

状态变量面板分为总览（Summary）和当前值（Current Value）两个子面板：

* 总览面板显示了当前应用运行时，状态变量更新的总体情况，包含了状态变量的名称、更新次数、装饰器类型、所属组件、所属类、当前值。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9c/v3/0LxZbJnbRvW7Z4u6LloDSA/zh-cn_image_0000002571386868.png?HW-CC-KV=V1&HW-CC-Date=20260611T072919Z&HW-CC-Expire=86400&HW-CC-Sign=0636F52C74556D84A7CCC2BB041A952091ED4BBC81AC7FF92610B129B3E93C3E)
* 当前值面板记录了状态变量实时变化的数据，包含了状态变量的更新时间、名称、所属组件、所属类、装饰器类型、当前值、影响的组件数量。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/34/v3/aIgL7grZR1SX9vW7PQAUhA/zh-cn_image_0000002602186033.png?HW-CC-KV=V1&HW-CC-Date=20260611T072919Z&HW-CC-Expire=86400&HW-CC-Sign=62F4FB2C13B79B1422AC8ECD8BA9DA15104A9136C439360CC84D8F569473DEFE)当点击右侧的箭头时，新弹出的面板将显示当前选中状态变量影响的组件列表，包含影响组件的组件名、组件ID、是否为自定义组件。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/15/v3/XNqgXSAWRaWyJ5auaUz5Ng/zh-cn_image_0000002602065979.png?HW-CC-KV=V1&HW-CC-Date=20260611T072919Z&HW-CC-Expire=86400&HW-CC-Sign=5457D4F28314817B7508CD07A408945F4E1641E093ACD617DD774E5EAD9AC5C1)

说明

* 打开状态变量面板后才会开始监听状态变量的更新，因此，无法查看面板打开前状态变量的更新情况。
* 同一次调试过程中，关闭状态变量面板不会清空之前的数据，当前值面板最多展示1000条数据，超过限制后，仅展示最新的1000条数据。
