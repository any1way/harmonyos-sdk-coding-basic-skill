---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-app-analyzer-history-reports
title: 管理体检报告
breadcrumb: 指南 > 编写与调试应用 > 开发自测试 > 应用与元服务体检 > 管理体检报告
category: harmonyos-guides
scraped_at: 2026-06-11T15:30:05+08:00
doc_updated_at: 2026-04-30
content_hash: sha256:14a104853b2eaf7327e8eb9847c4745bc6ecfcabeab097ea85b7729d92234032
---
AppAnalyzer支持查看、导出、导入体检报告，具体如下。

## 查看报告

### DevEco Studio 6.0.1 Beta1及以上版本

1. 在DevEco Studio中，点击菜单栏**Tools >** **AppAnalyzer**，弹出AppAnalyzer页面。
2. 点击底部**History**按钮，可查看最近15次的体检报告卡片，点击卡片可跳转至详细的体检报告。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bb/v3/zaY9Eb7gS--pcqjtisA6Dw/zh-cn_image_0000002571546732.png?HW-CC-KV=V1&HW-CC-Date=20260611T073004Z&HW-CC-Expire=86400&HW-CC-Sign=1E89AB0A2AE9BB7A08DDBD5B3A8B4F81F1EB154B62147AA8249C21BFCC9551D7)

### DevEco Studio 6.0.1 Beta1以下版本

1. 在DevEco Studio中，点击菜单栏**Tools >** **AppAnalyzer**，弹出AppAnalyzer页面。
2. 点击底部**历史记录**按钮，可查看最近15次的体检报告记录，点击时间戳可跳转至详细的体检报告。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c9/v3/Tv89sZ8xRBap29RTMY4J2g/zh-cn_image_0000002571387096.png?HW-CC-KV=V1&HW-CC-Date=20260611T073004Z&HW-CC-Expire=86400&HW-CC-Sign=B3C8A11B8B31BFDF6D0E3FFCABA362702F842D90E3BA3150A66B15F9909C4681)

## 导出报告

从DevEco Studio 6.1.0 Release版本开始，AppAnalyzer支持导出体检报告，以实现报告的共享。使用该功能，需要满足以下条件。

* 支持导出场景化体检、规则体检、上架前体检这三种体检方式的报告。
* 历史版本生成的体检报告不支持导出，仅DevEco Studio 6.1.0 Release及以上版本生成的体检报告才支持导出。

操作步骤如下：

1. 点击AppAnalyzer底部的**History**按钮，选择符合条件的报告卡片进入报告页面，点击右上角的**Export**按钮，选择需要保存的路径，点击**OK**后，等待报告导出。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bb/v3/mOffT32ERJm0Wgteu8NhSA/zh-cn_image_0000002602186269.png?HW-CC-KV=V1&HW-CC-Date=20260611T073004Z&HW-CC-Expire=86400&HW-CC-Sign=D2E75EC359289E614EFECAFA5FD05CA8A33A78A2DA555120DF41F90E3F5B2DDD)
2. 报告导出成功后，在DevEco Studio右下角会弹框提示，点击**View the report**可打开报告保存的路径。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1e/v3/lPl8mvKySjSBEG13ysU8QA/zh-cn_image_0000002602066215.png?HW-CC-KV=V1&HW-CC-Date=20260611T073004Z&HW-CC-Expire=86400&HW-CC-Sign=5620633CD426D6DA124C25062E6FC35374D255397288B86CAEE2C39A48019395)

## 导入报告

从DevEco Studio 6.1.0 Release版本开始，如需查看他人的体检报告，可使用导入报告功能，需要满足以下条件。

* 支持导入场景化体检、规则体检、上架前体检这三种体检方式的报告。如需导入DevEco Testing的报告，请查看[导入DevEco Testing的检测报告进行诊断](<../导入DevEco Testing的检测报告进行诊断/ide-app-analyzer-testing.md>)。
* 导入报告使用的DevEco Studio版本，要求不低于导出报告时使用的版本，仅校验版本号前两位，例如6.1.x.x导出的报告，可以在6.1.x.x及以上版本中导入。

操作步骤如下：

1. 点击AppAnalyzer底部的**History**按钮，点击右上角的**Import**按钮，根据界面提示，确保即将导入的报告满足相关要求。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/33/v3/M33oghpUQP6OOLynaZJmlQ/zh-cn_image_0000002571546736.png?HW-CC-KV=V1&HW-CC-Date=20260611T073004Z&HW-CC-Expire=86400&HW-CC-Sign=A4F8D5DAB003ACCE6A3326A41FB0FA7678A39E2DC448641DB9F75A10AA9FC913)
2. 选择本地的体检报告zip文件，点击**OK**后，等待报告导入。导入成功后，AppAnalyzer会自动打开报告。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/78/v3/riI3u1fURG-7--GMopGpdA/zh-cn_image_0000002571546734.png?HW-CC-KV=V1&HW-CC-Date=20260611T073004Z&HW-CC-Expire=86400&HW-CC-Sign=A527364CE537305962C11D6E4188ABCA8A8A56A4245F29DAEA1C4FF1B2EA22EA)
