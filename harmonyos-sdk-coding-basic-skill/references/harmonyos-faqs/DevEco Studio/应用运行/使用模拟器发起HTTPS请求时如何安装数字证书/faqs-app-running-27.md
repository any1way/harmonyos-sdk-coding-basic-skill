---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-running-27
title: 使用模拟器发起HTTPS请求时如何安装数字证书
breadcrumb: FAQ > DevEco Studio > 应用运行 > 使用模拟器发起HTTPS请求时如何安装数字证书
category: harmonyos-faqs
scraped_at: 2026-06-12T10:44:23+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:8eee35fb0268c24640359791c6989ca8015cb463f73eb293efc3a04d5514b08b
---

**问题现象**

在使用网络代理发送HTTPS请求时，需要安装网站服务器的数字证书。

**解决措施**

1. 将证书拖拽上传至模拟器，可在文件管理的“我的手机”>“下载”目录下查看上传的文件。
2. 安装证书的方式如下：
   * 点击**设置 > WLAN >**![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b2/v3/W1iT4aeXTCK4dgaq6KqVyA/zh-cn_image_0000002395407910.png?HW-CC-KV=V1&HW-CC-Date=20260612T024422Z&HW-CC-Expire=86400&HW-CC-Sign=6391CC6A99808EF0C38F20082DFC22D649DFD0037D75878C6A58F18389AEC060)**> 安装证书 > CA证书**，选择pem格式证书进行安装。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cd/v3/gb9-W9RKSOaHeRVOSM1-mQ/zh-cn_image_0000002229758177.png?HW-CC-KV=V1&HW-CC-Date=20260612T024422Z&HW-CC-Expire=86400&HW-CC-Sign=AFCEAD86CB2BC3FCD74AA5C21B33AEC35BFE234A0678B63C15A0250B7EFAD67D) ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/16/v3/IfgonmPoTYWKiHM2oFy9Xw/zh-cn_image_0000002194317924.png?HW-CC-KV=V1&HW-CC-Date=20260612T024422Z&HW-CC-Expire=86400&HW-CC-Sign=917B9CBE51BD4F453C047F66D6C6CFE940DF633A9C759AC74F6813C07453902D)
   * 在本机命令行窗口中使用以下命令打开证书管理。

     ```
     1. hdc shell aa start -a MainAbility -b com.ohos.certmanager
     ```

     选择从存储设备安装，安装pem格式的证书。
