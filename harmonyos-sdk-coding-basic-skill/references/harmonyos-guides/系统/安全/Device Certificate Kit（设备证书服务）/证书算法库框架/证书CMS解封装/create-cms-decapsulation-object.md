---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/create-cms-decapsulation-object
title: 证书CMS解封装
breadcrumb: 指南 > 系统 > 安全 > Device Certificate Kit（设备证书服务） > 证书算法库框架 > 证书CMS解封装
category: harmonyos-guides
scraped_at: 2026-06-11T14:43:25+08:00
doc_updated_at: 2026-06-05
content_hash: sha256:d72a5c78715fd4caac7fcc71f46ccfa2b1d99fdd890c2c2dbadab7fe2fbcd1b1
---
从API version 22开始，支持证书CMS解封装。

PKCS#7是用于存储签名或加密数据的标准语法。CMS作为PKCS#7的扩展，支持的数据类型包括数据、签名数据、封装数据、签名和封装数据、摘要数据以及加密数据。该标准常用于保护数据的完整性和机密性。

目前仅支持CMS签名数据和封装数据。

## 开发步骤

1. 导入[证书模块](<../../../../../../harmonyos-references/Device Certificate Kit（设备证书服务）/ArkTS API/@ohos.security.cert (证书模块)/js-apis-cert.md>)。

   ```
   1. import { cert } from '@kit.DeviceCertificateKit';
   ```
