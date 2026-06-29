---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-form-liveformextensionability
title: @ohos.app.form.LiveFormExtensionAbility (LiveFormExtensionAbility)
breadcrumb: API参考 > 应用框架 > Form Kit（卡片开发服务） > ArkTS API > @ohos.app.form.LiveFormExtensionAbility (LiveFormExtensionAbility)
category: harmonyos-references
scraped_at: 2026-06-01T15:58:25+08:00
doc_updated_at: 2026-04-30
content_hash: sha256:50e19bad25e61fb0437c0ff05f5b33d97b585b9449a3f9cd833344838ee4dc91
---
LiveFormExtensionAbility模块提供互动卡片功能，包括创建、销毁互动卡片等，继承自[ExtensionAbility](<../../../Ability Kit（程序框架服务）/ArkTS API/Stage模型能力的接口/@ohos.app.ability.ExtensionAbility (扩展能力基类)/js-apis-app-ability-extensionability.md>)。

说明

本模块首批接口从API version 20开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

本模块接口仅可在Stage模型下使用。

本模块设置了不允许调用的API名单，调用名单中的API将导致功能异常，详情请参见[附录](js-apis-app-form-liveformextensionability.md#附录)。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { LiveFormExtensionAbility } from '@kit.FormKit';
```

## LiveFormExtensionAbility

PhonePC/2in1TabletTVWearable

互动卡片扩展类。包含互动卡片提供方接收创建和销毁互动卡片的通知接口。

### 属性

PhonePC/2in1TabletTVWearable

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Ability.Form

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| context | [LiveFormExtensionContext](../application/LiveFormExtensionContext/js-apis-application-liveformextensioncontext.md) | 否 | 否 | LiveFormExtensionAbility的上下文环境，继承自[ExtensionContext](<../../../Ability Kit（程序框架服务）/ArkTS API/接口依赖的元素及定义/application/ExtensionContext/js-apis-inner-application-extensioncontext.md>)。 |

### onLiveFormCreate

PhonePC/2in1TabletTVWearable

onLiveFormCreate(liveFormInfo: LiveFormInfo, session: UIExtensionContentSession): void

LiveFormExtensionAbility界面内容对象创建后调用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Ability.Form

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| liveFormInfo | [LiveFormInfo](js-apis-app-form-liveformextensionability.md#liveforminfo) | 是 | 互动卡片信息，包括卡片id等信息。 |
| session | [UIExtensionContentSession](<../../../Ability Kit（程序框架服务）/ArkTS API/Stage模型能力的接口/@ohos.app.ability.UIExtensionContentSession (带界面扩展能力的界面操作类)/js-apis-app-ability_18888586.md>) | 是 | LiveFormExtensionAbility界面内容相关信息。 |

**示例：**

```
1. import { UIExtensionContentSession } from '@kit.AbilityKit';
2. import { LiveFormExtensionAbility, LiveFormInfo } from '@kit.FormKit';

4. const TAG: string = '[testTag] LiveFormExtAbility';

6. export default class LiveFormExtAbility extends LiveFormExtensionAbility {
7. onLiveFormCreate(liveFormInfo: LiveFormInfo, session: UIExtensionContentSession) {
8. console.info(TAG, `onLiveFormCreate, formId: ${liveFormInfo.formId}`);
9. }
10. }
```

### onLiveFormDestroy

PhonePC/2in1TabletTVWearable

onLiveFormDestroy(liveFormInfo: LiveFormInfo): void

LiveFormExtensionAbility生命周期回调，在销毁时回调，执行资源清理等操作。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Ability.Form

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| liveFormInfo | [LiveFormInfo](js-apis-app-form-liveformextensionability.md#liveforminfo) | 是 | 互动卡片信息，包括卡片id等信息。 |

**示例：**

```
1. import { LiveFormExtensionAbility, LiveFormInfo } from '@kit.FormKit';

3. const TAG: string = '[testTag] LiveFormExtAbility';

5. export default class LiveFormExtAbility extends LiveFormExtensionAbility {
6. onLiveFormDestroy(liveFormInfo: LiveFormInfo) {
7. console.info(TAG, `onLiveFormDestroy, liveFormInfo: ${liveFormInfo.formId}`);
8. }
9. }
```

### LiveFormInfo

PhonePC/2in1TabletTVWearable

互动卡片信息。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Ability.Form

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| formId | string | 否 | 否 | 卡片id。 |
| rect | [formInfo.Rect](<../@ohos.app.form.formInfo (formInfo)/js-apis-app-form-forminfo.md#rect20>) | 否 | 否 | 卡片位置和大小信息。 |
| borderRadius | number | 否 | 否 | 卡片圆角半径信息。取值大于0，单位vp。 |

## 附录

PhonePC/2in1TabletTVWearable

本模块不允许调用的API名单如下。

| Kit名称 | 模块名称 |
| --- | --- |
| AbilityKit | [@ohos.ability.featureAbility (FeatureAbility模块)](<../../../Ability Kit（程序框架服务）/ArkTS API/FA模型能力的接口/@ohos.ability.featureAbility (FeatureAbility模块)/js-apis-ability-featureability.md>)  [@ohos.ability.particleAbility (ParticleAbility模块)](<../../../Ability Kit（程序框架服务）/ArkTS API/FA模型能力的接口/@ohos.ability.particleAbility (ParticleAbility模块)/js-apis-ability-particleability.md>)  [@ohos.bundle.launcherBundleManager (launcherBundleManager模块)](<../../../Ability Kit（程序框架服务）/ArkTS API/通用能力的接口(推荐)/@ohos.bundle.launcherBundleManager (launcherBundleManager模块)/js-apis-launcherbundlemanager.md>)  [@ohos.continuation.continuationManager (流转/协同管理)](<../../../Ability Kit（程序框架服务）/ArkTS API/Stage模型能力的接口/@ohos.continuation.continuationManager (流转协同管理)/js-apis-continuation-continuationmanager.md>) |
| BasicServicesKit | [@ohos.account.appAccount (应用账号管理)](<../../../基础功能/Basic Services Kit（基础服务）/ArkTS API/账号管理/@ohos.account.appAccount (应用账号管理)/js-apis-appaccount.md>)  [@ohos.account.distributedAccount (分布式账号管理)](<../../../基础功能/Basic Services Kit（基础服务）/ArkTS API/账号管理/@ohos.account.distributedAccount (分布式账号管理)/js-apis-distributed-account.md>)  [@ohos.account.osAccount (系统账号管理)](<../../../基础功能/Basic Services Kit（基础服务）/ArkTS API/账号管理/@ohos.account.osAccount (系统账号管理)/js-apis-osaccount.md>)  [@ohos.pasteboard (剪贴板)](<../../../基础功能/Basic Services Kit（基础服务）/ArkTS API/数据文件处理/@ohos.pasteboard (剪贴板)/js-apis-pasteboard.md>)  [@ohos.request (上传下载)](<../../../基础功能/Basic Services Kit（基础服务）/ArkTS API/数据文件处理/@ohos.request (上传下载)/js-apis-request.md>)  [@ohos.wallpaper (壁纸)](<../../../基础功能/Basic Services Kit（基础服务）/ArkTS API/其他/@ohos.wallpaper (壁纸)/js-apis-wallpaper.md>) |
| BackgroundTasksKit | [@ohos.backgroundTaskManager (后台任务管理)](<../../../Background Tasks Kit（后台任务开发服务）/ArkTS API/已停止维护的接口/@ohos.backgroundTaskManager (后台任务管理)/js-apis-backgroundtaskmanager.md>)  [@ohos.resourceschedule.backgroundTaskManager (后台任务管理)](<../../../Background Tasks Kit（后台任务开发服务）/ArkTS API/@ohos.resourceschedule.backgroundTaskManager (后台任务管理)/js-apis-resourceschedule-backgroundtaskmanager.md>)  [@ohos.reminderAgent (后台代理提醒)](<../../../Background Tasks Kit（后台任务开发服务）/ArkTS API/已停止维护的接口/@ohos.reminderAgent (后台代理提醒)/js-apis-reminderagent.md>)  [@ohos.reminderAgentManager (后台代理提醒)](<../../../Background Tasks Kit（后台任务开发服务）/ArkTS API/@ohos.reminderAgentManager (后台代理提醒)/js-apis-reminderagentmanager.md>) |
| CalendarKit | [@ohos.calendarManager (日程管理能力)](<../../../Calendar Kit（日历服务）/ArkTS API/@ohos.calendarManager (日程管理能力)/js-apis-calendarmanager.md>) |
| ConnectivityKit | [@ohos.connectedTag (有源标签)](<../../../网络/Connectivity Kit（短距通信服务）/ArkTS API/@ohos.connectedTag (有源标签)/js-apis-connectedtag.md>)  [@ohos.nfc.cardEmulation (标准NFC-cardEmulation)](<../../../网络/Connectivity Kit（短距通信服务）/ArkTS API/@ohos.nfc.cardEmulation (标准NFC-cardEmulation)/js-apis-cardemulation.md>)  [@ohos.nfc.controller (标准NFC)](<../../../网络/Connectivity Kit（短距通信服务）/ArkTS API/@ohos.nfc.controller (标准NFC)/js-apis-nfccontroller.md>)  [@ohos.nfc.tag (标准NFC-Tag)](<../../../网络/Connectivity Kit（短距通信服务）/ArkTS API/@ohos.nfc.tag (标准NFC-Tag)/js-apis-nfctag.md>)  [nfctech (标准NFC-Tag Nfc 技术)](<../../../网络/Connectivity Kit（短距通信服务）/ArkTS API/tag/nfctech (标准NFC-Tag Nfc 技术)/js-apis-nfctech.md>)  [tagSession (标准NFC-Tag TagSession)](<../../../网络/Connectivity Kit（短距通信服务）/ArkTS API/tag/tagSession (标准NFC-Tag TagSession)/js-apis-tagsession.md>) |
| ContactsKit | [@ohos.contact (联系人)](<../../../Contacts Kit（联系人服务）/ArkTS API/@ohos.contact (联系人)/js-apis-contact.md>) |
| ArkData | [@ohos.data.distributedData (分布式数据管理)](<../../../ArkData（方舟数据管理）/ArkTS API/已停止维护的接口/@ohos.data.distributedData (分布式数据管理)/js-apis-distributed-data.md>)  [@ohos.data.distributedDataObject (分布式数据对象)](<../../../ArkData（方舟数据管理）/ArkTS API/@ohos.data.distributedDataObject (分布式数据对象)/js-apis-data-distributedobject.md>)  [@ohos.data.distributedKVStore (分布式键值数据库)](<../../../ArkData（方舟数据管理）/ArkTS API/@ohos.data.distributedKVStore (分布式键值数据库)/js-apis-distributedkvstore.md>) |
| MDMKit | [@ohos.enterprise.adminManager (admin权限管理)](<../../../基础功能/MDM Kit（企业设备管理服务）/ArkTS API/@ohos.enterprise.adminManager（admin权限管理）/js-apis-enterprise-adminmanager.md>)  [@ohos.enterprise.deviceInfo（设备信息管理）](<../../../基础功能/MDM Kit（企业设备管理服务）/ArkTS API/@ohos.enterprise.deviceInfo（设备信息管理）/js-apis-enterprise-deviceinfo.md>) |
| CoreFileKit | [@ohos.file.picker (选择器)](<../../../Core File Kit（文件基础服务）/ArkTS API/@ohos.file.picker (选择器)/js-apis-file-picker.md>) |
| MediaLibraryKit | [@ohos.file.sendablePhotoAccessHelper (基于Sendable对象的相册管理模块)](<../../../Media Library Kit（媒体文件管理服务）/ArkTS API/@ohos.file.sendablePhotoAccessHelper (基于Sendable对象的相册管理模块)/js-apis-sendablephotoaccesshelper.md>)  [@ohos.file.AlbumPickerComponent (Album Picker组件)](<../../../Media Library Kit（媒体文件管理服务）/ArkTS组件/@ohos.file.AlbumPickerComponent (Album Picker组件)/ohos-file-albumpickercomponent.md>)  [@ohos.file.PhotoPickerComponent (PhotoPicker组件)](<../../../Media Library Kit（媒体文件管理服务）/ArkTS组件/@ohos.file.PhotoPickerComponent (PhotoPicker组件)/ohos-file-photopickercomponent.md>)  [@ohos.file.RecentPhotoComponent (最近图片组件)](<../../../Media Library Kit（媒体文件管理服务）/ArkTS组件/@ohos.file.RecentPhotoComponent (最近图片组件)/ohos-file-recentphotocomponent.md>)  [@ohos.multimedia.movingphotoview (动态照片)](<../../../Media Library Kit（媒体文件管理服务）/ArkTS组件/@ohos.multimedia.movingphotoview (动态照片)/ohos-multimedia-movingphotoview.md>) |
| PerformanceAnalysisKit | [@ohos.hidebug (Debug调试)](<../../../调测调优/Performance Analysis Kit（性能分析服务）/ArkTS API/@ohos.hidebug (Debug调试)/js-apis-hidebug.md>) |
| AudioKit | [@ohos.multimedia.audio (音频管理)](<../../../Audio Kit（音频服务）/ArkTS API/@ohos.multimedia.audio (音频管理)/模块描述/arkts-apis-audio.md>) |
| CameraKit | [@ohos.multimedia.cameraPicker (相机选择器)](<../../../Camera Kit（相机服务）/ArkTS API/@ohos.multimedia.cameraPicker (相机选择器)/js-apis-camerapicker.md>)  [@ohos.multimedia.camera (相机管理)](<../../../Camera Kit（相机服务）/ArkTS API/@ohos.multimedia.camera (相机管理)/模块描述/arkts-apis-camera.md>) |
| AVSessionKit | [@ohos.multimedia.avCastPicker (投播组件)](<../../../AVSession Kit（音视频播控服务）/ArkTS组件/@ohos.multimedia.avCastPicker (投播组件)/ohos-multimedia-avcastpicker.md>)  [@ohos.multimedia.avsession (媒体会话管理)](<../../../AVSession Kit（音视频播控服务）/ArkTS API/@ohos.multimedia.avsession (媒体会话管理)/模块描述/arkts-apis-avsession.md>) |
| MediaKit | [@ohos.multimedia.media (媒体服务)](<../../../Media Kit（媒体服务）/ArkTS API/@ohos.multimedia.media (媒体服务)/模块描述/arkts-apis-media.md>) |
| NotificationKit | [@ohos.notification (Notification模块)](<../../../Notification Kit（用户通知服务）/ArkTS API/已停止维护的接口/@ohos.notification (Notification模块)/js-apis-notification.md>)  [@ohos.notificationManager (NotificationManager模块)](<../../../Notification Kit（用户通知服务）/ArkTS API/@ohos.notificationManager (NotificationManager模块)/js-apis-notificationmanager.md>) |
| TelephonyKit | [@ohos.telephony.call (拨打电话)](<../../../网络/Telephony Kit（蜂窝通信服务）/ArkTS API/@ohos.telephony.call (拨打电话)/js-apis-call.md>)  [@ohos.telephony.data (蜂窝数据)](<../../../网络/Telephony Kit（蜂窝通信服务）/ArkTS API/@ohos.telephony.data (蜂窝数据)/js-apis-telephony-data.md>)  [@ohos.telephony.observer (observer)](<../../../网络/Telephony Kit（蜂窝通信服务）/ArkTS API/@ohos.telephony.observer (observer)/js-apis-observer.md>)  [@ohos.telephony.radio (网络搜索)](<../../../网络/Telephony Kit（蜂窝通信服务）/ArkTS API/@ohos.telephony.radio (网络搜索)/js-apis-radio.md>)  [@ohos.telephony.sim (SIM卡管理)](<../../../网络/Telephony Kit（蜂窝通信服务）/ArkTS API/@ohos.telephony.sim (SIM卡管理)/js-apis-sim.md>)  [@ohos.telephony.sms (短信服务)](<../../../网络/Telephony Kit（蜂窝通信服务）/ArkTS API/@ohos.telephony.sms (短信服务)/js-apis-sms.md>) |
| UserAuthenticationKit | [@ohos.userIAM.userAuth (用户认证)](<../../../安全/User Authentication Kit（用户认证服务）/ArkTS API/@ohos.userIAM.userAuth (用户认证)/js-apis-useriam-userauth.md>) |
| ArkUI | [@ohos.window (窗口)](<../../../ArkUI（方舟UI框架）/ArkTS API/窗口管理/@ohos.window (窗口)/模块描述/arkts-apis-window.md>) |
| MapKit | [sceneMap（场景化控件）](<../../../Map Kit（地图服务）/ArkTS API/sceneMap（场景化控件）/map-scenemap.md>) |
| PaymentKit | [paymentService (鸿蒙支付服务)](<../../../Payment Kit（鸿蒙支付服务）/ArkTS API/paymentService (鸿蒙支付服务)/payment-paymentservice.md>) |
| ServiceCollaborationKit | [devicePicker (设备选择控制器)](<../../../网络/Service Collaboration Kit（协同服务）/ArkTS组件/devicePicker (设备选择控制器)/servicecollaboration-devicepicker.md>)  [CollaborationDevicePicker (流转控件)](<../../../网络/Service Collaboration Kit（协同服务）/ArkTS组件/CollaborationDevicePicker (流转控件)/servicecollaboration-collaborationdevicepicker.md>) |
| ShareKit | [systemShare（分享）](<../../../Share Kit（分享服务）/ArkTS API/systemShare（分享）/share-system-share.md>)  [harmonyShare（华为分享）](<../../../Share Kit（分享服务）/ArkTS API/harmonyShare（华为分享）/share-harmony-share.md>) |
| VisionKit | [CardRecognition（卡证识别控件）](<../../../Vision Kit（场景化视觉服务）/ArkTS组件/CardRecognition（卡证识别控件）/vision-card-recognition.md>)  [DocumentScanner（文档扫描控件）](<../../../Vision Kit（场景化视觉服务）/ArkTS组件/DocumentScanner（文档扫描控件）/vision-document-scanner.md>) |
| ScanKit | [Scan Kit（统一扫码服务）](<../../../Scan Kit（统一扫码服务）/scan-api.md>) |
