---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-test-8
title: ohosTest测试文件引用了entry模块的方法，测试时报cppcrash
breadcrumb: FAQ > DevEco Studio > 应用测试 > ohosTest测试文件引用了entry模块的方法，测试时报cppcrash
category: harmonyos-faqs
scraped_at: 2026-06-12T10:45:41+08:00
doc_updated_at: 2026-06-05
content_hash: sha256:3b1d8f45ac8ede0ca841ad23aed222924161aaaa3beec254d587bcc6ca2aa67e
---

**问题现象**

如果ohosTest测试文件引用了entry的方法，并且entry中存在以普通形式（例如"entry/ets/workers/Worker.ets"）加载worker时，测试执行期间会报cppcrash。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/43/v3/r1KKtObcS5CEGMxjiehHaQ/zh-cn_image_0000002194318400.png?HW-CC-KV=V1&HW-CC-Date=20260612T024540Z&HW-CC-Expire=86400&HW-CC-Sign=D37E6C608ADDD12B53CA5FD391F21D4E4281ABDB52A55959451885555239E9C8)

**解决措施**

修改entry中实例化worker的路径形式为带@标识的路径加载形式或相对路径加载形式，再次执行测试以确保可以正常通过。

* @标识路径加载形式("@entry/ets/workers/Worker.ets")：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b1/v3/xnBvTL0ZQ7KQEltaloJo4Q/zh-cn_image_0000002194158792.png?HW-CC-KV=V1&HW-CC-Date=20260612T024540Z&HW-CC-Expire=86400&HW-CC-Sign=B7168578E94EE066BC742DD7C574E8077F4A1682C40E03482EF31C4B683441E7)
* 相对路径加载形式("../workers/Worker.ets")：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0c/v3/vFdv6mTpQqGttYKkW4_HbA/zh-cn_image_0000002229758665.png?HW-CC-KV=V1&HW-CC-Date=20260612T024540Z&HW-CC-Expire=86400&HW-CC-Sign=941BE4490E1180357C51D3B15C59446A122559931A478E571D5E20BFB3E7474C)
