---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-cursorcontroller
title: Class (CursorController)
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS API > UI界面 > @ohos.arkui.UIContext (UIContext) > Class (CursorController)
category: harmonyos-references
scraped_at: 2026-06-11T15:41:50+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:e505587627399871998ea92dde0ca1ba2f4d5deefabf9f41b6b45d20ad7b7c2a
---
提供光标样式设置的能力。

说明

* 本模块首批接口从API version 10开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
* 本Class首批接口从API version 12开始支持。
* 以下API需先使用UIContext中的[getCursorController()](<../Class (UIContext)/arkts-apis-uicontext-uicontext.md#getcursorcontroller12>)方法获取CursorController实例，再通过此实例调用对应方法。

## restoreDefault12+

PhonePC/2in1TabletTVWearable

restoreDefault(): void

恢复默认的光标样式。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**示例：**

当光标移出绿框时，通过CursorController的restoreDefault方法恢复默认光标样式。

```
1. import { pointer } from '@kit.InputKit';
2. import { UIContext, CursorController } from '@kit.ArkUI';

4. @Entry
5. @Component
6. struct CursorControlExample {
7. @State text: string = '';
8. cursorCustom: CursorController = this.getUIContext().getCursorController();

10. build() {
11. Column() {
12. Row().height(200).width(200).backgroundColor(Color.Green).position({x: 150 ,y:70})
13. .onHover((flag) => {
14. if (flag) {
15. this.cursorCustom.setCursor(pointer.PointerStyle.EAST);
16. } else {
17. console.info("restoreDefault");
18. this.cursorCustom.restoreDefault();
19. }
20. })
21. }.width('100%')
22. }
23. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/78/v3/KeVPts99QACQCrUfNiiJvA/zh-cn_image_0000002592219870.gif?HW-CC-KV=V1&HW-CC-Date=20260611T074149Z&HW-CC-Expire=86400&HW-CC-Sign=7889E975169FACFD95A65FF91338A6D411512B3CFFC9FC28EBD952F5142891D6)

## setCursor12+

PhonePC/2in1TabletTVWearable

setCursor(value: PointerStyle): void

更改当前的鼠标光标样式。

说明

该接口调用后不会立即生效，而是在下一帧改变鼠标光标样式。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [PointerStyle](../Types/arkts-apis-uicontext-t.md#pointerstyle12) | 是 | 光标样式。 |

**示例：**

当光标进入蓝框时，通过CursorController的setCursor方法修改光标样式为PointerStyle.WEST。

```
1. import { pointer } from '@kit.InputKit';
2. import { UIContext, CursorController } from '@kit.ArkUI';

4. @Entry
5. @Component
6. struct CursorControlExample {
7. @State text: string = '';
8. cursorCustom: CursorController = this.getUIContext().getCursorController();

10. build() {
11. Column() {
12. Row().height(200).width(200).backgroundColor(Color.Blue).position({x: 100 ,y:70})
13. .onHover((flag) => {
14. if (flag) {
15. this.cursorCustom.setCursor(pointer.PointerStyle.WEST);
16. } else {
17. this.cursorCustom.restoreDefault();
18. }
19. })
20. }.width('100%')
21. }
22. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6b/v3/HihowdT7TnS5C1Zwx0THAA/zh-cn_image_0000002592379804.gif?HW-CC-KV=V1&HW-CC-Date=20260611T074149Z&HW-CC-Expire=86400&HW-CC-Sign=16D52AC2D20E74A3C5F6E5C0BD6E6A3579D8FD789492D9115C00F2F951685986)
