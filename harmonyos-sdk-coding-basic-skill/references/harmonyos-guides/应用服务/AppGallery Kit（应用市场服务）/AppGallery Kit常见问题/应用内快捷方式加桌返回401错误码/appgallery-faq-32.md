---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/appgallery-faq-32
title: 应用内快捷方式加桌返回401错误码
breadcrumb: 指南 > 应用服务 > AppGallery Kit（应用市场服务） > AppGallery Kit常见问题 > 应用内快捷方式加桌返回401错误码
category: harmonyos-guides
scraped_at: 2026-06-01T15:01:30+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:d478d71389656af4883c585ad553a5b0a6f1a91205367cd19145b53c533d16da
---
**问题现象**

调用应用内快捷方式接口加桌时，返回401错误码，参数错误。

**可能原因**

1. [checkPinShortcutPermitted](<../../../../../harmonyos-references/AppGallery Kit（应用市场服务）/ArkTS API/productViewManager (应用市场推荐)/store-productviewmanager.md#productviewmanagercheckpinshortcutpermitted>)校验快捷方式是否允许加桌接口：

   * 上下文context为空。
   * 快捷方式shortcutId长度超过63字节。
   * 快捷方式目标want中参数parameters非基本字符串类型或键值长度超过1024个字符。
   * 静态快捷方式名称资源索引labelResName为空或对应的资源不存在。
   * 静态快捷方式图标资源索引iconResName为空或对应的资源不存在。
   * 自定义快捷方式名称文本label为空或者长度超过255个字符。
   * 自定义快捷方式图标路径foregroundIcon无权限访问或文件不存在。
   * 自定义快捷方式图标格式非png或者webp格式。
   * 自定义快捷方式图标大小超过100KB。
   * 不支持为其他应用添加快捷方式。
2. [requestNewPinShortcut](<../../../../../harmonyos-references/AppGallery Kit（应用市场服务）/ArkTS API/productViewManager (应用市场推荐)/store-productviewmanager.md#productviewmanagerrequestnewpinshortcut>)创建快捷方式加桌接口：

   * 上下文context为空。
   * 快捷方式校验结果tid为空。
