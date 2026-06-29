---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/servicecollaboration-richeditor-title
title: 跨设备互通（RichEditor控件）
breadcrumb: 指南 > 系统 > 网络 > Service Collaboration Kit（协同服务） > 跨设备互通（RichEditor控件）
category: harmonyos-guides
scraped_at: 2026-06-11T14:49:26+08:00
doc_updated_at: 2026-06-05
content_hash: sha256:630194070b95d26096879b08a3a0c147c993278b556a5dda35b38a9d3876b068
---
富文本控件[RichEditor](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/文本与输入/RichEditor/ts-basic-components-richeditor.md)已集成跨设备互通能力。在Tablet或PC/2in1设备上，用户可通过其右键菜单调用Phone的相机、扫描及图库（访问图片）功能。

## 场景介绍

您通过此能力实现跨设备交互，可以使用其他设备的相机、扫描和图库功能。

## 约束与限制

需同时满足以下条件，才能使用该功能：

* **设备限制**

  + 本端设备：HarmonyOS版本为HarmonyOS 5及以上的Tablet或PC/2in1设备。
  + 远端设备：HarmonyOS版本为HarmonyOS 5及以上、具有相机能力的Phone或Tablet设备。
* **使用限制**

  + 双端设备需要登录同一华为账号。
  + 跨设备互通API支持根据特定调用策略调用设备。调用策略：PC/2in1设备可以调用Tablet和Phone，Tablet可以调用Phone，同类型设备不可调用。
  + 双端设备需要打开WLAN和蓝牙开关。条件允许时，建议双端设备接入同一个局域网，可提升唤醒相机的速度。

## 开发步骤

添加[RichEditor](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/文本与输入/RichEditor/ts-basic-components-richeditor.md)富文本组件，即可在富文本组件中右键中选择其他设备进行导入，通过onWillChange属性对回传的照片进行处理。

```
1. @Entry
2. @Component
3. struct Index {
4. controller: RichEditorController = new RichEditorController();
5. options: RichEditorOptions = { controller: this.controller };

7. build() {
8. Column() {
9. Column() {
10. RichEditor(this.options)
11. .onWillChange((value: RichEditorChangeValue) => {
12. if (value?.replacedImageSpans[0]?.imageStyle?.objectFit != 0) {
13. return true;
14. }
15. for (let item of value.replacedImageSpans) {
16. this.controller.addImageSpan(item.valuePixelMap, {
17. imageStyle: {
18. size: ['500px', '500px'],
19. layoutStyle: {
20. borderRadius: '10px'
21. }
22. }
23. });
24. }
25. return false;
26. })
27. .borderWidth(1)
28. .borderColor(Color.Green)
29. .width('100%')
30. .height('100%')
31. }
32. .borderWidth(1)
33. .borderColor(Color.Red)
34. .width('100%')
35. .height('70%')
36. }
37. }
38. }
```

富文本组件使用流程如下：

1.在富文本区域右键。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b2/v3/_FXlABhnTQ2v2OGEQPafWg/zh-cn_image_0000002592378800.png?HW-CC-KV=V1&HW-CC-Date=20260611T064925Z&HW-CC-Expire=86400&HW-CC-Sign=5D191230E0AC9C27D12E4BDBBE6E56CEC79DCB3B4CAAAE2443DA6A6D0222D91E)

2.选择想要使用的能力。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/32/v3/956NplvmST2zC9gsoXJ5uA/zh-cn_image_0000002622858307.png?HW-CC-KV=V1&HW-CC-Date=20260611T064925Z&HW-CC-Expire=86400&HW-CC-Sign=B74A6C80E83905D5BC1F83BC3486924E26B3B80F0DE8DC915BEBE203059E6AB6)

3.等待对端设备拍照回传。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f2/v3/owGTOFQPTgSHRnZ20CV81g/zh-cn_image_0000002622698429.png?HW-CC-KV=V1&HW-CC-Date=20260611T064925Z&HW-CC-Expire=86400&HW-CC-Sign=45F3A42FC39024DC8451AE7063C23966952E4D28CCA9BA1736B7C294B4B3A608)

4.图片回传后，在光标后面已嵌入一张图片。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/28/v3/tNvnzVl6RJeuhM4VFlFgMg/zh-cn_image_0000002592218868.png?HW-CC-KV=V1&HW-CC-Date=20260611T064925Z&HW-CC-Expire=86400&HW-CC-Sign=E1BC2ED6B0F3930DC55155FF16EF2FBBBA0D8666C94B831D85C25FA06F9917E1)

## 关闭富文本跨设备互通能力

如果需要关闭富文本右键菜单跨设备互通能力，可通过editMenuOptions属性自定义菜单内容去除跨设备互通菜单项，示例如下：

```
1. @Entry
2. @Component
3. struct Index {
4. controller: RichEditorController = new RichEditorController();
5. options: RichEditorOptions = { controller: this.controller };

7. build() {
8. Column() {
9. Column() {
10. RichEditor(this.options)
11. .editMenuOptions({
12. onCreateMenu: (menuItems: Array<TextMenuItem>) => {
13. if (menuItems.length === 0) {
14. return menuItems;
15. }
16. let newMenuItems: TextMenuItem[] = [];
17. menuItems.forEach((item, index) => {
18. if (!item.id.equals(TextMenuItemId.COLLABORATION_SERVICE)) {
19. newMenuItems.push(item);
20. }
21. });
22. return newMenuItems;
23. },
24. onMenuItemClick: (menuItem: TextMenuItem, textRange: TextRange) => {
25. return false;
26. }
27. })
28. .borderWidth(1)
29. .borderColor(Color.Green)
30. .width('100%')
31. .height('100%')
32. }
33. .borderWidth(1)
34. .borderColor(Color.Red)
35. .width('100%')
36. .height('70%')
37. }
38. }
39. }
```
