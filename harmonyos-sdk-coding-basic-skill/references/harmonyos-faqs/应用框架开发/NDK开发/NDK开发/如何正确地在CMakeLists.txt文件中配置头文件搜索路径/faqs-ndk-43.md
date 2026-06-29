---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ndk-43
title: 如何正确地在CMakeLists.txt文件中配置头文件搜索路径
breadcrumb: FAQ > 应用框架开发 > NDK开发 > NDK开发 > 如何正确地在CMakeLists.txt文件中配置头文件搜索路径
category: harmonyos-faqs
scraped_at: 2026-06-12T10:25:13+08:00
doc_updated_at: 2026-03-12
content_hash: sha256:dc6e721eed8c4fbd1d511bbb3485fbb9dd8100aeaa6fc67d554335a4de97e26c
---

请按照以下示例进行配置：

**例1****：**

目录结构：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c4/v3/VlVf2JyNR-WATEyekK2OOA/zh-cn_image_0000002199836868.png?HW-CC-KV=V1&HW-CC-Date=20260612T022512Z&HW-CC-Expire=86400&HW-CC-Sign=A44483EF8A168B764FAD1BC031B3FA3A4B4B32A385BAB52EAA5ADE3BE492F6F8)

CMakeLists.txt配置头文件搜索路径：

include\_directories(${NATIVERENDER\_ROOT\_PATH}/include)

cpp文件中引用头文件:

#include 'test.h'

**例2****：**

目录结构：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7e/v3/tA_1rE3sRmSVVMUpU-aykw/zh-cn_image_0000002234797125.png?HW-CC-KV=V1&HW-CC-Date=20260612T022512Z&HW-CC-Expire=86400&HW-CC-Sign=C6276D32D383A02022839C86195DC5B1CF2DBCFDF6092F9B6D55C8C0262BEFE8)

CMakeLists.txt配置头文件搜索路径：

include\_directories(${NATIVERENDER\_ROOT\_PATH})

cpp文件中引用头文件:

#include 'include/test/test.h'

**例3：**

目录结构：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ad/v3/MXdqHG9PTXKJ1V89V75bow/zh-cn_image_0000002234956969.png?HW-CC-KV=V1&HW-CC-Date=20260612T022512Z&HW-CC-Expire=86400&HW-CC-Sign=7185EE03139987BA76A41EC8C5864EF73F4532AC1224689DC43240231A92B231)

CMakeLists.txt配置头文件搜索路径：

include\_directories(${NATIVERENDER\_ROOT\_PATH}/include)

cpp文件中引用头文件:

#include 'test/test.h'

**例4:**

目录结构：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/26/v3/YE7lm8SRSm-u4-QPWu5HaQ/zh-cn_image_0000002199996680.png?HW-CC-KV=V1&HW-CC-Date=20260612T022512Z&HW-CC-Expire=86400&HW-CC-Sign=873CBF353D03139082131FD57041AB36E3702EDC8A0BA8085A7C43C7FB1884AE)

CMakeLists.txt配置头文件搜索路径:

include\_directories(${NATIVERENDER\_ROOT\_PATH}/include/test)

cpp文件中引用头文件:

#include 'test.h'
