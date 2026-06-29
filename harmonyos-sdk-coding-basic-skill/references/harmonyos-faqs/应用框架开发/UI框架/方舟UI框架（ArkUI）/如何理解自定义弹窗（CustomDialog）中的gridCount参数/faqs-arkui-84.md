---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-84
title: 如何理解自定义弹窗（CustomDialog）中的gridCount参数
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > 如何理解自定义弹窗（CustomDialog）中的gridCount参数
category: harmonyos-faqs
scraped_at: 2026-06-12T10:27:08+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:17759a6e6c7d8c38ebdfddf6b040d43a93f275d4a3d8675988e130c2dabddf25
---
gridCount参数表示弹窗宽度占用的栅格列数。系统将窗口宽度等分为若干栅格列，不同设备的栅格列数不同。例如，手机屏幕密度值在320vp到600vp之间时，栅格列数为4，gridCount的有效值为1到4。

**参考链接**

[CustomDialogControllerOptions（包含gridCount等参数）](<../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/弹窗/自定义弹窗 (CustomDialog)/ts-methods-custom-dialog-box.md#customdialogcontrolleroptions对象说明>)
