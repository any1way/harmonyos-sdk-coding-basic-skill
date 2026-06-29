---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-code-completion
title: 代码生成/补全
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码生成/补全
category: harmonyos-guides
scraped_at: 2026-06-11T15:22:46+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:22b578cb0314500a097185df5ff782a4096e3dcc0ef84fba1de99faca8343ffc
---

## 代码自动补全

提供代码的自动补全能力，编辑器工具会分析上下文，并根据输入的内容，提示可补全的类、方法、字段和关键字的名称等，支持模糊匹配。

自动补全功能默认按最短路径进行排序，如仅需按照最近使用过的类、方法、字段和关键字等名称提供补全内容排序，可以在**File > Settings**（macOS为**DevEco Studio > Preferences/Settings**） **> Editor > General > Code Completion** 中勾选“Sort suggestions by recently used”。

说明

若已勾选代码补全按最近使用排序但未生效，请检查**Code Completion**页面，确保“Sort suggestions alphabetically”已取消勾选。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8/v3/IuwKzrnCSYWLGFhTVJkyTg/zh-cn_image_0000002602066391.png?HW-CC-KV=V1&HW-CC-Date=20260611T071847Z&HW-CC-Expire=86400&HW-CC-Sign=FE11BA89D51F01A142F5DC9A8B0D67822563E714513D447E077C83AF59CAB382)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6d/v3/vxqyxqmwQLam9zpZAWj5jw/zh-cn_image_0000002571387278.gif?HW-CC-KV=V1&HW-CC-Date=20260611T071847Z&HW-CC-Expire=86400&HW-CC-Sign=F97E8405F118E716D05C41DDCB68B84AC386E6A4D905FAD558C3DA4370E5034E)

## 快速覆写父类

DevEco Studio提供Override Methods，辅助开发者根据父类模板快速生成子类方法，提升开发效率。将光标放于子类定义位置，使用**快捷键Ctrl+O**（macOS为**Control+O**），或右键单击**Generate**...，选择**Override Methods**，指定需要覆写的对象（方法、变量等），点击**OK**将自动生成该对象的覆写代码。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1e/v3/_FDzvNHUQqe4oB4YTL5hwA/zh-cn_image_0000002602186447.gif?HW-CC-KV=V1&HW-CC-Date=20260611T071847Z&HW-CC-Expire=86400&HW-CC-Sign=67ED5FF15BCC00B65FF1DD1FF65E4AC65CDC47C2746AFDC5B92823C7D319A285)

## 快速生成构造器

编辑器支持为类快速生成一个对应的构造函数。

在类中使用**快捷键Alt+Insert**（macOS为**Command+N**），或单击鼠标右键选择**Generate**...，在弹窗中选择**Constructor**，选择一个或多个需要生成构造函数的参数，点击**OK**。若选择**Select None**，则生成不带参数的构造器。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fc/v3/vCUjQH5ATkqjTW9KKm6TUg/zh-cn_image_0000002571387274.gif?HW-CC-KV=V1&HW-CC-Date=20260611T071847Z&HW-CC-Expire=86400&HW-CC-Sign=CD13ADFAB9BD7ECE4D958102D86F5593D23CA30BCA11D5C614D01C822B69CB72)

## 快速生成get/set方法

编辑器支持为类成员变量或对象属性快速生成get和set方法。

将光标放置在当前类中，单击右键选择**Generate...>Getter and Setter**，或者使用快捷键**Alt+Insert**（macOS为**Command+N**），在菜单中选择**Getter and Setter**，完成方法快速生成。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/db/v3/XKkkwwRZSFyKyny5k-ZPOA/zh-cn_image_0000002602186445.gif?HW-CC-KV=V1&HW-CC-Date=20260611T071847Z&HW-CC-Expire=86400&HW-CC-Sign=269FFA939447D1D4D07B6B7229743517DD202D6945C3200742F161D0167B93CE)

## 快速生成声明信息到Index文件

编辑器支持将HSP和HAR模块中变量、方法、接口、类等需要对外暴露的信息，通过**Generate...>Declarations**功能，批量在Index.ets文件中进行声明，便于其他模块调用。

在HSP或HAR模块内的文件编辑界面，单击右键选择**Generate...>****Declarations**，或者使用快捷键**Alt+Insert**（macOS为****Command+N****），在菜单中选择**Declarations**，按住快捷键Ctrl并选择需要声明的变量名、方法名、接口名、类名等，即可在模块的Index.ets文件中批量生成相应的声明信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8f/v3/4qaSA1fPRn-1gNr13SFaRw/zh-cn_image_0000002571546912.gif?HW-CC-KV=V1&HW-CC-Date=20260611T071847Z&HW-CC-Expire=86400&HW-CC-Sign=1BD66A0397CE556186E3F52F0C844F1B05D609707336C3ABB103FC54130A41C0)
