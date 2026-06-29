---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-running-39
title: Windows电脑上启动模拟器，提示可申请内存不足
breadcrumb: FAQ > DevEco Studio > 应用运行 > Windows电脑上启动模拟器，提示可申请内存不足
category: harmonyos-faqs
scraped_at: 2026-06-12T10:44:33+08:00
doc_updated_at: 2026-06-05
content_hash: sha256:5de0488e016bfcc67f40e6a02861480b48818f241458fe2025aa3ce11dc7af4f
---

**问题现象**

启动模拟器时，如果系统提示“当前可申请的内存不足”，表示Windows电脑内存不足。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3f/v3/P4eWR_cHRwWJgn06TUraeg/zh-cn_image_0000002229604313.png?HW-CC-KV=V1&HW-CC-Date=20260612T024432Z&HW-CC-Expire=86400&HW-CC-Sign=6B5EEC5493F526869BE7D1FDC785E701C4A74121973C54F7F590663212FD68CA)

**解决措施**

1. 打开任务管理器的详细信息页面，在列表表头右键选择列，勾选“提交大小”，然后点击“提交大小”列进行排序，关闭提交大小占用高的进程。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/82/v3/oz21aYNYTySVbX8dozjk2Q/zh-cn_image_0000002229758817.png?HW-CC-KV=V1&HW-CC-Date=20260612T024432Z&HW-CC-Expire=86400&HW-CC-Sign=76BCAB6221BBC55A15A188E4232A2A05B6108EC7770318D609C8F50DAD412B1D "点击放大")
2. 打开任务管理器的性能和内存页面，确保已提交内存的剩余量大于模拟器设置的RAM大小。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/29/v3/-VBiQ26FT-2A6aqSG66h5g/zh-cn_image_0000002194158932.png?HW-CC-KV=V1&HW-CC-Date=20260612T024432Z&HW-CC-Expire=86400&HW-CC-Sign=39E1F97266FD1284E13D404C28018E0E5E276C0B88D1E06E045AC3B102A24B4C)
