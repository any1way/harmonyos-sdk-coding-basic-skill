---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-coding-15
title: DevEco Studio上使用生成NAPI功能时， 提示“Could not find usage of napi_module_register in napi_init.cpp.”错误
breadcrumb: FAQ > DevEco Studio > 代码编辑 > DevEco Studio上使用生成NAPI功能时， 提示“Could not find usage of napi_module_register in napi_init.cpp.”错误
category: harmonyos-faqs
scraped_at: 2026-06-12T10:40:46+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:252d8f0c310f0a8ba89d1f774b40a7a0737de56d8b2e93e3072ef8ec4e645423
---

**问题现象**

右键单击函数， 在弹出的菜单中依次选择 Generate... > NAPI， 生成胶水代码报错。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/af/v3/AQjZAYgaRO2WBtpOKad8Gg/zh-cn_image_0000002229758437.png?HW-CC-KV=V1&HW-CC-Date=20260612T024045Z&HW-CC-Expire=86400&HW-CC-Sign=3CDF27E373875905395771AC08AFAB06EC7D9007A3596EEC50EBF5D93BA0EB2A)

**解决措施**

检查napi\_init.cpp文件的RegisterEntryModule函数中是否调用了napi\_module\_register函数。napi\_module\_register的参数类型为napi\_module\*, napi\_module初始化示例代码如下图所示。然后重新生成NAPI。

字段含义：

nm\_version: N-API模块版本

nm\_flags: 模块的属性标志

nm\_filename: N-API模块的文件名

nm\_register\_func: 注册函数

nm\_modname: 模块名称

nm\_priv: 私有数据指针

reserved: 保留字段

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/80/v3/VZGeUV2rSm29o_Ceic2DSQ/zh-cn_image_0000002519864254.png?HW-CC-KV=V1&HW-CC-Date=20260612T024045Z&HW-CC-Expire=86400&HW-CC-Sign=7C60BDB1A22E99058C9B2D8B3CA058EEBD184249911E2CBBE5327C1594ACFD7E)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b3/v3/UQ5oWahUTpOSENKzKwHyvg/zh-cn_image_0000002229603969.png?HW-CC-KV=V1&HW-CC-Date=20260612T024045Z&HW-CC-Expire=86400&HW-CC-Sign=CA4AD1DAC35009E7176F611AD362EA2D42BD69FE0DBD2D29028245D5E4918B38)
