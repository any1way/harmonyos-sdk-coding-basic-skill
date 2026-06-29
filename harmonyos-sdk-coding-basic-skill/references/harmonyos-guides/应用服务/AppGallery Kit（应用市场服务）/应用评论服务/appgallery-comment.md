---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/appgallery-comment
title: 应用评论服务
breadcrumb: 指南 > 应用服务 > AppGallery Kit（应用市场服务） > 应用评论服务
category: harmonyos-guides
scraped_at: 2026-06-11T15:04:22+08:00
doc_updated_at: 2026-04-30
content_hash: sha256:0e8c57fa51fe35ab412b0ad30847ce96db9ae7a388335304d32ee515c82405b7
---
通过应用评论服务，用户无需进入应用市场应用详情页，可以直接在应用内进行评论。

说明

从版本6.0.0(20)开始，支持拉起应用评论弹框。

## 场景介绍

开发者可以通过该接口拉起应用评论弹窗对应用进行评分及评论，无需进入应用市场应用详情页进行评论。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bb/v3/uqdpHBkJSBS9b65KiArsEg/zh-cn_image_0000002592379162.jpg?HW-CC-KV=V1&HW-CC-Date=20260611T070421Z&HW-CC-Expire=86400&HW-CC-Sign=58792B73F8D956B0DF19EE26EE9FCDC7550BF473A0F89376E581AB0BCCDB05EE)

## 业务流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/22/v3/8TieB6zHSjmn729ezs1M-A/zh-cn_image_0000002622858669.png?HW-CC-KV=V1&HW-CC-Date=20260611T070421Z&HW-CC-Expire=86400&HW-CC-Sign=C070604E3BDB53E5E35FB0D00E7D8DA3362CD90545D0AC4828C8C422BA91ED57)

