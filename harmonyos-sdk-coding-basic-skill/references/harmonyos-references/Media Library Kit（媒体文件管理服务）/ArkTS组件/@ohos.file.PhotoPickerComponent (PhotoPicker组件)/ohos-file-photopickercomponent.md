---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-file-photopickercomponent
title: @ohos.file.PhotoPickerComponent (PhotoPicker组件)
breadcrumb: API参考 > 媒体 > Media Library Kit（媒体文件管理服务） > ArkTS组件 > @ohos.file.PhotoPickerComponent (PhotoPicker组件)
category: harmonyos-references
scraped_at: 2026-06-11T16:35:19+08:00
doc_updated_at: 2026-05-26
content_hash: sha256:736a1fed9d952255cbd5de7a80e12f581cb78c9835cc4030f85ccc85490112a0
---
应用可以在布局中嵌入PhotoPicker组件，通过此组件，应用无需申请权限，即可实现媒体文件选择功能。在用户选择媒体文件后，应用即可访问用户选中的图片或视频文件。仅包含读权限。

需要注意的是PhotoPickerComponent不能嵌套使用，且不建议在PhotoPickerComponent上覆盖设置了overlay属性的组件，将导致PhotoPickerComponent无法接受手势事件。

应用嵌入组件后，用户可直接在PhotoPicker组件中选择图片或视频文件。

说明

