---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-136
title: 编译报错“The required attribute: module-name is missing”
breadcrumb: FAQ > DevEco Studio > 编译构建 > 编译报错“The required attribute: module-name is missing”
category: harmonyos-faqs
scraped_at: 2026-06-12T10:42:58+08:00
doc_updated_at: 2026-06-05
content_hash: sha256:771993aa5e86c4b59582e68e6e97077bf865759bbb072674686aa34be7f99ae6
---
**错误描述**

缺少必需属性：module-name。

**可能原因**

1. build-profile.json5 文件中缺少模块名称。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5d/v3/mM7DOndFSkqyFk9w9eFhYw/zh-cn_image_0000002229758649.png?HW-CC-KV=V1&HW-CC-Date=20260612T024257Z&HW-CC-Expire=86400&HW-CC-Sign=9A7094B917F5C6C4111A85539C6A545542D3D1E0337A8CA278E894C9B12E6EF5)
2. 在hvigorconfig.ts中动态添加模块时未设置模块名。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b1/v3/tSfsm9l6RUCUIIK7S03twg/zh-cn_image_0000002194158776.png?HW-CC-KV=V1&HW-CC-Date=20260612T024257Z&HW-CC-Expire=86400&HW-CC-Sign=83990E2770F1B2E3DF946A272ABD0AF472E021C887BEF97109F6E2D9C7D34932)

**解决措施**

1. 进入项目根目录下的build-profile.json5文件，确保module下有非空的name字段。
2. 进入项目根目录下的hvigorconfig.ts文件，确保includeNode方法的参数name字段存在且非空。

**参考链接**

[Hvigor脚本文件](../../../../harmonyos-guides/构建应用/概述/构建系统生命周期/ide-hvigor-life-cycle.md#section810245135914)
