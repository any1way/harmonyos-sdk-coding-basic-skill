---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/changelogs-for-all-apps-6101
title: 针对所有应用的变更
breadcrumb: 版本说明 > HarmonyOS 6.1.0(23) > OS平台能力 > OS平台行为变更说明 > 针对所有应用的变更
category: harmonyos-releases
scraped_at: 2026-06-01T10:39:38+08:00
doc_updated_at: 2026-05-26
content_hash: sha256:2a8807db8e7d901f3ee0e90fa29a3191bc936712505616fe68f25fd7feb8de15
---
## ArkUI

### Progress组件color属性设置渐变色规格变更

**变更原因**

Progress的渐变色能力增强，新增支持通过color设置Linear和Capsule进度条前景色为渐变色。

**变更影响**

此变更涉及应用适配。

说明

此变更已做版本隔离，变更仅在应用的targetSdkVersion设置为大于等于6.1.0(23)时生效。

变更前：Progress进度条的Linear和Capsule样式通过color设置渐变色，设置后仅会显示为默认主题色。

变更后：Progress进度条的Linear和Capsule样式通过color设置渐变色，设置后会显示为指定的渐变色。

例如使用下面代码，通过color设置Linear和Capsule样式进度条的前景色为渐变色，变更前均显示为默认主题色蓝色，变更后可以显示为实际的设置效果。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct ProgressExample {
5. private gradientColor: LinearGradient = new LinearGradient([{ color: "#E5B87B", offset: 0.5 },
6. { color: "#E05F2A", offset: 1.0 }])
7. public gradientColor2: LinearGradient = new LinearGradient([{ color: "#99CD78", offset: 0.5 },
8. { color: "#53BA49", offset: 1.0 }])

10. build() {
11. Column({ space: 15 }) {
12. Text('Linear：').fontSize(9).width('90%')
13. Progress({ value: 70, total: 100, type: ProgressType.Linear })
14. .width(200).style({ strokeWidth: 10 })
15. .color(this.gradientColor)

17. Text('Capsule：').fontSize(9).width('90%')
18. Progress({ value: 50, total: 100, type: ProgressType.Capsule })
19. .width(200).style({ strokeWidth: 40 })
20. .color(this.gradientColor2)
21. }.width('100%').padding({ top: 5 })
22. }
23. }
```

| 变更前 | 变更后 |
| --- | --- |
|  |  |

**起始API Level**

7

**变更的接口/组件**

Progress组件的color属性。

**适配指导**

开发者需根据实际需求进行适配，如果期望进度条设置为单色，color中value参数的类型需为ResourceColor，参考示例如下。如果期望设置为渐变色，value参数的类型需为LinearGradient。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct ProgressExample {
5. build() {
6. Column({ space: 15 }) {
7. Text('Linear Progress').fontSize(9).fontColor(0xCCCCCC).width('90%')
8. Progress({ value: 20, total: 150, type: ProgressType.Linear }).color(Color.Grey).value(50).width(200)

10. Text('Capsule Progress').fontSize(9).fontColor(0xCCCCCC).width('90%')
11. Row({ space: 40 }) {
12. Progress({ value: 20, total: 150, type: ProgressType.Capsule }).color(Color.Grey).value(50).width(100).height(50)
13. }
14. }.width('100%').margin({ top: 30 })
15. }
16. }
```

### 横屏悬浮窗尺寸优化

**变更原因**

应用横屏布局尺寸按横屏屏幕大小布局，旧悬浮窗尺寸过小导致要额外适配显示布局。

**变更影响**

显示效果调整，横屏悬浮窗应用布局尺寸优化，仅改变应用布局尺寸，通过调整scale值保障用户界面看到的窗口大小不变。

以下场景可能需要应用适配：应用监听窗口size做了不同布局效果。

变更前：布局尺寸使用屏幕**宽度**作为横向应用布局宽度，高是宽的一定比例。

变更后：布局尺寸使用屏幕**高度**作为横向应用布局宽度，高是宽的一定比例。

**起始API Level**

6

**变更的接口/组件**

不涉及

**适配指导**

默认效果变更，开发者需审视此变更是否对自身相关业务代码逻辑产生影响，若有影响需根据自身业务代码进行对应适配。

### 新增状态管理V1校验报错

**变更原因**

