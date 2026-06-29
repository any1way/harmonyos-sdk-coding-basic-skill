---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-thermal
title: 热管理错误码
breadcrumb: API参考 > 系统 > 基础功能 > Basic Services Kit（基础服务） > 错误码 > 热管理错误码
category: harmonyos-references
scraped_at: 2026-06-11T16:19:02+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:c4145adaf03f2c0821b641039ffa5e39e6f9139a8f62e54caaa8de63429c63d5
---
说明

以下仅介绍本模块特有错误码，通用错误码请参考[通用错误码说明文档](../../../../通用错误码/errorcode-universal.md)。

## 4800101 连接服务失败

**错误信息**

Failed to connect to the service.

**错误描述**

操作失败，连接系统服务发生异常。

**可能原因**

1. 系统服务停止运行。
2. 系统服务内部通讯发生异常。

**处理步骤**

检查系统服务是否正常运行。

1. 在控制台中输入如下命令，查看当前的系统服务列表。

   ```
   1. > hdc shell hidumper -ls
   ```
2. 查看系统服务列表中是否包含ThermalService系统服务。
