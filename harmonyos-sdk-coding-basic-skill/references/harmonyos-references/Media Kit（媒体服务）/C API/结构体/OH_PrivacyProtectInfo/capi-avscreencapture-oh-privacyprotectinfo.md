---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-avscreencapture-oh-privacyprotectinfo
title: OH_PrivacyProtectInfo
breadcrumb: API参考 > 媒体 > Media Kit（媒体服务） > C API > 结构体 > OH_PrivacyProtectInfo
category: harmonyos-references
scraped_at: 2026-06-01T16:25:13+08:00
doc_updated_at: 2026-04-30
content_hash: sha256:1ee30a6888d6e777d589f910e281a81294adad5aa3e61ad799eddb1407cd0a96
---
```
1. typedef struct {...} OH_PrivacyProtectInfo
```

## 概述

PhonePC/2in1TabletTV

隐私保护信息结构体。

**起始版本：** 24

**相关模块：** [AVScreenCapture](../../模块/AVScreenCapture/capi-avscreencapture.md)

**所在头文件：** [native\_avscreen\_capture\_base.h](../../头文件/native_avscreen_capture_base.h/capi-native-avscreen-capture-base-h.md)

## 汇总

PhonePC/2in1TabletTV

### 成员变量

PhonePC/2in1TabletTV

| 名称 | 描述 |
| --- | --- |
| bool systemWindowProtection | 是否开启系统窗口隐私保护。true表示开启隐私保护，false表示关闭隐私保护。  **起始版本：** 24 |
| bool sensitiveAppProtection | 是否开启敏感应用的隐私保护。true表示开启隐私保护，false表示关闭隐私保护。  **起始版本：** 24 |
