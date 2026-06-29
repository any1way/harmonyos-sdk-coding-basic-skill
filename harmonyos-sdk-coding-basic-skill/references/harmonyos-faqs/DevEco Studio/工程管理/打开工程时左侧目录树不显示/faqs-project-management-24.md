---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-project-management-24
title: 打开工程时左侧目录树不显示
breadcrumb: FAQ > DevEco Studio > 工程管理 > 打开工程时左侧目录树不显示
category: harmonyos-faqs
scraped_at: 2026-06-12T10:40:35+08:00
doc_updated_at: 2026-04-27
content_hash: sha256:57384717dac8234fdb1dfd1e6cff15336f44ef4d76ba38f8201b76e99496851c
---

**问题现象**

左侧目录树不显示，如下图所示。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/55/v3/irkkNxrxQBymnNmi8ets2A/zh-cn_image_0000002583384877.png?HW-CC-KV=V1&HW-CC-Date=20260612T024034Z&HW-CC-Expire=86400&HW-CC-Sign=FE352CF32A438F4CAE13A5EDB99663A60A313E43DB3C5C0E0F5AC98EA3323D20)

**问题原因**

**情况1：**

在 macOS上，系统对隐私权限的管理非常严格。如果没有获得访问特定目录（如“下载”或“桌面”）的权限，就会出现项目虽然打开了，但左侧目录树一片空白的情况。

**情况2：**

当用户删除工程目录下的.idea/modules文件夹或者.idea/modules文件夹不存在时，如下图所示。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5/v3/wnpjUqpCQIOOxomPROmBfg/zh-cn_image_0000002552745208.png?HW-CC-KV=V1&HW-CC-Date=20260612T024034Z&HW-CC-Expire=86400&HW-CC-Sign=1F8C15294B749A3CC401D52315DF91D1134549F721280E8FC97BD3E6279DEBFD)

由于modules文件夹下的iml文件定义了详细的工程模块结构信息，modules.xml定义了工程模块结构文件的位置。删除modules文件夹后根据modules.xml无法找到对应的iml文件。

**解决措施**

**情况1：**

如果缺少访问权限，设置项目文件夹访问权限就可以解决问题：系统设置->隐私与安全->文件和文件夹->允许访问（找到DevEco Studio，点击展开），重启IDE，工程目录树才可以恢复

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b7/v3/XTlau2fTS2CHVRcp5qKx2w/zh-cn_image_0000002583305609.png?HW-CC-KV=V1&HW-CC-Date=20260612T024034Z&HW-CC-Expire=86400&HW-CC-Sign=FB141FE1DDB70F0C7404FB077B665BF62EC5876DA20B350E79DA47248317FAB2)

**情况2：**

需要关闭工程，在文件管理器中删除工程的modules.xml，重新启动IDE打开工程，工程目录树才可以恢复。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f2/v3/SB-SuHS9Qc-d5-cRBsuQJQ/zh-cn_image_0000002583385109.png?HW-CC-KV=V1&HW-CC-Date=20260612T024034Z&HW-CC-Expire=86400&HW-CC-Sign=2E26BF7BCD76F15DD352676FB6AEBE64CAAEEB95ACB5BBC2A478D719210ADA47)