* 该组件从API version 12开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。
* 该组件不支持[同层渲染](../../../../harmonyos-guides/应用框架/ArkWeb（方舟Web）/同层渲染/web-same-layer.md)。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. // 在API version 23之前的版本中，需要使用'import { api1, api2, ... } from @ohos.file.PhotoPickerComponent'的导入方式。
2. import {
3. PhotoPickerComponent, PickerController, PickerOptions,
4. DataType, BaseItemInfo, ItemInfo, PhotoBrowserInfo, ItemType, ClickType,
5. MaxCountType, PhotoBrowserRange, PhotoBrowserUIElement,
6. ItemsDeletedCallback, ExceedMaxSelectedCallback, CurrentAlbumDeletedCallback, SingleLineConfig,
7. BadgeConfig, PreselectedInfo, SaveMode, BadgeType, VideoPlayerState, ItemDisplayRatio
8. } from '@kit.MediaLibraryKit';
```

## 属性

PhonePC/2in1TabletTVWearable

支持[通用属性](../../../ArkUI（方舟UI框架）/ArkTS组件/通用属性/ts-component-general-attributes.md)。

## PhotoPickerComponent

PhonePC/2in1TabletTVWearable

PhotoPickerComponent({ pickerOptions?: PickerOptions, onSelect?: (uri: string) => void, onDeselect?: (uri: string) => void, onItemClicked?: (itemInfo: ItemInfo, clickType: ClickType) => boolean, onItemClickedNotify?: ItemClickedNotifyCallback, onEnterPhotoBrowser?: (photoBrowserInfo: PhotoBrowserInfo) => boolean, onExitPhotoBrowser?: (photoBrowserInfo: PhotoBrowserInfo) => boolean, onPickerControllerReady?: () => void, onPhotoBrowserChanged?: (browserItemInfo: BaseItemInfo) => boolean, onSelectedItemsDeleted?: ItemsDeletedCallback, onExceedMaxSelected?: ExceedMaxSelectedCallback, onCurrentAlbumDeleted?: CurrentAlbumDeletedCallback, onVideoPlayStateChanged?: videoPlayStateChangedCallback, pickerController: PickerController })

应用可以在布局中嵌入PhotoPickerComponent组件，通过此组件，应用无需申请权限，即可访问公共目录中的图片或视频文件。

说明

如果当前PhotoPickerComponent组件嵌套在Tabs组件中使用，Tabs组件的左右滑动会与图片选择大图界面的左右滑动切换手势发生冲突。

可在进退大图的回调中设置Tabs组件是否支持滑动来规避，该问题将在后续版本修复。

**装饰器类型**：@Component

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 名称 | 类型 | 必填 | 装饰器类型 | 说明 |
| --- | --- | --- | --- | --- |
| pickerOptions | [PickerOptions](ohos-file-photopickercomponent.md#pickeroptions) | 否 | - | picker配置参数信息。  **元服务API**：从API version 12开始，该接口支持在元服务中使用。 |
| onSelect | (uri: string) => void | 否 | - | 用户在Picker组件中勾选图片时产生的回调事件，将图片uri报给应用。  **元服务API**：从API version 12开始，该接口支持在元服务中使用。 |
| onDeselect | (uri: string) => void | 否 | - | 用户在Picker组件中取消勾选图片时产生的回调事件，同时也会将图片uri报给应用。  **元服务API**：从API version 12开始，该接口支持在元服务中使用。 |
| onItemClicked | (itemInfo: [ItemInfo](ohos-file-photopickercomponent.md#iteminfo), clickType: [ClickType](ohos-file-photopickercomponent.md#clicktype)) => boolean | 否 | - | 用户在picker组件中点击宫格产生的回调事件。  点击图片（缩略图宫格）时，返回值为true则勾选此图片，否则不响应勾选，URI不授权；点击相机宫格，返回值为true则拉起系统相机，否则不拉起相机，由应用自行处理。  **元服务API**：从API version 12开始，该接口支持在元服务中使用。 |
| onItemClickedNotify23+ | [ItemClickedNotifyCallback](ohos-file-photopickercomponent.md#itemclickednotifycallback23) | 否 | - | 用户在picker组件中点击宫格产生的回调事件。  应用可执行自身是否选中逻辑，需要配合addData方法一同使用，通过ADD\_ITEM\_CLICK\_RESULT进行选中或不选中。若未设置选中结果，在2秒或PhotoPicker被关闭时取消授权。  **模型约束：** 此接口仅可在Stage模型下使用。  **元服务API**：从API version 23开始，该接口支持在元服务中使用。 |
| onPinchGridSwitched23+ | [PinchGridSwitchedCallback](ohos-file-photopickercomponent.md#pinchgridswitchedcallback23) | 否 | - | 宫格捏合时产生的回调事件。仅在[GridPinchModeType](<../../ArkTS API/@ohos.file.photoAccessHelper (相册管理模块)/Enums/arkts-apis-photoaccesshelper-e.md#gridpinchmodetype23>)配置为FULL\_FUNCTION\_GRID时被触发。  **模型约束：** 此接口仅可在Stage模型下使用。  **元服务API**：从API version 23开始，该接口支持在元服务中使用。 |
| onEnterPhotoBrowser | (photoBrowserInfo: [PhotoBrowserInfo](ohos-file-photopickercomponent.md#photobrowserinfo)) => boolean | 否 | - | 点击进入大图时产生的回调事件，将大图相关信息报给应用。不对返回值做特殊处理。  **元服务API**：从API version 12开始，该接口支持在元服务中使用。 |
| onExitPhotoBrowser | (photoBrowserInfo: [PhotoBrowserInfo](ohos-file-photopickercomponent.md#photobrowserinfo)) => boolean | 否 | - | 退出大图时产生的回调事件，将大图相关信息报给应用。不对返回值做特殊处理。  **元服务API**：从API version 12开始，该接口支持在元服务中使用。 |
| onPickerControllerReady | () => void | 否 | - | 当pickerController可用时产生的回调事件。  调用PickerController相关接口需在该回调后才能生效。  **元服务API**：从API version 12开始，该接口支持在元服务中使用。 |
| onPhotoBrowserChanged | (browserItemInfo: [BaseItemInfo](ohos-file-photopickercomponent.md#baseiteminfo)) => boolean | 否 | - | 大图左右滑动时产生的回调事件，将大图相关信息报给应用。仅在多选模式下生效。不对返回值做特殊处理。  **元服务API**：从API version 12开始，该接口支持在元服务中使用。 |
| onSelectedItemsDeleted13+ | [ItemsDeletedCallback](ohos-file-photopickercomponent.md#itemsdeletedcallback13) | 否 | - | 已勾选的图片被删除时产生的回调，并将被删除图片的相关信息回调给应用。  **元服务API**：从API version 13开始，该接口支持在元服务中使用。 |
| onExceedMaxSelected13+ | [ExceedMaxSelectedCallback](ohos-file-photopickercomponent.md#exceedmaxselectedcallback13) | 否 | - | 选择达到最大选择数量（最大图片选择数量或者是最大视频选择数量亦或是总的最大选择数量）之后再次点击勾选时产生的回调。  - 若选择的数量达到了最大图片选择数量且未达到总的最大选择数量则回调的参数exceedMaxCountType为[MaxCountType](ohos-file-photopickercomponent.md#maxcounttype).PHOTO\_MAX\_COUNT。  - 若选择的数量达到了最大视频选择数量且未达到总的最大选择数量则回调的参数exceedMaxCountType为[MaxCountType](ohos-file-photopickercomponent.md#maxcounttype).VIDEO\_MAX\_COUNT。  - 只要选择的数量达到了总的最大选择数量则回调的参数exceedMaxCountType为[MaxCountType](ohos-file-photopickercomponent.md#maxcounttype).TOTAL\_MAX\_COUNT。  **元服务API**：从API version 13开始，该接口支持在元服务中使用。 |
| onCurrentAlbumDeleted13+ | [CurrentAlbumDeletedCallback](ohos-file-photopickercomponent.md#currentalbumdeletedcallback13) | 否 | - | 当前相册被删除时产生的回调。  当前相册是指通过pickerController.[setData](ohos-file-photopickercomponent.md#setdata)([DataType](ohos-file-photopickercomponent.md#datatype).SET\_ALBUM\_URI, currentAlbumUri)接口设置给宫格组件的相册，即“currentAlbumUri”。  当前相册被删除后若使用方刷新自己的相册标题栏，使用方可以设置自己的标题栏名称为默认的相册名例如“图片和视频”、“图片”或“视频”，然后通过pickerController.[setData](ohos-file-photopickercomponent.md#setdata)([DataType](ohos-file-photopickercomponent.md#datatype).SET\_ALBUM\_URI, '')接口传空串去刷新宫格页为默认相册。  **元服务API**：从API version 13开始，该接口支持在元服务中使用。 |
| onVideoPlayStateChanged14+ | [videoPlayStateChangedCallback](ohos-file-photopickercomponent.md#videoplaystatechangedcallback14) | 否 | - | 大图页视频播放状态改变时回调。  **元服务API**：从API version 14开始，该接口支持在元服务中使用。 |
| pickerController | [PickerController](ohos-file-photopickercomponent.md#pickercontroller) | 是 | @ObjectLink | 应用可通过PickerController向Picker组件发送数据。  **元服务API**：从API version 12开始，该接口支持在元服务中使用。 |
| onMovingPhotoBadgeStateChanged22+ | [MovingPhotoBadgeStateChangedCallback](ohos-file-photopickercomponent.md#movingphotobadgestatechangedcallback22) | 否 | - | 用户在Picker组件中打开/关闭动态效果时产生的回调。将图片uri和动态照片状态报给应用。  **元服务API**：从API version 22开始，该接口支持在元服务中使用。 |
| onScrollStopAtStart23+ | [ScrollStopAtStartCallback](ohos-file-photopickercomponent.md#scrollstopatstartcallback23) | 否 | - | 用户在Picker组件滑动停止、处于宫格内容起始位置时的回调。  **模型约束：** 此接口仅可在Stage模型下使用。  **元服务API**：从API version 23开始，该接口支持在元服务中使用。 |
| onScrollStopAtEnd23+ | [ScrollStopAtEndCallback](ohos-file-photopickercomponent.md#scrollstopatendcallback23) | 否 | - | 用户在Picker组件滑动停止、处于宫格内容结束位置时的回调。  **模型约束：** 此接口仅可在Stage模型下使用。  **元服务API**：从API version 23开始，该接口支持在元服务中使用。 |
| onPhotoBrowserChangeStart23+ | [PhotoBrowserChangeStartCallback](ohos-file-photopickercomponent.md#photobrowserchangestartcallback23) | 否 | - | 宫格视图进入到大图视图、大图浏览切换时产生的回调。  **模型约束：** 此接口仅可在Stage模型下使用。  **元服务API**：从API version 23开始，该接口支持在元服务中使用。 |
| onError23+ | [ErrorCallback](ohos-file-photopickercomponent.md#errorcallback23) | 否 | - | 使用PhotoPickerComponent组件发生错误时产生的回调。  **模型约束：** 此接口仅可在Stage模型下使用。  **元服务API**：从API version 23开始，该接口支持在元服务中使用。 |

## PickerOptions

PhonePC/2in1TabletTVWearable

Picker配置选项，继承自[photoAccessHelper.BaseSelectOptions](<../../ArkTS API/@ohos.file.photoAccessHelper (相册管理模块)/Classes (其他)/arkts-apis-photoaccesshelper-class.md#baseselectoptions>)。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| checkBoxColor | string | 否 | 是 | 勾选框的背景色。  格式为8位十六进制颜色代码。前2位表示透明度，后6位表示RGB颜色值。  示例：'#FFFFFFFF'表示白色不透明背景；'#80FF0000'表示半透明红色背景。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| backgroundColor | string | 否 | 是 | picker宫格页面背景色。格式为8位十六进制颜色代码。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| isRepeatSelectSupported | boolean | 否 | 是 | 是否支持单张图片重复选择。true表示支持，false表示不支持。默认值为false。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| checkboxTextColor | string | 否 | 是 | 勾选框内文本颜色。格式为8位十六进制颜色代码（该能力从API version 19开始支持，API version 19之前系统默认为白色）。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| photoBrowserBackgroundColorMode | [PickerColorMode](ohos-file-photopickercomponent.md#pickercolormode) | 否 | 是 | 大图背景颜色。包括跟随系统、浅色模式以及深色模式，默认为跟随系统。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| maxSelectedReminderMode | [ReminderMode](ohos-file-photopickercomponent.md#remindermode) | 否 | 是 | 选择数量达到最大时的提示方式。包括弹toast提示、不提示以及蒙层提示，默认为弹toast提示。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| orientation | [PickerOrientation](ohos-file-photopickercomponent.md#pickerorientation) | 否 | 是 | 宫格页面滑动预览方向，包括水平和竖直两个方向，默认为竖直方向（该能力从API version 20开始支持，API version 20之前系统默认为竖直方向）。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| selectMode | [SelectMode](ohos-file-photopickercomponent.md#selectmode) | 否 | 是 | 选择模式。包括多选和单选，默认为多选。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| maxPhotoSelectNumber | number | 否 | 是 | 图片最大的选择数量。最大值为500，受到最大选择总数的限制。默认为500。  **模型约束：** 此接口仅可在Stage模型下使用。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| maxVideoSelectNumber | number | 否 | 是 | 视频最大的选择数量。最大值为500，受到系统中所有媒体文件最大选择总数的限制。默认为500。  **模型约束：** 此接口仅可在Stage模型下使用。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| isSlidingSelectionSupported13+ | boolean | 否 | 是 | 是否支持滑动多选，true表示支持，false表示不支持。默认值为false。重复选择场景不支持滑动多选。  **元服务API：** 从API version 13开始，该接口支持在元服务中使用。 |
| photoBrowserCheckboxPosition13+ | [number, number] | 否 | 是 | 设置大图页checkbox的位置。第一个参数为X方向偏移量，第二个参数为Y方向偏移量。传参范围[0, 1]，代表距离组件左上角0%-100%的偏移量。默认值为[0, 0]。  **元服务API：** 从API version 13开始，该接口支持在元服务中使用。 |
| gridMargin14+ | [Margin](../../../ArkUI（方舟UI框架）/ArkTS组件/通用属性/布局与边框/尺寸设置/ts-universal-attributes-size.md#margin) | 否 | 是 | 设置组件宫格页margin。  **元服务API：** 从API version 14开始，该接口支持在元服务中使用。 |
| photoBrowserMargin14+ | [Margin](../../../ArkUI（方舟UI框架）/ArkTS组件/通用属性/布局与边框/尺寸设置/ts-universal-attributes-size.md#margin) | 否 | 是 | 设置组件大图页margin。  **元服务API：** 从API version 14开始，该接口支持在元服务中使用。 |
| singleLineConfig20+ | [SingleLineConfig](ohos-file-photopickercomponent.md#singlelineconfig20) | 否 | 是 | 设置组件宫格页单行显示模式。单行模式下，组件不提供打开大图浏览相关功能。组件不支持大图相关回调，PickerController不支持大图相关的接口，接口调用将无效。  **元服务API：** 从API version 20开始，该接口支持在元服务中使用。 |
| uiComponentColorMode20+ | [PickerColorMode](ohos-file-photopickercomponent.md#pickercolormode) | 否 | 是 | Picker的颜色模式。Picker宫格界面除背景色之外其他组件的深浅色风格，包括搜索框、相机入口、安全使用图库提示组件、推荐气泡等组件，一般与backgroundColor配合使用。默认为PickerColorMode.AUTO，跟随系统深浅色切换。  该属性一般设置PickerColorMode.LIGHT时不与深颜色的backgroundColor搭配；设置PickerColorMode.DARK时不与浅颜色的backgroundColor搭配，否则会出现组件背景或文字无法看清楚的问题。  **元服务API：** 从API version 20开始，该接口支持在元服务中使用。 |
| gridStartOffset20+ | number | 否 | 是 | 组件宫格缩略图第一行与组件顶部的预留空间。默认值0，单位vp。  **元服务API：** 从API version 20开始，该接口支持在元服务中使用。 |
| gridEndOffset20+ | number | 否 | 是 | 组件宫格缩略图最后一行与组件底部的预留空间。默认值0，单位vp。  **元服务API：** 从API version 20开始，该接口支持在元服务中使用。 |
| pickerIndex21+ | number | 否 | 是 | 通过设置唯一序号来区分不同的pickerComponent。默认值为-1，-1时不做区分。  **元服务API：** 从API version 21开始，该接口支持在元服务中使用。 |
| preselectedInfos21+ | Array<[PreselectedInfo](ohos-file-photopickercomponent.md#preselectedinfo21)> | 否 | 是 | 支持在指定pickerIndex的PhotoPickerComponent中回显用户已选择的数据。  **元服务API：** 从API version 21开始，该接口支持在元服务中使用。 |
| badgeConfig21+ | [BadgeConfig](ohos-file-photopickercomponent.md#badgeconfig21) | 否 | 是 | 支持配置特殊角标显示。Picker目前仅支持一种类型的角标，详见[BadgeType](ohos-file-photopickercomponent.md#badgetype21)。  **元服务API：** 从API version 21开始，该接口支持在元服务中使用。 |
| isSlidingSupported23+ | boolean | 否 | 是 | 是否屏蔽PhotoPickerComponent的滚动。true表示不屏蔽滚动事件，响应用户滚动。false表示屏蔽滚动事件，不响应用户滚动。  默认为true。  **模型约束**：此接口仅可在Stage模型下使用。  **元服务API**：从API version 23开始，该接口支持在元服务中使用。 |
| edgeEffect23+ | [EdgeEffect](../../../ArkUI（方舟UI框架）/ArkTS组件/公共定义/枚举说明/ts-appendix-enums.md#edgeeffect) | 否 | 是 | Picker宫格页滑动到边缘处的滑动效果。  默认为[EdgeEffect.Spring](../../../ArkUI（方舟UI框架）/ArkTS组件/公共定义/枚举说明/ts-appendix-enums.md#edgeeffect)。  **模型约束：** 此接口仅可在Stage模型下使用。  **元服务API**：从API version 23开始，该接口支持在元服务中使用。 |
| appAlbumFilters23+ | Array<string> | 否 | 是 | 仅显示与指定bundle name对应的相册内容。  **模型约束：** 此接口仅可在Stage模型下使用。  **元服务API**：从API version 23开始，该接口支持在元服务中使用。 |
| backgroundOpacity24+ | number | 否 | 是 | 支持配置picker背景透明度。取值范围为[0, 1]，0表示完全透明，1表示完全不透明。  **模型约束：** 此接口仅可在Stage模型下使用。  **元服务API**：从API version 24开始，该接口支持在元服务中使用。 |

## ItemsDeletedCallback13+

PhonePC/2in1TabletTVWearable

type ItemsDeletedCallback = (baseItemInfos: Array<BaseItemInfo>) => void

已勾选的图片被删除时产生的回调事件。

**元服务API：** 从API version 13开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| baseItemInfos | Array<[BaseItemInfo](ohos-file-photopickercomponent.md#baseiteminfo)> | 是 | 照片的基本信息。 |

## ExceedMaxSelectedCallback13+

PhonePC/2in1TabletTVWearable

type ExceedMaxSelectedCallback = (exceedMaxCountType: MaxCountType) => void

选择达到最大选择数量之后再次点击勾选时的回调事件。

**元服务API：** 从API version 13开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| exceedMaxCountType | [MaxCountType](ohos-file-photopickercomponent.md#maxcounttype) | 是 | 达到最大选择数量的类型。类型包含图片最大选择数量、视频最大选择数量以及总的最大选择数量。 |

## CurrentAlbumDeletedCallback13+

PhonePC/2in1TabletTVWearable

type CurrentAlbumDeletedCallback = () => void

当前相册被删除时的回调事件。

**元服务API：** 从API version 13开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

## videoPlayStateChangedCallback14+

PhonePC/2in1TabletTVWearable

type videoPlayStateChangedCallback = (state: VideoPlayerState) => void

大图页视频播放状态改变时的回调事件。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| state | [VideoPlayerState](ohos-file-photopickercomponent.md#videoplayerstate14) | 是 | 视频播放状态。 |

## MovingPhotoBadgeStateChangedCallback22+

PhonePC/2in1TabletTVWearable

type MovingPhotoBadgeStateChangedCallback = (uri: string, state: photoAccessHelper.MovingPhotoBadgeStateType) => void

用户在Picker组件中打开/关闭动态效果时的回调事件。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| uri | string | 是 | 动态照片uri。 |
| state | [photoAccessHelper.MovingPhotoBadgeStateType](<../../ArkTS API/@ohos.file.photoAccessHelper (相册管理模块)/Enums/arkts-apis-photoaccesshelper-e.md#movingphotobadgestatetype22>) | 是 | 动态照片状态。 |

## ScrollStopAtStartCallback23+

PhonePC/2in1TabletTVWearable

type ScrollStopAtStartCallback = () => void

表示用户滑动picker宫格页，当滚动停止并处于宫格内容开始位置时的回调事件类型。

**模型约束**： 此接口仅可在Stage模型下使用。

**元服务API：** 从API version 23开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

## ItemClickedNotifyCallback23+

PhonePC/2in1TabletTVWearable

type ItemClickedNotifyCallback = (itemInfo: ItemInfo, clickType: ClickType) => void

用户在picker组件中点击宫格产生的回调事件。

**模型约束**： 此接口仅可在Stage模型下使用。

**元服务API：** 从API version 23开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| itemInfo | [ItemInfo](ohos-file-photopickercomponent.md#iteminfo) | 是 | 被点击的宫格类型。包括缩略图宫格和相机宫格。 |
| clickType | [ClickType](ohos-file-photopickercomponent.md#clicktype) | 是 | 点击操作的类型。 |

**示例：**

```
1. import {
2. ClickType,
3. DataType,
4. ItemInfo,
5. PhotoPickerComponent,
6. PickerController,
7. PickerOptions,
8. } from '@kit.MediaLibraryKit';
9. import { ClickResult, ItemClickedNotifyCallback } from '@ohos.file.PhotoPickerComponent';

