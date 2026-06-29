---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-advertising
title: @ohos.advertising (广告服务框架)
breadcrumb: API参考 > 应用服务 > Ads Kit（广告服务） > ArkTS API > @ohos.advertising (广告服务框架)
category: harmonyos-references
scraped_at: 2026-06-11T16:42:52+08:00
doc_updated_at: 2026-06-05
content_hash: sha256:ab37ee651dfe8b0609ea13846b9c312781a6ddcb80ad7f1ae95c1aaf388ca861
---
本模块提供广告操作能力，包括请求广告、展示广告。

说明

本模块首批接口从API version 11开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

PhonePC/2in1Tablet

```
1. import { advertising } from '@kit.AdsKit';
```

## advertising.showAd

PhonePC/2in1Tablet

showAd(ad: Advertisement, options: AdDisplayOptions, context?: common.UIAbilityContext): void

展示全屏广告。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Advertising.Ads

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| ad | [Advertisement](js-apis-advertising.md#advertisement) | 是 | 广告对象。 |
| options | [AdDisplayOptions](js-apis-advertising.md#addisplayoptions) | 是 | 广告展示参数。 |
| context | common.[UIAbilityContext](<../../../Ability Kit（程序框架服务）/ArkTS API/接口依赖的元素及定义/application/UIAbilityContext/js-apis-inner-application-uiabilitycontext.md>) | 否 | UIAbility的上下文环境，不设置从api: @ohos.app.ability.common中获取。 |

**错误码：**

以下错误码的详细介绍请参见[广告服务框架错误码参考](../../错误码/广告服务框架错误码/errorcode-ads.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Invalid input parameter. Possible causes: 1. Mandatory parameters are left unspecified. |
| 21800001 | System internal error. |
| 21800004 | Failed to display the ad. |

**示例：**

其中context的获取方式参见[各类Context的获取方式](<../../../../harmonyos-guides/应用框架/Ability Kit（程序框架服务）/Stage模型开发指导/Stage模型应用组件/应用上下文Context/application-context-stage.md#context的获取方式>)。

```
1. import { common } from '@kit.AbilityKit';
2. import { advertising } from '@kit.AdsKit';

4. function showAd(ad: advertising.Advertisement, context?: common.UIAbilityContext): void {
5. // 广告展示参数，开发者可根据项目实际情况设置
6. const adDisplayOptions: advertising.AdDisplayOptions = {};
7. // 调用全屏广告展示接口
8. advertising.showAd(ad, adDisplayOptions, context);
9. }
```

## advertising.getAdRequestBody12+

PhonePC/2in1Tablet

getAdRequestBody(adParams: AdRequestParams[], adOptions: AdOptions): Promise<string>

获取广告请求响应体，使用Promise异步回调。

**系统能力：** SystemCapability.Advertising.Ads

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| adParams | [AdRequestParams[]](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-advertising#adrequestparams) | 是 | 广告请求参数。 |
| adOptions | [AdOptions](js-apis-advertising.md#adoptions) | 是 | 广告配置参数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<string> | Promise对象，返回字符类型的广告数据。 |

**错误码：**

以下错误码的详细介绍请参见[广告服务框架错误码参考](../../错误码/广告服务框架错误码/errorcode-ads.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Invalid input parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Device not supported. |
| 21800001 | System internal error. |

**示例：**

```
1. import { advertising } from '@kit.AdsKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. function getAdRequestBody(adRequestParamsArray: advertising.AdRequestParams[]): void {
5. // 广告配置参数，开发者可根据项目实际情况设置
6. const adOptions: advertising.AdOptions = {};
7. advertising.getAdRequestBody(adRequestParamsArray, adOptions).then((data: string) => {
8. hilog.info(0x0000, 'testTag', `Succeeded in getting ad request body. Data is ${data}`);
9. });
10. }
```

## advertising.parseAdResponse12+

PhonePC/2in1Tablet

parseAdResponse(adResponse: string, listener: MultiSlotsAdLoadListener, context: common.UIAbilityContext): void

解析并处理广告响应体。

**系统能力：** SystemCapability.Advertising.Ads

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| adResponse | string | 是 | 广告响应体。 |
| listener | [MultiSlotsAdLoadListener](js-apis-advertising.md#multislotsadloadlistener) | 是 | 请求广告回调监听。 |
| context | common.[UIAbilityContext](<../../../Ability Kit（程序框架服务）/ArkTS API/接口依赖的元素及定义/application/UIAbilityContext/js-apis-inner-application-uiabilitycontext.md>) | 是 | UIAbility的上下文环境。 |

**错误码：**

以下错误码的详细介绍请参见[广告服务框架错误码参考](../../错误码/广告服务框架错误码/errorcode-ads.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Invalid input parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Device not supported. |
| 21800001 | System internal error. |
| 21800005 | Failed to parse the ad response. |

**示例：**

其中context的获取方式参见[各类Context的获取方式](<../../../../harmonyos-guides/应用框架/Ability Kit（程序框架服务）/Stage模型开发指导/Stage模型应用组件/应用上下文Context/application-context-stage.md#context的获取方式>)。

```
1. import { common } from '@kit.AbilityKit';
2. import { advertising } from '@kit.AdsKit';
3. import { hilog } from '@kit.PerformanceAnalysisKit';

5. function parseAdResponse(adResponse: string, context: common.UIAbilityContext): void {
6. // 广告解析处理回调监听
7. const multiSlotsAdLoaderListener: advertising.MultiSlotsAdLoadListener = {
8. onAdLoadFailure: (errorCode: number, errorMsg: string) => {
9. hilog.error(0x0000, 'testTag', `Failed to load multiSlots ad. Code is ${errorCode}, message is ${errorMsg}`);
10. },
11. onAdLoadSuccess: (ads: Map<string, Array<advertising.Advertisement>>) => {
12. hilog.info(0x0000, 'testTag', 'Succeeded in loading multiSlots ad');
13. // 保存解析处理完成的广告内容用于展示
14. const returnAds: advertising.Advertisement[] = [];
15. ads.forEach((adsArray) => returnAds.push(...adsArray));
16. }
17. };
18. // 调用响应体解析接口
19. advertising.parseAdResponse(adResponse, multiSlotsAdLoaderListener, context);
20. }
```

## advertising.registerWebAdInterface12+

PhonePC/2in1Tablet

registerWebAdInterface(controller: web\_webview.WebviewController, context: common.UIAbilityContext): void

注入广告JavaScript对象到Web组件中。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Advertising.Ads

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| controller | web\_webview.[WebviewController](<../../../ArkWeb（方舟Web）/ArkTS API/@ohos.web.webview (Webview)/Class (WebviewController)/arkts-apis-webview-webviewcontroller.md>) | 是 | Web组件控制器。 |
| context | common.[UIAbilityContext](<../../../Ability Kit（程序框架服务）/ArkTS API/接口依赖的元素及定义/application/UIAbilityContext/js-apis-inner-application-uiabilitycontext.md>) | 是 | UIAbility的上下文环境。 |

**错误码：**

以下错误码的详细介绍请参见[广告服务框架错误码参考](../../错误码/广告服务框架错误码/errorcode-ads.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Invalid input parameter. Possible causes: 1. Mandatory parameters are left unspecified. |
| 21800001 | System internal error. |

**示例：**

```
1. import { common } from '@kit.AbilityKit';
2. import { advertising } from '@kit.AdsKit';
3. import { webview } from '@kit.ArkWeb';

5. @Entry
6. @Component
7. struct Index {
8. private context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
9. private webViewController: webview.WebviewController = new webview.WebviewController();

11. build() {
12. Column() {
13. Button('registerWebAdInterface')
14. .onClick(() => {
15. advertising.registerWebAdInterface(this.webViewController, this.context);
16. })

18. Web({ src: 'https://www.example.com', controller: this.webViewController })
19. }
20. .width('100%')
21. .height('100%')
22. }
23. }
```

## advertising.registerWebAdInterface16+

PhonePC/2in1Tablet

registerWebAdInterface(controller: web\_webview.WebviewController, context: common.UIAbilityContext, needRefresh: boolean): void

注入广告JavaScript对象到Web组件中。

**元服务API：** 从API version 16开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Advertising.Ads

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| controller | web\_webview.[WebviewController](<../../../ArkWeb（方舟Web）/ArkTS API/@ohos.web.webview (Webview)/Class (WebviewController)/arkts-apis-webview-webviewcontroller.md>) | 是 | Web组件控制器。 |
| context | common.[UIAbilityContext](<../../../Ability Kit（程序框架服务）/ArkTS API/接口依赖的元素及定义/application/UIAbilityContext/js-apis-inner-application-uiabilitycontext.md>) | 是 | UIAbility的上下文环境。 |
| needRefresh | boolean | 是 | 是否需要刷新页面（true: 需要；false: 不需要）。 |

**错误码：**

以下错误码的详细介绍请参见[广告服务框架错误码参考](../../错误码/广告服务框架错误码/errorcode-ads.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Invalid input parameter. Possible causes: Mandatory parameters are left unspecified. |
| 21800001 | System internal error. |

**示例：**

```
1. import { common } from '@kit.AbilityKit';
2. import { advertising } from '@kit.AdsKit';
3. import { webview } from '@kit.ArkWeb';

5. @Entry
6. @Component
7. struct Index {
8. private context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
9. private webViewController: webview.WebviewController = new webview.WebviewController();

11. build() {
12. Column() {
13. Button('registerWebAdInterface')
14. .onClick(() => {
15. advertising.registerWebAdInterface(this.webViewController, this.context, true);
16. })

18. Web({ src: 'https://www.example.com', controller: this.webViewController })
19. }
20. .width('100%')
21. .height('100%')
22. }
23. }
```

## advertising.deleteWebAdInterface16+

PhonePC/2in1Tablet

deleteWebAdInterface(controller: web\_webview.WebviewController, needRefresh: boolean): void

删除通过registerWebAdInterface注入的广告JavaScript对象。

**元服务API：** 从API version 16开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Advertising.Ads

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| controller | web\_webview.[WebviewController](<../../../ArkWeb（方舟Web）/ArkTS API/@ohos.web.webview (Webview)/Class (WebviewController)/arkts-apis-webview-webviewcontroller.md>) | 是 | Web组件控制器。 |
| needRefresh | boolean | 是 | 是否需要刷新页面（true: 需要；false: 不需要）。 |

**错误码：**

以下错误码的详细介绍请参见[广告服务框架错误码参考](../../错误码/广告服务框架错误码/errorcode-ads.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Invalid input parameter. Possible causes: Mandatory parameters are left unspecified. |
| 21800001 | System internal error. |

**示例：**

```
1. import { advertising } from '@kit.AdsKit';
2. import { webview } from '@kit.ArkWeb';

4. @Entry
5. @Component
6. struct Index {
7. private webViewController: webview.WebviewController = new webview.WebviewController();

9. build() {
10. Column() {
11. Button('deleteWebAdInterface')
12. .onClick(() => {
13. advertising.deleteWebAdInterface(this.webViewController, true);
14. })

16. Web({ src: 'https://www.example.com', controller: this.webViewController })
17. }
18. .width('100%')
19. .height('100%')
20. }
21. }
```

## AdLoader

PhonePC/2in1Tablet

提供加载广告的功能。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Advertising.Ads

### constructor

PhonePC/2in1Tablet

constructor(context: common.Context)

构造函数。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Advertising.Ads

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | common.[Context](<../../../Ability Kit（程序框架服务）/ArkTS API/接口依赖的元素及定义/application/Context (Stage模型的上下文基类)/js-apis-inner-application-context.md>) | 是 | ability或application的上下文环境。 |

**示例：**

其中context的获取方式参见[各类Context的获取方式](<../../../../harmonyos-guides/应用框架/Ability Kit（程序框架服务）/Stage模型开发指导/Stage模型应用组件/应用上下文Context/application-context-stage.md#context的获取方式>)。

```
1. import { common } from '@kit.AbilityKit';
2. import { advertising } from '@kit.AdsKit';

4. function createAdLoader(context: common.Context): void {
5. const adLoader: advertising.AdLoader = new advertising.AdLoader(context);
6. }
```

### loadAd

PhonePC/2in1Tablet

loadAd(adParam: AdRequestParams, adOptions: AdOptions, listener: AdLoadListener): void

请求单广告位广告。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Advertising.Ads

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| adParam | [AdRequestParams](js-apis-advertising.md#adrequestparams) | 是 | 广告请求参数。 |
| adOptions | [AdOptions](js-apis-advertising.md#adoptions) | 是 | 广告配置参数。 |
| listener | [AdLoadListener](js-apis-advertising.md#adloadlistener) | 是 | 请求广告回调监听。 |

**错误码：**

以下错误码的详细介绍请参见[广告服务框架错误码参考](../../错误码/广告服务框架错误码/errorcode-ads.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Invalid input parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed. |
| 801 | Device not supported. |
| 21800001 | System internal error. |
| 21800003 | Failed to load the ad request. |

**示例：**

其中context的获取方式参见[各类Context的获取方式](<../../../../harmonyos-guides/应用框架/Ability Kit（程序框架服务）/Stage模型开发指导/Stage模型应用组件/应用上下文Context/application-context-stage.md#context的获取方式>)。

```
1. import { common } from '@kit.AbilityKit';
2. import { advertising } from '@kit.AdsKit';
3. import { hilog } from '@kit.PerformanceAnalysisKit';

5. function loadAd(context: common.Context, adRequestParams: advertising.AdRequestParams): void {
6. // 广告配置参数，开发者可根据项目实际情况设置
7. const adOptions: advertising.AdOptions = {};
8. // 广告请求回调监听
9. const adLoaderListener: advertising.AdLoadListener = {
10. onAdLoadFailure: (errorCode: number, errorMsg: string) => {
11. hilog.error(0x0000, 'testTag', `Failed to load ad. Code is ${errorCode}, message is ${errorMsg}`);
12. },
13. onAdLoadSuccess: (ads: Array<advertising.Advertisement>) => {
14. hilog.info(0x0000, 'testTag', 'Succeeded in loading ad');
15. // 保存请求到的广告内容用于展示
16. const returnAds: advertising.Advertisement[] = ads;
17. }
18. };
19. // 创建AdLoader广告对象
20. const adLoader: advertising.AdLoader = new advertising.AdLoader(context);
21. // 调用广告请求接口
22. adLoader.loadAd(adRequestParams, adOptions, adLoaderListener);
23. }
```

### loadAdWithMultiSlots

PhonePC/2in1Tablet

loadAdWithMultiSlots(adParams: AdRequestParams[], adOptions: AdOptions, listener: MultiSlotsAdLoadListener): void

请求多广告位广告。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Advertising.Ads

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| adParams | [AdRequestParams](js-apis-advertising.md#adrequestparams)[] | 是 | 广告请求参数。 |
| adOptions | [AdOptions](js-apis-advertising.md#adoptions) | 是 | 广告配置参数。 |
| listener | [MultiSlotsAdLoadListener](js-apis-advertising.md#multislotsadloadlistener) | 是 | 请求广告回调监听。 |

**错误码：**

以下错误码的详细介绍请参见[广告服务框架错误码参考](../../错误码/广告服务框架错误码/errorcode-ads.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Invalid input parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed. |
| 801 | Device not supported. |
| 21800001 | System internal error. |
| 21800003 | Failed to load the ad request. |

**示例：**

其中context的获取方式参见[各类Context的获取方式](<../../../../harmonyos-guides/应用框架/Ability Kit（程序框架服务）/Stage模型开发指导/Stage模型应用组件/应用上下文Context/application-context-stage.md#context的获取方式>)。

```
1. import { common } from '@kit.AbilityKit';
2. import { advertising } from '@kit.AdsKit';
3. import { hilog } from '@kit.PerformanceAnalysisKit';

5. function loadAdWithMultiSlots(context: common.Context, adRequestParamsArray: advertising.AdRequestParams[]): void {
6. // 广告配置参数，开发者可根据项目实际情况设置
7. const adOptions: advertising.AdOptions = {};
8. // 广告请求回调监听
9. const multiSlotsAdLoaderListener: advertising.MultiSlotsAdLoadListener = {
10. onAdLoadFailure: (errorCode: number, errorMsg: string) => {
11. hilog.error(0x0000, 'testTag', `Failed to load multiSlots ad. Code is ${errorCode}, message is ${errorMsg}`);
12. },
13. onAdLoadSuccess: (ads: Map<string, Array<advertising.Advertisement>>) => {
14. hilog.info(0x0000, 'testTag', 'Succeeded in loading multiSlots ad');
15. // 保存请求到的广告内容用于展示
16. const returnAds: advertising.Advertisement[] = [];
17. ads.forEach((adsArray) => returnAds.push(...adsArray));
18. }
19. };
20. // 创建AdLoader广告对象
21. const adLoader: advertising.AdLoader = new advertising.AdLoader(context);
22. // 调用广告请求接口
23. adLoader.loadAdWithMultiSlots(adRequestParamsArray, adOptions, multiSlotsAdLoaderListener);
24. }
```

## AdLoadListener

PhonePC/2in1Tablet

单广告位广告请求回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Advertising.Ads

### onAdLoadFailure

PhonePC/2in1Tablet

onAdLoadFailure(errorCode: number, errorMsg: string): void

广告请求失败回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Advertising.Ads

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| errorCode | number | 是 | 广告请求失败的错误码。 |
| errorMsg | string | 是 | 广告请求失败的错误信息。 |

### onAdLoadSuccess

PhonePC/2in1Tablet

onAdLoadSuccess(ads: Array<Advertisement>): void

广告请求成功后回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Advertising.Ads

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| ads | Array<[Advertisement](js-apis-advertising.md#advertisement)> | 是 | 广告数据。 |

**示例：**

```
1. import { advertising } from '@kit.AdsKit';

3. const adLoaderListener: advertising.AdLoadListener = {
4. onAdLoadFailure: (errorCode: number, errorMsg: string) => {
5. },
6. onAdLoadSuccess: (ads: Array<advertising.Advertisement>) => {
7. }
8. }
```

## MultiSlotsAdLoadListener

PhonePC/2in1Tablet

多广告位广告请求回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Advertising.Ads

### onAdLoadFailure

PhonePC/2in1Tablet

onAdLoadFailure(errorCode: number, errorMsg: string): void

多广告位广告请求失败回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Advertising.Ads

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| errorCode | number | 是 | 广告请求失败的错误码。 |
| errorMsg | string | 是 | 广告请求失败的错误信息。 |

### onAdLoadSuccess

PhonePC/2in1Tablet

onAdLoadSuccess(adsMap: Map<string, Array<Advertisement>>): void

多广告位广告请求成功后回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Advertising.Ads

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| adsMap | Map<string, Array<[Advertisement](js-apis-advertising.md#advertisement)>> | 是 | 广告数据。 |

**示例：**

```
1. import { advertising } from '@kit.AdsKit';

3. const multiSlotsAdLoadListener: advertising.MultiSlotsAdLoadListener = {
4. onAdLoadFailure: (errorCode: number, errorMsg: string) => {
5. },
6. onAdLoadSuccess: (adsMap: Map<string, Array<advertising.Advertisement>>) => {
7. }
8. }
```

## AdInteractionListener

PhonePC/2in1Tablet

广告状态变化回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Advertising.Ads

### onStatusChanged

PhonePC/2in1Tablet

onStatusChanged(status: string, ad: Advertisement, data: string)

广告状态回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Advertising.Ads

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| status | string | 是 | 广告展示状态。  - onAdLoad：广告加载成功。  - onAdFail：广告加载失败。 |
| ad | [Advertisement](js-apis-advertising.md#advertisement) | 是 | 发生状态变化的广告内容。 |
| data | string | 是 | 扩展信息。 |

**示例：**

```
1. import { advertising } from '@kit.AdsKit';

3. const adInteractionListener: advertising.AdInteractionListener = {
4. onStatusChanged: (status: string, ad: advertising.Advertisement, data: string) => {
5. }
6. }
```

## AdOptions

PhonePC/2in1Tablet

广告配置参数。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Advertising.Ads

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| tagForChildProtection | number | 否 | 是 | 设置儿童保护标签，是否希望根据 COPPA 的规定将您的内容视为面向儿童的内容。  - -1：不确定。  - 0：不希望。  - 1：希望。 |
| adContentClassification | string | 否 | 是 | 设置广告内容分级上限。  - W：3+，所有受众。  - PI：7+，家长指导。  - J：12+，青少年。  - A：16+/18+，成人受众。 |
| nonPersonalizedAd | number | 否 | 是 | 设置是否只请求非个性化广告。  - 0：请求个性化广告与非个性化广告。  - 1：只请求非个性化广告。 |
| [key: string] | number | boolean | string | undefined | 否 | 是 | 自定义参数。 |

## AdRequestParams

PhonePC/2in1Tablet

广告请求参数。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Advertising.Ads

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| adId | string | 否 | 否 | 广告位ID。 |
| adType | number | 否 | 是 | 请求的广告类型。  - 1：开屏广告。  - 3：原生广告。  - 7：激励广告。  - 8：横幅广告。  - 12：插屏广告。  - 60：贴片广告。 |
| adCount | number | 否 | 是 | 请求的广告数量。 |
| adWidth | number | 否 | 是 | 请求广告时期望的创意宽度，单位vp。 |
| adHeight | number | 否 | 是 | 请求广告时期望的创意高度，单位vp。 |
| adSearchKeyword | string | 否 | 是 | 广告关键字。 |
| [key: string] | number | boolean | string | undefined | 否 | 是 | 自定义参数。  - oaid: 类型string，开放匿名设备标识符，用于精准推送广告。 |

## AdDisplayOptions

PhonePC/2in1Tablet

广告展示参数。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Advertising.Ads

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| customData | string | 否 | 是 | 媒体自定义数据。 |
| userId | string | 否 | 是 | 媒体自定义用户id。 |
| useMobileDataReminder | boolean | 否 | 是 | 使用移动数据播放视频或下载应用时是否弹框通知用户。  - true：弹框通知。  - false：不弹框通知。 |
| mute | boolean | 否 | 是 | 广告视频播放是否静音。  - true：静音播放。  - false：非静音播放。 |
| audioFocusType | number | 否 | 是 | 视频播放过程中获得音频焦点的场景类型。  - 0：视频播放静音、非静音时都获取焦点。  - 1：视频静音播放时不获取焦点。  - 2：视频播放静音、非静音时都不获取焦点。 |
| [key: string] | number | boolean | string | undefined | 否 | 是 | 自定义参数。  - refreshTime：类型number，单位：ms，取值范围[30000, 120000]。AutoAdComponent组件可选自定义参数，用于控制广告的轮播时间间隔。填写了该参数，则广告按照参数配置的时间间隔轮播，否则广告不会轮播，只会展示广告响应中的第一个广告内容。 |

## Advertisement

PhonePC/2in1Tablet

type Advertisement = \_Advertisement

请求的广告内容。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Advertising.Ads

| 类型 | 说明 |
| --- | --- |
| [\_Advertisement](<../advertisement/advertisement (广告内容)/js-apis-advertisement.md>) | 表示Advertisement对象。 |
