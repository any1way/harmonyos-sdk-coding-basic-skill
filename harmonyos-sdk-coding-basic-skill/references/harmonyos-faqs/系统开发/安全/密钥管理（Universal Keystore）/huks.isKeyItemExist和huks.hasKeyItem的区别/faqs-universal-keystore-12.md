---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-universal-keystore-12
title: huks.isKeyItemExist和huks.hasKeyItem的区别
breadcrumb: FAQ > 系统开发 > 安全 > 密钥管理（Universal Keystore） > huks.isKeyItemExist和huks.hasKeyItem的区别
category: harmonyos-faqs
scraped_at: 2026-06-12T10:37:14+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:260c0d16221cb6a1c8315d2188e70b891e7ff6f8496085ee7e2a6f876a848b7f
---
[huks.isKeyItemExist](<../../../../../harmonyos-references/Universal Keystore Kit（密钥管理服务）/ArkTS API/@ohos.security.huks (通用密钥库系统)/js-apis-huks.md#huksiskeyitemexist9>)：若密钥存在，data为true，若密钥不存在，则error中会输出密钥不存在的error code。开发者需要通过错误码判断密钥不存在，不符合逻辑习惯。建议使用hasKeyItem接口。

[huks.hasKeyItem](<../../../../../harmonyos-references/Universal Keystore Kit（密钥管理服务）/ArkTS API/@ohos.security.huks (通用密钥库系统)/js-apis-huks.md#hukshaskeyitem11>)：若密钥存在，返回值为true，若密钥不存在，返回值为false。