11. const DOMAIN = 0x0000;
12. const TAG: string = 'clickedNotifyDemo';

14. interface Checks {
15. isOnClicked: boolean;
16. isOnClickedNotify: boolean;
17. }

19. export interface ClickResultEx {
20. uri: string,
21. isSelected: boolean,
22. }

24. @Entry
25. @Component
26. struct PickerPage {
27. @State pickerController: PickerController = new PickerController();
28. private pickerOptions: PickerOptions = new PickerOptions();
29. @State currentUri: string = '';
30. @State currentState: number = 0;
31. @State clickedUris: Map<string, ClickResultEx> = new Map();
32. private isOnClicked: boolean = false;
33. private isOnClickedNotify: boolean = false;

35. onClicked: (itemInfo: ItemInfo, clickType: ClickType) => boolean = (itemInfo: ItemInfo, clickType: ClickType) => {
36. return true;
37. };
38. // 当一个宫格被点击时，代码会验证该宫格对应URI是否有效，如无效，则忽略。
39. // 然后，会检查clickedUris中否已存在该URI的记录。如没有，则创建一条记录并将isSelected属性设置为true。
40. // 如果记录存在，则将该记录的isSelected属性更新为true。
41. // 数据保存完成后点击“setClickResult”按钮，会调用addData(SET_ITEM_CLICK_RESULT)将对应宫格设置为选中状态。
42. onClickedNotify: ItemClickedNotifyCallback = (itemInfo: ItemInfo, clickType: ClickType) => {
43. if (!itemInfo.uri) {
44. return;
45. }

47. let clickResult = this.clickedUris.get(itemInfo.uri);
48. if (!clickResult) {
49. clickResult = {
50. uri: itemInfo.uri,
51. isSelected: true,
52. };
53. } else {
54. clickResult.isSelected = true;
55. }
56. this.clickedUris.set(itemInfo.uri, clickResult);
57. };

59. aboutToAppear(): void {
60. let params = this.getUIContext().getRouter().getParams() as Checks;

62. this.pickerOptions.isSlidingSelectionSupported = true;
63. this.pickerOptions.isSearchSupported = false;
64. this.isOnClicked = params.isOnClicked;
65. // 从index.ets页面获取参数。
66. this.isOnClickedNotify = params.isOnClickedNotify;
67. this.pickerOptions.maxPhotoSelectNumber = 500;
68. }

70. // 从this.clickedUris获取这些URI，后续在调用pickerController.addData()设置宫格item选中时使用。
71. getClickedUris(): ClickResult[] {
72. let uris: ClickResultEx[] = [];
73. this.clickedUris.forEach((uri, index) => {
74. uris.push(uri)
75. })
76. return uris;
77. }

79. build() {
80. Column() {
81. Row() {
82. // 照片选择器组件调用。
83. PhotoPickerComponent({
84. pickerOptions: this.pickerOptions,
85. pickerController: this.pickerController,
86. onItemClicked: this.isOnClicked ? this.onClicked : undefined,
87. onItemClickedNotify: this.isOnClickedNotify ? this.onClickedNotify : undefined,
88. onSelect: (uri: string) => {},
89. onDeselect: (uri: string) => {}
90. })
91. }.height('50%')

93. Row() {
94. Column() {
95. Text('Selected assets')
96. ForEach(this.getClickedUris(), (uri: ClickResult) => {
97. Row() {
98. // 能够移除选择或添加选择。
99. Checkbox({ name: "OnClick" })
100. .select(uri.isSelected)
101. .onChange((checked: boolean) => {
102. let clickResult = this.clickedUris.get(uri.uri);
103. if (!clickResult) {
104. clickResult = {
105. uri: uri.uri,
106. isSelected: checked
107. };
108. } else {
109. clickResult.isSelected = checked;
110. }
111. if (uri.uri !== 'abnormal') {
112. this.clickedUris.set(uri.uri, clickResult);
113. }
114. }).margin({ right: 5 })
115. Text(uri.uri.slice(-30)).margin({right: 5}).width(150)
116. // 从this.clickeduris中移除选择项。
117. Button('Delete').onClick(() => {
118. this.clickedUris.delete(uri.uri);
119. })
120. // 此处代码为异常场景样例，当传入异常URI时，picker宫格选中不生效。
121. Button('Abnormal').onClick(() => {
122. let clickResult = this.clickedUris.get(uri.uri);
123. if (clickResult) {
124. let oldClickUri = clickResult.uri;
125. clickResult.uri = 'abnormal'
126. this.clickedUris.set(oldClickUri, clickResult)
127. }
128. })
129. }.width('100%')
130. })
131. }
132. }.height('20%')

134. Row() {
135. // 发送URI(SET_ITEM_CLICK_RESULT)。
136. Button('Set ClickResult')
137. .onClick(() => {
138. this.pickerController.addData(DataType.SET_ITEM_CLICK_RESULT, this.getClickedUris())
139. })
140. }.height('10%')
141. }
142. .height('100%')
143. .width('100%')
144. }
145. }
```

## ScrollStopAtEndCallback23+

PhonePC/2in1TabletTVWearable

type ScrollStopAtEndCallback = () => void

表示用户滑动picker宫格页，当滚动停止并处于宫格内容结束位置时的回调事件类型。

**模型约束**： 此接口仅可在Stage模型下使用。

**元服务API：** 从API version 23开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

## PhotoBrowserChangeStartCallback23+

PhonePC/2in1TabletTVWearable

type PhotoBrowserChangeStartCallback = (targetPhotoInfo: BaseItemInfo) => void

宫格视图进入到大图视图、大图浏览切换时产生的回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从API version 23开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| targetPhotoInfo | [BaseItemInfo](ohos-file-photopickercomponent.md#baseiteminfo) | 是 | 照片的基本信息。 |

## PinchGridSwitchedCallback23+

PhonePC/2in1TabletTVWearable

type PinchGridSwitchedCallback = (gridLevel: photoAccessHelper.GridLevel) => void

用户在宫格组件内捏合时产生的回调事件。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从API version 23开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| gridLevel | [photoAccessHelper.GridLevel](<../../ArkTS API/@ohos.file.photoAccessHelper (相册管理模块)/Enums/arkts-apis-photoaccesshelper-e.md#gridlevel23>) | 是 | 宫格列数的档位。 |

## ErrorCallback23+

PhonePC/2in1TabletTVWearable

type ErrorCallback = (pickerError: PickerError) => void

PhotoPickerComponent产生错误时的回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从API version 23开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| pickerError | [PickerError](ohos-file-photopickercomponent.md#pickererror23) | 是 | 产生的错误的基本信息。 |

## PickerController

PhonePC/2in1TabletTVWearable

应用可通过PickerController向picker组件发送数据。

**装饰器类型**：@Observed

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

### setData

PhonePC/2in1TabletTVWearable

setData(dataType: DataType, data: Object): void

应用可通过该接口向picker组件发送数据，并通过DataType来区分具体发送什么类型的数据。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| dataType | [DataType](ohos-file-photopickercomponent.md#datatype) | 是 | 发送数据的数据类型。 |
| data | Object | 是 | 发送的数据。 |

### addData21+

PhonePC/2in1TabletTVWearable

addData(dataType: DataType, data: Object): void

应用可通过该接口向picker组件发送增加配置数据。通过[DataType](ohos-file-photopickercomponent.md#datatype)来区分具体发送的数据类型，该方法仅支持SET\_BADGE\_CONFIGS类型。

**元服务API**：从API version 21开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| dataType | [DataType](ohos-file-photopickercomponent.md#datatype) | 是 | 发送增加配置数据的数据类型。 |
| data | Object | 是 | 发送的增加配置数据。 |

### deleteData21+

PhonePC/2in1TabletTVWearable

deleteData(dataType: DataType, data: Object): void

应用可通过该接口向picker组件发送移除配置数据。通过[DataType](ohos-file-photopickercomponent.md#datatype)来区分具体发送的数据类型，该方法仅支持SET\_BADGE\_CONFIGS类型。

**元服务API**：从API version 21开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| dataType | [DataType](ohos-file-photopickercomponent.md#datatype) | 是 | 发送移除配置数据的数据类型。 |
| data | Object | 是 | 发送的移除配置数据。 |

### setMaxSelected

PhonePC/2in1TabletTVWearable

setMaxSelected(maxSelected: MaxSelected): void

应用可通过该接口，实时地设置图片的最大选择数量、视频的最大选择数量以及总的最大选择数量。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| maxSelected | [MaxSelected](ohos-file-photopickercomponent.md#maxselected) | 是 | 最大选择数量。 |

### setPhotoBrowserItem

PhonePC/2in1TabletTVWearable

setPhotoBrowserItem(uri: string, photoBrowserRange?: PhotoBrowserRange): void

应用可通过该接口,切换picker组件至大图浏览模式浏览图片；当已处于大图浏览模式时，切换浏览的图片。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| uri | string | 是 | 指定大图浏览的图片uri。仅支持指定用户已选择的图片，未选择的图片不生效。 |
| photoBrowserRange | [PhotoBrowserRange](ohos-file-photopickercomponent.md#photobrowserrange) | 否 | 打开大图浏览模式后，左右滑动切换浏览图片的范围，可配置仅浏览用户选择的或浏览全部图片，视频。默认：PhotoBrowserRange.ALL。浏览全部图片，视频。 |

### exitPhotoBrowser13+

PhonePC/2in1TabletTVWearable

exitPhotoBrowser(): void

应用可通过该接口，向picker发送退出大图的通知。

**元服务API**：从API version 13开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

### setPhotoBrowserUIElementVisibility13+

PhonePC/2in1TabletTVWearable

setPhotoBrowserUIElementVisibility(elements: Array<PhotoBrowserUIElement>, isVisible: boolean): void

应用可通过该接口，设置大图页大图预览组件外其他UI元素是否可见。不设置则默认可见。

**元服务API**：从API version 13开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| elements | Array<[PhotoBrowserUIElement](ohos-file-photopickercomponent.md#photobrowseruielement13)> | 是 | 大图页大图预览组件外其他UI元素。 |
| isVisible | boolean | 是 | 设置的elements元素是否可见。true表示可见，false表示不可见。默认值为false。 |

### replacePhotoPickerPreview15+

PhonePC/2in1TabletTVWearable

replacePhotoPickerPreview(originalUri: string, newUri: string, callback: AsyncCallback<void>): void

应用可通过该接口，将photoPicker中用户勾选的图片替换为应用后期编辑修改后的图片。

**元服务API**：从API version 15开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| originalUri | string | 是 | 原uri，将会被替换掉的uri。 |
| newUri | string | 是 | 新uri，即替换后的uri。基于originalUri修改后期望在photoPicker上替换originalUri显示的，暂存在应用沙箱的图片/视频uri。 |
| callback | AsyncCallback<void> | 是 | 调用接口完成替换后的回调。 |

### saveTrustedPhotoAssets15+

PhonePC/2in1TabletTVWearable

saveTrustedPhotoAssets(trustedUris: Array<string>, callback: AsyncCallback<Array<string>>, configs?: Array<photoAccessHelper.PhotoCreationConfig>, saveMode?: SaveMode): void

应用可通过该接口，保存对应uri列表的文件。使用时，一般结合[replacePhotoPickerPreview](ohos-file-photopickercomponent.md#replacephotopickerpreview15)接口使用，将替换显示成功后的应用沙箱图片/视频newUris保存到图库。

**元服务API**：从API version 15开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| trustedUris | Array<string> | 是 | 需要保存到图库的应用沙箱图片/视频uri。trustedUris一般来自[replacePhotoPickerPreview](ohos-file-photopickercomponent.md#replacephotopickerpreview15)替换显示成功的newUri。 |
| callback | AsyncCallback<Array<string>> | 是 | 返回保存后新生成的媒体库文件对应的uri。 |
| configs | Array<[photoAccessHelper.PhotoCreationConfig](<../../ArkTS API/@ohos.file.photoAccessHelper (相册管理模块)/Interfaces (其他)/arkts-apis-photoaccesshelper-i.md#photocreationconfig12>)> | 否 | 需要保存的文件对应的配置参数。  **注意：**  1. 传入subtype选项，配置项不生效，仅支持保存DEFAULT类型图片。  默认使用trustedUris对应mediaItem的title、fileNameExtension和photoType值，且subtype固定为DEFAULT。  2. 该参数在[SaveMode](ohos-file-photopickercomponent.md#savemode15)为OVERWRITE下不生效。 |
| saveMode | [SaveMode](ohos-file-photopickercomponent.md#savemode15) | 否 | 图片保存模式。  默认使用SAVE\_AS模式保存为新图片。 |

### updatePickerOptions22+

PhonePC/2in1TabletTVWearable

updatePickerOptions(updateConfig: UpdatablePickerConfigs): Promise<void>

应用通过该接口，更新PhotoPickerComponent的属性。使用Promise异步回调。

**元服务API**：从API version 22开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| updateConfig | [UpdatablePickerConfigs](ohos-file-photopickercomponent.md#updatablepickerconfigs22) | 是 | 支持更新的PhotoPickerComponent属性，为[PickerOptions](ohos-file-photopickercomponent.md#pickeroptions)的子集。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

### saveTrustedPhotoAssetsEx23+

PhonePC/2in1TabletTVWearable

saveTrustedPhotoAssetsEx(trustedUris: Array<string>,settings?: Array<photoAccessHelper.CreationSetting>, saveMode?: SaveMode): Promise<Array<string>>

应用可通过该接口保存对应URI列表中的文件。使用Promise异步回调。

说明

此接口通常与[replacePhotoPickerPreview](ohos-file-photopickercomponent.md#replacephotopickerpreview15)接口结合使用，以保存替换显示成功后的应用沙箱图片或视频newUris到图库。

**模型约束**：此接口仅可在Stage模型下使用。

**元服务API**：从API version 23开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| trustedUris | Array<string> | 是 | 需要保存到图库的应用沙箱图片或视频URI。  trustedUris一般来自[replacePhotoPickerPreview](ohos-file-photopickercomponent.md#replacephotopickerpreview15)替换显示成功后的应用沙箱图片或视频newUri。 |
| settings | Array<[photoAccessHelper.CreationSetting](<../../ArkTS API/@ohos.file.photoAccessHelper (相册管理模块)/Interfaces (其他)/arkts-apis-photoaccesshelper-i.md#creationsetting23>)> | 否 | 需要保存的文件对应的配置参数。  默认使用trustedUris对应mediaItem的title、fileNameExtension和photoType值。 |
| saveMode | [SaveMode](ohos-file-photopickercomponent.md#savemode15) | 否 | 图片或视频的保存模式。  默认使用SAVE\_AS模式保存为新图片。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<Array<string>> | Promise对象，返回保存后新生成的媒体库文件对应的URI。 |

### setMovingPhotoState23+

PhonePC/2in1TabletTVWearable

setMovingPhotoState(movingPhotoState: photoAccessHelper.MovingPhotoBadgeStateType): Promise<void>

应用通过该接口，设置大图浏览下当前动态照片的效果。使用Promise异步回调。

仅在大图浏览下设置生效，不支持设置NOT\_MOVING\_PHOTO。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API**：从API version 23开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| movingPhotoState | [photoAccessHelper.MovingPhotoBadgeStateType](<../../ArkTS API/@ohos.file.photoAccessHelper (相册管理模块)/Enums/arkts-apis-photoaccesshelper-e.md#movingphotobadgestatetype22>) | 是 | 设置当前大图动态照片的状态。 |

**错误码：**

以下错误码的详细介绍请参见[媒体库错误码](../../错误码/媒体库错误码/errorcode-medialibrary.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 23800151 | Scene parameters validate failed, possible causes: 1. An invalid enumeration value was passed. Only MOVING\_PHOTO\_ENABLE and MOVING\_PHOTO\_DISABLE are supported for configuration |
| 23800202 | Invalid call context. Possible causes: 1. The API is called outside the photo browsing scenario. 2. The API is called when isMovingPhotoBadgeShown is already set to true. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

## BaseItemInfo

PhonePC/2in1TabletTVWearable

图片、视频相关信息。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| uri | string | 否 | 是 | 图片、视频的uri。  当[ItemType](ohos-file-photopickercomponent.md#itemtype)为THUMBNAIL时支持，否则为空。  **注意：**  当资源为连拍照片类型时，仅返回该连拍组的封面资源。  **元服务API**：从API version 12开始，该接口支持在元服务中使用。 |
| mimeType | string | 否 | 是 | 图片、视频的mimeType。  当[ItemType](ohos-file-photopickercomponent.md#itemtype)为THUMBNAIL时支持，否则为空。  开发者可以通过mimeType的字符串前缀判断媒体类型：以'image/'开头表示图片，以'video/'开头表示视频。具体判断方式请参考[使用mimeType字段来判断资源类型](<../../../../harmonyos-guides/媒体/Media Library Kit（媒体文件管理服务）/Media Library Kit常见问题/如何正确判断媒体资源类型/medialibrary-asset-judgment-faq.md#使用mimetype字段来判断资源类型>)。  **元服务API**：从API version 12开始，该接口支持在元服务中使用。 |
| width | number | 否 | 是 | 图片、视频的宽（单位：像素）。  当[ItemType](ohos-file-photopickercomponent.md#itemtype)为THUMBNAIL时支持，否则为空。  **元服务API**：从API version 12开始，该接口支持在元服务中使用。 |
| height | number | 否 | 是 | 图片、视频的高（单位：像素）。  当[ItemType](ohos-file-photopickercomponent.md#itemtype)为THUMBNAIL时支持，否则为空。  **元服务API**：从API version 12开始，该接口支持在元服务中使用。 |
| size | number | 否 | 是 | 图片、视频的大小（单位：字节）。  当[ItemType](ohos-file-photopickercomponent.md#itemtype)为THUMBNAIL时支持，否则为空。  **模型约束**：此接口仅可在Stage模型下使用。  **元服务API**：从API version 12开始，该接口支持在元服务中使用。 |
| duration | number | 否 | 是 | 视频的持续时间（单位：毫秒）。  当[ItemType](ohos-file-photopickercomponent.md#itemtype)为THUMBNAIL时支持，否则为空。  **元服务API**：从API version 12开始，该接口支持在元服务中使用。 |
| photoSubType21+ | [photoAccessHelper.PhotoSubtype](<../../ArkTS API/@ohos.file.photoAccessHelper (相册管理模块)/Enums/arkts-apis-photoaccesshelper-e.md#photosubtype12>) | 否 | 是 | 图片类型，包括DEFAULT、MOVING\_PHOTO和BURST。  非特殊类型图片默认为DEFAULT（0）。  **元服务API**：从API version 21开始，该接口支持在元服务中使用。 |
| dynamicRangeType21+ | [photoAccessHelper.DynamicRangeType](<../../ArkTS API/@ohos.file.photoAccessHelper (相册管理模块)/Enums/arkts-apis-photoaccesshelper-e.md#dynamicrangetype12>) | 否 | 是 | 媒体文件动态范围模型，包括HDR和SDR。  对于movingPhoto专指封面图片的动态范围类型。  **元服务API**：从API version 21开始，该接口支持在元服务中使用。 |
| orientation21+ | number | 否 | 是 | 图片/视频方向信息。  1.“TOP-left”，图像未旋转。  2.“TOP-right”，镜像水平翻转。  3.“Bottom-right”，图像旋转180°。  4.“Bottom-left”，镜像垂直翻转。  5.“Left-top”，先镜像水平翻转，再顺时针旋转270°。  6.“Right-top”，顺时针旋转90°。  7.“Right-bottom”，先镜像水平翻转，再顺时针旋转90°。  8.“Left-bottom”，顺时针旋转270°。  携带镜像信息的图片无论旋转与否其宽高属性都与原图保持一致，无镜像信息的图片其宽高属性会更新为旋转后的结果。  **元服务API**：从API version 21开始，该接口支持在元服务中使用。 |
| movingPhotoBadgeState22+ | [photoAccessHelper.MovingPhotoBadgeStateType](<../../ArkTS API/@ohos.file.photoAccessHelper (相册管理模块)/Enums/arkts-apis-photoaccesshelper-e.md#movingphotobadgestatetype22>) | 否 | 是 | 动态照片的状态。  当[ItemType](ohos-file-photopickercomponent.md#itemtype)为THUMBNAIL时支持，否则为空。  **元服务API**：从API version 22开始，该接口支持在元服务中使用。 |
| videoMode22+ | [photoAccessHelper.VideoMode](<../../ArkTS API/@ohos.file.photoAccessHelper (相册管理模块)/Enums/arkts-apis-photoaccesshelper-e.md#videomode22>) | 否 | 是 | 视频文件的log模式。  **元服务API**：从API version 22开始，该接口支持在元服务中使用。 |

## ItemInfo

PhonePC/2in1TabletTVWearable

继承自[BaseItemInfo](ohos-file-photopickercomponent.md#baseiteminfo)，增加私有参数itemType。

图片、视频相关信息。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| itemType | [ItemType](ohos-file-photopickercomponent.md#itemtype) | 否 | 是 | 被点击的item类型。包括缩略图item和相机item。 |

## PhotoBrowserInfo

PhonePC/2in1TabletTVWearable

大图相关信息。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| animatorParams | [AnimatorParams](ohos-file-photopickercomponent.md#animatorparams) | 否 | 是 | 进入、退出大图界面时的动效参数。 |

## AnimatorParams

PhonePC/2in1TabletTVWearable

进退大图动效参数。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| duration | number | 否 | 是 | 动效时长（单位：毫秒）。 |
| curve | [Curve](<../../../ArkUI（方舟UI框架）/ArkTS API/UI界面/@ohos.curves (插值计算)/js-apis-curve.md#curve>) | [ICurve](<../../../ArkUI（方舟UI框架）/ArkTS API/UI界面/@ohos.curves (插值计算)/js-apis-curve.md#icurve9>) | string | 否 | 是 | 动效曲线。 |

## MaxSelected

PhonePC/2in1TabletTVWearable

最大选择数量。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| data | Map<[MaxCountType](ohos-file-photopickercomponent.md#maxcounttype), number> | 否 | 是 | 最大选择数量（包含图片的最大选择数量、视频的最大选择数量以及总的最大选择数量）。 |

## SingleLineConfig20+

PhonePC/2in1TabletTVWearable

单行显示模式配置项。单行模式下，组件不提供打开大图浏览相关功能。组件不支持大图相关回调，PickerController不支持大图相关的接口，接口调用将无效。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| itemDisplayRatio | [ItemDisplayRatio](ohos-file-photopickercomponent.md#itemdisplayratio20) | 否 | 是 | 宫格显示宽高比，支持1:1，原图宽高比两种模式，默认为宽高比1:1显示。 |
| itemBorderRadius | [Length](../../../ArkUI（方舟UI框架）/ArkTS组件/公共定义/基础类型定义/ts-types.md#length) | [BorderRadiuses](../../../ArkUI（方舟UI框架）/ArkTS组件/公共定义/基础类型定义/ts-types.md#borderradiuses9) | [LocalizedBorderRadiuses](../../../ArkUI（方舟UI框架）/ArkTS组件/公共定义/基础类型定义/ts-types.md#localizedborderradiuses12) | 否 | 是 | 宫格圆角属性。 |
| itemGap | [Length](../../../ArkUI（方舟UI框架）/ArkTS组件/公共定义/基础类型定义/ts-types.md#length) | 否 | 是 | 宫格间距。 |

## BadgeConfig21+

PhonePC/2in1TabletTVWearable

特殊角标配置项。

**元服务API**：从API version 21开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| badgeType | [BadgeType](ohos-file-photopickercomponent.md#badgetype21) | 否 | 是 | 特殊角标的类型。 |
| uris | Array<string> | 否 | 是 | 显示角标的资产uri数据。 |

## ClickResult23+

PhonePC/2in1TabletTVWearable

设置指定URI的资产是否被选中。

**模型约束**：此接口仅可在Stage模型下使用。

**元服务API**：从API version 23开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| uri | string | 否 | 否 | 媒体文件资产的URI。 |
| isSelected | boolean | 否 | 否 | 设置指定的媒体文件资产是否被选中，true表示选中，false表示不选中。 |

## PreselectedInfo21+

PhonePC/2in1TabletTVWearable

预选中的文件以及文件对应的PhotoPickerComponent序号。

**元服务API**：从API version 21开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| uri | string | 否 | 否 | 选中媒体文件的uri。 |
| preselectablePickerIndex | number | 否 | 是 | 限制仅在指定序号的PhotoPickerComponent中进行自动选中；默认为-1，即可支持在任意序号的PhotoPickerComponent中自动选中。 |

## UpdatablePickerConfigs22+

PhonePC/2in1TabletTVWearable

支持更新的PhotoPickerComponent属性，为[PickerOptions](ohos-file-photopickercomponent.md#pickeroptions)的子集。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| mimeType | [photoAccessHelper.PhotoViewMIMETypes](<../../ArkTS API/@ohos.file.photoAccessHelper (相册管理模块)/Enums/arkts-apis-photoaccesshelper-e.md#photoviewmimetypes>) | 否 | 是 | 可选择的媒体文件类型。  若无此参数，则默认为图片和视频类型。  **元服务API**：从API version 22开始，该接口支持在元服务中使用。 |
| mimeTypeFilter | [photoAccessHelper.MimeTypeFilter](<../../ArkTS API/@ohos.file.photoAccessHelper (相册管理模块)/Classes (其他)/arkts-apis-photoaccesshelper-class.md#mimetypefilter19>) | 否 | 是 | 文件类型的过滤配置，支持指定多个类型过滤。  - 当配置mimeTypeFilter参数时，mimeType的配置自动失效。  - 当配置该参数时，仅显示配置过滤类型对应的媒体文件，建议提示用户仅支持选择指定类型的图片/视频。  **元服务API**：从API version 22开始，该接口支持在元服务中使用。 |
| maxSelectNumber | number | 否 | 是 | 选择媒体文件数量的最大值（单位：个）。  最大可设置为500，若不设置则默认为50。  **元服务API**：从API version 22开始，该接口支持在元服务中使用。 |
| maxPhotoSelectNumber | number | 否 | 是 | 图片最大的选择数量（单位：个）。  最大值为500，受到最大选择总数的限制。默认为500。  **元服务API**：从API version 22开始，该接口支持在元服务中使用。 |
| maxVideoSelectNumber | number | 否 | 是 | 视频最大的选择数量（单位：个）。  最大值为500，受到系统中所有媒体文件最大选择总数的限制。默认为500。  **元服务API**：从API version 22开始，该接口支持在元服务中使用。 |
| selectMode | [SelectMode](ohos-file-photopickercomponent.md#selectmode) | 否 | 是 | Picker选择模式。  包括多选和单选，默认为多选。  **元服务API**：从API version 22开始，该接口支持在元服务中使用。 |
| singleSelectionMode | [photoAccessHelper.SingleSelectionMode](<../../ArkTS API/@ohos.file.photoAccessHelper (相册管理模块)/Enums/arkts-apis-photoaccesshelper-e.md#singleselectionmode18>) | 否 | 是 | 单选模式类型。默认为大图预览模式（SingleSelectionMode.BROWSER\_MODE）。  **元服务API**：从API version 22开始，该接口支持在元服务中使用。 |
| isRepeatSelectSupported | boolean | 否 | 是 | 是否支持单张图片重复选择。  true表示支持，false表示不支持。默认为false。  **元服务API**：从API version 22开始，该接口支持在元服务中使用。 |
| preselectedUris | Array<string> | 否 | 是 | 已选择图片的uri数据。  **元服务API**：从API version 22开始，该接口支持在元服务中使用。 |
| checkBoxColor | string | 否 | 是 | 勾选框的背景色。  格式为8位十六进制颜色代码。  **元服务API**：从API version 22开始，该接口支持在元服务中使用。 |
| backgroundColor | string | 否 | 是 | Picker宫格页面背景色。  格式为8位十六进制颜色代码。  **元服务API**：从API version 22开始，该接口支持在元服务中使用。 |
| checkboxTextColor | string | 否 | 是 | 勾选框内文本颜色。  格式为8位十六进制颜色代码。  **元服务API**：从API version 22开始，该接口支持在元服务中使用。 |
| photoBrowserBackgroundColorMode | [PickerColorMode](ohos-file-photopickercomponent.md#pickercolormode) | 否 | 是 | 大图背景颜色。  包括跟随系统、浅色模式以及深色模式，默认为跟随系统。  **元服务API**：从API version 22开始，该接口支持在元服务中使用。 |
| uiComponentColorMode | [PickerColorMode](ohos-file-photopickercomponent.md#pickercolormode) | 否 | 是 | Picker UI组件的颜色模式。  Picker宫格界面除背景色之外其他组件的深浅色风格，包括搜索框、相机入口、安全使用图库提示组件、推荐气泡等组件，一般与backgroundColor配合使用。默认为PickerColorMode.AUTO，跟随系统深浅色切换。  该属性设置为PickerColorMode.LIGHT时，一般不与深颜色的backgroundColor搭配；设置为PickerColorMode.DARK时，不与浅颜色的backgroundColor搭配，避免出现组件背景或文字无法看清楚的问题。  **元服务API**：从API version 22开始，该接口支持在元服务中使用。 |
| isSlidingSupported23+ | boolean | 否 | 是 | 是否屏蔽PhotoPickerComponent的滚动。true表示不屏蔽滚动事件，响应用户滚动。false表示屏蔽滚动事件，不响应用户滚动。  默认为true。  **模型约束**：此接口仅可在Stage模型下使用。  **元服务API**：从API version 23开始，该接口支持在元服务中使用。 |
| edgeEffect23+ | [EdgeEffect](../../../ArkUI（方舟UI框架）/ArkTS组件/公共定义/枚举说明/ts-appendix-enums.md#edgeeffect) | 否 | 是 | Picker宫格页滑动到边缘处的滑动效果。  默认为[EdgeEffect.Spring](../../../ArkUI（方舟UI框架）/ArkTS组件/公共定义/枚举说明/ts-appendix-enums.md#edgeeffect)。  **模型约束：** 此接口仅可在Stage模型下使用。  **元服务API**：从API version 23开始，该接口支持在元服务中使用。 |
| appAlbumFilters23+ | Array<string> | 否 | 是 | 仅显示与指定bundle name对应的相册内容。  **模型约束：** 此接口仅可在Stage模型下使用。  **元服务API**：从API version 23开始，该接口支持在元服务中使用。 |
| autoPlayScenes23+ | Array<[photoAccessHelper.AutoPlayScene](<../../ArkTS API/@ohos.file.photoAccessHelper (相册管理模块)/Classes (其他)/arkts-apis-photoaccesshelper-class.md#autoplayscene23>)> | 否 | 是 | 设置动态照片播放模式。长度限制为2个，超出取前2个，多余的会自动忽略。  **模型约束：** 此接口仅可在Stage模型下使用。  **元服务API：** 从API version 23开始，该接口支持在元服务中使用。 |
| backgroundOpacity24+ | number | 否 | 是 | 支持配置picker背景透明度。取值范围为[0, 1]，0表示完全透明，1表示完全不透明。  **模型约束：** 此接口仅可在Stage模型下使用。  **元服务API**：从API version 24开始，该接口支持在元服务中使用。 |

## PickerError23+

PhonePC/2in1TabletTVWearable

使用PhotoPickerComponent组件发生错误时返回的错误的接口名称、错误码和错误描述。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API**：从API version 23开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| functionName | string | 否 | 否 | 产生错误的接口名称。 |
| errorCode | number | 否 | 否 | 错误码。 |
| message | string | 否 | 否 | 接口返回的具体错误描述信息。 |

## DataType

PhonePC/2in1TabletTVWearable

枚举，PickerController向picker组件发送数据的数据类型。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| SET\_SELECTED\_URIS | 1 | 发送已选择的数据列表，通知picker组件勾选状态刷新，需要传入string数组类型。  例如：应用在自己的页面中删除某张图片后，需要把剩下的已选择的数据列表通过setData接口通知到picker组件，从而触发picker组件勾选框状态刷新正确。  **元服务API**：从API version 12开始，该接口支持在元服务中使用。 |
| SET\_ALBUM\_URI | 2 | 发送已选择相册，通知picker组件刷新相册，需要传入string类型。  例如：应用在自己的页面中选择相册后，需要把已选择的相册uri通过setData接口通知到picker组件，从而触发picker组件刷新相册数据。  **元服务API**：从API version 12开始，该接口支持在元服务中使用。 |
| SET\_SELECTED\_INFO21+ | 3 | 发送已选择的文件uri以及选中的picker序号。当picker序号与参数中的picker序号匹配时，已选择文件支持在当前picker里自动选中。  **元服务API**：从API version 21开始，该接口支持在元服务中使用。 |
| SET\_BADGE\_CONFIGS21+ | 4 | 发送需要显示角标的配置，类型为[badgeConfig](ohos-file-photopickercomponent.md#badgeconfig21)，包含角标的类型和对应文件uri的数据列表。配置后，对应文件会显示配置类型的角标。  **元服务API**：从API version 21开始，该接口支持在元服务中使用。 |
| SET\_ITEM\_CLICK\_RESULT23+ | 5 | 发送点击后的结果，类型为[ClickResult](ohos-file-photopickercomponent.md#clickresult23)。  **模型约束：** 此接口仅可在Stage模型下使用。  **元服务API**：从API version 23开始，该接口支持在元服务中使用。 |

## ItemType

PhonePC/2in1TabletTVWearable

被点击item的类型。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| THUMBNAIL | 0 | 图片、视频item（缩略图item）。 |
| CAMERA | 1 | 相机item。 |

## ClickType

PhonePC/2in1TabletTVWearable

点击操作的类型。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| SELECTED | 0 | 选择操作（勾选图片或者点击相机item）。 |
| DESELECTED | 1 | 取消选择操作（取消勾选图片）。 |

## PickerOrientation

PhonePC/2in1TabletTVWearable

Picker宫格页面滑动预览的方向。

从API20开始，该能力支持配置；在API12-19，该能力设置不生效，默认为竖直方向。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| VERTICAL | 0 | 竖直方向。 |
| HORIZONTAL | 1 | 水平方向。 |

## SelectMode

PhonePC/2in1TabletTVWearable

选择模式。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| SINGLE\_SELECT | 0 | 单选模式。 |
| MULTI\_SELECT | 1 | 多选模式。 |

## PickerColorMode

PhonePC/2in1TabletTVWearable

Picker的颜色模式。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core。

| 名称 | 值 | 说明 |
| --- | --- | --- |
| AUTO | 0 | 跟随系统。 |
| LIGHT | 1 | 浅色模式。 |
| DARK | 2 | 深色模式。 |

## ReminderMode

PhonePC/2in1TabletTVWearable

最大选择数量提示方式。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| NONE | 0 | 不提示。 |
| TOAST | 1 | 弹toast提示。 |
| MASK | 2 | 蒙灰提示。 |

## MaxCountType

PhonePC/2in1TabletTVWearable

最大选择数量的类型。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| TOTAL\_MAX\_COUNT | 0 | 总的最大选择数量。 |
| PHOTO\_MAX\_COUNT | 1 | 图片的最大选择数量（不能大于总的最大选择数量）。 |
| VIDEO\_MAX\_COUNT | 2 | 视频的最大选择数量（不能大于总的最大选择数量）。 |

## PhotoBrowserRange

PhonePC/2in1TabletTVWearable

打开大图浏览模式后，左右滑动切换浏览图片的范围。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| ALL | 0 | 全部图片，视频。 |
| SELECTED\_ONLY | 1 | 仅用户已选择的图片，视频。 |

## PhotoBrowserUIElement13+

PhonePC/2in1TabletTVWearable

大图页大图预览组件外其他UI元素。

**元服务API**：从API version 13开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| CHECKBOX | 0 | 大图页勾选框。 |
| BACK\_BUTTON | 1 | 大图页返回按钮。 |

## SaveMode15+

PhonePC/2in1TabletTVWearable

图片/视频保存模式。

**元服务API**：从API version 15开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| SAVE\_AS | 0 | 另存为新的图片/视频。 |
| OVERWRITE | 1 | 覆盖原有图片/视频，覆盖后支持在图库中将保存内容回退，还原成原始图片/视频。 |

## BadgeType21+

PhonePC/2in1TabletTVWearable

表示特殊角标类型的枚举。

**元服务API**：从API version 21开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| BADGE\_UPLOADED | 0 | 已上传。 |

## VideoPlayerState14+

PhonePC/2in1TabletTVWearable

视频播放状态。

**元服务API**：从API version 14开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| PLAYING | 0 | 视频播放中。 |
| PAUSED | 1 | 视频播放暂停。 |
| STOPPED | 2 | 视频播放停止。 |
| SEEK\_START | 3 | 开始拖拽进度条。 |
| SEEK\_FINISH | 4 | 结束拖拽进度条。 |

## ItemDisplayRatio20+

PhonePC/2in1TabletTVWearable

单行布局宫格显示宽高比模式，包括1:1和原图宽高比两种模式。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| SQUARE\_RATIO | 0 | 1:1比例显示。 |
| ORIGINAL\_SIZE\_RATIO | 1 | 原图宽高比显示。 |

## 示例一（PhotoPickerComponent组件的使用）

PhonePC/2in1TabletTVWearable

```
1. // xxx.ets
2. // 从API version 23开始，推荐使用统一导入方式，从'@kit.MediaLibraryKit'导入所需模块。
3. // 在API version 23之前的版本中，需要使用分别导入方式。
4. // import { PhotoPickerComponent, PickerController, PickerOptions, DataType, BaseItemInfo, ItemInfo, PhotoBrowserInfo, ItemType, ClickType, MaxCountType, PhotoBrowserRange, PhotoBrowserUIElement, ItemsDeletedCallback, ExceedMaxSelectedCallback, CurrentAlbumDeletedCallback, videoPlayStateChangedCallback, VideoPlayerState } from '@ohos.file.PhotoPickerComponent';
5. // import { photoAccessHelper } from '@ohos.file.photoAccessHelper';
6. import {
7. PhotoPickerComponent,
8. PickerController,
9. PickerOptions,
10. DataType,
11. BaseItemInfo,
12. ItemInfo,
13. PhotoBrowserInfo,
14. ItemType,
15. ClickType,
16. MaxCountType,
17. PhotoBrowserRange,
18. PhotoBrowserUIElement,
19. ItemsDeletedCallback,
20. ExceedMaxSelectedCallback,
21. CurrentAlbumDeletedCallback,
22. videoPlayStateChangedCallback,
23. VideoPlayerState,
24. photoAccessHelper
25. } from '@kit.MediaLibraryKit';
26. import { dataSharePredicates } from '@kit.ArkData';
27. import { common } from '@kit.AbilityKit';

