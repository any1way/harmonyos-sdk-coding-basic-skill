---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/store-attribution-trigger-custom
title: 自定义转化事件
breadcrumb: 指南 > 应用服务 > AppGallery Kit（应用市场服务） > 应用归因服务 > 开发准备 > 管理转化事件 > 自定义转化事件
category: harmonyos-guides
scraped_at: 2026-06-11T15:04:14+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:a73134bba4a8f935f123b113857f2221ed656034962289b53749425d9cb03197
---

**开发者角色的合作伙伴在转化事件管理页面可以做如下操作**：

新增、修改、删除、查看自定义转化事件。

新增、修改、删除自定义转化事件时，相应的操作会被运营人员在后台审核通过或驳回，仅被审核通过的自定义转化事件才能生效。

## 新增

1. 在左侧点击转化事件管理菜单栏，进入自定义转化事件页面。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8a/v3/LEuHkkjwSeWKOSkpTOrBjA/zh-cn_image_0000002592379152.png?HW-CC-KV=V1&HW-CC-Date=20260611T070413Z&HW-CC-Expire=86400&HW-CC-Sign=4386306F6AE260AA69CEA3A09BB3134F99BA3C8A302E20B71374212270839A67)
2. 点击右上角“新增”按钮，进入新增自定义转化事件页面。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e1/v3/-CUuOocaSB218KscHwTJJA/zh-cn_image_0000002622858659.png?HW-CC-KV=V1&HW-CC-Date=20260611T070413Z&HW-CC-Expire=86400&HW-CC-Sign=3C119F4F5710393CA0C8B8E6686EA5F84787A3EE5ECBF6D549B84FB6FFC8F0D7)
3. 填写“转化事件名称”、“转化事件编码”、“含义说明”信息，点击“确认”按钮后会生成一条状态是“新建待审核”的自定义转化事件。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6c/v3/dxW5e6kRQIa23OQvPGeXyg/zh-cn_image_0000002622698781.png?HW-CC-KV=V1&HW-CC-Date=20260611T070413Z&HW-CC-Expire=86400&HW-CC-Sign=725F00EF079965325B918289A8C44B41136ABA6C403F8E4B893A9DA864F46722)

说明

* 转化事件编码范围只能为[501, 600]。
* 转化事件名称或转化事件编码不能重复。

## 修改

1. 点击处于已生效或者驳回状态的自定义转化事件列表右侧“编辑”按钮：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2d/v3/Mup4gDi9Sd-05wmI0i5ReQ/zh-cn_image_0000002592219220.png?HW-CC-KV=V1&HW-CC-Date=20260611T070413Z&HW-CC-Expire=86400&HW-CC-Sign=F4DA0D8E93E48EFEE3907E66C27841B98D391F71586C20D22F6094D3FC7F1B67)
2. 进入编辑页面，修改“转化事件名称”、“转化事件编码”、“含义说明”信息后点击“确认”按钮。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/99/v3/EI4DND8SR0emWepS-i2i-w/zh-cn_image_0000002592379154.png?HW-CC-KV=V1&HW-CC-Date=20260611T070413Z&HW-CC-Expire=86400&HW-CC-Sign=818197E625CB0131FDC3916BCFE7C6F23F871EA552684EA0E3B37F99831572A6)
3. 修改后的数据状态为“修改待审核”或者“新建待审核”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/eb/v3/F38-Hr7oTV66nLJOp1b1OA/zh-cn_image_0000002622858661.png?HW-CC-KV=V1&HW-CC-Date=20260611T070413Z&HW-CC-Expire=86400&HW-CC-Sign=7C075D0E36C91121714521D59F1ECCFB9A60CDA7B0F42C5C2693B1D216185BE6)

“修改待审核”状态的自定义转化事件被审核通过后才能生效，如果被驳回，则维持修改之前的转化事件名称和转化事件编码值。

说明

* 修改后的转化事件名称或转化事件编码不能与已生效或者审核中的转化事件名称或转化事件编码重复。
* 对驳回状态的自定义转化事件进行编辑修改，修改后的状态为“新建待审核”。

## 删除

点击列表右侧的“删除”按钮，并在弹出框中点击“确认”。

状态为“已驳回”的自定义转化事件可以直接删除。

状态为“生效”的自定义转化事件，点击“确认”后该条自定义转化事件的状态由“生效”变为“删除待审核”。

删除待审核的自定义转化事件需要审核人员审核通过后，才会被删除。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a3/v3/-0rOe4DIQXGQPsr0cJMThw/zh-cn_image_0000002622698783.png?HW-CC-KV=V1&HW-CC-Date=20260611T070413Z&HW-CC-Expire=86400&HW-CC-Sign=A2AD03792A95F894CC11166B1668DD9F1C45D04016563FA446BA391A8840DDDC)

## 查看

点击左侧转化事件管理菜单栏，进入自定义转化事件页面查看自定义转化事件信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/29/v3/rBuB4ixRTl-noB_OS-vnHw/zh-cn_image_0000002592219222.png?HW-CC-KV=V1&HW-CC-Date=20260611T070413Z&HW-CC-Expire=86400&HW-CC-Sign=E0030A21862E7449384BC9DE59854AC3C55ECADF6378B7A13DED9FD24134FD1B)
