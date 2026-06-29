---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-development-environment-4
title: 下载HarmonyOS SDK时提示网络连接错误
breadcrumb: FAQ > DevEco Studio > 环境准备 > 下载HarmonyOS SDK时提示网络连接错误
category: harmonyos-faqs
scraped_at: 2026-06-12T10:40:07+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:25c3b19b4fa626ad57676666766568b4b8a00656f6cae5598937087060eb7e25
---

**问题现象**

网络连接正常，但下载HarmonyOS SDK时提示网络连接错误。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5e/v3/zzXyProeRBmGX9AM_cPPwA/zh-cn_image_0000002229758633.png?HW-CC-KV=V1&HW-CC-Date=20260612T024006Z&HW-CC-Expire=86400&HW-CC-Sign=7B8757AD42FFD2FD13002BF7231B3DB84692FA0EAF05E6DE3A6F8320B6145686)

**解决措施**

由于使用的PC系统语言为英文且区域码为US，可能导致问题。请按照以下步骤将区域码修改为CN，在修改前请确保已关闭DevEco Studio。

在C:\Users\\_username\_\AppData\Roaming\Huawei\DevEcoStudio4.1\options路径下（MacOS 路径为/Users/\_username\_/Library/Application Support/Huawei/DevEcoStudio4.1/options），打开country.region.xml文件，将countryregion name修改为“CN”。

```
1. <application>
2. <component name="CountryRegionSetting">
3. <countryregion name="CN"/>
4. </component>
5. </application>
```
