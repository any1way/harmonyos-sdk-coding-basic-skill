---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/reader-setting-scaled-density
title: 监听文本缩放因子变化
breadcrumb: 指南 > 应用服务 > Reader Kit（阅读服务） > 书籍内容排版 > 修改阅读设置 > 监听文本缩放因子变化
category: harmonyos-guides
scraped_at: 2026-06-11T15:13:48+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:dd9eae9965e330dda7e51b6c9f3f1a0d97a253174942137ba3873655e8896e5a
---
在[智慧多窗](../../../../../应用框架/ArkUI（方舟UI框架）/窗口管理/智慧多窗应用开发指南/智慧多窗简介/multi-window-intro.md)等场景时，文本缩放因子[Display.scaledDensity](<../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS API/屏幕管理/@ohos.display (屏幕属性)/js-apis-display.md#display>)属性会发生变化。如果文本缩放因子的值与当前值不符，开发者需要更新[ReaderSetting](<../../../../../../harmonyos-references/Reader Kit（阅读服务）/ArkTS API/readerCore（阅读核心能力）/reader-read-core.md#readersetting>)的scaledDensity属性，触发ReaderComponentController组件控制器的setPageConfig接口重新进行页面排版。

## 接口说明

监听文本缩放因子变化主要涉及1个接口，具体介绍如下表所示。

| 接口名 | 描述 |
| --- | --- |
| [setPageConfig](<../../../../../../harmonyos-references/Reader Kit（阅读服务）/ArkTS API/readerCore（阅读核心能力）/reader-read-core.md#setpageconfig>)(pageConfig: ReaderSetting): void | 设置或者修改页面排版属性。 |

## 开发准备

在监听文本缩放因子变化之前，请先确保已经'[构建阅读器](../../构建阅读器/reader-read-page.md)'。

## 开发步骤

1. 导入相关模块。

   ```
   1. import { display } from '@kit.ArkUI';
   2. import { hilog } from '@kit.PerformanceAnalysisKit';
   ```
2. 通过[display.on](<../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS API/屏幕管理/@ohos.display (屏幕属性)/js-apis-display.md#displayonaddremovechange>)接口监听文本缩放因子的变化。

   在监听接口中比对系统值与当前值是否一致，如果不一致则通过应用级变量的状态管理[AppStorage](<../../../../../应用框架/ArkUI（方舟UI框架）/UI开发 (ArkTS声明式开发范式)/学习UI范式状态管理/状态管理（V1）/管理应用拥有的状态/AppStorage：应用全局的UI状态存储/arkts-appstorage.md>)将isDensityChange值设为true，并退出阅读页。

   ```
   1. @Entry
   2. @Component
   3. struct Reader {
   4. private screenDensityCallBack: Callback<number> | null = null;

   6. aboutToAppear(): void {
   7. this.registerScreenDensityChange();
   8. hilog.info(0x0000, 'testTag',
   9. 'aboutToAppear : current scaledDensity = ' + this.readerSetting.scaledDensity + ', change scaledDensity = ' +
   10. display.getDefaultDisplaySync().scaledDensity);
   11. }

   13. /**
   14. * 注册缩放文本缩放因子变化监听
   15. */
   16. registerScreenDensityChange() {
   17. this.screenDensityCallBack = (data: number) => {
   18. let displaySync = display.getDefaultDisplaySync();
   19. let scaledDensity = displaySync.scaledDensity;
   20. if (scaledDensity !== this.readerSetting.scaledDensity) {
   21. AppStorage.setOrCreate('isDensityChange', true);
   22. this.getUIContext().getRouter().back();
   23. }
   24. }
   25. display.on('change', this.screenDensityCallBack);
   26. }

   28. aboutToDisappear(): void {
   29. display.off('change', this.screenDensityCallBack);
   30. }

   32. build() {
   33. // 需要开发者根据构建阅读器章节自行实现
   34. }
   35. }
   ```
3. 在阅读页的上级页面通过[@StorageLink](<../../../../../应用框架/ArkUI（方舟UI框架）/UI开发 (ArkTS声明式开发范式)/学习UI范式状态管理/状态管理（V1）/管理应用拥有的状态/AppStorage：应用全局的UI状态存储/arkts-appstorage.md#storagelink>)装饰器监听isDensityChange字段的变化。

   当退出阅读页时，会触发上级Index页面的onPageShow生命周期回调。若检测到isDensityChange字段值变更，将执行重新进入阅读页的方法。

   开发者可参考[阅读进度通知](../../../书籍内容交互/阅读进度通知/reader-progress.md)章节保存阅读进度，在进阅读页时将保存的进度信息传入到阅读页，在阅读页通过[startPlay](<../../../../../../harmonyos-references/Reader Kit（阅读服务）/ArkTS API/readerCore（阅读核心能力）/reader-read-core.md#startplay>)接口继续阅读。

   ```
   1. import { hilog } from '@kit.PerformanceAnalysisKit';

   3. @Entry
   4. @Component
   5. struct Index {
   6. /**
   7. * 系统字体缩放因子是否发生变化，如果变化需要重启阅读器
   8. */
   9. @StorageLink('isDensityChange') isDensityChange: boolean = false;

   11. onPageShow(): void {
   12. // 文本缩放因子变化需要重新打开书籍
   13. if (this.isDensityChange) {
   14. this.jumper();
   15. AppStorage.setOrCreate('isDensityChange', false);
   16. }
   17. }

   19. private jumper() {
   20. this.getUIContext().getRouter().pushUrl({ url: "pages/Reader" }).catch(() => {
   21. hilog.error(0x0000, 'testTag', 'pushUrl failed');
   22. });
   23. }

   25. build() {
   26. // 需要开发者根据业务需要自行实现
   27. }
   28. }
   ```
