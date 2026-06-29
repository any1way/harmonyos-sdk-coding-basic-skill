---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-arkui-advanced-splitlayout
title: SplitLayout
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 系统预置UI组件库 > SplitLayout
category: harmonyos-references
scraped_at: 2026-06-11T15:50:22+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:9f32a3de9df6e76299afc5dfc3591f9105bdb4b7ee611069999972c32f84d396
---
上下结构布局介绍了常用的页面布局样式。主要分为上下文本和上下图文两种类型。

说明

* 该组件从API version 10开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。
* 该组件仅可在Stage模型下使用。
* 如果SplitLayout设置[通用属性](../../通用属性/ts-component-general-attributes.md)和[通用事件](../../通用事件/ts-component-general-events.md)，编译工具链会额外生成节点\_\_Common\_\_，并将通用属性或通用事件挂载在\_\_Common\_\_上，而不是直接应用到SplitLayout本身。这可能导致开发者设置的通用属性或通用事件不生效或不符合预期，因此，不建议SplitLayout设置通用属性和通用事件。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { SplitLayout } from '@kit.ArkUI';
```

## 子组件

PhonePC/2in1TabletTVWearable

无

## SplitLayout

PhonePC/2in1TabletTVWearable

SplitLayout({mainImage: Resource, primaryText: string, secondaryText?: string, tertiaryText?: string, container: () => void })

**装饰器类型：**@Component

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

| 名称 | 类型 | 必填 | 装饰器类型 | 说明 |
| --- | --- | --- | --- | --- |
| mainImage | [ResourceStr](../../公共定义/基础类型定义/ts-types.md#resourcestr) | 是 | @State | 传入图片。 |
| primaryText | [ResourceStr](../../公共定义/基础类型定义/ts-types.md#resourcestr) | 是 | @Prop | 标题内容。 |
| secondaryText | [ResourceStr](../../公共定义/基础类型定义/ts-types.md#resourcestr) | 否 | @Prop | 副标题内容。当需要在标题下方显示副标题时传入，不传入时取默认值，不显示副标题。 |
| tertiaryText | [ResourceStr](../../公共定义/基础类型定义/ts-types.md#resourcestr) | 否 | @Prop | 辅助文本。当需要显示辅助文本时传入，不传入时取默认值，不显示辅助文本。 |
| container | () => void | 是 | @BuilderParam | 容器内组件。 |

## 事件

PhonePC/2in1TabletTVWearable

不支持[通用事件](../../通用事件/ts-component-general-events.md)。

## 示例

PhonePC/2in1TabletTVWearable

该示例通过SplitLayout实现了页面布局，并具备自适应能力。

```
1. import { SplitLayout } from '@kit.ArkUI';

3. @Entry
4. @Component
5. struct Index {
6. @State demoImage: Resource = $r("app.media.background");

8. build() {
9. Column() {
10. SplitLayout({
11. mainImage: this.demoImage,
12. primaryText: '新歌推荐',
13. secondaryText: '私人订制新歌精选站，为你推荐专属优质新歌;',
14. tertiaryText: '每日更新',
15. }) {
16. Text('示例：空白区域容器内可添加组件')
17. .margin({ top: 36 })
18. }
19. }
20. .justifyContent(FlexAlign.SpaceBetween)
21. .height('100%')
22. .width('100%')
23. }
24. }
```

小于等于600vp布局：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f9/v3/GNFQvQZHSK-LvzbFKySJWQ/zh-cn_image_0000002622700161.png?HW-CC-KV=V1&HW-CC-Date=20260611T075021Z&HW-CC-Expire=86400&HW-CC-Sign=BC3C5240C3BA313C781B72B72799A8EE714FD85ECD0F064897E27B809F27708B)

大于600vp且小于等于840vp的布局：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6c/v3/miih93RrRCyCRJZvIK-mAg/zh-cn_image_0000002592220602.png?HW-CC-KV=V1&HW-CC-Date=20260611T075021Z&HW-CC-Expire=86400&HW-CC-Sign=9CC24443D14551EA8471DBE44254573FB4750D65EC02D41776821260DC95611A)

大于840vp布局：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bd/v3/VDCl9ip0RD2UP2feLnHn9Q/zh-cn_image_0000002592380534.png?HW-CC-KV=V1&HW-CC-Date=20260611T075021Z&HW-CC-Expire=86400&HW-CC-Sign=01B7BD48E42CCC37C9625FBE6E6B3D8029C011671420C543C115B53EB6727185)
