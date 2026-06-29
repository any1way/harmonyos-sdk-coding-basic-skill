---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/devicesecurity-taas-verifycertchain
title: 验证匿名证书链
breadcrumb: 指南 > 系统 > 安全 > Device Security Kit（设备安全服务） > 可信应用服务 > 签名验证 > 验证匿名证书链
category: harmonyos-guides
scraped_at: 2026-06-11T14:43:57+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:00a7ffb54cb9dc8c248286fa3686251e008224ef3a709b9d0b3d782dfa3bbb29
---
为防止第三方伪造数据，端侧和云侧在对数据进行验签之前，必须先验证匿名证书链的正确性。端侧对匿名证书链的校验处理接口，请参考“[证书链校验器对象的创建和校验](<../../../../Device Certificate Kit（设备证书服务）/证书算法库框架/证书链校验器对象的创建和校验/create-verify-cerchainvalidator-object.md>)”。云侧对匿名证书链的校验处理接口，请参考“[设备真实性证明](<../../../../Universal Keystore Kit（密钥管理服务）/本地密钥管理/应用真实性证明/device-attestation.md>)”的服务器端开发章节。

初始化证明会话时返回的匿名证书链包含三级证书，验证步骤如下：

1. 使用[Universal Keystore Kit](<../../../../Universal Keystore Kit（密钥管理服务）/Universal Keystore Kit简介/huks-overview.md>)官网提供的根CA证书对匿名证书链的合法性进行校验。（[根CA证书下载地址](https://pki.consumer.huawei.com/ca/cer/Huawei_CBG_ECC_Device_Attestation_Root_CA.cer)）

   说明

   请勿在应用服务器中使用子CA证书对密钥证明证书链进行校验，子CA证书可能会因为有效期结束、证书被吊销等发生变化。
2. 解析三级证书获取应用公钥、AppID、密钥管理部件ID。

   1. 应用公钥直接从密钥证明证书的subjectPublicKeyInfo字段获取。
   2. AppID从扩展字段“1.3.6.1.4.1.2011.2.376.2.1.3.1”获取。
   3. 密钥管理部件ID从扩展字段“1.3.6.1.4.1.2011.2.376.2.2.2.6”获取。
3. 检查三级证书的扩展字段是否符合预期：

   1. 密钥管理部件ID应为“0E01669E9CFF3848A9538568F1A483E3”。
   2. AppID的值应为调用创建证明密钥接口的应用AppID。

   说明

   “应用AppID”指的是HarmonyOS应用的ID，包含bundleName和签名证书公钥的哈希值。 获取应用AppID方法请参考“[bundleManager 模块](<../../../../../../../harmonyos-references/Ability Kit（程序框架服务）/ArkTS API/通用能力的接口(推荐)/@ohos.bundle.bundleManager (应用程序包管理模块)/js-apis-bundlemanager.md#bundlemanagergetbundleinfoforself-1>)”。
