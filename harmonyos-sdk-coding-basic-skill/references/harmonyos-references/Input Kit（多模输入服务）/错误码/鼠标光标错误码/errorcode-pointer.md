---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-pointer
title: 鼠标光标错误码
breadcrumb: API参考 > 系统 > 基础功能 > Input Kit（多模输入服务） > 错误码 > 鼠标光标错误码
category: harmonyos-references
scraped_at: 2026-06-11T16:20:44+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:dd0eb78ac435dad67ca1b71c134ade7aaeb8af7edcfdb4c8ac69257501d8c97e
---
说明

* 以下仅介绍本模块特有错误码，通用错误码请参考[通用错误码说明文档](../../../../通用错误码/errorcode-universal.md)。

## 26500001 无效的windowId

PhonePC/2in1TabletTV

**错误信息**

Invalid windowId. Possible causes: The window id does not belong to the current process.

**错误描述**

无效的窗口ID。

**可能原因**

窗口ID不属于当前进程。

**处理步骤**

请检查并传入当前进程的窗口ID，可通过windowClass.[getWindowProperties()](<../../../../ArkUI（方舟UI框架）/ArkTS API/窗口管理/@ohos.window (窗口)/Interface (Window)/arkts-apis-window-window.md#getwindowproperties9>)接口获取当前窗口属性，窗口属性中含有窗口ID。

## 3800001 多模输入服务内部错误

PhoneTV

**错误信息**

Input service exception. Possible causes: 1. Memory allocation failure. 2. Thread busy. 3. Service terminated abnormally. 4. Other unexpected errors. Try again later.

**错误描述**

多模输入服务内部错误。

**可能原因**

内存分配失败，线程繁忙，服务异常退出等非预期错误。

**处理步骤**

建议稍后重试。
