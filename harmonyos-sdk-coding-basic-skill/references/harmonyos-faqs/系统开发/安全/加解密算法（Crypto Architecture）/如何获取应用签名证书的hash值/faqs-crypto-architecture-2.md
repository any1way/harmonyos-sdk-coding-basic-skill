---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-crypto-architecture-2
title: 如何获取应用签名证书的hash值
breadcrumb: FAQ > 系统开发 > 安全 > 加解密算法（Crypto Architecture） > 如何获取应用签名证书的hash值
category: harmonyos-faqs
scraped_at: 2026-06-12T10:36:54+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:244b7034cf9d2e3269a9e918ed3df2a2cb67daf19e50d7e42586a42e67def5bd
---
* “应用指纹”signatureInfo.fingerprint是应用签名证书（.cer文件）的SHA-256哈希值，当前支持获取本应用的指纹。示例代码如下：

  ```
  1. import { bundleManager } from '@kit.AbilityKit';
  2. import { hilog } from '@kit.PerformanceAnalysisKit';
  3. import { BusinessError } from '@kit.BasicServicesKit';

  5. let bundleFlags = bundleManager.BundleFlag.GET_BUNDLE_INFO_WITH_SIGNATURE_INFO;
  6. try {
  7. bundleManager.getBundleInfoForSelf(bundleFlags).then((data) => {
  8. hilog.info(0x0000, 'testTag', 'getBundleInfoForSelf successfully. Data: %{public}s', JSON.stringify(data));
  9. //In the data, you can obtain the signtureInfo, which is the signature certificate information of the application
  10. }).catch((err: BusinessError) => {
  11. hilog.error(0x0000, 'testTag', 'getBundleInfoForSelf failed. Cause: %{public}s', err.message);
  12. });
  13. } catch (err) {
  14. let message = (err as BusinessError).message;
  15. hilog.error(0x0000, 'testTag', 'getBundleInfoForSelf failed: %{public}s', message);
  16. }
  ```

  [ObtainCertificateHashValue\_One.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/CryptoArchitectureKit/entry/src/main/ets/pages/ObtainCertificateHashValue_One.ets#L21-L36)

* 对于hash值，可使用加解密框架的hash算法，目前支持SHA1、SHA224、SHA256、SHA384、SHA512、MD5。示例代码如下：

  ```
  1. import { common } from '@kit.AbilityKit';
  2. import { BusinessError } from '@kit.BasicServicesKit';
  3. import { hash } from '@kit.CoreFileKit';

  5. let context = AppStorage.get("context") as common.UIAbilityContext;
  6. let pathDir = context.filesDir;

  8. let filePath = pathDir + "/test.txt";
  9. hash.hash(filePath, "sha256").then((str: string) => {
  10. console.info("calculate file hash succeed:" + str);
  11. }).catch((err: BusinessError) => {
  12. console.error("calculate file hash failed with error message: " + err.message + ", error code: " + err.code);
  13. });
  ```

  [ObtainCertificateHashValue\_Two.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/CryptoArchitectureKit/entry/src/main/ets/pages/ObtainCertificateHashValue_Two.ets#L21-L33)

**参考链接**

[SignatureInfo](<../../../../../harmonyos-references/Ability Kit（程序框架服务）/ArkTS API/接口依赖的元素及定义/bundleManager/BundleInfo/js-apis-bundlemanager-bundleinfo.md#signatureinfo>)

[@ohos.file.hash (文件哈希处理)](<../../../../../harmonyos-references/Core File Kit（文件基础服务）/ArkTS API/@ohos.file.hash (文件哈希处理)/js-apis-file-hash.md>)
