---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-package-structure-71
title: 应用静态快捷方式如何接入X键
breadcrumb: FAQ > 应用框架开发 > 程序包结构 > 应用静态快捷方式如何接入X键
category: harmonyos-faqs
scraped_at: 2026-06-12T10:21:19+08:00
doc_updated_at: 2026-04-08
content_hash: sha256:9d0fc2f6527b5db9bfd103897b63a132c6b717c58b358b13e05c19432590f3d0
---
**现有机制：**

X键当前已经支持将应用的静态快捷方式，添加至X键的九宫格面板，后续用户可以通过单击X键呼出九宫格面板后，点击已添加进来的静态快捷方式图标，快速启动，一键直达。注：当前X键九宫格面板对所有应用开放静态快捷方式，X键双击/长按列表中只对部分应用开放静态快捷方式。

**适用场景：**

应用的功能入口深，操作步骤复杂。

**实现方案：**

应用的静态快捷方式可以接入X键的前提是，应用需要创建自己的静态快捷方式，创建出来的静态快捷方式，在桌面长按应用图标，图标上方会显示静态快捷方式（注：桌面上最多显示4个静态快捷方式），另外X键编辑界面中也会显示（注：X键编辑界面暂不限制应用静态快捷方式的显示数量），并且可以点击快捷方式后面的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/be/v3/aoMQ1uZvS1iT1LB5Ylpq6w/zh-cn_image_0000002537542426.png?HW-CC-KV=V1&HW-CC-Date=20260612T022118Z&HW-CC-Expire=86400&HW-CC-Sign=A5E7BB7C4329F02602518F0B9E8500FC6AFB222A88C6103B0E2D25C9CEC4CA5E)图标添加至X键九宫格面板，具体效果如下图：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d9/v3/MbT41qBaQq-nhPxN0xOw1g/zh-cn_image_0000002568302199.png?HW-CC-KV=V1&HW-CC-Date=20260612T022118Z&HW-CC-Expire=86400&HW-CC-Sign=168463F28413B18233696FF25B2EFC1E8196B7EF061CF387B7C329E98FE24A5B)

**参考链接：**

[创建应用静态快捷方式](../../../../harmonyos-guides/基础入门/开发基础知识/典型场景的开发指导/创建应用静态快捷方式/typical-scenario-configuration.md)
