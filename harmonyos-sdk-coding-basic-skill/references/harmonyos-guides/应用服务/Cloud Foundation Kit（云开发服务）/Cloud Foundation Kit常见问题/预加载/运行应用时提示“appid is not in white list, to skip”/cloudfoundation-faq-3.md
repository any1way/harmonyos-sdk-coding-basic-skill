---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cloudfoundation-faq-3
title: 运行应用时提示“appid **** is not in white list, to skip”
breadcrumb: 指南 > 应用服务 > Cloud Foundation Kit（云开发服务） > Cloud Foundation Kit常见问题 > 预加载 > 运行应用时提示“appid **** is not in white list, to skip”
category: harmonyos-guides
scraped_at: 2026-06-11T15:06:22+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:4e4895311fbae0846a0dbc96dd403daa9c45a28ac2a4b28731e2572a6c323dfe
---
**问题现象**

运行应用时提示“appid \*\*\*\* is not in white list, to skip”。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b7/v3/INpic-8wSGyPDxtR8bKpMQ/zh-cn_image_0000002622858759.png?HW-CC-KV=V1&HW-CC-Date=20260611T070621Z&HW-CC-Expire=86400&HW-CC-Sign=06EA04A4C84D407D25B7B69D3212BA28A2F62AC57D8527C68736DC5D97EF8B8E)

**解决措施**

出现此错误，是因为手机白名单中未包含当前应用。可按照如下步骤排查和解决：

1. 确认云侧是否已开通云函数和预加载服务。须确保已成功开通。
2. 确认日志中提示的APP ID前缀与云侧创建应用的实际APP ID是否一致。若两者不一致，可能使用了错误的签名方式。请更改为[关联注册应用进行自动签名](../../../../../编写与调试应用/配置调试签名/ide-signing.md#section20943184413328)或者[手动签名](../../../../../编写与调试应用/配置调试签名/ide-signing.md#section297715173233)方式。
3. 手机端进入“设置->系统->日期和时间”，关闭“自动设置”开关，将“日期”往后加1天，然后卸载应用重新安装，应用会自动更新白名单。
