---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-debugging-57
title: DevEco如何配置不响应raise捕获到的assert信号
breadcrumb: FAQ > DevEco Studio > 应用调试 > DevEco如何配置不响应raise捕获到的assert信号
category: harmonyos-faqs
scraped_at: 2026-06-12T10:45:05+08:00
doc_updated_at: 2026-03-12
content_hash: sha256:8f2e481fa74a1f0b87e96c488a819109f7db500c8f7785da8a26bcdd70a89c9d
---

在DevEco Studio RUN/Debug Configurations中的Edit Configurations > Debugger > LLDB Post Attach Commands，添加配置：process handle -p false -s false -n false signal。其中，signal为assert发送的信号。详细步骤如图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1e/v3/xZQ2Bu8LQdGdg2ooNApT5w/zh-cn_image_0000002194158524.png?HW-CC-KV=V1&HW-CC-Date=20260612T024504Z&HW-CC-Expire=86400&HW-CC-Sign=4D65F0FCBC48E80C409EACBCD83FA35213E877B03482972EA1246A553ED3F60D)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0/v3/ovy3idR2TgGwElGQucioKg/zh-cn_image_0000002229603925.png?HW-CC-KV=V1&HW-CC-Date=20260612T024504Z&HW-CC-Expire=86400&HW-CC-Sign=C4559BF3579A407156CBFCCB69CB82296C04D59DB2A4C4A1FEDDDCABF6C3E003 "点击放大")
