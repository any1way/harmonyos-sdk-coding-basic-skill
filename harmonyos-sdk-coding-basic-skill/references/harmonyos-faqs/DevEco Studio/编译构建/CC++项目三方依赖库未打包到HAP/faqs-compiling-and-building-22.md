---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-22
title: C/C++项目三方依赖库未打包到HAP
breadcrumb: FAQ > DevEco Studio > 编译构建 > C/C++项目三方依赖库未打包到HAP
category: harmonyos-faqs
scraped_at: 2026-06-12T10:41:17+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:932cc9699cf2be6ace7c68ee77318dcf2882a7defb6ef875ba816c0adb396831
---

**问题现象**

C/C++项目依赖三方so时，在打包生成HAP后，发现三方so未打包到HAP中。

**解决措施**

当前DevEco Studio对C/C++项目中第三方so文件的寻址方式存在限制。如果第三方so文件未打包到HAP中，请尝试修改so文件的引入方式。

1. 定义一个别名，例如jsbind\_shared\_lib\_tracing，代表将要引入的三方so。
2. 使用SHARED IMPORT将三方so动态引入。
3. 使用IMPORTED\_LOCATION定义引入的so文件位置。
4. 将定义的三方so声明给目标。![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/81/v3/CTluJ8BVSTWeLLIlBxUqfg/zh-cn_image_0000002194318404.png?HW-CC-KV=V1&HW-CC-Date=20260612T024116Z&HW-CC-Expire=86400&HW-CC-Sign=1057B6F3D183247B7BDBC78E04E832387F3CB62DEB8A001C3E9EEE9A1602BBF6)
5. 再次打包生成HAP，确认三方so已打包到HAP中。
