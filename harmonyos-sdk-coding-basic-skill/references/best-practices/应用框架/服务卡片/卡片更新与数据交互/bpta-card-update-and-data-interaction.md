---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-card-update-and-data-interaction
title: 卡片更新与数据交互
breadcrumb: 最佳实践 > 应用框架 > 服务卡片 > 卡片更新与数据交互
category: best-practices
scraped_at: 2026-06-11T16:57:40+08:00
doc_updated_at: 2026-03-12
content_hash: sha256:a9d7cdf116ed34f004d8631078bee0790078040cbd634ad3df6efb9bb40c5578
---
## 概述

服务卡片给用户提供一目了然的信息内容，具有易用可见、智能可选和多端可变的特点，提供给用户简洁、高效的体验。系统通过[卡片开发服务](<../../../../harmonyos-guides/应用框架/Form Kit（卡片开发服务）/form-kit.md>)（Form Kit），提供了丰富的服务卡片开发能力，涵盖了卡片的创建、交互、更新与管理等多个方面，使开发者能够高效完成个性化服务卡片的开发。

**图1** 天气卡片

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/83/v3/b5J-5bkPSFm3zlwZ4MKmew/zh-cn_image_0000002427681508.jpg?HW-CC-KV=V1&HW-CC-Date=20260611T085738Z&HW-CC-Expire=86400&HW-CC-Sign=C3C3878BEF6342C5C4F4972887594218517C5BB4A63453210A9111B77BB6C9CC "点击放大")

### 卡片更新场景

服务卡片通常用于展示最新的信息或数据。通过卡片更新机制，开发者可以确保卡片上展示的内容是最新的，从而满足用户对实时信息的需求。例如，新闻应用可以通过更新卡片来展示最新的新闻标题和摘要，天气应用可以通过更新卡片来提供最新的天气信息。

卡片更新的频率和策略直接影响用户体验。如果卡片内容长时间不更新，用户可能会认为应用不活跃或不可靠，从而降低对应用的信任度和使用频率。相反，通过合理的卡片更新机制，可以保持卡片内容的新鲜感和吸引力，提升用户的使用体验和满意度。

通常需要进行卡片数据加载或卡片更新的场景有以下几种类型：

**表1** 卡片更新场景

| 场景类型 | 场景描述 | | |
| --- | --- | --- | --- |
| 主动刷新 | * 添加卡片时，初始化卡片数据。 例如，从桌面添加卡片，弹出卡片预览弹窗时，进行卡片数据初始化加载。 | * 卡片UI交互时，进行卡片更新。 例如，点击卡片刷新按钮，更新卡片推荐内容；音乐类卡片点击播放按钮，拉起应用至后台播放音乐，更新播放按钮状态。 | * 应用侧交互引起变化，更新数据到卡片。 例如，在应用侧点击收藏按钮改变文章的收藏状态时，同步更新卡片的收藏状态。 |
| 被动刷新 | * 定时更新、定点更新以及指定下次刷新时间间隔更新。例如，定时更新新闻卡片的推荐内容。 | | |

本文将以[实现卡片更新与数据交互功能](https://gitcode.com/harmonyos_samples/CardInfoRefresh)示例应用为例，介绍卡片数据交互流程、如何实现常见的卡片更新场景以及卡片更新开发过程中的常见问题和注意事项。

## 实现原理

### 卡片运行机制简介

**图2** 卡片提供方和使用方  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1/v3/5HqYQ5XdQk6FxBHrU65lAA/zh-cn_image_0000002461241349.jpg?HW-CC-KV=V1&HW-CC-Date=20260611T085738Z&HW-CC-Expire=86400&HW-CC-Sign=3BB8E2F9C729FFC2816CA80B7FE8502CE2A377D023D151C72FDB402C255C650F "点击放大")

以天气卡片为例，天气应用作为[卡片提供方](<../../../../harmonyos-guides/应用框架/Form Kit（卡片开发服务）/Form Kit简介/formkit-overview.md#服务卡片架构>)，提供天气卡片的显示内容、控件布局和卡片交互处理逻辑。例如，天气卡片显示地点、温度和天气情况，点击卡片跳转至天气应用等。此时，桌面作为[卡片使用方](<../../../../harmonyos-guides/应用框架/Form Kit（卡片开发服务）/Form Kit简介/formkit-overview.md#服务卡片架构>)，即卡片的宿主应用，控制天气卡片在桌面中展示的位置并展示卡片内容。ArkTS服务卡片的实现依赖ArkTS卡片框架的能力，卡片框架管理卡片生命周期和刷新机制，负责卡片页面的渲染。如下图所示，卡片提供方和使用方都依赖于卡片框架，天气应用提供的天气卡片，其添加、删除和刷新依赖框架的卡片管理服务，桌面展示天气卡片内容依赖框架的卡片渲染服务。关于卡片提供方、使用方和卡片框架的详细内容可参考[ArkTS卡片实现原理](<../../../../harmonyos-guides/应用框架/Form Kit（卡片开发服务）/ArkTS卡片开发（推荐）/ArkTS卡片概述/arkts-form-overview.md#实现原理>)。

**图3** 卡片运行机制示例

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b8/v3/_5B7p1IWQBOELBhjWkZAcg/zh-cn_image_0000002461241901.jpg?HW-CC-KV=V1&HW-CC-Date=20260611T085738Z&HW-CC-Expire=86400&HW-CC-Sign=57369C6355F39A643ADAF5154FCE460481FDA93223D8D556046C8D4AF3DBBDB4 "点击放大")

