---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-debugging-63
title: 2in1设备attach调试失败和增量调试失败
breadcrumb: FAQ > DevEco Studio > 应用调试 > 2in1设备attach调试失败和增量调试失败
category: harmonyos-faqs
scraped_at: 2026-06-12T10:45:09+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:65a3eaa0ed0c6f135fc881ab76e90bea267f274f3d00fbd58280e3481a6bdf50
---

**问题现象**

1、2in1设备应用调试失败，报错信息如下图所示。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e1/v3/4v2S2fueRQ-7Mb-SUO_Eaw/zh-cn_image_0000002557414329.png?HW-CC-KV=V1&HW-CC-Date=20260612T024508Z&HW-CC-Expire=86400&HW-CC-Sign=6CA9C53DD39EFEEC542F9150FB719B7D936CE97D17A247D31783910405683A33)

2、2in1设备应用使用增量调试失败，报错信息如下图所示。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3c/v3/09YzdGMUR-i158cWlDdljw/zh-cn_image_0000002526214500.png?HW-CC-KV=V1&HW-CC-Date=20260612T024508Z&HW-CC-Expire=86400&HW-CC-Sign=C830D7A280907075FD3A2DE442232457B795DD7B6C591E4DAA0D4D9E20452472)

**解决措施**

2in1设备报上述错误可能原因是应用开启了应用加速服务功能，请在设备的**设置 > 应用加速服务**中，查看应用是否开启了应用加速服务，并关闭应用的加速服务。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6c/v3/zFQOtI-MTWyEQKYByzow_Q/zh-cn_image_0000002557334361.png?HW-CC-KV=V1&HW-CC-Date=20260612T024508Z&HW-CC-Expire=86400&HW-CC-Sign=35A6309D8CA1EED5C5D80816D09253B375E035E522BC37E2908FCE584821EBA6)
