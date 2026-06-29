---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-universal-keystore-3
title: 并发场景下AES加密失败
breadcrumb: FAQ > 系统开发 > 安全 > 密钥管理（Universal Keystore） > 并发场景下AES加密失败
category: harmonyos-faqs
scraped_at: 2026-06-12T10:37:08+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:1f80fb007c635afb7608375f1778e8253d6342c85ed341246747ba28c16c56d5
---
**原因**

使用HUKS重复导入相同的密钥时，[huks.importKeyItem](<../../../../../harmonyos-references/Universal Keystore Kit（密钥管理服务）/ArkTS API/@ohos.security.huks (通用密钥库系统)/js-apis-huks.md#huksimportkeyitem9>)会判断密钥是否存在。如果存在，会删除并重新生成密钥，这可能导致其他线程的init操作失败。

**解决措施**

使用HUKS时，相同密钥只需导入一次，系统会安全存储密钥，并使用密钥别名进行密码学操作。如果不需要系统保存密钥，可以使用cryptoFramework。
