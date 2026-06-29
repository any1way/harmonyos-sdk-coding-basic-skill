---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ndk-63
title: 如何通过多个xxx.d.ts文件导出Native侧接口
breadcrumb: FAQ > 应用框架开发 > NDK开发 > NDK开发 > 如何通过多个xxx.d.ts文件导出Native侧接口
category: harmonyos-faqs
scraped_at: 2026-06-12T10:25:31+08:00
doc_updated_at: 2026-03-17
content_hash: sha256:fbc3e8caf2b4334f186045b86a2b17f636692c4c1e7ce5e8465b8b836d65943b
---

**问题现象**

由于底层C++库规模较大，向外暴露的接口数量较多，建议将其拆分成多个.d.ts文件以便归类。

**解决措施**

在oh-package.json5中的types字段只能指定一个出口。如果需要封装多个.d.ts文件中的接口，可以使用重导出的方式。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dc/v3/6rVGt5CeTuC-U8uKSe8rEA/zh-cn_image_0000002194318472.png?HW-CC-KV=V1&HW-CC-Date=20260612T022530Z&HW-CC-Expire=86400&HW-CC-Sign=70DFC0757BFA9392C401E244B295AED92E37B1EEFBFA3832209F7C0C76FDD4BC "点击放大")

实现方式：

在index1.d.ts文件中声明Native侧导出接口，然后通过index.d.ts文件重导出到ArkTS侧使用。

在index1.d.ts文件中导出接口。

```
1. export const sub: (a: number, b: number) => number;
```

[index1.d.ts](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/Ndk/ndk1/Modulea/src/main/cpp/types/libmodulea/index1.d.ts#L5-L5)

在index.d.ts文件中重导出这些接口。

```
1. export {sub} from './index1'
2. export const add: (a: number, b: number) => number;
```

[Index.d.ts](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/Ndk/ndk1/Modulea/src/main/cpp/types/libmodulea/Index.d.ts#L5-L6)
