---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/os-new-feature-511-beta1
title: 新增和增强特性
breadcrumb: 版本说明 > 历史版本 > HarmonyOS 5.1.1(19) > OS平台能力 > 新增和增强特性
category: harmonyos-releases
scraped_at: 2026-06-01T10:45:38+08:00
doc_updated_at: 2026-03-17
content_hash: sha256:36b4fa4e108a10490c9d9137a4dc99cb557a6d2f5d013864daa5675eb3c0d2c5
---
## ArkUI

* 弹窗能力增强。包括：
  + 进一步丰富弹窗在Native侧的能力，包括：设置自定义弹窗显示的顺序、边框宽度和边框颜色等。（[API参考](<../../../../../harmonyos-references/ArkUI（方舟UI框架）/C API/结构体/ArkUI_NativeDialogAPI_3/capi-arkui-nativemodule-arkui-nativedialogapi-3.md>)）
  + 支持通过侧滑手势关闭OverlayManager下的[ComponentContent](<../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS API/UI界面/arkui/ComponentContent/js-apis-arkui-componentcontent.md>)。（[API参考](<../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS API/UI界面/@ohos.arkui.UIContext (UIContext)/Interfaces (其他)/arkts-apis-uicontext-i.md#overlaymanageroptions15>)）
  + 支持设置弹窗内容和蒙层显示的过渡效果。（[API参考](<../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS API/UI界面/@ohos.promptAction (弹窗)/js-apis-promptaction.md#basedialogoptions11>)）
  + 支持设置弹窗是否获取焦点。（[API参考](<../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS API/UI界面/@ohos.promptAction (弹窗)/js-apis-promptaction.md#basedialogoptions11>)）

* XComponent支持在Native侧获取XComponent节点实例、注册XComponent持有的Surface的生命周期回调和触摸、鼠标、按键等组件事件回调。（[API参考](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/渲染绘制/XComponent/ts-basic-components-xcomponent.md#xcomponent19)）
* 新增LazyVGridLayout组件，用于实现懒加载的网格布局。（[API参考](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/滚动与滑动/LazyVGridLayout/ts-container-lazyvgridlayout.md)）
* Tabs支持设置子组件的最大缓存个数和缓存模式。（[API参考](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/导航与切换/Tabs/ts-container-tabs.md#cachedmaxcount19)）
* List组件支持从末尾开始布局。（[API参考](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/滚动与滑动/List/ts-container-list.md#stackfromend19)）
* 丰富Swiper组件在Native侧的能力，包括：创建并设置数字导航指示器的样式、创建并设置导航箭头的样式等。（[API参考](<../../../../../harmonyos-references/ArkUI（方舟UI框架）/C API/头文件/native_type.h/capi-native-type-h.md#oh_arkui_swiperdigitindicator_create>)）
* Swiper组件支持设置圆点导航点间距和导航点底部相对于Swiper的位置。（[API参考](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/滚动与滑动/Swiper/ts-container-swiper.md#space19)）
* Navigation支持获取当前路由栈中的路由页面信息数组，并将数组更新为指定内容，实现路由转场。（[API参考](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/导航与切换/Navigation/ts-basic-components-navigation.md#getpathstack19)）
* 新增onNewParam回调，当栈中存在的NavDestination页面通过单实例方式移动到栈顶时，触发对应的生命周期。（[API参考](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/导航与切换/NavDestination/ts-basic-components-navdestination.md#onnewparam19)）
* 属性字符串和RichEditor支持设置段落间距。（[API参考-属性字符串](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/文本与输入/属性字符串/ts-universal-styled-string.md#属性-8)、[API参考-RichEditor](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/文本与输入/RichEditor/ts-basic-components-richeditor.md#richeditorparagraphstyle11)）
* 支持设置关键帧动画（keyframeAnimateTo）的期望帧率。（[API参考-ArkTS](<../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/动画/关键帧动画 (keyframeAnimateTo)/ts-keyframeanimateto.md#keyframeanimateparam对象说明>)、[API参考-C](<../../../../../harmonyos-references/ArkUI（方舟UI框架）/C API/头文件/native_animate.h/capi-native-animate-h.md#oh_arkui_keyframeanimateoption_setexpectedframerate>)）
* 支持在按键事件发生时获取NumLock/CapsLock/ScrollLock的状态。（[API参考-ArkTS](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/通用事件/基础输入事件/按键事件/ts-universal-events-key.md#keyevent对象说明)、[API参考-C](<../../../../../harmonyos-references/ArkUI（方舟UI框架）/C API/头文件/native_key_event.h/capi-native-key-event-h.md#oh_arkui_keyevent_isnumlockon>)）
* 拖拽释放时，支持应用延迟返回处理结果。（[API参考](<../../../../../harmonyos-references/ArkUI（方舟UI框架）/C API/头文件/drag_and_drop.h/capi-drag-and-drop-h.md#oh_arkui_dragevent_requestdragendpending>)）
* 支持监听Pan手势的[onActionStart](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/手势处理/基础手势/PanGesture/ts-basic-gestures-pangesture.md#事件)事件，可获取触发Pan手势事件的相关信息。（[API参考](<../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS API/UI界面/@ohos.arkui.UIContext (UIContext)/Class (UIObserver)/arkts-apis-uicontext-uiobserver.md#onbeforepanstart19>)）
* 背景图支持通过NODE\_BACKGROUND\_IMAGE\_RESIZABLE\_WITH\_SLICE属性，在拉伸时可调整大小。（[API参考](<../../../../../harmonyos-references/ArkUI（方舟UI框架）/C API/头文件/native_node.h/capi-native-node-h.md#arkui_nodeattributetype>)）
* 针对PC/2in1设备的窗口能力新增支持更改子窗口所属的父窗口。（[API参考](<../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS API/窗口管理/@ohos.window (窗口)/Interface (Window)/arkts-apis-window-window.md#setparentwindow19>)）
* 屏幕属性新增屏幕显示内容的显示模式枚举。该枚举在屏幕实例中传递。（[API参考](<../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS API/屏幕管理/@ohos.display (屏幕属性)/js-apis-display.md#displaysourcemode19>)）

## Performance Analysis Kit

* HiTraceMeter新增一批API，增强了HiTraceMeter的打点能力和日志能力。（[指南](<../../../../../harmonyos-guides/系统/调测调优/Performance Analysis Kit（性能分析服务）/性能跟踪/hitracemeter.md>)）
* hitrace命令新增支持“--trace\_level”参数，用于设置trace输出级别的阈值。（[指南](../../../../../harmonyos-guides/系统/调测调优/调试命令/hitrace/hitrace.md)）

## Camera Kit

新增支持查询和使用相机微距的能力。（[API参考](<../../../../../harmonyos-references/Camera Kit（相机服务）/ArkTS API/@ohos.multimedia.camera (相机管理)/Interface (Macro)/arkts-apis-camera-macro.md>)）

## CANN Kit

支持AscendC算子开发，可实现对NPU的编程。（[指南](<../../../../../harmonyos-guides/AI/CANN Kit（CANN异构计算框架服务）/AscendC算子开发/cannkit-ascendc-operator-development.md>)）

## Core Speech Kit

文本转语音能力新增支持音色下载。（[API参考](<../../../../../harmonyos-references/Core Speech Kit（基础语音服务）/ArkTS API/textToSpeech（文本转语音）/hms-ai-texttospeech.md#texttospeechdownloadvoice>)）

## Device Security Kit

新增支持获取诈骗应用信息。（[指南](<../../../../../harmonyos-guides/系统/安全/Device Security Kit（设备安全服务）/反诈选择器/获取诈骗应用/devicesecurity-selectfraudapp.md>)、[API参考](<../../../../../harmonyos-references/安全/Device Security Kit（设备安全服务）/ArkTS API/AntifraudPicker（反诈选择器）/devicesecurity-antifraudpicker-api.md#selectfraudapp>)）

## Enterprise Data Guard Kit

* 新增支持只写模式打开[用户数据目录](<../../../../../harmonyos-guides/系统/安全/Enterprise Data Guard Kit（企业数据保护服务）/Enterprise Data Guard Kit简介/dataguard-introduction.md#访问限制>)下的文件。（[API参考](<../../../../../harmonyos-references/安全/Enterprise Data Guard Kit（企业数据保护服务）/ArkTS API/fileGuard (文件分级管控)/dataguard-fileguard.md#openfilewrite>)）
* 新增支持设置文件自定义属性标签，方便应用对管控文件进行标识、分类。（[API参考](<../../../../../harmonyos-references/安全/Enterprise Data Guard Kit（企业数据保护服务）/ArkTS API/fileGuard (文件分级管控)/dataguard-fileguard.md#setfilecustomtag>)）

## Graphics Accelerate Kit

新增支持应用通过自身下载器下载资源包。（[指南](<../../../../../harmonyos-guides/图形/Graphics Accelerate Kit（图形加速服务）/游戏资源加速服务/资源包后台下载/系统后台下载资源包/extension协同下载/graphics-accelerate-assetdownload-back-self.md>)、[API参考](<../../../../../harmonyos-references/Graphics Accelerate Kit（图形加速服务）/ArkTS API/assetDownloadManager（资源包下载管理）/graphics-accelerate-assetdownloadmanager.md#appdownloadstatus>)）

## Health Service Kit

新增支持在Wearable设备中调用该Kit的能力。（[指南](<../../../../../harmonyos-guides/应用服务/Health Service Kit（运动健康服务）/开发接入/Wearable应用开发/health-wearable-app-dev.md>)）

## Map Kit

* 新增控制mark文字显隐能力。（[指南](<../../../../../harmonyos-guides/应用服务/Map Kit（地图服务）/在地图上绘制/标记/map-marker.md#控制marker文字显隐>)、[API参考](<../../../../../harmonyos-references/Map Kit（地图服务）/ArkTS API/map（地图显示功能）/Interface (Marker)/map-map-marker.md#setannotationvisible>)）
* 新增支持地图logo顶部居中和底部居中两个布局位置。（[API参考](<../../../../../harmonyos-references/Map Kit（地图服务）/ArkTS API/mapCommon（地图属性模型）/map-common.md#logoalignment>)）
* 新增公交交通规划能力。（[指南](<../../../../../harmonyos-guides/应用服务/Map Kit（地图服务）/路径规划/出行路线规划/map-navi-routes.md#公共交通规划>)、[API参考](<../../../../../harmonyos-references/Map Kit（地图服务）/ArkTS API/navi（路径规划）/map-navi-api.md#gettransitroutes>)）
* 新增地图比例尺支持公英制切换能力。（[指南](<../../../../../harmonyos-guides/应用服务/Map Kit（地图服务）/创建地图/显示地图/map-presenting.md#设置地图属性>)、[API参考](<../../../../../harmonyos-references/Map Kit（地图服务）/ArkTS API/mapCommon（地图属性模型）/map-common.md#scaleunit>)）
* 新增室内图功能，提供室内地图和楼层选择的能力。（[指南](<../../../../../harmonyos-guides/应用服务/Map Kit（地图服务）/创建地图/显示地图/map-presenting.md#室内图>)、[API参考](<../../../../../harmonyos-references/Map Kit（地图服务）/ArkTS API/map（地图显示功能）/Class (MapComponentController)/map-map-mapcomponentcontroller.md#setindoormapenabled>)）

## MDM Kit

新增支持设置Wi-Fi黑名单、白名单能力。（[API参考](<../../../../../harmonyos-references/基础功能/MDM Kit（企业设备管理服务）/ArkTS API/@ohos.enterprise.wifiManager（Wi-Fi管理）/js-apis-enterprise-wifimanager.md#wifimanageraddallowedwifilist19>)）

## Payment Kit

* 新增支持实名信息验证、实名信息授权。（[指南](<../../../../../harmonyos-guides/应用服务/Payment Kit（鸿蒙支付服务）/用户身份验证服务/实名信息验证授权场景/payment-real-name-verification.md>)）
* 新增支持人脸核身实人验证。（[指南](<../../../../../harmonyos-guides/应用服务/Payment Kit（鸿蒙支付服务）/用户身份验证服务/人脸核身实人验证场景/payment-real-name-face-verification.md>)）

## Pen kit

新增支持应用监听手写笔双击/轻捏事件。（[API参考](<../../../../../harmonyos-references/硬件/Pen Kit（手写笔服务）/ArkTS API/stylusInteraction (手写笔交互功能)/pen-stylusinteraction.md>)）

## Scan Kit

码图生成能力新增支持2in1设备。（[指南](<../../../../../harmonyos-guides/媒体/Scan Kit（统一扫码服务）/Scan Kit简介/scan-introduction.md#支持的设备>)）

## Vision Kit

新增支持在未完成卡证识别退出的场景下，返回结果码信息。（[API参考](<../../../../../harmonyos-references/Vision Kit（场景化视觉服务）/ArkTS组件/CardRecognition（卡证识别控件）/vision-card-recognition.md#cardrecognition>)）

## UI Design Kit

新增支持应用注册加载自定义Symbol能力。（[指南](<../../../../../harmonyos-guides/应用框架/UI Design Kit（UI设计套件）/应用加载自定义Symbol/ui-design-custom-symbol-res-register.md>)、[API参考](<../../../../../harmonyos-references/UI Design Kit（UI设计套件）/ArkTS API/symbolRegister/ui-design-symbolregister.md>)）

## 其他

从5.1.1(19) Release开始，支持TV设备的应用开发。除通用的底座基础能力外，涉及对TV设备提供支持的Kit包括但不限于：

AppGallery Kit、CANN Kit、Cloud Foundation Kit、Game Service Kit、IAP Kit、NearLink Kit、Push Kit、Remote Communication Kit、Scan Kit、Scenario Fusion Kit、Service Collaboration Kit、Share Kit、UI Design Kit、XEngine Kit
