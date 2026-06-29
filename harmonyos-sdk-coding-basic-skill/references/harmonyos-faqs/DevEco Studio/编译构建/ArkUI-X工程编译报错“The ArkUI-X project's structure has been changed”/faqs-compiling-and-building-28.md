---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-28
title: ArkUI-X工程编译报错“The ArkUI-X project's structure has been changed”
breadcrumb: FAQ > DevEco Studio > 编译构建 > ArkUI-X工程编译报错“The ArkUI-X project's structure has been changed”
category: harmonyos-faqs
scraped_at: 2026-06-12T10:41:19+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:cb8fdd68a17f9c5d404b12d36e5dc56fca3a986d5c1bbbb5ec15491b32420738
---

**问题现象**

使用DevEco Studio 4.0.0.700及以上版本打开ArkUI-X历史工程时，工程同步或构建会提示“ERROR: The ArkUI-X project's structure has been changed. Migrate and adapt the project as instructed in FAQs.”。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8f/v3/9M4wtzVzQCu4OfaJuBYQiA/zh-cn_image_0000002194158592.png?HW-CC-KV=V1&HW-CC-Date=20260612T024118Z&HW-CC-Expire=86400&HW-CC-Sign=7B138649CC88781EFD9624E9F388F2C261A01B3CDBC7C5D7C8FBA698EA5EDCF4)

**解决措施**

出现该提示的原因是在旧版本的ArkUI-X工程模板中，ArkUI-X工程标识（"crossplatform": true）配置在工程目录下build-profile.json5中，在DevEco Studio 4.0.0.700及以上版本需要在工程目录下.arkui-x/arkui-x-config.json5文件中配置ArkUI-X工程模块、工程标识等信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2d/v3/RdeR70NnSpui0d1U4H6ktw/zh-cn_image_0000002229758465.png?HW-CC-KV=V1&HW-CC-Date=20260612T024118Z&HW-CC-Expire=86400&HW-CC-Sign=44F5C848A10BBE2A0574386AF2BF555ECB3C5E080F94DA4F3EB099AEBC432E88)

配置位置变更后，使用历史工程模板的开发者，如果使用DevEco Studio 4.0.0.700及以上版本，需手动迁移适配新的工程结构。迁移步骤如下：

1. 删除工程目录下build-profile.json5中的ArkUI-X工程标识（"crossplatform": true）。
2. 在工程下.arkui-x目录中新建arkui-x-config.json5文件，配置内容为 "crossplatform": true, "modules"中配置工程中所有ArkUI-X模块的module name。

   工程迁移后结构如下：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/56/v3/-4ZSANR0QKGnhJTaq90d8w/zh-cn_image_0000002229758461.png?HW-CC-KV=V1&HW-CC-Date=20260612T024118Z&HW-CC-Expire=86400&HW-CC-Sign=E2F85BAA0985CA54F741C1C0D26EEC31ACEEDB2F9C3A2A3BEC8FA01ADDAD5CC8)
3. 迁移完成后，点击菜单栏 File > Sync and Refresh Project 同步工程，然后重新编译构建。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d7/v3/glsKz-1rRjWGKecsOTus0A/zh-cn_image_0000002229603993.png?HW-CC-KV=V1&HW-CC-Date=20260612T024118Z&HW-CC-Expire=86400&HW-CC-Sign=FA0099326588EE87F83CC1CAC698F300177C56905B8916AA53601EAC32F4A9DF)
