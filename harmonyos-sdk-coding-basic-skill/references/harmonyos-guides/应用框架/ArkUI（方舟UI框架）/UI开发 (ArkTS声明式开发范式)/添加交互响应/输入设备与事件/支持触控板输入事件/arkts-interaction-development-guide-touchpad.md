---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-interaction-development-guide-touchpad
title: 支持触控板输入事件
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (ArkTS声明式开发范式) > 添加交互响应 > 输入设备与事件 > 支持触控板输入事件
category: harmonyos-guides
scraped_at: 2026-06-11T14:31:49+08:00
doc_updated_at: 2026-06-03
content_hash: sha256:1a5e6086ba7fdf927aace12b55561af58381a4a0d15e8a646b1621b02ffeb274
---
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ca/v3/ILVBw2r5RRW-V9Iok8RhFA/zh-cn_image_0000002622697907.png?HW-CC-KV=V1&HW-CC-Date=20260611T063148Z&HW-CC-Expire=86400&HW-CC-Sign=62BC8CC2960D585044E7DECAD80E874EC9F173EEE70F1C34222894AF47857341)

当用户使用触控板时，会根据不同的操作方式生成相应的事件。单指点触会产生鼠标左键点击事件，单指轻触移动会产生不按键的鼠标移动事件；双指点触会产生鼠标右键点击事件，双指轻触移动会产生轴事件。

说明

需要注意的是，与触屏不同，触控板上的多指操作并不会体现在上报的事件中，应用无法获取手指信息。

## 单指操作

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3a/v3/jyWwHURPSzuIxfU0DK5x_Q/zh-cn_image_0000002592218346.png?HW-CC-KV=V1&HW-CC-Date=20260611T063148Z&HW-CC-Expire=86400&HW-CC-Sign=841646379E547E6395FB876E6291F8E9263167E31AF13F9F345747A90E7F5615)

单指操作触控板与操作鼠标的方式相同。例如，轻触后滑动会产生鼠标移动事件，而重按则会产生鼠标左键按下事件。若需判断鼠标事件是来自触控板还是鼠标设备，可以通过[sourceType](../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/手势处理/绑定手势/绑定手势事件/ts-gesture-settings.md#sourcetype枚举说明8)和[sourceTool](../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/手势处理/绑定手势/绑定手势事件/ts-gesture-settings.md#sourcetool枚举说明9)信息进行区分。

对该种操作产生的事件的处理，请参考[处理鼠标移动](../支持鼠标输入事件/arkts-interaction-development-guide-mouse.md#处理鼠标移动)章节。

## 双指滑动

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d8/v3/D5acEMavTxCxaY0e4NgnVw/zh-cn_image_0000002592378280.png?HW-CC-KV=V1&HW-CC-Date=20260611T063148Z&HW-CC-Expire=86400&HW-CC-Sign=FACC7A67C10B4065D3D27B0A782331A4CB39F1B46E9F7A39B7A4522367504BED)

与鼠标滚轮不同，触控板上双指滑动产生的轴事件上报的数值单位并非角度，而是位移像素，为了区分该点，在处理轴值之前，可以通过sourceType及sourceTool来区分。

当用户使用双指横滑时，可从[axisHorizontal](../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/手势处理/手势控制/自定义手势判定/ts-gesture-customize-judge.md#属性)中获取横向轴值（位移像素），向右滑动时，上报数值为负，向左滑动时，上报数值为正。使用双指竖滑时，可从[axisVertical](../../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/手势处理/手势控制/自定义手势判定/ts-gesture-customize-judge.md#属性)获取到纵向轴值（位移像素），向上滑动时，上报数值为正，向下滑动时，上报数值为负。

同滚轮一样，产生的轴事件可以驱动滑动手势的触发。向右滑动时，上报offsetX数值为正，向左滑动时，上报offsetX数值为负。向上滑动时，上报offsetY数值为负，向下滑动时，上报offsetY数值为正。

说明

只有在开始滚动操作的那一刻光标所在位置下的组件上的手势会被收集。

## 双指捏合

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ef/v3/huKghx8YQFyaA_2wXkNHYA/zh-cn_image_0000002622857787.png?HW-CC-KV=V1&HW-CC-Date=20260611T063148Z&HW-CC-Expire=86400&HW-CC-Sign=733A2750DD3A8A0E70D5A6165D21DF5A1FFF25DE0BA606C68C040C2051D7F8E0)

在触控板上通过双指捏合，可以产生捏合缩放值上报。该值表示一个相对缩放比例，可用于实现UI缩放效果。系统上报的数值为一个scale比例，其以双指开始捏合的那一刻（此时为1.0）为基准参考。当双指往外扩张时，scale逐渐从1.0增大；当双指往内合并时，scale逐渐减小。
