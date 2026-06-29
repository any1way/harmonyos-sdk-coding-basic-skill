---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-prompt
title: @ohos.prompt (弹窗)
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS API > 已停止维护的接口 > @ohos.prompt (弹窗)
category: harmonyos-references
scraped_at: 2026-06-11T15:43:30+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:e6ade6ed77ed02d29ecff2b8346ae90b0fc25b93cf9fa571556564472a89db2f
---
创建并显示文本提示框、对话框和操作菜单。

说明

从API version 9 开始，该接口不再维护，推荐使用新接口[@ohos.promptAction (弹窗)](<../../UI界面/@ohos.promptAction (弹窗)/js-apis-promptaction.md>)。

本模块首批接口从API version 8开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import prompt from '@ohos.prompt'
```

## prompt.showToast

PhonePC/2in1TabletTVWearable

showToast(options: ShowToastOptions): void

创建并显示文本提示框。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [ShowToastOptions](js-apis-prompt.md#showtoastoptions) | 是 | 文本弹窗选项。 |

**示例：**

```
1. import prompt from '@ohos.prompt'
2. prompt.showToast({
3. message: 'Message Info',
4. duration: 2000
5. });
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/09/v3/0mKwcxO8RUapT7XAyxGJ_A/zh-cn_image_0000002622859367.gif?HW-CC-KV=V1&HW-CC-Date=20260611T074328Z&HW-CC-Expire=86400&HW-CC-Sign=0942FAD32618F1270471476F9E3B3543779E23572B79CD8C5F46246DFF137A0C)

## ShowToastOptions

PhonePC/2in1TabletTVWearable

文本提示框的选项。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full。

| 名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| message | string | 是 | 显示的文本信息。 |
| duration | number | 否 | 默认值1500ms，取值区间：1500ms-10000ms。若小于1500ms则取默认值，若大于10000ms则取上限值10000ms。 |
| bottom | string| number | 否 | 设置弹窗边框距离屏幕底部的位置，无上限值，默认单位vp。 |

## prompt.showDialog

PhonePC/2in1TabletTVWearable

showDialog(options: ShowDialogOptions): Promise<ShowDialogSuccessResponse>

创建并显示对话框，对话框响应后同步返回结果。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [ShowDialogOptions](js-apis-prompt.md#showdialogoptions) | 是 | 对话框选项。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[ShowDialogSuccessResponse](js-apis-prompt.md#showdialogsuccessresponse)> | 对话框响应结果。 |

**示例：**

```
1. import prompt from '@ohos.prompt'
2. prompt.showDialog({
3. title: 'Title Info',
4. message: 'Message Info',
5. buttons: [
6. {
7. text: 'button1',
8. color: '#000000'
9. },
10. {
11. text: 'button2',
12. color: '#000000'
13. }
14. ],
15. })
16. .then(data => {
17. console.info('showDialog success, click button: ' + data.index);
18. })
19. .catch((err:Error) => {
20. console.info('showDialog error: ' + err);
21. })
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/98/v3/DkQPqfBNSC2ixJop8lXHnA/zh-cn_image_0000002622859331.gif?HW-CC-KV=V1&HW-CC-Date=20260611T074328Z&HW-CC-Expire=86400&HW-CC-Sign=8116971969B381E3138B2FA393F3FD8265109FCAF2D1C852A6D315030E5897AF)

## prompt.showDialog

PhonePC/2in1TabletTVWearable

showDialog(options: ShowDialogOptions, callback: AsyncCallback<ShowDialogSuccessResponse>):void

创建并显示对话框，对话框响应结果异步返回。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [ShowDialogOptions](js-apis-prompt.md#showdialogoptions) | 是 | 页面显示对话框信息描述。 |
| callback | AsyncCallback<[ShowDialogSuccessResponse](js-apis-prompt.md#showdialogsuccessresponse)> | 是 | 对话框响应结果回调。 |

**示例：**

```
1. import prompt from '@ohos.prompt'
2. prompt.showDialog({
3. title: 'showDialog Title Info',
4. message: 'Message Info',
5. buttons: [
6. {
7. text: 'button1',
8. color: '#000000'
9. },
10. {
11. text: 'button2',
12. color: '#000000'
13. }
14. ]
15. }, (err, data) => {
16. if (err) {
17. console.info('showDialog err: ' + err);
18. return;
19. }
20. console.info('showDialog success callback, click button: ' + data.index);
21. });
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ee/v3/CRn-Kpc1Sa-dI6Ln0hk3HA/zh-cn_image_0000002622699451.gif?HW-CC-KV=V1&HW-CC-Date=20260611T074328Z&HW-CC-Expire=86400&HW-CC-Sign=0CBEBBA628F066D069B0137CFB8A84F1E552816E3CC11947AED802C8D0CD7969)

