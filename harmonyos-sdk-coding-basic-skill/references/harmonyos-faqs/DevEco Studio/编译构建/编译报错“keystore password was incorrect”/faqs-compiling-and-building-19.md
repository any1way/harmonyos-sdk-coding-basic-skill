---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-19
title: 编译报错“keystore password was incorrect”
breadcrumb: FAQ > DevEco Studio > 编译构建 > 编译报错“keystore password was incorrect”
category: harmonyos-faqs
scraped_at: 2026-06-12T10:41:13+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:3fd3c88f93a86db59c80f5a879e2975032601158f987f09f005816ee5d84157d
---

**问题现象**

编译时出现错误，提示“ERROR - hap-sign-tool: error: ACCESS\_ERROR, code: 109. Details: Init keystore failed: keystore password was incorrect”。请检查密钥库密码是否正确。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/be/v3/QHEu4ngCSMe7Frq7i_eBgw/zh-cn_image_0000002229603737.png?HW-CC-KV=V1&HW-CC-Date=20260612T024112Z&HW-CC-Expire=86400&HW-CC-Sign=9049469C9B2A69B3277F49FCC7D820B2146D9BF32CE003F09E16A31DA4A53F29)

**报错原因**

密钥库(p12)的密码错误。签名文件中的签名密码错误导致该问题出现。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b9/v3/bXU4Of11SSeTc1m7BGj-9w/zh-cn_image_0000002436501498.png?HW-CC-KV=V1&HW-CC-Date=20260612T024112Z&HW-CC-Expire=86400&HW-CC-Sign=96EE4F2C77B50A6D936779F536836A1CF7C54AFEE7146BD38EE900DC8D55AFD4)

注意

密钥库密码和密钥密码在创建p12文件时由开发者输入，请牢记这些密码。build-profile.json5文件中记录了密码的密文，但签名工具需要输入密码明文，不能直接使用build-profile.json5中的值。

**常见场景**

1. 密码输入错误。
2. 在命令行中输入了密文。
3. 密钥（keyAlias）密码和密钥库（p12）密码混淆。

**解决措施**

重新自动签名可以解决该问题：

1. 点击**File > Project Structure > Project > Signing Configs**，打开签名配置页面。

2. 勾选“Automatically generate signing”（如果是HarmonyOS工程，还需勾选“Support HarmonyOS”），等待重新签名，点击**OK**。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ad/v3/bcMPkwdzTHqflAhcUvLCQg/zh-cn_image_0000002229758209.png?HW-CC-KV=V1&HW-CC-Date=20260612T024112Z&HW-CC-Expire=86400&HW-CC-Sign=B4BF38CDCB42F9FC683BC17A4C82C210675CEED5E3DF2A2813A5D86CCD602E66)
