---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-styled-string
title: 属性字符串错误码
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > 错误码 > UI界面 > 属性字符串错误码
category: harmonyos-references
scraped_at: 2026-06-01T15:53:57+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:ce0eb1441f73bc215b22c960642ce12b49c1f55ca1388d66ed2ff780d8e787d9
---
说明

以下仅介绍本模块特有错误码，通用错误码请参考[通用错误码说明文档](../../../../通用错误码/errorcode-universal.md)。

## 170001 转换错误

**错误信息**

Convert Error.

**错误描述**

fromHtml无法将传入的字符串转换出对应的属性字符串。

**可能原因**

字符串为空或字符串不符合HTML格式。

**处理步骤**

NA

## 180101 无效的属性字符串

**错误信息**

invalid styled string.

**错误描述**

属性字符串序列化CAPI中，ArkUI\_StyledString\_Descriptor的属性字符串对象为空。

**可能原因**

参数中传递属性字符串有误。

**处理步骤**

检查参数中是否正确传递属性字符串。
