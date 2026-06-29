---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-profiler-15
title: 录制Snapshot模板时，看不到taskPool线程内存信息
breadcrumb: FAQ > DevEco Studio > 性能分析 > 录制Snapshot模板时，看不到taskPool线程内存信息
category: harmonyos-faqs
scraped_at: 2026-06-12T10:45:27+08:00
doc_updated_at: 2026-03-12
content_hash: sha256:3926b44025b6eb74f0801cc7726deab56ff9c7660ab03172f2c3e05c597ebffe
---
**问题现象**

录制Snapshot模板时，无法看到taskPool线程的内存信息。

**可能原因**

Snapshot模板只支持dump主线程的虚拟机堆内存。

**解决措施**

可使用hidumper --mem-jsheap ${pid} -T ${tid}获取指定进程指定JS线程的虚拟机堆内存，文件生成后导入Profiler查看。详细信息参考[查询虚拟机堆内存](../../../../harmonyos-guides/系统/调测调优/调试命令/hidumper/hidumper/hidumper.md#查询虚拟机堆内存)。
