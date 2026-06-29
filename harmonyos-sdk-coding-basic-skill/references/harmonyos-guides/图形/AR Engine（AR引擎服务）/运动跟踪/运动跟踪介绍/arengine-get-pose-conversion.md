---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arengine-get-pose-conversion
title: 运动跟踪介绍
breadcrumb: 指南 > 图形 > AR Engine（AR引擎服务） > 运动跟踪 > 运动跟踪介绍
category: harmonyos-guides
scraped_at: 2026-06-11T14:59:10+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:8e83d00c283acb1a5d6bcbd384ba26e25f23556ff39bfcf247b8ea9a7bcf854d
---

AR Engine通过获取终端设备摄像头数据，结合图像特征和惯性传感器（IMU），计算设备位置（沿x、y、z轴方向位移）和姿态（绕x、y、z轴旋转），实现6自由度（6DoF）运动跟踪能力。

设备位姿描述了物体在真实世界中的位置和朝向。通过AR Engine，开发者可以实时获取设备在空间中任意时刻的位姿。

**图1** 6DoF运动跟踪能力示意图（红色线代表设备运动方向）

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f2/v3/0wuXexsZSI2-oSNjgrJ3hQ/zh-cn_image_0000002592378982.png?HW-CC-KV=V1&HW-CC-Date=20260611T065909Z&HW-CC-Expire=86400&HW-CC-Sign=C4E136729E61DBEF80DAF204A2273A39F389421D12AA0E8656EB9F89DA5CB2B3)

## 世界坐标系与位姿示意

设备位姿一般在世界坐标系下进行表示。世界坐标系描述了真实物理空间中物体的绝对位置，其正方向如图2所示。

**图2** 世界坐标系示意图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/78/v3/nlBx7daEQTKUptIhVKXBmQ/zh-cn_image_0000002622858489.png?HW-CC-KV=V1&HW-CC-Date=20260611T065909Z&HW-CC-Expire=86400&HW-CC-Sign=E19DDEDC560C1C17C0C58C93A2E47BC0E2A7FB213E23E4E375AF6F5B601BC8FC)

AR Engine会自动完成世界坐标系初始化。

在AR Engine中，设备位姿由一个7维向量描述，包括旋转量![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e5/v3/yeezUiInQzmu67Gtn6_ymw/zh-cn_image_0000002622698611.png?HW-CC-KV=V1&HW-CC-Date=20260611T065909Z&HW-CC-Expire=86400&HW-CC-Sign=C3B8698AE8987E1A289D926451EAA57393B45736636969AE2145ED2A28D135BD)和位移量![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2e/v3/1zIUrp3pSjyqyHAw4ZDzcQ/zh-cn_image_0000002592219050.png?HW-CC-KV=V1&HW-CC-Date=20260611T065909Z&HW-CC-Expire=86400&HW-CC-Sign=9C636364570456FD394155E93A2E6B3F80BA718DB439CC7F053344DFF7F2B03D)。其中旋转量![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/45/v3/CV13imEGTWaewRfRj-9yHA/zh-cn_image_0000002592378984.png?HW-CC-KV=V1&HW-CC-Date=20260611T065909Z&HW-CC-Expire=86400&HW-CC-Sign=CD4184CE71691201AAAE4BD556040FF782ECC9D4413D3D90AA67362E9A9A1B9D)是一组四元数，描述了设备相对于坐标原点的旋转状态；位移量![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/76/v3/blQomkvhQ3KfJDgluT2VHg/zh-cn_image_0000002622858491.png?HW-CC-KV=V1&HW-CC-Date=20260611T065909Z&HW-CC-Expire=86400&HW-CC-Sign=6E4252646939351E8C07F7BEA5D73CB66568CA96834608C1B0FA882D8B4FB72F)是一组三维向量，描述了设备相对于坐标原点的平移状态，如下图所示。

**图3** 设备位姿的旋转和平移变化示意图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e7/v3/YvON9ef5QO637MjPkCX6Dg/zh-cn_image_0000002622698613.png?HW-CC-KV=V1&HW-CC-Date=20260611T065909Z&HW-CC-Expire=86400&HW-CC-Sign=52C2D0AAF9BAD03F25AFA0103B7DD37F380CA38B9CD7A33A75030FB424AB753F)

通过旋转分量和平移分量，可以描述设备在空间中任意时刻的位姿状态。
