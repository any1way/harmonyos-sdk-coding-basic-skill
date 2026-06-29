---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-running-20
title: 模拟器在后台放置一段时间后会卡在加载状态，CPU占用率高
breadcrumb: FAQ > DevEco Studio > 应用运行 > 模拟器在后台放置一段时间后会卡在加载状态，CPU占用率高
category: harmonyos-faqs
scraped_at: 2026-06-12T10:44:16+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:c635acdb6b4bd7c8a009449afe593957df9cbb88036915c44bc56ca3a36ab4ee
---

**问题描述**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/26/v3/16e2OoHgRsSO4r6IqeeHQA/zh-cn_image_0000002229603801.png?HW-CC-KV=V1&HW-CC-Date=20260612T024415Z&HW-CC-Expire=86400&HW-CC-Sign=754812D2FEFCFEAF76E0D27ACE17AA8CEAE5E1ED90F848011B13C760CC767D1B)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e0/v3/hkLo7EX2RsqfXEPNcoIqJg/zh-cn_image_0000002194318016.png?HW-CC-KV=V1&HW-CC-Date=20260612T024415Z&HW-CC-Expire=86400&HW-CC-Sign=5B2577AB4F4B79B0FF389DCA009C31C0621A498A93041C11F17780DACC803EF3)

打开活动检测器，发现模拟器的CPU占用率为80%。

**解决措施**

1.打开模拟器设备管理页面。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/12/v3/cas87oX3Sq2MqUb1KhkqZg/zh-cn_image_0000002229603789.png?HW-CC-KV=V1&HW-CC-Date=20260612T024415Z&HW-CC-Expire=86400&HW-CC-Sign=5908BC707D621510B7BE9476B390B9856A24BB2A3E99924FCCE89C351FF863DB)

2.选择“新建模拟器”弹窗。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c7/v3/NVARhxCgQ2-KC1ImAWKeHA/zh-cn_image_0000002194158400.png?HW-CC-KV=V1&HW-CC-Date=20260612T024415Z&HW-CC-Expire=86400&HW-CC-Sign=F348CAE3821FE9ED4519539D754364B059E8938B731D2D93256FB81CF8404194)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d0/v3/Ou8xtBu4TSmimeaxyveHTg/zh-cn_image_0000002229758273.png?HW-CC-KV=V1&HW-CC-Date=20260612T024415Z&HW-CC-Expire=86400&HW-CC-Sign=5AC562F5C0149AC54C0B75F6344871DD32C3D4CA895CA365EDEB6AB54E014ADD)

3.复制路径并用文件夹打开system-image\HarmonyOS-NEXT-DB1\phone\_x86。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f8/v3/c3qE16gnQzuQ2Oe1ekHAvQ/zh-cn_image_0000002229758269.png?HW-CC-KV=V1&HW-CC-Date=20260612T024415Z&HW-CC-Expire=86400&HW-CC-Sign=489CCFE8D610CEB4D17218B50D5F9D9BE045C50CC36F6FA71DA7B5B6C476DD4A)

4.打开features.ini文件，将bootanimation.feature.key的值改为true，保存后重启模拟器。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ff/v3/iSYRdPwYSnmeftToPMNgUQ/zh-cn_image_0000002194158396.png?HW-CC-KV=V1&HW-CC-Date=20260612T024415Z&HW-CC-Expire=86400&HW-CC-Sign=A582B52A17B307F4306EAC8834DFEFDA73FC40E2CCF1639F19108515A09A44F2)
