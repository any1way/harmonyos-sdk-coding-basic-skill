---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-90
title: 如何将ArrayBuffer转成string
breadcrumb: FAQ > 应用框架开发 > ArkTS语言 > 方舟编程语言（ArkTS） > 如何将ArrayBuffer转成string
category: harmonyos-faqs
scraped_at: 2026-06-12T10:23:14+08:00
doc_updated_at: 2026-03-17
content_hash: sha256:59483dfdf2d41ab61766d844469e8971490363fc9f57928bbf586e9e2c249013
---
可以通过util.TextDecoder.create()方法创建一个实例，再通过[decodeToString()](<../../../../../harmonyos-references/ArkTS（方舟编程语言）/ArkTS API/@ohos.util (util工具函数)/js-apis-util.md#decodetostring12>)方法进行转换。

```
1. let decoder = util.TextDecoder.create('utf-8');
2. let str = decoder.decodeToString(new Uint8Array(arrayBuffer));
```

[TextDecoder.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkTS/entry/src/main/ets/pages/TextDecoder.ets#L36-L37)

开发者可以将 proArrayBuffer 返回的 ArrayBuffer 类型的数据 arrayBufferVal 转换为字符串。

```
1. import { util, buffer } from '@kit.ArkTS';

3. let blobValue: buffer.Blob = new buffer.Blob(['name', 'age', 'sex']);
4. let proArrayBuffer = blobValue.arrayBuffer();

6. proArrayBuffer.then((arrayBufferVal: ArrayBuffer) => {
7. let decoder = util.TextDecoder.create('utf-8');
8. let stringData = decoder.decodeToString(new Uint8Array(arrayBufferVal));
9. console.log('stringData:', stringData);
10. });
```

[TextDecoder.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkTS/entry/src/main/ets/pages/TextDecoder.ets#L21-L30)
