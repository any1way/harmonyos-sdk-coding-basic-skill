---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-debug-arkts-attach-to-process
title: 等待调试
breadcrumb: 指南 > 编写与调试应用 > 应用调试 > 代码调试 > ArkTS代码调试 > 等待调试
category: harmonyos-guides
scraped_at: 2026-06-11T15:28:58+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:b4799fb0a34e8f13af45cfb9c09d14068ce29ad1388278e5ed1736fa46977d81
---

开发者可以通过将某个应用设置为“等待调试模式”，然后当开发者需要对应用进行调试时，拉起应用即可快速进入调试。

说明

* 应用设置为“等待调试模式”后，此时如果启动普通的debug调试，将会取消当前的等待调试模式。
* 设置“等待调试模式”前，需要将应用安装到设备上。

## 操作步骤

1. 在设备选择框中选择调试的设备，并单击Run > Attach to Process by Name。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a5/v3/nz6WM3NcQJ6vut5lzxorTA/zh-cn_image_0000002571387646.png?HW-CC-KV=V1&HW-CC-Date=20260611T072857Z&HW-CC-Expire=86400&HW-CC-Sign=A4B1F1449EEA2051FEB7BB907DFFA4C57EF176C6C9DE2A3DB73EAE9D5D20390D)
2. 选择需要设置为“等待调试模式”的应用（默认为当前工程），选择需要进行调试的调试类型。然后单击**Attach**，即可将该应用设置为“等待调试模式”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/69/v3/xxHXQDqASm2BN3LKnzs0xw/zh-cn_image_0000002602186815.png?HW-CC-KV=V1&HW-CC-Date=20260611T072857Z&HW-CC-Expire=86400&HW-CC-Sign=4766171F7500DFD4BA2AD9DD41530B84149E17D2E77670825930A2E49E3CA2C4)

   此时会在DevEco Studio底部显示一个等待进度条，在应用被拉起之前，将一直处于等待状态。可通过进度条右侧的取消按钮进行取消。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/78/v3/Mb5-IdxTRiGg3ZQNpuPt1A/zh-cn_image_0000002602066759.png?HW-CC-KV=V1&HW-CC-Date=20260611T072857Z&HW-CC-Expire=86400&HW-CC-Sign=DAEE036B67D96533439070EA74EDBA44FCA7D2EDF0E5FBD223395D01C0D49FDF)
3. 拉起设备端应用，此时将会进入调试。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e/v3/Si77BxNfQdaed8VdOMP4bQ/zh-cn_image_0000002571547284.png?HW-CC-KV=V1&HW-CC-Date=20260611T072857Z&HW-CC-Expire=86400&HW-CC-Sign=AF85EA05739CFD3B9F937FE2B31329369CEFB9C91C975E66D8D378A6399D818D)
