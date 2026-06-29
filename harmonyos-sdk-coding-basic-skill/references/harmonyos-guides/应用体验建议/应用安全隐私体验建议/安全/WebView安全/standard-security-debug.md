---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/standard-security-debug
title: WebView安全
breadcrumb: 指南 > 应用体验建议 > 应用安全隐私体验建议 > 安全 > WebView安全
category: harmonyos-guides
scraped_at: 2026-06-01T15:29:00+08:00
doc_updated_at: 2026-01-28
content_hash: sha256:faa2ae0d913bb35f89e9adb88cc817ebbd824c0c68bf4382c310a82291017982
---
|  |  |
| --- | --- |
| 描述 | 不加载不安全的URL或页面。 |
| 类型 | 建议 |
| 适用设备 | 手机，平板，PC/2in1，智慧屏，车机 |
| 应用形态适用性 | 鸿蒙应用，鸿蒙元服务 |
| 说明 | 实现方案参考[最佳实践](../../../../../best-practices/应用安全/应用安全编码实践/bpta-harmony-application-security.md#section1113104054110) |

|  |  |
| --- | --- |
| 描述 | 不能将mixedMode属性配置成All。 |
| 类型 | 建议 |
| 适用设备 | 手机，平板，PC/2in1，智慧屏，车机 |
| 应用形态适用性 | 鸿蒙应用，鸿蒙元服务 |
| 说明 | 实现方案参考[最佳实践](../../../../../best-practices/应用安全/应用安全编码实践/bpta-harmony-application-security.md#section4947114114317) |

|  |  |
| --- | --- |
| 描述 | 在加载webview页面时不得在SSL校验出错时继续加载页面。 |
| 类型 | 规则 |
| 适用设备 | 手机，平板，PC/2in1，智慧屏，车机，穿戴 |
| 应用形态适用性 | 鸿蒙应用，鸿蒙元服务 |
| 说明 | 实现方案参考[最佳实践](../../../../../best-practices/应用安全/应用安全编码实践/bpta-harmony-application-security.md#section1256314434316) |

|  |  |
| --- | --- |
| 描述 | 未经用户同意不得在WebView页面返回位置信息。 |
| 类型 | 规则 |
| 适用设备 | 手机，平板，PC/2in1，智慧屏，车机，穿戴 |
| 应用形态适用性 | 鸿蒙应用，鸿蒙元服务 |
| 说明 | 实现方案参考[最佳实践](../../../../../best-practices/应用安全/应用安全编码实践/bpta-harmony-application-security.md#section12671987440) |
