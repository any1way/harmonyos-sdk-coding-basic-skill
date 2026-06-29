---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-126
title: 如何解决编译报错“Indexed access is not supported for fields(arkts-no-props-by-index)”的问题
breadcrumb: FAQ > DevEco Studio > 编译构建 > 如何解决编译报错“Indexed access is not supported for fields(arkts-no-props-by-index)”的问题
category: harmonyos-faqs
scraped_at: 2026-06-12T10:42:47+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:ae4d147d64a832cf31cddc32e65be68be3e3283bae4dae0cc68415659989a6f5
---

**问题现象**

动态调用类或接口的字段会导致编译报错：Indexed access is not supported for fields (arkts-no-props-by-index)。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8a/v3/e0P2s7BNReuu_BFOmEgVzA/zh-cn_image_0000002229604089.png?HW-CC-KV=V1&HW-CC-Date=20260612T024246Z&HW-CC-Expire=86400&HW-CC-Sign=4CA90D1BC954EAEFB5B093BA252520AA4E88191F2DBAF56EFE2400DBDAE4F5CE)

**解决方案**

修改代码：

```
1. getValue(breakpoint: string): T {
2. return Reflect.get(this.options, breakpoint) as T;
3. }
```

[BreakPointType.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/CompilingAndBuilding/entry/src/main/ets/commpent/BreakPointType.ets#L19-L21)
