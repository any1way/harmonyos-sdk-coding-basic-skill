---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkweb-26
title: 登录信息的cookie应该在什么时机注入？如何确保刚刚打开的web能注入登录信息cookie
breadcrumb: FAQ > 应用框架开发 > Web框架 > Web开发（ArkWeb） > 登录信息的cookie应该在什么时机注入？如何确保刚刚打开的web能注入登录信息cookie
category: harmonyos-faqs
scraped_at: 2026-06-12T10:35:49+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:0456fb85239f4b115bcda336e6405d1caf58e0e7433c97085ead812d2d440605
---
[webview.once](<../../../../../harmonyos-references/ArkWeb（方舟Web）/ArkTS API/@ohos.web.webview (Webview)/Functions/arkts-apis-webview-f.md#webviewonce>)可以订阅一次指定类型Web事件的回调。一般在web初始化完成后可以注入。

```
1. import { webview } from '@kit.ArkWeb'

3. webview.once("webInited", () => {
4. console.log("setCookie");
5. webview.WebCookieManager.configCookie("https://www.example.com", 'a=b,c=d,e=f');
6. })

8. @Entry
9. @Component
10. struct WebComponent {
11. controller: webview.WebviewController = new webview.WebviewController();

13. build() {
14. Column() {
15. Web({ src: 'www.example.com', controller: this.controller })
16. }
17. }
18. }
```

[CookieInject.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/ArkWebKit/entry/src/main/ets/pages/CookieInject.ets#L21-L38)
