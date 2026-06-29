---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/os-new-feature-611
title: OS新增和增强特性
breadcrumb: 版本说明 > HarmonyOS 6.1.1(24) > OS平台能力 > OS新增和增强特性
category: harmonyos-releases
scraped_at: 2026-06-01T10:38:34+08:00
doc_updated_at: 2026-05-26
content_hash: sha256:60e7a8c36527284760b02a9f494cdcba7fd77df193e6f8c619df7424b0ae9957
---
## 6.1.1(24) Release新增和增强特性

### Ability Kit

AbilityStage组件管理器新增AbilityStage即将创建第一个Ability的回调（[API参考](<../../../../harmonyos-references/Ability Kit（程序框架服务）/ArkTS API/Stage模型能力的接口/@ohos.app.ability.AbilityStage (AbilityStage组件管理器)/js-apis-app-ability-abilitystage.md#onabouttocreateability24>)），以及当进程从应用快照启动时的回调（[API参考](<../../../../harmonyos-references/Ability Kit（程序框架服务）/ArkTS API/Stage模型能力的接口/@ohos.app.ability.AbilityStage (AbilityStage组件管理器)/js-apis-app-ability-abilitystage.md#onlaunchfromhypersnap24>)）。

### ArkTS

* 新增enableLocalHandleDetection接口，保证EventHandler和libuv机制的任务在scope范围内执行，从而避免内存泄漏。（[API参考](<../../../../harmonyos-references/ArkTS（方舟编程语言）/ArkTS API/@ohos.util (util工具函数)/js-apis-util.md#enablelocalhandledetection24>)）
* XML解析新增支持XmlSAXHandler，定义了SAX解析xml文本时的回调方法。开发者需要实现这些回调方法来处理xml文本的不同部分。这些回调方法会在xml解析过程的对应时机触发。（[API参考](<../../../../harmonyos-references/ArkTS（方舟编程语言）/ArkTS API/@ohos.xml (XML解析与生成)/js-apis-xml.md#xmlsaxhandler24>)）

### ArkWeb

在下载任务完成的回调中，新增支持获取下载项的原始URL地址（[API参考](<../../../../harmonyos-references/ArkWeb（方舟Web）/ArkTS API/@ohos.web.webview (Webview)/Class (WebDownloadItem)/arkts-apis-webview-webdownloaditem.md#getoriginalurl24>)）；新增支持获取引用页的URL地址（[API参考](<../../../../harmonyos-references/ArkWeb（方舟Web）/ArkTS API/@ohos.web.webview (Webview)/Class (WebDownloadItem)/arkts-apis-webview-webdownloaditem.md#getreferrerurl24>)）。

### Call Service Kit

在企业员工来电或去电时，开发者可通过来电、去电手机号查询获取对应的企业服务信息，帮助员工快速了解通话号码相关的企业服务数据，目前支持快递类型的企业服务。（[指南](<../../../../harmonyos-guides/应用服务/Call Service Kit（通话服务）/企业服务信息来去电页面显示/callservice-enterprise-sersvice-display.md>)、[API参考](<../../../../harmonyos-references/Call Service Kit（通话服务）/ArkTS API/CallerInfoQueryExtensionAbility (来去电信息查询扩展Ability)/callservicekit-callerinfoquery-extension-ability.md#onquerybusinessservicedata>)）

### Camera Kit

新增一批拍照/录像模式下的相机专业能力，包括：

* 新增支持订阅（[ArkTS API参考](<../../../../harmonyos-references/Camera Kit（相机服务）/ArkTS API/@ohos.multimedia.camera (相机管理)/Interface (Flash)/arkts-apis-camera-flash.md#onflashstatechange24>)、[C API参考](<../../../../harmonyos-references/Camera Kit（相机服务）/C API/头文件/capture_session.h/capi-capture-session-h.md#oh_capturesession_registerflashstatechangecallback>)）/取消订阅（[ArkTS API参考](<../../../../harmonyos-references/Camera Kit（相机服务）/ArkTS API/@ohos.multimedia.camera (相机管理)/Interface (Flash)/arkts-apis-camera-flash.md#offflashstatechange24>)、[C API参考](<../../../../harmonyos-references/Camera Kit（相机服务）/C API/头文件/capture_session.h/capi-capture-session-h.md#oh_capturesession_unregisterflashstatechangecallback>)）闪光灯状态变化事件回调。
* 新增光学防抖（OIS）相关参数的查询和设置能力。包括查询和设置OIS模式、获取和设置各轴向偏移量信息。
  + ArkTS API参考[Interface (OIS)](<../../../../harmonyos-references/Camera Kit（相机服务）/ArkTS API/@ohos.multimedia.camera (相机管理)/Interface (OIS)/arkts-apis-camera-ois.md>)和[Interface (OISQuery)](<../../../../harmonyos-references/Camera Kit（相机服务）/ArkTS API/@ohos.multimedia.camera (相机管理)/Interface (OISQuery)/arkts-apis-camera-oisquery.md>)。
  + C API参考可在[capture\_session.h](<../../../../harmonyos-references/Camera Kit（相机服务）/C API/头文件/capture_session.h/capi-capture-session-h.md#oh_capturesession_setoismodecustom>)页面搜索关键字“OIS”。
* 相机设备定义中新增多个细节信息，包括镜头焦距、等效焦距、最小对焦距离、镜头畸变参数、内参标定参数、传感器的物理尺寸、传感器的像素阵列大小、传感器的滤色阵列排列方式。同时支持管理逻辑摄像头：
  + ArkTS API参考可在[CameraDevice参数定义](<../../../../harmonyos-references/Camera Kit（相机服务）/ArkTS API/@ohos.multimedia.camera (相机管理)/Interfaces (其他)/arkts-apis-camera-i.md#cameradevice>)中搜索对应关键字。
  + C API参考可在[capture\_session.h](<../../../../harmonyos-references/Camera Kit（相机服务）/C API/头文件/capture_session.h/capi-capture-session-h.md#oh_capturesession_setoismodecustom>)页面搜索对应关键字。
* 相机设备定义中新增支持管理逻辑摄像头的能力：
  + ArkTS API参考见[CameraDevice参数定义](<../../../../harmonyos-references/Camera Kit（相机服务）/ArkTS API/@ohos.multimedia.camera (相机管理)/Interfaces (其他)/arkts-apis-camera-i.md#cameradevice>)，支持通过isLogicalCamera参数查询是否为逻辑摄像头，并通过constituentCameraDevices参数定义组成此逻辑相机的物理相机列表。
  + C API支持[查询是否为逻辑摄像头](<../../../../harmonyos-references/Camera Kit（相机服务）/C API/头文件/camera_device.h/capi-camera-device-h.md#oh_cameradevice_islogicalcamera>)、[查询逻辑摄像头包含的所有物理摄像头](<../../../../harmonyos-references/Camera Kit（相机服务）/C API/头文件/camera_device.h/capi-camera-device-h.md#oh_cameradevice_getlogicalcameraconstituentcameradevices>)、[删除组成逻辑摄像头的所有物理摄像头](<../../../../harmonyos-references/Camera Kit（相机服务）/C API/头文件/camera_device.h/capi-camera-device-h.md#oh_cameradevice_deleteconstituentcameradevices>)。
* 相机曝光设置增强：
  + ArkTS API新增自动曝光类，支持自动曝光操作（[API参考](<../../../../harmonyos-references/Camera Kit（相机服务）/ArkTS API/@ohos.multimedia.camera (相机管理)/Interface (AutoExposure)/arkts-apis-camera-autoexposure.md>)）；新增手动曝光设置（[API参考](<../../../../harmonyos-references/Camera Kit（相机服务）/ArkTS API/@ohos.multimedia.camera (相机管理)/Interface (ManualExposure)/arkts-apis-camera-manualexposure.md>)）和手动曝光对象的查询（[API参考](<../../../../harmonyos-references/Camera Kit（相机服务）/ArkTS API/@ohos.multimedia.camera (相机管理)/Interface (ManualExposureQuery)/arkts-apis-camera-manualexposurequery.md>)）。
  + C API新增支持曝光操作的原子能力，包括查询指定曝光测光模式是否支持（[API参考](<../../../../harmonyos-references/Camera Kit（相机服务）/C API/头文件/capture_session.h/capi-capture-session-h.md#oh_capturesession_isexposuremeteringmodesupported>)）、获取当前曝光测光模式（[API参考](<../../../../harmonyos-references/Camera Kit（相机服务）/C API/头文件/capture_session.h/capi-capture-session-h.md#oh_capturesession_getexposuremeteringmode>)）、设置曝光测光模式（[API参考](<../../../../harmonyos-references/Camera Kit（相机服务）/C API/头文件/capture_session.h/capi-capture-session-h.md#oh_capturesession_setexposuremeteringmode>)）、获取支持的曝光时间范围（[API参考](<../../../../harmonyos-references/Camera Kit（相机服务）/C API/头文件/capture_session.h/capi-capture-session-h.md#oh_capturesession_getsupportedexposuredurationrange>)）、设置曝光时间（[API参考](<../../../../harmonyos-references/Camera Kit（相机服务）/C API/头文件/capture_session.h/capi-capture-session-h.md#oh_capturesession_setexposureduration>)）、获取当前曝光时间（[API参考](<../../../../harmonyos-references/Camera Kit（相机服务）/C API/头文件/capture_session.h/capi-capture-session-h.md#oh_capturesession_getexposureduration>)）、捕获会话曝光时间变更回调（[API参考](<../../../../harmonyos-references/Camera Kit（相机服务）/C API/头文件/capture_session.h/capi-capture-session-h.md#oh_capturesession_onexposuredurationchange>)）、注册曝光信息变更事件回调（[API参考](<../../../../harmonyos-references/Camera Kit（相机服务）/C API/头文件/capture_session.h/capi-capture-session-h.md#oh_capturesession_registerexposureinfochangecallback>)）、注销曝光信息变更回调（[API参考](<../../../../harmonyos-references/Camera Kit（相机服务）/C API/头文件/capture_session.h/capi-capture-session-h.md#oh_capturesession_unregisterexposureinfochangecallback>)）。
* 新增手动对焦相关能力：
  + ArkTS API新增手动对焦对象定义（[API参考](<../../../../harmonyos-references/Camera Kit（相机服务）/ArkTS API/@ohos.multimedia.camera (相机管理)/Interface (ManualFocus)/arkts-apis-camera-manualfocus.md>)）和手动对焦对象的查询能力（[API参考](<../../../../harmonyos-references/Camera Kit（相机服务）/ArkTS API/@ohos.multimedia.camera (相机管理)/Interface (ManualFocusQuery)/arkts-apis-camera-manualfocusquery.md>)）。
  + C API新增支持查询是否支持对焦距离设置（[API参考](<../../../../harmonyos-references/Camera Kit（相机服务）/C API/头文件/capture_session.h/capi-capture-session-h.md#oh_capturesession_isfocusdistancesupported>)）、获取当前对焦距离（[API参考](<../../../../harmonyos-references/Camera Kit（相机服务）/C API/头文件/capture_session.h/capi-capture-session-h.md#oh_capturesession_getfocusdistance>)）以及设置对焦距离（[API参考](<../../../../harmonyos-references/Camera Kit（相机服务）/C API/头文件/capture_session.h/capi-capture-session-h.md#oh_capturesession_setfocusdistance>)）。
* 新增手动设置ISO感光度的相关能力：
  + ArkTS API新增手动ISO对象定义（[API参考](<../../../../harmonyos-references/Camera Kit（相机服务）/ArkTS API/@ohos.multimedia.camera (相机管理)/Interface (ManualIso)/arkts-apis-camera-manualiso.md>)）和手动ISO对象的查询能力（[API参考](<../../../../harmonyos-references/Camera Kit（相机服务）/ArkTS API/@ohos.multimedia.camera (相机管理)/Interface (ManualIsoQuery)/arkts-apis-camera-manualisoquery.md>)）。
  + C API新增支持查询ISO感光度范围（[API参考](<../../../../harmonyos-references/Camera Kit（相机服务）/C API/头文件/capture_session.h/capi-capture-session-h.md#oh_capturesession_getsupportedisorange>)）、获取当前ISO感光度值（[API参考](<../../../../harmonyos-references/Camera Kit（相机服务）/C API/头文件/capture_session.h/capi-capture-session-h.md#oh_capturesession_getiso>)）以及设置ISO感光度值（[API参考](<../../../../harmonyos-references/Camera Kit（相机服务）/C API/头文件/capture_session.h/capi-capture-session-h.md#oh_capturesession_setiso>)）。
* 新增手动设置物理光圈的相关能力：
  + ArkTS API新增物理光圈对象定义（[API参考](<../../../../harmonyos-references/Camera Kit（相机服务）/ArkTS API/@ohos.multimedia.camera (相机管理)/Interface (Aperture)/arkts-apis-camera-aperture.md>)）和物理光圈对象的查询能力（[API参考](<../../../../harmonyos-references/Camera Kit（相机服务）/ArkTS API/@ohos.multimedia.camera (相机管理)/Interface (ApertureQuery)/arkts-apis-camera-aperturequery.md>)）。
  + C API新增支持获取当前物理光圈值（[API参考](<../../../../harmonyos-references/Camera Kit（相机服务）/C API/头文件/capture_session.h/capi-capture-session-h.md#oh_capturesession_getphysicalaperture>)）、设置物理光圈值（[API参考](<../../../../harmonyos-references/Camera Kit（相机服务）/C API/头文件/capture_session.h/capi-capture-session-h.md#oh_capturesession_setphysicalaperture>)）、获取支持的物理光圈列表（[API参考](<../../../../harmonyos-references/Camera Kit（相机服务）/C API/头文件/capture_session.h/capi-capture-session-h.md#oh_capturesession_getsupportedphysicalapertures>)）以及删除支持的物理光圈列表（[API参考](<../../../../harmonyos-references/Camera Kit（相机服务）/C API/头文件/capture_session.h/capi-capture-session-h.md#oh_capturesession_deletephysicalapertures>)）。

### CANN Kit

针对PC设备开放大语言模型推理API，新增支持接入大语言模型，实现计算链路的加速封装和计算加速。（[指南](<../../../../harmonyos-guides/AI/CANN Kit（CANN异构计算框架服务）/LLM大模型能力开放/简介/cannkit-llm-summary.md>)）

### MDM Kit

设备设置管理支持对当前用户下被隐藏的设置项列表进行添加、删除、查询操作。（[API参考](<../../../../harmonyos-references/基础功能/MDM Kit（企业设备管理服务）/ArkTS API/@ohos.enterprise.deviceSettings （设备设置管理）/js-apis-enterprise-devicesettings.md#devicesettingsaddhiddensettingsmenu24>)）

## 6.1.1(24) Beta1新增和增强特性

### Ability Kit

* Ability上次退出的信息字段新增支持获取退出原因。（[API参考](<../../../../harmonyos-references/Ability Kit（程序框架服务）/ArkTS API/Stage模型能力的接口/@ohos.app.ability.AbilityConstant (Ability相关常量)/js-apis-app-ability-abilityconstant.md#lastexitdetailinfo18>)）
* AbilityStage上下文新增launchElement字段，用于在AbilityStage调用onCreate时告知应用正在加载的Ability，从而动态加载资源。（[API参考](<../../../../harmonyos-references/Ability Kit（程序框架服务）/ArkTS API/接口依赖的元素及定义/application/AbilityStageContext/js-apis-inner-application-abilitystagecontext.md#属性>)）

### AppGallery Kit

新增支持查询、删除应用内快捷方式的能力，支持用户查看、管理应用的桌面快捷方式。（[指南](<../../../../harmonyos-guides/应用服务/AppGallery Kit（应用市场服务）/应用市场推荐/应用内快捷方式/查询应用内快捷方式/appgallery-productview-getshortcut.md>)、[API参考](<../../../../harmonyos-references/AppGallery Kit（应用市场服务）/ArkTS API/productViewManager (应用市场推荐)/store-productviewmanager.md#productviewmanagergetpinshortcutinfos>)）

### ArkData

* 新增创建或打开已有的关系型数据库的同步方法。同步方法可阻塞线程直到获取到RdbStore。（[API参考](<../../../../harmonyos-references/ArkData（方舟数据管理）/ArkTS API/@ohos.data.relationalStore (关系型数据库)/Functions/arkts-apis-data-relationalstore-f.md#relationalstoregetrdbstoresync24>)）

### ArkGraphics 2D

* 新增支持为组件内容添加HDR（高动态范围成像）提亮效果。（[API参考](<../../../../harmonyos-references/ArkGraphics 2D（方舟2D图形服务）/ArkTS API/@ohos.graphics.uiEffect (效果级联)/js-apis-uieffect.md#hdrbrightnessratio24>)）
* 新增支持视频的AIHDR格式。（[API参考](<../../../../harmonyos-references/ArkGraphics 2D（方舟2D图形服务）/ArkTS API/@ohos.graphics.hdrCapability (HDR能力)/js-apis-hdrcapability.md#hdrformat>)）

### ArkTS

* 虚拟机维测能力增强：
  + 新增支持获取所有虚拟机线程的堆内存信息，包括线程ID、线程名称、堆类型和堆对象大小。（[API参考](<../../../../harmonyos-references/ArkTS（方舟编程语言）/ArkTS API/@ohos.util (util工具函数)/js-apis-util.md#getallvmheapmemoryinfo24>)）
  + 新增堆内存超过预警阈值的回调函数，在虚拟机主线程完成垃圾回收后如果堆内存仍超过预警阈值则触发回调执行。（[API参考](<../../../../harmonyos-references/ArkTS（方舟编程语言）/ArkTS API/@ohos.util (util工具函数)/js-apis-util.md#onvmheapmemorypressure24>)）
* taskpool的execute方法增强，执行任务或任务组可以指定任务超时时长。如果任务或任务组的执行时间超过设置的超时时长，则抛出对应错误信息。（[API参考](<../../../../harmonyos-references/ArkTS（方舟编程语言）/ArkTS API/@ohos.taskpool (启动任务池)/js-apis-taskpool.md#taskpoolexecute24>)）

### ArkUI

* 应用主动接入平行视界功能时，通过新API接口能够运行时获取当前平行视界的分栏状态，方便对业务逻辑&UX动效等进行调整。（[API参考](<../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS API/UI界面/@ohos.arkui.UIContext (UIContext)/Class (UIContext)/arkts-apis-uicontext-uicontext.md>)）
* 自定义组件支持跨Ability迁移。（[指南](<../../../../harmonyos-guides/应用框架/ArkUI（方舟UI框架）/UI开发 (ArkTS声明式开发范式)/学习UI范式基本语法/自定义组件/创建自定义组件/arkts-create-custom-components.md#自定义组件支持跨ability迁移>)）
* 新增多个组件的C API：[OH\_ArkUI\_DecorationStyleOptions](<../../../../harmonyos-references/ArkUI（方舟UI框架）/C API/结构体/OH_ArkUI_DecorationStyleOptions/arkui-nativemodule-oh-arkui-decorationstyleoptions.md>)、[OH\_ArkUI\_TextDataDetectorConfig](<../../../../harmonyos-references/ArkUI（方舟UI框架）/C API/结构体/OH_ArkUI_TextDataDetectorConfig/arkui-nativemodule-oh-arkui-textdatadetectorconfig.md>)、[OH\_ArkUI\_TextEditorSelectionMenuOptions](<../../../../harmonyos-references/ArkUI（方舟UI框架）/C API/结构体/OH_ArkUI_TextEditorSelectionMenuOptions/tivemodule-oh-arkui-texteditorselectionmenuoptions.md>)、[OH\_ArkUI\_TextEditorPlaceholderOptions](<../../../../harmonyos-references/ArkUI（方舟UI框架）/C API/结构体/OH_ArkUI_TextEditorPlaceholderOptions/nativemodule-oh-arkui-texteditorplaceholderoptions.md>)、[OH\_ArkUI\_TextEditorStyledStringController](<../../../../harmonyos-references/ArkUI（方舟UI框架）/C API/结构体/OH_ArkUI_TextEditorStyledStringController/vemodule-oh-arkui-texteditorstyledstringcontroller.md>)、[OH\_ArkUI\_TextEditorParagraphStyle](<../../../../harmonyos-references/ArkUI（方舟UI框架）/C API/结构体/OH_ArkUI_TextEditorParagraphStyle/kui-nativemodule-oh-arkui-texteditorparagraphstyle.md>)、[OH\_ArkUI\_ShadowOptions](<../../../../harmonyos-references/ArkUI（方舟UI框架）/C API/结构体/OH_ArkUI_ShadowOptions/capi-arkui-nativemodule-oh-arkui-shadowoptions.md>)、[OH\_ArkUI\_TextEditorTextStyle](<../../../../harmonyos-references/ArkUI（方舟UI框架）/C API/结构体/OH_ArkUI_TextEditorTextStyle/pi-arkui-nativemodule-oh-arkui-texteditortextstyle.md>)。
* 新增一批属性字符串的C API。（[API参考](<../../../../harmonyos-references/ArkUI（方舟UI框架）/C API/头文件/styled_string.h/capi-styled-string-h.md#oh_arkui_styledstringkey>)）
* 支持将含有竞争策略的事件分发到目标UI组件节点。（[API参考](<../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS API/UI界面/arkui/BuilderNode/js-apis-arkui-buildernode.md#postinputeventwithstrategy24>)）
* 新增支持获取UIContext对应页面的根节点。（[ArkTS API参考](<../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS API/UI界面/@ohos.arkui.UIContext (UIContext)/Class (UIContext)/arkts-apis-uicontext-uicontext.md#getpagerootnode24>)、[C API参考](<../../../../harmonyos-references/ArkUI（方舟UI框架）/C API/头文件/native_node.h/capi-native-node-h.md#oh_arkui_nativemodule_getpagerootnodehandlebycontext>)）
* Text组件新增支持根据坐标获取最近的字符的位置信息。（[ArkTS API参考](../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/文本与输入/文本组件公共接口/ts-text-common.md#getcharacterpositionatcoordinate24)、[C API参考](<../../../../harmonyos-references/ArkUI（方舟UI框架）/C API/头文件/styled_string.h/capi-styled-string-h.md#oh_arkui_textlayoutmanager_getcharacterpositionatcoordinate>)）
* 新增拖拽异步通知接口，可以在拖拽的落入行为中指定采取剪切或者复制的处理方式（[API参考](<../../../../harmonyos-references/ArkUI（方舟UI框架）/C API/头文件/drag_and_drop.h/capi-drag-and-drop-h.md#oh_arkui_notifysuggesteddropoperation>)），以及指定是否执行拖拽落入行为的动效（[API参考](<../../../../harmonyos-references/ArkUI（方舟UI框架）/C API/头文件/drag_and_drop.h/capi-drag-and-drop-h.md#oh_arkui_notifydisabledefaultdropanimation>)）。
* 新增onNeedSoftkeyboard回调，支持开发者配置焦点转移后不关闭拉起的软键盘。（[ArkTS API参考](../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/通用事件/交互响应事件/键盘判断事件/ts-universal-events-onneedsoftkeyboard.md)、[C API参考-NODE\_ON\_NEED\_SOFTKEYBOARD](<../../../../harmonyos-references/ArkUI（方舟UI框架）/C API/头文件/native_node.h/capi-native-node-h.md#arkui_nodeeventtype>)）
* CanvasRenderingContext2D（[API参考](../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/画布绘制/CanvasRenderingContext2D/ts-canvasrenderingcontext2d.md#antialias24)）和OffscreenCanvasRenderingContext2D（[API参考](../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/画布绘制/OffscreenCanvasRenderingContext2D/ts-offscreencanvasrenderingcontext2d.md#antialias24)）新增antialias属性，支持关闭文本抗锯齿功能。
* 分段按钮新增enableStateAnimation配置项，用于指定selectedIndexes在绑定的状态变量发生变化时是否执行系统动画。（[API参考](../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/系统预置UI组件库/SegmentButton/ohos-arkui-advanced-segmentbutton.md#segmentbutton-1)）
* Tabs组件新增支持嵌套滚动能力。（[API参考](../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/导航与切换/Tabs/ts-container-tabs.md#nestedscroll24)）
* JS组件新增支持旋转表冠事件监听接口。（[API参考-ArkUI.Full](../../../../harmonyos-references/ArkUI（方舟UI框架）/JS组件/兼容JS的类Web开发范式（ArkUI.Full）/全局接口/旋转表冠事件监听/js-components-common-monitorcrownevents.md)、[API参考-ArkUI.Lite](../../../../harmonyos-references/ArkUI（方舟UI框架）/JS组件/兼容JS的类Web开发范式（ArkUI.Lite）/全局接口/旋转表冠事件监听/js-lite-common-monitorcrownevents.md)）
* 多行文本的缩略模式新增支持设置为省略行首内容（MULTILINE\_START）或省略行中内容（MULTILINE\_CENTER）。（[ArkTS API参考](../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/公共定义/枚举说明/ts-appendix-enums.md#ellipsismode11)、[API参考](<../../../../harmonyos-references/ArkUI（方舟UI框架）/C API/头文件/native_type.h/capi-native-type-h.md#arkui_ellipsismode>)）
* 新增动态布局容器组件，支持在运行时动态切换不同的布局算法，不改变子组件的状态。（[指南](<../../../../harmonyos-guides/应用框架/ArkUI（方舟UI框架）/UI开发 (ArkTS声明式开发范式)/组件布局/构建布局/动态布局 (DynamicLayout)/arkts-layout-development-dynamiclayout.md>)）
* 窗口管理新增支持按需销毁窗口（WindowStage）的页面内容（UIContent）。（[API参考](<../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS API/窗口管理/@ohos.window (窗口)/Interface (WindowStage)/arkts-apis-window-windowstage.md#releaseuicontent24>)）

### ArkWeb

* ArkWeb网页请求支持User-Agent Client Hints功能。（[API参考](<../../../../harmonyos-references/ArkWeb（方舟Web）/ArkTS API/@ohos.web.webview (Webview)/Class (WebviewController)/arkts-apis-webview-webviewcontroller.md#setuseragentclienthintsenabled24>)）
* ArkWeb新增默认右键菜单启用开关，可通过该接口控制默认的右键菜单是否开启。（[API参考](<../../../../harmonyos-references/ArkWeb（方舟Web）/ArkTS 组件/Web/属性/arkts-basic-components-web-attributes.md#enabledefaultcontextmenu24>)）
* 设置Web页的URL白名单，只有白名单内的URL才能允许加载/跳转，否则将拦截并弹出告警页。（[API参考](<../../../../harmonyos-references/ArkWeb（方舟Web）/ArkTS API/@ohos.web.webview (Webview)/Class (WebviewController)/arkts-apis-webview-webviewcontroller.md#seturltrustlist24>)）

### Audio Kit

* 音频采集和音频渲染新增支持设置独立的音频会话策略和行为参数。（[API参考-音频采集](<../../../../harmonyos-references/Audio Kit（音频服务）/ArkTS API/@ohos.multimedia.audio (音频管理)/Interface (AudioCapturer)/arkts-apis-audio-audiocapturer.md#setindependentaudiosessionstrategy24>)、[API参考-音频渲染](<../../../../harmonyos-references/Audio Kit（音频服务）/ArkTS API/@ohos.multimedia.audio (音频管理)/Interface (AudioRenderer)/arkts-apis-audio-audiorenderer.md#setindependentaudiosessionstrategy24>)）
* 新增OH\_MIDI的C API，支持应用通过USB或蓝牙BLE连接外接MIDI设备（如MIDI键盘、电子琴、MIDI控制器等），实现MIDI消息的收发、设备枚举与热插拔监听，可用于音乐创作、乐器录制与教学、MIDI设备控制等场景。（[指南](<../../../../harmonyos-guides/媒体/Audio Kit（音频服务）/MIDI设备通信/OH_MIDI概述(CC++)/midi-overview.md>)）

### AVCodec Kit

* 新增支持Cinepak媒体格式的编解码能力。（[指南](<../../../../harmonyos-guides/媒体/AVCodec Kit（音视频编解码服务）/AVCodec支持的格式/avcodec-support-formats.md#媒体编解码>)）
* 新增支持筛选特定MIME类型的安全解码器，在处理受数字版权管理保护的DRM媒体资源时，可以使用支持安全链路的"安全解码器"。（[指南](<../../../../harmonyos-guides/媒体/AVCodec Kit（音视频编解码服务）/音视频编解码/获取支持的编解码能力/obtain-supported-codecs.md#筛选特定mime类型的安全解码器drm播放场景>)）

### AVSession Kit

新增支持后台播放模式的设置，可由应用告知系统是否支持后台播放，系统根据能力决策实况胶囊的显示。（[API参考](<../../../../harmonyos-references/AVSession Kit（音视频播控服务）/ArkTS API/@ohos.multimedia.avsession (媒体会话管理)/Interface (AVSession)/arkts-apis-avsession-avsession.md#setbackgroundplaymode24>)）

### Camera Kit

新增支持创建延迟预览输出对象，在配流时替代普通的预览输出对象加入数据流（[API参考](<../../../../harmonyos-references/Camera Kit（相机服务）/ArkTS API/@ohos.multimedia.camera (相机管理)/Interface (CameraManager)/arkts-apis-camera-cameramanager.md#createdeferredpreviewoutput24>)）。同时支持配置延迟预览的Surface（[API参考](<../../../../harmonyos-references/Camera Kit（相机服务）/ArkTS API/@ohos.multimedia.camera (相机管理)/Interface (PreviewOutput)/arkts-apis-camera-previewoutput.md#adddeferredsurface24>)）。

### Connectivity Kit

* 新增支持通过C API获取Wi-Fi连接信息。（[API参考](<../../../../harmonyos-references/网络/Connectivity Kit（短距通信服务）/C API/头文件/oh_wifi.h/capi-oh-wifi-h.md#oh_wifi_getlinkedinfo>)）
* 新增A2DP的播放状态广播以及SCO广播事件。（[API参考](<../../../../harmonyos-references/基础功能/Basic Services Kit（基础服务）/ArkTS API/进程线程通信/系统定义的公共事件/commoneventmanager-definitions.md#common_event_bluetooth_a2dpsource_play_state_change24>)）

### Content Embed Kit

【新增Kit】Content Embed Kit（内容嵌入服务）提供应用间文档互相嵌入与协同编辑的框架能力，并为开发者封装了客户端与服务端的开发接口，便于快速实现文档跨应用嵌入与协作。（[指南](<../../../../harmonyos-guides/应用框架/Content Embed Kit（内容嵌入服务）/Content Embed Kit简介/content-embed-kit-overview.md>)、[API参考](<../../../../harmonyos-references/Content Embed Kit（内容嵌入服务）/C API/模块/ContentEmbed/capi-contentembed.md>)）

### Desktop Extension Kit

* 新增支持更新单个一级菜单项内容。（[API参考](<../../../../harmonyos-references/基础功能/Desktop Extension Kit（桌面拓展服务）/ArkTS API/statusBarManager（状态栏管理服务）/statusbar-extension-manager.md#statusbarmanagerupdatestatusbarmenuitem>)）
* 新增支持更新单个二级菜单项内容。（[API参考](<../../../../harmonyos-references/基础功能/Desktop Extension Kit（桌面拓展服务）/ArkTS API/statusBarManager（状态栏管理服务）/statusbar-extension-manager.md#statusbarmanagerupdatestatusbarsubmenuitem>)）
* 新增支持配置菜单项的默认显示图标、及选中时显示的图标。（[API参考](<../../../../harmonyos-references/基础功能/Desktop Extension Kit（桌面拓展服务）/ArkTS API/statusBarManager（状态栏管理服务）/statusbar-extension-manager.md#statusbarmenuitemoptions>)）

### Device Security Kit

* 新增代码签名信息查询功能，开发者可获取设备上已签名的文件签名信息。（[指南-ArkTS](<../../../../harmonyos-guides/系统/安全/Device Security Kit（设备安全服务）/安全审计/代码签名信息查询场景/devicesecurity-audit-acquirecodesign-arkts.md>)、[API参考-ArkTS](<../../../../harmonyos-references/Device Security Kit（设备安全服务）/ArkTS API/SecurityAudit（安全审计）/devicesecurity-securityaudit-api.md#acquirecodesign>)、[指南-C/C++](<../../../../harmonyos-guides/系统/安全/Device Security Kit（设备安全服务）/安全审计/代码签名信息查询场景（CC++）/devicesecurity-audit-acquirecodesign-c.md>)、[API参考-C/C++](<../../../../harmonyos-references/Device Security Kit（设备安全服务）/C API/模块/SecurityAudit/devicesecurity-capi-securityaudit.md#hms_securityaudit_acquirecodesign>)）
* 数字盾服务新增支持Tablet、PC/2in1设备。（[指南](<../../../../harmonyos-guides/系统/安全/Device Security Kit（设备安全服务）/Device Security Kit简介/devicesecurity-introduction.md#支持的设备>)、[API参考](<../../../../harmonyos-references/Device Security Kit（设备安全服务）/ArkTS API/TrustedAuthentication（数字盾服务）/devicesecurity-trusted-auth-api.md>)）
* 新增系统安全专项相关事件：进程提权事件、进程异常调试事件、系统目录异常挂载事件、进程异常崩溃事件、应用代码未签名事件、应用代码验签异常事件、驱动代码验签异常事件、驱动非法映射内核内存事件、内核内存异常使用事件。（[指南-ArkTS](<../../../../harmonyos-guides/系统/安全/Device Security Kit（设备安全服务）/安全审计/多客户端订阅场景/订阅通知类事件/devicesecurity-audit-subscribe-arkts-filterevent.md>)、[API参考-ArkTS](<../../../../harmonyos-references/Device Security Kit（设备安全服务）/ArkTS API/SecurityAudit（安全审计）/devicesecurity-securityaudit-api.md#notifyevent>)、[指南-C/C++](<../../../../harmonyos-guides/系统/安全/Device Security Kit（设备安全服务）/安全审计/多客户端订阅场景（CC++）/订阅通知类事件/devicesecurity-audit-subscribe-c-filterevent.md>)、[API参考-C/C++](<../../../../harmonyos-references/Device Security Kit（设备安全服务）/C API/模块/SecurityAudit/devicesecurity-capi-securityaudit.md#securityaudit_notify_event>)）

### Enterprise Data Guard

* 新增放通应用列表管理功能，开发者可设定特定应用不受KIA策略管控。（[指南](<../../../../harmonyos-guides/系统/安全/Enterprise Data Guard Kit（企业数据保护服务）/文件分级管控/添加、删除和获取放通应用列表/fileguard-unrestricted-app-list.md>)、[API参考](<../../../../harmonyos-references/安全/Enterprise Data Guard Kit（企业数据保护服务）/ArkTS API/fileGuard (文件分级管控)/dataguard-fileguard.md#addunrestrictedapplicationlist>)）
* 新增设置上位机和下位机之间的HDC鉴权密钥。（[指南](<../../../../harmonyos-guides/系统/安全/Enterprise Data Guard Kit（企业数据保护服务）/文件分级管控/设置HDC鉴权密钥/fileguard-set-hdc-authentication-key.md>)、[API参考](<../../../../harmonyos-references/安全/Enterprise Data Guard Kit（企业数据保护服务）/ArkTS API/fileGuard (文件分级管控)/dataguard-fileguard.md#sethdcauthenticationkey>)）
* 新增订阅或取消订阅打印服务启动事件。（[指南](<../../../../harmonyos-guides/系统/安全/Enterprise Data Guard Kit（企业数据保护服务）/文件分级管控/订阅或取消订阅打印服务启动事件/fileguard-print-startup-event.md>)、[API参考](<../../../../harmonyos-references/安全/Enterprise Data Guard Kit（企业数据保护服务）/ArkTS API/fileGuard (文件分级管控)/dataguard-fileguard.md#onprintstartup>)）
* 新增弹框验证锁屏密码用于获取重置锁屏密码的恢复密钥。（[指南](<../../../../harmonyos-guides/系统/安全/Enterprise Data Guard Kit（企业数据保护服务）/企业恢复密钥/获取重置锁屏密码的企业恢复密钥/recoverykey-getkeyforresetpin.md>)、[API参考](<../../../../harmonyos-references/Enterprise Data Guard Kit（企业数据保护服务）/ArkTS API/recoveryKey（企业恢复密钥）/dataguard-recoverykey.md#verifyuserbydialog>)）

### Enterprise Threat Protection Kit

【新增Kit】Enterprise Threat Protection Kit（企业威胁防护服务）提供了构建安全防护应用的核心能力，专注于文件访问与处置。应用可对文件进行扫描以识别潜在威胁，并对威胁文件执行隔离、恢复或删除操作，从而有效保护企业设备的数据安全。详细信息请参见[Enterprise Threat Protection Kit开发指南](<../../../../harmonyos-guides/系统/安全/Enterprise Threat Protection Kit（企业威胁防护服务）/enterprise-threat-protection-kit-guide.md>)。

### FAST Kit

* 新增并发哈希表。（[指南](<../../../../harmonyos-guides/系统/基础功能/FAST Kit（算法加速服务）/使用ConcurrentHashmap在多线程下完成键值信息的查找维护/fast-concurrent-hashmap.md>)、[API参考](<../../../../harmonyos-references/基础功能/FAST Kit（算法加速服务）/C API/头文件和结构体/头文件/fast_ads_concurrent_hashmap.h/fast-kit-fast-ads-concurrent-hashmap-8h.md>)）
* 新增部分向量运算和复数处理功能。（[指南](<../../../../harmonyos-guides/系统/基础功能/FAST Kit（算法加速服务）/使用DSP进行向量计算/fast-dsp-vector-calculation.md>)、[API参考](<../../../../harmonyos-references/基础功能/FAST Kit（算法加速服务）/C API/头文件和结构体/头文件/fast_dsp_common.h/fast-kit-fast-dsp-common-8h.md>)）
* 新增二阶IIR滤波器功能。（[指南](<../../../../harmonyos-guides/系统/基础功能/FAST Kit（算法加速服务）/使用DSP进行二阶IIR滤波/fast-dsp-iir-filter.md>)、[API参考](<../../../../harmonyos-references/基础功能/FAST Kit（算法加速服务）/C API/头文件和结构体/头文件/fast_dsp_common.h/fast-kit-fast-dsp-common-8h.md>)）

### Form Kit

在onUpdateForm回调中新增支持卡片更新原因字段。（[API参考](<../../../../harmonyos-references/Form Kit（卡片开发服务）/ArkTS API/@ohos.app.form.formInfo (formInfo)/js-apis-app-form-forminfo.md#formupdatereason24>)）

### Image Kit

新增WebP图像元数据类，用于存储图像的元数据。（[API参考](<../../../../harmonyos-references/Image Kit（图片处理服务）/ArkTS API/@ohos.multimedia.image (图片处理)/class (WebPMetadata)/arkts-apis-image-webpmetadata.md>)）

### Input Kit

C API输入事件增强，提供输入事件的压力、相对窗口左上角的XY相对坐标等事件。（[API参考](<../../../../harmonyos-references/基础功能/Input Kit（多模输入服务）/C API/头文件/oh_input_manager.h/capi-oh-input-manager-h.md#oh_input_settoucheventpressure>)）

### Live View Kit

* 新增支持点击实况窗卡片辅助区结束实况窗。（[API参考](<../../../../harmonyos-references/Live View Kit（实况窗服务）/ArkTS API/liveViewManager/liveview-liveviewmanager.md#actiontype>)）
* 新增实况窗最长存活时间参数配置，系统将在达到预设时间后自动结束实况窗。（[API参考](<../../../../harmonyos-references/Live View Kit（实况窗服务）/ArkTS API/liveViewManager/liveview-liveviewmanager.md#primarydata>)）

### Map Kit

* 关键字搜索场景下，查询结果新增支持展示相关性分数。（[API参考](<../../../../harmonyos-references/Map Kit（地图服务）/ArkTS API/site（地点搜索）/map-site.md#site>)）
* 在区划查询场景下，新增支持选择区划层级范围。（[指南](<../../../../harmonyos-guides/应用服务/Map Kit（地图服务）/地图Picker/区划选择/map-location-division.md#开发步骤>)、[API参考](<../../../../harmonyos-references/Map Kit（地图服务）/ArkTS API/sceneMap（场景化控件）/map-scenemap.md#districtselectoptions>)）
* 新增支持设置Marker注释背景颜色。（[API参考](<../../../../harmonyos-references/Map Kit（地图服务）/ArkTS API/mapCommon（地图属性模型）/map-common.md#markeroptions>)）
* 瓦片图层场景下，新增支持高层级复用低层级瓦片。（[指南](<../../../../harmonyos-guides/应用服务/Map Kit（地图服务）/在地图上绘制/瓦片图层/map-tile.md#支持高层级复用低层级瓦片>)、[API参考](<../../../../harmonyos-references/Map Kit（地图服务）/ArkTS API/mapCommon（地图属性模型）/map-common.md#tileoverlayoptions>)）
* 新增支持拉起地图App离线地图管理页面和地点详情。（[指南-离线地图管理页面](<../../../../harmonyos-guides/应用服务/Map Kit（地图服务）/通过地图应用实现导航等能力/map-petalmaps.md#打开地图应用离线地图管理页面>)、[API参考-离线地图管理页面](<../../../../harmonyos-references/Map Kit（地图服务）/ArkTS API/petalMaps（拉起地图应用）/map-petal-maps.md#openmapofflinedatamanagement>)、[指南-地点详情](<../../../../harmonyos-guides/应用服务/Map Kit（地图服务）/通过地图应用实现导航等能力/map-petalmaps.md#打开地图应用查看地点详情>)、[API参考-地点详情](<../../../../harmonyos-references/Map Kit（地图服务）/ArkTS API/petalMaps（拉起地图应用）/map-petal-maps.md#poidetailparams>)）
* 新增Marker长按事件监听能力。（[指南](<../../../../harmonyos-guides/应用服务/Map Kit（地图服务）/在地图上绘制/标记/map-marker.md#设置监听标记长按事件>)、[API参考](<../../../../harmonyos-references/Map Kit（地图服务）/ArkTS API/map（地图显示功能）/Interface (MapEventManager)/map-map-mapeventmanager.md#onmarkerlongclick>)）
* 新增POI长按事件监听能力。（[API参考](<../../../../harmonyos-references/Map Kit（地图服务）/ArkTS API/map（地图显示功能）/Interface (MapEventManager)/map-map-mapeventmanager.md#onpoilongclick>)）

### NearLink Kit

新增获取星闪合作设备集合管理信息的能力。（[指南](<../../../../harmonyos-guides/系统/网络/NearLink Kit（星闪服务）/获取星闪合作设备集合信息/nearlink-cdsm-information.md>)、[API参考](<../../../../harmonyos-references/NearLink Kit（星闪服务）/ArkTS API/cdsm（星闪合作设备集合能力）/nearlink-cdsm.md>)）

### MDM Kit

* kiosk模式下，新增支持通过上划停留手势进入最近任务栏（ALLOW\_GESTURE\_CONTROL）以及通过边缘内划停留手势进入侧边DOCK栏（ALLOW\_SIDE\_DOCK）。（[API参考](<../../../../harmonyos-references/基础功能/MDM Kit（企业设备管理服务）/ArkTS API/@ohos.enterprise.applicationManager（应用管理）/js-apis-enterprise-applicationmanager.md#kioskfeature20>)）
* 新增支持安装和卸载企业重签名证书的能力。（[API参考](<../../../../harmonyos-references/基础功能/MDM Kit（企业设备管理服务）/ArkTS API/@ohos.enterprise.securityManager（安全管理）/js-apis-enterprise-securitymanager.md#securitymanagerinstallenterpriseresignaturecertificate24>)）
* 新增支持根据位置索引添加应用到PC/2in1设备的底部快捷栏的能力。（[API参考](<../../../../harmonyos-references/基础功能/MDM Kit（企业设备管理服务）/ArkTS API/@ohos.enterprise.applicationManager（应用管理）/js-apis-enterprise-applicationmanager.md#applicationmanageradddockapp24>)）

### Media Kit

* C API新增隐私保护设置的回调函数，用于响应截屏录屏时捕获的隐私保护事件。（[API参考](<../../../../harmonyos-references/Media Kit（媒体服务）/C API/头文件/native_avscreen_capture.h/capi-native-avscreen-capture-h.md#oh_avscreencapture_setprivacyprotectcallback>)）
* C API新增支持获取多屏幕录制能力信息（[API参考](<../../../../harmonyos-references/Media Kit（媒体服务）/C API/头文件/native_avscreen_capture.h/capi-native-avscreen-capture-h.md#oh_avscreencapture_getmultidisplaycapturecapability>)），以及通过DisplayID选择多屏幕进行录制（[API参考](<../../../../harmonyos-references/Media Kit（媒体服务）/C API/头文件/native_avscreen_capture.h/capi-native-avscreen-capture-h.md#oh_avscreencapture_getmultidisplayidsselected>)）。

### Network Boost Kit

新增支持设置数据传输低功耗模式。（[API参考](<../../../../harmonyos-references/网络/Network Boost Kit（网络加速服务）/ArkTS API/netBoost（网络加速）/networkboost-netboost.md#netboostsetlowpowermode>)）

### Network Kit

TLS支持证书链的验证，可通过传入数组的方式最多支持到1000个证书。（[API参考](<../../../../harmonyos-references/网络/Network Kit（网络服务）/ArkTS API/@ohos.net.socket (Socket连接)/js-apis-socket.md#tlssecureoptions9>)）

### Notification Kit

* 新增支持查询本APP通知中wantAgent字段的部分信息。（[API参考](<../../../../harmonyos-references/Notification Kit（用户通知服务）/ArkTS API/@ohos.notificationManager (NotificationManager模块)/js-apis-notificationmanager.md#notificationmanagergetnotificationparameters24>)）
* 新增支持使用应用沙箱内的文件作为通知的自定义铃声。（[指南](<../../../../harmonyos-guides/应用服务/Notification Kit（用户通知服务）/发布通知/为通知添加自定义铃声/notification-customized-ringtone.md>)）

### Payment Kit

人脸核身能力新增支持PC设备。（[指南](<../../../../harmonyos-guides/应用服务/Payment Kit（鸿蒙支付服务）/Payment Kit简介/payment-introduction.md>)、[API参考](<../../../../harmonyos-references/Payment Kit（鸿蒙支付服务）/ArkTS API/realNameService(身份验证服务)/payment-realnameservice.md>)）

### Performance Analysis Kit

* 当应用发生SIGPIPE异常退出时，在Debug版本应用可开启SIGPIPE信号打印调用栈功能辅助定位问题。（[指南](<../../../../harmonyos-guides/系统/调测调优/Performance Analysis Kit（性能分析服务）/故障检测/崩溃检测/Cpp Crash（进程崩溃）检测/cppcrash-guidelines.md#应用发生sigpipe异常退出>)）
* hiprofiler新增文件缓存模式（use\_file\_cache\_mode），通过将缓存数据落盘，提升内存分配信息的采集性能。（[指南](../../../../harmonyos-guides/系统/调测调优/调试命令/hiprofiler/hiprofiler.md#native-hook插件)）
* HiDebug新增资源采集功能，支持按需采集应用进程资源分配栈至沙箱，覆盖文件描述符、线程、Native/GPU内存及全局句柄等类别，辅助定位资源泄漏。（[指南](<../../../../harmonyos-guides/系统/调测调优/Performance Analysis Kit（性能分析服务）/系统调试信息获取/HiDebug能力概述/hidebug-guidelines.md>)）
* HiDebug新增支持获取应用程序进程的物理内存使用信息。（[API参考](<../../../../harmonyos-references/调测调优/Performance Analysis Kit（性能分析服务）/ArkTS API/@ohos.hidebug (Debug调试)/js-apis-hidebug.md#hidebuggetrssinfo24>)）
* HiDebug新增支持将转储的堆快照由线程级改为进程级。（[API参考](<../../../../harmonyos-references/调测调优/Performance Analysis Kit（性能分析服务）/ArkTS API/@ohos.hidebug (Debug调试)/js-apis-hidebug.md#hidebugsetprocdumpinsharedoom24>)）
* HiDebug新增提供包括内核信息在内的Trace采集请求接口。（[ArkTS API参考](<../../../../harmonyos-references/调测调优/Performance Analysis Kit（性能分析服务）/ArkTS API/@ohos.hidebug (Debug调试)/js-apis-hidebug.md#hidebugrequesttrace24>)、[C API参考](<../../../../harmonyos-references/Performance Analysis Kit（性能分析服务）/C API/头文件/hidebug.h/capi-hidebug-h.md#oh_hidebug_requesttrace>)）
* HiAppEvent新增多个参数，用于自定义APP\_CRASH事件中的CPP\_CRASH类型的日志规格，包括打印PC、LR寄存器扩展字节范围的内存内容（[OH\_APP\_CRASH\_PARAM\_EXTEND\_PC\_LR\_PRINTING](<../../../../harmonyos-references/Performance Analysis Kit（性能分析服务）/C API/头文件/hiappevent_param.h/capi-hiappevent-param-h.md#oh_app_crash_param_extend_pc_lr_printing>)）、按设置的参数值大小截断（[OH\_APP\_CRASH\_PARAM\_LOG\_FILE\_CUTOFF\_SZ\_BYTES](<../../../../harmonyos-references/Performance Analysis Kit（性能分析服务）/C API/头文件/hiappevent_param.h/capi-hiappevent-param-h.md#oh_app_crash_param_log_file_cutoff_sz_bytes>)）、只打印崩溃日志中出现的地址所属的VMA映射信息（[OH\_APP\_CRASH\_PARAM\_SIMPLIFY\_VMA\_PRINTING](<../../../../harmonyos-references/Performance Analysis Kit（性能分析服务）/C API/头文件/hiappevent_param.h/capi-hiappevent-param-h.md#oh_app_crash_param_simplify_vma_printing>)）、在CPP\_CRASH场景拼接应用沙箱中指定文件的日志（[OH\_APP\_CRASH\_PARAM\_MERGE\_CPPCRASH\_APP\_LOG](<../../../../harmonyos-references/Performance Analysis Kit（性能分析服务）/C API/头文件/hiappevent_param.h/capi-hiappevent-param-h.md#oh_app_crash_param_merge_cppcrash_app_log>)）。

### Remote Communication Kit

* 新增支持发起仅建立连接的请求。（[指南](<../../../../harmonyos-guides/系统/网络/Remote Communication Kit（远场通信服务）/提升HTTP传输性能/通过预建连接提升HTTP传输性能/remote-communication-pre-connect.md>)、[API参考-ArkTS](<../../../../harmonyos-references/网络/Remote Communication Kit（远场通信服务）/ArkTS API/rcp（数据请求）/remote-communication-rcp.md#request>)、[API参考-C/C++](<../../../../harmonyos-references/网络/Remote Communication Kit（远场通信服务）/C API/模块/RemoteCommunication/remote-communication-overview.md#hms_rcp_setrequestconnectonly>)）
* 新增支持C API获取默认session。（[API参考](<../../../../harmonyos-references/网络/Remote Communication Kit（远场通信服务）/C API/模块/RemoteCommunication/remote-communication-overview.md#hms_rcp_getdefaultsession>)）
* 新增支持配置蜂窝网络失败时是否抛出错误。（[API参考](<../../../../harmonyos-references/网络/Remote Communication Kit（远场通信服务）/ArkTS API/rcp（数据请求）/remote-communication-rcp.md#transferconfiguration>)）

### Screen Time Guard Kit

新增支持请求用户授权的同时配置管控应用在管控生效过程中是否可卸载。（[指南](<../../../../harmonyos-guides/应用服务/Screen Time Guard Kit（屏幕时间守护服务）/用户授权管理/请求用户授权/screentimeguard-request-user-auth.md>)、[API参考](<../../../../harmonyos-references/Screen Time Guard Kit（屏幕时间守护服务）/ArkTS API/GuardService（屏幕时间守护服务）/screentimeguard-guardservice.md#requestuserauth-1>)）

### Speech Kit

* AI字幕初始化场景下，新增支持设置源语言、目标语言以及对应语言下字体颜色和字体大小。（[API参考](<../../../../harmonyos-references/Speech Kit（场景化语音服务）/ArkTS组件/AICaptionComponent（AI字幕组件）/speech-aicaptioncomponent.md#aicaptionoptions>)）
* 朗读控件新增TextReaderIconV2图标接口，支持对ArkTS的状态管理V2装饰器的适配。（[API参考](<../../../../harmonyos-references/Speech Kit（场景化语音服务）/ArkTS组件/TextReaderIconV2（朗读听筒图标）/speech-textreadericonv2.md>)）

### UI Design Kit

底部页签新增支持页签栏和迷你栏垂直布局样式。（[API参考](<../../../../harmonyos-references/UI Design Kit（UI设计套件）/ArkTS组件/HdsTabs/ui-design-hdstabs.md#hdsbarlayoutmode>)）

### Vision Kit

卡证识别场景下，新增支持识别港澳居民来往内地通行证、台湾居民来往大陆通行证。（[API参考](<../../../../harmonyos-references/Vision Kit（场景化视觉服务）/ArkTS组件/CardRecognition（卡证识别控件）/vision-card-recognition.md#cardtype>)）

### 标准库

新增Seccomp开放系统调用列表。（[API参考](../../../../harmonyos-references/附录/Seccomp开放系统调用列表/seccomp-symbol.md)）
