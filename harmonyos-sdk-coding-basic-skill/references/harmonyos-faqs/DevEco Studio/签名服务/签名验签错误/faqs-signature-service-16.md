---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-signature-service-16
title: 签名验签错误
breadcrumb: FAQ > DevEco Studio > 签名服务 > 签名验签错误
category: harmonyos-faqs
scraped_at: 2026-06-12T10:44:02+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:7d5e98d6ff5a8168855aacbfc7457af35d4c6b45fc230508eb95f66966dcaeec
---

**问题现象**

打包签名提示“**Verify Signature failed**”错误。

**问题原因**

签名使用密钥库文件内的私钥与证书不匹配，导致工具验证签名失败。

**错误场景**

1、打包签名场景，签名时使用的证书和密钥不一致，证书文件中包含的公钥与签名密钥库文件内keyalias对应的私钥不匹配。

2、验证包完整性场景，已签名的HAP包被篡改。

**解决方案**

场景1：检查配置的证书文件和密钥库文件是否匹配，检查步骤如下：

1、查看签名配置。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bb/v3/QiBJCpgJRW6dEdDpzmSFJQ/zh-cn_image_0000002342678238.png?HW-CC-KV=V1&HW-CC-Date=20260612T024401Z&HW-CC-Expire=86400&HW-CC-Sign=01B9116CB2F67F4FEDD2227C6A85D0CF89459F2131F6E7C80B0FC42698134C42)

2、查看密钥库文件签名密钥关联的证书公钥信息（SubjectKeyIdentifier），示例：keytool -list -v -keystore ${Store file} -storepass ${Store password} -alias ${Key alias}。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6d/v3/oEnMCQIMSBap94boASxpaw/zh-cn_image_0000002342518438.png?HW-CC-KV=V1&HW-CC-Date=20260612T024401Z&HW-CC-Expire=86400&HW-CC-Sign=28CA0A9F7AD6C0417A583C020FB872E6C53AEB3B870B9D5535855795EE0478F1)

3、查看配置的证书文件中公钥信息，应用市场申请的证书，发布者是CN=Huawei CBG Developer Relations CA G2, OU=Huawei CBG, O=Huawei, C=CN，示例：keytool -printcert -file ${Certpath file}。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bb/v3/ombxzMF1RpGpdcUG5dFvug/zh-cn_image_0000002376516261.png?HW-CC-KV=V1&HW-CC-Date=20260612T024401Z&HW-CC-Expire=86400&HW-CC-Sign=7CFC0AF81EE4D55AC09E1DFFFCC269FF68C8C9560C9FF4C6AECF04F01DA124F5)

步骤2与步骤3中的公钥信息（SubjectKeyIdentifier）不一致，则配置的证书文件和密钥库文件不匹配。

场景2：重新打包签名。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bd/v3/3hrZxZt6Rt-EKEfmfkaPtA/zh-cn_image_0000002376396381.png?HW-CC-KV=V1&HW-CC-Date=20260612T024401Z&HW-CC-Expire=86400&HW-CC-Sign=0BBEE8A29747AC8D8AFECF8744DA7190A60414746AD142C1F8D5FC380D28FB61)