2. 调用[证书CMS封装](../证书CMS封装/create-cms-enveloped-object.md)进行CMS数据封装。
3. 调用[cert.createCmsParser](<../../../../../../harmonyos-references/Device Certificate Kit（设备证书服务）/ArkTS API/@ohos.security.cert (证书模块)/js-apis-cert.md#certcreatecmsparser22>)创建CmsParser对象。
4. 调用[cmsParser.setRawData](<../../../../../../harmonyos-references/Device Certificate Kit（设备证书服务）/ArkTS API/@ohos.security.cert (证书模块)/js-apis-cert.md#setrawdata22>)设置CMS数据。
5. 调用[cmsParser.decryptEnvelopedData](<../../../../../../harmonyos-references/Device Certificate Kit（设备证书服务）/ArkTS API/@ohos.security.cert (证书模块)/js-apis-cert.md#decryptenvelopeddata22>)解密封装数据。

解封装示例：

```
1. import { cert } from '@kit.DeviceCertificateKit';

3. let ECC_256_PUBKEY: string =
4. '-----BEGIN CERTIFICATE-----\n' +
5. 'MIICGDCCAb6gAwIBAgIGAXKnJjrAMAoGCCqGSM49BAMCMFcxCzAJBgNVBAYTAkNO\n' +
6. 'MQ8wDQYDVQQIDAbpmZXopb8xDzANBgNVBAcMBuilv+WuiTEPMA0GA1UECgwG5rWL\n' +
7. '6K+VMRUwEwYDVQQDDAzkuK3mlofmtYvor5UwHhcNMjUwOTE2MDY0MTMwWhcNMzUw\n' +
8. 'OTE0MDY0MTMwWjBXMQswCQYDVQQGEwJDTjEPMA0GA1UECAwG6ZmV6KW/MQ8wDQYD\n' +
9. 'VQQHDAbopb/lrokxDzANBgNVBAoMBua1i+ivlTEVMBMGA1UEAwwM5Lit5paH5rWL\n' +
10. '6K+VMFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAEB06h4SzOryi3d7PW9yN2wACC\n' +
11. 'VxlduBQjVLWZlDKhFKkdZjve8mUyytSSbBj/rrzR2XmzUzofuNkUbAtje3DDJqN2\n' +
12. 'MHQwHQYDVR0OBBYEFNtUldgBESf31bwTnYtApIctaSdtMB8GA1UdIwQYMBaAFNtU\n' +
13. 'ldgBESf31bwTnYtApIctaSdtMAsGA1UdDwQEAwIBBjAJBgNVHREEAjAAMAkGA1Ud\n' +
14. 'EgQCMAAwDwYDVR0TAQH/BAUwAwEB/zAKBggqhkjOPQQDAgNIADBFAiEAzxzaG2vR\n' +
15. 'zUnFFL3X3lRQ0IOJrb6cvkSZuaFd4bW2lgUCIHW6QGGnECDFMbDNz7Og9kjkt+3k\n' +
16. 'FmEJWqEMYudBH3Ul\n' +
17. '-----END CERTIFICATE-----';
18. let ECC_256_PRIVATE: string =
19. '-----BEGIN PRIVATE KEY-----\n' +
20. 'MIGHAgEAMBMGByqGSM49AgEGCCqGSM49AwEHBG0wawIBAQQgOYwEyIw3ZNIAL4xO\n' +
21. 'pP6eVcQYcrL2sfnt6vB0z9tKmMmhRANCAAQHTqHhLM6vKLd3s9b3I3bAAIJXGV24\n' +
22. 'FCNUtZmUMqEUqR1mO97yZTLK1JJsGP+uvNHZebNTOh+42RRsC2N7cMMm\n' +
23. '-----END PRIVATE KEY-----';

25. // string转Uint8Array。
26. function stringToUint8Array(str: string): Uint8Array {
27. let arr: number[] = [];
28. for (let i = 0, j = str.length; i < j; i++) {
29. arr.push(str.charCodeAt(i));
30. };
31. return new Uint8Array(arr);
32. }

34. async function createX509Cert(inStream: string): Promise<cert.X509Cert> {
35. let encodingBlob: cert.EncodingBlob = {
36. data: stringToUint8Array(inStream),
37. encodingFormat: cert.EncodingFormat.FORMAT_PEM
38. };
39. let x509Cert: cert.X509Cert = {} as cert.X509Cert;
40. try {
41. x509Cert = await cert.createX509Cert(encodingBlob);
42. } catch (error) {
43. console.error(`createX509Cert failed: errCode: ${error.code}, message: ${error.message}`);
44. }
45. return x509Cert;
46. }

48. async function testCmsDecryptTest() {
49. try {
50. let plainText: Uint8Array = new Uint8Array([0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07]);
51. let x509CertEc: cert.X509Cert = await createX509Cert(ECC_256_PUBKEY);
52. let cms: cert.CmsGenerator = cert.createCmsGenerator(cert.CmsContentType.ENVELOPED_DATA);
53. let option: cert.CmsGeneratorOptions = {
54. outFormat: cert.CmsFormat.PEM
55. };
56. cms.setRecipientEncryptionAlgorithm(cert.CmsRecipientEncryptionAlgorithm.AES_128_GCM);
57. let recipientInfo: cert.CmsRecipientInfo = {
58. keyAgreeInfo: {
59. cert: x509CertEc,
60. digestAlgorithm: cert.CmsKeyAgreeRecipientDigestAlgorithm.SHA256
61. }
62. };
63. await cms.addRecipientInfo(recipientInfo);
64. console.info('add recipient result: success, digestAlgorithm = ' + recipientInfo.keyAgreeInfo?.digestAlgorithm);
65. let envelopeData = await cms.doFinal(plainText, option);
66. console.info('doFinal result: success, envelopeData = ' + envelopeData);
67. let cipherText = await cms.getEncryptedContentData();
68. console.info('getEncryptedContentData result: success, cipherText = ' + cipherText);
69. let config: cert.CmsEnvelopedDecryptionConfig = {
70. keyInfo: {
71. key: ECC_256_PRIVATE
72. },
73. };
74. let cmsDecrypt: cert.CmsParser = cert.createCmsParser();
75. await cmsDecrypt.setRawData(envelopeData, cert.CmsFormat.PEM);
76. let decPlainText: Uint8Array = await cmsDecrypt.decryptEnvelopedData(config);
77. console.info('[XTS] decryptEnvelopedData result: success, decPlainText = ' + decPlainText);
78. console.info('decryptEnvelopedData result: success.');
79. } catch (error) {
80. console.error(`decryptEnvelopedData failed: errCode: ${error.code}, message: ${error.message}`);
81. }
82. }
```

[CreateCmsDecapsulationObject.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/Security/DeviceCertificateKit/CertificateAlgorithmLibrary/entry/src/main/ets/pages/CreateCmsDecapsulationObject.ets#L16-L101)