自定义组件struct中使用状态管理V1的装饰器装饰Function类型的变量时，会出现运行时crash异常，提示开发者不支持装饰Function类型。为提升开发者运行时代码的稳定性，新增编译报错：如果自定义组件struct中使用状态管理V1的装饰器装饰Function类型的变量，则编译报错并中断编译。

**变更影响**

此变更涉及应用适配。

变更前：自定义组件struct中使用状态管理V1装饰器装饰Function类型的变量时，编译能通过，但运行时会出现crash，并提示不支持该装饰方式。

变更后：新增编译报错：如果自定义组件struct中使用状态管理V1的装饰器装饰Function类型的变量，则编译报错并中断编译，编译报错：The V1 decorator 'xxx' cannot be applied to a Function-type variable 'yyy'。

**起始 API Level**

不涉及API

**变更的接口/组件**

ArkUI状态管理V1装饰器：

@State, @Prop, @Link, @Provide, @Consume, @StorageLink, @LocalStorageLink, @StorageProp, @LocalStorageProp, @ObjectLink

**适配指导**

当被状态管理V1的装饰器装饰的变量类型为Function类型（如下示例为Function类型）时，可以将对应的状态管理V1的装饰器移除，使用常规变量声明修复编译与运行时异常。

编译报错示例：

```
1. @Entry
2. @Component
3. struct Index {
4. @State func1: Function = () => {}; // 编译报错
5. @State func2: (input: number) => void = (input: number) => {}; // 编译报错

7. build() {
8. // 业务代码
9. }
10. }
```

将@State移除后可修复编译报错：

```
1. @Entry
2. @Component
3. struct Index {
4. func1: Function = () => {};
5. func2: (input: number) => void = (input: number) => {};

7. build() {
8. // 业务代码
9. }
10. }
```

## ArkGraphics 2D（该变更同时涉及ArkUI）

### WordBreak.HYPHENATION移除以下六种语言连字符“-”断词换行能力的支持：捷克语、印度尼西亚语、拉脱维亚语、马其顿语、斯洛伐克语、塞尔维亚语

**变更原因**

Hyphen库将移除部分不兼容语种，这些语种的连字符“-”进行断词换行能力将会失效。

**变更影响**

变更前：针对捷克语、印度尼西亚语、拉脱维亚语、马其顿语、斯洛伐克语、塞尔维亚语的语言环境下，Hyphen断词模式下会有连字符“-”断词换行效果。

变更后：针对捷克语、印度尼西亚语、拉脱维亚语、马其顿语、斯洛伐克语、塞尔维亚语的语言环境下，Hyphen断词模式下连字符“-”断词换行效果不再生效，换行效果自动回落到以单词为单位进行换行。

**起始 API Level**

18

**变更的接口/组件**

* ArkUI：文本组件text.d.ts文件TextAttribute中wordBreak属性对应属性值：WordBreak.HYPHENATION
* ArkGraphics 2D：
  + ArkTS API：@ohos.graphics.text.d.ts文件interface ParagraphStyle中wordBreak属性对应属性值：WordBreak.BREAK\_HYPHEN
  + C API：drawing\_text\_typography.h文件enum OH\_Drawing\_WordBreakType中类型：WORD\_BREAK\_TYPE\_BREAK\_HYPHEN

**适配指导**

默认效果变更：接口默认效果变更，但开发者需审视此变更是否对自身相关业务展示效果产生影响，若有影响需根据自身业务代码进行对应适配。

## Localization Kit

### 全球化接口与运行时接口本地化显示优化及换行能力增强

**变更原因**

