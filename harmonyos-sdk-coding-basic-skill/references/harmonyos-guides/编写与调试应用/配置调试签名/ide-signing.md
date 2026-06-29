---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-signing
title: 配置调试签名
breadcrumb: 指南 > 编写与调试应用 > 配置调试签名
category: harmonyos-guides
scraped_at: 2026-06-11T15:28:31+08:00
doc_updated_at: 2026-06-10
content_hash: sha256:a62159e7e6cd84d918ecb15a796217a6ae4deb4f58320dee5dea273326e7fe98
---
针对开发调试场景，DevEco Studio为开发者提供了[自动签名](ide-signing.md#section18815157237)方案，帮助开发者高效进行调试。此外，也可以选择[手动签名](ide-signing.md#section297715173233)方式生成调试签名。

## 使用场景说明

* 自动签名仅用于调试场景，方便开发者进行应用调试。部分调试场景下必须使用手动签名：
  1. 当需要进行跨设备调试、跨应用交互调试、断网情况下调试或者多用户共同开发且需要共享密钥时，必须使用[手动签名](ide-signing.md#section297715173233)。
  2. 如果开发过程中使用到需要审批的权限时，例如：
     1. 使用部分不支持自动签名的[受限开放权限](../../系统/安全/程序访问控制/应用权限管控/应用权限列表/受限开放权限/restricted-permissions.md)时，必须使用[手动签名](ide-signing.md#section297715173233)。支持自动签名的ACL权限清单请参见[自动签名支持的ACL权限](ide-signing.md#section5301916183411)。
     2. 需要华为业务方审核的权限时（例如华为账号一键登录等），必须使用手动签名。
  3. 若kit需要配置指纹，建议使用手动签名。
* 发布场景必须使用手动签名。

## 自动签名

DevEco Studio 6.0.0 Beta3及之前版本，自动签名未关联注册的应用。

从DevEco Studio 6.0.0 Beta5版本开始，自动签名新增关联注册应用的方式，签名操作界面新增“**Associate with registered application**”选项。

* 关联注册应用的自动签名：与应用市场（AppGallery Connect，简称AGC）的应用绑定，可在DevEco Studio开通[开放能力](https://developer.huawei.com/consumer/cn/doc/app/agc-help-create-app-0000002247955506#section1817619495251)。
* 未关联注册应用的自动签名：未与应用市场的应用绑定，不支持在DevEco Studio开通开放能力。

### 约束与限制

* 从DevEco Studio 6.1.1 Beta1版本开始，关联注册应用的自动签名支持在所有国家/地区使用。
* 使用自动签名前，请确保本地系统时间与北京时间（UTC/GMT+08:00）保持一致。如果不一致，将导致签名失败。

### 关联注册应用

**操作步骤**

1. 连接真机设备或模拟器，具体请参考[使用本地真机运行应用/元服务](../使用本地真机运行应用/ide-run-device.md)或[使用模拟器运行应用/元服务](../使用模拟器运行应用/ide-run-emulator.md)，真机连接成功后如下图所示：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e1/v3/Ul6Gugs7SoOkZzQaWbx76g/zh-cn_image_0000002602186279.png?HW-CC-KV=V1&HW-CC-Date=20260611T072508Z&HW-CC-Expire=86400&HW-CC-Sign=B9D88A306774CC1F444ED724D72612ACA06B63E1C1824A02B4CD25ADFBDA6088)

   说明

   如果同时连接多个设备，则使用自动化签名时，会同时将这多个设备的信息写到证书文件中。
2. 进入**File > Project Structure... > Project > Signing Configs**界面，勾选“**Associate with registered application**”。如果未登录，请先点击**Sign In**进行登录。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a6/v3/sGrfnTncTOqs4-og5cBnlg/zh-cn_image_0000002602186289.png?HW-CC-KV=V1&HW-CC-Date=20260611T072508Z&HW-CC-Expire=86400&HW-CC-Sign=2579CB9725D4E1A93C2DCEEBE00539AD187D6FB146CD999C3E1766D2D87A2DF2 "点击放大")

   说明

   * 点击**Team**下拉框，可以切换团队账号。
   * 开始签名后，DevEco Studio根据Bundle name查询该团队在AGC上同包名的应用。若在AGC查询到应用，则进行自动签名；若在AGC未查询到应用或应用冲突，请根据提示信息修改后重新自动签名，具体修改请参考[常见问题](<../../../harmonyos-faqs/DevEco Studio/签名服务/配置调试签名异常/faqs-signature-service-18.md>)。
3. 点击**Enable open capabilities**，在DevEco Studio上开通[开放能力](https://developer.huawei.com/consumer/cn/doc/app/agc-help-create-app-0000002247955506#section1817619495251)。当前支持开通如下四种开放能力：Push Kit（[推送服务](<../../应用服务/Push Kit（推送服务）/Push Kit简介/push-kit-introduction.md>)）、Device status detection（[应用设备状态检测](<../../系统/安全/Device Security Kit（设备安全服务）/应用设备状态检测/devicesecurity-deviceverify-develop.md>)）、Map Kit（[地图服务](<../../应用服务/Map Kit（地图服务）/Map Kit简介/map-introduction.md>)）、Safety Detect（[安全检测服务](<../../系统/安全/Device Security Kit（设备安全服务）/安全检测/devicesecurity-safetydetect-develop.md>)），应用根据需要进行勾选。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7b/v3/vyYA8fudSuibtltlQ48Cmg/zh-cn_image_0000002571546768.png?HW-CC-KV=V1&HW-CC-Date=20260611T072508Z&HW-CC-Expire=86400&HW-CC-Sign=1A874793B25CB08C2CEBBDDF83FC1A196492D2639815650CC3435CE1CDDDFD3D)
4. （可选）在配置文件中添加ACL权限信息，ACL权限清单请参考[自动签名支持的ACL权限](ide-signing.md#section5301916183411)。

   在需要使用权限的模块的module.json5（Stage模型）/config.json（FA模型）文件中添加“requestPermissions”/“reqPermissions”字段，并在字段下添加对应的权限名等信息。以下示例为在Stage模型工程中增加"ohos.permission.ACCESS\_DDK\_USB"权限。

   ```
   1. {
   2. "module": {
   3. ...
   4. "requestPermissions": [{
   5. "name": "ohos.permission.ACCESS_DDK_USB",
   6. }],
   7. ...
   8. }
   9. }
   ```

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/06/v3/u_xX-reIQculhMhprI5YOQ/zh-cn_image_0000002571387112.png?HW-CC-KV=V1&HW-CC-Date=20260611T072508Z&HW-CC-Expire=86400&HW-CC-Sign=CACAE0A9DFBEC6F311998414562ECE04C6EDAB0529FB8935F00327A4CAB41EB6)

   修改配置文件后点击**OK**，若应用已在AGC申请该权限则签名成功；若应用未申请该权限，会导致签名失败，点击Notice弹窗中"**submit a permission request in AppGallery Connect**"或"**Submit**"，跳转至AGC申请权限，然后再返回DevEco Studio界面重新签名。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cf/v3/RgSd5ifyTPuukG45c-QRIg/zh-cn_image_0000002602066241.png?HW-CC-KV=V1&HW-CC-Date=20260611T072508Z&HW-CC-Expire=86400&HW-CC-Sign=D3D0BB294C1CBAF75EF78930FCC5BB1519D186D8D6B56D21D2DAFC7C54CF5C4F "点击放大")

   说明

   * 申请ACL前注意事项：
     + 在申请ACL权限前，请审视是否符合[受限权限的使用场景](../../系统/安全/程序访问控制/应用权限管控/应用权限列表/受限开放权限/restricted-permissions.md)。当前仅少量符合特殊场景的应用可在通过审批后，使用受限权限。申请方式请见[申请使用受限权限](../../系统/安全/程序访问控制/应用权限管控/申请应用权限/申请受限权限/declare-permissions-in-acl.md)。
     + 涉及受限权限的应用，在上架时，应用市场（AGC）将根据应用的使用场景审核是否可以使用对应的受限权限。如不符合，应用的上架申请将被驳回，审核方式请见[发布HarmonyOS应用](https://developer.huawei.com/consumer/cn/doc/app/agc-help-release-app-0000002271695230)。
   * 申请ACL后Profile证书说明：
     + 在ACL权限申请审批完成前，可获得一个有效期较短的临时Profile证书，使应用完成签名。临时证书到期后，若申请仍未审批通过，签名时需再次申请和再次获取临时证书。
     + 在ACL权限申请审批完成后，可获取一个有效期较长的正式Profile证书。
5. 签名完成后，在本地生成密钥（.p12）、证书请求文件（.csr）、数字证书（.cer）及Profile文件（.p7b）。将鼠标悬停在Provisioning Profile: DevEco Managed Profile后![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8c/v3/n7X0p1OZR5KZ7VBGYneXpQ/zh-cn_image_0000002602186307.png?HW-CC-KV=V1&HW-CC-Date=20260611T072508Z&HW-CC-Expire=86400&HW-CC-Sign=F8D882608330CEFE3D05B190C4AA619940F0E79C2B4B6419C34D2899B5A541FC)，可查看证书有效期、包名（bundle name）、ACL权限（acl）、开放能力（capability）等信息；或进入工程级build-profile.json5文件，在“signingConfigs”下可查看到配置成功的签名信息。

### 未关联注册应用

**HarmonyOS工程****按以下步骤操作：**

1. 连接真机设备或模拟器，具体请参考[使用本地真机运行应用/元服务](../使用本地真机运行应用/ide-run-device.md)或[使用模拟器运行应用/元服务](../使用模拟器运行应用/ide-run-emulator.md)，真机连接成功后如下图所示：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8f/v3/3PdnACIyRoGRsKXWeCTRLg/zh-cn_image_0000002571387126.png?HW-CC-KV=V1&HW-CC-Date=20260611T072508Z&HW-CC-Expire=86400&HW-CC-Sign=537B31EDD33DE92A530C9DD7898607A37E6DE796B14D0C0EEF148FBFC45F711E)

   说明

   如果同时连接多个设备，则使用自动化签名时，会同时将这多个设备的信息写到证书文件中。
2. 进入**File > Project Structure... > Project > Signing Configs**界面，勾选“**Automatically generate signature**”即可完成签名。如果未登录，请先单击**Sign In**进行登录，然后自动完成签名。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/47/v3/1B3Z6_iDQh697hSmliXdtQ/zh-cn_image_0000002571387138.png?HW-CC-KV=V1&HW-CC-Date=20260611T072508Z&HW-CC-Expire=86400&HW-CC-Sign=3C83954198AA2A737F10D8EA2FB4CCD1DFB26635BD6DCD382F24225B9EAEDA07 "点击放大")
3. （可选）在配置文件中添加ACL权限信息，ACL权限清单请参考[自动签名支持的ACL权限](ide-signing.md#section5301916183411)。修改配置文件后，点击**Ok。**

   在需要使用权限的模块的module.json5（Stage模型）/config.json（FA模型）文件中添加“requestPermissions”/“reqPermissions”字段，并在字段下添加对应的权限名等信息，以在Stage模型工程中增加"ohos.permission.ACCESS\_DDK\_USB"权限为例。

   ```
   1. {
   2. "module": {
   3. ...
   4. "requestPermissions": [{
   5. "name": "ohos.permission.ACCESS_DDK_USB",
   6. }],
   7. ...
   8. }
   9. }
   ```

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5a/v3/5SuiZ99-RiSh31VgDrFd9g/zh-cn_image_0000002571387110.png?HW-CC-KV=V1&HW-CC-Date=20260611T072508Z&HW-CC-Expire=86400&HW-CC-Sign=037221AC3F836C6C157FF6C460480F327AE3E9D1D918F7E2BD251BD3CF7DE62B)

   说明

   * 在调试签名时，不会强校验配置文件中添加的ACL权限。
   * 涉及受限权限的应用，上架时，应用市场（AGC）将根据应用的使用场景审核是否可以使用对应的受限权限，如不符合，应用的上架申请将被驳回。在配置ACL权限前，请审视是否符合[受限权限的使用场景](../../系统/安全/程序访问控制/应用权限管控/应用权限列表/受限开放权限/restricted-permissions.md)。当前仅少量符合特殊场景的应用可在通过审批后，使用受限权限，申请方式请见[申请使用受限权限](../../系统/安全/程序访问控制/应用权限管控/申请应用权限/申请受限权限/declare-permissions-in-acl.md)。
4. 签名完成后，在本地生成密钥（.p12）、证书请求文件（.csr）、数字证书（.cer）及Profile文件（.p7b）。将鼠标悬停在Provisioning Profile: DevEco Managed Profile后![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/44/v3/XZYsSeFITEi0VhllwIINug/zh-cn_image_0000002571546754.png?HW-CC-KV=V1&HW-CC-Date=20260611T072508Z&HW-CC-Expire=86400&HW-CC-Sign=FA4269965E8D0BF19A4D44261C30A510E7B71B177959E91F2EA80A907695F727)，可查看证书有效期、包名（bundle name）、ACL权限（acl）、开放能力（capability）等信息；或进入工程级build-profile.json5文件，在“signingConfigs”下可查看到配置成功的签名信息。

**OpenHarmony工程****按以下步骤操作：**

1. 连接真机设备或模拟器，具体请参考[使用本地真机运行应用/元服务](../使用本地真机运行应用/ide-run-device.md)或[使用模拟器运行应用/元服务](../使用模拟器运行应用/ide-run-emulator.md)，真机连接成功后如下图所示：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/91/v3/0s_CA9C6SMeQRV24rC84KQ/zh-cn_image_0000002571387132.png?HW-CC-KV=V1&HW-CC-Date=20260611T072508Z&HW-CC-Expire=86400&HW-CC-Sign=DEB3DF3AC6DD4AEDEB3A742E3EB54BFCBE050B9FD1F796D1D851293888FCCD6B)
2. 进入**File > Project Structure... > Project > Signing Configs**界面。仅勾选“**Automatically generate signature**”时，生成OpenHarmony签名；勾选“**Support HarmonyOS**”和“**Automatically generate signature**”时，生成HarmonyOS签名。如果未登录，请先单击**Sign In**进行登录。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/07/v3/qvvDUioHQgKMJfA_RjhsOA/zh-cn_image_0000002602186287.png?HW-CC-KV=V1&HW-CC-Date=20260611T072508Z&HW-CC-Expire=86400&HW-CC-Sign=A2413B1395E6EFB8BD42897FFB6EEB072A003063F7EF12E02B7669122C17963C)

   签名完成后，如下图所示。在本地生成密钥（.p12）、证书请求文件（.csr）、数字证书（.cer）及Profile文件（.p7b），数字证书在AGCt网站的“证书、APP ID和Profile”页签中可以查看。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/84/v3/P74NFuWATGqDR2VLDCRcsQ/zh-cn_image_0000002571387140.png?HW-CC-KV=V1&HW-CC-Date=20260611T072508Z&HW-CC-Expire=86400&HW-CC-Sign=8526BECE3222A2CD1B22B8CAFE0D4F00F8A6439BF69B2B9596E52C2166BDCB37)

   说明

   * OpenHarmony工程签名时，推荐使用HarmonyOS签名。因为OpenHarmony签名是Release签名，Release签名的应用不支持调试和打印debug日志等。此外，OpenHarmony签名可能会影响应用运行。
   * 如果同时连接多个设备，则使用自动化签名时，会同时将这多个设备的信息写到证书文件中。

