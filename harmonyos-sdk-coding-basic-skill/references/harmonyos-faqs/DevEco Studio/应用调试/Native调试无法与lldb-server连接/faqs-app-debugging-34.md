---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-debugging-34
title: Native调试无法与lldb-server连接
breadcrumb: FAQ > DevEco Studio > 应用调试 > Native调试无法与lldb-server连接
category: harmonyos-faqs
scraped_at: 2026-06-12T10:44:58+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:51cf3bccb02a5c0cd4a5fac352c30a17d7323084043961df66327eb3c9a972f9
---

**问题现象：**Native调试长时间没有启动，最后DevEco Studio超时报错"Attach request timeout after 600000 milliseconds"或Native调试启动后报错"Failed to connect port"。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a/v3/hqKAM57jQA-cKYzXngt53w/zh-cn_image_0000002229758601.jpg?HW-CC-KV=V1&HW-CC-Date=20260612T024457Z&HW-CC-Expire=86400&HW-CC-Sign=8A2CC10F6FB21B75BA0AB070924645341A4FB140BCE6219BD7D8584C7BFB6564)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/83/v3/8bl_ZTCLTom5HwoDLhNJ-Q/zh-cn_image_0000002194318340.png?HW-CC-KV=V1&HW-CC-Date=20260612T024457Z&HW-CC-Expire=86400&HW-CC-Sign=1C21F7876AA00003AE05CEE28B9064CAF11D0F90E71D1338D823A09EC2FDBD48)

**可能原因：**

linux或MacOS 下 /etc/hosts文件被修改。

**解决措施：**

1. 在/etc/hosts文件后添加如下内容：

   ```
   1. 127.0.0.1 localhost
   2. 255.255.255.255 broadcasthost
   3. ::1 localhost
   ```
2. 重启电脑使修改生效。
