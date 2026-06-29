---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-debugging-25
title: 启动C++调试时出现错误，提示“Failed to connect to unix-abstract-connect”
breadcrumb: FAQ > DevEco Studio > 应用调试 > 启动C++调试时出现错误，提示“Failed to connect to unix-abstract-connect”
category: harmonyos-faqs
scraped_at: 2026-06-12T10:44:52+08:00
doc_updated_at: 2026-03-12
content_hash: sha256:0d8d1e8fda4b7eff2a94a28edb47636fd26a6135137622c55ab0cb9d15469c37
---

**问题现象**

启动C++调试时出现错误，提示“Failed to connect to unix-abstract-connect://\\*\\*\\*\\*\\*\\*\\*\\*\\*.sock: Connection shut down by remote side while waiting for reply to initial handshake packet”。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/74/v3/Zfc_e_cWQZmflQeOcuMPYQ/zh-cn_image_0000002194158920.png?HW-CC-KV=V1&HW-CC-Date=20260612T024451Z&HW-CC-Expire=86400&HW-CC-Sign=9263959AEC31BAFC818B38752174004242228C4AC46BE435F025D7026D5D5B13)

**解决措施**

1. 如果设备镜像与DevEco Studio版本不匹配，请尝试更换设备镜像版本以解决问题。
2. 签名使用了release证书，请更换为debug证书。
3. 到设备路径 /data/local/tmp/debugserver/ 下，删除与应用包名相同的文件夹。