## 手动签名

HarmonyOS应用/元服务通过数字证书（.cer文件）和Profile文件（.p7b文件）来保证应用/元服务的完整性。在申请调试数字证书和调试Profile文件前，需要通过DevEco Studio生成密钥（存储在格式为.p12的密钥库文件中）和证书请求文件（.csr文件）

**基本概念**

* **密钥**：格式为.p12，包含非对称加密中使用的公钥和私钥，存储在密钥库文件中，公钥和私钥用于数字签名和验证。
* **证书请求文件**：格式为.csr，全称为Certificate Signing Request，包含密钥对中的公钥和通用名称、组织名称、组织单位等信息，用于向AppGallery Connect申请数字证书。
* **数字证书**：格式为.cer，由华为AppGallery Connect颁发。
* **Profile文件**：格式为.p7b，包含HarmonyOS应用/元服务的包名、数字证书信息、描述应用/元服务允许申请的证书权限列表，以及允许应用/元服务调试的设备列表（如果应用/元服务类型为Release类型，则设备列表为空）等内容，每个应用/元服务包中均必须包含一个Profile文件。

从DevEco Studio 6.1.0 Beta2版本开始，手动签名时，生成密钥和证书请求文件的操作界面发生变更。

### 生成密钥和证书请求文件

**DevEco Studio 6.1.0 Beta2及之后版本**

