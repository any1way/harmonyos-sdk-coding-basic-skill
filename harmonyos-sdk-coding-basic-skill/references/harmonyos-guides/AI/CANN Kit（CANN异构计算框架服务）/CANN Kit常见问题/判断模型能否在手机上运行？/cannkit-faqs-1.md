---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-faqs-1
title: 判断模型能否在手机上运行？
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > CANN Kit常见问题 > 判断模型能否在手机上运行？
category: harmonyos-guides
scraped_at: 2026-06-01T15:13:13+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:f53cdc286c54e87772ec180486b95977052b9a34027d6e42650890a178d37b18
---
通过调用接口[HMS\_HiAICompatibility\_CheckFromFile](<../../../../../harmonyos-references/CANN Kit（CANN异构计算框架服务）/C API/模块/CANN/cannkit.md#hms_hiaicompatibility_checkfromfile>)或者[HMS\_HiAICompatibility\_CheckFromBuffer](<../../../../../harmonyos-references/CANN Kit（CANN异构计算框架服务）/C API/模块/CANN/cannkit.md#hms_hiaicompatibility_checkfrombuffer>)，传入编译后的模型文件或者模型buffer，如果返回“HIAI\_COMPATIBILITY\_COMPATIBLE”表示兼容性检查通过，模型可以在手机上运行。
