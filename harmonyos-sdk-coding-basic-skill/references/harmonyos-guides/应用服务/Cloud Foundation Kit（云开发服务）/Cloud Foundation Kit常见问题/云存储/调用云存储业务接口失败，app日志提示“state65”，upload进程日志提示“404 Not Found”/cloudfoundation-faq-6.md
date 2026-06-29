---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cloudfoundation-faq-6
title: 调用云存储业务接口失败，app日志提示“"state":65”，upload进程日志提示“404 Not Found”
breadcrumb: 指南 > 应用服务 > Cloud Foundation Kit（云开发服务） > Cloud Foundation Kit常见问题 > 云存储 > 调用云存储业务接口失败，app日志提示“"state":65”，upload进程日志提示“404 Not Found”
category: harmonyos-guides
scraped_at: 2026-06-11T15:06:18+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:cc9b1a4d6ff6932336a57957952e91ea5f677708e403704628f8c8c392b49810
---

**问题现象**

通过“使用指定的实例”方式初始化云存储实例时，调用业务接口（如调用uploadFile接口上传文件）失败，出现如下错误提示：

* app日志提示“"state":65”

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6e/v3/8OorUIWIT2W0ZNTrlUbZSw/zh-cn_image_0000002592379248.png?HW-CC-KV=V1&HW-CC-Date=20260611T070617Z&HW-CC-Expire=86400&HW-CC-Sign=162A8F45F7868CA1D9E313313557E4D3CCFED37C6C9C223E4C9BCADA349A7107)
* upload进程的日志提示“404 Not Found”（通过设置“No filters”模式、过滤“C01C50”关键字查找）

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/14/v3/nw4bu6WURW6imojMW_Ngww/zh-cn_image_0000002622858757.png?HW-CC-KV=V1&HW-CC-Date=20260611T070617Z&HW-CC-Expire=86400&HW-CC-Sign=C27559D26D4808693DEB01A9A6B0575AEDC6B96FB1143B75F82F6C06F7800C89)

**解决措施**

出现此问题，原因是当前云侧不存在该存储实例，或传入的存储实例名称错误。

请检查您传入的存储实例名称，确保云侧存在该存储实例，且传入的存储实例名称与云侧存储实例名称完全一致。
