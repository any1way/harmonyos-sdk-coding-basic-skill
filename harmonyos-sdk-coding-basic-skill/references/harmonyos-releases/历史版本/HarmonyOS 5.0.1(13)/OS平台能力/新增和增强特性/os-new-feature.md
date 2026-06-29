---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/os-new-feature
title: 新增和增强特性
breadcrumb: 版本说明 > 历史版本 > HarmonyOS 5.0.1(13) > OS平台能力 > 新增和增强特性
category: harmonyos-releases
scraped_at: 2026-06-01T10:50:12+08:00
doc_updated_at: 2026-05-25
content_hash: sha256:dd205229a4837b98e9fe5942525561353bc8083343bd1d9b1bedf7f2a7964ece
---
## Ability Kit

* 支持PC/2in1设备创建Native子进程，并传递参数到子进程。（[指南](<../../../../../harmonyos-guides/应用框架/Ability Kit（程序框架服务）/Native子进程开发指导/创建终止Native子进程（CC++）/capi-nativechildprocess-development-guideline.md>)）
* 包管理新增定义ElementName的C API。（[API参考](<../../../../../harmonyos-references/Ability Kit（程序框架服务）/C API/结构体/OH_NativeBundle_ElementName/capi-native-bundle-oh-nativebundle-elementname.md>)）
* 元能力新增C API，提供从ApplicationContext中获取cache路径、Area以及bundleName的能力。（[API参考](<../../../../../harmonyos-references/Ability Kit（程序框架服务）/C API/头文件/application_context.h/capi-application-context-h.md>)）

## ArkData

Preferences部件提供C API。（[指南](<../../../../../harmonyos-guides/应用框架/ArkData（方舟数据管理）/应用数据持久化/通过用户首选项实现数据持久化 (CC++)/preferences-guidelines.md>)、[API参考](<../../../../../harmonyos-references/ArkData（方舟数据管理）/C API/模块/Preferences/capi-preferences.md>)）

## ArkUI

