---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/huks-query-authentication-status-ndk
title: 查询认证状态(C/C++)
breadcrumb: 指南 > 系统 > 安全 > Universal Keystore Kit（密钥管理服务） > 外部密钥管理扩展 > UkeyPIN码认证管理 > 查询认证状态(C/C++)
category: harmonyos-guides
scraped_at: 2026-06-01T11:18:53+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:1352ccdee3bdf9c2014551369a098a4fc711a9660715b8918a8ae5a06f4b88d6
---
从API 22开始，huksExternalCrypto提供PIN码认证状态查询功能接口。应用可以通过该接口查询PIN码是否认证通过。具体的场景介绍及规格，请参考[Ukey PIN码认证介绍及规格](<../Ukey PIN码认证介绍及规格/huks-ukey-pin-authentication-management-overview.md>)。

## 在CMake脚本中链接相关动态库

```
1. target_link_libraries(entry PUBLIC libhuks_ndk.z.so libhuks_external_crypto.z.so)
```

## 开发步骤

1. 通过证书管理系统能力提供的[证书选择接口](<../../../../../../../harmonyos-references/安全/Device Certificate Kit（设备证书服务）/ArkTS API/@ohos.security.certManagerDialog (证书管理对话框模块)/js-apis-certmanagerdialog.md#certificatemanagerdialogopenauthorizedialog22>)获取[keyUri](<../../../../../../../harmonyos-references/安全/Device Certificate Kit（设备证书服务）/ArkTS API/@ohos.security.certManagerDialog (证书管理对话框模块)/js-apis-certmanagerdialog.md#certreference22>)，并将其作为resourceId。
2. 调用[OH\_Huks\_InitExternalCryptoParamSet](<../../../../../../../harmonyos-references/Universal Keystore Kit（密钥管理服务）/C API/头文件/native_huks_external_crypto_api.h/capi-native-huks-external-crypto-api-h.md#oh_huks_initexternalcryptoparamset>)指定参数配置。
3. 调用[OH\_Huks\_GetUkeyPinAuthState](<../../../../../../../harmonyos-references/Universal Keystore Kit（密钥管理服务）/C API/头文件/native_huks_external_crypto_api.h/capi-native-huks-external-crypto-api-h.md#oh_huks_getukeypinauthstate>)获取PIN码认证状态。

## 开发案例

```
1. #include "huks/native_huks_external_crypto_api.h"
2. #include "huks/native_huks_param.h"
3. #include "napi/native_api.h"
4. #include <string.h>

6. OH_Huks_Result InitParamSet(
7. struct OH_Huks_ExternalCryptoParamSet **paramSet,
8. const struct OH_Huks_ExternalCryptoParam *params,
9. uint32_t paramCount)
10. {
11. OH_Huks_Result ret = OH_Huks_InitExternalCryptoParamSet(paramSet);
12. if (ret.errorCode != OH_HUKS_SUCCESS) {
13. return ret;
14. }
15. ret = OH_Huks_AddExternalCryptoParams(*paramSet, params, paramCount);
16. if (ret.errorCode != OH_HUKS_SUCCESS) {
17. OH_Huks_FreeExternalCryptoParamSet(paramSet);
18. return ret;
19. }
20. ret = OH_Huks_BuildExternalCryptoParamSet(paramSet);
21. if (ret.errorCode != OH_HUKS_SUCCESS) {
22. OH_Huks_FreeExternalCryptoParamSet(paramSet);
23. return ret;
24. }
25. return ret;
26. }

28. static const char *resourceId = "{\"providerName\":\"testProviderName\",\"abilityName\":\"CryptoExtension\",\"bundleName\":\"com.example.cryptoapplication\",\"index\":{\"key\":\"testKey\"}}";

30. static struct OH_Huks_ExternalCryptoParam g_getPinStateParamsTest[] = {};

32. static napi_value GetUkeyPinAuthState(napi_env env, napi_callback_info info)
33. {
34. struct OH_Huks_Blob g_resourceId = {
35. (uint32_t)strlen(resourceId),
36. (uint8_t *)resourceId
37. };
38. struct OH_Huks_ExternalCryptoParamSet *pinStateParamSet = nullptr;
39. OH_Huks_ExternalPinAuthState authState = OH_HUKS_EXT_CRYPTO_PIN_NO_AUTH;
40. OH_Huks_Result ohResult;
41. do {
42. ohResult = InitParamSet(&pinStateParamSet, g_getPinStateParamsTest,
43. sizeof(g_getPinStateParamsTest) / sizeof(OH_Huks_ExternalCryptoParam));
44. if (ohResult.errorCode != OH_HUKS_SUCCESS) {
45. break;
46. }
47. ohResult = OH_Huks_GetUkeyPinAuthState(&g_resourceId, pinStateParamSet, &authState);
48. if (ohResult.errorCode != OH_HUKS_SUCCESS) {
49. break;
50. }
51. } while (0);
52. OH_Huks_FreeExternalCryptoParamSet(&pinStateParamSet);

54. napi_value ret;
55. napi_create_int32(env, ohResult.errorCode, &ret);
56. return ret;
57. }
```
