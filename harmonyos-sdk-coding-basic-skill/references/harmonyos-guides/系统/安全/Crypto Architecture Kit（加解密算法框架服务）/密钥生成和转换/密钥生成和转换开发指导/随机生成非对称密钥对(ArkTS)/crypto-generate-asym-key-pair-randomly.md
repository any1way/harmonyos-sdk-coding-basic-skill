---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-generate-asym-key-pair-randomly
title: 随机生成非对称密钥对(ArkTS)
breadcrumb: 指南 > 系统 > 安全 > Crypto Architecture Kit（加解密算法框架服务） > 密钥生成和转换 > 密钥生成和转换开发指导 > 随机生成非对称密钥对(ArkTS)
category: harmonyos-guides
scraped_at: 2026-06-11T14:40:59+08:00
doc_updated_at: 2026-05-26
content_hash: sha256:4fd12b1b5435c6d8d744be2c6a26e6838f98c5913914caf633da18dd2b39913b
---
以RSA和SM2为例，随机生成非对称密钥对（KeyPair），并获得二进制数据。

非对称密钥对可用于后续加解密等操作，二进制数据可用于存储或传输。

## 随机生成RSA密钥对

对应的算法规格请查看[非对称密钥生成和转换规格：RSA](../../密钥生成和转换规格/非对称密钥生成和转换规格/crypto-asym-key-generation-conversion-spec.md#rsa)。

1. 调用[cryptoFramework.createAsyKeyGenerator](<../../../../../../../harmonyos-references/Crypto Architecture Kit（加解密算法框架服务）/ArkTS API/@ohos.security.cryptoFramework (加解密算法库框架)/js-apis-cryptoframework.md#cryptoframeworkcreateasykeygenerator>)，指定字符串参数'RSA1024|PRIMES\_2'，创建RSA密钥类型为RSA1024、素数个数为2的非对称密钥生成器（AsyKeyGenerator）。
2. 调用[AsyKeyGenerator.generateKeyPair](<../../../../../../../harmonyos-references/Crypto Architecture Kit（加解密算法框架服务）/ArkTS API/@ohos.security.cryptoFramework (加解密算法库框架)/js-apis-cryptoframework.md#generatekeypair-1>)，随机生成非对称密钥对象（KeyPair）。

   KeyPair对象中包括公钥PubKey、私钥PriKey。
3. 调用[PubKey.getEncoded](<../../../../../../../harmonyos-references/Crypto Architecture Kit（加解密算法框架服务）/ArkTS API/@ohos.security.cryptoFramework (加解密算法库框架)/js-apis-cryptoframework.md#getencoded>)和[PriKey.getEncoded](<../../../../../../../harmonyos-references/Crypto Architecture Kit（加解密算法框架服务）/ArkTS API/@ohos.security.cryptoFramework (加解密算法库框架)/js-apis-cryptoframework.md#getencoded>)，分别获取密钥对象的二进制数据。

* 以使用Promise方式随机生成RSA密钥对为例：

  ```
  1. import { cryptoFramework } from '@kit.CryptoArchitectureKit';

  3. function generateAsyKey() {
  4. // 创建一个AsyKeyGenerator实例
  5. let rsaGenerator = cryptoFramework.createAsyKeyGenerator('RSA1024|PRIMES_2');
  6. // 使用密钥生成器随机生成非对称密钥对
  7. let keyGenPromise = rsaGenerator.generateKeyPair();
  8. keyGenPromise.then(keyPair => {
  9. let pubKey = keyPair.pubKey;
  10. let priKey = keyPair.priKey;
  11. // 获取非对称密钥对的二进制数据
  12. let pkBlob = pubKey.getEncoded();
  13. let skBlob = priKey.getEncoded();
  14. console.info('pk bin data: ' + pkBlob.data);
  15. console.info('sk bin data: ' + skBlob.data);
  16. });
  17. }
  ```

  [Promise.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/Security/CryptoArchitectureKit/KeyGenerationConversion/RandomlyGenerateAsymmetricKeyPairArkTS/entry/src/main/ets/pages/rsa/Promise.ets#L16-L34)
* 同步返回结果（调用方法[generateKeyPairSync](<../../../../../../../harmonyos-references/Crypto Architecture Kit（加解密算法框架服务）/ArkTS API/@ohos.security.cryptoFramework (加解密算法库框架)/js-apis-cryptoframework.md#generatekeypairsync12>)）：

  ```
  1. import { cryptoFramework } from '@kit.CryptoArchitectureKit';

  3. function generateAsyKeySync() {
  4. // 创建一个AsyKeyGenerator实例
  5. let rsaGenerator = cryptoFramework.createAsyKeyGenerator('RSA1024|PRIMES_2');
  6. // 使用密钥生成器随机生成非对称密钥对
  7. try {
  8. let keyPair = rsaGenerator.generateKeyPairSync();
  9. if (keyPair != null) {
  10. let pubKey = keyPair.pubKey;
  11. let priKey = keyPair.priKey;
  12. // 获取非对称密钥对的二进制数据
  13. let pkBlob = pubKey.getEncoded();
  14. let skBlob = priKey.getEncoded();
  15. console.info('pk bin data: ' + pkBlob.data);
  16. console.info('sk bin data: ' + skBlob.data);
  17. } else {
  18. console.error('[Sync]: get key pair result: fail!');
  19. }
  20. } catch (e) {
  21. console.error(`get key pair failed: errCode: ${e.code}, message: ${e.message}`);
  22. }
  23. }
  ```

  [Sync.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/Security/CryptoArchitectureKit/KeyGenerationConversion/RandomlyGenerateAsymmetricKeyPairArkTS/entry/src/main/ets/pages/rsa/Sync.ets#L16-L40)

## 随机生成SM2密钥对

对应的算法规格请查看[非对称密钥生成和转换规格：SM2](../../密钥生成和转换规格/非对称密钥生成和转换规格/crypto-asym-key-generation-conversion-spec.md#sm2)。

1. 调用[cryptoFramework.createAsyKeyGenerator](<../../../../../../../harmonyos-references/Crypto Architecture Kit（加解密算法框架服务）/ArkTS API/@ohos.security.cryptoFramework (加解密算法库框架)/js-apis-cryptoframework.md#cryptoframeworkcreateasykeygenerator>)，指定字符串参数'SM2\_256'，创建密钥算法为SM2、密钥长度为256位的非对称密钥生成器（AsyKeyGenerator）。
2. 调用[AsyKeyGenerator.generateKeyPair](<../../../../../../../harmonyos-references/Crypto Architecture Kit（加解密算法框架服务）/ArkTS API/@ohos.security.cryptoFramework (加解密算法库框架)/js-apis-cryptoframework.md#generatekeypair-1>)，随机生成非对称密钥对象（KeyPair）。

   KeyPair对象中包括公钥PubKey、私钥PriKey。
3. 调用[PubKey.getEncoded](<../../../../../../../harmonyos-references/Crypto Architecture Kit（加解密算法框架服务）/ArkTS API/@ohos.security.cryptoFramework (加解密算法库框架)/js-apis-cryptoframework.md#getencoded>)和[PriKey.getEncoded](<../../../../../../../harmonyos-references/Crypto Architecture Kit（加解密算法框架服务）/ArkTS API/@ohos.security.cryptoFramework (加解密算法库框架)/js-apis-cryptoframework.md#getencoded>)，分别获取密钥对象的二进制数据。

* 以使用Promise方式随机生成SM2密钥对为例：

  ```
  1. import { cryptoFramework } from '@kit.CryptoArchitectureKit';

  3. function generateSM2Key() {
  4. // 创建一个AsyKeyGenerator实例
  5. let sm2Generator = cryptoFramework.createAsyKeyGenerator('SM2_256');
  6. // 使用密钥生成器随机生成非对称密钥对
  7. let keyGenPromise = sm2Generator.generateKeyPair();
  8. keyGenPromise.then(keyPair => {
  9. let pubKey = keyPair.pubKey;
  10. let priKey = keyPair.priKey;
  11. // 获取非对称密钥对的二进制数据
  12. let pkBlob = pubKey.getEncoded();
  13. let skBlob = priKey.getEncoded();
  14. console.info('pk bin data: ' + pkBlob.data);
  15. console.info('sk bin data: ' + skBlob.data);
  16. });
  17. }
  ```

  [Promise.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/Security/CryptoArchitectureKit/KeyGenerationConversion/RandomlyGenerateAsymmetricKeyPairArkTS/entry/src/main/ets/pages/sm2/Promise.ets#L16-L34)
* 同步返回结果（调用方法[generateKeyPairSync](<../../../../../../../harmonyos-references/Crypto Architecture Kit（加解密算法框架服务）/ArkTS API/@ohos.security.cryptoFramework (加解密算法库框架)/js-apis-cryptoframework.md#generatekeypairsync12>)）：

  ```
  1. import { cryptoFramework } from '@kit.CryptoArchitectureKit';

  3. function generateSM2KeySync() {
  4. // 创建一个AsyKeyGenerator实例
  5. let sm2Generator = cryptoFramework.createAsyKeyGenerator('SM2_256');
  6. // 使用密钥生成器随机生成非对称密钥对
  7. try {
  8. let keyPair = sm2Generator.generateKeyPairSync();
  9. if (keyPair != null) {
  10. let pubKey = keyPair.pubKey;
  11. let priKey = keyPair.priKey;
  12. // 获取非对称密钥对的二进制数据
  13. let pkBlob = pubKey.getEncoded();
  14. let skBlob = priKey.getEncoded();
  15. console.info('pk bin data: ' + pkBlob.data);
  16. console.info('sk bin data: ' + skBlob.data);
  17. } else {
  18. console.error('[Sync]: get key pair result: fail!');
  19. }
  20. } catch (e) {
  21. console.error(`get key pair failed: errCode: ${e.code}, message: ${e.message}`);
  22. }
  23. }
  ```

  [Sync.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/Security/CryptoArchitectureKit/KeyGenerationConversion/RandomlyGenerateAsymmetricKeyPairArkTS/entry/src/main/ets/pages/sm2/Sync.ets#L16-L40)
