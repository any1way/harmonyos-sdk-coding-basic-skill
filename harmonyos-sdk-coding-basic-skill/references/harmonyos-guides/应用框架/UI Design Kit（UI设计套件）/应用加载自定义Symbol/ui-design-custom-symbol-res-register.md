---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ui-design-custom-symbol-res-register
title: 应用加载自定义Symbol
breadcrumb: 指南 > 应用框架 > UI Design Kit（UI设计套件） > 应用加载自定义Symbol
category: harmonyos-guides
scraped_at: 2026-06-11T14:39:36+08:00
doc_updated_at: 2026-05-07
content_hash: sha256:2a3da7e105b2406e5173b4d7908e4c134c26520c0e6705128de4bc51ed5c2ea7
---
## 场景介绍

从5.1.1 (19)版本开始，新增支持资源注册。

适用于需要快速定制应用内[Symbol图标](<../../../../harmonyos-references/UI Design Kit（UI设计套件）/ArkTS API/symbolRegister/ui-design-symbolregister.md>)，不想强依赖于系统版本中预制的系统Symbol图标资源。

## 约束条件

资源注册支持Phone、Tablet、PC/2in1设备。

## 开发步骤

1. 将UX设计师提供的Symbol图标资源（TTF文件）与动效参数资源（JSON文件）放入entry/src/main/resources/rawfile下，可新建目录。

   说明：[Symbol资源制作流程参考](https://developer.huawei.com/consumer/cn/doc/design-guides/system-icons-0000001929854962)

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/76/v3/sXd-9MRoRSWfc2ZFXNfRGQ/zh-cn_image_0000002622698331.png?HW-CC-KV=V1&HW-CC-Date=20260611T063935Z&HW-CC-Expire=86400&HW-CC-Sign=EA4F67C0597D783B59815A91E9B878C242FCCAD928557382D59E93850E14348B)
2. 多语言场景，在entry/src/main/resources目录中对应语言目录下的string.json文件中配置对应的Symbol图标Unicode值。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3d/v3/YFNG9q8YSyirAlEn7wmjcA/zh-cn_image_0000002592218770.png?HW-CC-KV=V1&HW-CC-Date=20260611T063935Z&HW-CC-Expire=86400&HW-CC-Sign=3335464968BA76E5246B7E706375811D22BEE82113A931757FA2DAAC1C0BA4C3)

   ```
   1. {
   2. "string": [
   3. {
   4. "name": "symbol_custom_phone_fill_1",
   5. "value": "0x100016"
   6. }
   7. ]
   8. }
   ```
3. 导入相关模块。

   ```
   1. import { symbolRegister } from '@kit.UIDesignKit';
   2. import { BusinessError } from '@kit.BasicServicesKit';
   ```
4. 在通过SymbolGlyph/SymbolSpan组件展示自定义Symbol图标前，需要注册加载图标资源与动效参数资源。

   ```
   1. try {
   2. let result = symbolRegister.registerSymbol($rawfile("symbol/symbol_register.ttf"), $rawfile("symbol/symbol_register.json"));
   3. } catch (error) {
   4. let err = error as BusinessError;
   5. console.error("errCode: " + err.code)
   6. console.error("error: " + err.message);
   7. }
   ```
5. 在需要展示自定义Symbol图标的页面通过SymbolGlyph/SymbolSpan组件展示该图标。

   ```
   1. struct test {
   2. build() {
   3. Column(){
   4. SymbolGlyph($r('app.string.symbol_custom_phone_fill_1'))
   5. }
   6. }
   7. }
   ```

## 开发实例

```
1. import { symbolRegister } from '@kit.UIDesignKit'
2. import { BusinessError } from '@kit.BasicServicesKit'

4. @Entry
5. @Component
6. struct test {
7. aboutToAppear(): void {
8. try {
9. let result = symbolRegister.registerSymbol($rawfile("symbol/symbol_register.ttf"), $rawfile("symbol/symbol_register.json"));
10. } catch (error) {
11. let err = error as BusinessError;
12. console.error("errCode: " + err.code)
13. console.error("error: " + err.message);
14. }
15. }
16. build() {
17. Column(){
18. SymbolGlyph($r('app.string.symbol_custom_phone_fill_1'))
19. }
20. }
21. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a6/v3/4by7uFdCTF-5QAYzWUYUBg/zh-cn_image_0000002592378704.png?HW-CC-KV=V1&HW-CC-Date=20260611T063935Z&HW-CC-Expire=86400&HW-CC-Sign=B1E7E0E0C9569CBB50F766B229BBB8D17E1C669FFC8BD28AFAC396F5CBEEC8F9)
