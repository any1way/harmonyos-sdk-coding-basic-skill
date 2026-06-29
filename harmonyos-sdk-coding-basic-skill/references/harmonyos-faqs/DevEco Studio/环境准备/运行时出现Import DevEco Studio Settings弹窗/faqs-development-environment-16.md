---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-development-environment-16
title: 运行时出现Import DevEco Studio Settings弹窗
breadcrumb: FAQ > DevEco Studio > 环境准备 > 运行时出现Import DevEco Studio Settings弹窗
category: harmonyos-faqs
scraped_at: 2026-06-12T10:40:17+08:00
doc_updated_at: 2026-06-05
content_hash: sha256:e4feda17189fd3c89e8ae32aea70c7f8fd09918248282758520fe36bfdb5fb8f
---

**问题现象**

问题出现包含两种场景：

场景一：首次运行DevEco Studio时，出现**Import DevEco Studio Settings**弹窗。

场景二：本地清理DevEco Studio缓存后再次下载安装运行时，可能出现**Import DevEco Studio Settings**弹窗。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9b/v3/OMmU35RTSLGuVI2GYDUTiA/zh-cn_image_0000002474225988.png?HW-CC-KV=V1&HW-CC-Date=20260612T024017Z&HW-CC-Expire=86400&HW-CC-Sign=43D09AA1D1E214900FEAE4BE158FD2B553BF8355FBDEF329A07F37B6ED2063C7)

**解决措施**

方案一：建议保持默认勾选项**Do not import settings**。

方案二：勾选**Config or installation directory**，上传配置项压缩包（settings.zip）。

说明

* 点击**File** > **Manage IDE Settings** > **Export Settings**...将包含Ark插件等配置项导出，再次运行时可以将配置项直接导入。
* DevEco Studio版本不同，支持导出的配置项不同。可导出的配置项需以具体版本为准。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e7/v3/s29gxZ_TSfGeYYbVtgyFyw/zh-cn_image_0000002509067411.png?HW-CC-KV=V1&HW-CC-Date=20260612T024017Z&HW-CC-Expire=86400&HW-CC-Sign=9A8FBA28F4A3BD49602657C8039075CEF0CBF63A1A1E1972B9D9A5F077579099)
