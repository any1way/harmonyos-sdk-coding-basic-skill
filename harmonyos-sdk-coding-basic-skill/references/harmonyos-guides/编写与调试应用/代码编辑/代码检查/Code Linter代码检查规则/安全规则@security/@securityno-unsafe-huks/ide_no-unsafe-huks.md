---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_no-unsafe-huks
title: @security/no-unsafe-huks
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 安全规则@security > @security/no-unsafe-huks
category: harmonyos-guides
scraped_at: 2026-06-01T15:21:39+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:e3d477b49fd83d13425421f82dede7d6bea8eaf35bed10d22adedbdb7b226505
---
此规则禁止在HUKS中使用不安全的加密模式ECB，不安全的摘要算法MD5、SHA1，填充算法NONE、PKCS1-V1\_5。推荐使用HUKS的AES-GCM算法，详情参见：[对称加解密算法](https://developer.huawei.com/consumer/cn/doc/AppGallery-connect-Guides/aegis-encryption-and-decryption-symmetry-0000001861247310)。

## 规则配置

```
1. // code-linter.json5
2. {
3. "rules": {
4. "@security/no-unsafe-huks": "warn"
5. }
6. }
```

## 选项

该规则无需配置额外选项。

## 正例

```
1. import {huks} from '@kit.UniversalKeystoreKit';
2. let keyAlias: string = 'keyAlias';
3. let properties: Array<huks.HuksParam> = [
4. {
5. tag: huks.HuksTag.HUKS_TAG_ALGORITHM,
6. value: huks.HuksKeyAlg.HUKS_ALG_ECC
7. },
8. {
9. tag: huks.HuksTag.HUKS_TAG_KEY_SIZE,
10. value: huks.HuksKeySize.HUKS_ECC_KEY_SIZE_256
11. },
12. {
13. tag: huks.HuksTag.HUKS_TAG_PURPOSE,
14. value:
15. huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_SIGN |
16. huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_VERIFY
17. },
18. {
19. tag: huks.HuksTag.HUKS_TAG_BLOCK_MODE,
20. value: huks.HuksCipherMode.HUKS_MODE_CBC
21. },
22. {
23. tag: huks.HuksTag.HUKS_TAG_DIGEST,
24. value: huks.HuksKeyDigest.HUKS_DIGEST_SHA256
25. },
26. {
27. tag: huks.HuksTag.HUKS_TAG_PADDING,
28. value: huks.HuksKeyPadding.HUKS_PADDING_PKCS7
29. }
30. ];
31. let options: huks.HuksOptions = {
32. properties: properties
33. };
34. huks.generateKeyItem(keyAlias, options);
```

## 反例

```
1. import {huks} from '@kit.UniversalKeystoreKit';
2. let keyAlias: string = 'keyAlias';
3. let properties: Array<huks.HuksParam> = [
4. {
5. tag: huks.HuksTag.HUKS_TAG_ALGORITHM,
6. value: huks.HuksKeyAlg.HUKS_ALG_ECC
7. },
8. {
9. tag: huks.HuksTag.HUKS_TAG_KEY_SIZE,
10. value: huks.HuksKeySize.HUKS_ECC_KEY_SIZE_256
11. },
12. {
13. tag: huks.HuksTag.HUKS_TAG_PURPOSE,
14. value:
15. huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_SIGN |
16. huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_VERIFY
17. },
18. {
19. tag: huks.HuksTag.HUKS_TAG_BLOCK_MODE,
20. value: huks.HuksCipherMode.HUKS_MODE_ECB
21. },
22. {
23. tag: huks.HuksTag.HUKS_TAG_DIGEST,
24. value: huks.HuksKeyDigest.HUKS_DIGEST_SHA1
25. },
26. {
27. tag: huks.HuksTag.HUKS_TAG_PADDING,
28. value: huks.HuksKeyPadding.HUKS_PADDING_NONE
29. }
30. ];
31. let options: huks.HuksOptions = {
32. properties: properties
33. };
34. huks.generateKeyItem(keyAlias, options);
```

## 规则集

```
1. plugin:@security/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](<../../../Code Linter代码检查/ide-code-linter.md>)。
