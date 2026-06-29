---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ui-js-building-ui-layout-intro
title: 布局说明
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (兼容JS的类Web开发范式) > 构建用户界面 > 构建布局 > 布局说明
category: harmonyos-guides
scraped_at: 2026-06-11T14:33:15+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:1acf3eee43f747cf4b93113b94128963f62a9d483dd15ef41b7f6661b04305cc
---

设备的基准宽度为720px（px为逻辑像素，非物理像素），实际显示效果会根据实际屏幕宽度进行缩放。

其换算关系如下：

组件的width设为100px时，在宽度为720物理像素的屏幕上，实际显示为100物理像素；在宽度为1440物理像素的屏幕上，实际显示为200物理像素。

一个页面的基本元素包含标题区域、文本区域、图片区域等，每个基本元素内还可以包含多个子元素，开发者根据需求还可以添加按钮、开关、进度条等组件。在构建页面布局时，需要对每个基本元素思考以下几个问题：

* 该元素的尺寸和排列位置
* 是否有重叠的元素
* 是否需要设置对齐、内间距或者边界
* 是否包含子元素及其排列位置
* 是否需要容器组件及其类型

将页面中的元素分解之后再对每个基本元素按顺序实现，可以减少多层嵌套造成的视觉混乱和逻辑混乱，提高代码的可读性，方便对页面做后续的调整。以下图为例进行分解：

**图1** 页面布局分解

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c0/v3/L0ZZQtvQTaOb90rWwfYLQQ/zh-cn_image_0000002592218486.png?HW-CC-KV=V1&HW-CC-Date=20260611T063315Z&HW-CC-Expire=86400&HW-CC-Sign=6458FD2FADC6E2B2AB3B15379ADE8A7828870FF5384D6B4B5D9FDE3FD0743556)

**图2** 留言区布局分解

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/03/v3/Ta8r6mDwROedPKBpG6nMXw/zh-cn_image_0000002592378420.png?HW-CC-KV=V1&HW-CC-Date=20260611T063315Z&HW-CC-Expire=86400&HW-CC-Sign=8D40076DF58DDCB2B1FCA4877D7C5EC47CABD2135D7FBBBCB7E6605A8E8BE40D)
