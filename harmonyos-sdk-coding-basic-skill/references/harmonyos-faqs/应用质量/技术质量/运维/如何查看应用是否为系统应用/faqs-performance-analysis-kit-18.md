---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-performance-analysis-kit-18
title: 如何查看应用是否为系统应用
breadcrumb: FAQ > 应用质量 > 技术质量 > 运维 > 如何查看应用是否为系统应用
category: harmonyos-faqs
scraped_at: 2026-06-12T10:19:27+08:00
doc_updated_at: 2026-06-05
content_hash: sha256:15f58c44597c2c5024cb6fbf3e95358721582b268e87a8425f34adc0bab999b0
---
1. 连接设备。
2. 执行以下命令打印日志（Bundle Name获取参考：[bundleManager.getBundleInfoForSelf](<../../../../../harmonyos-references/Ability Kit（程序框架服务）/ArkTS API/通用能力的接口(推荐)/@ohos.bundle.bundleManager (应用程序包管理模块)/js-apis-bundlemanager.md#bundlemanagergetbundleinfoforself>)）：

   ```
   1. hdc shell bm dump -n <Bundle Name>
   ```
3. 当isSystemApp字段返回值为true时，表示当前应用是系统应用。

   返回的部分结果如下图所示：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d6/v3/qwxOtp_TR1K1p7DRfJTM6g/zh-cn_image_0000002244305208.png?HW-CC-KV=V1&HW-CC-Date=20260612T021926Z&HW-CC-Expire=86400&HW-CC-Sign=373BC2731F9B5ACF760B35AAEAD25919AC906D6522FB93F4275B0F24AC29C795 "点击放大")

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b2/v3/wc7lE5bUTU2x5Sz_a4PFlg/zh-cn_image_0000002279264169.png?HW-CC-KV=V1&HW-CC-Date=20260612T021926Z&HW-CC-Expire=86400&HW-CC-Sign=9C6C3A6E745CE9BA471B2F0CDCBB75BA52720F71DB6F4BA182B8972E221C85BE "点击放大")