1. 在主菜单栏单击**Build > Generate Key** **and CSR**。
2. 在**Generate Key** **and CSR**界面，可以单击**Select an existing key**选择已有的密钥库文件（存储有密钥的.p12文件），若没有密钥库文件则进行填写。下面以新创建密钥库文件为例进行说明。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/af/v3/PvcG2iOpTBCn9P3-tP9ULw/zh-cn_image_0000002602066239.png?HW-CC-KV=V1&HW-CC-Date=20260611T072508Z&HW-CC-Expire=86400&HW-CC-Sign=A4C2F7CA5A7805992CDE503BD40E8A3D233F141913BB97204CC16963F955295E)
3. 在**Generate Key**窗口，填写密钥库信息后，点击**Next**。
   * **Keystore Name**：填写p12文件名称，仅允许包含字母、数字、下划线（\_）、中划线（-）、句号（.）。
   * **Select file save path**：设置密钥库文件存储路径。
   * **Key store password**：设置密钥库密码，必须由大写字母、小写字母、数字和特殊符号中的两种以上字符的组合，长度至少为8位。请记住该密码，后续签名配置需要使用。
   * **Confirm password**：再次输入密钥库密码。
   * **Alias**：密钥别名。请记住该别名，后续签名配置需要使用。
   * **Advance Setting**：密钥库文件的高级设置，选填。
     + **Validity(years)：**选填，证书有效期，建议设置为25年及以上，覆盖应用/元服务的完整生命周期。
     + **First and last name：**选填，通用名称，可填写应用名称或开发者姓名等。
     + **Organizational unit**：选填，组织单位，可填写部门名称或个人开发等。
     + **Organization：**选填，组织名称，可填写公司全称或开发者姓名等。
     + **City or locality：**选填，城市或地区。
     + **State or province：**选填，州或省。
     + **Country code(XX)：**选填，[国家码](https://developer.huawei.com/consumer/cn/doc/app/agc-help-connect-api-appendix-countrycode-0000002236201362)。

     说明

     First and last name、Organizational unit、Organization、City or locality、State or province填写要求小于64个字符，不可使用双引号（"）、斜杠（\）、反引号（`）。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/83/v3/zFdEcvEaTaC0BkQBLFwgHQ/zh-cn_image_0000002571546778.png?HW-CC-KV=V1&HW-CC-Date=20260611T072508Z&HW-CC-Expire=86400&HW-CC-Sign=2423B74D6E7158BC2FEDB30F78D4CB38EBB928FDEFA67CB2C66666F46C9831DD)
4. 在**Generate** **Certificate Request File (CSR)**窗口，设置CSR文件名和CSR文件存储路径后，点击**Finish**。
   * **CSR File Name**：填写CSR文件名称，仅允许包含字母、数字、下划线（\_）、中划线（-）、句号（.）。
   * **Select file save path**：设置CSR文件存储路径。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/99/v3/C2MeNjGlQoCmdo-p2KaS7g/zh-cn_image_0000002571387120.png?HW-CC-KV=V1&HW-CC-Date=20260611T072508Z&HW-CC-Expire=86400&HW-CC-Sign=9A973F2307F16450895935CAB4D9A7AC0EB76F60F24DDB1F320BEBECCB83E14C)