1. 用户需要在应用内评论应用。
2. 应用调用[showCommentDialog](<../../../../harmonyos-references/AppGallery Kit（应用市场服务）/ArkTS API/commentManager（应用评论服务）/appgallery-commentmanager.md#commentmanagershowcommentdialog>)接口拉起应用评论弹窗。
3. AppGalleryKit返回接口调用结果给应用。
4. 应用返回评论窗口给用户。

## 约束与限制

应用评论服务不支持模拟器，请使用真机调试。

## 接口说明

应用评论服务提供以下接口，具体API说明详见[接口文档](<../../../../harmonyos-references/AppGallery Kit（应用市场服务）/ArkTS API/commentManager（应用评论服务）/appgallery-commentmanager.md>)。

| 接口名 | 描述 |
| --- | --- |
| [showCommentDialog](<../../../../harmonyos-references/AppGallery Kit（应用市场服务）/ArkTS API/commentManager（应用评论服务）/appgallery-commentmanager.md#commentmanagershowcommentdialog>)(context: common.UIExtensionContext | common.UIAbilityContext): Promise<void> | 拉起应用评论弹窗，用户可以在应用内评论应用。 |

## 开发步骤

1. 导入commentManager模块及相关公共模块。

   ```
   1. import { commentManager} from '@kit.AppGalleryKit';
   2. import { hilog } from '@kit.PerformanceAnalysisKit';
   3. import { BusinessError } from '@kit.BasicServicesKit';
   4. import type { common } from '@kit.AbilityKit';
   ```
2. 调用[showCommentDialog](<../../../../harmonyos-references/AppGallery Kit（应用市场服务）/ArkTS API/commentManager（应用评论服务）/appgallery-commentmanager.md#commentmanagershowcommentdialog>)方法拉起评论弹窗。

   ```
   1. try {
   2. const uiContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
   3. commentManager.showCommentDialog(uiContext).then(()=>{
   4. hilog.info(0, 'TAG', "succeeded in showing commentDialog.");
   5. }).catch((error: BusinessError<Object>) => {
   6. hilog.error(0, 'TAG', `showCommentDialog failed, Code: ${error.code}, message: ${error.message}`);
   7. });
   8. } catch (error) {
   9. hilog.error(0, 'TAG', `showCommentDialog failed, Code: ${error.code}, message: ${error.message}`);
   10. }
   ```

## 通过Deep Linking方式拉起写评论页

当应用需要跳转应用市场内对该应用进行评分与评论时，开发者可使用Deep Linking链接的方式拉起应用市场写评论页，通过拼接应用市场Deep Linking链接，在应用中调用或网页中点击Deep Linking链接在应用详情页拉起写评论页，用户可以在页面内进行评分与评论。

构造拼接bundleName和action的Deep Linking链接，其中bundleName为需要拉起写评论页的应用包名，action隐式指定为write-review，表示进入详情页后，下一步将拉起写评论页，其格式为：

```
1. uri: 'store://appgallery.huawei.com/app/detail?id=' + bundleName + '&action=write-review',
```

在应用中调用[startAbility](<../../../../harmonyos-references/Ability Kit（程序框架服务）/ArkTS API/接口依赖的元素及定义/application/UIAbilityContext/js-apis-inner-application-uiabilitycontext.md#startability-2>)方法，拉起应用市场应用的写评论页：

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. import type { common, Want } from '@kit.AbilityKit';

5. // 通过Deep Linking拉起应用市场指定的应用写评论页
6. function startAppGalleryDetailAbility(context: common.UIAbilityContext, bundleName: string): void {
7. let want: Want = {
8. action: 'ohos.want.action.appdetail', // 隐式指定action为ohos.want.action.appdetail
9. uri: 'store://appgallery.huawei.com/app/detail?id=' + bundleName + '&action=write-review'// bundleName为需要拉起写评论页的应用包名，action隐式指定为write-review，表示进入详情页后，下一步将拉起写评论页。
10. };
11. context.startAbility(want).then(() => {
12. hilog.info(0x0001, 'TAG', "Succeeded in starting Ability successfully.")
13. }).catch((error: BusinessError) => {
14. hilog.error(0x0001, 'TAG', `Failed to startAbility. Code: ${error.code}, message is ${error.message}`);
15. });
16. }

18. @Entry
19. @Component
20. struct StartAppGalleryDetailAbilityView {
21. @State message: string = '通过Deep Linking拉起应用市场写评论页'

23. build() {
24. Row() {
25. Column() {
26. Button(this.message)
27. .fontSize(24)
28. .fontWeight(FontWeight.Bold)
29. .onClick(() => {
30. const context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
31. // 按实际需求获取应用的bundleName，例如bundleName: 'com.huawei.hmsapp.books'
32. const bundleName = 'xxxx';
33. startAppGalleryDetailAbility(context, bundleName);
34. })
35. }
36. .width('100%')
37. }
38. .height('100%')
39. }
40. }
```

在网页中打开Deep Linking链接拉起应用市场应用的写评论页：

```
1. <html lang="en">
2. <head>
3. <meta charset="UTF-8">
4. </head>
5. <body>
6. <div>
7. <button type="button" onclick="openDeepLink()">通过Deep Linking拉起应用市场写评论页</button>
8. </div>
9. </body>
10. </html>
11. <script>
12. function openDeepLink() {
13. window.open('store://appgallery.huawei.com/app/detail?id=com.xxxx.xxxx&action=write-review')
14. }
15. </script>
```

## 通过App Linking方式拉起写评论页

当应用需要跳转应用市场内对该应用进行评分与评论时，开发者可使用App Linking链接的方式拉起应用市场写评论页，通过拼接应用市场App Linking链接，在应用中调用或网页中点击App Linking链接在应用详情页拉起写评论页，用户可以在页面内进行评分与评论。

构造拼接bundleName的App Linking链接，其中bundleName为需要拉起写评论页的应用包名，action隐式指定为write-review，表示进入详情页后，下一步将拉起写评论页，其格式为：

```
1. let link: string = 'https://appgallery.huawei.com/app/detail?id=' + bundleName + '&action=write-review';
```

在应用中调用[openLink](<../../../../harmonyos-references/Ability Kit（程序框架服务）/ArkTS API/接口依赖的元素及定义/application/UIAbilityContext/js-apis-inner-application-uiabilitycontext.md#openlink12>)接口拉起App Linking链接：

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. import type { common } from '@kit.AbilityKit';

5. @Entry
6. @Component
7. struct Index {
8. build() {
9. Button('start app linking', { type: ButtonType.Capsule, stateEffect: true })
10. .width('87%')
11. .height('5%')
12. .margin({ bottom: '12vp' })
13. .onClick(() => {
14. let context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
15. // 需要拼接不同的应用包名，用以打开不同的应用写评论页,例如：bundleName: 'com.huawei.hmsapp.books'
16. let bundleName: string = 'xxxx';
17. let link: string = 'https://appgallery.huawei.com/app/detail?id=' + bundleName + '&action=write-review';
18. // 以App Linking优先的方式在应用市场打开指定包名的应用写评论页
19. context.openLink(link, { appLinkingOnly: false })
20. .then(() => {
21. hilog.info(0x0001, 'TAG', 'openlink success.');
22. })
23. .catch((error: BusinessError) => {
24. hilog.error(0x0001, 'TAG', `openlink failed. Code: ${error.code}, message is ${error.message}`);
25. });
26. })
27. }
28. }
```

在网页中打开App Linking链接：

```
1. <html lang="en">
2. <head>
3. <meta charset="UTF-8">
4. <title>跳转示例</title>
5. </head>
6. <body>
7. <a href='https://appgallery.huawei.com/app/detail?id=bundleName&action=write-review'>通过AppLinking拉起应用市场写评论页</a>
8. </body>
9. </html>
```
