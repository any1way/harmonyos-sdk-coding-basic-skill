---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/liveview-faq-4
title: 关于实况窗模板使用的问题
breadcrumb: 指南 > 应用服务 > Live View Kit（实况窗服务） > Live View Kit常见问题 > 关于实况窗模板使用的问题
category: harmonyos-guides
scraped_at: 2026-06-11T15:09:21+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:d2e72e0d65ada705adec2b7c44b9905a8dbb9eecc93675875066943ac290fe55
---
## 采用进度可视化模板并且indicatorType为INDICATOR\_TYPE\_OVERLAY时，图片较宽，无法完全覆盖进度条

当indicatorType=INDICATOR\_TYPE\_OVERLAY时，图标区域为64\*56vp，图片较宽时会按比例进行缩放。应用需要自己修改图片大小和样式来达到想要的效果。

理想效果图 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d5/v3/cgGMJkcOSFS2dL2u9dHUxA/zh-cn_image_0000002622698983.png?HW-CC-KV=V1&HW-CC-Date=20260611T070920Z&HW-CC-Expire=86400&HW-CC-Sign=C6E0A396009E938603CC0706DB727A5909693BE20C15EC7FD10FD484BC27FF79)

## 如何修改 "实况窗左上角图标"

除导航模板通过[currentNavigationIcon](<../../../../../harmonyos-references/Live View Kit（实况窗服务）/ArkTS API/liveViewManager/liveview-liveviewmanager.md#navigationlayout>)设置左上角图标外，其他模板不支持修改实况窗左上角图标，默认展示为应用Logo图标。
