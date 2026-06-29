---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-local-database-management-33
title: 如何获知数据存储沙箱路径
breadcrumb: FAQ > 应用框架开发 > 本地数据和文件 > 本地数据库管理 > 如何获知数据存储沙箱路径
category: harmonyos-faqs
scraped_at: 2026-06-12T10:34:35+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:83aa9e506cd56fd8820b1742a909f328b02eb51fb33b2adeec7ffac43fb1e631
---
关系型数据库：

"/data/app/el2/100/database/(bundleName)/entry/rdb/"下的.db文件

键值型数据库：

"/data/app/el2/100/database/(bundleName)/entry/kvdb/<系统默认生成文件名>/single\_ver/main/"路径下的.db文件

首选项：

"data/app/el2/100/base/(bundleName)/haps/entry/preferences"路径下的文件

应用持久化存储路径：

"/data/app/el2/100/base/(bundleName)/haps/<模块名>/files/persistent\_storage"

通过[获取应用文件路径](<../../../../../harmonyos-guides/应用框架/Ability Kit（程序框架服务）/Stage模型开发指导/Stage模型应用组件/应用上下文Context/application-context-stage.md#获取应用文件路径>)获取kvStore、Rdb路径前缀databaseDir和preferences路径前缀preferencesDir，后面自行拼接。
