---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ason-parsing-generation
title: ASON解析与生成
breadcrumb: 指南 > 应用框架 > ArkTS（方舟编程语言） > ArkTS并发 > 并发线程间通信 > 线程间通信对象 > Sendable对象 > ASON解析与生成
category: harmonyos-guides
scraped_at: 2026-06-11T14:27:09+08:00
doc_updated_at: 2026-06-03
content_hash: sha256:bb9683a7694222ee16a3d0884b018f5a3d8e70b466a85b8d79ded9bf730d3aab
---
[ASON](<../../../../../../../../harmonyos-references/ArkTS（方舟编程语言）/ArkTS API/@arkts.utils (ArkTS工具库)/ArkTSUtils.ASON/arkts-apis-arkts-utils-ason.md>)工具与JS提供的JSON工具类似，JSON用于进行JS对象的序列化（stringify）、反序列化（parse）。ASON则提供了[Sendable对象](../Sendable对象简介/arkts-sendable.md)的序列化、反序列化能力。使用ASON.stringify方法可将对象转换为字符串，使用ASON.parse方法可将字符串转换为Sendable对象，从而实现对象在并发任务间的高性能引用传递。

ASON.stringify方法还支持将Map和Set对象转换为字符串，可转换的Map和Set类型包括：Map、Set、[collections.Map](<../../../../../../../../harmonyos-references/ArkTS（方舟编程语言）/ArkTS API/@arkts.collections (ArkTS容器集)/Class (Map)/arkts-apis-arkts-collections-map.md>)、[collections.Set](<../../../../../../../../harmonyos-references/ArkTS（方舟编程语言）/ArkTS API/@arkts.collections (ArkTS容器集)/Class (Set)/arkts-apis-arkts-collections-set.md>)、[HashMap](<../../../../../../../../harmonyos-references/ArkTS（方舟编程语言）/ArkTS API/@ohos.util.HashMap (非线性容器HashMap)/js-apis-hashmap.md#hashmap>)、[HashSet](<../../../../../../../../harmonyos-references/ArkTS（方舟编程语言）/ArkTS API/@ohos.util.HashSet (非线性容器HashSet)/js-apis-hashset.md#hashset>)。

说明

ASON.parse默认生成的对象为Sendable对象，布局不可变，不支持增删属性。如果返回的对象需要支持增删属性，可以指定返回类型为[collections.Map](<../../../../../../../../harmonyos-references/ArkTS（方舟编程语言）/ArkTS API/@arkts.collections (ArkTS容器集)/Class (Map)/arkts-apis-arkts-collections-map.md>)对象。

## 使用示例

使用ASON提供的接口，对[Sendable对象](../Sendable对象简介/arkts-sendable.md)进行序列化、反序列化。

```
1. import { ArkTSUtils, collections } from '@kit.ArkTS';

3. @Entry
4. @Component
5. struct Index {
6. @State message: string = 'Hello World';

8. build() {
9. RelativeContainer() {
10. Text(this.message)
11. .id('HelloWorld')
12. .fontSize(50)
13. .fontWeight(FontWeight.Bold)
14. .alignRules({
15. center: { anchor: '__container__', align: VerticalAlign.Center },
16. middle: { anchor: '__container__', align: HorizontalAlign.Center }
17. })
18. .onClick(() => {
19. console.info(ArkTSUtils.ASON.parse('{}'));
20. console.info(ArkTSUtils.ASON.stringify(new collections.Array(1, 2, 3)));

22. let options2: ArkTSUtils.ASON.ParseOptions = {
23. bigIntMode: ArkTSUtils.ASON.BigIntMode.PARSE_AS_BIGINT,
24. parseReturnType: ArkTSUtils.ASON.ParseReturnType.MAP,
25. }
26. let jsonText = '{"largeNumber":112233445566778899}';
27. let map = ArkTSUtils.ASON.parse(jsonText, undefined, options2);
28. // 执行结果为：{"largeNumber":112233445566778899}
29. console.info(ArkTSUtils.ASON.stringify(map));
30. this.message = 'success';
31. })
32. }
33. .height('100%')
34. .width('100%')
35. }
36. }
```

[AsonParsingGeneration.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkTS/ArkTsConcurrent/ConcurrentThreadCommunication/InterThreadCommunicationObjects/SendableObject/SendableObjectRelated/entry/src/main/ets/managers/AsonParsingGeneration.ets#L16-L53)