5. 创建CSR文件成功，可以在存储路径下获取生成的密钥库文件（.p12）、证书请求文件（.csr）。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/36/v3/rVYCOgpUQQyvFWe8Z3tpbw/zh-cn_image_0000002571387124.png?HW-CC-KV=V1&HW-CC-Date=20260611T072508Z&HW-CC-Expire=86400&HW-CC-Sign=98DF40D55741AE4653112EA9B497F19FE61A5C756988573C2A8D06FA7B9EDFB4)

**DevEco Studio 6.1.0 Beta2之前版本**

1. 在主菜单栏单击**Build > Generate Key** **and CSR**。

   说明

   如果本地已有对应的密钥，无需新生成密钥，可以在**Generate Key**界面中单击下方的Skip跳过密钥生成过程，直接使用已有密钥生成证书请求文件。
2. 在**Key store file**中，可以单击**Choose Existing**选择已有的密钥库文件（存储有密钥的.p12文件）；如果没有密钥库文件，单击**New**进行创建。下面以新创建密钥库文件为例进行说明。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c2/v3/1Vz4op2FTJ2qOM-48d4m8g/zh-cn_image_0000002602066249.png?HW-CC-KV=V1&HW-CC-Date=20260611T072508Z&HW-CC-Expire=86400&HW-CC-Sign=FEDBB4FDBA29F73FDB267D71B6C4D847F302D698215E1DCDE5EB2BD9BF3400EB)
3. 在**Create Key Store**窗口，填写密钥库信息后，单击**OK**。
   * **Key store file**：设置密钥库文件存储路径，并填写p12文件名。
   * **Password**：设置密钥库密码，必须由大写字母、小写字母、数字和特殊符号中的两种以上字符的组合，长度至少为8位。请记住该密码，后续签名配置需要使用。
   * **Confirm password**：再次输入密钥库密码。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c9/v3/6_r4Eu94RBmlLzZPzS0iYg/zh-cn_image_0000002602186305.png?HW-CC-KV=V1&HW-CC-Date=20260611T072508Z&HW-CC-Expire=86400&HW-CC-Sign=B0379203E287D1988146B276AE57AB8074F8128A5A7E005AE7160B9B9D071970)
