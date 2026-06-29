---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-132
title: 编译初始化报错“resource busy or locked, open 'xxx\outputs\build-logs\build.log'”
breadcrumb: FAQ > DevEco Studio > 编译构建 > 编译初始化报错“resource busy or locked, open 'xxx\outputs\build-logs\build.log'”
category: harmonyos-faqs
scraped_at: 2026-06-12T10:42:54+08:00
doc_updated_at: 2026-06-05
content_hash: sha256:ffe53e477286b1079588bbe57e59927dff38ce99881b43e0542665997a15edba
---

**问题现象**

在升级DevEco Studio至5.0.3.403版本后，打开旧工程时，可能会遇到以下错误：resource busy or locked, open 'xxx\outputs\build-logs\build.log'。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/13/v3/pHQC9CyeSXuvJJeqh4J2jw/zh-cn_image_0000002194158364.png?HW-CC-KV=V1&HW-CC-Date=20260612T024253Z&HW-CC-Expire=86400&HW-CC-Sign=BBB6A46A07506B89F7F4488F2E2B3C1D79DF6DC1529147B7D23C770E76A8E496)

**问题原因**

初始化时，日志写入存在冲突，.hvigor目录中的build-log文件被占用，导致报错。

**解决方案**

* 方法一：点击编辑器窗口上方的Sync Now。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/39/v3/cGCjXABZRyCz8o2Ptyhakg/zh-cn_image_0000002194317984.png?HW-CC-KV=V1&HW-CC-Date=20260612T024253Z&HW-CC-Expire=86400&HW-CC-Sign=91DF60DCF5B908FB7B8B1F7A9CA2B4ED8185F31DCE75504E0BB727BD1D6A6C6F)
* 方法二：点击工具栏**File > Sync and Refresh Project**。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/68/v3/SdY0giWgS6-LdCrdjD7sBg/zh-cn_image_0000002229758229.png?HW-CC-KV=V1&HW-CC-Date=20260612T024253Z&HW-CC-Expire=86400&HW-CC-Sign=2D69312D1535623C03BFC891D84780AB129F6FE4A87EA919A31D7EA6B4D19754)
* 方法三：如果方法一和方法二无法解决问题，可以手动删除工程目录下的 .hvigor目录，然后重启并执行 Sync。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cd/v3/CoDrWiSOThS5X1iKHJ7DRw/zh-cn_image_0000002229758233.png?HW-CC-KV=V1&HW-CC-Date=20260612T024253Z&HW-CC-Expire=86400&HW-CC-Sign=112F008B91EBAB86332D8299F1598A2E5031C3BC198D23E893E52F4146228751)
