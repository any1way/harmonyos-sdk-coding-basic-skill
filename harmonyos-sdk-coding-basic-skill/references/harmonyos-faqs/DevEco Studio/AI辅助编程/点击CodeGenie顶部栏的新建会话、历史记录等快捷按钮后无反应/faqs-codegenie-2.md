---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-codegenie-2
title: 点击CodeGenie顶部栏的新建会话、历史记录等快捷按钮后无反应
breadcrumb: FAQ > DevEco Studio > AI辅助编程 > 点击CodeGenie顶部栏的新建会话、历史记录等快捷按钮后无反应
category: harmonyos-faqs
scraped_at: 2026-06-12T10:45:54+08:00
doc_updated_at: 2026-04-02
content_hash: sha256:a8a4341536e173e31f2fc0a255441d2e980ebb796100e219388897a8eb98fc64
---
**问题现象**

CodeGenie使用过程中，点击顶部栏新建会话、历史记录、Agent配置等快捷按钮后无反应。

**问题原因**

代码异常，导致前端渲染问题。

**解决措施**

1. 保存工程并关闭DevEco Studio。
2. 打开当前DevEco Studio的安装目录，按如下安装路径找到**codegenie-plugin**文件夹，手动删除此文件夹或将此文件夹移动到其他位置缓存备份。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/11/v3/glPf1p8ATb-r-ttd8YlsuQ/zh-cn_image_0000002566394897.png?HW-CC-KV=V1&HW-CC-Date=20260612T024553Z&HW-CC-Expire=86400&HW-CC-Sign=FEF703FA54096D7F12EC3B2969CEBFBEC74F4F664739D5C1B14F5170F89E9B5E)
3. 在[官网链接](https://developer.huawei.com/consumer/cn/download/deveco-codegenie)下载最新发布的**DevEco CodeGenie 6.0.2 Release**版本，按照[插件安装指导](../../../../harmonyos-guides/使用AI智能辅助编程/工具概述/ide-codegenie.md#section18337533718)安装和使用新版本插件。