29. @Entry
30. @Component
31. struct PickerDemo {
32. pickerOptions: PickerOptions = new PickerOptions();
33. @State pickerController: PickerController = new PickerController();
34. @State selectUris: string[] = [];
35. @State currentUri: string = '';
36. @State isBrowserShow: boolean = false;
37. private selectedItemsDeletedCallback: ItemsDeletedCallback =
38. (baseItemInfos: Array<BaseItemInfo>) => this.onSelectedItemsDeleted(baseItemInfos);
39. private exceedMaxSelectedCallback: ExceedMaxSelectedCallback =
40. (exceedMaxCountType: MaxCountType) => this.onExceedMaxSelected(exceedMaxCountType);
41. private currentAlbumDeletedCallback: CurrentAlbumDeletedCallback = () => this.onCurrentAlbumDeleted();
42. private videoPlayStateChangedCallback: videoPlayStateChangedCallback =
43. (state: VideoPlayerState) => this.videoPlayStateChanged(state);
44. private thumbnail: PixelMap[] = [];
45. private assets: photoAccessHelper.PhotoAsset[] = [];

47. aboutToAppear() {
48. this.pickerOptions.MIMEType = photoAccessHelper.PhotoViewMIMETypes.IMAGE_VIDEO_TYPE;
49. this.pickerOptions.maxSelectNumber = 5;
50. this.pickerOptions.isSearchSupported = false;
51. this.pickerOptions.isPhotoTakingSupported = false;
52. this.pickerOptions.photoBrowserCheckboxPosition = [0.5, 0.5];
53. // 其他属性.....
54. }

56. private onSelect(uri: string): void {
57. // 添加。
58. if (uri) {
59. this.selectUris.push(uri);
60. }
61. }

63. private onDeselect(uri: string): void {
64. // 移除。
65. if (uri) {
66. this.selectUris = this.selectUris.filter((item: string) => {
67. return item != uri;
68. })
69. }
70. }

72. private onItemClicked(itemInfo: ItemInfo, clickType: ClickType): boolean {
73. if (!itemInfo) {
74. return false;
75. }
76. let type: ItemType | undefined = itemInfo.itemType;
77. let uri: string | undefined = itemInfo.uri;
78. if (type === ItemType.CAMERA) {
79. // 点击相机item。
80. return true; // 返回true则拉起系统相机，若应用需要自行处理则返回false。
81. } else {
82. if (clickType === ClickType.SELECTED) {
83. // 应用做自己的业务处理（注：非长耗时操作，例如openSync大文件）。
84. if (uri) {
85. this.selectUris.push(uri);
86. this.pickerOptions.preselectedUris = [...this.selectUris];
87. }
88. return true; // 返回true则勾选，否则不响应勾选。
89. } else {
90. if (uri) {
91. this.selectUris = this.selectUris.filter((item: string) => {
92. return item != uri;
93. });
94. this.pickerOptions.preselectedUris = [...this.selectUris];
95. }
96. }
97. return true;
98. }
99. }

101. private onEnterPhotoBrowser(photoBrowserInfo: PhotoBrowserInfo): boolean {
102. // 进入大图的回调。
103. this.isBrowserShow = true;
104. return true;
105. }

107. private onExitPhotoBrowser(photoBrowserInfo: PhotoBrowserInfo): boolean {
108. // 退出大图的回调。
109. this.isBrowserShow = false;
110. return true;
111. }

113. private onPickerControllerReady(): void {
114. // 接收到该回调后，便可通过pickerController相关接口向picker发送数据，在此之前不生效。
115. let elements: number[] = [PhotoBrowserUIElement.BACK_BUTTON];
116. this.pickerController.setPhotoBrowserUIElementVisibility(elements, false); // 设置大图页不显示返回按钮。
117. }

119. private onPhotoBrowserChanged(browserItemInfo: BaseItemInfo): boolean {
120. // 大图左右滑动的回调。
121. this.currentUri = browserItemInfo.uri ?? '';
122. return true;
123. }

125. private onSelectedItemsDeleted(baseItemInfos: Array<BaseItemInfo>): void {
126. // 已勾选图片被删除时的回调。
127. }

129. private onExceedMaxSelected(exceedMaxCountType: MaxCountType): void {
130. // 超过最大选择数量再次点击时的回调。
131. }

133. private onCurrentAlbumDeleted(): void {
134. // 当前相册被删除时的回调。
135. }

137. private videoPlayStateChanged(state: VideoPlayerState): void {
138. // 当视频播放状态变化时回调。
139. }
140. build() {
141. Flex({
142. direction: FlexDirection.Column,
143. justifyContent: FlexAlign.Center,
144. alignItems: ItemAlign.Center
145. }) {
146. Column() {
147. if (this.isBrowserShow) {
148. // 这里模拟应用自己的大图返回按钮。
149. Row() {
150. Button("退出大图").width('33%').height('8%').onClick(() => {
151. this.pickerController.exitPhotoBrowser();
152. })
153. }.margin({ bottom: 20 })
154. }

156. PhotoPickerComponent({
157. pickerOptions: this.pickerOptions,
158. onSelect: (uri: string): void => this.onSelect(uri),
159. onDeselect: (uri: string): void => this.onDeselect(uri),
160. onItemClicked: (itemInfo: ItemInfo, clickType: ClickType): boolean => this.onItemClicked(itemInfo,
161. clickType), // 该接口可替代上面两个接口。
162. onEnterPhotoBrowser: (photoBrowserInfo: PhotoBrowserInfo): boolean => this.onEnterPhotoBrowser(photoBrowserInfo),
163. onExitPhotoBrowser: (photoBrowserInfo: PhotoBrowserInfo): boolean => this.onExitPhotoBrowser(photoBrowserInfo),
164. onPickerControllerReady: (): void => this.onPickerControllerReady(),
165. onPhotoBrowserChanged: (browserItemInfo: BaseItemInfo): boolean => this.onPhotoBrowserChanged(browserItemInfo),
166. onSelectedItemsDeleted: this.selectedItemsDeletedCallback,
167. onExceedMaxSelected: this.exceedMaxSelectedCallback,
168. onCurrentAlbumDeleted: this.currentAlbumDeletedCallback,
169. onVideoPlayStateChanged: this.videoPlayStateChangedCallback,
170. pickerController: this.pickerController,
171. }).height('60%').width('100%')

173. // 这里模拟应用侧底部的选择栏。
174. if (this.isBrowserShow) {
175. Row() {
176. ForEach(this.assets, async (asset: photoAccessHelper.PhotoAsset, index) => {
177. if (asset.uri === this.currentUri) {
178. Image(this.thumbnail[index])
179. .height('10%')
180. .width('10%')
181. .onClick(() => {
182. })
183. .borderWidth(1)
184. .borderColor('red')
185. } else {
186. Image(this.thumbnail[index]).height('10%').width('10%').onClick(() => {
187. this.pickerController.setData(DataType.SET_SELECTED_URIS, this.selectUris);
188. this.pickerController.setPhotoBrowserItem(asset.uri, PhotoBrowserRange.ALL);
189. })
190. }
191. }, (uri: string) => JSON.stringify(uri))
192. }
193. } else {
194. Button('预览').width('33%').height('5%').onClick(async () => {
195. if (this.selectUris.length > 0) {
196. this.thumbnail = [];
197. this.assets = [];
198. for (let selectUri of this.selectUris) {
199. let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
200. predicates.equalTo(photoAccessHelper.PhotoKeys.URI, selectUri);
201. let fetchOptions: photoAccessHelper.FetchOptions = {
202. fetchColumns: [],
203. predicates: predicates
204. };
205. let context: Context = this.getUIContext().getHostContext() as common.UIAbilityContext;
206. let photoHelper = photoAccessHelper.getPhotoAccessHelper(context);
207. let fetchResult: photoAccessHelper.FetchResult<photoAccessHelper.PhotoAsset> =
208. await photoHelper.getAssets(fetchOptions);
209. let asset = await fetchResult.getFirstObject()
210. this.assets.push(asset);
211. this.thumbnail.push(await asset.getThumbnail())
212. }
213. this.pickerController.setPhotoBrowserItem(this.selectUris[0], PhotoBrowserRange.SELECTED_ONLY);
214. }
215. })
216. }
217. }
218. }
219. }
220. }
```

## 示例二（使用PhotoPickerComponent实现抽屉组件效果）

PhonePC/2in1TabletTVWearable

从API version 23开始，可以通过[PickerOptions](ohos-file-photopickercomponent.md#pickeroptions)的isSlidingSupported、[PhotoPickerComponent](ohos-file-photopickercomponent.md#photopickercomponent)的onScrollStopAtStart和onScrollStopAtEnd回调来实现抽屉效果。

```
1. // xxx.ets
2. import { display } from '@kit.ArkUI';
3. import { PhotoPickerComponent, PickerController, PickerOptions } from '@kit.MediaLibraryKit';
4. const enum DrawerState {
5. // 展开状态。
6. Expanding,
7. // 收缩状态。
8. Collapsing,
9. // 滑动状态。
10. Sliding
11. }

