---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/os-new-feature-502
title: 新增和增强特性
breadcrumb: 版本说明 > 历史版本 > HarmonyOS 5.0.2(14) > OS平台能力 > 新增和增强特性
category: harmonyos-releases
scraped_at: 2026-06-01T10:49:21+08:00
doc_updated_at: 2026-05-18
content_hash: sha256:158bad6cc8b7da81900e9ad88e8e472779f77b8ce98423437dfee50c6772b797
---
## Ability Kit

* HSP支持在配置文件中声明除入口Ability以外的UIAbility组件。（[指南](../../../../../harmonyos-guides/基础入门/开发基础知识/应用程序包基础知识/应用程序包开发与使用/HSP/in-app-hsp.md#约束限制)）
* 针对PC/2in1与平板设备，新增支持自定义应用启动时的启动页。（[API参考](<../../../../../harmonyos-references/Ability Kit（程序框架服务）/ArkTS API/Stage模型能力的接口/@ohos.app.ability.StartOptions (startAbility的可选参数)/js-apis-app-ability-startoptions.md#startoptions>)）
* 通过Want传递对象间信息时支持在parameters参数中携带应用分身的索引（ohos.param.callerAppCloneIndex）。（[API参考](<../../../../../harmonyos-references/Ability Kit（程序框架服务）/ArkTS API/通用能力的接口(推荐)/@ohos.app.ability.Want (Want)/js-apis-app-ability-want.md#want>)）
* 新增支持获取应用上下文的能力。（[API参考](<../../../../../harmonyos-references/Ability Kit（程序框架服务）/ArkTS API/Stage模型能力的接口/@ohos.app.ability.application (应用工具类)/js-apis-app-ability-application.md#applicationgetapplicationcontext14>)）
* 开放包管理能力供三方应用调用。（[API参考](<../../../../../harmonyos-references/Ability Kit（程序框架服务）/ArkTS API/通用能力的接口(推荐)/@ohos.bundle.bundleManager (应用程序包管理模块)/js-apis-bundlemanager.md>)）
* 新增支持UIAbility备份恢复的能力。（[API参考](<../../../../../harmonyos-references/Ability Kit（程序框架服务）/ArkTS API/接口依赖的元素及定义/application/UIAbilityContext/js-apis-inner-application-uiabilitycontext.md#setrestoreenabled14>)，[指南](<../../../../../harmonyos-guides/应用框架/Ability Kit（程序框架服务）/Stage模型开发指导/Stage模型应用组件/UIAbility组件/UIAbility备份恢复/ability-recover-guideline.md>)）
* 新增支持获取当前应用多实例的唯一实例标识。（[API参考](<../../../../../harmonyos-references/Ability Kit（程序框架服务）/ArkTS API/接口依赖的元素及定义/application/ApplicationContext (应用上下文)/js-apis-inner-application-applicationcontext.md#applicationcontextgetcurrentinstancekey14>)）
* 环境变量信息的定义中新增当前应用字体的唯一ID的定义fontId。（[API参考](<../../../../../harmonyos-references/Ability Kit（程序框架服务）/ArkTS API/通用能力的接口(推荐)/@ohos.app.ability.Configuration (环境变量)/js-apis-app-ability-configuration.md#configuration>)）
* 新增C API，支持获取当前应用适用的设备类型。适用于在将手机应用分发到平板/PC/2in1设备时，合理适配布局和字体大小。（[API参考](<../../../../../harmonyos-references/Ability Kit（程序框架服务）/C API/头文件/native_interface_bundle.h/capi-native-interface-bundle-h.md#oh_nativebundle_getcompatibledevicetype>)）

## ArkData

* 新增flushSync()接口支持将缓存的Preferences实例中的数据存储到共享用户首选项的持久化文件中。（[API参考](<../../../../../harmonyos-references/ArkData（方舟数据管理）/ArkTS API/@ohos.data.sendablePreferences (共享用户首选项)/js-apis-data-sendablepreferences.md#flushsync14>)）
* 关系型数据库（RDB）的配置属性StoreConfig新增参数cryptoParam，用于自定义加密参数。（[API参考](<../../../../../harmonyos-references/ArkData（方舟数据管理）/ArkTS API/@ohos.data.relationalStore (关系型数据库)/Interfaces (其他)/arkts-apis-data-relationalstore-i.md#cryptoparam14>)）
* 关系型数据库（RDB）新增支持创建可并发的事务对象。（[API参考](<../../../../../harmonyos-references/ArkData（方舟数据管理）/ArkTS API/@ohos.data.relationalStore (关系型数据库)/Interface (RdbStore)/arkts-apis-data-relationalstore-rdbstore.md#createtransaction14>)）
* 标准化数据结构（UDMF）新增内容卡片类型的数据结构（ContentForm）。（[API参考](<../../../../../harmonyos-references/ArkData（方舟数据管理）/ArkTS API/@ohos.data.uniformDataStruct (标准化数据结构)/js-apis-data-uniformdatastruct.md#contentform14>)）
* 标准化数据结构（UDMF）新增支持设置应用内拖拽通道数据可使用的范围。（[API参考](<../../../../../harmonyos-references/ArkData（方舟数据管理）/ArkTS API/@ohos.data.unifiedDataChannel (标准化数据通路)/js-apis-data-unifieddatachannel.md#unifieddatachannelsetappshareoptions14>)）

## ArkGraphics 2D

* 新增C API，支持获取系统全局字体集。（[API参考](<../../../../../harmonyos-references/ArkGraphics 2D（方舟2D图形服务）/C API/头文件/drawing_font_collection.h/capi-drawing-font-collection-h.md#oh_drawing_getfontcollectionglobalinstance>)）
* 新增Decoupled VSync（DVSync）的C API能力以提高自绘制动画场景的流畅性。（[API参考](<../../../../../harmonyos-references/ArkGraphics 2D（方舟2D图形服务）/C API/头文件/native_vsync.h/capi-native-vsync-h.md#oh_nativevsync_dvsyncswitch>)）
* 新增一个模糊效果的处理能力，增加着色器效果平铺模式，影响图像边缘的模糊效果。（[API参考](<../../../../../harmonyos-references/ArkGraphics 2D（方舟2D图形服务）/ArkTS API/@ohos.effectKit (图像效果)/js-apis-effectkit.md#blur14>)）
* 新增C API，使浏览器支持动态帧率。（[API参考](<../../../../../harmonyos-references/ArkGraphics 2D（方舟2D图形服务）/C API/头文件/native_vsync.h/capi-native-vsync-h.md#oh_nativevsync_create_forassociatedwindow>)）

## ArkUI

* 文本输入时的键盘避让模式支持光标避让。（[指南](<../../../../../harmonyos-guides/应用框架/ArkUI（方舟UI框架）/UI开发 (ArkTS声明式开发范式)/使用文本/文本输入 (TextInputTextAreaSearch)/arkts-common-components-text-input.md#光标避让>)）
* 新增支持将属性字符串转换成HTML格式字符串的能力。（[API参考](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/文本与输入/属性字符串/ts-universal-styled-string.md#tohtml14)）
* 新增支持设置子窗的模态类型。（[API参考](<../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS API/窗口管理/@ohos.window (窗口)/Interface (Window)/arkts-apis-window-window.md#setsubwindowmodal14>)）
* 新增支持对容器设置组件级的安全区域。（[API参考](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/通用属性/布局与边框/尺寸设置/ts-universal-attributes-size.md#safeareapadding14)）
* 新增支持获取文本组件中指定字符的绘制区域信息。（[API参考](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/文本与输入/文本组件公共接口/ts-text-common.md#getrectsforrange14)）
* Navigation（NavDestination）的title和menus属性新增支持Resource资源类型。（[API参考-title属性](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/导航与切换/NavDestination/ts-basic-components-navdestination.md#title)、[API参考-menus属性](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/导航与切换/Navigation/ts-basic-components-navigation.md#navigationmenuitem)）
* Navigation自定义转场动画能力增强，支持分别设置系统标题栏动画和内容动画。（[API参考](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/导航与切换/NavDestination/ts-basic-components-navdestination.md#systemtransition14)）
* TextArea、Search组件新增新的onSubmit事件用于在事件提交时保持组件的编辑状态。（[API参考-TextArea组件](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/文本与输入/TextArea/ts-basic-components-textarea.md#onsubmit14)、[API参考-Search组件](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/文本与输入/Search/ts-basic-components-search.md#onsubmit14)）
* 按键事件新增unicode对象，支持返回当前keyEvent对应按键的unicode码值。（[API参考](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/通用事件/基础输入事件/按键事件/ts-universal-events-key.md#keyevent对象说明)）
* 半模态转场的SheetOptions新增enableHoverMode和hoverModeArea属性用于支持悬停。（[API参考](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/通用属性/模态转场设置/半模态转场/ts-universal-attributes-sheet-transition.md#sheetoptions)）
* 文本选择器组件（TextPicker）新增支持滑动停止时的事件回调。（[API参考](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/按钮与选择/TextPicker/ts-basic-components-textpicker.md#onscrollstop14)）
* 新增C API，支持为OH\_NativeXComponent实例注册带有返回值的按键事件回调。（[API参考](<../../../../../harmonyos-references/ArkUI（方舟UI框架）/C API/头文件/native_interface_xcomponent.h/capi-native-interface-xcomponent-h.md#oh_nativexcomponent_registerkeyeventcallbackwithresult>)）
* ArkUI的NodeAttributeType新增获取滚动类组件及所有子组件全展开尺寸的C API属性定义。（[API参考](<../../../../../harmonyos-references/ArkUI（方舟UI框架）/C API/头文件/native_node.h/capi-native-node-h.md#arkui_nodeattributetype>)）
* List组件新增支持设置列表中ListItem/ListItemGroup的预加载数量，并支持配置是否显示预加载节点。（[API参考](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/滚动与滑动/List/ts-container-list.md#cachedcount14)）
* 滚动组件新增支持设置滚动容器的内容层裁剪区域。（[API参考](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/滚动与滑动/滚动组件通用接口/ts-container-scrollable-common.md#clipcontent14)）
* 滚动组件新增支持设置边缘渐隐效果及设置边缘渐隐长度。（[API参考](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/滚动与滑动/滚动组件通用接口/ts-container-scrollable-common.md#fadingedge14)）
* Grid、WaterFlow组件新增支持设置预加载的GridItem、FlowItem数量，并配置是否显示预加载节点。（[API参考-Grid](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/滚动与滑动/Grid/ts-container-grid.md#cachedcount14)、[API参考-WaterFlow](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/滚动与滑动/WaterFlow/ts-container-waterflow.md#cachedcount14)）
* ImageSpan组件新增支持为图像设置颜色滤镜效果。（[API参考](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/文本与输入/ImageSpan/ts-basic-components-imagespan.md#colorfilter14)）
* SegmentButton组件新增支持适老化大字体。（[API参考](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/系统预置UI组件库/SegmentButton/ohos-arkui-advanced-segmentbutton.md#segmentbutton-1)）
* 属性字符串新增支持设置文字背景色。（[API参考](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/文本与输入/属性字符串/ts-universal-styled-string.md#backgroundcolorstyle14)）
* 属性字符串新增支持设置为超链接。（[API参考](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/文本与输入/属性字符串/ts-universal-styled-string.md#urlstyle14)）
* Chip和ChipGroup组件新增支持多种类型的无障碍朗读能力。（[API参考-Chip](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/系统预置UI组件库/Chip/ohos-arkui-advanced-chip.md)、[API参考-ChipGroup](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/系统预置UI组件库/ChipGroup/ohos-arkui-advanced-chipgroup.md)）
* 日期滑动选择器弹窗（DatePickerDialog）新增支持设置切换农历开关的样式。（[API参考](<../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/弹窗/日期滑动选择器弹窗 (DatePickerDialog)/ts-methods-datepicker-dialog.md#lunarswitchstyle14对象说明>)）
* Tabs组件新增支持对底部页签适配组件级布局安全区。（[API参考](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/导航与切换/Tabs/ts-container-tabs.md#barheight)）
* Text组件新增支持设置选中文本的手柄颜色和底板颜色。（[API参考](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/文本与输入/Text/ts-basic-components-text.md#caretcolor14)）
* 新增支持设置跑马灯（Marquee）的动态帧率。（[API参考](<../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS API/UI界面/@ohos.arkui.UIContext (UIContext)/Class (MarqueeDynamicSyncScene)/arkts-apis-uicontext-marqueedynamicsyncscene.md>)）
* 手势处理的能力涉及到的六类手势事件新增支持设置允许的事件输入源。（[API参考](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/手势处理/手势公共接口/ts-gesture-common.md#allowedtypes14)）
* 组件的位置设置，新增支持对形成链的组件进行重新布局（仅当父容器为RelativeContainer时生效）。（[API参考](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/通用属性/布局与边框/位置设置/ts-universal-attributes-location.md#chainweight14)）
* 组件的背景设置，新增支持设置窗口失焦后，窗口内控件模糊效果会被移除。（[API参考](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/通用属性/基础属性/背景设置/ts-universal-attributes-background.md#backgroundeffectoptions11)）
* 路由跳转新增支持设置页面是否可恢复。（[API参考](<../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS API/UI界面/@ohos.router (页面路由)(不推荐)/js-apis-router.md#routeroptions>)）
* 新增C API，支持获取节点的节点类型（[API参考](<../../../../../harmonyos-references/ArkUI（方舟UI框架）/C API/头文件/native_node.h/capi-native-node-h.md#oh_arkui_nodeutils_getnodetype>)）和窗口信息（[API参考](<../../../../../harmonyos-references/ArkUI（方舟UI框架）/C API/头文件/native_node.h/capi-native-node-h.md#oh_arkui_nodeutils_getwindowinfo>)）。
* FrameNode新增支持手势事件。（[API参考](<../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS API/UI界面/arkui/FrameNode/js-apis-arkui-framenode.md#gestureevent14>)）
* Image组件新增支持设置图片的显示方向。（[API参考](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/图片与视频/Image/ts-basic-components-image.md#orientation14)）
* RichEditor新增支持鼠标悬停事件回调（OnHoverCallback）。（[API参考](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/文本与输入/RichEditor/ts-basic-components-richeditor.md#onhovercallback14)）
* Navigation页面栈新增支持配置可在异常退出时恢复。（[API参考](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/导航与切换/Navigation/ts-basic-components-navigation.md#recoverable14)）
* 新增支持绑定NavDestination组件和可滚动容器组件，当滑动可滚动容器组件时，会触发所有与其绑定的NavDestination组件的标题栏和工具栏的显示和隐藏动效。（[API参考](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/导航与切换/NavDestination/ts-basic-components-navdestination.md#bindtoscrollable14)）
* 新增支持设置窗口使用效果模板，比如使用有透视的背景模糊效果。（[API参考](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/通用属性/视效与模糊/特效绘制合并/ts-universal-attributes-use-effect.md#useeffect14)）
* 针对PC/2in1设备的应用的窗口管理，新增通过应用窗口关闭按钮关闭应用的监听，使用该API可忽略已设置的预关闭开关的回调。（[API参考](<../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS API/窗口管理/@ohos.window (窗口)/Interface (WindowStage)/arkts-apis-window-windowstage.md#onwindowstageclose14>)）
* 针对PC/2in1设备的应用的窗口管理，新增自定义应用主窗口大小和位置的能力，通过配置文件module.json5进行配置。（[指南](../../../../../harmonyos-guides/基础入门/开发基础知识/应用配置文件（Stage模型）/module.json5配置文件/module-configuration-file.md#metadata标签)）
* 针对PC/2in1设备的应用的窗口管理，新增支持将应用从最小化恢复到前台显示的能力。（[API参考](<../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS API/窗口管理/@ohos.window (窗口)/Interface (Window)/arkts-apis-window-window.md#restore14>)）
* 针对PC/2in1设备的应用的窗口管理，新增支持查询本应用内指定坐标下的可见窗口的能力。（[API参考](<../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS API/窗口管理/@ohos.window (窗口)/Functions/arkts-apis-window-f.md#windowgetwindowsbycoordinate14>)）
* 针对PC/2in1设备的应用的窗口管理，新增支持使能/禁用通过拖拽方式缩放主窗口或子窗口。（[API参考](<../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS API/窗口管理/@ohos.window (窗口)/Interface (Window)/arkts-apis-window-window.md#setresizebydragenabled14>)）
* 针对PC/2in1设备的应用的窗口管理，新增支持设置主窗口为模态窗口。（[API参考](<../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS API/窗口管理/@ohos.window (窗口)/Interface (WindowStage)/arkts-apis-window-windowstage.md#setwindowmodal14>)）
* 针对PC/2in1设备的应用的窗口管理，新增支持应用控制启动页消失时机。（[API参考](<../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS API/窗口管理/@ohos.window (窗口)/Interface (WindowStage)/arkts-apis-window-windowstage.md#removestartingwindow14>)）
* 针对PC/2in1设备的应用的窗口管理，新增支持设置主窗的尺寸记忆是否启用。（[API参考](<../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS API/窗口管理/@ohos.window (窗口)/Interface (WindowStage)/arkts-apis-window-windowstage.md#setwindowrectautosave14>)）
* 针对PC/2in1设备的应用的窗口管理，新增支持设置主窗口进入全屏沉浸式时鼠标Hover到热区上隐藏窗口标题栏和dock栏。（[API参考](<../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS API/窗口管理/@ohos.window (窗口)/Interface (Window)/arkts-apis-window-window.md#settitleanddockhovershown14>)）
* 针对PC/2in1设备的应用的窗口管理，新增支持设置主窗标题栏上的最大化、最小化、关闭按钮是否可见。（[API参考](<../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS API/窗口管理/@ohos.window (窗口)/Interface (Window)/arkts-apis-window-window.md#setwindowtitlebuttonvisible14>)）
* 针对PC/2in1设备的应用的窗口管理，新增支持设置主窗口置于其他应用窗口之上而不被遮挡。（[API参考](<../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS API/窗口管理/@ohos.window (窗口)/Interface (Window)/arkts-apis-window-window.md#setwindowtopmost14>)）
* 针对PC/2in1设备的应用的窗口管理，新增支持对窗口所在屏幕进行事件监听，例如当前窗口移动到其他屏幕时，可以从此接口监听到这个行为。（[API参考](<../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS API/窗口管理/@ohos.window (窗口)/Interface (Window)/arkts-apis-window-window.md#ondisplayidchange14>)）
* 针对PC/2in1设备的应用的窗口管理，新增支持应用窗口无系统标题栏场景下拖拽移动窗口的能力。（[API参考](<../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS API/窗口管理/@ohos.window (窗口)/Interface (Window)/arkts-apis-window-window.md#startmoving14>)）

## ArkWeb

* 用户主动收起软键盘时，新增支持设置焦点从输入框转移到Web的body上，使文本框失焦。（[API参考](<../../../../../harmonyos-references/ArkWeb（方舟Web）/ArkTS 组件/Web/属性/arkts-basic-components-web-attributes.md#bluronkeyboardhidemode14>)）
* 新增C API，用于获取调用JavaScriptProxy最后一帧的url。（[API参考](<../../../../../harmonyos-references/ArkWeb（方舟Web）/C API/结构体/ArkWeb_ControllerAPI/capi-web-arkweb-controllerapi.md#getlastjavascriptproxycallingframeurl>)）
* 新增支持获取默认的用户代理。（[API参考](<../../../../../harmonyos-references/ArkWeb（方舟Web）/ArkTS API/@ohos.web.webview (Webview)/Class (WebviewController)/arkts-apis-webview-webviewcontroller.md#getdefaultuseragent14>)）
* 新增支持为指定url设置cookie的值。（[API参考](<../../../../../harmonyos-references/ArkWeb（方舟Web）/ArkTS API/@ohos.web.webview (Webview)/Class (WebCookieManager)/arkts-apis-webview-webcookiemanager.md#configcookiesync14>)）
* 新增支持上下左右四种嵌套滚动模式。（[API参考](<../../../../../harmonyos-references/ArkWeb（方舟Web）/ArkTS 组件/Web/属性/arkts-basic-components-web-attributes.md#nestedscroll11>)）
* 新增支持根据指定的内存压力等级主动清理Web组件占用的缓存。（[API参考](<../../../../../harmonyos-references/ArkWeb（方舟Web）/ArkTS API/@ohos.web.webview (Webview)/Class (WebviewController)/arkts-apis-webview-webviewcontroller.md#trimmemorybypressurelevel14>)）
* 新增支持网页另存为PDF的能力。（[API参考](<../../../../../harmonyos-references/ArkWeb（方舟Web）/ArkTS API/@ohos.web.webview (Webview)/Class (WebviewController)/arkts-apis-webview-webviewcontroller.md#createpdf14>)）
* 新增支持设置滚动动画的持续时间。（[API参考-scrollTo](<../../../../../harmonyos-references/ArkWeb（方舟Web）/ArkTS API/@ohos.web.webview (Webview)/Class (WebviewController)/arkts-apis-webview-webviewcontroller.md#scrollto>)、[API参考-scrollBy](<../../../../../harmonyos-references/ArkWeb（方舟Web）/ArkTS API/@ohos.web.webview (Webview)/Class (WebviewController)/arkts-apis-webview-webviewcontroller.md#scrollby>)）
* 新增支持设置滚动条常驻。（[API参考](<../../../../../harmonyos-references/ArkWeb（方舟Web）/ArkTS 组件/Web/属性/arkts-basic-components-web-attributes.md#forcedisplayscrollbar14>)）

## AVCodec Kit

音视频编解码的C API新增支持HE-AAC编解码能力，该能力仅在HarmonyOS支持。（[API参考](<../../../../../harmonyos-references/AVCodec Kit（音视频编解码服务）/C API/模块/CodecBase/capi-codecbase.md#媒体编解码格式>)）

## AVSession Kit

新增支持投播半模态对象的能力。（[API参考](<../../../../../harmonyos-references/AVSession Kit（音视频播控服务）/ArkTS API/@ohos.multimedia.avsession (媒体会话管理)/Class (AVCastPickerHelper)/arkts-apis-avsession-avcastpickerhelper.md>)）

## Basic Service Kit

* 设备信息（Device Info）模块新增productModelAlias属性用于支持查询设备认证型号的别名。（[API参考](<../../../../../harmonyos-references/基础功能/Basic Services Kit（基础服务）/ArkTS API/设备管理/@ohos.deviceInfo (设备信息)/js-apis-device-info.md>)）
* 剪贴板新增支持通过MIME定义和使用多种格式的内容对象。（[API参考](<../../../../../harmonyos-references/基础功能/Basic Services Kit（基础服务）/ArkTS API/数据文件处理/@ohos.pasteboard (剪贴板)/js-apis-pasteboard.md#pasteboardcreatedata14>)）
* 剪贴板新增C API和ArkTS API支持获取剪贴板内容的MIME类型。（[C API参考](<../../../../../harmonyos-references/基础功能/Basic Services Kit（基础服务）/C API/头文件/oh_pasteboard.h/capi-oh-pasteboard-h.md#oh_pasteboard_getmimetypes>)、[ArkTS API参考](<../../../../../harmonyos-references/基础功能/Basic Services Kit（基础服务）/ArkTS API/数据文件处理/@ohos.pasteboard (剪贴板)/js-apis-pasteboard.md#getmimetypes14>)）
* USB管理新增支持检查应用程序是否有权访问USB配件。（[API参考](<../../../../../harmonyos-references/基础功能/Basic Services Kit（基础服务）/ArkTS API/设备管理/@ohos.usbManager (USB管理)/js-apis-usbmanager.md#usbmanagerhasaccessoryright14>)）

## Call Service Kit

* kit名称修改，导致kit文件名称变更。（[指南](<../../../../../harmonyos-guides/应用服务/Call Service Kit（通话服务）/Call Service Kit简介/call-introduction.md>)）
* 支持企业联系人来去电显示功能。（[指南](<../../../../../harmonyos-guides/应用服务/Call Service Kit（通话服务）/企业联系人信息来去电页面显示/callservice-enterprise-contact-display.md>)）

## Camera Kit

新增C API和ArkTS API用于设置录像质量的优先级，提供高质量和功耗平衡两档选择。（[C API参考](<../../../../../harmonyos-references/Camera Kit（相机服务）/C API/头文件/capture_session.h/capi-capture-session-h.md#oh_capturesession_setqualityprioritization>)、[ArkTS API参考](<../../../../../harmonyos-references/Camera Kit（相机服务）/ArkTS API/@ohos.multimedia.camera (相机管理)/Interface (VideoSession)/arkts-apis-camera-videosession.md#setqualityprioritization14>)）

## Core File Kit

新增支持获取保存成功后的文件后缀类型的下标。（[API参考](<../../../../../harmonyos-references/Core File Kit（文件基础服务）/ArkTS API/@ohos.file.picker (选择器)/js-apis-file-picker.md#getselectedindex14>)）

## Crypto Architecture Kit

[非对称密钥生成和转换](<../../../../../harmonyos-guides/系统/安全/Crypto Architecture Kit（加解密算法框架服务）/密钥生成和转换/密钥生成和转换规格/非对称密钥生成和转换规格/crypto-asym-key-generation-conversion-spec.md#使用字符串参数生成-1>)、[密钥协商](<../../../../../harmonyos-guides/系统/安全/Crypto Architecture Kit（加解密算法框架服务）/密钥协商/密钥协商介绍及算法规格/crypto-key-agreement-overview.md#ecdh>)、[签名验签](<../../../../../harmonyos-guides/系统/安全/Crypto Architecture Kit（加解密算法框架服务）/签名验签/签名验签介绍及算法规格/crypto-sign-sig-verify-overview.md#ecdsa>)所使用的ECC算法支持secp256k1曲线。

## Data Protection Kit

新增数据防泄漏（DLP）解决方案，通过C API提供对应能力的调用。（[API参考](<../../../../../harmonyos-references/安全/Data Protection Kit（数据保护服务）/C API/模块/DlpPermissionApi/capi-dlppermissionapi.md>)）

## Game Service Kit

* 游戏场景感知模块提供C API。（[API参考](<../../../../../harmonyos-references/Game Service Kit（游戏服务）/C API/gameservice-c.md>)）
* 支持订阅或查询GPU信息时，返回GPU当前频点。（[API参考](<../../../../../harmonyos-references/Game Service Kit（游戏服务）/ArkTS API/gamePerformance (游戏场景感知)/gameservice-gameperformance.md#gpuinfo>)）

## IAP Kit

支持非续期订阅类型商品的购买。（[指南](<../../../../../harmonyos-guides/应用服务/IAP Kit（应用内支付服务）/商品购买/非续期订阅商品购买/iap-nonrenewable.md>)）

## IME Kit

输入法框架提供的编辑框属性新增编辑框所属应用的包名。（[API参考](<../../../../../harmonyos-references/IME Kit（输入法开发服务）/ArkTS API/@ohos.inputMethodEngine (输入法服务)/js-apis-inputmethodengine.md#editorattribute>)）

## Live View Kit

支持设置左右文本模板扩展区文本子样式类型、右侧标题和内容的右上角展示内容、中间间隔文本、扩展区底部内容等。（[API参考](<../../../../../harmonyos-references/Live View Kit（实况窗服务）/ArkTS API/liveViewManager/liveview-liveviewmanager.md#flightlayout>)）

## Location Kit

新增地理围栏类型的ExtensionAbility，提供基于位置的地理围栏的能力。（[指南](<../../../../../harmonyos-guides/应用服务/Location Kit（位置服务）/地理围栏开发指导/云侧围栏开发指导/fenceextensionability.md>)、[API参考](<../../../../../harmonyos-references/Location Kit（位置服务）/ArkTS API/@ohos.app.ability.FenceExtensionAbility (FenceExtensionAbility)/js-apis-app-ability-fenceextensionability.md>)）

## MDM Kit

* 企业应用禁用设备功能的能力新增支持禁用设备相机能力。（[API参考](<../../../../../harmonyos-references/基础功能/MDM Kit（企业设备管理服务）/ArkTS API/@ohos.enterprise.restrictions （限制类策略）/js-apis-enterprise-restrictions.md#restrictionssetdisallowedpolicy>)）
* 企业应用安装事件新增一类回调，该回调返回的信息包括安装包名和账号ID。（[API参考](<../../../../../harmonyos-references/基础功能/MDM Kit（企业设备管理服务）/ArkTS API/@ohos.enterprise.EnterpriseAdminExtensionAbility（企业设备管理扩展能力）/js-apis-enterpriseadminextensionability.md#onbundleadded14>)）
* 企业应用新增支持委托其他应用来设置设备的管控策略。（[API参考](<../../../../../harmonyos-references/基础功能/MDM Kit（企业设备管理服务）/ArkTS API/@ohos.enterprise.adminManager（admin权限管理）/js-apis-enterprise-adminmanager.md#adminmanagersetdelegatedpolicies14>)）
* 企业应用新增支持设置禁用/启用设备指纹功能，该能力目前仅限PC/2in1设备使用。（[API参考](<../../../../../harmonyos-references/基础功能/MDM Kit（企业设备管理服务）/ArkTS API/@ohos.enterprise.restrictions （限制类策略）/js-apis-enterprise-restrictions.md#restrictionssetdisallowedpolicyforaccount14>)）
* 企业应用新增支持设置禁用屏幕快照（即截屏）功能，该能力目前仅限PC/2in1设备使用。（[API参考](<../../../../../harmonyos-references/基础功能/MDM Kit（企业设备管理服务）/ArkTS API/@ohos.enterprise.restrictions （限制类策略）/js-apis-enterprise-restrictions.md#restrictionsadddisallowedlistforaccount14>)）
* 企业应用新增支持对应用设置水印的能力，该能力目前仅限PC/2in1设备使用。（[API参考](<../../../../../harmonyos-references/基础功能/MDM Kit（企业设备管理服务）/ArkTS API/@ohos.enterprise.securityManager（安全管理）/js-apis-enterprise-securitymanager.md#securitymanagersetwatermarkimage14>)）
* 企业应用新增支持“设备管理”应用添加保活的应用，该能力目前仅限PC/2in1设备使用。（[API参考](<../../../../../harmonyos-references/基础功能/MDM Kit（企业设备管理服务）/ArkTS API/@ohos.enterprise.applicationManager（应用管理）/js-apis-enterprise-applicationmanager.md#applicationmanageraddkeepaliveapps14>)）
* 企业应用新增支持“设备管理”应用添加禁止使用的USB设备类型，该能力目前仅限PC/2in1设备使用。（[API参考](<../../../../../harmonyos-references/基础功能/MDM Kit（企业设备管理服务）/ArkTS API/@ohos.enterprise.usbManager（USB管理）/js-apis-enterprise-usbmanager.md#usbmanageradddisallowedusbdevices14>)）

## Media Kit

* 新增C API支持设置录屏时的最大帧率。（[API参考](<../../../../../harmonyos-references/Media Kit（媒体服务）/C API/头文件/native_avscreen_capture.h/capi-native-avscreen-capture-h.md#oh_avscreencapture_setmaxvideoframerate>)）
* 流媒体新增一批错误码以细化流媒体播放可能出现的异常场景。（[API参考](<../../../../../harmonyos-references/Media Kit（媒体服务）/ArkTS API/@ohos.multimedia.media (媒体服务)/Enums/arkts-apis-media-e.md#averrorcode9>)）

## Media Library Kit

* 新增支持定义配置相册图片后的完成按钮，可显示“完成”、“发送”或“添加”。（[API参考](<../../../../../harmonyos-references/Media Library Kit（媒体文件管理服务）/ArkTS API/@ohos.file.photoAccessHelper (相册管理模块)/Enums/arkts-apis-photoaccesshelper-e.md#completebuttontext14>)）
* Photo Picker组件新增支持大图页视频播放状态的回调videoPlayStateChangedCallback。（[API参考](<../../../../../harmonyos-references/Media Library Kit（媒体文件管理服务）/ArkTS组件/@ohos.file.PhotoPickerComponent (PhotoPicker组件)/ohos-file-photopickercomponent.md#videoplaystatechangedcallback14>)）

## Payment Kit

新增通用收银台，支持多种支付方式。（[指南](<../../../../../harmonyos-guides/应用服务/Payment Kit（鸿蒙支付服务）/通用收银台接入/payment-common-pay-connect.md>)）

## Push Kit

支持场景化消息类型为通知消息场景（DEFAULT类型）。（[API参考](<../../../../../harmonyos-references/Push Kit（推送服务）/ArkTS API/pushService（推送服务基础能力）/push-pushservice.md#pushservicepushtype>)）

## Scenario Fusion Kit

* 支持文件路径转换，即可实现将源文件路径转换为目标文件路径。（[指南](<../../../../../harmonyos-guides/应用服务/Scenario Fusion Kit（融合场景服务）/文件路径转换API/scenario-fusion-api-path-conversion.md>)）
* 支持权限设置button，实现二次拉起权限设置弹框。（[指南](<../../../../../harmonyos-guides/应用服务/Scenario Fusion Kit（融合场景服务）/场景化Button/权限设置Button/scenario-fusion-button-permissiononsetting.md>)）

## Speech Kit

* 朗读控件支持在线预录制播报场景。（[API参考](<../../../../../harmonyos-references/Speech Kit（场景化语音服务）/ArkTS API/TextReader（朗读控件）/speech-textreader-api.md#readinfo>)）
* 朗读控件支持[朗读起播](<../../../../../harmonyos-references/Speech Kit（场景化语音服务）/ArkTS API/TextReader（朗读控件）/speech-textreader-api.md#start-1>)以及[起播参数](<../../../../../harmonyos-references/Speech Kit（场景化语音服务）/ArkTS API/TextReader（朗读控件）/speech-textreader-api.md#startparams>)、[朗读参数](<../../../../../harmonyos-references/Speech Kit（场景化语音服务）/ArkTS API/TextReader（朗读控件）/speech-textreader-api.md#readerparam>)的定制。

## Status Bar Extension Kit

支持监听状态栏图标点击事件、右键菜单点击事件。（[API参考-监听状态栏图标点击事件](<../../../../../harmonyos-references/基础功能/Desktop Extension Kit（桌面拓展服务）/ArkTS API/statusBarManager（状态栏管理服务）/statusbar-extension-manager.md#statusbarmanageronstatusbariconclick>)，[API参考-监听右键菜单点击事件](<../../../../../harmonyos-references/基础功能/Desktop Extension Kit（桌面拓展服务）/ArkTS API/statusBarManager（状态栏管理服务）/statusbar-extension-manager.md#statusbarmanageronrightmenuclick>)）

## Store Kit

* 支持应用市场推荐场景下，应用内快捷方式加桌。（[指南](<../../../../../harmonyos-guides/应用服务/AppGallery Kit（应用市场服务）/应用市场推荐/应用内快捷方式/添加桌面快捷方式/appgallery-productview-addshortcut.md>)）
* 应用详情页展示和元服务卡片加桌场景下，支持成功打开和关闭回调函数。（[API参考](<../../../../../harmonyos-references/AppGallery Kit（应用市场服务）/ArkTS API/productViewManager (应用市场推荐)/store-productviewmanager.md#productviewcallback>)）
* 应用详情页展示场景下，支持设置登记归因来源的广告曝光数据属性参数。（[API参考](<../../../../../harmonyos-references/AppGallery Kit（应用市场服务）/ArkTS API/productViewManager (应用市场推荐)/store-productviewmanager.md#skexposure>)）
* 产品特性按需分发新增C接口，支持用户按需动态下载所需的增强特性。（[API参考](<../../../../../harmonyos-references/AppGallery Kit（应用市场服务）/C API/store-c.md>)）
* 支持拉起标准化隐私弹框。（[API参考](<../../../../../harmonyos-references/AppGallery Kit（应用市场服务）/ArkTS API/privacyManager（隐私管理服务）/store-privacymanager.md#privacymanagerrequestappprivacyconsent>)）

## Vision Kit

* 支持对身份证图片质量检测，包括检测身份证图片是否完整、是否反光。（[API参考](<../../../../../harmonyos-references/Vision Kit（场景化视觉服务）/ArkTS组件/CardRecognition（卡证识别控件）/vision-card-recognition.md#idcardconfig>)）
* 支持获取当前图片分析UI状态。（[API参考](<../../../../../harmonyos-references/Vision Kit（场景化视觉服务）/ArkTS API/visionImageAnalyzer（AI识图控件）/vision-image-analyzer.md#getimageanalyzeruistatus>)）

## Weather Service Kit

支持根据调用方提供的上下文信息获取天气数据。（[API参考](<../../../../../harmonyos-references/Weather Service Kit（天气服务）/ArkTS API/weatherService（天气数据服务）/weather-service-weatherservice.md#weatherservicegetweatherwithcontext>)）

## XEngine Kit

新增支持平板和PC/2in1设备。（[指南](<../../../../../harmonyos-guides/图形/XEngine Kit（GPU加速引擎服务）/开发准备/xengine-kit-preparations.md#硬件要求>)）

## 公共

* 配置文件[module.json5中abilities标签](../../../../../harmonyos-guides/基础入门/开发基础知识/应用配置文件（Stage模型）/module.json5配置文件/module-configuration-file.md#abilities标签)的orientation属性新增支持通过资源索引方式（$string）进行配置。
* 配置文件[module.json5中extensionAbilities标签](../../../../../harmonyos-guides/基础入门/开发基础知识/应用配置文件（Stage模型）/module.json5配置文件/module-configuration-file.md#extensionabilities标签)的extensionProcessMode属性新增支持配置runWithMainProcess类型，表示该ExtensionAbility和应用主进程共进程。
* 配置文件[module.json5中extensionAbilities标签](../../../../../harmonyos-guides/基础入门/开发基础知识/应用配置文件（Stage模型）/module.json5配置文件/module-configuration-file.md#extensionabilities标签)新增process属性，type为embeddedUI的ExtensionAbility可通过该属性的配置使ExtensionAbility和Ability运行在同一进程。

## 工具

* 使用[打包工具](../../../../../harmonyos-guides/系统/调测调优/调试命令/打包拆包工具/打包工具/packing-tool.md#app打包指令)打包APP时，支持打包加密配置文件。本特性不涉及命令、接口的新增，仍可参照原有工具指导进行打包操作。
* [mediatool工具](../../../../../harmonyos-guides/系统/调测调优/调试命令/命令行工具/媒体库资源访问工具/mediatool.md#查询命令mediatool-query)查询媒体库资源的命令新增返回资源源文件真实路径或媒体资源uri的参数。