## ShowDialogOptions

PhonePC/2in1TabletTVWearable

对话框的选项。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| title | string | 否 | 标题文本。 |
| message | string | 否 | 内容文本。 |
| buttons | [[Button](js-apis-prompt.md#button),[Button](js-apis-prompt.md#button)?,[Button](js-apis-prompt.md#button)?] | 否 | 对话框中按钮的数组，结构为：{text:'button', color: '#666666'}，支持1-3个按钮。其中第一个为positiveButton，第二个为negativeButton，第三个为neutralButton。 |

## ShowDialogSuccessResponse

PhonePC/2in1TabletTVWearable

对话框的响应结果。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | number | 是 | 选中按钮在buttons数组中的索引。 |

## prompt.showActionMenu

PhonePC/2in1TabletTVWearable

showActionMenu(options: ActionMenuOptions, callback: AsyncCallback<ActionMenuSuccessResponse>):void

创建并显示操作菜单，菜单响应结果异步返回。

**系统能力：** 以下各项对应的系统能力均为SystemCapability.ArkUI.ArkUI.Full。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [ActionMenuOptions](js-apis-prompt.md#actionmenuoptions) | 是 | 操作菜单选项。 |
| callback | AsyncCallback<[ActionMenuSuccessResponse](js-apis-prompt.md#actionmenusuccessresponse)> | 是 | 菜单响应结果回调。 |

**示例：**

```
1. import prompt from '@ohos.prompt'
2. prompt.showActionMenu({
3. title: 'Title Info',
4. buttons: [
5. {
6. text: 'item1',
7. color: '#666666'
8. },
9. {
10. text: 'item2',
11. color: '#000000'
12. },
13. ]
14. }, (err, data) => {
15. if (err) {
16. console.info('showActionMenu err: ' + err);
17. return;
18. }
19. console.info('showActionMenu success callback, click button: ' + data.index);
20. })
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/10/v3/vu9wSSTIQruLiK4bwWzbSA/zh-cn_image_0000002622859333.gif?HW-CC-KV=V1&HW-CC-Date=20260611T074328Z&HW-CC-Expire=86400&HW-CC-Sign=C9A4C61A8E95A1F3F1C96291AEBA673FA5816B32E12D8612A182CC7C3D765083)

## prompt.showActionMenu

PhonePC/2in1TabletTVWearable

showActionMenu(options: ActionMenuOptions): Promise<ActionMenuSuccessResponse>

创建并显示操作菜单，菜单响应后同步返回结果。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [ActionMenuOptions](js-apis-prompt.md#actionmenuoptions) | 是 | 操作菜单选项。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[ActionMenuSuccessResponse](js-apis-prompt.md#actionmenusuccessresponse)> | 菜单响应结果。 |

**示例：**

```
1. import prompt from '@ohos.prompt'
2. prompt.showActionMenu({
3. title: 'showActionMenu Title Info',
4. buttons: [
5. {
6. text: 'item1',
7. color: '#666666'
8. },
9. {
10. text: 'item2',
11. color: '#000000'
12. },
13. ]
14. })
15. .then(data => {
16. console.info('showActionMenu success, click button: ' + data.index);
17. })
18. .catch((err:Error) => {
19. console.info('showActionMenu error: ' + err);
20. })
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a3/v3/O_LNTRN2TFGMWDW19epI6A/zh-cn_image_0000002592219892.gif?HW-CC-KV=V1&HW-CC-Date=20260611T074328Z&HW-CC-Expire=86400&HW-CC-Sign=49524C83CACEF9C1CBAF506CD26D4F0FDEF9A440E785E74A5D93D2C4B6A827F0)

## ActionMenuOptions

PhonePC/2in1TabletTVWearable

操作菜单的选项。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full。

| 名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| title | string | 否 | 标题文本。 |
| buttons | [[Button](js-apis-prompt.md#button),[Button](js-apis-prompt.md#button)?,[Button](js-apis-prompt.md#button)?,[Button](js-apis-prompt.md#button)?,[Button](js-apis-prompt.md#button)?,[Button](js-apis-prompt.md#button)?] | 是 | 菜单中菜单项按钮的数组，结构为：{text:'button', color: '#666666'}，支持1-6个按钮。大于6个按钮时弹窗不显示。 |

## ActionMenuSuccessResponse

PhonePC/2in1TabletTVWearable

操作菜单的响应结果。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | number | 是 | 选中按钮在buttons数组中的索引，从0开始。 |

## Button

PhonePC/2in1TabletTVWearable

菜单中的菜单项按钮。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| text | string | 是 | 按钮文本内容。 |
| color | string | 是 | 按钮文本颜色。 |
