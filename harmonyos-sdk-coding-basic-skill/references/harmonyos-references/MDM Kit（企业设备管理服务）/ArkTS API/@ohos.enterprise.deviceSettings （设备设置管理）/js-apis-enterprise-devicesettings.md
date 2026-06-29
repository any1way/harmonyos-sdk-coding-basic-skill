---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-enterprise-devicesettings
title: @ohos.enterprise.deviceSettings （设备设置管理）
breadcrumb: API参考 > 系统 > 基础功能 > MDM Kit（企业设备管理服务） > ArkTS API > @ohos.enterprise.deviceSettings （设备设置管理）
category: harmonyos-references
scraped_at: 2026-06-11T16:21:11+08:00
doc_updated_at: 2026-05-26
content_hash: sha256:1c80bf4292cb69ce78e6639c816bf14c7117cfd504806ae861130373d8a457ae
---
本模块提供企业设备设置能力，包括设置、获取设备息屏时间等。

说明

本模块首批接口从API version 12开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

本模块接口仅可在Stage模型下使用。

本模块接口仅对设备管理应用开放，且调用接口前需激活设备管理应用，具体请参考[MDM Kit开发指南](<../../../../../harmonyos-guides/系统/基础功能/MDM Kit（企业设备管理服务）/MDM Kit开发指南/mdm-kit-guide.md>)。

## 导入模块

PhonePC/2in1Tablet

```
1. import { deviceSettings } from '@kit.MDMKit';
```

## deviceSettings.setValue

PhonePC/2in1Tablet

setValue(admin: Want, item: string, value: string): void

设置设备策略。

