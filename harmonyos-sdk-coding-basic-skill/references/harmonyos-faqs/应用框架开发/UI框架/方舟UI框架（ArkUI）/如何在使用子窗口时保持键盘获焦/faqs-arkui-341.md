---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-341
title: 如何在使用子窗口时保持键盘获焦
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > 如何在使用子窗口时保持键盘获焦
category: harmonyos-faqs
scraped_at: 2026-06-12T10:31:19+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:9ce2bddc40ede753bb3d8e09dae46c59600cf8d7dd5661548bfac964e008a275
---
**解决措施**

可以使用窗口@ohos.window的[keepKeyboardOnFocus](<../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS API/窗口管理/@ohos.window (窗口)/Interface (Window)/arkts-apis-window-window.md#keepkeyboardonfocus11>)接口，该接口可在窗口获焦时保留由其他窗口创建的软键盘，但仅支持系统窗口与应用子窗口，调用此接口前需确保窗口已获得焦点，且仅当软键盘由其他窗口创建时才有效。
