---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arengine-faq-3
title: 反光、光线暗或者弱纹理场景（输入图像颜色变化小）下无法识别平面
breadcrumb: 指南 > 图形 > AR Engine（AR引擎服务） > AR Engine常见问题 > 反光、光线暗或者弱纹理场景（输入图像颜色变化小）下无法识别平面
category: harmonyos-guides
scraped_at: 2026-06-11T15:00:02+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:62bd71d2eee48f88673e4e06eff3726aadf29ab18c651f4afb95afe831394d7c
---

## 现象描述

使用环境跟踪能力时，如果输入图像中有反光、光线暗、有弱纹理（输入图像颜色变化小），识别到的点云数量会变少甚至没有，出平面时间也会变长或无法生成平面。

1. 反光：镜面，光滑的大理石地板等

   **图1** 镜面

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/35/v3/HrhYMiGnQyCEFWHGIzJ_ZQ/zh-cn_image_0000002592219058.jpg?HW-CC-KV=V1&HW-CC-Date=20260611T065958Z&HW-CC-Expire=86400&HW-CC-Sign=0CAFCB0CD46155082048B54F495DEC21EC07CF49166E3229B5E6C8B6D0DC237E)
2. 光线暗：夜晚的路面或摄像头遮挡等。

   **图2** 夜晚的路面

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6c/v3/fLNgBpADSDi0r3C3Fgfz9w/zh-cn_image_0000002592378992.jpg?HW-CC-KV=V1&HW-CC-Date=20260611T065958Z&HW-CC-Expire=86400&HW-CC-Sign=4D53E6684522CA42E97CD44E79C0C988E7C8DDB1159BC025A21EC0B014D331CF)
3. 弱纹理：如单色柜子、单色桌面和墙面等。

   **图3** 墙面

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c2/v3/l6G2ShuxRAS8bm9iR2aBlQ/zh-cn_image_0000002622858499.jpg?HW-CC-KV=V1&HW-CC-Date=20260611T065958Z&HW-CC-Expire=86400&HW-CC-Sign=79242F9466602416BBD5F4040596F5BD0EEB1D148E33AC02D2F3E2FE7559D528)

   **图4** 纯色的桌面

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/27/v3/ga3tCBm8QbGgWnezT81hMw/zh-cn_image_0000002622698621.jpg?HW-CC-KV=V1&HW-CC-Date=20260611T065958Z&HW-CC-Expire=86400&HW-CC-Sign=838FEF9ED40DE6BCC65964F3459032A9F97D87F6D2BECDA6B7C06AC45A55DEF9)

## 可能原因

AR Engine通过输入的图像数据进行平面上特征点的计算，如果输入图像数据中存在反光、光线暗和弱纹理，AR Engine计算后只能得到很少的点，而平面根据识别到的点云生成，因此会导致平面出现缓慢或无法出现的现象。

## 处理步骤

建议应用在持续无法获取点云或平面数据时，提示用户移动相机，避免画面中持续出现反光、光线暗或弱纹理。
