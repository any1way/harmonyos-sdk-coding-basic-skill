---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-previewer-arkui
title: 查看ArkUI预览效果
breadcrumb: 指南 > 编写与调试应用 > 界面预览 > 查看ArkUI预览效果
category: harmonyos-guides
scraped_at: 2026-06-11T15:28:23+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:a70f800151e7f30b7380de45b0d1912764d05a45d1cf15c1670139a85b38653f
---

ArkUI预览支持页面预览、组件预览和卡片预览，下图中左侧图标![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c3/v3/pWReki0OTj6K7icAQ5jkeQ/zh-cn_image_0000002571387466.png?HW-CC-KV=V1&HW-CC-Date=20260611T072531Z&HW-CC-Expire=86400&HW-CC-Sign=04E54E411E205BA1C421B0061D56D48B8A5E5A0E3517188BDFF44451F41BD364)为页面预览，右侧图标![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ea/v3/QgXlzMR6QYK1Qd3KG8l3iA/zh-cn_image_0000002571547098.png?HW-CC-KV=V1&HW-CC-Date=20260611T072531Z&HW-CC-Expire=86400&HW-CC-Sign=FE3A997FA085807C44AF6194ABB8FADFB1C28315552C1EF25099737F134DB7D7)为组件预览，卡片预览在创建卡片文件后可直接预览。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c6/v3/Jc9EaGzZSt6GvqDdYixE6g/zh-cn_image_0000002602066579.png?HW-CC-KV=V1&HW-CC-Date=20260611T072531Z&HW-CC-Expire=86400&HW-CC-Sign=00592513B945E9206FB74163846D3FD64F30D8F99341C73F2C27FA686F2AC3F4)

## 页面预览

ArkTS应用/元服务支持页面预览。页面预览通过在工程的ets文件头部添加@Entry实现。

@Entry的使用参考如下示例：

```
1. @Entry
2. @Component
3. struct Index {
4. @State message: string = 'Hello World'

6. build() {
7. Row() {
8. Column() {
9. Text(this.message)
10. .fontSize(50)
11. .fontWeight(FontWeight.Bold)
12. }
13. .width('100%')
14. }
15. .height('100%')
16. }
17. }
```

## 组件预览

ArkTS应用/元服务支持组件预览。组件预览支持实时预览，不支持动态图和动态预览。组件预览通过在组件前添加注解@Preview实现，在单个源文件中，最多可以使用10个@Preview装饰自定义组件。

@Preview的使用参考如下示例：

```
1. @Preview({
2. title: 'ContentTable'
3. })
4. @Component
5. struct ContentTablePreview {
6. build() {
7. Flex() {
8. ContentTable({ foodItem: getDefaultFoodData() })
9. }
10. }
11. }
```

以上示例的组件预览效果如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1b/v3/aAyZIB1DT6OWsKjXzU6EmA/zh-cn_image_0000002602186635.gif?HW-CC-KV=V1&HW-CC-Date=20260611T072531Z&HW-CC-Expire=86400&HW-CC-Sign=2B4270E16BF48FC15FEC65FB7AF7967A8272109D6EB176AE8C017E82697AEDE8 "点击放大")

组件预览默认的预览设备为Phone，若您想查看不同的设备，或者不同的屏幕形状，或者不同设备语言等情况下的组件预览效果，可以通过设置@Preview的参数，指定预览设备的相关属性。若不设置@Preview的参数，默认的设备属性如下所示：

```
1. @Preview({
2. title: 'Component1',  //预览组件的名称
3. deviceType: 'phone',  //指定当前组件预览渲染的设备类型，默认为Phone
4. width: 1080,  //预览设备的宽度，单位：px
5. height: 2340,  //预览设备的长度，单位：px
6. colorMode: 'light',  //显示的亮暗模式，当前支持取值为light
7. dpi: 480,  //预览设备的屏幕DPI值
8. locale: 'zh_CN',  //预览设备的语言，如zh_CN、en_US等
9. orientation: 'portrait',  //预览设备的横竖屏状态，取值为portrait或landscape
10. roundScreen: false  //设备的屏幕形状是否为圆形
11. })
```

请注意，如果被预览的组件是依赖参数注入的组件，建议的预览方式是：定义一个组件片段，在该片段中声明将要预览的组件，以及该组件依赖的入参，并在组件片段上标注@Preview注解，以表明将预览该片段中的内容。例如，要预览如下组件：

```
1. @Component
2. struct Title {
3. @Prop context: string;
4. build() {
5. Text(this.context)
6. }
7. }
```

建议按如下方式预览：

```
1. @Preview
2. @Component    //定义组件片段TitlePreview
3. struct TitlePreview {
4. build() {
5. Title({ context: 'MyTitle' })    //在该片段中声明将要预览的组件Title，以及该组件依赖的入参 {context: 'MyTitle'}
6. }
7. }
```

## 卡片预览

创建卡片并选中卡片文件后，点击右侧边栏**Previewer**按钮即可预览卡片。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/36/v3/DPb0QvF3T2SERKnOu8hKmg/zh-cn_image_0000002602186631.png?HW-CC-KV=V1&HW-CC-Date=20260611T072531Z&HW-CC-Expire=86400&HW-CC-Sign=A5888C16D05FEAAF0249D3E60662063F54B3FF71A9F92ABC56E2801EE0512080 "点击放大")