4. 在**Generate Key** **and CSR**界面，继续填写密钥信息后，单击**Next**。
   * **Alias**：必填，别名，用于标识密钥名称。请记住该别名，后续签名配置需要使用。
   * **Password**：必填，密码，与密钥库密码保持一致，无需手动输入。
   * **Validity(years)：**选填，证书有效期，建议设置为25年及以上，覆盖应用/元服务的完整生命周期。
   * **First and last name：**选填，通用名称，可填写应用名称或开发者姓名等。
   * **Organizational unit**：选填，组织单位，可填写部门名称或个人开发等。
   * **Organization：**选填，组织名称，可填写公司全称或开发者姓名等。
   * **City or locality：**选填，城市或地区。
   * **State or province：**选填，州或省。
   * **Country code(XX)：**选填，[国家码](https://developer.huawei.com/consumer/cn/doc/app/agc-help-connect-api-appendix-countrycode-0000002236201362)。

   说明

   First and last name、Organizational unit、Organization、City or locality、State or province要求：字符长度为（0，64），且不可使用双引号（"）、斜杠（\）、反引号（`）。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0d/v3/Y_DbMcIjRBi2hSbZdGDqAg/zh-cn_image_0000002571387128.png?HW-CC-KV=V1&HW-CC-Date=20260611T072508Z&HW-CC-Expire=86400&HW-CC-Sign=20C84C6B2094ED7A8FCC13A5EB506E40DA2948991EE967EC66D206CA0A396612)
5. 在**Generate Key** **and CSR**界面，设置CSR文件存储路径和CSR文件名。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/21/v3/hVMqRwAUSuaaC-b9gvC4dw/zh-cn_image_0000002602066243.png?HW-CC-KV=V1&HW-CC-Date=20260611T072508Z&HW-CC-Expire=86400&HW-CC-Sign=EFE8A740F2F26F621E5218981874B00E34CB57497F1D0AF4540CB0ED43755FD1)
6. 单击**Finish**，创建CSR文件成功，可以在存储路径下获取生成的密钥库文件（.p12）、证书请求文件（.csr）和material文件夹（存放密码加密材料等）。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/74/v3/v-OlzaHpT-KuFjXywMqIfA/zh-cn_image_0000002571387130.png?HW-CC-KV=V1&HW-CC-Date=20260611T072508Z&HW-CC-Expire=86400&HW-CC-Sign=5B2677ED4C5C2DC903D86235B9395DE2D1025473542A4D34442B05DEF1C271C8)

