---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-project-management-4
title: 打开历史工程，报错提示“Install failed FetchPackageInfo: hypium failed”
breadcrumb: FAQ > DevEco Studio > 工程管理 > 打开历史工程，报错提示“Install failed FetchPackageInfo: hypium failed”
category: harmonyos-faqs
scraped_at: 2026-06-12T10:40:22+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:44073a04d8b838d96ea6c190777e6867a52078e51322ea40ae9de88afa1245e7
---

**问题现象**

在DevEco Studio打开历史工程，依赖安装不成功，报错信息为“Install failed FetchPackageInfo: hypium failed”。

**解决措施**

导致该问题的原因是包名使用错误。在工程级**oh-package.json5**中，将**devDependencies**字段下"hypium"修改为"@ohos/hypium"。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/15/v3/C4v2trPyQbqPnSrHwFjOuw/zh-cn_image_0000002194158560.png?HW-CC-KV=V1&HW-CC-Date=20260612T024021Z&HW-CC-Expire=86400&HW-CC-Sign=2A73725925CBC100BED7565D49DEBA64C1BCF7E36E0205A69DA8FDFBB0FBEF10)

@ohos/hypium版本号可通过ohpm命令获取，在DevEco Studio中打开Terminal，输入**ohpm info @ohos/hypium**命令，输出结果中dist-tags下方即为版本号。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fa/v3/pnUNDhZWSmKFl45vYSvk2g/zh-cn_image_0000002402257997.png?HW-CC-KV=V1&HW-CC-Date=20260612T024021Z&HW-CC-Expire=86400&HW-CC-Sign=5312AAC059D9CFB283E854C06262BDA6A5371F8D0CED25AF0D11CFFB4852CA2E)
