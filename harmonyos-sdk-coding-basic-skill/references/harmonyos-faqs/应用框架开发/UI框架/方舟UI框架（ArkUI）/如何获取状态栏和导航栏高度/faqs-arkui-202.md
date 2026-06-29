---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-202
title: 如何获取状态栏和导航栏高度
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > 如何获取状态栏和导航栏高度
category: harmonyos-faqs
scraped_at: 2026-06-12T10:29:05+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:fc98f25cd2133a7477de3cfb60e0dd7da2fcc8da726121ab1e7d5cf61b367eba
---
获取系统状态栏和导航栏等规避区域。使用系统提供的 getWindowAvoidArea 获取系统规避区域。返回值中的 topRect.height 即为系统状态栏的高度，单位为 px。参考代码如下：

```
1. // MainAbility.ets
2. import { common, UIAbility } from '@kit.AbilityKit';
3. import { window } from '@kit.ArkUI';

5. /**
6. * Get the height of the system status bar and navigation bar
7. * @param context
8. * @returns
9. */
10. async function getWindowAvoidArea(context: common.UIAbilityContext): Promise<window.AvoidArea | null> {
11. try {
12. // The default area of the system includes the status bar and navigation bar
13. const mainWindow = await window.getLastWindow(context);
14. const avoidAreaType = window.AvoidAreaType.TYPE_SYSTEM;
15. const avoidArea = mainWindow.getWindowAvoidArea(avoidAreaType);
16. const avoidAreaTypeNavigationBar = window.AvoidAreaType.TYPE_NAVIGATION_INDICATOR;
17. const avoidAreaNavigationBar = mainWindow.getWindowAvoidArea(avoidAreaTypeNavigationBar);
18. const height = avoidArea.topRect.height;
19. const heightNavigationBar = avoidAreaNavigationBar.bottomRect.height;
20. return avoidArea
21. } catch (e) {
22. console.log('getWindowAvoidArea fail');
23. return null
24. }
25. }

27. export default class MainAbility extends UIAbility {
28. // do something
29. async onWindowStageCreate(windowStage: window.WindowStage) {
30. getWindowAvoidArea(this.context);
31. windowStage.loadContent('pages/index');
32. }

34. // do something
35. }
```

[EntryAbilityGetHeightAndStatus.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/entryability/EntryAbilityGetHeightAndStatus.ets#L21-L56)

**参考链接**

[getWindowAvoidArea](<../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS API/UI界面/@ohos.arkui.uiExtension (uiExtension)/js-apis-arkui-uiextension.md#getwindowavoidarea>)
