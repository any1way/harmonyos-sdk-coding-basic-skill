---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-emulator-start-and-close
title: 启动和关闭模拟器
breadcrumb: 指南 > 编写与调试应用 > 使用模拟器运行应用 > 管理模拟器 > 启动和关闭模拟器
category: harmonyos-guides
scraped_at: 2026-06-11T15:28:38+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:cc384f123f7f4415c88c015bc731db5401829f02305087a87da1689cf7c91985
---

在设备管理器页面，单击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/af/v3/NXb7IwJGSMKuU1bX4DX7aA/zh-cn_image_0000002602064787.png?HW-CC-KV=V1&HW-CC-Date=20260611T072838Z&HW-CC-Expire=86400&HW-CC-Sign=E85418A321D48B1ADF36D385E1AF448219AE7C0D95173844476D57B07746591E)即可启动模拟器。模拟器启动时会默认携带之前运行时的用户数据，包括用户上传的文件，安装的应用等。如果是新创建的模拟器，则不会携带用户数据。如果想清除之前运行时的用户数据，点击**Actions >** ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7b/v3/esCGiqy7QFm1iMLU-E2f6g/zh-cn_image_0000002571385672.png?HW-CC-KV=V1&HW-CC-Date=20260611T072838Z&HW-CC-Expire=86400&HW-CC-Sign=E0955ADB5BED38187F14B69FE712A5B17E64472153E13D15BB594C67B66F7ABC) **> Wipe User Data**。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/55/v3/eVlFV5YWTO2E-PiiN-0OcA/zh-cn_image_0000002571385706.png?HW-CC-KV=V1&HW-CC-Date=20260611T072838Z&HW-CC-Expire=86400&HW-CC-Sign=98B8921AB89B6AB0C40B1C10A907817627FCF7D4C9EF3957F124D65593FA1E93 "点击放大")

从DevEco Studio 6.1.0 Beta1版本开始，如果创建模拟器时选择热启动，则启动模拟器时会加载上次关闭时保存的快照，启动后会恢复至上次关闭时的状态。热启动后，多屏状态会恢复为单屏状态，折叠屏模拟器会恢复成默认展开状态。

如果热启动后出现异常，可点击**Actions >** ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f/v3/pC1kbq1fSF-ciE9D0sOl3A/zh-cn_image_0000002602064817.png?HW-CC-KV=V1&HW-CC-Date=20260611T072838Z&HW-CC-Expire=86400&HW-CC-Sign=FE446EAFB876B4F49B095B91C3C725CAB9889FC8CF5616392957FE9C360BE54E) **> Wipe User Data**清除用户数据后重新启动。

例如推包运行后关闭模拟器，再次启动时会显示在上次运行的界面。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/40/v3/dWe5XVyyR2aBYEwbhv50CA/zh-cn_image_0000002571385708.png?HW-CC-KV=V1&HW-CC-Date=20260611T072838Z&HW-CC-Expire=86400&HW-CC-Sign=4BB56A002C56FEF2DDC00B4BFD8EEDFA9CC85CFFD14CA9AAAEA47152BA349286 "点击放大")

在模拟器运行期间，可以点击**Actions >** ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f1/v3/fRVONUE6RcKDh-_900gOtw/zh-cn_image_0000002602184873.png?HW-CC-KV=V1&HW-CC-Date=20260611T072838Z&HW-CC-Expire=86400&HW-CC-Sign=CC4A832AE5B1DADEBDC2427D9642469C27EDD02A066C88DADFDB1170124EFAA2) **> Show on Disk**显示模拟器在本地生成的用户数据。点击**Actions >** ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8b/v3/x2Gb9B2_SBmYMpsG76GNow/zh-cn_image_0000002571545308.png?HW-CC-KV=V1&HW-CC-Date=20260611T072838Z&HW-CC-Expire=86400&HW-CC-Sign=76CB48384F7C036E662044195633BA7A2EF30C59793F36FE90DB463A7D4A3F3F) **> Generate logs**可以生成模拟器自启动到此刻的所有日志信息。想要关闭运行中的模拟器，可以在设备管理器页面点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0b/v3/Mkv_5Xi3Q62514I17uHhkQ/zh-cn_image_0000002571385704.png?HW-CC-KV=V1&HW-CC-Date=20260611T072838Z&HW-CC-Expire=86400&HW-CC-Sign=7DE3468B9BEABED09AE233EF76A524E4AC917BF49CA4B28439CCAA2B97E22722)，或者点击模拟器工具栏上的关闭按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/df/v3/JlJyHAiqQMO-0-uFaZZ78g/zh-cn_image_0000002602064825.png?HW-CC-KV=V1&HW-CC-Date=20260611T072838Z&HW-CC-Expire=86400&HW-CC-Sign=A3A0363C42ECFBA160B7AC7C26BF36ABF3AA9FA7FF99B4744BBA1EF7447910CF)。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e5/v3/SBqJb_1JSPu4JV_oLVOFIw/zh-cn_image_0000002602064783.png?HW-CC-KV=V1&HW-CC-Date=20260611T072838Z&HW-CC-Expire=86400&HW-CC-Sign=50D4AFF7F7215A570EFDB970BAB272BD8490CCEE1BF5505C88CF505E487DB09A "点击放大")

模拟器关闭后，点击**Actions >** ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1c/v3/XDXBiI6SSJS3CNNPiXxvog/zh-cn_image_0000002602064823.png?HW-CC-KV=V1&HW-CC-Date=20260611T072838Z&HW-CC-Expire=86400&HW-CC-Sign=D2FA41653C5200F21861A756AE14A6892CBB24BEF038F007FF8C78482C503B92) **> Delete**可以删除模拟器，并清除模拟器的用户数据和配置信息。