### 申请调试证书

在AGC中申请和下载调试证书，具体请参考[申请调试证书](https://developer.huawei.com/consumer/cn/doc/app/agc-help-debug-cert-0000002283256797)。

说明

如您未在AGC中注册该应用，申请前需要在AGC中注册，具体请参考[创建HarmonyOS应用](https://developer.huawei.com/consumer/cn/doc/app/agc-help-create-app-0000002247955506)。

### 申请调试Profile文件和添加权限信息

1. （可选）如需使用ACL权限，在AGC中[申请ACL权限](https://developer.huawei.com/consumer/cn/doc/app/agc-help-apply-acl-0000002394212138)。同时，在DevEco Studio配置文件中添加权限信息。

   说明

   * ACL权限申请仅支持中国境内（香港特别行政区、澳门特别行政区、中国台湾除外）。
   * 若应用因特殊场景要求使用受限开放权限，请务必在此步骤进行申请，否则应用将在审核时被驳回。受限开放权限可申请的特殊场景请参考[受限开放权限](../../系统/安全/程序访问控制/应用权限管控/应用权限列表/受限开放权限/restricted-permissions.md)。
   * 确保应用申请受限开放权限时提供的场景和功能信息准确。如果应用内使用的受限开放权限超出您申请的范围，或申请权限后使用的功能和场景超出可使用的范围，将影响应用上架。

   在需要使用权限的模块的module.json5（Stage模型）/config.json（FA模型）文件中添加“requestPermissions”/“reqPermissions”字段，并在字段下添加对应的权限名等信息，以在Stage模型工程中增加"ohos.permission.ACCESS\_DDK\_USB"权限为例。

   ```
   1. {
   2. "module": {
   3. ...
   4. "requestPermissions": [{
   5. "name": "ohos.permission.ACCESS_DDK_USB",
   6. }],
   7. ...
   8. }
   9. }
   ```

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/34/v3/vJG4b56WRnGmqpa99qbQXw/zh-cn_image_0000002602066237.png?HW-CC-KV=V1&HW-CC-Date=20260611T072508Z&HW-CC-Expire=86400&HW-CC-Sign=15D88C827974527FB11DC58C207F60E430587B66B984AC476CA64D890E6A2B4C)
2. 在AGC中申请和下载Profile文件，具体请参考[申请调试Profile](https://developer.huawei.com/consumer/cn/doc/app/agc-help-debug-profile-0000002248181278)。

### 配置签名信息

1. 连接真机设备，确保[DevEco Studio与真机设备已连接](../使用本地真机运行应用/ide-run-device.md)。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e9/v3/2HhRYtn_T7yFFyheF3IjXg/zh-cn_image_0000002602186285.png?HW-CC-KV=V1&HW-CC-Date=20260611T072508Z&HW-CC-Expire=86400&HW-CC-Sign=C9CFC4AA680D0B1834D0444C222D13D90232CB0A25128E94036FC0F46E659513)
2. 在**File >** **Project Structure >** **Project > Signing Configs**窗口中，取消勾选“Automatically generate signature”和“Associate with registered application”，分别配置密钥(.p12文件)、Profile(.p7b文件)和数字证书(.cer文件)的路径等信息，配置完毕后点击**Apply**。
   * **Store file**：选择密钥库文件，文件后缀为.p12，该文件为[生成密钥和证书请求文件](ide-signing.md#section462703710326)中生成的.p12文件。
   * **Store password**：输入密钥库密码，该密码与[生成密钥和证书请求文件](ide-signing.md#section462703710326)中填写的密钥库密码保持一致。
   * **Key alias**：输入密钥的别名信息，与[生成密钥和证书请求文件](ide-signing.md#section462703710326)中填写的别名保持一致。
   * **Key password**：输入密钥的密码，与[生成密钥和证书请求文件](ide-signing.md#section462703710326)中填写的**Store Password**保持一致。
   * **Sign alg**：签名算法，固定为SHA256withECDSA。
   * **Profile file**：选择[申请调试Profile文件和添加权限信息](ide-signing.md#section89479413571)中生成的Profile文件，文件后缀为.p7b。
   * **Certpath file**：选择[申请调试证书](ide-signing.md#section081822416419)中生成的数字证书文件，文件后缀为.cer。

   说明

   * Store file，Profile file，Certpath file三个字段支持配置相对路径，以项目根目录为起点，配置文件所在位置的路径名称。
   * 密钥库文件、密钥库密码、密钥别名、密钥密码、Profile文件、数字证书文件必须配套使用，否则会导致签名失败。若失败请根据报错信息进行修改，再进行签名。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/59/v3/Jad2dAfNTLu7-3fm5iOWuA/zh-cn_image_0000002602066255.png?HW-CC-KV=V1&HW-CC-Date=20260611T072508Z&HW-CC-Expire=86400&HW-CC-Sign=9AC5FB6B731AB8BC5124E9BF3AD3FE57E8468CE1B676DCDA7339C6433475B073 "点击放大")

   配置完成后，将鼠标悬停在**Provisioning Profile: DevEco Manage Profile**后![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5f/v3/D2yuzU_jS3K73mOBCDPYEQ/zh-cn_image_0000002571546772.png?HW-CC-KV=V1&HW-CC-Date=20260611T072508Z&HW-CC-Expire=86400&HW-CC-Sign=033304D38360A692B52488B0B7E0D64EE92F21E140F262B589C9F134D968E742)，可查看证书有效期、包名（bundle name）、企业名称（common name）、ACL权限（acl）、开放能力（capability）相关信息；或者进入工程级build-profile.json5文件，在“signingConfigs”下可查看到配置成功的签名信息。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/81/v3/tvYKlRFnRJquV8u_lE_xLQ/zh-cn_image_0000002602066229.png?HW-CC-KV=V1&HW-CC-Date=20260611T072508Z&HW-CC-Expire=86400&HW-CC-Sign=8797819FE9AD4FC38FFA51515F0D8E0AF0CA1594C3A465FDDD75123FC78694BA "点击放大")
3. 进入工程级build-profile.json5文件，在“signingConfigs”下可查看到配置成功的签名信息，点击右上角的“Run”按钮运行应用/元服务。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1e/v3/m7okYDO6RV6LU8cNYLv2Xg/zh-cn_image_0000002571387122.png?HW-CC-KV=V1&HW-CC-Date=20260611T072508Z&HW-CC-Expire=86400&HW-CC-Sign=A9E032CF84DFA9CE5B2FA99338B644D6AA0011C7CFD8102E8B736C28CEF96EAA)

## 附录

### 自动签名支持的ACL权限

自动签名当前支持申请的ACL权限的清单如下所示。执行[操作步骤](ide-signing.md#section18815157237)后，DevEco Studio将校验当前配置的ACL权限是否在以下列表中，然后通过应用市场（AGC）申请对应的Profile文件，用于签名打包，从而避免繁琐的手动签名步骤。

从DevEco Studio 6.1.0 Beta2版本开始，自动签名支持配置的ACL权限具体参考[受限开放权限](../../系统/安全/程序访问控制/应用权限管控/应用权限列表/受限开放权限/restricted-permissions.md)。

**6.0.2 Beta****1**

新增权限

* ohos.permission.SUBSCRIBE\_NOTIFICATION
* ohos.permission.ACCESS\_USER\_FULL\_DISK
* ohos.permission.CUSTOM\_SCREEN\_RECORDING
* ohos.permission.GET\_IP\_MAC\_INFO

**6.0.1 Release****（6.0.1.260）**

新增权限

* ohos.permission.SET\_SYSTEMSHARE\_APPLAUNCHTRUSTLIST
* ohos.permission.HOOK\_KEY\_EVENT
* ohos.permission.WEB\_NATIVE\_MESSAGING

**6.0.0 Beta3**

新增权限

* ohos.permission.CUSTOMIZE\_SAVE\_BUTTON
* ohos.permission.GET\_ABILITY\_INFO
* ohos.permission.LINKTURBO
* ohos.permission.GET\_WIFI\_LOCAL\_MAC
* ohos.permission.GET\_ETHERNET\_LOCAL\_MAC
* ohos.permission.USE\_FLOAT\_BALL
* ohos.permission.READ\_LOCAL\_DEVICE\_NAME
* ohos.permission.ACCESS\_NET\_TRACE\_INFO
* ohos.permission.KEEP\_BACKGROUND\_RUNNING\_SYSTEM
* ohos.permission.atomicService.MANAGE\_STORAGE
* ohos.permission.MANAGE\_SCREEN\_TIME\_GUARD

**5.1.0 Release**

新增权限

* ohos.permission.ACCESS\_DDK\_USB\_SERIAL
* ohos.permission.ACCESS\_DDK\_SCSI\_PERIPHERAL
* ohos.permission.USE\_FRAUD\_APP\_PICKER

**5.0.5 Release**

新增权限

* ohos.permission.kernel.DISABLE\_GOTPLT\_RO\_PROTECTION
* ohos.permission.MANAGE\_APN\_SETTING

**5.0.3 Release**

新增权限

* ohos.permission.READ\_WRITE\_USB\_DEV
* ohos.permission.USE\_FRAUD\_CALL\_LOG\_PICKER
* ohos.permission.USE\_FRAUD\_MESSAGES\_PICKER
* ohos.permission.ACCESS\_DISK\_PHY\_INFO
* ohos.permission.SET\_PAC\_URL
* ohos.permission.PERSONAL\_MANAGE\_RESTRICTIONS
* ohos.permission.START\_PROVISIONING\_MESSAGE
* ohos.permission.PRELOAD\_FILE
* ohos.permission.kernel.ALLOW\_WRITABLE\_CODE\_MEMORY
* ohos.permission.kernel.DISABLE\_CODE\_MEMORY\_PROTECTION
* ohos.permission.kernel.ALLOW\_EXECUTABLE\_FORT\_MEMORY
* ohos.permission.GET\_WIFI\_PEERS\_MAC
* ohos.permission.READ\_WRITE\_DESKTOP\_DIRECTORY
* ohos.permission.MANAGE\_PASTEBOARD\_APP\_SHARE\_OPTION
* ohos.permission.MANAGE\_UDMF\_APP\_SHARE\_OPTION
* ohos.permission.READ\_WRITE\_USER\_FILE

**5.0.0 Release**

支持权限

* ohos.permission.READ\_CONTACTS
* ohos.permission.WRITE\_CONTACTS
* ohos.permission.READ\_AUDIO
* ohos.permission.WRITE\_AUDIO
* ohos.permission.READ\_IMAGEVIDEO
* ohos.permission.READ\_PASTEBOARD
* ohos.permission.WRITE\_IMAGEVIDEO
* ohos.permission.ACCESS\_DDK\_USB
* ohos.permission.ACCESS\_DDK\_HID
* ohos.permission.SYSTEM\_FLOAT\_WINDOW
* ohos.permission.FILE\_ACCESS\_PERSIST
* ohos.permission.INPUT\_MONITORING
* ohos.permission.INTERCEPT\_INPUT\_EVENT
* ohos.permission.SHORT\_TERM\_WRITE\_IMAGEVIDEO
