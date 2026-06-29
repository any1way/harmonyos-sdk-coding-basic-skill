---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-462
title: AppStorage存了对象之后里面的值取不出来，什么原因
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > AppStorage存了对象之后里面的值取不出来，什么原因
category: harmonyos-faqs
scraped_at: 2026-06-12T10:33:33+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:9bf3c61a1f4b03f1986e45ba486b158a76fe4371fa27e9a90cb19885a5ac1bc5
---
**问题描述**

AppStorage存的数据取不出来，存储包含字符串数组的对象时会出现异常。

**解决措施**

AppStorage结合PersistentStorage实现持久化存储UI状态时，可以存储字符串数据，但不支持嵌套对象（对象数组，对象的属性是对象等）。因为目前框架无法检测AppStorage中嵌套对象（包括数组）值的变化，所以无法写回到PersistentStorage中。

**参考链接**

[PersistentStorage：持久化存储UI状态](<../../../../../harmonyos-guides/应用框架/ArkUI（方舟UI框架）/UI开发 (ArkTS声明式开发范式)/学习UI范式状态管理/状态管理（V1）/管理应用拥有的状态/PersistentStorage：持久化存储UI状态/arkts-persiststorage.md#限制条件>)
