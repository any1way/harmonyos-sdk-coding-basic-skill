---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkweb-25
title: 多个Cookie如何进行批量设置
breadcrumb: FAQ > 应用框架开发 > Web框架 > Web开发（ArkWeb） > 多个Cookie如何进行批量设置
category: harmonyos-faqs
scraped_at: 2026-06-12T10:35:48+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:5c24b08ae8894f3ad36f06062b80393f1aae3ed45eec85d8e09f0ff8078029fa
---
[Class (WebCookieManager)](<../../../../../harmonyos-references/ArkWeb（方舟Web）/ArkTS API/@ohos.web.webview (Webview)/Class (WebCookieManager)/arkts-apis-webview-webcookiemanager.md>)提供了[configCookieSync](<../../../../../harmonyos-references/ArkWeb（方舟Web）/ArkTS API/@ohos.web.webview (Webview)/Class (WebCookieManager)/arkts-apis-webview-webcookiemanager.md#configcookiesync11>)方法与[configCookie](<../../../../../harmonyos-references/ArkWeb（方舟Web）/ArkTS API/@ohos.web.webview (Webview)/Class (WebCookieManager)/arkts-apis-webview-webcookiemanager.md#configcookie11>)方法，用于同步和异步设置 Cookie。目前，接口不支持一次性批量设置多个 Cookie，建议通过多次调用 `configCookie` 或 `configCookieSync` 方法来实现多个 Cookie 的设置。

```
1. import { webview } from '@kit.ArkWeb';

3. webview.once("webInited", () => {
4. console.info("webInited setCookie");
5. webview.WebCookieManager.configCookie("https://www.example.com", 'a=b');
6. webview.WebCookieManager.configCookie("https://www.example.com", 'c=d');
7. webview.WebCookieManager.configCookie("https://www.example.com", 'e=f');
8. })

10. @Entry
11. @Component
12. struct LoginCookieConfig {
13. controller: webview.WebviewController = new webview.WebviewController();

15. build() {
16. Column() {
17. Button('fetchCookieSync')
18. .onClick(() => {
19. try {
20. let value = webview.WebCookieManager.fetchCookieSync('https://www.example.com');
21. console.log(`fetchCookieSync cookie value is: ${value}`);
22. } catch (error) {
23. console.error(`fetchCookieSync failed,error is: ${JSON.stringify(error)}`);
24. }
25. })
26. Web({ src: 'www.example.com', controller: this.controller })
27. }
28. }
29. }
```

[LoginCookieConfig.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/ArkWebKit/entry/src/main/ets/pages/LoginCookieConfig.ets#L21-L49)
