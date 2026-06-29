---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/account-faq-5
title: 使用华为账号一键登录功能时，是以华为账号的UnionID/OpenID还是以手机号作为用户的主要标识
breadcrumb: 指南 > 应用服务 > Account Kit（华为账号服务） > Account Kit常见问题 > 使用华为账号一键登录功能时，是以华为账号的UnionID/OpenID还是以手机号作为用户的主要标识
category: harmonyos-guides
scraped_at: 2026-06-01T14:59:40+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:e3f2d21c08c9cd1323a34b0097dfd34f246039f7a22b32a8442a766616667fce
---
推荐使用华为账号的UnionID/OpenID作为用户的主要标识，并将应用与华为账号绑定的手机号关联。华为账号的UnionID/OpenID不会发生变化，即使换绑手机号，仍然可以使用华为账号登录原来绑定的应用账号。该方式可以保障应用账号在多设备、多场景和多应用服务类型间（如应用、元服务等）的互联互通，保证应用的统一体验。若应用使用手机号作为用户的主要标识，如果华为账号换绑了手机号，再登录应用，就是新手机号对应的账号。华为账号一键登录详细流程请参考[用户场景设计](../../登录/华为账号一键登录（获取手机号和UnionIDOpenID）/account-phone-unionid-login.md#用户场景设计)。
