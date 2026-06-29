---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-network-9
title: http请求的官方示例代码中的extraData是什么类型
breadcrumb: FAQ > 系统开发 > 网络 > 网络（Network） > http请求的官方示例代码中的extraData是什么类型
category: harmonyos-faqs
scraped_at: 2026-06-12T10:37:24+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:54de933983f5817372cb3c88a5ea1972d3488c73c98d364d1d906a3276bf37cd
---
1. 文档中对extraData的定义是“extraData?: string | Object | ArrayBuffer”，也就是extraData支持string、Object和ArrayBuffer三种类型。
2. 有如下三种方法可供选择。

   ```
   1. 1）extraData:"data to send";
   2. 2）extraData:{ data: "data to send", };
   3. 3）extraData:{ data: new ArrayBuffer(1)};
   ```

   [ExtraData.txt](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/NetworkKit/entry/src/main/ets/pages/ExtraData.txt#L8-L10)

**参考链接**

[HttpRequestOptions](<../../../../../harmonyos-references/网络/Network Kit（网络服务）/ArkTS API/@ohos.net.http (数据请求)/js-apis-http.md#httprequestoptions>)
