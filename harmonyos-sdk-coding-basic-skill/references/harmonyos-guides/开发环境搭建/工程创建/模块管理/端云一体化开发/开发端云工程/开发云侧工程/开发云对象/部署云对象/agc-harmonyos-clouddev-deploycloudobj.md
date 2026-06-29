---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/agc-harmonyos-clouddev-deploycloudobj
title: 部署云对象
breadcrumb: 指南 > 开发环境搭建 > 工程创建 > 模块管理 > 端云一体化开发 > 开发端云工程 > 开发云侧工程 > 开发云对象 > 部署云对象
category: harmonyos-guides
scraped_at: 2026-06-01T15:18:29+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:8c9502da4d86ecbdeb171e7566a718e2512bc0f2b0aafae7d784f8a4e3221b38
---

完成云对象代码开发后，您可将云对象部署到AGC云端，支持单个部署和批量部署。

单个部署仅部署选中的云对象，批量部署则会将整个“cloudfunctions”目录下的所有云对象同时部署到AGC云端。

下文以部署单个云对象“my-cloud-object”为例，介绍如何部署云对象。

1. 右击“my-cloud-object”云对象目录，选择“Deploy 'my-cloud-object'”。

   说明

   如需批量部署多个云对象，右击“cloudfunctions”目录，选择“Deploy Cloud Functions”即可部署该目录下所有云对象。如“cloudfunctions”目录下同时存在云函数和云对象，云函数和云对象将会被一起部署到AGC云端。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/12/v3/FYoD1WkKR7OLfsoEZgU2Bw/zh-cn_image_0000002179338528.png?HW-CC-KV=V1&HW-CC-Date=20260601T071830Z&HW-CC-Expire=86400&HW-CC-Sign=36E6FFB886C9700957DDE1C2A93D453C5DF9807D161F9B2EC64CF01E4C8DA48B)
2. 您可在底部状态栏右侧查看云对象打包与部署进度。

   请您耐心等待，直至出现“Deploy successfully”消息，表示当前云对象已成功部署。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b8/v3/vysXI6jgSS-SOuGxth7Upg/zh-cn_image_0000002214704473.png?HW-CC-KV=V1&HW-CC-Date=20260601T071830Z&HW-CC-Expire=86400&HW-CC-Sign=B3A45607430AAE9742DBDCC51AB8C978A84A3FD49A2FBF8C67ADD1BB2C512FAD)
3. 在菜单栏选择“Tools > CloudDev”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5f/v3/P2dGnppSQwuY-P9dRyWXbw/zh-cn_image_0000002179498224.png?HW-CC-KV=V1&HW-CC-Date=20260601T071830Z&HW-CC-Expire=86400&HW-CC-Sign=3DA402069252B7B2CFD44D2E6D8F0A5FCB7C0D097C000FEA7947F5D309CBAF2B)
4. 在打开的CloudDev面板中，点击“Serverless > Cloud Functions”下的“Go to console”，进入当前项目的云函数服务页面。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/12/v3/65U2yXZ-Te6xh_A3OB7xcw/zh-cn_image_0000002214858857.png?HW-CC-KV=V1&HW-CC-Date=20260601T071830Z&HW-CC-Expire=86400&HW-CC-Sign=6CB4336E62FC62AC4D64A3B4047F5909C795B69B4F2E7340B4272845B61F272A)
5. 查看到“my-cloud-object”云对象已成功部署至AGC云端，云对象名称与本地工程的云对象目录名相同。

   部署成功后，您便可以从端侧调用云对象了，具体请参见[在端侧调用云对象](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/agc-harmonyos-clouddev-invokecloudobj)。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c7/v3/_KhspIwjQYWPvJ-rxyn8BA/zh-cn_image_0000002179338540.png?HW-CC-KV=V1&HW-CC-Date=20260601T071830Z&HW-CC-Expire=86400&HW-CC-Sign=E0B8845E16E1C8D0AA8AC077185C24042FF4919B24783569E3C1B933674ECA83)
