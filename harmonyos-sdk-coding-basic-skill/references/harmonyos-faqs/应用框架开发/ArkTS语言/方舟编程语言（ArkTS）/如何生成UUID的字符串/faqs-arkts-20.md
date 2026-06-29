---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-20
title: 如何生成UUID的字符串
breadcrumb: FAQ > 应用框架开发 > ArkTS语言 > 方舟编程语言（ArkTS） > 如何生成UUID的字符串
category: harmonyos-faqs
scraped_at: 2026-06-12T10:22:40+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:5d83da670049e20192a62aef3d264454386fdea054295ab68dee44a7d0139540
---
使用util工具的generateRandomUUID函数可以生成字符串类型的UUID，示例如下：

```
1. let uuid = util.generateRandomUUID(true);
2. console.info("RFC 4122 Version 4 UUID:" + uuid); // Output randomly generated UUID
```

[Uuid.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkTS/entry/src/main/ets/pages/Uuid.ets#L7-L8)

**参考链接**

[util.generateRandomUUID](<../../../../../harmonyos-references/ArkTS（方舟编程语言）/ArkTS API/@ohos.util (util工具函数)/js-apis-util.md#utilgeneraterandomuuid9>)
