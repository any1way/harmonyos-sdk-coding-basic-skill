---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-key-derivation-using-x963kdf-ndk
title: 使用X963KDF进行密钥派生(C/C++)
breadcrumb: 指南 > 系统 > 安全 > Crypto Architecture Kit（加解密算法框架服务） > 密钥派生 > 使用X963KDF进行密钥派生(C/C++)
category: harmonyos-guides
scraped_at: 2026-06-01T11:15:34+08:00
doc_updated_at: 2026-05-26
content_hash: sha256:048f7de41c0d047bb827d9514e5dbcfc07726179eb83cd395468f313b3dc5962
---
从API version 22开始，算法库支持使用该算法进行密钥派生操作。

对应算法规格请查看[密钥派生算法规格：X963KDF](../密钥派生介绍及算法规格/crypto-key-derivation-overview.md#x963kdf算法)。

## 开发步骤

1. 调用[OH\_CryptoKdfParams\_Create](<../../../../../../harmonyos-references/Crypto Architecture Kit（加解密算法框架服务）/C API/头文件/crypto_kdf.h/capi-crypto-kdf-h.md#oh_cryptokdfparams_create>)，指定字符串参数'X963KDF'，创建密钥派生参数对象。
2. 调用[OH\_CryptoKdfParams\_SetParam](<../../../../../../harmonyos-references/Crypto Architecture Kit（加解密算法框架服务）/C API/头文件/crypto_kdf.h/capi-crypto-kdf-h.md#oh_cryptokdfparams_setparam>)，设置X963KDF所需的参数。示例如下：

   * CRYPTO\_KDF\_KEY\_DATABLOB：用于生成派生密钥的原始密钥材料。
   * CRYPTO\_KDF\_INFO\_DATABLOB：应用程序特定的信息（可选）。
3. 调用[OH\_CryptoKdf\_Create](<../../../../../../harmonyos-references/Crypto Architecture Kit（加解密算法框架服务）/C API/头文件/crypto_kdf.h/capi-crypto-kdf-h.md#oh_cryptokdf_create>)，指定字符串参数'X963KDF|SHA256'，创建密钥派生函数对象。
4. 调用[OH\_CryptoKdf\_Derive](<../../../../../../harmonyos-references/Crypto Architecture Kit（加解密算法框架服务）/C API/头文件/crypto_kdf.h/capi-crypto-kdf-h.md#oh_cryptokdf_derive>)，指定目标密钥的字节长度，进行密钥派生。

```
1. #include "CryptoArchitectureKit/crypto_architecture_kit.h"
2. #include <cstdio>
3. #include <cstring>
4. #include "file.h"

6. OH_Crypto_ErrCode doTestX963Kdf()
7. {
8. // 创建X963KDF参数对象。
9. OH_CryptoKdfParams *params = nullptr;
10. OH_Crypto_ErrCode ret = OH_CryptoKdfParams_Create("X963KDF", &params);
11. if (ret != CRYPTO_SUCCESS) {
12. return ret;
13. }

15. // 设置原始密钥材料。
16. const char *keyData = "012345678901234567890123456789";
17. Crypto_DataBlob key = {
18. .data = reinterpret_cast<uint8_t *>(const_cast<char *>(keyData)),
19. .len = strlen(keyData)
20. };
21. ret = OH_CryptoKdfParams_SetParam(params, CRYPTO_KDF_KEY_DATABLOB, &key);
22. if (ret != CRYPTO_SUCCESS) {
23. OH_CryptoKdfParams_Destroy(params);
24. return ret;
25. }

27. // 设置应用程序特定信息。
28. const char *infoData = "infostring";
29. Crypto_DataBlob info = {
30. .data = reinterpret_cast<uint8_t *>(const_cast<char *>(infoData)),
31. .len = strlen(infoData)
32. };
33. ret = OH_CryptoKdfParams_SetParam(params, CRYPTO_KDF_INFO_DATABLOB, &info);
34. if (ret != CRYPTO_SUCCESS) {
35. OH_CryptoKdfParams_Destroy(params);
36. return ret;
37. }

39. // 创建密钥派生函数对象。
40. OH_CryptoKdf *kdfCtx = nullptr;
41. ret = OH_CryptoKdf_Create("X963KDF|SHA256", &kdfCtx);
42. if (ret != CRYPTO_SUCCESS) {
43. OH_CryptoKdfParams_Destroy(params);
44. return ret;
45. }

47. // 派生密钥。
48. Crypto_DataBlob out = {0};
49. uint32_t keyLength = 32; // 生成32字节的密钥。
50. ret = OH_CryptoKdf_Derive(kdfCtx, params, keyLength, &out);
51. if (ret != CRYPTO_SUCCESS) {
52. OH_CryptoKdf_Destroy(kdfCtx);
53. OH_CryptoKdfParams_Destroy(params);
54. return ret;
55. }

57. printf("Derived key length: %u\n", out.len);

59. // 清理资源。
60. OH_Crypto_FreeDataBlob(&out);
61. OH_CryptoKdf_Destroy(kdfCtx);
62. OH_CryptoKdfParams_Destroy(params);
63. return CRYPTO_SUCCESS;
64. }
```

[x963kdf\_test.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/Security/CryptoArchitectureKit/KeyDerivation/X963KDFDerivation/entry/src/main/cpp/types/project/x963kdf_test.cpp#L16-L81)
