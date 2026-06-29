---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-coding-14
title: DevEco Studio上使用生成NAPI功能时， 提示“Failed to generate NAPI, check the napi_init.cpp file and try again. ”错误
breadcrumb: FAQ > DevEco Studio > 代码编辑 > DevEco Studio上使用生成NAPI功能时， 提示“Failed to generate NAPI, check the napi_init.cpp file and try again. ”错误
category: harmonyos-faqs
scraped_at: 2026-06-12T10:40:44+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:feb4ed202b5f920675c4f2fbb76ce616b83c04f472b183bb64e6a192b98ac5a1
---

**问题现象**

右键单击函数， 在弹出的菜单中依次选择 Generate... > NAPI， 生成胶水代码报错。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c6/v3/KUSW7v0tS7WqtqjUdTXS-Q/zh-cn_image_0000002229604349.png?HW-CC-KV=V1&HW-CC-Date=20260612T024044Z&HW-CC-Expire=86400&HW-CC-Sign=644E9FFBC34F08BBCEB5E5E33B627EA41CCFB0E83D187CCB558AF88020464270)

**解决措施**

检查napi\_init.cpp文件的Init函数中是否初始化了napi\_property\_descriptor变量。没有初始化请添加napi\_property\_descriptor desc[] = {}; 然后重新生成NAPI。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d5/v3/1xNjVYwbStOXVGR82hU27g/zh-cn_image_0000002194318564.png?HW-CC-KV=V1&HW-CC-Date=20260612T024044Z&HW-CC-Expire=86400&HW-CC-Sign=EF2AA5D2E88C0DDA93C1A42AE7022AF2D10507A214D2EBF1135DB51E94FBC2F0)
