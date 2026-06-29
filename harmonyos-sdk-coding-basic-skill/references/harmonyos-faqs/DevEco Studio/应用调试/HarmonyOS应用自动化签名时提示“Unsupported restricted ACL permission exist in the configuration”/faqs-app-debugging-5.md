---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-debugging-5
title: HarmonyOS应用自动化签名时提示“Unsupported restricted ACL permission exist in the configuration”
breadcrumb: FAQ > DevEco Studio > 应用调试 > HarmonyOS应用自动化签名时提示“Unsupported restricted ACL permission exist in the configuration”
category: harmonyos-faqs
scraped_at: 2026-06-12T10:44:40+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:51d95216105c6207de06de618c4b4c48eccd7faa868ddb617ebd178c9bf137ce
---
**问题现象**

在对HarmonyOS应用工程中，勾选“Automatically generate signature”时，提示“Unsupported restricted ACL permission exist in the configuration”报错信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/94/v3/--gwDbbXRMec2Mqe2DBnwA/zh-cn_image_0000002250504069.png?HW-CC-KV=V1&HW-CC-Date=20260612T024439Z&HW-CC-Expire=86400&HW-CC-Sign=F6FBDC187429016990B19405D77B22FC9A4688C11A5CF6D403FD7ED43C11820F)

**解决措施**

出现该问题的原因是当前DevEco Studio自动签名只支持部分的ACL权限，当前工程中使用了不在支持范围之内的ACL权限，建议尝试手动签名。

**参考链接**

[自动签名支持的ACL权限](../../../../harmonyos-guides/编写与调试应用/配置调试签名/ide-signing.md#section5301916183411)

[手动签名](../../../../harmonyos-guides/编写与调试应用/配置调试签名/ide-signing.md#section297715173233)
