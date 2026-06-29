---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-15
title: ArkTS中有类似Java中的System.arraycopy数组复制的方法吗
breadcrumb: FAQ > 应用框架开发 > ArkTS语言 > 方舟编程语言（ArkTS） > ArkTS中有类似Java中的System.arraycopy数组复制的方法吗
category: harmonyos-faqs
scraped_at: 2026-06-12T10:22:36+08:00
doc_updated_at: 2026-03-17
content_hash: sha256:90bfd8ad5a4d44a19bddd6841fad9fbd887afedb1c5e858441bd842b99dcd595
---
可以通过 buffer.concat() 方法，将数组中的内容复制到新的 Buffer 对象中并返回。参考代码如下：

```
1. import { buffer } from '@kit.ArkTS';

3. let buf1 = buffer.from("1234");
4. let buf2 = buffer.from("abcd");
5. let buf = buffer.concat([buf1, buf2]);
6. console.info(buf.toString('hex'));
7. // Output result:3132333461626364
```

[Buffer.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkTS/entry/src/main/ets/pages/Buffer.ets#L21-L27)

**参考链接**

[buffer.concat](<../../../../../harmonyos-references/ArkTS（方舟编程语言）/ArkTS API/@ohos.buffer (Buffer)/js-apis-buffer.md#bufferconcat>)
