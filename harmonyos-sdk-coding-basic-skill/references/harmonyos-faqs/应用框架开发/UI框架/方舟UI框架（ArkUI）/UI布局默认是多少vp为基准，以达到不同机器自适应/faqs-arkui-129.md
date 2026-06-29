---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-129
title: UI布局默认是多少vp为基准，以达到不同机器自适应
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > UI布局默认是多少vp为基准，以达到不同机器自适应
category: harmonyos-faqs
scraped_at: 2026-06-12T10:27:54+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:7ad478bb2b9f6d4bc7096c66ddeb6d8989b3dfcb35470dce1098600f916c00e5
---
无论屏幕分辨率或密度如何，组件的视觉效果保持一致。

vp具体计算公式为：vp= px/(DPI/160)

px 是屏幕的真实物理像素值，densityDPI 通常指系统屏幕密度，densityPixels是屏幕密度与标准DPI的比率，常见取值有 0.75、1.0、1.5、2.0、3.0 等。在HarmonyOS中，标准DPI为160。以华为Mate 40 Pro为例，densityDPI为 560，densityPixels为3.5。要查看真机的DPI，可以调用屏幕属性中的display接口查询。

```
1. import { display } from '@kit.ArkUI';

3. let displayClass: display.Display | null = null;
4. try {
5. displayClass = display.getDefaultDisplaySync();
6. } catch (exception) {
7. console.error('Failed to obtain the default display object. Code: ' + JSON.stringify(exception));
8. }
```

[AdaptiveForDifferentmMachines.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/AdaptiveForDifferentmMachines.ets#L22-L29)

如果原型图没有提供vp单位的布局，开发者可以根据densityPixels把px转为vp，HarmonyOS也封装了现成的接口[px2vp()](<../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS API/UI界面/@ohos.arkui.UIContext (UIContext)/Class (UIContext)/arkts-apis-uicontext-uicontext.md#px2vp12>)和[vp2px()](<../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS API/UI界面/@ohos.arkui.UIContext (UIContext)/Class (UIContext)/arkts-apis-uicontext-uicontext.md#vp2px12>)供开发者直接调用。

**参考链接**

[像素单位](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/公共定义/像素单位/ts-pixel-units.md)，[@ohos.display (屏幕属性)](<../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS API/屏幕管理/@ohos.display (屏幕属性)/js-apis-display.md>)
