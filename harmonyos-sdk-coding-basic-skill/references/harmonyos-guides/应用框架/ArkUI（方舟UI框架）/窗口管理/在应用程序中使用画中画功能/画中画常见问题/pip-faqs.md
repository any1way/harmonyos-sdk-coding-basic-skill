---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/pip-faqs
title: 画中画常见问题
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > 窗口管理 > 在应用程序中使用画中画功能 > 画中画常见问题
category: harmonyos-guides
scraped_at: 2026-06-01T11:08:50+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:4fe00688ad2aa2a0d7d542b40802ae2c3d72674266ffa1c8829dec555145ff88
---
## 画中画如何实现多个视频流播放

开发者需要实现多个视频流播放，可以通过自定义节点将视频流封装为NodeController，创建画中画时配置为自定义节点[customUIController](<../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS API/窗口管理/@ohos.PiPWindow (画中画窗口)/js-apis-pipwindow.md#pipconfiguration>)，实现多个视频流播放 。

## 画中画如何实现节点切换

开发者可以使用画中画typeNode方案，typeNode方案支持通过[updateContentNode](<../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS API/窗口管理/@ohos.PiPWindow (画中画窗口)/js-apis-pipwindow.md#updatecontentnode18>)方法更新画中画节点。

## 画中画如何解决拖动删除或点击关闭按钮关闭后，后台声音仍然存在的问题

对于申请了长时任务的应用，画中画拖动删除或点击关闭后仅删除画中画窗口，并不会结束应用进程。开发者需要开启画中画生命周期监听，在STOPPED生命周期中主动关闭任务或进程。
