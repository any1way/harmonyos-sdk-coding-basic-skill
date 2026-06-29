---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-200
title: 如何获取窗口的宽度
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > 如何获取窗口的宽度
category: harmonyos-faqs
scraped_at: 2026-06-12T10:29:02+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:f0300fce6481e520ea2aa233201673052fd250bfee68d8aa5406b30638666990
---
可以通过getWindowProperties接口获取窗口属性。窗口属性的windowRect表示窗口尺寸。参考代码如下：

```
1. import { window } from '@kit.ArkUI';

3. @Entry
4. @Component
5. struct WindowProperties {
6. context = this.getUIContext();

8. build() {
9. Text("Scroll Area")
10. .width("100%")
11. .height("100%")
12. .backgroundColor(0X330000FF)
13. .fontSize(16)
14. .textAlign(TextAlign.Center)
15. .onClick(() => {
16. window.getLastWindow(this.context.getHostContext()).then((data) => {
17. // get window attribute
18. let properties = data?.getWindowProperties();
19. // Get window width and height
20. console.log("windowClass width: " + properties.windowRect.width);
21. console.log("windowClass height: " + properties.windowRect.height);
22. });
23. })
24. }
25. }
```

[WindowProperties.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/WindowProperties.ets#L21-L45)

**参考链接**

[WindowRect](<../../../../../harmonyos-references/Ability Kit（程序框架服务）/ArkTS API/通用能力的接口(推荐)/@ohos.app.ability.dialogRequest (dialogRequest模块)/js-apis-app-ability-dialogrequest.md#windowrect10>)
