---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/agc-harmonyos-clouddev-deployfunc
title: 部署函数
breadcrumb: 指南 > 开发环境搭建 > 工程创建 > 模块管理 > 端云一体化开发 > 开发端云工程 > 开发云侧工程 > 开发云函数 > 部署函数
category: harmonyos-guides
scraped_at: 2026-06-01T15:18:25+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:265b220c017df39392d9690b56de6f17b479a9be582af17d8f983610c40cc8f6
---

完成函数代码开发后，您可将函数部署到AGC云端，支持单个部署和批量部署。

单个部署仅部署选中的函数，批量部署则会将整个“cloudfunctions”目录下的所有函数同时部署到AGC云端。

下文以部署单个函数“my-cloud-function”为例，介绍如何部署函数。

1. 右击“my-cloud-function”函数目录，选择“Deploy 'my-cloud-function'”。

   说明

   如需批量部署多个函数，右击“cloudfunctions”目录，选择“Deploy Cloud Functions”即可部署该目录下所有函数。如“cloudfunctions”目录下同时存在云函数和云对象，云函数和云对象将会被一起部署到AGC云端。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/88/v3/oRuCcjXsRz2rdRRVvqWV0Q/zh-cn_image_0000002179498368.png?HW-CC-KV=V1&HW-CC-Date=20260601T071825Z&HW-CC-Expire=86400&HW-CC-Sign=5A27F1B99E7FD161D657586EB424B6E3D3E1A008C6F631D1CA09753448302F50)
2. 您可在底部状态栏右侧查看函数打包与部署进度。

   请您耐心等待，直至出现“Deploy successfully”消息，表示当前函数已成功部署。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/50/v3/iKkq8PhTST-z01_51mqMJQ/zh-cn_image_0000002179498360.png?HW-CC-KV=V1&HW-CC-Date=20260601T071825Z&HW-CC-Expire=86400&HW-CC-Sign=52FD0023F227528050E18FDBE205C8F306FE5C5BB6BE44A0B2B21B58DA9F9B52)
3. 在菜单栏选择“Tools > CloudDev”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5b/v3/FSwXHLM-TWuuMTBERlBPMA/zh-cn_image_0000002214858997.png?HW-CC-KV=V1&HW-CC-Date=20260601T071825Z&HW-CC-Expire=86400&HW-CC-Sign=19DAA86E112240B6BA5572F28EBB62BE0C31301F1EC8B8A31E5E1AB89294AD8F)
4. 在打开的CloudDev面板中，点击“Serverless > Cloud Functions”下的“Go to console”，进入当前项目的云函数服务页面。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/82/v3/47kACfcXR9ua0ZlYZPMOBQ/zh-cn_image_0000002214704617.png?HW-CC-KV=V1&HW-CC-Date=20260601T071825Z&HW-CC-Expire=86400&HW-CC-Sign=56261E6CB93CABD0A365F003A0DF3E445A784863F6820CF5B3B3AD76A63E1CBA)
5. 查看到“my-cloud-function”函数已成功部署至AGC云端，函数名称与本地工程的函数目录名相同。

   部署成功后，您便可以从端侧调用云函数了，具体请参见[在端侧调用云函数](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/agc-harmonyos-clouddev-invokecloudfunc)。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/16/v3/9Csf-7lIQ0mvFd5_hToO1g/zh-cn_image_0000002179338680.png?HW-CC-KV=V1&HW-CC-Date=20260601T071825Z&HW-CC-Expire=86400&HW-CC-Sign=D68D57BA408F54E6168D8D40E0A18A5A36A2950E316EE9E99CD45179A00848F4)
