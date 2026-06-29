---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-key-derivation-using-hkdf-ndk
title: 使用HKDF进行密钥派生(C/C++)
breadcrumb: 指南 > 系统 > 安全 > Crypto Architecture Kit（加解密算法框架服务） > 密钥派生 > 使用HKDF进行密钥派生(C/C++)
category: harmonyos-guides
scraped_at: 2026-06-11T14:42:57+08:00
doc_updated_at: 2026-06-03
content_hash: sha256:949e9642eb1771f54b6dbdd2fa1ff5c9c1a1736ddf04f0ce9b6d36363f597c08
---
对应算法规格请查看[密钥派生算法规格：HKDF](../密钥派生介绍及算法规格/crypto-key-derivation-overview.md#hkdf算法)。

## 开发步骤

1. 调用[OH\_CryptoKdfParams\_Create](<../../../../../../harmonyos-references/Crypto Architecture Kit（加解密算法框架服务）/C API/头文件/crypto_kdf.h/capi-crypto-kdf-h.md#oh_cryptokdfparams_create>)，指定字符串参数'HKDF'，创建密钥派生参数对象。
2. 调用[OH\_CryptoKdfParams\_SetParam](<../../../../../../harmonyos-references/Crypto Architecture Kit（加解密算法框架服务）/C API/头文件/crypto_kdf.h/capi-crypto-kdf-h.md#oh_cryptokdfparams_setparam>)，设置HKDF所需的参数。示例如下：

   * CRYPTO\_KDF\_KEY\_DATABLOB：用于生成派生密钥的原始密钥材料。
   * CRYPTO\_KDF\_SALT\_DATABLOB：盐值。
   * CRYPTO\_KDF\_INFO\_DATABLOB：应用程序特定的信息（可选）。
3. 调用[OH\_CryptoKdf\_Create](<../../../../../../harmonyos-references/Crypto Architecture Kit（加解密算法框架服务）/C API/头文件/crypto_kdf.h/capi-crypto-kdf-h.md#oh_cryptokdf_create>)，指定字符串参数'HKDF|SHA256|EXTRACT\_AND\_EXPAND'，创建密钥派生函数对象。
4. 调用[OH\_CryptoKdf\_Derive](<../../../../../../harmonyos-references/Crypto Architecture Kit（加解密算法框架服务）/C API/头文件/crypto_kdf.h/capi-crypto-kdf-h.md#oh_cryptokdf_derive>)，指定目标密钥的字节长度，进行密钥派生。

```
1. #include "CryptoArchitectureKit/crypto_architecture_kit.h"
2. #include <cstdio>
3. #include <cstring>
4. #include "file.h"

6. static OH_Crypto_ErrCode setParams(OH_CryptoKdfParams **params)
7. {
8. const char *keyData = "012345678901234567890123456789";
9. Crypto_DataBlob key = {
10. .data = reinterpret_cast<uint8_t *>(const_cast<char *>(keyData)),
11. .len = strlen(keyData)
12. };
13. OH_Crypto_ErrCode ret = OH_CryptoKdfParams_SetParam(*params, CRYPTO_KDF_KEY_DATABLOB, &key);
14. if (ret != CRYPTO_SUCCESS) {
15. OH_CryptoKdfParams_Destroy(*params);
16. *params = nullptr;
17. return ret;
18. }

20. // 设置盐值。
21. const char *saltData = "saltstring";
22. Crypto_DataBlob salt = {
23. .data = reinterpret_cast<uint8_t *>(const_cast<char *>(saltData)),
24. .len = strlen(saltData)
25. };
26. ret = OH_CryptoKdfParams_SetParam(*params, CRYPTO_KDF_SALT_DATABLOB, &salt);
27. if (ret != CRYPTO_SUCCESS) {
28. OH_CryptoKdfParams_Destroy(*params);
29. *params = nullptr;
30. return ret;
31. }

33. // 设置应用程序特定信息（可选）。
34. const char *infoData = "infostring";
35. Crypto_DataBlob info = {
36. .data = reinterpret_cast<uint8_t *>(const_cast<char *>(infoData)),
37. .len = strlen(infoData)
38. };
39. ret = OH_CryptoKdfParams_SetParam(*params, CRYPTO_KDF_INFO_DATABLOB, &info);
40. if (ret != CRYPTO_SUCCESS) {
41. OH_CryptoKdfParams_Destroy(*params);
42. *params = nullptr;
43. return ret;
44. }
45. return CRYPTO_SUCCESS;
46. }

48. OH_Crypto_ErrCode doTestHkdf()
49. {
50. // 创建HKDF参数对象。
51. OH_CryptoKdfParams *params = nullptr;
52. OH_Crypto_ErrCode ret = OH_CryptoKdfParams_Create("HKDF", &params);
53. if (ret != CRYPTO_SUCCESS) {
54. return ret;
55. }

57. ret = setParams(&params);
58. if (ret != CRYPTO_SUCCESS) {
59. return ret;
60. }

62. // 创建密钥派生函数对象。
63. OH_CryptoKdf *kdfCtx = nullptr;
64. ret = OH_CryptoKdf_Create("HKDF|SHA256|EXTRACT_AND_EXPAND", &kdfCtx);
65. if (ret != CRYPTO_SUCCESS) {
66. OH_CryptoKdfParams_Destroy(params);
67. return ret;
68. }

70. // 派生密钥。
71. Crypto_DataBlob out = {0};
72. uint32_t keyLength = 32; // 生成32字节的密钥。
73. ret = OH_CryptoKdf_Derive(kdfCtx, params, keyLength, &out);
74. if (ret != CRYPTO_SUCCESS) {
75. OH_CryptoKdf_Destroy(kdfCtx);
76. OH_CryptoKdfParams_Destroy(params);
77. return ret;
78. }

80. printf("Derived key length: %u\n", out.len);

82. // 清理资源。
83. OH_Crypto_FreeDataBlob(&out);
84. OH_CryptoKdf_Destroy(kdfCtx);
85. OH_CryptoKdfParams_Destroy(params);
86. return CRYPTO_SUCCESS;
87. }
```

[hkdf\_test.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/Security/CryptoArchitectureKit/KeyDerivation/HKDFDerivation/entry/src/main/cpp/types/project/hkdf_test.cpp#L16-L104)
