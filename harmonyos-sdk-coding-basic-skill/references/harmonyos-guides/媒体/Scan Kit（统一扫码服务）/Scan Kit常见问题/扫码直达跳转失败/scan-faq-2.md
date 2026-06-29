---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/scan-faq-2
title: 扫码直达跳转失败
breadcrumb: 指南 > 媒体 > Scan Kit（统一扫码服务） > Scan Kit常见问题 > 扫码直达跳转失败
category: harmonyos-guides
scraped_at: 2026-06-01T11:31:33+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:127b91303109674ea4f374cfa99e7d405c88f0e65fc59ed46912273937405f30
---
**问题现象**

扫码直达跳转失败。

**解决措施**

请检查App Linking配置是否正确：

1. 检查开发者网站服务器配置是否正确。
2. 检查App Linking中网址域名关联是否正确。
3. 检查应用的module.json5文件中域名关联是否正确。
4. 检查应用的签名是否正确，参考[手动签名](../../../../编写与调试应用/配置调试签名/ide-signing.md#section297715173233)。

详情参考：App Linking的[FAQ](<../../../../应用服务/App Linking Kit（应用链接服务）/通过App Linking应用链接拉起指定应用/app-linking-startupapp.md#faq>)。
