---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-common-components-progress-indicator
title: 进度条 (Progress)
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (ArkTS声明式开发范式) > 添加组件 > 进度条 (Progress)
category: harmonyos-guides
scraped_at: 2026-06-11T14:31:07+08:00
doc_updated_at: 2026-05-26
content_hash: sha256:aec766ef480b416ef1db06faf68370d9fe5d142dbf4ac40da064934451892f1c
---
Progress是进度条显示组件，显示内容通常为目标操作的当前进度。具体用法请参考[Progress](../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/信息展示/Progress/ts-basic-components-progress.md)。

## 创建进度条

Progress通过调用接口来创建，接口调用方式如下：

```
1. Progress(options: {value: number, total?: number, type?: ProgressType})
```

其中，value用于设置初始进度值，total用于设置进度总长度，type用于设置Progress样式。

```
1. Progress({ value: 24, total: 100, type: ProgressType.Linear }) // 创建一个进度总长为100，初始进度值为24的线性进度条
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bc/v3/JkQQ2AQ0SImHZAqR-rhQqw/zh-cn_image_0000002622857729.png?HW-CC-KV=V1&HW-CC-Date=20260611T063105Z&HW-CC-Expire=86400&HW-CC-Sign=BBED5A400D5D49543E50FA5E0613411485F90DD5CB12596828D6AEA1C6EECDAA)

## 设置进度条样式

Progress有5种可选类型，通过[ProgressType](../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/信息展示/Progress/ts-basic-components-progress.md#progresstype8枚举说明)可以设置进度条样式。ProgressType类型包括：ProgressType.Linear（线性样式）、 ProgressType.Ring（环形无刻度样式）、ProgressType.ScaleRing（环形有刻度样式）、ProgressType.Eclipse（圆形样式）和ProgressType.Capsule（胶囊样式）。

* 线性样式进度条（默认类型）

  说明

  从API version 9开始，组件高度大于宽度时，自适应垂直显示；组件高度等于宽度时，保持水平显示。

  ```
  1. Progress({ value: 20, total: 100, type: ProgressType.Linear }).width(200).height(50)
  2. Progress({ value: 20, total: 100, type: ProgressType.Linear }).width(50).height(200)
  ```

  [Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkUISample/InfoComponent/ProgressProject/entry/src/main/ets/pages/Index.ets#L38-L41)

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/47/v3/KYkC2OFRSBOY--BZe2cAEA/zh-cn_image_0000002622697851.png?HW-CC-KV=V1&HW-CC-Date=20260611T063105Z&HW-CC-Expire=86400&HW-CC-Sign=DE09CC185EA255232E343A66EFB99AF95FD4947CD1E671697A81FE68C7CEA469)
* 环形无刻度样式进度条

  ```
  1. // 从左往右，1号环形进度条，默认前景色为蓝色渐变，默认strokeWidth进度条宽度为2.0vp
  2. Progress({ value: 40, total: 150, type: ProgressType.Ring }).width(100).height(100)
  3. // 从左往右，2号环形进度条
  4. Progress({ value: 40, total: 150, type: ProgressType.Ring }).width(100).height(100)
  5. .color(Color.Grey)    // 进度条前景色为灰色
  6. .style({ strokeWidth: 15})    // 设置strokeWidth进度条宽度为15.0vp
  ```

  [Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkUISample/InfoComponent/ProgressProject/entry/src/main/ets/pages/Index.ets#L46-L53)

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7f/v3/ZEtB77x6Q2aY9C-TslUPGQ/zh-cn_image_0000002592218290.png?HW-CC-KV=V1&HW-CC-Date=20260611T063105Z&HW-CC-Expire=86400&HW-CC-Sign=CAC31DD1C4271D445D19B1941E06F7D1775B6AA90D9BE67693DF1812DC40C1FF)
* 环形有刻度样式进度条

  ```
  1. Progress({ value: 20, total: 150, type: ProgressType.ScaleRing }).width(100).height(100)
  2. .backgroundColor(Color.Black)
  3. .style({ scaleCount: 20, scaleWidth: 5 })    // 设置环形有刻度进度条总刻度数为20，刻度宽度为5vp
  4. Progress({ value: 20, total: 150, type: ProgressType.ScaleRing }).width(100).height(100)
  5. .backgroundColor(Color.Black)
  6. .style({ strokeWidth: 15, scaleCount: 20, scaleWidth: 5 })    // 设置环形有刻度进度条宽度15，总刻度数为20，刻度宽度为5vp
  7. Progress({ value: 20, total: 150, type: ProgressType.ScaleRing }).width(100).height(100)
  8. .backgroundColor(Color.Black)
  9. .style({ strokeWidth: 15, scaleCount: 20, scaleWidth: 3 })    // 设置环形有刻度进度条宽度15，总刻度数为20，刻度宽度为3vp
  ```

  [Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkUISample/InfoComponent/ProgressProject/entry/src/main/ets/pages/Index.ets#L59-L69)

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c2/v3/ndm3kik6QZCpmi2sHz61tQ/zh-cn_image_0000002592378224.png?HW-CC-KV=V1&HW-CC-Date=20260611T063105Z&HW-CC-Expire=86400&HW-CC-Sign=2143F73D948A165B4553F5C11F3A9371EDFA1B1E6F9997E8DDBC96F4D81FA801)
* 圆形样式进度条

  ```
  1. // 从左往右，1号圆形进度条，默认前景色为蓝色
  2. Progress({ value: 10, total: 150, type: ProgressType.Eclipse }).width(100).height(100)
  3. // 从左往右，2号圆形进度条，指定前景色为灰色
  4. Progress({ value: 20, total: 150, type: ProgressType.Eclipse }).color(Color.Grey).width(100).height(100)
  ```

  [Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkUISample/InfoComponent/ProgressProject/entry/src/main/ets/pages/Index.ets#L75-L80)

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ea/v3/BREruDJpTsqOL6i7XlMRMw/zh-cn_image_0000002622857731.png?HW-CC-KV=V1&HW-CC-Date=20260611T063105Z&HW-CC-Expire=86400&HW-CC-Sign=432A5FDD38FE6370E1005F1EF361C1623806296D3619A48E908F3E8E2CE4ECCA)
* 胶囊样式进度条

  说明

  + 头尾两端圆弧处的进度展示效果与ProgressType.Eclipse样式一致。
  + 中段处的进度展示效果为矩形状长条，与ProgressType.Linear线性样式相似。
  + 组件高度大于宽度时，自适应垂直显示。

  ```
  1. Progress({ value: 10, total: 150, type: ProgressType.Capsule }).width(100).height(50)
  2. Progress({ value: 20, total: 150, type: ProgressType.Capsule }).width(50).height(100).color(Color.Grey)
  3. Progress({ value: 50, total: 150, type: ProgressType.Capsule }).width(50).height(100).color(Color.Blue).backgroundColor(Color.Black)
  ```

  [Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkUISample/InfoComponent/ProgressProject/entry/src/main/ets/pages/Index.ets#L86-L90)

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/13/v3/ScMFq7oiRA647Z3J3v3S1Q/zh-cn_image_0000002622697853.png?HW-CC-KV=V1&HW-CC-Date=20260611T063105Z&HW-CC-Expire=86400&HW-CC-Sign=AF24D29096C511640EE405DA11FF7D0C201C25224218CF19CE0C7E50F83B7544)

## 场景示例

更新当前进度值，如应用安装进度条，可通过点击Button增加progressValue，value属性将progressValue设置给Progress组件，进度条组件即会触发刷新，更新当前进度。

```
1. @Entry
2. @Component
3. struct ProgressCase1 {
4. @State progressValue: number = 0;    // 设置进度条初始值为0
5. build() {
6. Column() {
7. Column() {
8. Progress({value:0, total:100, type:ProgressType.Capsule}).width(200).height(50).value(this.progressValue)
9. Row().width('100%').height(5)
10. // 请将$r('app.string.progress_add')替换为实际资源文件，在本示例中该资源文件的value值为"进度条+5"
11. Button($r('app.string.progress_add'))
12. .onClick(()=>{
13. this.progressValue += 5;
14. if (this.progressValue > 100){
15. this.progressValue = 0;
16. }
17. })
18. }
19. }.width('100%').height('100%')
20. }
21. }
```

[ProgressCase1.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkUISample/InfoComponent/ProgressProject/entry/src/main/ets/pages/ProgressCase1.ets#L15-L37)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bc/v3/ThAaGNE3QKuMw0sERiES0A/zh-cn_image_0000002592218292.gif?HW-CC-KV=V1&HW-CC-Date=20260611T063105Z&HW-CC-Expire=86400&HW-CC-Sign=C813911B29E39F4E12CD3BE4C6CB89926492856740C0F109DF8C734FBBA26D9C)
