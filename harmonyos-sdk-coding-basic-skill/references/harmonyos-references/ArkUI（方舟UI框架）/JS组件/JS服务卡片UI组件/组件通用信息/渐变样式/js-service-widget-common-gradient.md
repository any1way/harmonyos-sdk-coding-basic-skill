---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-service-widget-common-gradient
title: 渐变样式
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > JS组件 > JS服务卡片UI组件 > 组件通用信息 > 渐变样式
category: harmonyos-references
scraped_at: 2026-06-11T15:53:32+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:87dc93510e7d972c10ead99d33967fc25430140658c30c916d878317ce9aed67
---

组件普遍支持在style或css中设置渐变样式，可以平稳过渡两个或多个指定的颜色。

说明

从API version 8开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

开发框架支持线性渐变 (linear-gradient)和重复线性渐变 (repeating-linear-gradient)两种渐变效果。

## 线性渐变/重复线性渐变

PhonePC/2in1TabletTVWearable

使用渐变样式，需要定义过渡方向和过渡颜色。

### 过渡方向

PhonePC/2in1TabletTVWearable

通过direction或者angle指定过渡方向。

* direction：进行方向渐变。
* angle：进行角度渐变。

```
1. background: linear-gradient(direction/angle, color, color, ...);
2. background: repeating-linear-gradient(direction/angle, color, color, ...);
```

### 过渡颜色

PhonePC/2in1TabletTVWearable

支持以下四种方式：#ff0000、#ffff0000、rgb(255, 0, 0)、rgba(255, 0, 0, 1)，需要指定至少两种颜色。

**参数：**

| 名称 | 类型 | 默认值 | 必填 | 描述 |
| --- | --- | --- | --- | --- |
| direction | to <side-or-corner> <side-or-corner> = [left | right] || [top | bottom] | to bottom (由上到下渐变) | 否 | 指定过渡方向，如：to left (从右向左渐变) ，或者to bottom right (从左上角到右下角)。 |
| angle | <deg> | 180deg | 否 | 指定过渡方向，以元素几何中心为坐标原点，水平方向为X轴，angle指定了渐变线与Y轴的夹角(顺时针方向)。 |
| color | <color> [<length>|<percentage>] | - | 是 | 定义使用渐变样式区域内颜色的渐变效果。 |

**示例：**

1. 默认渐变方向为从上向下渐变。

   ```
   1. #gradient {
   2. height: 300px;
   3. width: 600px;
   4. /* 从顶部开始向底部由红色向绿色渐变 */
   5. background: linear-gradient(red, #00ff00);
   6. }
   ```

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f6/v3/Bp0u-epSSNGKL1WAa0bI-Q/zh-cn_image_0000002592380826.png?HW-CC-KV=V1&HW-CC-Date=20260611T075331Z&HW-CC-Expire=86400&HW-CC-Sign=0E231C3D37F80EBB78D4C8D557E2AB4D6FBE5F6CE575866589AE9AAABF12EB04)
2. 45度夹角渐变。

   ```
   1. /* 45度夹角，从红色渐变到绿色 */
   2. background: linear-gradient(45deg, rgb(255, 0, 0),rgb(0, 255, 0));
   ```

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/83/v3/vNbp-tgRS9-G5Xl5wJpgLA/zh-cn_image_0000002622860337.png?HW-CC-KV=V1&HW-CC-Date=20260611T075331Z&HW-CC-Expire=86400&HW-CC-Sign=2643130D19C5481A4D6F6FE7A75A4C3C1E599A4485F6DE86E6968C850AA38999)
3. 设置方向从左向右渐变。

   ```
   1. /* 从左向右渐变，在距离左边90px和距离左边360px (600*0.6) 之间270px宽度形成渐变 */
   2. background: linear-gradient(to right, rgb(255, 0, 0) 90px, rgb(0, 255, 0) 60%);
   ```

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/69/v3/FNkPROX0Q4OYaCWUpyXsKA/zh-cn_image_0000002622700455.png?HW-CC-KV=V1&HW-CC-Date=20260611T075331Z&HW-CC-Expire=86400&HW-CC-Sign=D36BE7746806B840C411F282EBAFC6C577F17DA17AE7E50070B4BB2BF16172B1)
4. 重复渐变。

   ```
   1. /* 从左向右重复渐变，重复渐变区域30px（60-30）透明度0.5 */
   2. background: repeating-linear-gradient(to right, rgba(255, 255, 0, 1) 30vp,rgba(0, 0, 255, .5) 60vp);
   ```

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3b/v3/BjmkLAsoQX-nWoMnanS86g/zh-cn_image_0000002592220896.png?HW-CC-KV=V1&HW-CC-Date=20260611T075331Z&HW-CC-Expire=86400&HW-CC-Sign=C7EC06F00A361BF200D6BB3C8E9B46A47CAC164839E0589DC1F13A2548E2BD26)