### 卡片数据交互

卡片更新场景的实现，依赖于[FormExtensionAbility](<../../../../harmonyos-references/Form Kit（卡片开发服务）/ArkTS API/@ohos.app.form.FormExtensionAbility (FormExtensionAbility)/js-apis-app-form-formextensionability.md>)生命周期、[formProvider模块](<../../../../harmonyos-references/Form Kit（卡片开发服务）/ArkTS API/@ohos.app.form.formProvider (formProvider)/js-apis-app-form-formprovider.md>)提供的[updateForm()](<../../../../harmonyos-references/Form Kit（卡片开发服务）/ArkTS API/@ohos.app.form.formProvider (formProvider)/js-apis-app-form-formprovider.md#formproviderupdateform>)接口和卡片框架提供的卡片刷新机制。如下图所示，应用主进程和应用的卡片进程是两个独立的进程，应用主进程持有[UIAbility](<../../../../harmonyos-guides/应用框架/Ability Kit（程序框架服务）/Stage模型开发指导/Stage模型应用组件/UIAbility组件/uiability.md>)，应用的卡片进程持有[FormExtensionAbility](<../../../../harmonyos-references/Form Kit（卡片开发服务）/ArkTS API/@ohos.app.form.FormExtensionAbility (FormExtensionAbility)/js-apis-app-form-formextensionability.md>)。卡片的UI页面由系统服务统一进行渲染，由卡片使用方（例如桌面）进行呈现。如果卡片数据不依赖于应用主进程，在卡片进程中使用卡片框架能力就能实现卡片更新。如果卡片数据依赖于应用主进程，应用主进程使用[FormProvider模块](<../../../../harmonyos-references/Form Kit（卡片开发服务）/ArkTS API/@ohos.app.form.formProvider (formProvider)/js-apis-app-form-formprovider.md>)提供的[updateForm()](<../../../../harmonyos-references/Form Kit（卡片开发服务）/ArkTS API/@ohos.app.form.formProvider (formProvider)/js-apis-app-form-formprovider.md#formproviderupdateform>)接口更新卡片时，需要明确卡片ID，所以卡片ID在添加卡片时需要进行存储，此类场景下需要借助卡片框架和数据存储等系统能力，保证应用主进程和卡片进程的卡片ID数据一致性。

**图4** 应用主进程与卡片进程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dc/v3/6-dW6VnNSiCz4sBuZbodKA/zh-cn_image_0000002427844140.jpg?HW-CC-KV=V1&HW-CC-Date=20260611T085738Z&HW-CC-Expire=86400&HW-CC-Sign=C071AF433482155FBD59FFA5A9DCF418C3E938EA0BFD58380E05B22EA50122D3 "点击放大")

本文主要介绍由卡片或应用UI交互引起的、由系统刷新机制定时或定点触发的[卡片更新场景](bpta-card-update-and-data-interaction.md#section430210710274)。一般情况下，卡片实现这几种常见场景就可以满足用户对卡片信息更新的诉求。还有一类是需要实时更新信息的应用卡片，例如出行打车类卡片，用户对信息的实时性要求很高，这类场景可以通过[Push Kit（推送服务）](<../../../../harmonyos-guides/应用服务/Push Kit（推送服务）/push-kit-guide.md>)的能力来实现，详细可参考[推送卡片刷新消息](<../../../../harmonyos-guides/应用服务/Push Kit（推送服务）/推送场景化消息/推送卡片刷新消息/push-form-update.md>)。

## 卡片数据初始化

### 场景描述

添加卡片时需要对卡片进行数据初始化，卡片创建及卡片配置参考[ArkTS卡片开发指导](<../../../../harmonyos-guides/应用框架/Form Kit（卡片开发服务）/ArkTS卡片开发（推荐）/arkts-ui.md>)，本章节将对卡片数据初始化的流程进行介绍。

**图5** 卡片预览页  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b1/v3/8eaTZyf0SV-5_ssC4GoT6w/zh-cn_image_0000002194011496.png?HW-CC-KV=V1&HW-CC-Date=20260611T085738Z&HW-CC-Expire=86400&HW-CC-Sign=80EEC557AD4EA343F38C0DF4DE500C32C11D54266832676BAE9F10CE49D31798 "点击放大")

### 开发流程

添加卡片时，卡片数据初始化流程：

**图6** 卡片数据初始化流程  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/69/v3/UxLpFFSzRqWUBrMP5XslrA/zh-cn_image_0000002461363873.jpg?HW-CC-KV=V1&HW-CC-Date=20260611T085738Z&HW-CC-Expire=86400&HW-CC-Sign=C44D9E4B2B11312E40FD3CD46EC5671CDB686A548B74FA3141E66F6A24F66E61 "点击放大")

