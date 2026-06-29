---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-env
title: 环境变量错误码
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > 错误码 > UI界面 > 环境变量错误码
category: harmonyos-references
scraped_at: 2026-06-01T15:54:11+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:5386ddcecfdca85784e3406acdf1d5c730653562d5846ae105868554de7d0cd0
---
说明

以下仅介绍本模块特有错误码，通用错误码请参考[通用错误码](../../../../通用错误码/errorcode-universal.md)。

## 140000 @Env非法入参

**错误信息**

Invalid key for @Env

**错误描述**

[@Env](../../../ArkTS组件/响应式环境变量/@Env：环境变量/ts-env-system-property.md#env)非法入参。

**可能原因**

@Env入参非法。@Env仅支持[SystemProperties](../../../ArkTS组件/响应式环境变量/@Env：环境变量/ts-env-system-property.md#systemproperties)类型参数，详情见[@Env支持参数](<../../../../../harmonyos-guides/应用框架/ArkUI（方舟UI框架）/UI开发 (ArkTS声明式开发范式)/学习响应式环境变量/@Env：环境变量/arkts-env-system-property.md#env支持参数>)。

**处理步骤**

确保@Env参数类型为[SystemProperties](../../../ArkTS组件/响应式环境变量/@Env：环境变量/ts-env-system-property.md#systemproperties)，详情见[@Env支持开发指南](<../../../../../harmonyos-guides/应用框架/ArkUI（方舟UI框架）/UI开发 (ArkTS声明式开发范式)/学习响应式环境变量/@Env：环境变量/arkts-env-system-property.md>)。
