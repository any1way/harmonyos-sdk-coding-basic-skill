---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkweb-67
title: WebView如何设置mixcontent策略，用以解决http与https混合加载的问题
breadcrumb: FAQ > 应用框架开发 > Web框架 > Web开发（ArkWeb） > WebView如何设置mixcontent策略，用以解决http与https混合加载的问题
category: harmonyos-faqs
scraped_at: 2026-06-12T10:36:14+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:d7963fbefb91737e7a7dc8e6a5132ae123e3de2e3f481cd60de93c15060600b0
---
ArkWeb提供mixedMode(mixedMode: MixedMode)接口，用于设置是否允许加载HTTP和HTTPS混合内容。默认情况下，不允许加载混合内容。

在工程的module.json5配置文件中添加网络访问权限ohos.permission.INTERNET。

参考代码如下：

```
1. // xxx.ets
2. import { webview } from '@kit.ArkWeb';

4. @Entry
5. @Component
6. struct WebComponent {
7. controller: webview.WebviewController = new webview.WebviewController();
8. // MixedMode.All indicates that all mixed content is allowed to be loaded (HTTP/HTTPS)
9. @State mixedMode: MixedMode = MixedMode.All;
10. build() {
11. Column() {
12. Web({ src: 'www.example.com', controller: this.controller })
13. .mixedMode(this.mixedMode)
14. }
15. }
16. }
```

[MixContent.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/ArkWebKit/entry/src/main/ets/pages/MixContent.ets#L21-L36)

**参考链接**

[mixedMode](<../../../../../harmonyos-references/ArkWeb（方舟Web）/ArkTS 组件/Web/属性/arkts-basic-components-web-attributes.md#mixedmode>)
