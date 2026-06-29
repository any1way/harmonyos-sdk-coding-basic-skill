---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-performance-analysis-kit-68
title: 安装VPN软件astrill后hdc访问不了设备
breadcrumb: FAQ > 应用质量 > 技术质量 > 运维 > 安装VPN软件astrill后hdc访问不了设备
category: harmonyos-faqs
scraped_at: 2026-06-12T10:20:09+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:1ae7d97be6172f0ce07036c90833d967a8c8b15e178962271676874371da62c9
---
**问题现象**

hdc访问不了设备。hdc list targets -v出现unknown状态。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e0/v3/LzcGNoD1Rr2E75zFo7cLOA/zh-cn_image_0000002474863621.png?HW-CC-KV=V1&HW-CC-Date=20260612T022008Z&HW-CC-Expire=86400&HW-CC-Sign=B20AB075273CC2C03EBAD92E3978D05CAA33824A5231B7ADEF688F74275E97A8)

查看hdc.log日志

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9a/v3/P3ctL6CNRdOXwooPbqqDLg/zh-cn_image_0000002474943789.png?HW-CC-KV=V1&HW-CC-Date=20260612T022008Z&HW-CC-Expire=86400&HW-CC-Sign=17EBF0FB62608EB79AC8D0FDD9C90A2BE6387BB74DD8C2969A8E2134B9375E2D)

**可能原因**

系统兼容问题。在win10上安装vpn工具astrill后，会导致出现这样问题。

**解决措施**

* 当前版本hdc建议卸载掉vpn软件，注意不是停掉vpn，而是卸载vpn。
* 参考[hdc版本配套表](../../../../../harmonyos-guides/系统/调测调优/调试命令/hdc/hdc.md#hdc版本配套表)升级最新版本后重试。
