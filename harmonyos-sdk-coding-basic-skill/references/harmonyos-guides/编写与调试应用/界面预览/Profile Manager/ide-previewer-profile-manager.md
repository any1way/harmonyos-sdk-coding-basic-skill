---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-previewer-profile-manager
title: Profile Manager
breadcrumb: 指南 > 编写与调试应用 > 界面预览 > Profile Manager
category: harmonyos-guides
scraped_at: 2026-06-11T15:28:23+08:00
doc_updated_at: 2026-03-17
content_hash: sha256:b139e775e6f3052a27876dce5508d8a8b0a72dd12de410696443fbaf8160dbeb
---
由于真机设备型号众多，不同设备型号的屏幕分辨率可能各不相同。因此，在HarmonyOS应用/元服务开发过程中，为了适配多种设备型号，可能需要查看不同设备上的界面显示效果。对此，DevEco Studio的预览器提供了Profile Manager功能，支持开发者自定义预览设备Profile（包含分辨率和语言），从而可以通过定义不同的预览设备Profile，查看HarmonyOS应用/元服务在不同设备上的预览显示效果。当前支持自定义设备分辨率及系统语言。

定义设备后，可以在Previewer右上角，单击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c8/v3/inzmtkckRQWI5ZUOuCkMvg/zh-cn_image_0000002602065919.png?HW-CC-KV=V1&HW-CC-Date=20260611T072558Z&HW-CC-Expire=86400&HW-CC-Sign=A0198A99B27A3CA9A62AD770F144FCB8EB551DDD7E8DC982B2F71D9CC62D56D8)按钮，打开Profile管理器，切换预览设备。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/48/v3/fMVN3HihTYaek8Um4YYZPQ/zh-cn_image_0000002571546440.png?HW-CC-KV=V1&HW-CC-Date=20260611T072558Z&HW-CC-Expire=86400&HW-CC-Sign=EFA9A4B1359F69C49B9545EDAA846089359AFB3608DB3E84D969E56FD6536319)

同时，Profile Manager还支持多设备预览功能，具体请参考[查看多端设备预览效果](../查看多端设备预览效果/ide-previewer-multi-profile.md)。

下面以自定义一款Phone设备为例，介绍设备Profile Manager的使用方法。

1. 在预览器界面，打开Profile Manager界面。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/04/v3/4VjCoI31TlyonexZ0uH3gA/zh-cn_image_0000002571386802.png?HW-CC-KV=V1&HW-CC-Date=20260611T072558Z&HW-CC-Expire=86400&HW-CC-Sign=80AC8143959E4C7D3E90B74B8DFAAE6523987C6EF7CF4A556B9A6E4F121050C1)
2. 在Profile Manager界面，单击**+ New Profile**按钮，添加设备。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f9/v3/7GnltRndR3KXONx1Ta3Y3Q/zh-cn_image_0000002602065917.png?HW-CC-KV=V1&HW-CC-Date=20260611T072558Z&HW-CC-Expire=86400&HW-CC-Sign=DAB22C57789A326D53A8472F0044057987157FE4D8372D9C39F31D72AC2795F0)
3. 在**Create Profile**界面，填写新增设备的信息，如**Profile ID**（设备型号）、**Device type**（设备类型）、**Resolution**（分辨率）和**Language and region**（语言和区域）等。其中Device type只能选择module.json5中deviceTypes字段已定义的设备。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2d/v3/7eESM1hQQOmLkWTVCDvQtQ/zh-cn_image_0000002571386800.png?HW-CC-KV=V1&HW-CC-Date=20260611T072558Z&HW-CC-Expire=86400&HW-CC-Sign=38CB1E82C2D012B8978C82012E3B38B0AC7EE54904A1D412CED745354424E5B4)
4. 设备信息填写完成后，单击**OK**完成创建。
