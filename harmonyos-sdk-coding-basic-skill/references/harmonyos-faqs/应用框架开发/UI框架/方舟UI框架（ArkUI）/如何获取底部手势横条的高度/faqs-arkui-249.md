---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-249
title: 如何获取底部手势横条的高度
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > 如何获取底部手势横条的高度
category: harmonyos-faqs
scraped_at: 2026-06-12T10:29:54+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:585c8c358febdfa2a05294c9a7ef1060d451b75d21c98b63d913355c1cb0bf75
---
可以使用window的[getWindowAvoidArea()](<../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS API/UI界面/@ohos.arkui.uiExtension (uiExtension)/js-apis-arkui-uiextension.md#getwindowavoidarea>)方法获取内容规避区域，需设置type为AvoidAreaType.TYPE\_NAVIGATION\_INDICATOR。

```
1. import { window } from '@kit.ArkUI';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. @Entry
5. @Component
6. struct GetBottomNavBarHeight {
7. context = this.getUIContext();

9. build() {
10. Column() {
11. Button('Get the height of the bottom gesture bar')
12. .onClick(() => {
13. let type = window.AvoidAreaType.TYPE_NAVIGATION_INDICATOR;
14. window.getLastWindow(this.context.getHostContext()).then((data) => {
15. let avoidArea = data.getWindowAvoidArea(type);
16. // Get the height of the navigation bar area
17. let bottomRectHeight = avoidArea.bottomRect.height;
18. console.info(`window bottomRectHeight is: ${bottomRectHeight}`);
19. }).catch((err: BusinessError) => {
20. console.error(`Failed to obtain the window. Cause: ${JSON.stringify(err)}`);
21. });
22. })
23. }
24. }
25. }
```

[BottomNavBarHeight.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/BottomNavBarHeight.ets#L21-L46)