13. @Entry
14. @Component
15. struct Drawer {
16. @State pickerController: PickerController = new PickerController();
17. private pickerOptions: PickerOptions = new PickerOptions();
18. // 屏幕高度，单位为vp。
19. @State screenHeight: number = 0;
20. // 抽屉高度，单位为vp。
21. @State drawerHeight: number = 0;
22. // 抽屉的偏移量，单位为vp。
23. @State offsetY: number = 0;
24. // 抽屉是否展开。
25. @State isExpanded: boolean = false;
26. // 拖拽起始位置，单位为vp。
27. private startY: number = 0;
28. // 当前拖拽的偏移量，单位为vp。
29. private currentOffset: number = 0;
30. // 自定义抽屉高度在整个屏幕的占比。
31. private drawerRatio: number = 0.8;
32. // 自定义初始化时隐藏抽屉的占比。
33. private hideRatio: number = 0.8;
34. // 初始化为收缩状态。
35. private drawerState: DrawerState = DrawerState.Collapsing;
36. // 手势响应阈值，判断手势是否为向下。
37. private pullingDownThreshold: number = -5;

39. aboutToAppear(): void {
40. // 获取屏幕高度。
41. let displayInfo = display.getDefaultDisplaySync();
42. this.screenHeight = displayInfo.height / displayInfo.densityPixels;
43. // 获取抽屉高度，示例为屏幕高度的0.8倍，可自定义修改。
44. this.drawerHeight = this.screenHeight * this.drawerRatio;
45. // 初始时抽屉在底部（隐藏高度），示例为隐藏抽屉的0.8倍。
46. this.offsetY = this.drawerHeight * this.hideRatio;
47. // 初始化时Picker不支持滑动。
48. this.pickerOptions.isSlidingSupported = false;
49. // 无边缘回弹。
50. this.pickerOptions.edgeEffect = EdgeEffect.None;
51. // 不展示搜索框。
52. this.pickerOptions.isSearchSupported = false;
53. }

55. private scrollStopAtStart() {
56. // 状态变更为展开状态，同时设置宫格不能滑动。
57. this.drawerState = DrawerState.Expanding;
58. this.pickerController.updatePickerOptions({
59. isSlidingSupported: false
60. })
61. }

63. private toggleDrawer() {
64. if (this.isExpanded) {
65. this.hideDrawer();
66. } else {
67. this.showDrawer();
68. }
69. }

71. private hideDrawer() {
72. this.getUIContext()?.animateTo({
73. duration: 300,
74. curve: Curve.EaseOut,
75. onFinish: () => {
76. this.isExpanded = false;
77. }
78. }, () => {
79. this.drawerState = DrawerState.Collapsing;
80. this.offsetY = this.drawerHeight * 0.8;
81. })
82. }

84. private showDrawer() {
85. this.getUIContext()?.animateTo({
86. duration: 300,
87. curve: Curve.EaseOut,
88. onFinish: () => {
89. this.isExpanded = true;
90. }
91. }, () => {
92. this.drawerState = DrawerState.Expanding;
93. this.offsetY = 0;
94. })
95. }

97. build() {
98. RelativeContainer() {
99. // 主内容区域。
100. Column() {
101. Text('主页面内容')
102. .fontSize(24)
103. .fontWeight(FontWeight.Bold)
104. .margin({ bottom: 20 })

106. Text('这是一个使用RelativeContainer实现的底部抽屉效果')
107. .fontSize(16)
108. .fontColor('#666')
109. .margin({ bottom: 30 })
110. .textAlign(TextAlign.Center)
111. .width('80%')

113. Button(this.isExpanded ? '收起抽屉' : '展开抽屉')
114. .onClick(() => {
115. this.toggleDrawer();
116. })
117. }
118. .width('100%')
119. .padding(20)
120. .alignItems(HorizontalAlign.Center)
121. .backgroundColor('#f5f5f5')
122. .borderRadius(10)
123. .alignRules({
124. top: { anchor: '__container__', align: VerticalAlign.Top },
125. left: { anchor: '__container__', align: HorizontalAlign.Start },
126. right: { anchor: '__container__', align: HorizontalAlign.End },
127. })
128. .height('100%')

130. if (this.isExpanded) {
131. Column()
132. .width('100%')
133. .height('100%')
134. .backgroundColor('#80000000')
135. .alignRules({
136. top: { anchor: '__container__', align: VerticalAlign.Top },
137. left: { anchor: '__container__', align: HorizontalAlign.Start },
138. right: { anchor: '__container__', align: HorizontalAlign.End },
139. bottom: { anchor: '__container__', align: VerticalAlign.Bottom },
140. })
141. .onClick(() => {
142. this.hideDrawer();
143. })
144. }

146. Column() {
147. Row()
148. .width(50)
149. .height(5)
150. .backgroundColor('#CCC')
151. .borderRadius(3)
152. .margin({ top: 12, bottom: 8 })

154. Text('抽屉菜单')
155. .fontSize(18)
156. .fontWeight(FontWeight.Medium)
157. .margin({ bottom: 10 })

159. Divider()
160. .width('90%')
161. .margin({ bottom: 10 })

163. PhotoPickerComponent({
164. pickerOptions: this.pickerOptions,
165. pickerController: this.pickerController,
166. onScrollStopAtStart: this.scrollStopAtStart
167. })
168. .layoutWeight(1)
169. .width('100%')
170. }
171. .width('100%')
172. .height(this.drawerHeight)
173. .backgroundColor(Color.White)
174. .borderRadius({ topLeft: 20, topRight: 20 })
175. .shadow({ radius: 10, color: '#33000000' })
176. .alignRules({
177. left: { anchor: '__container__', align: HorizontalAlign.Start },
178. right: { anchor: '__container__', align: HorizontalAlign.End },
179. bottom: { anchor: '__container__', align: VerticalAlign.Bottom },
180. })
181. .translate({ y: this.offsetY })
182. .gesture(
183. PanGesture({ direction: PanDirection.Vertical })
184. // 记录抽屉开始拖拽的位置。
185. .onActionStart((event: GestureEvent) => {
186. this.startY = event.fingerList[0].globalY || 0;
187. this.currentOffset = this.offsetY;
188. })
189. .onActionUpdate((event: GestureEvent) => {
190. // 如果是Picker滑动状态，不改变抽屉的高度，直接返回。
191. if (this.drawerState === DrawerState.Sliding) {
192. return;
193. }
194. // 如果抽屉的状态是展开或者收缩则需要通过手势来进一步改变抽屉状态。
195. // 计算移动距离。
196. const deltaY = event.fingerList[0].globalY - this.startY || 0;
197. // 当抽屉处于展开状态且用户向下滑动时，开启宫格滑动功能并将抽屉状态切换为滑动状态。
198. if (this.drawerState === DrawerState.Expanding && deltaY < this.pullingDownThreshold) {
199. this.pickerController.updatePickerOptions({
200. isSlidingSupported: true
201. })
202. this.drawerState = DrawerState.Sliding
203. }
204. let newOffset = this.currentOffset + deltaY;
205. if (newOffset < 0) {
206. newOffset = 0;
207. }
208. this.offsetY = newOffset;
209. })
210. .onActionEnd(()=>{
211. // 手势结束，根据位置自动展开或收起。
212. if (this.offsetY > this.drawerHeight / 2) {
213. // 滑动超过抽屉高度一半，抽屉状态置为收缩状态。
214. this.hideDrawer();
215. } else {
216. // 滑动不到抽屉高度一半，抽屉状态置为展开状态。
217. this.showDrawer();
218. }
219. })
220. )
221. }
222. .width('100%')
223. .height('100%')
224. .backgroundColor('#E0E0E0')
225. }
226. }
```
