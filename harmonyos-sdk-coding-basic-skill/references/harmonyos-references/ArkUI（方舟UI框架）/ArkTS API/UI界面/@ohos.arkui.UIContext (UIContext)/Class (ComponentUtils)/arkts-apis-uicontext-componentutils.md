---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-componentutils
title: Class (ComponentUtils)
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS API > UI界面 > @ohos.arkui.UIContext (UIContext) > Class (ComponentUtils)
category: harmonyos-references
scraped_at: 2026-06-01T15:36:56+08:00
doc_updated_at: 2026-05-12
content_hash: sha256:24e29de4f190b53625e8675a841fa5b05c66aabff451a0bf9e16d8f6599c86c8
---
提供获取组件绘制区域坐标和大小的能力。

说明

* 本模块首批接口从API version 10开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
* 本Class首批接口从API version 10开始支持。
* 以下API需先使用UIContext中的[getComponentUtils()](<../Class (UIContext)/arkts-apis-uicontext-uicontext.md#getcomponentutils>)方法获取到ComponentUtils对象，再通过该对象调用对应方法。

## getRectangleById

PhonePC/2in1TabletTVWearable

getRectangleById(id: string): componentUtils.ComponentInfo

获取组件大小、位置、平移、缩放、旋转及仿射矩阵属性信息。

说明

该接口需要在目标组件布局完成以后获取目标组件区域大小信息，建议在[布局回调](<../../@ohos.arkui.inspector (布局回调)/js-apis-arkui-inspector.md>)中使用该接口。如果组件动态创建但未挂载组件树，则无法通过该接口获取正常的组件信息。因为组件在未挂载组件树的情况下，一般未经过UI框架正常的测量与布局，此时请确保组件正常挂载组件树后再尝试获取组件信息。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| id | string | 是 | 组件唯一标识id。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [componentUtils.ComponentInfo](<../../@ohos.arkui.componentUtils (componentUtils)/js-apis-arkui-componentutils.md#componentinfo>) | 组件大小、位置、平移缩放旋转及仿射矩阵属性信息。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../../../../通用错误码/errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 100001 | UI execution context not found. |

**示例：**

```
1. import { ComponentUtils } from '@kit.ArkUI';

3. @Entry
4. @Component
5. struct Index {
6. @State message: string = 'Hello World';

8. build() {
9. RelativeContainer() {
10. Text(this.message)
11. .id('HelloWorld')
12. .fontSize($r('app.float.page_text_font_size'))
13. .fontWeight(FontWeight.Bold)
14. .alignRules({
15. center: { anchor: '__container__', align: VerticalAlign.Center },
16. middle: { anchor: '__container__', align: HorizontalAlign.Center }
17. })
18. .onClick(() => {
19. this.message = 'Welcome';
20. let componentUtils: ComponentUtils = this.getUIContext().getComponentUtils();
21. let modePosition = componentUtils.getRectangleById("HelloWorld");
22. let width = modePosition.size.width; // 获取组件的宽度
23. let height = modePosition.size.height; // 获取组件的高度
24. let localOffsetX = modePosition.localOffset.x; // 获取组件相对于父组件的x轴偏移
25. let localOffsetY = modePosition.localOffset.y; // 获取组件相对于父组件的y轴偏移
26. console.info(`width: ${width}, height: ${height}, localOffsetX: ${localOffsetX}, localOffsetY: ${localOffsetY}`);
27. })
28. }
29. .height('100%')
30. .width('100%')
31. }
32. }
```
