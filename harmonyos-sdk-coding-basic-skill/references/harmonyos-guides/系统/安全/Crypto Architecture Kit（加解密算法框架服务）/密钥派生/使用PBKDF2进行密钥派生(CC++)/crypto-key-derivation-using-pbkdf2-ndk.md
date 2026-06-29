---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-key-derivation-using-pbkdf2-ndk
title: 使用PBKDF2进行密钥派生(C/C++)
breadcrumb: 指南 > 系统 > 安全 > Crypto Architecture Kit（加解密算法框架服务） > 密钥派生 > 使用PBKDF2进行密钥派生(C/C++)
category: harmonyos-guides
scraped_at: 2026-06-11T14:42:54+08:00
doc_updated_at: 2026-06-03
content_hash: sha256:840c69659d36cbe564e6afa03a600d2c579d02fcf1dcbe741bdb3d6c36416d98
---
对应的算法规格请查看[密钥派生算法规格：PBKDF2](../密钥派生介绍及算法规格/crypto-key-derivation-overview.md#pbkdf2算法)。

## 开发步骤

1. 调用[OH\_CryptoKdfParams\_Create](<../../../../../../harmonyos-references/Crypto Architecture Kit（加解密算法框架服务）/C API/头文件/crypto_kdf.h/capi-crypto-kdf-h.md#oh_cryptokdfparams_create>)，指定字符串参数'PBKDF2'，创建密钥派生参数对象。
2. 调用[OH\_CryptoKdfParams\_SetParam](<../../../../../../harmonyos-references/Crypto Architecture Kit（加解密算法框架服务）/C API/头文件/crypto_kdf.h/capi-crypto-kdf-h.md#oh_cryptokdfparams_setparam>)，设置PBKDF2所需的参数。示例如下：

   * CRYPTO\_KDF\_KEY\_DATABLOB：用于生成派生密钥的原始密码。
   * CRYPTO\_KDF\_SALT\_DATABLOB：盐值。
   * CRYPTO\_KDF\_ITER\_COUNT\_INT：重复运算的次数，需要为正整数。
3. 调用[OH\_CryptoKdf\_Create](<../../../../../../harmonyos-references/Crypto Architecture Kit（加解密算法框架服务）/C API/头文件/crypto_kdf.h/capi-crypto-kdf-h.md#oh_cryptokdf_create>)，指定字符串参数'PBKDF2|SHA256'，创建密钥派生函数对象。
4. 调用[OH\_CryptoKdf\_Derive](<../../../../../../harmonyos-references/Crypto Architecture Kit（加解密算法框架服务）/C API/头文件/crypto_kdf.h/capi-crypto-kdf-h.md#oh_cryptokdf_derive>)，指定目标密钥的字节长度，进行密钥派生。

```
1. #include "CryptoArchitectureKit/crypto_architecture_kit.h"
2. #include <cstdio>
3. #include <cstring>
4. #include "file.h"

6. static OH_Crypto_ErrCode setParams(OH_CryptoKdfParams **params)
7. {
8. char password[] = "123456";
9. const char *salt = "saltstring";
10. int iterations = 10000;
11. // 设置密码。
12. Crypto_DataBlob passwordBlob = {
13. .data = reinterpret_cast<uint8_t *>(const_cast<char *>(password)),
14. .len = strlen(password)
15. };
16. OH_Crypto_ErrCode ret = OH_CryptoKdfParams_SetParam(*params, CRYPTO_KDF_KEY_DATABLOB, &passwordBlob);
17. if (ret != CRYPTO_SUCCESS) {
18. (void)memset(password, 0, sizeof(password));
19. OH_CryptoKdfParams_Destroy(*params);
20. *params = nullptr;
21. return ret;
22. }

24. // 设置盐值。
25. Crypto_DataBlob saltBlob = {
26. .data = reinterpret_cast<uint8_t *>(const_cast<char *>(salt)),
27. .len = strlen(salt)
28. };
29. ret = OH_CryptoKdfParams_SetParam(*params, CRYPTO_KDF_SALT_DATABLOB, &saltBlob);
30. if (ret != CRYPTO_SUCCESS) {
31. (void)memset(password, 0, sizeof(password));
32. OH_CryptoKdfParams_Destroy(*params);
33. *params = nullptr;
34. return ret;
35. }

37. // 设置迭代次数。
38. Crypto_DataBlob iterationsBlob = {
39. .data = reinterpret_cast<uint8_t *>(&iterations),
40. .len = sizeof(int)
41. };
42. ret = OH_CryptoKdfParams_SetParam(*params, CRYPTO_KDF_ITER_COUNT_INT, &iterationsBlob);
43. if (ret != CRYPTO_SUCCESS) {
44. (void)memset(password, 0, sizeof(password));
45. OH_CryptoKdfParams_Destroy(*params);
46. *params = nullptr;
47. return ret;
48. }
49. return CRYPTO_SUCCESS;
50. }

52. OH_Crypto_ErrCode doTestPbkdf2()
53. {
54. // 创建PBKDF2参数对象。
55. OH_CryptoKdfParams *params = nullptr;
56. OH_Crypto_ErrCode ret = OH_CryptoKdfParams_Create("PBKDF2", &params);
57. if (ret != CRYPTO_SUCCESS) {
58. return ret;
59. }

61. ret = setParams(&params);
62. if (ret != CRYPTO_SUCCESS) {
63. return ret;
64. }

66. // 创建密钥派生函数对象。
67. OH_CryptoKdf *kdfCtx = nullptr;
68. ret = OH_CryptoKdf_Create("PBKDF2|SHA256", &kdfCtx);
69. if (ret != CRYPTO_SUCCESS) {
70. OH_CryptoKdfParams_Destroy(params);
71. return ret;
72. }

74. // 派生密钥。
75. Crypto_DataBlob out = {0};
76. uint32_t keyLength = 32; // 生成32字节的密钥。
77. ret = OH_CryptoKdf_Derive(kdfCtx, params, keyLength, &out);
78. if (ret != CRYPTO_SUCCESS) {
79. OH_CryptoKdf_Destroy(kdfCtx);
80. OH_CryptoKdfParams_Destroy(params);
81. return ret;
82. }

84. printf("Derived key length: %u\n", out.len);

86. // 清理资源。
87. OH_Crypto_FreeDataBlob(&out);
88. OH_CryptoKdf_Destroy(kdfCtx);
89. OH_CryptoKdfParams_Destroy(params);
90. return CRYPTO_SUCCESS;
91. }
```

[pbkdf2\_test.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/Security/CryptoArchitectureKit/KeyDerivation/PBKDF2Derivation/entry/src/main/cpp/types/project/pbkdf2_test.cpp#L16-L108)
