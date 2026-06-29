---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-test-9
title: ohosTest测试文件引用了启动页的导出方法，测试时报错“Load Page Failed: pages/Index”
breadcrumb: FAQ > DevEco Studio > 应用测试 > ohosTest测试文件引用了启动页的导出方法，测试时报错“Load Page Failed: pages/Index”
category: harmonyos-faqs
scraped_at: 2026-06-12T10:45:42+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:99f5b2ce0860f4df7e866a405336349719d2aea9e0338f079aa5856c4fa155dd
---

**问题现象**

在测试文件中引用启动页的导出方法并拉起启动页面所在的Ability时，执行测试会抛出jscrash，错误信息为：“Load Page Failed: pages/Index”。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a6/v3/eWwPSr_6RIqtYPc6c1YM8w/zh-cn_image_0000002229604273.png?HW-CC-KV=V1&HW-CC-Date=20260612T024541Z&HW-CC-Expire=86400&HW-CC-Sign=411A6F06DEA72B4B32C4261011C3EC8192FA997B79A3C7B6855A44740088B72F)**解决措施**

拉起启动页面所在Ability时指定当前模块名称，执行测试，用例正常运行。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3e/v3/9h-vhghrQIiXQpKnBdZJoQ/zh-cn_image_0000002194158896.png?HW-CC-KV=V1&HW-CC-Date=20260612T024541Z&HW-CC-Expire=86400&HW-CC-Sign=E55A03538D907E18F4A897757962B7E259A578CC7DEAA0A41DF9335F5926FE67)
