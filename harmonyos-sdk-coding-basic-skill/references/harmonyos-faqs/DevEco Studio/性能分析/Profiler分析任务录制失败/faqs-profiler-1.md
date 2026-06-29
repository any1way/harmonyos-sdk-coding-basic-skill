---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-profiler-1
title: Profiler分析任务录制失败
breadcrumb: FAQ > DevEco Studio > 性能分析 > Profiler分析任务录制失败
category: harmonyos-faqs
scraped_at: 2026-06-12T10:45:11+08:00
doc_updated_at: 2026-06-05
content_hash: sha256:4b7c516207f0877b89615b7b4491bece96c8f08ba6f7d3641dc7ef8d8d99b8e8
---

**问题现象**

单击Profiler深度分析任务的启动录制按钮后，录制失败。

* DevEco Studio提示任务启动或录制失败。

* Session列表中任务显示异常图标。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2b/v3/ZL3M0_pxRg-eOhp9doV_2w/zh-cn_image_0000002194318540.png?HW-CC-KV=V1&HW-CC-Date=20260612T024511Z&HW-CC-Expire=86400&HW-CC-Sign=F00EA2B3E321C0F6185FFC8694AD9A529E7D3214BCE68F4D7294263315B82E50)

**解决措施**

启动深度分析任务录制后，将经历初始化、录制和停止录制后分析及组装数据三个阶段。每个阶段都可能遇到任务录制失败的问题，具体原因包括连接断开、插件错误和设备状态异常。

请参考以下步骤进行操作。

1. 确保设备亮屏运行。

2. 尝试重新推送包到设备，或者重启应用和服务。
3. 重启设备。
4. 重启DevEco Studio。