* RichEditor支持配置滚动条的显隐。（[API参考](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/文本与输入/RichEditor/ts-basic-components-richeditor.md#barstate13)）
* 通过XComponent接入的三方平台支持无障碍能力。（[API参考](<../../../../../harmonyos-references/ArkUI（方舟UI框架）/C API/头文件/native_interface_accessibility.h/capi-native-interface-accessibility-h.md>)、[指南](<../../../../../harmonyos-guides/应用框架/ArkUI（方舟UI框架）/UI开发 (基于NDK构建UI)/通过自绘制接入无障碍/ndk-accessibility-xcomponent.md>)）
* 支持使用ComponentContent类型参数设置ListItemGroup的头部和尾部组件。（[API参考](<../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS API/UI界面/arkui/ComponentContent/js-apis-arkui-componentcontent.md>)）
* 新增支持获取和设置当前窗口是否禁用返回手势的功能，该功能仅在主窗口全屏模式下生效。（[API参考](<../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS API/窗口管理/@ohos.window (窗口)/Interface (Window)/arkts-apis-window-window.md#setgesturebackenabled13>)）

## ArkWeb

* 支持获取资源响应数据和响应数据的准备状态。（[API参考](<../../../../../harmonyos-references/ArkWeb（方舟Web）/ArkTS 组件/Web/Class (WebResourceResponse)/arkts-basic-components-web-webresourceresponse.md#getresponsedataex13>)）
* 支持获取网页当前的滚动偏移量。（[API参考](<../../../../../harmonyos-references/ArkWeb（方舟Web）/ArkTS API/@ohos.web.webview (Webview)/Class (WebviewController)/arkts-apis-webview-webviewcontroller.md#getscrolloffset13>)）

## AVSession Kit

媒体播控模块提供C API。（[指南](<../../../../../harmonyos-guides/媒体/AVSession Kit（音视频播控服务）/本地媒体会话/媒体会话提供方(CC++)/using-ohavsession-developer.md>)）

## Background Tasks Kit

* 短时任务提供C API。（[指南](<../../../../../harmonyos-guides/应用框架/Background Tasks Kit（后台任务开发服务）/短时任务(CC++)/native-transient-task.md>)、[API参考](<../../../../../harmonyos-references/Background Tasks Kit（后台任务开发服务）/C API/模块/TransientTask/capi-transienttask.md>)）
* 新增音视频通话长时任务类型的定义。（[API参考](<../../../../../harmonyos-references/Background Tasks Kit（后台任务开发服务）/ArkTS API/@ohos.resourceschedule.backgroundTaskManager (后台任务管理)/js-apis-resourceschedule-backgroundtaskmanager.md#backgroundmode>)）

## Basic Services Kit

* 剪贴板模块提供C API。（[API参考](<../../../../../harmonyos-references/基础功能/Basic Services Kit（基础服务）/C API/头文件/oh_pasteboard.h/capi-oh-pasteboard-h.md>)）
* 打印服务模块新增C API。（[API参考](<../../../../../harmonyos-references/基础功能/Basic Services Kit（基础服务）/C API/模块/OH_Print/capi-oh-print.md>)）
* 电源管理模块新增C API。（[API参考](<../../../../../harmonyos-references/基础功能/Basic Services Kit（基础服务）/C API/模块/OH_BatteryInfo/capi-oh-batteryinfo.md>)）

## Camera Kit

优化相机预览流的处理机制，增加对stride值的处理。详见[双路预览（ArkTS）](<../../../../../harmonyos-guides/媒体/Camera Kit（相机服务）/开发相机应用基础能力(ArkTS)/双路预览(ArkTS)/camera-dual-channel-preview.md>)或[预览流二次处理（C/C++）](<../../../../../harmonyos-guides/媒体/Camera Kit（相机服务）/开发相机应用基础能力(CC++)/预览流二次处理(CC++)/native-camera-preview-imagereceiver.md>)。

## Connectivity Kit

* 支持通过C API获取蓝牙开关的状态。（[API参考](<../../../../../harmonyos-references/网络/Connectivity Kit（短距通信服务）/C API/模块/Bluetooth/capi-bluetooth.md>)）
* 支持通过C API获取Wi-Fi开关的状态。（[API参考](<../../../../../harmonyos-references/网络/Connectivity Kit（短距通信服务）/C API/模块/Wifi/capi-wifi.md>)）

## Core File Kit

文件共享fileuri模块新增C API。（[指南](<../../../../../harmonyos-guides/应用框架/Core File Kit（文件基础服务）/用户文件/FileUri开发指导(CC++)/native-fileuri-guidelines.md>)、[API参考](<../../../../../harmonyos-references/Core File Kit（文件基础服务）/C API/头文件/oh_file_uri.h/capi-oh-file-uri-h.md#oh_fileuri_getfilename>)）

## Device Security Kit

* 支持通过C API查询设备安全模式。（[API参考](<../../../../../harmonyos-references/安全/Device Security Kit（设备安全服务）/C API/模块/DeviceSecurityMode/devicesecurity-capi-devicesecuritymode.md>)）
* 支持通过C API为请求设置二进制数据接收回调。（[API参考](<../../../../../harmonyos-references/网络/Remote Communication Kit（远场通信服务）/C API/模块/RemoteCommunication/remote-communication-overview.md#hms_rcp_setrequestonbinarydatarecvcallback>)）

## Game Service Kit

游戏场景感知支持按需订阅设备状态变化和查询设备状态信息。（[API参考-订阅设备状态](<../../../../../harmonyos-references/Game Service Kit（游戏服务）/ArkTS API/gamePerformance (游戏场景感知)/gameservice-gameperformance.md#gameperformanceondevicestatechanged-1>)、[API参考-查询设备状态](<../../../../../harmonyos-references/Game Service Kit（游戏服务）/ArkTS API/gamePerformance (游戏场景感知)/gameservice-gameperformance.md#gameperformancegetdeviceinfobyscope>)）

## Image Kit

支持通过C API从PixelMap中读取ARGB格式的数据。（[API参考](<../../../../../harmonyos-references/Image Kit（图片处理服务）/C API/头文件/pixelmap_native.h/capi-pixelmap-native-h.md#oh_pixelmapnative_getargbpixels>)）

## Input Kit

多模输入能力新增一批C API。（[API参考](<../../../../../harmonyos-references/基础功能/Input Kit（多模输入服务）/C API/模块/input/capi-input.md>)）

## Location Kit

地理位置模块提供C API。（[API参考](<../../../../../harmonyos-references/Location Kit（位置服务）/C API/模块/Location/capi-location.md>)）

## Map Kit

支持设置地图经纬度范围和4个方向与边界之间的距离。（[API参考](<../../../../../harmonyos-references/Map Kit（地图服务）/ArkTS API/map（地图显示功能）/Functions/map-map-functions.md#newlatlngbounds-2>)）

## Media Library Kit

PhotoViewPicker能力增强：

* PickerOptions新增是否支持滑动多选的选项和设置大图页checkbox的位置的选项。（[API参考](<../../../../../harmonyos-references/Media Library Kit（媒体文件管理服务）/ArkTS组件/@ohos.file.PhotoPickerComponent (PhotoPicker组件)/ohos-file-photopickercomponent.md#pickeroptions>)）
* 新增向picker发送退出大图的通知的API。（[API参考](<../../../../../harmonyos-references/Media Library Kit（媒体文件管理服务）/ArkTS组件/@ohos.file.PhotoPickerComponent (PhotoPicker组件)/ohos-file-photopickercomponent.md#exitphotobrowser13>)）
* 新增设置大图页大图预览组件外其他UI元素是否可见的API。（[API参考](<../../../../../harmonyos-references/Media Library Kit（媒体文件管理服务）/ArkTS组件/@ohos.file.PhotoPickerComponent (PhotoPicker组件)/ohos-file-photopickercomponent.md#setphotobrowseruielementvisibility13>)）
* 新增定义大图页大图预览组件外其他UI元素的API。（[API参考](<../../../../../harmonyos-references/Media Library Kit（媒体文件管理服务）/ArkTS组件/@ohos.file.PhotoPickerComponent (PhotoPicker组件)/ohos-file-photopickercomponent.md#photobrowseruielement13>)）
* 支持PhotoPicker组件的删除通知等相关能力。（[API参考](<../../../../../harmonyos-references/Media Library Kit（媒体文件管理服务）/ArkTS组件/@ohos.file.PhotoPickerComponent (PhotoPicker组件)/ohos-file-photopickercomponent.md#itemsdeletedcallback13>)）

## NearLink Kit

【新增Kit】NearLink Kit（星闪服务）提供一种低功耗、高速率的短距离通信服务，支持星闪设备之间的连接、数据交互。

中心设备可以通过扫描发现外围设备，并发起连接。外围设备可以通过发送广播的方式被中心设备发现，和中心设备连接之后可以进行相应的数据传输。

详细信息请参见[NearLink Kit开发指南](<../../../../../harmonyos-guides/系统/网络/NearLink Kit（星闪服务）/NearLink Kit简介/nearlink-introduction.md>)。

## Notification Kit

通知服务新增C API。（[API参考](<../../../../../harmonyos-references/Notification Kit（用户通知服务）/C API/模块/NOTIFICATION/capi-notification.md>)）

## Payment Kit

新增数字人民币的接口。（[API参考](<../../../../../harmonyos-references/Payment Kit（鸿蒙支付服务）/ArkTS API/ecnyPaymentService (数字人民币服务)/payment-ecnypaymentservice.md>)）

## Remote Communication Kit

支持URPC场景下远程RPC调用能力。（[指南](<../../../../../harmonyos-guides/系统/网络/Remote Communication Kit（远场通信服务）/URPC场景/使用URPC进行远程程序调用/remote-communication-urpccall.md>)、[API参考](<../../../../../harmonyos-references/网络/Remote Communication Kit（远场通信服务）/ArkTS API/urpc（高性能rpc通信库）/remote-communication-urpcapi.md>)）

## Scan Kit

在默认界面扫码界面，支持用户点击关闭“隐私横幅”。当重新打开应用的默认界面扫码将只显示安全访问提示，3s后消失。（[指南](<../../../../../harmonyos-guides/媒体/Scan Kit（统一扫码服务）/默认界面扫码/scan-scanbarcode.md#业务流程>)）

## Sensor Service Kit

传感器模块新增游戏及线性加速度传感器的C API，其中枚举类型Sensor\_Type新增SENSOR\_TYPE\_ACCELEROMETER参数（[API参考-Sensor\_Type](<../../../../../harmonyos-references/硬件/Sensor Service Kit（传感器服务）/C API/头文件/oh_sensor_type.h/capi-oh-sensor-type-h.md#sensor_type>)），函数OH\_SensorEvent\_GetData(Sensor\_Event\* sensorEvent, float \*\*data, uint32\_t \*length)入参的传感器类型新增SENSOR\_TYPE\_LINEAR\_ACCELERATION（[API参考](<../../../../../harmonyos-references/硬件/Sensor Service Kit（传感器服务）/C API/头文件/oh_sensor.h/capi-oh-sensor-h.md#函数>)）。

## Telephony Kit

蜂窝网络模块提供C API。（[API参考-蜂窝数据](<../../../../../harmonyos-references/网络/Telephony Kit（蜂窝通信服务）/C API/头文件/telephony_data.h/capi-telephony-data-h.md>)、[API参考-网络搜索](<../../../../../harmonyos-references/网络/Telephony Kit（蜂窝通信服务）/C API/头文件/telephony_radio.h/capi-telephony-radio-h.md>)）

## Vision Kit

在AI识图场景下，支持设置图像分割菜单显示状态（[API参考](<../../../../../harmonyos-references/Vision Kit（场景化视觉服务）/ArkTS API/visionImageAnalyzer（AI识图控件）/vision-image-analyzer.md#setsubjectmenuvisibility>)）以及开启与取消监听图片搜索事件（[API参考-开启](<../../../../../harmonyos-references/Vision Kit（场景化视觉服务）/ArkTS API/visionImageAnalyzer（AI识图控件）/vision-image-analyzer.md#ontype-objectsearchpanelvisibilitychange>)、[API参考-取消](<../../../../../harmonyos-references/Vision Kit（场景化视觉服务）/ArkTS API/visionImageAnalyzer（AI识图控件）/vision-image-analyzer.md#offtype-objectsearchpanelvisibilitychange>)）。

## XEngine Kit

支持时域AI超分能力，即利用相机抖动获取不同位置的采样信息，融合时域实现超采样率和超分辨率功能，并利用神经网络达到抗锯齿效果。（[指南](<../../../../../harmonyos-guides/图形/XEngine Kit（GPU加速引擎服务）/时域AI超分/xengine-kit-ai-temporal-upscaling.md>)）

## Audio Kit

新增支持麦克风状态检测的ArkTS和C API，可查询并监听在使用麦克风录音时，麦克风是否被堵塞。（[API参考](<../../../../../harmonyos-references/Audio Kit（音频服务）/C API/头文件/native_audio_routing_manager.h/capi-native-audio-routing-manager-h.md#oh_audioroutingmanager_setmicblockstatuscallback>)）