ICU版本已从72.1升级至74.2，本次升级基于[ICU 74.2数据](https://icu.unicode.org/download/74)，优化了本地化表达习惯，使部分全球化接口及运行时接口的行为更贴合各地区的语言使用规范，同时提升了系统的文本换行处理能力。

**变更影响**

此变更涉及应用适配。

具体接口行为变化详见**变更的接口/组件**，系统换行能力更新如下：

| 变更前 | 变更后 |
| --- | --- |
| 中日韩表意字符未包含 U+2EBF0 至 U+2EE5F 范围内的字符。 | 中日韩表意字符新增该范围内 622 个表意字符及 5 个具有特殊含义的表意字符。 |
| 缅甸语、泰语、老挝语、高棉语不支持正字法音节之间进行断行处理，例如在Text控件中，缅甸语文本“သော့换行点ခလောက်”会在“换行点”处断开。 | 缅甸语、泰语、老挝语、高棉语支持正字法音节之间进行断行处理，例如在Text控件中，缅甸语文本“换行点သော့ခလောက်”会在“换行点”处断开。 |

**起始API Level**

API 6

**变更的接口/组件**

| 接口 | 变更场景举例 | 变更前返回值 | 变更后返回值 |
| --- | --- | --- | --- |
| [intl.DateTimeFormat.format](<../../../../../harmonyos-references/Localization Kit（本地化开发服务）/ArkTS API/@ohos.intl (国际化-Intl)/js-apis-intl.md#formatdeprecated>) | 繁体中文下格式化2024年4月23日 | 2024年4月23日 | 2024 年 4 月 23 日 |
| [intl.DateTimeFormat.formatRange](<../../../../../harmonyos-references/Localization Kit（本地化开发服务）/ArkTS API/@ohos.intl (国际化-Intl)/js-apis-intl.md#formatrangedeprecated>) | 英式英语下格式化2020年12月20日至21日 | 20/12/2020 – 21/12/2020 | 20/12/2020 – 21/12/2020 （日期间连接符变更） |
| [intl.Locale.maximize](<../../../../../harmonyos-references/Localization Kit（本地化开发服务）/ArkTS API/@ohos.intl (国际化-Intl)/js-apis-intl.md#maximizedeprecated>) | 区域ID为hy-arevmda | hyw | hyw-Armn-AM |
| [intl.Locale.minimize](<../../../../../harmonyos-references/Localization Kit（本地化开发服务）/ArkTS API/@ohos.intl (国际化-Intl)/js-apis-intl.md#minimizedeprecated>) | 区域ID为und-150 | ru | en-150 |
| [intl.RelativeTimeFormat.format](<../../../../../harmonyos-references/Localization Kit（本地化开发服务）/ArkTS API/@ohos.intl (国际化-Intl)/js-apis-intl.md#formatdeprecated-1>) | 英文下显示在1季度内 | in 1 qtr. | in 1q |
| [i18n.System.getDisplayCountry](<../../../../../harmonyos-references/Localization Kit（本地化开发服务）/ArkTS API/@ohos.i18n (国际化-I18n)/js-apis-i18n.md#getdisplaycountry9>) | 地区ID是AC，语言ID是es | Isla de la Ascensión | Isla Ascensión |
| [i18n.System.getDisplayLanguage](<../../../../../harmonyos-references/Localization Kit（本地化开发服务）/ArkTS API/@ohos.i18n (国际化-I18n)/js-apis-i18n.md#getdisplaylanguage9>) | 中文下显示语言ID为yue的名称 | 粤文 | 粤语 |
| [i18n.Transliterator.transform](<../../../../../harmonyos-references/Localization Kit（本地化开发服务）/ArkTS API/@ohos.i18n (国际化-I18n)/js-apis-i18n.md#transform9>) | 将꽇转换为拉丁文 | 꽇 | kē |
| [i18n.TimeZone.getDisplayName](<../../../../../harmonyos-references/Localization Kit（本地化开发服务）/ArkTS API/@ohos.i18n (国际化-I18n)/js-apis-i18n.md#getdisplayname>) | Asia/Kamchatka时区在捷克语下的显示名称 | Petropavlovsko-kamčatský standardní čas | petropavlovsko-kamčatský standardní čas |
| [i18n.Calendar.getDisplayName](<../../../../../harmonyos-references/Localization Kit（本地化开发服务）/ArkTS API/@ohos.i18n (国际化-I18n)/js-apis-i18n.md#getdisplayname8>) | type参数为islamic\_tbla的历法在中文下的显示名称 | 伊斯兰天文历 | islamic-tbla |
| [i18n.getSimpleDateTimeFormatBySkeleton](<../../../../../harmonyos-references/Localization Kit（本地化开发服务）/ArkTS API/@ohos.i18n (国际化-I18n)/js-apis-i18n.md#i18ngetsimpledatetimeformatbyskeleton20>) | 框架字符串传入yMdhms在中文下格式化日期 | 13/12/2024 上午6:30:25 | 13/12/2024 上午 6:30:25 |
| Date.toLocaleDateString | 在阿拉伯语下格式化日期 | 'الخميس، ٢٠ ديسمبر ٢٠١٢' | 'الخميس، ٢٠ ديسمبر، ٢٠١٢' |
| Date.toLocaleString | 在英文下格式化日期 | 10/20/2022, 6:00:00 PM | 10/20/2022, 6:00:00 PM（PM前的空白字符变更） |
| Date.toLocaleTimeString | 在英文下格式化日期 | 6:00:00 PM | 6:00:00 PM（PM前的空白字符变更） |
| Intl.DateTimeFormat.format | 繁体中文下格式化2024年4月23日 | 2024年4月23日 | 2024 年 4 月 23 日 |
| Intl.DateTimeFormat.formatRange | 英式英语下格式化2020年12月20日至21日 | 20/12/2020 – 21/12/2020 | 20/12/2020 – 21/12/2020（日期间连接符变更） |
| Intl.DateTimeFormat.formatRangeToParts | 英语下格式化2020年12月20日至21日 | { type: "literal", value: " – " } | {"type":"literal","value":" – "}（value中空白字符变更） |
| Intl.ListFormat.format | 在中文下格式化列表 | Motorcycle、Bus和Car | Motorcycle、Bus、Car |
| Intl.RelativeTimeFormat.format | 英文下显示在1季度内 | in 1 qtr. | in 1q |
| Intl.Locale.maximize | 区域ID为hy-arevmda | hyw | hyw-Armn-AM |
| Intl.Locale.minimize | 区域ID为und-150 | ru | en-150 |
| [ubrk\_next](<../../../../../harmonyos-references/附录/Native api中导出的ICU4C符号列表/icu4c-symbol.md>) | 对文本“[service@baidu.com](mailto:service@baidu.com)”进行分词解析 | @ 符号会与相邻字母粘连，“[service@baidu.com](mailto:service@baidu.com)”被识别为一个不可分割的整体。 | @ 符号两侧会被识别为单词边界，被识别为“service”、“@”、“baidu.com”三个部分。 |

**适配指导**

接口默认效果变更，但开发者需审视此变更是否对自身相关业务展示效果产生影响，若有影响需根据自身业务代码进行对应适配。

## Media Library Kit

### 动态照片资源的PhotoKeys.DURATION字段值变更

**变更原因**

图库应用需获取动态照片中附带视频片段的时长，并根据该时长判断是否支持生成3D动态照片。因此动态照片PhotoKeys.DURATION字段的取值由图片资源的默认值0变更为动态照片附带视频片段的时长。

**变更影响**

变更前：动态照片（PhotoKeys.PHOTO\_SUBTYPE=PhotoSubtype.MOVING\_PHOTO）的PhotoKeys.DURATION字段值为0。

变更后：动态照片（PhotoKeys.PHOTO\_SUBTYPE=PhotoSubtype.MOVING\_PHOTO）的PhotoKeys.DURATION字段值为视频部分的时长；若无法解析则为-1。

如果应用使用PhotoKeys.DURATION字段进行业务逻辑判断，如判断图片和视频的分类，则需要进行适配，改为使用其他接口进行判断。

**起始 API Level**

14

**变更的接口/组件**

PhotoKeys.DURATION

**适配指导**

DURATION字段值仅可用于表示视频或动态照片中附带视频片段的时长，若需要判断图片和视频的分类，建议使用mimeType字段或PhotoKeys.PHOTO\_TYPE字段进行判断。具体判断方法和示例代码如下：

* 使用mimeType字段判断图片和视频资源类型，具体判断方式如下：

  + 当mimeType以'image/'开头时，表示该媒体文件为图片。
  + 当mimeType以'video/'开头时，表示该媒体文件为视频。

  示例：

  ```
  1. function getMediaTypeByMimeType(mimeType: string): string {
  2. if (mimeType.startsWith('video/')) {
  3. return 'video';
  4. } else if (mimeType.startsWith('image/')) {
  5. return 'image';
  6. }
  7. return 'unknown';
  8. }
  ```
* 使用PhotoKeys.PHOTO\_TYPE字段判断图片和视频资源类型，具体判断方式如下：

  + 当PhotoKeys.PHOTO\_TYPE为PhotoType.IMAGE时，表示该媒体文件为图片。
  + 当PhotoKeys.PHOTO\_TYPE为PhotoType.VIDEO时，表示该媒体文件为视频。

  调用getAssets接口查询指定URI对应的图片或视频的PhotoKeys.PHOTO\_TYPE，以区分媒体类型，需要申请'ohos.permission.READ\_IMAGEVIDEO'权限。

  通过picker的方式调用getAssets接口查询指定URI对应的图片或视频的PhotoKeys.PHOTO\_TYPE，以区分媒体类型，则不需要申请此权限，详情请参考[指定URI获取图片或视频资源](<../../../../../harmonyos-guides/媒体/Media Library Kit（媒体文件管理服务）/使用Picker选择媒体库资源/photoaccesshelper-photoviewpicker.md#指定uri获取图片或视频资源>)。

  示例：

  ```
  1. import { photoAccessHelper } from '@kit.MediaLibraryKit';
  2. import { dataSharePredicates } from '@kit.ArkData';

  4. async function getMediaTypeByPhotoType(phAccessHelper: photoAccessHelper.PhotoAccessHelper, uri: string): Promise<string> {
  5. let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
  6. predicates.equalTo(photoAccessHelper.PhotoKeys.URI, uri);
  7. let fetchOptions: photoAccessHelper.FetchOptions = {
  8. fetchColumns: [
  9. photoAccessHelper.PhotoKeys.PHOTO_TYPE
  10. ],
  11. predicates: predicates
  12. };
  13. try {
  14. let fetchResult: photoAccessHelper.FetchResult<photoAccessHelper.PhotoAsset> = await phAccessHelper.getAssets(fetchOptions);
  15. if (fetchResult !== undefined) {
  16. console.info('fetchResult success');
  17. let photoAsset: photoAccessHelper.PhotoAsset = await fetchResult.getFirstObject();
  18. if (photoAsset !== undefined) {
  19. console.info('photoAsset.displayName :' + photoAsset.displayName);
  20. let photoType: photoAccessHelper.PhotoKeys = photoAccessHelper.PhotoKeys.PHOTO_TYPE;
  21. let photoAssetPhotoType : number = Number(photoAsset.get(photoType.toString()))
  22. if (photoAssetPhotoType === photoAccessHelper.PhotoType.VIDEO) {
  23. return 'video';
  24. } else if (photoAssetPhotoType === photoAccessHelper.PhotoType.IMAGE) {
  25. return 'image';
  26. }
  27. return 'unknown';
  28. }
  29. }
  30. } catch (err) {
  31. console.error(`getAssets failed, error: ${err.code}, ${err.message}`);
  32. }
  33. return 'undefined';
  34. }
  ```

说明

如果应用需要判断媒体资源是否为动态照片，建议使用PhotoKeys.PHOTO\_SUBTYPE字段进行判断。可参考上述判断图片和视频资源类型的示例，调用getAssets接口查询指定URI对应的图片或视频的PhotoKeys.PHOTO\_SUBTYPE字段，当PhotoKeys.PHOTO\_SUBTYPE为PhotoSubtype.MOVING\_PHOTO时，表示该媒体文件为动态照片。

## Performance Analysis Kit

### JS OOM异常崩溃栈形式变更

**访问级别**

其他

**变更原因**

变更前应用发生JS OOM异常时，既可能产生JS Crash，也可能产生CPP Crash，影响三方生态应用对OOM异常的数据统计。

**变更影响**

此变更不涉及应用适配。

变更前：应用主线程堆发生JS OOM异常时产生JS Crash，worker/taskpool线程堆发生JS OOM异常时产生CPP Crash，共享堆发生JS OOM异常时，既可能产生JS Crash，也可能产生CPP Crash。

变更后：应用主线程堆、worker/taskpool线程堆以及共享堆发生js OOM异常时，仅会产生jscrash。

| 线程堆 | 变更前 | 变更后 |
| --- | --- | --- |
| 主线程堆 | JS Crash | JS Crash |
| Worker/TaskPool线程堆 | CPP Crash | JS Crash |
| 共享堆 | JS Crash/CPP Crash | JS Crash |

**起始 API Level**

API 12

**变更的接口/组件**

不涉及

**适配指导**

默认行为变更，开发者需审视此变更是否对自身相关业务代码逻辑产生影响，若有影响需根据自身业务代码进行对应适配。
