---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-20
title: 编译报错“please check deviceType or distroFilter/distributionFilter of the module”
breadcrumb: FAQ > DevEco Studio > 编译构建 > 编译报错“please check deviceType or distroFilter/distributionFilter of the module”
category: harmonyos-faqs
scraped_at: 2026-06-12T10:41:15+08:00
doc_updated_at: 2026-06-05
content_hash: sha256:d46b4849ddaa92ea89ce8e99b278ccb14500ca7af6a5bd940ffb3a293496d473
---
**问题现象**

HarmonyOS DevEco Studio编译时出现错误，提示如下之一：

* Module: (xxx) and Module: (xxx) are entry, please check deviceType or distroFilter of the module.

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0b/v3/MMa6pDbeRJyPM9rbCWP5vQ/zh-cn_image_0000002229604261.png?HW-CC-KV=V1&HW-CC-Date=20260612T024114Z&HW-CC-Expire=86400&HW-CC-Sign=B904D92B1CB8DE41FD33764F15EC98403B189375D7E3C7A77A77DC550915CC7F)
* Module: (xxx) and Module: (xxx) have the same moduleName, please check deviceType or distroFilter of the module.

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f1/v3/FSSD4MpAQCqu8mFI_zn_Xg/zh-cn_image_0000002194158880.png?HW-CC-KV=V1&HW-CC-Date=20260612T024114Z&HW-CC-Expire=86400&HW-CC-Sign=04C78198928D163C749A7498B139F18221D0A030CA9DF89257581236626FA39E)
* Module: (xxx) and Module: (xxx) have the same packageName, please check deviceType or distroFilter of the module.

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b7/v3/pyFziZ--SEWFlhDextgXIg/zh-cn_image_0000002194318488.png?HW-CC-KV=V1&HW-CC-Date=20260612T024114Z&HW-CC-Expire=86400&HW-CC-Sign=63B1F0C40B8AD3BB498AD05E41BE51C17818BD32ED2693D5D35EEA82D3938B0F)
* Module: (xxx) and Module: (xxx) have the same ability name.

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bc/v3/AxTV5hnJTFGpoivSPQR9mg/zh-cn_image_0000002194318492.png?HW-CC-KV=V1&HW-CC-Date=20260612T024114Z&HW-CC-Expire=86400&HW-CC-Sign=679FCBE697738D55691C1D8667BF23648BC6324F53C84926570F346B01B90D27)

**解决措施**

* 可能是打包时工程未满足HAP唯一性校验逻辑，请参考[HAP唯一性校验逻辑](../../../../harmonyos-guides/构建应用/配置构建流程/HAP唯一性校验逻辑/ide-hvigor-verification-rule.md)修改工程配置，满足校验逻辑即可正常打包。
* 如果工程中仅有一种设备类型，请确保工程级build-profile.json5文件中，同一模块的不同目标target的applyToProducts字段对应的product不相同。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3a/v3/lLi-Y7yeTPSgcbpMS9UGIQ/zh-cn_image_0000002194158884.png?HW-CC-KV=V1&HW-CC-Date=20260612T024114Z&HW-CC-Expire=86400&HW-CC-Sign=4645291BE2098DB35796BB7E40C31C1B0CA7DD4BEE0E1C43149C02F7DAABA339)
