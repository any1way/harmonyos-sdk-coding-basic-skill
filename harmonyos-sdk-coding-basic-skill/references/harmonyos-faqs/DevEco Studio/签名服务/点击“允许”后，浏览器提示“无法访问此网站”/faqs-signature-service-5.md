---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-signature-service-5
title: 点击“允许”后，浏览器提示“无法访问此网站”
breadcrumb: FAQ > DevEco Studio > 签名服务 > 点击“允许”后，浏览器提示“无法访问此网站”
category: harmonyos-faqs
scraped_at: 2026-06-12T10:43:53+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:504923ce85f80e362a4c0a7f1609b313d7dc13faf06d258822b24868ef4844d7
---
**问题现象**

使用浏览器登录华为账号并点击“允许”按钮后，浏览器将跳转至http://localhost:10101/xxx，显示“无法访问此网站”。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c8/v3/tKebDVv_S1eGeI0UzINpxw/zh-cn_image_0000002194318008.png?HW-CC-KV=V1&HW-CC-Date=20260612T024352Z&HW-CC-Expire=86400&HW-CC-Sign=55B3DFF0D198A82A09FEA71E99E9A57D80F390A184355729E98C58E257A56A7F)

**解决措施**

出现该问题的原因是登录授权过程中，DevEco Studio与华为账号之间的登录通道异常。具体原因包括点击了DevEco Studio登录界面的**Cancel**按钮，或者DevEco Studio在登录过程中异常关闭。

请尝试重新登录；建议在登录过程中不要做其它操作，避免误操作。如果重新登录还是出现该界面，请根据[浏览器点击“允许”按钮后，出现登录客户端失败提示](../浏览器点击“允许”按钮后，出现登录客户端失败提示/faqs-signature-service-4.md)解决措施，检查和设置DevEco Studio的HTTP Proxy后进行重试。
