---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-signature-service-14
title: 签名证书文件解析错误
breadcrumb: FAQ > DevEco Studio > 签名服务 > 签名证书文件解析错误
category: harmonyos-faqs
scraped_at: 2026-06-12T10:44:00+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:81d4a541a94ef82d548ecd5f9ed764441ce3236859e8a52322e24471925d6a3c
---

**问题现象**

打包签名提示“**DerValue.getOID, not an OID 49 Detail: Please check the message from tools**”错误。

**可能原因**

解析证书文件失败，一般情况是由于用户传入了非标准证书文件或证书文件损坏而导致。

**常见错误场景**

Certpath file配置了错误的证书文件。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d3/v3/Wv3LRz61RNWG-rdYyNfvjw/zh-cn_image_0000002342518434.png?HW-CC-KV=V1&HW-CC-Date=20260612T024400Z&HW-CC-Expire=86400&HW-CC-Sign=28AE474FDDD50C56FF80F95076661FEE2108B8918C20C94C30D84BBB2618A2EE)

**解决措施**

检查Certpath file配置的证书文件是否为标准证书文件，检查方式如下：

DevEco Studio Terminal窗口使用keytool命令查看配置的证书文件，示例：keytool -printcert -file ${Certpath file}。

* 格式正确的证书文件。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/25/v3/wtiytBPZTeiGky-JIjFxdw/zh-cn_image_0000002376516257.png?HW-CC-KV=V1&HW-CC-Date=20260612T024400Z&HW-CC-Expire=86400&HW-CC-Sign=58746B68E7843030296BD606C75C4B1FAFD316C6D3B19C68163AAB1649D6A426)

* 格式错误的证书文件。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6f/v3/1nsoYetoQYm20WbeLNXBkw/zh-cn_image_0000002376396377.png?HW-CC-KV=V1&HW-CC-Date=20260612T024400Z&HW-CC-Expire=86400&HW-CC-Sign=3D498BFFF9E736B95EDD83BAAA0681B94A73AE404E87DEEC35FE2E5D24BB7799)