桌面长按应用图标待展示卡片列表时，首先触发[FormExtensionAbility](<../../../../harmonyos-references/Form Kit（卡片开发服务）/ArkTS API/@ohos.app.form.FormExtensionAbility (FormExtensionAbility)/js-apis-app-form-formextensionability.md>)生命周期接口onAddForm()。使用卡片参数枚举[FormParam](<../../../../harmonyos-references/Form Kit（卡片开发服务）/ArkTS API/@ohos.app.form.formInfo (formInfo)/js-apis-app-form-forminfo.md#formparam>)可以从生命周期接口onAddForm()的入参[want](<../../../../harmonyos-references/Ability Kit（程序框架服务）/ArkTS API/通用能力的接口(推荐)/@ohos.app.ability.Want (Want)/js-apis-app-ability-want.md>)中取出卡片的相关信息如卡片标识、卡片名称、卡片宽高等。针对必要的信息可以进行判断或者保存等操作。

```
import { Want } from '@kit.AbilityKit';
import { formBindingData, FormExtensionAbility, formInfo, formProvider } from '@kit.FormKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
// ...
const TAG: string = 'EntryFormAbility';

export default class EntryFormAbility extends FormExtensionAbility {
  onAddForm(want: Want): formBindingData.FormBindingData {
    if (!want || !want.parameters) {
      hilog.error(0x0000, TAG, `FormAbility onAddForm want or want.parameters is undefined`);
      return formBindingData.createFormBindingData('');
    }
    do {
      let formName: string = want.parameters[formInfo.FormParam.NAME_KEY] as string;
      let formId: string = want.parameters[formInfo.FormParam.IDENTITY_KEY] as string;
      // ...
    } while (0);
    return formBindingData.createFormBindingData('');
  }

  // ...
}
```

[EntryFormAbility.ets](https://gitcode.com/harmonyos_samples/CardInfoRefresh/blob/master/entry/src/main/ets/entryformability/EntryFormAbility.ets#L19-L173)

创建需要返回卡片的数据类，可以是包含若干键值对的Object或JSON格式的字符串。使用卡片数据绑定模块[formBindingData](<../../../../harmonyos-references/Form Kit（卡片开发服务）/ArkTS API/@ohos.app.form.formBindingData (卡片数据绑定类)/js-apis-app-form-formbindingdata.md#formbindingdata>)的createFormBindingData()接口封装卡片需要使用的数据类，作为生命周期接口onAddForm()的返回值并传递给卡片。

说明：若onAddForm()接口中无法直接构建数据类作为接口返回值初始化卡片，例如依赖数据库查询结果或等待网络数据等使用异步的场景，可以使用[formProvider模块](<../../../../harmonyos-references/Form Kit（卡片开发服务）/ArkTS API/@ohos.app.form.formProvider (formProvider)/js-apis-app-form-formprovider.md>)提供的[updateForm()](<../../../../harmonyos-references/Form Kit（卡片开发服务）/ArkTS API/@ohos.app.form.formProvider (formProvider)/js-apis-app-form-formprovider.md#formproviderupdateform>)接口将异步获取的数据推送至卡片。

```
export class FormData {
  formId: string = '';
  formTime: string = '';
  isFavor?: boolean = false;
  index?: number = 0;
  cardList: Array<CardListItemData> = [];

  constructor(formId: string) {
    this.formId = formId;
  }
}
```

[CommonData.ets](https://gitcode.com/HarmonyOS_Samples/CardInfoRefresh/blob/master/entry/src/main/ets/common/CommonData.ets#L42-L52)

```
import { BusinessError, systemDateTime } from '@kit.BasicServicesKit';
import { Want } from '@kit.AbilityKit';
import { formBindingData, FormExtensionAbility, formInfo, formProvider } from '@kit.FormKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { CardListItemData, CommonData, FormData } from '../common/CommonData';
// ...
export default class EntryFormAbility extends FormExtensionAbility {
  onAddForm(want: Want): formBindingData.FormBindingData {
    if (!want || !want.parameters) {
      hilog.error(0x0000, TAG, `FormAbility onAddForm want or want.parameters is undefined`);
      return formBindingData.createFormBindingData('');
    }
    do {
      let formName: string = want.parameters[formInfo.FormParam.NAME_KEY] as string;
      let formId: string = want.parameters[formInfo.FormParam.IDENTITY_KEY] as string;
      // ...
      if (formName === 'card_info_refresh') {
        let formData = new FormData(formId);
        formData.formTime = systemDateTime.getTime().toString();
        let formInfo: formBindingData.FormBindingData = formBindingData.createFormBindingData(formData);
        return formInfo;
      }

      let key: string = `${formId}_show_index`;
      let data = util.getFormInitData(key, preferences);
      if (formName === 'card_info_update') {
        // Save the index of the data items currently displayed on the card.
        util.preferencesPut(preferences, key, data.id);
        let formData = new FormData(formId);
        formData.cardList.push(data);
        let formInfo: formBindingData.FormBindingData = formBindingData.createFormBindingData(formData);
        return formInfo;
      }
    } while (0);
    return formBindingData.createFormBindingData('');
  }

  // ...
}
```

[EntryFormAbility.ets](https://gitcode.com/HarmonyOS_Samples/CardInfoRefresh/blob/master/entry/src/main/ets/entryformability/EntryFormAbility.ets#L17-L174)

卡片页面使用页面级的UI状态存储[LocalStorage](<../../../../harmonyos-guides/应用框架/ArkUI（方舟UI框架）/UI开发 (ArkTS声明式开发范式)/学习UI范式状态管理/状态管理（V1）/管理应用拥有的状态/LocalStorage：页面级UI状态存储/arkts-localstorage.md>)接收onAddForm()接口传递的数据。使用装饰器@LocalStorageProp装饰的状态变量接收数据类的详细信息，装饰器@LocalStorageProp(key)中的key值需与数据类的键值一一对应。使用获取的数据初始化卡片页面。

```
let storageLocal = new LocalStorage();

@Entry(storageLocal)
@Component
struct WidgetCard {
  // ...
  @LocalStorageProp('formTime') @Watch('onFormTimeChange') formTime: string = '';
  @LocalStorageProp('formId') formId: string = '';
  // ...
  onFormTimeChange() {
    // ...
  }
  // ...
  build() {
    // ...
  }
}
```

[WidgetCard.ets](https://gitcode.com/HarmonyOS_Samples/CardInfoRefresh/blob/master/entry/src/main/ets/widget/pages/WidgetCard.ets#L20-L212)

## 卡片UI交互引起卡片更新

### 场景描述

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/03/v3/iOI-fV-6S3K9_f4j1AwhmA/zh-cn_image_0000002229451777.gif?HW-CC-KV=V1&HW-CC-Date=20260611T085738Z&HW-CC-Expire=86400&HW-CC-Sign=37C6D14DDB9FAA3D4B94E874C20E7FCAC7AEF61F4C25A3D52CEF7E6F969D61E1 "点击放大")

一般情况下，简单的卡片UI交互会引起卡片更新。例如，智能家电控制类卡片，通过卡片控制家电开关时，卡片上的开关状态会随设备状态而改变；点击新闻类卡片刷新按钮，从网络获取最新数据更新推荐内容列表。这类更新场景可以[通过message事件](<../../../../harmonyos-guides/应用框架/Form Kit（卡片开发服务）/ArkTS卡片开发（推荐）/ArkTS卡片提供方开发指导/ArkTS卡片页面交互/卡片传递消息给应用（message事件）/arkts-ui-widget-event-formextensionability.md>)实现，仅在卡片进程就可以完成卡片更新。

### 开发流程

**图7** 卡片UI交互引起更新  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3e/v3/Ld-ZdsF6QmOimqPbJalb0Q/zh-cn_image_0000002427845712.jpg?HW-CC-KV=V1&HW-CC-Date=20260611T085738Z&HW-CC-Expire=86400&HW-CC-Sign=7DCDDBB98C132CECBE44D6232121754C969C249471D584AC31D7CF3F52C208DF "点击放大")

在卡片页面注册onClick()点击事件，动态卡片使用postCardAction()接口，静态卡片使用FormLink组件触发事件。本文以动态卡片为例，在点击事件回调中调用postCardAction()接口，action参数选择message触发message事件。message事件未设置abilityName参数时，默认拉起FormExtensionAbility。

```
Row() {
  this.buttonBuilder($r('app.string.message'))
}
.onClick(() => {
  postCardAction(this, {
    action: 'message',
    params: {
      message: 'Message refresh card.'
    }
  });
})
```

[WidgetCard.ets](https://gitcode.com/harmonyos_samples/CardInfoRefresh/blob/master/entry/src/main/ets/widget/pages/WidgetCard.ets#L172-L182)

message事件拉起FormExtensionAbility后触发onFormEvent()生命周期，构建卡片需要更新的数据类，调用[updateForm()](<../../../../harmonyos-references/Form Kit（卡片开发服务）/ArkTS API/@ohos.app.form.formProvider (formProvider)/js-apis-app-form-formprovider.md#formproviderupdateform>)接口推送数据至卡片。卡片页面中使用[LocalStorageProp](<../../../../harmonyos-guides/应用框架/ArkUI（方舟UI框架）/UI开发 (ArkTS声明式开发范式)/学习UI范式状态管理/状态管理（V1）/管理应用拥有的状态/LocalStorage：页面级UI状态存储/arkts-localstorage.md#localstorageprop>)装饰的状态变量更新后触发卡片更新。

```
import { formBindingData, FormExtensionAbility, formInfo, formProvider } from '@kit.FormKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { CardListItemData, CommonData, FormData } from '../common/CommonData';
// ...
const TAG: string = 'EntryFormAbility';

export default class EntryFormAbility extends FormExtensionAbility {
  // ...
  onFormEvent(formId: string, message: string) {
    // ...
    let formData = new FormData(formId);
    // ...
      let formMsg: formBindingData.FormBindingData = formBindingData.createFormBindingData(formData);
      formProvider.updateForm(formId, formMsg).then(() => {
        hilog.info(0x0000, TAG, 'updateForm success.');
      }).catch((error: Error) => {
        let err = error as BusinessError;
        hilog.error(0x0000, TAG, `updateForm failed. error code=${err.code}, message=${err.message}`);
      });
    } catch (error) {
      let err = error as BusinessError;
      hilog.error(0x0000, TAG, `getSync failed, error code=${err.code}, message=${err.message}`);
    }
  }

  // ...
}
```

[EntryFormAbility.ets](https://gitcode.com/harmonyos_samples/CardInfoRefresh/blob/master/entry/src/main/ets/entryformability/EntryFormAbility.ets#L22-L175)

## 拉起应用至后台时更新卡片

### 场景描述

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/63/v3/-PvUh8NFQUuKmjl7CefkWg/zh-cn_image_0000002193851912.gif?HW-CC-KV=V1&HW-CC-Date=20260611T085738Z&HW-CC-Expire=86400&HW-CC-Sign=8FEB11EF5C28B2249660C9BACEE7C031E43D25B86B8A2F48EF5555973FBF47C7 "点击放大")

卡片UI交互引起卡片更新，实现和应用在前台时相同的功能。例如，音乐类卡片，点击播放或切换按钮，拉起后台播放音乐，同时更新卡片上的播放状态。这类更新场景可以[通过call事件](<../../../../harmonyos-guides/应用框架/Form Kit（卡片开发服务）/ArkTS卡片开发（推荐）/ArkTS卡片提供方开发指导/ArkTS卡片页面交互/卡片拉起应用UIAbility到后台（call事件）/arkts-ui-widget-event-call.md>)实现，需要在卡片进程拉起应用主进程至后台时更新卡片。

### 开发流程

**图8** 拉起应用至后台时更新卡片  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ac/v3/6xLKTp1sRjymUeDjyJgW7A/zh-cn_image_0000002461364589.jpg?HW-CC-KV=V1&HW-CC-Date=20260611T085738Z&HW-CC-Expire=86400&HW-CC-Sign=B047ADF2ED8B1E753EC80D43700B9FD2E3C06BBA638F7BF21E904254FD7210D5 "点击放大")

在卡片页面注册onClick()点击事件，本文以动态卡片为例，在回调中调用postCardAction()接口（静态卡片使用静态用的FormLink），action参数选择call并配置需要调用的方法和传递的数据，触发call事件后台拉起指定UIAbility。配置参数注意以下限制：

* abilityName参数仅支持配置当前应用下的UIAbility，即配置在module.json5文件中的UIAbility。
* method为必选参数，且类型为string类型，用于触发UIAbility中对应的方法。
* 在当前call事件触发指定卡片刷新场景中，需设置formId参数，用于UIAbility接收后更新当前卡片。

```
Row() {
  this.buttonBuilder($r('app.string.call'))
}
.onClick(() => {
  postCardAction(this, {
    action: 'call',
    abilityName: 'EntryAbility',
    params: {
      formId: this.formId,
      method: 'updateCardInfo',
      params: {
        message: 'Call refresh card.'
      }
    }
  });
})
```

[WidgetCard.ets](https://gitcode.com/harmonyos_samples/CardInfoRefresh/blob/master/entry/src/main/ets/widget/pages/WidgetCard.ets#L153-L168)

在被拉起的UIAbility的onCreate()生命周期中，需要配置监听call事件所需的方法，监听的方法名与call事件配置的method保持一致。通过[readString()](<../../../../harmonyos-references/IPC Kit（进程间通信服务）/ArkTS API/@ohos.rpc (RPC通信)/js-apis-rpc.md#readstring9>)方法读取传递的字符串值后，使用JSON.parse()解析传递的参数。使用传递的formId并构建更新卡片需要的数据类型，调用[updateForm()](<../../../../harmonyos-references/Form Kit（卡片开发服务）/ArkTS API/@ohos.app.form.formProvider (formProvider)/js-apis-app-form-formprovider.md#formproviderupdateform>)接口推送数据至卡片。

注意，进程退出时需在onDestroy()生命周期中解除监听；监听配置的方法需返回实现rpc.Parcelable()接口的数据类。

```
import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { formBindingData, formInfo, formProvider } from '@kit.FormKit';
import { rpc } from '@kit.IPCKit';
import { CardListItemData, CommonData, FormData } from '../common/CommonData';
// ...
const TAG: string = 'EntryAbility';

export default class EntryAbility extends UIAbility {
  private callFunc = (data: rpc.MessageSequence): MyParcelable => {
    try {
      let params: Record<string, string> = JSON.parse(data.readString());
      if (params.formId !== undefined) {
        let formId: string = params.formId;
        let formData = new FormData(formId);
        let util = PreferencesUtil.getInstance();
        let preferences = util.getPreferences(this.context);
        if (!preferences) {
          return new MyParcelable(1);
        }
        let index: number = preferences.getSync(CommonConstants.DATA_INDEX, 0) as number;
        formData.cardList = CommonData.getData(index);
        util.preferencesPut(preferences, CommonConstants.DATA_INDEX, index + 1);
        let formMsg: formBindingData.FormBindingData = formBindingData.createFormBindingData(formData);
        formProvider.updateForm(formId, formMsg).then((data) => {
          hilog.info(0x0000, TAG, 'updateForm success.', JSON.stringify(data));
        }).catch((error: Error) => {
          let err = error as BusinessError;
          hilog.error(0x0000, TAG, `updateForm failed. error code=${err.code}, message=${err.message}`);
        });
      }
    } catch (error) {
      let err = error as BusinessError;
      hilog.error(0x0000, TAG, `callFunc failed, error code=${err.code}, message=${err.message}`);
    }
    return new MyParcelable(1);
  };
  // ...
  onCreate(want: Want, _launchParam: AbilityConstant.LaunchParam): void {
    // ...
    try {
      this.callee.on('updateCardInfo', this.callFunc);
    } catch (error) {
      let err = error as BusinessError;
      hilog.error(0x0000, TAG, `on updateCardInfo failed, error code=${err.code}, message=${err.message}`);
    }
    // ...
  }

  // ...
  onDestroy(): void {
    // ...
    try {
      this.callee.off('updateCardInfo');
      // ...
    } catch (error) {
      let err = error as BusinessError;
      hilog.error(0x0000, TAG, `Failed to disconnect callee. Cause: error code=${err.code}, message=${err.message}`);
    }
  }

  // ...
}

class MyParcelable implements rpc.Parcelable {
  num: number;

  constructor(num: number) {
    this.num = num;
  }

  marshalling(dataOut: rpc.MessageSequence): boolean {
    try {
      dataOut.writeInt(this.num);
    } catch (error) {
      let err = error as BusinessError;
      hilog.error(0x0000, 'MyParcelable', `marshalling failed, error code=${err.code}, message=${err.message}`);
    }
    return true;
  }

  unmarshalling(dataIn: rpc.MessageSequence): boolean {
    try {
      this.num = dataIn.readInt();
    } catch (error) {
      let err = error as BusinessError;
      hilog.error(0x0000, 'MyParcelable', `unmarshalling failed, error code=${err.code}, message=${err.message}`);
    }
    return true;
  }
}
```

[EntryAbility.ets](https://gitcode.com/harmonyos_samples/CardInfoRefresh/blob/master/entry/src/main/ets/entryability/EntryAbility.ets#L17-L327)

说明

提供方应用需要具备后台运行权限（[ohos.permission.KEEP\_BACKGROUND\_RUNNING](../../../../harmonyos-guides/系统/安全/程序访问控制/应用权限管控/应用权限列表/开放权限（系统授权）/permissions-for-all.md#ohospermissionkeep_background_running)）。

## 从卡片跳转到应用后更新卡片

### 场景描述

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8e/v3/-awALCrjS_eo5UXAfaz1qA/zh-cn_image_0000002193851920.gif?HW-CC-KV=V1&HW-CC-Date=20260611T085738Z&HW-CC-Expire=86400&HW-CC-Sign=6368613D194E6FB58FFBB20E5F3823067E883B9995040B4CDBEF6797716119AF "点击放大")

卡片UI交互跳转至应用后，引起卡片更新。用于定时更新类卡片手动触发卡片更新。例如，天气类卡片，点击卡片跳转至应用，应用实时刷新天气，同时更新卡片展示的天气数据。这类更新场景可以[通过router事件](<../../../../harmonyos-guides/应用框架/Form Kit（卡片开发服务）/ArkTS卡片开发（推荐）/ArkTS卡片提供方开发指导/ArkTS卡片页面交互/卡片跳转到应用页面（router事件）/arkts-ui-widget-event-router.md>)实现，需要从卡片进程跳转至应用主进程后进行卡片更新。

### 开发流程

**图9** 跳转到应用后更新卡片

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5a/v3/UIYUUre5SRiKxJit7bE6dg/zh-cn_image_0000002427849920.jpg?HW-CC-KV=V1&HW-CC-Date=20260611T085738Z&HW-CC-Expire=86400&HW-CC-Sign=808A9403C039686D70D4E4B714D6A18B94E66F92C16A268E8EB21E44B2A2C1DA "点击放大")

在卡片页面注册onClick()点击事件，在回调中调用postCardAction()接口，action参数选择router触发router事件。router事件拉起指定的UIAbility，使用abilityName进行配置。

```
Row(){
  this.buttonBuilder($r('app.string.router'))
}
.onClick(() => {
  postCardAction(this, {
    action: 'router',
    abilityName: 'EntryAbility',
    params: {
      message: 'Router refresh card.'
    }
  });
})
```

[WidgetCard.ets](https://gitcode.com/harmonyos_samples/CardInfoRefresh/blob/master/entry/src/main/ets/widget/pages/WidgetCard.ets#L138-L149)

在UIAbility中接收router事件并获取参数。若UIAbility未在后台运行，触发onCreate生命周期回调。若UIAbility已在后台运行，会触发onNewWant()生命周期回调。生命周期参数want包含卡片相关信息，执行卡片相关操作。判断params中包含的参数，构建卡片更新需要的数据类，调用[updateForm()](<../../../../harmonyos-references/Form Kit（卡片开发服务）/ArkTS API/@ohos.app.form.formProvider (formProvider)/js-apis-app-form-formprovider.md#formproviderupdateform>)接口推送数据至卡片。

```
import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { formBindingData, formInfo, formProvider } from '@kit.FormKit';
import { rpc } from '@kit.IPCKit';
import { CardListItemData, CommonData, FormData } from '../common/CommonData';
// ...
const TAG: string = 'EntryAbility';

export default class EntryAbility extends UIAbility {
  // ...
  onCreate(want: Want, _launchParam: AbilityConstant.LaunchParam): void {
    // ...
    this.updateInfo(want);
    // ...
  }

  // ...
  onNewWant(want: Want, _launchParam: AbilityConstant.LaunchParam): void {
    this.updateInfo(want);
  }

  private updateInfo(want: Want) {
    if (!want || !want.parameters || want.parameters[formInfo.FormParam.IDENTITY_KEY] === undefined) {
      return;
    }
    let message: string = (JSON.parse(want.parameters?.params as string))?.message;
    if (message === 'Router refresh card.') {
      let formId = want.parameters[formInfo.FormParam.IDENTITY_KEY].toString();
      let formData = new FormData(formId);
      // ...
        let formMsg: formBindingData.FormBindingData = formBindingData.createFormBindingData(formData);
        formProvider.updateForm(formId, formMsg)
          .then((data) => {
            hilog.info(0x0000, TAG, 'updateForm success.', JSON.stringify(data));
          })
          .catch((error: Error) => {
            let err = error as BusinessError;
            hilog.error(0x0000, TAG, `updateForm failed, error code=${err.code}, message=${err.message}`);
          });
      } catch (error) {
        let err = error as BusinessError;
        hilog.error(0x0000, TAG, `updateInfo failed, error code=${err.code}, message=${err.message}`);
      }
    }
  }

  // ...
}
```

[EntryAbility.ets](https://gitcode.com/harmonyos_samples/CardInfoRefresh/blob/master/entry/src/main/ets/entryability/EntryAbility.ets#L16-L297)

## 从应用更新数据到卡片

### 场景描述

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c2/v3/Qa8-UOaPQTGVC5whkXsa3w/zh-cn_image_0000002193851888.png?HW-CC-KV=V1&HW-CC-Date=20260611T085738Z&HW-CC-Expire=86400&HW-CC-Sign=713E9DC0C259DA3BDE64F4B0CCB85BBDC29C465015B7FA0296191BA05D8CC8DA "点击放大")

以应用点击收藏场景为例。卡片展示内容在应用内数据列表中，当点击应用内收藏按钮，收藏状态应同步至卡片。

### 开发流程

应用侧UI交互引起卡片数据变化时：

**图10** 从应用更新数据到卡片流程  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ae/v3/YvWJrODEQtmb6-ob9YDOdw/zh-cn_image_0000002461368797.jpg?HW-CC-KV=V1&HW-CC-Date=20260611T085738Z&HW-CC-Expire=86400&HW-CC-Sign=78F2DA7767705556450E4E54315E3D84D74C6C7AB4A452623C16688152A1E990 "点击放大")

图片展示卡片创建时，在onAddForm()生命周期中使用首选项保存卡片ID至卡片ID列表及卡片当前状态。

```
import { Want } from '@kit.AbilityKit';
import { formBindingData, FormExtensionAbility, formInfo, formProvider } from '@kit.FormKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { CardListItemData, CommonData, FormData } from '../common/CommonData';
import { CommonConstants } from '../common/CommonConstants';
import { PreferencesUtil } from '../common/utils/PreferencesUtil';

const TAG: string = 'EntryFormAbility';

export default class EntryFormAbility extends FormExtensionAbility {
  onAddForm(want: Want): formBindingData.FormBindingData {
    if (!want || !want.parameters) {
      hilog.error(0x0000, TAG, `FormAbility onAddForm want or want.parameters is undefined`);
      return formBindingData.createFormBindingData('');
    }
    do {
      let formName: string = want.parameters[formInfo.FormParam.NAME_KEY] as string;
      let formId: string = want.parameters[formInfo.FormParam.IDENTITY_KEY] as string;
      let util = PreferencesUtil.getInstance();
      let preferences = util.getPreferences(this.context);
      if (!preferences) {
        break;
      }
      // Save form id using preferences.
      util.addFormId(preferences, formId);

      // ...
      let key: string = `${formId}_show_index`;
      let data = util.getFormInitData(key, preferences);
      if (formName === 'card_info_update') {
        // Save the index of the data items currently displayed on the card.
        util.preferencesPut(preferences, key, data.id);
        let formData = new FormData(formId);
        formData.cardList.push(data);
        let tempFormInfo: formBindingData.FormBindingData = formBindingData.createFormBindingData(formData);
        return tempFormInfo;
      }
    } while (0);
    return formBindingData.createFormBindingData('');
  }

  // ...
}
```

[EntryFormAbility.ets](https://gitcode.com/HarmonyOS_Samples/CardInfoRefresh/blob/master/entry/src/main/ets/entryformability/EntryFormAbility.ets#L20-L176)

应用侧收藏按钮注册onClick()事件，事件回调触发时，使用首选项更新收藏状态，查询当前正在展示该收藏状态变化的数据的卡片，更新收藏状态到对应卡片。

```
Row() {
  // ...
}
.onClick(() => {
  let util = PreferencesUtil.getInstance();
  let preferences = util.getPreferences(this.getUIContext().getHostContext()!);
  if(!preferences) {
    return;
  }
  this.statusArr[this.itemData.id] = !this.statusArr[this.itemData.id];
  this.itemData.favour = this.statusArr[this.itemData.id!];
  util.preferencesPut(preferences, 'statusArr', this.statusArr)

  // Update page display data.
  AppStorage.set('statusArr', [...this.statusArr]);

  let idArr = PreferencesUtil.getInstance().getFormIds(preferences);
  if (idArr.length > 0) {
    idArr.forEach((formId: string) => {
      if (!preferences) {
        return;
      }
      try {
        if (preferences.getSync(`${formId}_show_index`, -1) as number === this.itemData.id) {
          let formData = new FormData(formId);
          formData.cardList = [this.itemData];
          let formMsg: formBindingData.FormBindingData = formBindingData.createFormBindingData(formData);
          formProvider.updateForm(formId, formMsg).then(() => {
            hilog.info(0x0000, TAG, `updateForm success.`);
          }).catch((error: Error) => {
            let err = error as BusinessError;
            hilog.error(0x0000, TAG, `updateForm failed: error code=${err.code}, message=${err.message}`);
          });
        }
      } catch (error) {
        let err = error as BusinessError;
        hilog.error(0x0000, TAG, `getSync failed, error code=${err.code}, message=${err.message}`);
      }
    })
  }
})
```

[Index.ets](https://gitcode.com/harmonyos_samples/CardInfoRefresh/blob/master/entry/src/main/ets/pages/Index.ets#L91-L142)

## 定时、定点更新卡片

### 场景描述

使用天气类或日历类应用时，卡片需要每日更新当日最新数据，方便用户获取最及时的信息。新闻阅读类卡片展示热点文章列表时，需要随时间变化进行定时更新。

服务卡片支持通过定时刷新及定点刷新的方式实现以上场景。

在使用定时和定点刷新功能之前，需要在form\_config.json配置文件中设置updateEnabled字段为true，以启用周期性刷新功能。出于安全及性能考虑，每张卡片每天最多通过定时方式触发刷新50次，定时刷新包含[卡片配置项updateDuration](<../../../../harmonyos-guides/应用框架/Form Kit（卡片开发服务）/ArkTS卡片开发（推荐）/配置ArkTS卡片的配置文件/arkts-ui-widget-configuration.md>)和调用setFormNextRefreshTime方法两种方式，当达到50次配额后，无法通过定时方式再次触发刷新，刷新次数会在每天的0点重置。

### 开发流程

**定时刷新**

定时刷新表示在指定的时间间隔后自动刷新卡片内容。可以在[form\_config.json](<../../../../harmonyos-guides/应用框架/Form Kit（卡片开发服务）/ArkTS卡片开发（推荐）/配置ArkTS卡片的配置文件/arkts-ui-widget-configuration.md>)配置文件的updateDuration字段中进行设置。卡片定时刷新的更新周期updateDuration字段的单位为30分钟，即最短为半小时（1 \* 30min）刷新一次。当取值为0时，表示该参数不生效，当取值为正整数N时，表示刷新周期为30\*N分钟。

定时刷新触发后，系统调用onUpdateForm()的生命周期回调函数，使用[updateForm()](<../../../../harmonyos-references/Form Kit（卡片开发服务）/ArkTS API/@ohos.app.form.formProvider (formProvider)/js-apis-app-form-formprovider.md#formproviderupdateform>)方法更新卡片内容。

```
import { formBindingData, FormExtensionAbility, formInfo, formProvider } from '@kit.FormKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { CardListItemData, CommonData, FormData } from '../common/CommonData';
// ...
export default class EntryFormAbility extends FormExtensionAbility {
  // ...
  onUpdateForm(formId: string) {
    // ...
    let formData = new FormData(formId);
    // ...
    let formMsg: formBindingData.FormBindingData = formBindingData.createFormBindingData(formData);
    formProvider.updateForm(formId, formMsg).catch((err: BusinessError) => {
      hilog.error(0x0000, TAG, `updateForm failed, error code=${err.code}, message=${err.message}`);
    });
  }

  // ...
}
```

[EntryFormAbility.ets](https://gitcode.com/harmonyos_samples/CardInfoRefresh/blob/master/entry/src/main/ets/entryformability/EntryFormAbility.ets#L23-L177)

**定点刷新**

定点刷新表示在每天的某个指定的时间点自动刷新卡片内容。通过在form\_config.json文件中配置scheduledUpdateTime字段实现，例如配置为14:00。定点刷新触发后，系统调用FormExtensionAbility的[onUpdateForm()](<../../../../harmonyos-references/Form Kit（卡片开发服务）/ArkTS API/@ohos.app.form.FormExtensionAbility (FormExtensionAbility)/js-apis-app-form-formextensionability.md#formextensionabilityonupdateform>)生命周期回调，相关操作参考定时刷新。

注意，当同时配置了定时刷新updateDuration和定点刷新scheduledUpdateTime时，定时刷新的优先级更高。为实现定点刷新updateDuration需要配置为0，配置大于0的数字时会导致定点刷新不生效。

```
{
  "forms": [
    {
      "name": "card_info_refresh",
      "displayName": "$string:widget_display_name",
      "description": "$string:widget_desc",
      "src": "./ets/widget/pages/WidgetCard.ets",
      "uiSyntax": "arkts",
      "window": {
        "designWidth": 720,
        "autoDesignWidth": true
      },
      "colorMode": "auto",
      "isDynamic": true,
      "isDefault": true,
      "updateEnabled": true,
      "scheduledUpdateTime": "14:00",
      "updateDuration": 0,
      "defaultDimension": "4*4",
      "supportDimensions": [
        "4*4"
      ]
    },
    // ...
  ]
}
```

更多注意事项参考[卡片定时刷新和定点刷新](<../../../../harmonyos-guides/应用框架/Form Kit（卡片开发服务）/ArkTS卡片开发（推荐）/ArkTS卡片提供方开发指导/ArkTS卡片页面刷新/ArkTS卡片页面刷新概述/arkts-ui-widget-interaction-overview.md#被动刷新>)。

## 常见问题

### 如何刷新指定类型的多个卡片

刷新所有同类卡片首先需要保存同类卡片的formId。在onAddForm()生命周期中，通过判断卡片名称，卡片宽高等信息，识别同类型卡片，将formId分类并持久化，如使用首选项或RDB。

应用侧更新状态需同步卡片时，从持久化的数据中获取该类型的formId数组，遍历数组调用formProvider.updateForm()推送卡片更新需要的数据。当卡片移除时，需要在onRemoveForm()生命周期中判断formId是否在该类型数组中，若存在需删除该数据项并更新持久化数据。

### 如何管理当前已加桌的所有卡片ID

长按App图标，弹出下拉菜单点击卡片，或者长按某张卡片，选择更多卡片，弹出“卡片加桌弹窗”时，所有的卡片都会触发onAddForm()生命周期回调。手动关闭卡片加桌弹窗或息屏，退出“卡片加桌弹窗”时，会触发所有卡片的onRemoveForm()生命周期回调。点击“添加至桌面”添加卡片时，退出“卡片加桌弹窗”，会触发除当前加桌卡片之外的其他卡片的onRemoveForm()生命周期回调。

当触发onAddForm()生命周期回调时，将卡片ID存储到数据库。当触发onRemoveForm()生命周期回调时，将卡片ID从数据库删除。数据库中未被删除的卡片ID，即是当前已加桌的所有卡片ID。

## 示例代码

* [实现卡片更新与数据交互功能](https://gitcode.com/harmonyos_samples/CardInfoRefresh)
