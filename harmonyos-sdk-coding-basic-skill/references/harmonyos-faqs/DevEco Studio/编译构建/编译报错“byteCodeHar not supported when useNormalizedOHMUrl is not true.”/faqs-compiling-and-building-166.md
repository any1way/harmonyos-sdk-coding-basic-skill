---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-166
title: 编译报错“byteCodeHar not supported when useNormalizedOHMUrl is not true.”
breadcrumb: FAQ > DevEco Studio > 编译构建 > 编译报错“byteCodeHar not supported when useNormalizedOHMUrl is not true.”
category: harmonyos-faqs
scraped_at: 2026-06-12T10:43:26+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:5cb45e2abaaabb44c7d9002202a8e6350a323f015b56f9194bfb0a15c89bcd3e
---
**错误描述**

当useNormalizedOHMUrl配置为false时，不支持编译字节码HAR。

**可能原因**

当HAR模块的build-profile.json5文件中的byteCodeHar字段配置为true时，工程级build-profile.json5文件中的useNormalizedOHMUrl字段未配置为true。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2d/v3/uU6c5bXxTja2oKvfltrvCw/zh-cn_image_0000002194318416.png?HW-CC-KV=V1&HW-CC-Date=20260612T024325Z&HW-CC-Expire=86400&HW-CC-Sign=47B746803746940A07D9BF532EC43D1AD5D27814C13E0100A4EC8299C41C5FEC)

**解决措施**

当HAR模块的build-profile.json5文件中byteCodeHar字段配置为true时，工程级build-profile.json5文件中的useNormalizedOHMUrl字段也必须配置为true。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/12/v3/4Y7BnEckSIeM9c3LKGJT5Q/zh-cn_image_0000002308297297.png?HW-CC-KV=V1&HW-CC-Date=20260612T024325Z&HW-CC-Expire=86400&HW-CC-Sign=E52DE25709D72BD2FA0893B99D6724F2A5BFBBF8CFDB70DAE8D8DAF6E290342F)

**参考链接**

[strictMode](../../../../harmonyos-guides/构建应用/配置文件/工程级build-profile.json5文件/ide-hvigor-build-profile-app.md#section13181758123312)
