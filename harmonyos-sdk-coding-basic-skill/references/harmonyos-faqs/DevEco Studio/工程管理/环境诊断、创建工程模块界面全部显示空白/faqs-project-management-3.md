---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-project-management-3
title: 环境诊断、创建工程/模块界面全部显示空白
breadcrumb: FAQ > DevEco Studio > 工程管理 > 环境诊断、创建工程/模块界面全部显示空白
category: harmonyos-faqs
scraped_at: 2026-06-12T10:40:21+08:00
doc_updated_at: 2026-03-17
content_hash: sha256:e8d18e4b417604cb6645c9dc5312b19749d6397585f4383492c024e03033f2ae
---

**问题现象**

打开环境诊断界面，选择工程或模块模板时，界面显示为空；工程预览界面同样为空。

**原因分析**

这些页面都是使用JCEF绘制的，JCEF无法正常启动会导致这种问题。

**可能原因一**

JCEF窗口组件的GPU兼容性有问题。

**解决措施**

关闭JCEF的GPU渲染。

解决JCEF窗口组件的GPU兼容性问题，点击右上角的放大镜图标。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/18/v3/JD0oyi54RBOttUs0pj1wJg/zh-cn_image_0000002327307086.png?HW-CC-KV=V1&HW-CC-Date=20260612T024020Z&HW-CC-Expire=86400&HW-CC-Sign=651E46E9031EE368D7B8F5EB5E6C313E3D6C6959E9ADE8765ADC77220C46F171)

输入registry，点击下面的Registry...选项。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6f/v3/MTVJxrJsRXGwGug7oIhdPw/zh-cn_image_0000002327147458.png?HW-CC-KV=V1&HW-CC-Date=20260612T024020Z&HW-CC-Expire=86400&HW-CC-Sign=FCC0615608A4F6D49DC6C931613ACEB915FBCBF89B3BD325D885D951A7199BA5)

搜索gpu，找到ide.browser.jcef.gpu.disable，然后勾选这一项，最后重启DevEco Studio。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2c/v3/jia58twwTwW09kjlGb3tfw/zh-cn_image_0000002361065777.png?HW-CC-KV=V1&HW-CC-Date=20260612T024020Z&HW-CC-Expire=86400&HW-CC-Sign=4416CEA76BF24488F250866445F183A0688F7BAB6E6C871E61A6BF221B7A7D64)

**可能原因二**

IntelliJ底座问题，没有权限启动JCEF。

**解决措施**

可能是DevEco Studio权限不足导致，找到DevEco Studio的启动图标，选中图标，然后右键 > 属性 > 兼容性 > 以管理员身份运行此程序 > 确定。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c7/v3/eRs86PMPQzmibn-A5qPVfw/zh-cn_image_0000002327319882.png?HW-CC-KV=V1&HW-CC-Date=20260612T024020Z&HW-CC-Expire=86400&HW-CC-Sign=E0D1894F55AF756501C35091CC02496F192012A148F452682AA064C7E4A2DA31)

**可能原因三**

JCEF文件缺失，可能被杀毒软件误删除。

**解决措施**

检查JCEF文件是否缺失。

JCEF文件缺失，可能被杀毒软件误删除，导致JCEF进程无法拉起，查看这两个文件是否还存在，如果不存在，则需要重新安装DevEco Studio。

${DevEco Studio安装目录}/jbr/bin/server/jvm.dll

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b0/v3/QlG-0m7WQuOneMuxQaxmXw/zh-cn_image_0000002327180308.png?HW-CC-KV=V1&HW-CC-Date=20260612T024020Z&HW-CC-Expire=86400&HW-CC-Sign=8B48F95F05E3DE5332FB6E3E239E17ED9F2FCF77E709BB91BAC40C50339A2200)

${DevEco Studio安装目录}/jbr/bin/chrome\_elf.dll

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d6/v3/lYhz3MOzSTSJ54YKztwlmg/zh-cn_image_0000002327341312.png?HW-CC-KV=V1&HW-CC-Date=20260612T024020Z&HW-CC-Expire=86400&HW-CC-Sign=D28A5D4DBB6EFDEE5732AEADF99533F25B63E25654F48CC75E5A2A70764B8AE2 "点击放大")

**可能原因四**

JCEF沙箱环境与当前电脑环境冲突。

**解决措施**

JCEF沙箱环境与当前电脑环境冲突，导致JCEF无法正常工作。

点击右上角的放大镜图标。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bd/v3/oNxmoRbZRJS5LyZOAw4cTA/zh-cn_image_0000002361164509.png?HW-CC-KV=V1&HW-CC-Date=20260612T024020Z&HW-CC-Expire=86400&HW-CC-Sign=DEAF47C23DFAB4DFB5FEE6ED9BEACC5B3193016AA04830EABB7FF71AD614BC8E)

输入registry，点击下面的Registry...选项。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b5/v3/XxqGtG6ASzWLSXxmtTEcdQ/zh-cn_image_0000002361164813.png?HW-CC-KV=V1&HW-CC-Date=20260612T024020Z&HW-CC-Expire=86400&HW-CC-Sign=0B48AD6AB75F7E009CB20033B603CCE13483D90ABA14AC481FDBA0D83D8F130C)

搜索sandbox，找到ide.browser.jcef.sandbox.enable，取消勾选这一项，最后重启DevEco Studio。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ca/v3/SAcw-TsVRM6DavO9Ph6tQQ/zh-cn_image_0000002361165633.png?HW-CC-KV=V1&HW-CC-Date=20260612T024020Z&HW-CC-Expire=86400&HW-CC-Sign=0E1828E04F06E54921D54465B0649242B0E90817B677EF29D011BAFC88283EEA)
