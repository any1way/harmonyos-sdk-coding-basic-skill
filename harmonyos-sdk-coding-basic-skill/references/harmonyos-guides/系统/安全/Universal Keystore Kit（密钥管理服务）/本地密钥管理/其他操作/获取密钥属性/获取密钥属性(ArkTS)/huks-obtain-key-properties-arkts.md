---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/huks-obtain-key-properties-arkts
title: 获取密钥属性(ArkTS)
breadcrumb: 指南 > 系统 > 安全 > Universal Keystore Kit（密钥管理服务） > 本地密钥管理 > 其他操作 > 获取密钥属性 > 获取密钥属性(ArkTS)
category: harmonyos-guides
scraped_at: 2026-06-01T11:18:29+08:00
doc_updated_at: 2026-05-26
content_hash: sha256:7483b743e1fb9ad1ebc4a700c54a4b208e3167148803870b2aedb93d53fc43ab
---
HUKS提供了接口供业务获取指定密钥的相关属性。在获取指定密钥属性前，需要确保已在HUKS中生成或导入持久化存储的密钥。

说明

轻量级智能穿戴不支持获取密钥属性功能。

从API 23开始支持[群组密钥](../../群组密钥/群组密钥介绍/huks-group-key-overview.md)特性。

## 开发步骤

1. 指定待查询的密钥别名keyAlias，密钥别名最大长度为128字节。
2. 调用接口[getKeyItemProperties](<../../../../../../../../harmonyos-references/安全/Universal Keystore Kit（密钥管理服务）/ArkTS API/@ohos.security.huks (通用密钥库系统)/js-apis-huks.md#huksgetkeyitemproperties9>)，传入参数keyAlias和options。options为预留参数，当前可传入空。
3. 返回值为[HuksReturnResult](<../../../../../../../../harmonyos-references/安全/Universal Keystore Kit（密钥管理服务）/ArkTS API/@ohos.security.huks (通用密钥库系统)/js-apis-huks.md#huksreturnresult9>)类型对象，获取的属性集在properties字段中。

```
1. import { huks } from '@kit.UniversalKeystoreKit';

3. /* 1. 设置密钥别名 */
4. let keyAlias = 'keyAlias';
5. /* option对象传空 */
6. let emptyOptions: huks.HuksOptions = {
7. properties: []
8. };
9. let properties1: huks.HuksParam[] = [
10. {
11. tag: huks.HuksTag.HUKS_TAG_ALGORITHM,
12. value: huks.HuksKeyAlg.HUKS_ALG_DH
13. },
14. {
15. tag: huks.HuksTag.HUKS_TAG_PURPOSE,
16. value: huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_AGREE
17. },
18. {
19. tag: huks.HuksTag.HUKS_TAG_KEY_SIZE,
20. value: huks.HuksKeySize.HUKS_DH_KEY_SIZE_2048
21. }
22. ];

24. let huksOptions: huks.HuksOptions = {
25. properties: properties1,
26. inData: new Uint8Array([])
27. }

29. /* 3.生成密钥 */
30. function generateKeyItem(keyAlias: string, huksOptions: huks.HuksOptions) {
31. return new Promise<void>((resolve, reject) => {
32. try {
33. huks.generateKeyItem(keyAlias, huksOptions, (error, data) => {
34. if (error) {
35. reject(error);
36. } else {
37. resolve(data);
38. }
39. });
40. } catch (error) {
41. throw (error as Error);
42. }
43. });
44. }

46. async function publicGenKeyFunc(keyAlias: string, huksOptions: huks.HuksOptions): Promise<string> {
47. console.info(`enter promise generateKeyItem`);
48. try {
49. await generateKeyItem(keyAlias, huksOptions)
50. .then((data) => {
51. console.info(`promise: generateKeyItem success, data = ${JSON.stringify(data)}`);
52. })
53. .catch((error: Error) => {
54. console.error(`promise: generateKeyItem failed, ${JSON.stringify(error)}`);
55. });
56. return 'Success';
57. } catch (error) {
58. console.error(`promise: generateKeyItem input arg invalid, ${JSON.stringify(error)}`);
59. return 'Failed';
60. }
61. }

63. async function testGenKey(): Promise<string> {
64. let ret = await publicGenKeyFunc(keyAlias, huksOptions);
65. return ret;
66. }

68. function check(): string {
69. try {
70. /* 1. 生成密钥 */
71. testGenKey();
72. /* 2. 获取密钥属性 */
73. huks.getKeyItemProperties(keyAlias, emptyOptions, (error, data) => {
74. if (error) {
75. console.error(`callback: getKeyItemProperties failed, ${JSON.stringify(error)}`);
76. } else {
77. console.info(`callback: getKeyItemProperties success, data = ${JSON.stringify(data)}`);
78. }
79. });
80. return 'Success';
81. } catch (error) {
82. console.error(`callback: getKeyItemProperties input arg invalid, ${JSON.stringify(error)}`);
83. return 'Failed';
84. }
85. }
```

[GetKeyAttributes.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/Security/UniversalKeystoreKit/OtherOperations/GetKeyAttributes/entry/src/main/ets/pages/GetKeyAttributes.ets#L16-L103)
