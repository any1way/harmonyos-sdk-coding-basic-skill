---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-ui-widget-creation
title: 创建ArkTS卡片
breadcrumb: 指南 > 应用框架 > Form Kit（卡片开发服务） > ArkTS卡片开发（推荐） > 创建ArkTS卡片
category: harmonyos-guides
scraped_at: 2026-06-11T14:37:30+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:985c44b90ddaa402f0f4e5d0ec94c2f97ca4a454632e81b669f4056abd1615ba
---
ArkTS卡片有两种创建卡片包的方式。开发者在开发过程中任选其一即可。

方式一：卡片和应用共包方式，创建步骤请参考[共包方式创建卡片](arkts-ui-widget-creation.md#方式一共包方式创建卡片)，此时卡片UI和应用代码在一个module内，最终编译产物也在同一个HAP包内。

方式二：独立卡片包方式，创建步骤请参考[独立包方式创建卡片](arkts-ui-widget-creation.md#方式二独立包方式创建卡片)，此时卡片UI和应用代码在不同module内，最终编译产物分为卡片包和应用包。从API version 20开始支持。

ArkTS卡片创建完成，在开发卡片过程中，支持对卡片进行[实时预览](../../../../开发环境搭建/工程创建/模块管理/创建服务卡片/ide-service-widget.md#section18171652015)。

## 方式一：共包方式创建卡片

### 创建步骤

**1. 新建工程**

在DevEco Studio中，选择创建Application或Atomic Service工程，这两种都支持创建卡片。工程创建指导具体请参考[创建一个新的工程](../../../../开发环境搭建/工程创建/创建一个新的工程/ide-create-new-project.md)。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/06/v3/4vvaGsMrTyeHxZfsdiD1RQ/zh-cn_image_0000002592378632.png?HW-CC-KV=V1&HW-CC-Date=20260611T063730Z&HW-CC-Expire=86400&HW-CC-Sign=6D742C7C4B5E42FEB3BE7B07647BA617DB9EF29E1328125328536F4216CB2B85)

说明

基于不同版本的DevEco Studio，请以实际界面为准。

**2. 新建卡片**

在已有的应用工程中，右键新建ArkTS卡片，具体操作如下。

* 选中entry目录单击右键选择【New】->【Service Widget】->【Dynamic Widget】。在API 10及以上 Stage模型的工程中，开发者可通过Service Widget菜单直接选择创建动态卡片（Dynamic Widget）或静态卡片（Static Widget）。创建卡片后，也可在卡片的[form\_config.json配置文件](../配置ArkTS卡片的配置文件/arkts-ui-widget-configuration.md#配置文件字段说明)中，通过isDynamic参数修改卡片类型：isDynamic置空或赋值为“true”，则该卡片为[动态卡片](../ArkTS卡片概述/arkts-form-overview.md#动态卡片)；isDynamic赋值为"false"，则该卡片为[静态卡片](../ArkTS卡片概述/arkts-form-overview.md#静态卡片)。静态卡片和动态卡片切换之后用户交互实现也需要修改，具体参考ArkTS卡片概述中的[动态卡片](../ArkTS卡片概述/arkts-form-overview.md#动态卡片)和[静态卡片](../ArkTS卡片概述/arkts-form-overview.md#静态卡片)。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/75/v3/Vc8j8pDwSXy4IepdykmeFw/zh-cn_image_0000002622858139.png?HW-CC-KV=V1&HW-CC-Date=20260611T063730Z&HW-CC-Expire=86400&HW-CC-Sign=E1F422A8C2C6742421C11C48956B48684604B658CA1A089359700D725A04F1D9)
* 选择模板后，点击【Next】。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/13/v3/PzAJvfEBSMKsh5Z6MuVfQA/zh-cn_image_0000002622698261.png?HW-CC-KV=V1&HW-CC-Date=20260611T063730Z&HW-CC-Expire=86400&HW-CC-Sign=974B47E4F880910F157B667BDB5943CD489AE5ED11BE68217C7BD6E1A25463D3)
* 在选择卡片的开发语言类型（Language）时，选择ArkTS选项。选择卡片支持的外观规格（Support dimension）时，选择期望的卡片尺寸，然后选择默认的外观规格（Default dimension），最后点击“Finish”，即可完成ArkTS卡片创建。详细的卡片外观规格可参考[form\_config.json](../配置ArkTS卡片的配置文件/arkts-ui-widget-configuration.md#配置文件字段说明)配置文件，后续也可以在form\_config.json配置文件中修改卡片规格。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/62/v3/Dx5P5JFiRz2BBuuqHVHNqQ/zh-cn_image_0000002592218700.png?HW-CC-KV=V1&HW-CC-Date=20260611T063730Z&HW-CC-Expire=86400&HW-CC-Sign=D86DDBF454222DF32569E99D4B17E33CF1BB52984AE307A44DF64005F7EB0C9E)

  建议根据实际使用场景命名卡片名称，ArkTS卡片创建完成后，工程中会新增如下卡片相关文件：卡片生命周期管理文件（EntryFormAbility.ets）、卡片页面文件（WidgetCard.ets）和卡片配置文件（form\_config.json）。填写卡片配置之后点击【Finish】。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a6/v3/o9oNFzMNS4-__dGpHYDFsg/zh-cn_image_0000002592378634.png?HW-CC-KV=V1&HW-CC-Date=20260611T063730Z&HW-CC-Expire=86400&HW-CC-Sign=8D00CDD8B43C12A6ED4DB5A6E552F075E270CF1E3F96C64653B54FC564EB2F68)

### 工程结构介绍

**图1** ArkTS卡片工程目录、相关模块

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4/v3/5AE9GmPwQOm5PYA0_2zdUQ/zh-cn_image_0000002622858141.png?HW-CC-KV=V1&HW-CC-Date=20260611T063730Z&HW-CC-Expire=86400&HW-CC-Sign=D7AB91EF5584DF60D6E12F8787DADE8BD236E05A373CDCA309D472EF72668D58)

* [FormExtensionAbility](<../../../../../harmonyos-references/Form Kit（卡片开发服务）/ArkTS API/@ohos.app.form.FormExtensionAbility (FormExtensionAbility)/js-apis-app-form-formextensionability.md>)：卡片扩展模块，提供卡片创建、销毁、刷新等生命周期回调。
* [FormExtensionContext](<../../../../../harmonyos-references/Form Kit（卡片开发服务）/ArkTS API/application/FormExtensionContext/js-apis-inner-application-formextensioncontext.md>)：FormExtensionAbility的上下文环境，提供FormExtensionAbility具有的接口和能力。
* [formProvider](<../../../../../harmonyos-references/Form Kit（卡片开发服务）/ArkTS API/@ohos.app.form.formProvider (formProvider)/js-apis-app-form-formprovider.md>)：提供了获取卡片信息、更新卡片、设置卡片更新时间等能力。
* [formInfo](<../../../../../harmonyos-references/Form Kit（卡片开发服务）/ArkTS API/@ohos.app.form.formInfo (formInfo)/js-apis-app-form-forminfo.md>)：提供了卡片信息和状态等相关类型和枚举。
* [formBindingData](<../../../../../harmonyos-references/Form Kit（卡片开发服务）/ArkTS API/@ohos.app.form.formBindingData (卡片数据绑定类)/js-apis-app-form-formbindingdata.md>)：提供卡片数据绑定的能力，包括FormBindingData对象的创建、相关信息的描述。
* [页面布局（WidgetCard.ets）](../ArkTS卡片提供方开发指导/ArkTS卡片UI界面开发/ArkTS卡片界面开发概述/arkts-ui-widget-page-overview.md)：基于ArkUI提供卡片UI开发能力。

  + [ArkTS卡片通用能力](../ArkTS卡片提供方开发指导/ArkTS卡片UI界面开发/ArkTS卡片界面开发概述/arkts-ui-widget-page-overview.md#arkts卡片支持的页面能力)：提供了能在ArkTS卡片中使用的组件、属性和API。
  + [ArkTS卡片特有能力](../ArkTS卡片提供方开发指导/ArkTS卡片页面交互/ArkTS卡片页面交互概述/arkts-ui-widget-event-overview.md)：postCardAction用于卡片内部和提供方应用间的交互，仅在卡片中可以调用。
* [卡片配置](../配置ArkTS卡片的配置文件/arkts-ui-widget-configuration.md)：包含FormExtensionAbility的配置和卡片的配置。

  + 在[module.json5配置文件](../../../../基础入门/开发基础知识/应用配置文件（Stage模型）/module.json5配置文件/module-configuration-file.md)中的extensionAbilities标签下，配置FormExtensionAbility相关信息。
  + 在resources/base/profile/目录下的[form\_config.json](../配置ArkTS卡片的配置文件/arkts-ui-widget-configuration.md#配置文件字段说明)配置文件中，配置卡片（WidgetCard.ets）相关信息。

## 方式二：独立包方式创建卡片

### 创建步骤

**1. 新建工程**

在DevEco Studio中，选择创建Application或Atomic Service工程，这两种都支持创建卡片。工程创建指导具体请参考[创建一个新的工程](../../../../开发环境搭建/工程创建/创建一个新的工程/ide-create-new-project.md)。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/78/v3/BAHGR565S3u1NgsYOASEHA/zh-cn_image_0000002592378632.png?HW-CC-KV=V1&HW-CC-Date=20260611T063730Z&HW-CC-Expire=86400&HW-CC-Sign=05B901DB877079BCAEFE50C600B67E8794A6C8F64DC94D42F80131917A3560F1)

说明

基于不同版本的DevEco Studio，请以实际界面为准。

**2. 新建卡片**

* 选中entry目录单击右键选择【New】->【Service Widget】->【Dynamic Widget(Standalone)】。在Service Widget菜单可直接选择创建独立包的动态卡片（Dynamic Widget(standalone)）或静态卡片（Static Widget(standalone)）。创建服务卡片后，也可以在卡片的[form\_config.json配置文件](../配置ArkTS卡片的配置文件/arkts-ui-widget-configuration.md#配置文件字段说明)中，通过isDynamic参数修改卡片类型：isDynamic置空或赋值为“true”，则该卡片为[动态卡片](../ArkTS卡片概述/arkts-form-overview.md#动态卡片)；isDynamic赋值为"false"，则该卡片为[静态卡片](../ArkTS卡片概述/arkts-form-overview.md#静态卡片)。静态卡片和动态卡片切换之后用户交互实现也需要修改，具体参考ArkTS卡片概述中的[动态卡片](../ArkTS卡片概述/arkts-form-overview.md#动态卡片)和[静态卡片](../ArkTS卡片概述/arkts-form-overview.md#静态卡片)。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e2/v3/B8px7QabTr-DggNbJNUpvw/zh-cn_image_0000002622698263.png?HW-CC-KV=V1&HW-CC-Date=20260611T063730Z&HW-CC-Expire=86400&HW-CC-Sign=A04558BA7E3F51884DF67F292F3FFF7AB70AA6EA9E55A297AFFD74B5FA5FB6B8)
* 选择模板后，点击【Next】。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/45/v3/81r_TnPOQcelueskKaJnLw/zh-cn_image_0000002622698261.png?HW-CC-KV=V1&HW-CC-Date=20260611T063730Z&HW-CC-Expire=86400&HW-CC-Sign=941E800EA85DE29A4DBEE146F97AD53898EBF64B8BF265139C719ACA56EFD38A)
* 填写卡片配置之后点击【Finish】。卡片创建成功后，entry包中包含应用和卡片后端能力；library包中包含卡片UI侧能力。entry模块下的module.json5配置文件中的formWidgetModule字段需关联library模块，library模块下的module.json5配置文件中的formExtensionModule字段需关联entry模块，以实现卡片包和应用包相互关联。创建完成后，会自动生成配置文件并配置，后续也可以按照[卡片配置文件](../配置ArkTS卡片的配置文件/arkts-ui-widget-configuration.md)修改配置。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/85/v3/yLR3Y1wzTxG_oktDjKNVRw/zh-cn_image_0000002592218702.png?HW-CC-KV=V1&HW-CC-Date=20260611T063730Z&HW-CC-Expire=86400&HW-CC-Sign=6A5B2C7B8403F57F225E6D54929EE2E8F7264C0D00662D5A6C2E3F709F8E51FB)

### 工程结构介绍

独立卡片包与卡片共包方式创建卡片，仅工程结构存在差异，生成的文件是一致的，各文件具体内容请参考[共包方式工程结构介绍](arkts-ui-widget-creation.md#工程结构介绍)。

**图2** 独立卡片包工程目录。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/82/v3/J1vErKd_T5iU6yA-vrMztg/zh-cn_image_0000002592378636.png?HW-CC-KV=V1&HW-CC-Date=20260611T063730Z&HW-CC-Expire=86400&HW-CC-Sign=A67B9D588D2C4DB3BB88715EE997A1AEE7534F8ED4E7BE842E60D62130D8DD29)

说明

独立卡片包中应用包和卡片包为2个独立模块，因此需要关注同时安装的应用包和卡片包版本号一致。
