---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-package-structure-69
title: 如何在应用内共享HSP
breadcrumb: FAQ > 应用框架开发 > 程序包结构 > 如何在应用内共享HSP
category: harmonyos-faqs
scraped_at: 2026-06-12T10:21:16+08:00
doc_updated_at: 2026-06-05
content_hash: sha256:34053c3d8b697a2dce5b95d9c1e409bdbbe658083af0cb58d0bd7f58b8e95f83
---
如需在应用内共享HSP，请将HSP共享包上传至私仓。动态共享包HSP不能直接发布在私仓内，需要先转换为.tgz包。请按以下操作编译生成\*.tgz包。

1. 将编译模式设为release。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/23/v3/YU8_anAsRcCxZA0JYaDQrw/zh-cn_image_0000002215625442.png?HW-CC-KV=V1&HW-CC-Date=20260612T022115Z&HW-CC-Expire=86400&HW-CC-Sign=B820FCE16CF630D30B493C2A798A8DBEC4581CC2DF37010B7D5927DE3D94A655 "点击放大")
2. 选中HSP模块的根目录，点击Build > Make Module {libraryName}，启动构建。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e2/v3/QU7jeSmYQCi6P4-vGZaq5w/zh-cn_image_0000002215465626.png?HW-CC-KV=V1&HW-CC-Date=20260612T022115Z&HW-CC-Expire=86400&HW-CC-Sign=36EC99D4A851AE016C47A5ADF0E79923AA14352528207548E32BDCCEEE813581)
3. 构建完成后，build目录下生成HSP包产物，其中.tgz用来上传至私仓（请参考[将三方库发布到 ohpm-repo](../../../../harmonyos-guides/开发环境搭建/工程创建/模块管理/ohpm-repo私仓搭建工具/快速开始/ide-ohpm-repo-quickstart.md#zh-cn_topic_0000001792256157_将三方库发布到ohpm-repo)）。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fa/v3/1hb_RolSTgODFyFo0SXkyA/zh-cn_image_0000002250545457.png?HW-CC-KV=V1&HW-CC-Date=20260612T022115Z&HW-CC-Expire=86400&HW-CC-Sign=879F70B1FD2C6AEE3CFB385038E31C107AABF280522DD71901BBC49E0A020566 "点击放大")
4. 上传到仓库，然后使用 `ohpm install` 命令将依赖安装到工程的oh-package.json5文件的dependencies字段中，即可查看对外共享的 HSP 方法。

**参考链接**

[创建HSP模块](../../../../harmonyos-guides/开发环境搭建/工程创建/模块管理/开发发布和管理共享包/开发动态共享包/ide-hsp.md#section79378499185)
