---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-print-print-printerinfo
title: Print_PrinterInfo
breadcrumb: API参考 > 系统 > 基础功能 > Basic Services Kit（基础服务） > C API > 结构体 > Print_PrinterInfo
category: harmonyos-references
scraped_at: 2026-06-11T16:18:44+08:00
doc_updated_at: 2026-06-09
content_hash: sha256:aeedd2f44e59f36d8c0a88b30002df5365277a37f90935f6ae7444903fbbb4e7
---
```
1. typedef struct {...} Print_PrinterInfo
```

## 概述

PhonePC/2in1Tablet

表示打印机信息。

**起始版本：** 12

**相关模块：** [OH\_Print](../../模块/OH_Print/capi-oh-print.md)

**所在头文件：** [ohprint.h](../../头文件/ohprint.h/capi-ohprint-h.md)

## 汇总

PhonePC/2in1Tablet

### 成员变量

PhonePC/2in1Tablet

| 名称 | 描述 |
| --- | --- |
| [Print\_PrinterState](../../头文件/ohprint.h/capi-ohprint-h.md#print_printerstate) printerState | 打印机状态。 |
| [Print\_PrinterCapability](../Print_PrinterCapability/capi-oh-print-print-printercapability.md) capability | 打印机能力。 |
| [Print\_DefaultValue](../Print_DefaultValue/capi-oh-print-print-defaultvalue.md) defaultValue | 打印机当前属性。 |
| bool isDefaultPrinter | 默认打印机。 |
| char \*printerId | 打印机 ID。 |
| char \*printerName | 打印机名称。 |
| char \*description | 打印机描述。 |
| char \*location | 打印机位置。 |
| char \*makeAndModel | 打印机品牌和型号信息。 |
| char \*printerUri | 打印机 URI。 |
| char \*detailInfo | JSON 格式的详细信息。  支持的键包括：  - **printerAlias**：string类型，表示打印机别名，**起始版本：** 24。  - **vendorId**：int类型，表示USB打印机的VID，**起始版本：** 12。  - **productId**：int类型，表示USB打印机的PID，**起始版本：** 12。  - **protocol**：string数组，表示探测到的打印机支持的协议列表，**起始版本：** 24。  - **ipp**：string类型，表示探测到的IPP协议对应的打印机URI，**起始版本：** 24。  - **ipps**：string类型，表示探测到的IPPS协议对应的打印机URI，**起始版本：** 24。  - **lpd**：string类型，表示探测到的LPD协议对应的打印机URI，**起始版本：** 24。  - **socket**：string类型，表示探测到的Socket协议对应的打印机URI，**起始版本：** 24。 |
