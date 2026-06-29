---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-smart-step-into
title: 智能步入
breadcrumb: 指南 > 编写与调试应用 > 应用调试 > 代码调试 > Native代码调试 > 智能步入
category: harmonyos-guides
scraped_at: 2026-06-11T15:29:14+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:f59c39f5abd07ff05499f621689860b98b57b8e57b6724f918bf9f7d6f106d51
---

进行C++调试时，当前代码行有多个函数调用时，开发者可以使用Smart Step Into功能![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/54/v3/Y9I69N_iQQKkinVZc-Sq0g/zh-cn_image_0000002571546500.png?HW-CC-KV=V1&HW-CC-Date=20260611T072914Z&HW-CC-Expire=86400&HW-CC-Sign=2EE5A04BC9B98DC4E8EA96E5AFEF23C4F1B063F4BA6D8914161F008B3EBBC9DF)直接Step Into到其中某一个函数的实现中。

## 操作步骤

通过点击调试窗口“entry-Native”调试器下的Debugger窗格中的按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b8/v3/i0Oy3ZIdQei_sKHXz0aSVA/zh-cn_image_0000002571386862.png?HW-CC-KV=V1&HW-CC-Date=20260611T072914Z&HW-CC-Expire=86400&HW-CC-Sign=ECE785F52298FB8950414488FA098DBC939525609ACE7435FF06CDF837DE07EA)（或使用快捷键**Shift+F7**）触发Smart Step Into功能后，DevEco Studio会将当前代码中可以进行跳转的函数进行高亮显示。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d7/v3/Gpvo_a_tRa-2VcS9ZzzGMw/zh-cn_image_0000002602065981.png?HW-CC-KV=V1&HW-CC-Date=20260611T072914Z&HW-CC-Expire=86400&HW-CC-Sign=D4C80162ABC846004D4CA57DDDD24231138642E9C579E6B1A6FD942C87E9D07D "点击放大")

开发者点击需要跳转的函数，程序会运行到目标函数的实现内。

说明

已经执行完毕的函数不会高亮显示。