**需要权限：** ohos.permission.ENTERPRISE\_MANAGE\_SETTINGS

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**冲突规则：** [配置](<../../../../../harmonyos-guides/系统/基础功能/MDM Kit（企业设备管理服务）/多应用管控/mdm-kit-multi-mdm.md#规则3配置>)。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| admin | [Want](<../../../../Ability Kit（程序框架服务）/ArkTS API/通用能力的接口(推荐)/@ohos.app.ability.Want (Want)/js-apis-app-ability-want.md>) | 是 | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |
| item | string | 是 | 设备设置策略类型。  - screenOff：设备息屏策略。对于PC/2in1设备，支持设置电池和电源供电下的设备息屏策略。  - dateTime：设置系统时间。  - powerPolicy：设备电源策略。该能力仅支持PC/2in1设备，策略设置之后不刷新设置—电源和电池页面，在手机平板设备设置后不生效。  对于PC/2in1设备，仅支持设置电池供电下的设备电源策略。设置设备超时灭屏时睡眠延迟策略，睡眠动作需要在设置—电源和电池页面显示的睡眠时间之后等待设置的delayTime才会生效。  - eyeComfort：从API version 23开始支持，设置护眼模式开关状态，仅支持全天开启和关闭护眼模式。  - defaultInputMethod：从API version 23开始支持，设置默认输入法。 |
| value | string | 是 | 策略类型值。  当item为screenOff时，value为设备息屏时间（单位：毫秒）。建议value值和设置页面手动操作下拉框中的可选项保持一致。  当item为dateTime时，value为要设置的系统时间（单位：毫秒）。  当item为powerPolicy时，value为JSON字符串，格式：{"powerScene":xx,"powerPolicy":{"powerPolicyAction":xx,"delayTime":xx}}。  powerScene为电源策略场景，可设置参数如下：  - 0：超时灭屏场景。  powerPolicyAction为休眠动作策略场景，可设置参数如下：  - 0：不执行动作。  - 1：自动进入睡眠。  - 2：强制进入睡眠。  - 3：进入休眠，该策略暂不生效。  - 4：关机。  delayTime为延迟时间（单位：毫秒），不支持设置为30000毫秒，其余数值均在允许范围内。  当item为eyeComfort时，value为护眼模式开关状态的字符串。  - on：全天开启护眼模式。  - off：关闭护眼模式。  当item为defaultInputMethod时，value为输入法应用包名字符串。  - 可以通过[getCurrentInputMethod](<../../../../IME Kit（输入法开发服务）/ArkTS API/@ohos.inputMethod (输入法框架)/js-apis-inputmethod.md#inputmethodgetcurrentinputmethod9>)获取当前输入法应用包名。 |

**错误码**：

以下错误码的详细介绍请参见[企业设备管理错误码](../../错误码/企业设备管理错误码/errorcode-enterprisedevicemanager.md)和[通用错误码](../../../../通用错误码/errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```
1. import { deviceSettings } from '@kit.MDMKit';
2. import { Want } from '@kit.AbilityKit';

4. let wantTemp: Want = {
5. // 需根据实际情况进行替换
6. bundleName: 'com.example.myapplication',
7. abilityName: 'EnterpriseAdminAbility'
8. };

10. try {
11. // 需根据实际情况进行替换
12. deviceSettings.setValue(wantTemp, 'screenOff', '3000');
13. console.info(`Succeeded in setting screen off time.`);
14. } catch (err) {
15. console.error(`Failed to set screen off time. Code: ${err.code}, message: ${err.message}`);
16. }
```

## deviceSettings.getValue

PhonePC/2in1Tablet

getValue(admin: Want, item: string): string

获取设备设置策略。

**需要权限：** ohos.permission.ENTERPRISE\_MANAGE\_SETTINGS

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| admin | [Want](<../../../../Ability Kit（程序框架服务）/ArkTS API/通用能力的接口(推荐)/@ohos.app.ability.Want (Want)/js-apis-app-ability-want.md>) | 是 | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |
| item | string | 是 | 设备设置策略类型。  - screenOff：设备息屏策略，对于PC/2in1设备，支持查询电池供电下的设备息屏策略。  - powerPolicy：设备电源策略，仅对PC/2in1设备生效，仅支持查询电池供电下的设备电源策略。  - eyeComfort：从API version 23开始支持，护眼模式开关状态。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 策略类型值。  当item为screenOff时，返回设备息屏时间（单位：毫秒），对于PC/2in1设备，返回设备电池供电下的息屏时间（单位：毫秒）。  当item为powerPolicy时，返回电源策略，对于PC/2in1设备，返回设备电池供电下的电源策略，格式为JSON字符串:{"powerScene":xx,"powerPolicy":{"powerPolicyAction":xx,"delayTime":xx}}。powerScene为电源策略场景；delayTime为延迟时间（单位：毫秒）；powerPolicyAction为休眠策略。  电源策略场景：  - 0：超时场景。  休眠策略：  - 0：不执行动作。  - 1：自动进入睡眠。  - 2：强制进入睡眠。  - 3：进入休眠，该策略暂不生效。  - 4：关机。  当item为eyeComfort时，value为护眼模式开关状态的字符串。  - on：全天开启护眼模式。  - off：关闭护眼模式。  - unknown：其他模式。 |

**错误码**：

以下错误码的详细介绍请参见[企业设备管理错误码](../../错误码/企业设备管理错误码/errorcode-enterprisedevicemanager.md)和[通用错误码](../../../../通用错误码/errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```
1. import { deviceSettings } from '@kit.MDMKit';
2. import { Want } from '@kit.AbilityKit';

4. let wantTemp: Want = {
5. // 需根据实际情况进行替换
6. bundleName: 'com.example.myapplication',
7. abilityName: 'EnterpriseAdminAbility'
8. };

10. try {
11. // 参数需根据实际情况进行替换
12. let result: string = deviceSettings.getValue(wantTemp, 'screenOff');
13. console.info(`Succeeded in getting screen off time, result : ${result}`);
14. } catch (err) {
15. console.error(`Failed to get screen off time. Code: ${err.code}, message: ${err.message}`);
16. }
```

## deviceSettings.setHomeWallpaper20+

PhonePC/2in1Tablet

setHomeWallpaper(admin: Want, fd: number): Promise<void>

设置桌面壁纸，使用Promise异步回调。

**需要权限：** ohos.permission.ENTERPRISE\_SET\_WALLPAPER

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**冲突规则：** [配置](<../../../../../harmonyos-guides/系统/基础功能/MDM Kit（企业设备管理服务）/多应用管控/mdm-kit-multi-mdm.md#规则3配置>)。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| admin | [Want](<../../../../Ability Kit（程序框架服务）/ArkTS API/通用能力的接口(推荐)/@ohos.app.ability.Want (Want)/js-apis-app-ability-want.md>) | 是 | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |
| fd | number | 是 | 需要设置为桌面壁纸图片的文件描述符，可以通过file.fs的[openSync](<../../../../Core File Kit（文件基础服务）/ArkTS API/@ohos.file.fs (文件管理)/js-apis-file-fs.md#fileioopensync>)接口获取应用沙箱目录下的图片文件描述符。壁纸图片大小不能超过100MB。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。当设置桌面壁纸失败后会抛出错误对象。 |

**错误码**：

以下错误码的详细介绍请参见[企业设备管理错误码](../../错误码/企业设备管理错误码/errorcode-enterprisedevicemanager.md)和[通用错误码](../../../../通用错误码/errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 9200012 | Parameter verification failed. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |

**示例：**

```
1. import { deviceSettings } from '@kit.MDMKit';
2. import { common, Want } from '@kit.AbilityKit';
3. import { BusinessError } from '@kit.BasicServicesKit';
4. import { fileIo as fs }  from '@kit.CoreFileKit';

6. let wantTemp: Want = {
7. // 请根据实际情况修改
8. bundleName: 'com.example.myapplication',
9. abilityName: 'EnterpriseAdminAbility'
10. };

12. // 请在组件内获取context，确保this.getUIContext().getHostContext()返回结果为UIAbilityContext
13. const context = this.getUIContext().getHostContext() as common.UIAbilityContext;
14. // 参数根据实际情况进行替换
15. let filename: string = "homewallpaper.jpg";
16. let filePath: string = context.filesDir + '/' + filename;
17. let fd: number = fs.openSync(filePath, fs.OpenMode.READ_WRITE).fd;
18. deviceSettings.setHomeWallpaper(wantTemp, fd).then(() => {
19. console.info('Succeeded in setting home wallpaper');
20. }).catch((err: BusinessError) => {
21. console.error(`Failed to set home wallpaper. Code: ${err.code}, message: ${err.message}`);
22. }).finally(() => {
23. fs.closeSync(fd);
24. });
```

## deviceSettings.setUnlockWallpaper20+

PhonePC/2in1Tablet

setUnlockWallpaper(admin: Want, fd: number): Promise<void>

设置锁屏壁纸，使用Promise异步回调。

**需要权限：** ohos.permission.ENTERPRISE\_SET\_WALLPAPER

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**冲突规则：** [配置](<../../../../../harmonyos-guides/系统/基础功能/MDM Kit（企业设备管理服务）/多应用管控/mdm-kit-multi-mdm.md#规则3配置>)。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| admin | [Want](<../../../../Ability Kit（程序框架服务）/ArkTS API/通用能力的接口(推荐)/@ohos.app.ability.Want (Want)/js-apis-app-ability-want.md>) | 是 | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |
| fd | number | 是 | 需要设置为锁屏壁纸图片的文件描述符，可以通过file.fs的[openSync](<../../../../Core File Kit（文件基础服务）/ArkTS API/@ohos.file.fs (文件管理)/js-apis-file-fs.md#fileioopensync>)接口获取应用沙箱目录下的图片文件描述符。壁纸图片大小不能超过100MB。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。当设置锁屏壁纸失败后会抛出错误对象。 |

**错误码**：

以下错误码的详细介绍请参见[企业设备管理错误码](../../错误码/企业设备管理错误码/errorcode-enterprisedevicemanager.md)和[通用错误码](../../../../通用错误码/errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 9200012 | Parameter verification failed. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |

**示例：**

```
1. import { deviceSettings } from '@kit.MDMKit';
2. import { common, Want } from '@kit.AbilityKit';
3. import { BusinessError } from '@kit.BasicServicesKit';
4. import { fileIo as fs }  from '@kit.CoreFileKit';

6. let wantTemp: Want = {
7. // 需根据实际情况进行替换
8. bundleName: 'com.example.myapplication',
9. abilityName: 'EnterpriseAdminAbility'
10. };

12. // 请在组件内获取context，确保this.getUIContext().getHostContext()返回结果为UIAbilityContext
13. const context = this.getUIContext().getHostContext() as common.UIAbilityContext;
14. // 参数根据实际情况进行替换
15. let filename: string = "lockwallpaper.jpg";
16. let filePath: string = context.filesDir + '/' + filename;
17. let fd: number = fs.openSync(filePath, fs.OpenMode.READ_WRITE).fd;
18. deviceSettings.setUnlockWallpaper(wantTemp, fd).then(() => {
19. console.info('Succeeded in setting lock wallpaper');
20. }).catch((err: BusinessError) => {
21. console.error(`Failed to set lock wallpaper. Code: ${err.code}, message: ${err.message}`);
22. });
```

## deviceSettings.setValueForAccount24+

PhonePC/2in1Tablet

setValueForAccount(admin: Want, item: SettingsItem, accountId: number, value: string): void

设置指定用户的设备设置策略。该接口可以设置指定用户在设置应用中的某个参数，比如设置用户100的设备名称等。

**需要权限：** ohos.permission.ENTERPRISE\_MANAGE\_SETTINGS

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| admin | [Want](<../../../../Ability Kit（程序框架服务）/ArkTS API/通用能力的接口(推荐)/@ohos.app.ability.Want (Want)/js-apis-app-ability-want.md>) | 是 | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |
| item | [SettingsItem](js-apis-enterprise-devicesettings.md#settingsitem24) | 是 | 设备设置策略类型。 |
| accountId | number | 是 | 用户ID，取值范围：大于等于0。  accountId可以通过[getOsAccountLocalId](<../../../Basic Services Kit（基础服务）/ArkTS API/账号管理/@ohos.account.osAccount (系统账号管理)/js-apis-osaccount.md#getosaccountlocalid9>)等接口来获取。 |
| value | string | 是 | 策略类型值。  当item为[SettingsItem.DEVICE\_NAME](js-apis-enterprise-devicesettings.md#settingsitem24)时，value为设备名称的字符串。 字符串长度范围：大于等于1，小于等于100。只允许设置当前用户的设备名称，设置其他用户的设备名称返回9200012错误码。  当item为[SettingsItem.FLOATING\_NAVIGATION](js-apis-enterprise-devicesettings.md#settingsitem24)时，在Phone和Tablet设备中可正常调用，在其他设备中返回801错误码。只允许设置当前用户的三键导航，设置其他用户的三键导航不会生效，value为三键导航的开关状态。  - '0'：表示开启三键导航（通过接口[enterKioskMode](<../../../../Ability Kit（程序框架服务）/ArkTS API/通用能力的接口(推荐)/@ohos.app.ability.kioskManager (Kiosk模式管理)/js-apis-app-ability-kioskmanager.md#kioskmanagerenterkioskmode>)进入Kiosk模式下，三键导航显示依赖底部手势开启；即三键导航开关和底部手势开关同时开启时，三键导航才会显示。底部手势可通过接口[applicationManager.setKioskFeatures](../@ohos.enterprise.applicationManager（应用管理）/js-apis-enterprise-applicationmanager.md#applicationmanagersetkioskfeatures20)设置开启或关闭）。  - '1'：表示关闭三键导航。 |

**错误码**：

以下错误码的详细介绍请参见[企业设备管理错误码](../../错误码/企业设备管理错误码/errorcode-enterprisedevicemanager.md)和[通用错误码](../../../../通用错误码/errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 9200012 | Parameter verification failed. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |

**示例：**

```
1. import { deviceSettings } from '@kit.MDMKit';
2. import { Want } from '@kit.AbilityKit';

4. let wantTemp: Want = {
5. // 需根据实际情况进行替换
6. bundleName: 'com.example.myapplication',
7. abilityName: 'EnterpriseAdminAbility'
8. };

10. try {
11. // 需根据实际情况进行替换
12. let accountId = 100;
13. let floatingNavigationStatus: string = "0"
14. deviceSettings.setValueForAccount(wantTemp, deviceSettings.SettingsItem.FLOATING_NAVIGATION, accountId, floatingNavigationStatus);
15. console.info('Succeeded in setting floating navigation status.');
16. } catch (err) {
17. console.error(`Failed to set floating navigation status. Code: ${err.code}, message: ${err.message}`);
18. }
```

## deviceSettings.getValueForAccount24+

PhonePC/2in1Tablet

getValueForAccount(admin: Want, item: SettingsItem, accountId: number): string

获取指定用户的设备设置策略。该接口可以获取指定用户在设置应用中的某个参数，比如获取用户100的设备名称等。

**需要权限：** ohos.permission.ENTERPRISE\_MANAGE\_SETTINGS

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| admin | [Want](<../../../../Ability Kit（程序框架服务）/ArkTS API/通用能力的接口(推荐)/@ohos.app.ability.Want (Want)/js-apis-app-ability-want.md>) | 是 | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |
| item | [SettingsItem](js-apis-enterprise-devicesettings.md#settingsitem24) | 是 | 设备设置策略类型。 |
| accountId | number | 是 | 用户ID，取值范围：大于等于0。  accountId可以通过[getOsAccountLocalId](<../../../Basic Services Kit（基础服务）/ArkTS API/账号管理/@ohos.account.osAccount (系统账号管理)/js-apis-osaccount.md#getosaccountlocalid9>)等接口来获取。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 策略类型值。  当item为[SettingsItem.DEVICE\_NAME](js-apis-enterprise-devicesettings.md#settingsitem24)时，返回当前用户的设备名称，查询非当前用户的设备名称返回9200012错误码。  当item为[SettingsItem.FLOATING\_NAVIGATION](js-apis-enterprise-devicesettings.md#settingsitem24)时，返回指定用户的三键导航的开关状态。  当item为[SettingsItem.FLOATING\_NAVIGATION](js-apis-enterprise-devicesettings.md#settingsitem24)时，该接口在Phone和Tablet设备中可正常调用，在其他设备中返回801错误码。 |

**错误码**：

以下错误码的详细介绍请参见[企业设备管理错误码](../../错误码/企业设备管理错误码/errorcode-enterprisedevicemanager.md)和[通用错误码](../../../../通用错误码/errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 9200012 | Parameter verification failed. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |

**示例：**

```
1. import { deviceSettings } from '@kit.MDMKit';
2. import { Want } from '@kit.AbilityKit';

4. let wantTemp: Want = {
5. // 需根据实际情况进行替换
6. bundleName: 'com.example.myapplication',
7. abilityName: 'EnterpriseAdminAbility'
8. };

10. try {
11. // 需根据实际情况进行替换
12. let accountId = 100;
13. let result: string = deviceSettings.getValueForAccount(wantTemp, deviceSettings.SettingsItem.FLOATING_NAVIGATION, accountId);
14. console.info(`Succeeded in getting floating navigation status., result : ${result}`);
15. } catch (err) {
16. console.error(`Failed to get floating navigation status. Code: ${err.code}, message: ${err.message}`);
17. }
```

## deviceSettings.addHiddenSettingsMenu24+

PhonePC/2in1Tablet

addHiddenSettingsMenu(admin: Want, menusToHidden: Array<SettingsMenu>): void

添加设置项至当前用户下的隐藏设置项列表。添加至隐藏设置项列表的设置项在当前用户的设置菜单中会被隐藏，隐藏后不可以在设置的搜索中搜索到。如果通过某种方式搜索到该设置项，点击后也无法打开。调用接口后即刻生效，无需重启设置应用。

**需要权限：** ohos.permission.ENTERPRISE\_MANAGE\_SETTINGS

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**设备行为差异：** 该接口在Phone和Tablet设备中可正常调用，在其他设备中返回801错误码。

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| admin | [Want](<../../../../Ability Kit（程序框架服务）/ArkTS API/通用能力的接口(推荐)/@ohos.app.ability.Want (Want)/js-apis-app-ability-want.md>) | 是 | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |
| menusToHidden | Array<[SettingsMenu](js-apis-enterprise-devicesettings.md#settingsmenu24)> | 是 | 隐藏的设置项列表。 |

**错误码**：

以下错误码的详细介绍请参见[企业设备管理错误码](../../错误码/企业设备管理错误码/errorcode-enterprisedevicemanager.md)和[通用错误码](../../../../通用错误码/errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 9200012 | Parameter verification failed. |
| 9200016 | Service timeout. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |

**示例：**

```
1. import { deviceSettings } from '@kit.MDMKit';
2. import { Want } from '@kit.AbilityKit';

4. let wantTemp: Want = {
5. // 需根据实际情况进行替换
6. bundleName: 'com.example.myapplication',
7. abilityName: 'EnterpriseAdminAbility'
8. };

10. let menusToHidden: Array<deviceSettings.SettingsMenu> = [
11. // 需根据实际情况进行替换或增加
12. deviceSettings.SettingsMenu.ACCOUNT_ID,
13. deviceSettings.SettingsMenu.WIFI,
14. ]

16. try {
17. deviceSettings.addHiddenSettingsMenu(wantTemp, menusToHidden);
18. console.info('Succeeded in adding hidden settings menu.');
19. } catch (err) {
20. console.error(`Failed to add hidden settings menu. Code: ${err.code}, message: ${err.message}`);
21. }
```

## deviceSettings.removeHiddenSettingsMenu24+

PhonePC/2in1Tablet

removeHiddenSettingsMenu(admin: Want, menusToHidden: Array<SettingsMenu>): void

将设置项从当前用户下的隐藏设置项列表中移除。隐藏设置项列表中的设置项在当前用户的设置菜单中会被隐藏，隐藏后不可以在设置的搜索中搜索到，如果通过某种方式搜索到该设置项，点击后也无法打开。若移除后剩余的隐藏设置项列表为空，则设置项会全部显示。调用接口后即刻生效，无需重启设置应用。

**需要权限：** ohos.permission.ENTERPRISE\_MANAGE\_SETTINGS

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**设备行为差异：** 该接口在Phone和Tablet设备中可正常调用，在其他设备中返回801错误码。

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| admin | [Want](<../../../../Ability Kit（程序框架服务）/ArkTS API/通用能力的接口(推荐)/@ohos.app.ability.Want (Want)/js-apis-app-ability-want.md>) | 是 | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |
| menusToHidden | Array<[SettingsMenu](js-apis-enterprise-devicesettings.md#settingsmenu24)> | 是 | 隐藏的设置项列表。 |

**错误码**：

以下错误码的详细介绍请参见[企业设备管理错误码](../../错误码/企业设备管理错误码/errorcode-enterprisedevicemanager.md)和[通用错误码](../../../../通用错误码/errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 9200012 | Parameter verification failed. |
| 9200016 | Service timeout. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |

**示例：**

```
1. import { deviceSettings } from '@kit.MDMKit';
2. import { Want } from '@kit.AbilityKit';

4. let wantTemp: Want = {
5. // 需根据实际情况进行替换
6. bundleName: 'com.example.myapplication',
7. abilityName: 'EnterpriseAdminAbility'
8. };

10. let menusToHidden: Array<deviceSettings.SettingsMenu> = [
11. // 需根据实际情况进行替换或增加
12. deviceSettings.SettingsMenu.ACCOUNT_ID,
13. deviceSettings.SettingsMenu.WIFI,
14. ]

16. try {
17. deviceSettings.removeHiddenSettingsMenu(wantTemp, menusToHidden);
18. console.info('Succeeded in removing hidden settings menu.');
19. } catch (err) {
20. console.error(`Failed to remove hidden settings menu. Code: ${err.code}, message: ${err.message}`);
21. }
```

## deviceSettings.getHiddenSettingsMenu24+

PhonePC/2in1Tablet

getHiddenSettingsMenu(admin: Want): Array<SettingsMenu>

获取配置在当前用户下被隐藏的设置项列表。

**需要权限：** ohos.permission.ENTERPRISE\_MANAGE\_SETTINGS

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**设备行为差异：** 该接口在Phone和Tablet设备中可正常调用，在其他设备中返回801错误码。

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| admin | [Want](<../../../../Ability Kit（程序框架服务）/ArkTS API/通用能力的接口(推荐)/@ohos.app.ability.Want (Want)/js-apis-app-ability-want.md>) | 是 | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array<[SettingsMenu](js-apis-enterprise-devicesettings.md#settingsmenu24)> | 隐藏的设置项列表。 |

**错误码**：

以下错误码的详细介绍请参见[企业设备管理错误码](../../错误码/企业设备管理错误码/errorcode-enterprisedevicemanager.md)和[通用错误码](../../../../通用错误码/errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |

**示例：**

```
1. import { deviceSettings } from '@kit.MDMKit';
2. import { Want } from '@kit.AbilityKit';

4. let wantTemp: Want = {
5. // 需根据实际情况进行替换
6. bundleName: 'com.example.myapplication',
7. abilityName: 'EnterpriseAdminAbility'
8. };

10. try {
11. const rawList: Array<number> = deviceSettings.getHiddenSettingsMenu(wantTemp) as Array<number>;
12. for (const item of rawList) {
13. const menu: deviceSettings.SettingsMenu = item as deviceSettings.SettingsMenu;
14. console.info(`Valid SettingsMenu item: ${item} -> ${menu}`);
15. }
16. console.info('Succeeded in getting hidden settings menu.');
17. } catch (err) {
18. console.error(`Failed to get hidden settings menu. Code: ${err.code}, message: ${err.message}`);
19. }
```

## SettingsItem24+

PhonePC/2in1Tablet

设置的策略类型。

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

| 名称 | 值 | 说明 |
| --- | --- | --- |
| DEVICE\_NAME | 0 | 设备名称。 |
| FLOATING\_NAVIGATION24+ | 1 | 三键导航。 |

## SettingsMenu24+

PhonePC/2in1Tablet

设置项列表。

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

| 名称 | 值 | 说明 |
| --- | --- | --- |
| ACCOUNT\_ID | 0 | 账号。 |
| WIFI | 1 | WLAN。 |
| WIFI\_PROXY\_SETTINGS | 2 | WLAN 代理。 |
| WIFI\_IP\_SETTINGS | 3 | WLAN IP 。 |
| BLUETOOTH | 4 | 星闪和蓝牙/蓝牙。 |
| NETWORK | 5 | 网络。 |
| MOBILE\_NETWORK | 6 | 移动网络。 |
| SUPER\_DEVICE | 7 | 多设备协同—超级终端。 |
| MORE\_CONNECTIVITY\_OPTIONS | 8 | 多设备协同。 |
| HOME\_SCREEN\_STYLE | 9 | 桌面和个性化。 |
| DISPLAY\_BRIGHTNESS | 10 | 显示和亮度。 |
| SOUND\_VIBRATION | 11 | 声音和振动。 |
| NOTIFICATIONS | 12 | 通知和状态栏。 |
| BIOMETRICS\_PASSWORD | 13 | 生物识别和密码。 |
| APPS\_AND\_SERVICES | 14 | 应用和元服务。 |
| BATTERY | 15 | 电池。 |
| STORAGE | 16 | 存储。 |
| PRIVACY\_AND\_SECURITY | 17 | 隐私和安全。 |
| DIGITAL\_BALANCE | 18 | 健康使用设备。 |
| SMART\_ASSISTANT | 19 | 智能助手。 |
| ACCESSIBILITY | 20 | 关怀和无障碍。 |
| SYSTEM | 21 | 系统。 |
| ABOUT\_DEVICE | 22 | 关于本机。 |
| SYSTEM\_NAVIGATION | 23 | 系统—系统导航。 |
| LANGUAGE\_REGION | 24 | 系统—语言和地区。 |
| INPUT\_METHODS | 25 | 系统—输入法。 |
| DATE\_TIME | 26 | 系统—日期和时间。 |
| DATA\_CLONE | 27 | 系统—数据克隆。 |
| BACKUP\_SETTINGS | 28 | 系统—备份和恢复。 |
| RESET | 29 | 系统—重置。 |
| SUPERHUB | 30 | 系统—中转站。 |
| USER\_EXPERIENCE | 31 | 系统—用户体验改进计划。 |
| SCREEN\_CAST | 32 | 多设备协同—无线投屏。 |
| PRINTERS\_SCANNERS | 33 | 打印机和扫描仪。 |
| MOBILE\_DATA | 34 | 移动网络—移动数据。 |
| PERSONAL\_HOTSPOT | 35 | 移动网络—个人热点。 |
| SIM\_MANAGEMENT | 36 | 移动网络—SIM卡管理。 |
| AIRPLANE\_MODE | 37 | 移动网络—飞行模式。 |
| MANAGE\_DATA\_USAGE | 38 | 移动网络—流量管理。 |
| VPN\_SETTINGS | 39 | 移动网络—VPN。 |
| TEXT\_DISPLAY\_SIZE | 40 | 显示和亮度—字体大小和界面缩放。 |
| APP\_DUPLICATOR | 41 | 系统—应用分身。 |
| SEARCH | 42 | 搜索。 |
