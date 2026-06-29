---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/movingphotoview-guidelines
title: 使用MovingPhotoView播放动态照片
breadcrumb: 指南 > 媒体 > Media Library Kit（媒体文件管理服务） > 动态照片 > 使用MovingPhotoView播放动态照片
category: harmonyos-guides
scraped_at: 2026-06-11T14:58:21+08:00
doc_updated_at: 2026-05-18
content_hash: sha256:f3d6db33cbfad9775348a2f78eacd00fa658f520958679ffaf94c07dd8377e7b
---
系统提供了MovingPhotoView组件，在一些社交类、图库类应用中，可用于播放动态照片文件。

## 约束与限制

针对MovingPhotoView组件的使用，有以下约束与限制：

* 当前不支持动态属性设置。
* 当前不支持设置ArkUI通用属性[expandSafeArea](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/通用属性/布局与边框/安全区域/ts-universal-attributes-expand-safe-area.md#expandsafearea)。
* 该组件长按触发播放时组件区域放大为1.1倍。
* 该组件使用[AVPlayer](<../../../../../harmonyos-references/Media Kit（媒体服务）/ArkTS API/@ohos.multimedia.media (媒体服务)/Interface (AVPlayer)/arkts-apis-media-avplayer.md>)进行播放，同时开启的AVPlayer个数不建议超过3个，超过3个可能会出现视频播放卡顿现象。

## 开发步骤

1. 导入动态照片模块。

   说明

   * MovingPhotoViewAttribute是用于配置MovingPhotoView组件属性的关键接口。API version 21及之前版本，导入MovingPhotoView组件后需要开发者手动导入MovingPhotoViewAttribute，否则会编译报错。从API version 22开始，编译工具链识别到导入MovingPhotoView组件后，会自动导入MovingPhotoViewAttribute，无需开发者手动导入。
   * MovingPhotoViewAttribute导入后，DevEco Studio会将其显示置灰，不影响开发者使用。

   API version 21及之前版本：

   ```
   1. //import { MovingPhotoView, MovingPhotoViewController, MovingPhotoViewAttribute } from '@kit.MediaLibraryKit';
   ```

   API version 22及之后版本：

   ```
   1. import { MovingPhotoView, MovingPhotoViewController } from '@kit.MediaLibraryKit';
   ```
2. 获取动态照片对象（[MovingPhoto](<../../../../../harmonyos-references/Media Library Kit（媒体文件管理服务）/ArkTS API/@ohos.file.photoAccessHelper (相册管理模块)/Interface (MovingPhoto)/arkts-apis-photoaccesshelper-movingphoto.md>)）。

   MovingPhoto对象需要通过photoAccessHelper接口创建或获取，MovingPhotoView只接收构造完成的MovingPhoto对象。

   创建、获取的方式可参考[访问和管理动态照片资源](../访问和管理动态照片资源/photoaccesshelper-movingphoto.md)。

   ```
   1. @State src: photoAccessHelper.MovingPhoto | undefined = undefined
   ```
3. 创建动态照片控制器（[MovingPhotoViewController](<../../../../../harmonyos-references/Media Library Kit（媒体文件管理服务）/ArkTS组件/@ohos.multimedia.movingphotoview (动态照片)/ohos-multimedia-movingphotoview.md#movingphotoviewcontroller>)），用于控制动态照片的播放状态（如播放、停止）。

   ```
   1. controller: MovingPhotoViewController = new MovingPhotoViewController();
   ```
4. 创建动态照片组件。

   以下参数取值仅为举例，具体每个属性的取值范围，可参考API文档：[@ohos.multimedia.movingphotoview](<../../../../../harmonyos-references/Media Library Kit（媒体文件管理服务）/ArkTS组件/@ohos.multimedia.movingphotoview (动态照片)/ohos-multimedia-movingphotoview.md>)。

   ```
   1. // API version 21及之前版本导入方式：import { photoAccessHelper, MovingPhotoView, MovingPhotoViewController, MovingPhotoViewAttribute } from '@kit.MediaLibraryKit';
   2. // API version 22及之后版本导入方式如下：
   3. // import { photoAccessHelper, MovingPhotoView, MovingPhotoViewController } from '@kit.MediaLibraryKit';

   5. @Entry
   6. @Component
   7. struct Index {
   8. @State src: photoAccessHelper.MovingPhoto | undefined = undefined
   9. // ...
   10. @State isMuted: boolean = false
   11. controller: MovingPhotoViewController = new MovingPhotoViewController();

   13. // ...

   15. build() {
   16. Column() {
   17. // ...

   19. MovingPhotoView({
   20. movingPhoto: this.src,
   21. controller: this.controller
   22. })
   23. // 是否静音播放，此处由按钮控制，默认值为false非静音播放。
   24. .muted(this.isMuted)
   25. // 视频显示模式，默认值为Cover。
   26. .objectFit(ImageFit.Cover)
   27. // 播放时触发。
   28. .onStart(() => {
   29. console.info('onStart');
   30. })
   31. // 播放结束触发。
   32. .onFinish(() => {
   33. console.info('onFinish');
   34. })
   35. // 播放停止触发。
   36. .onStop(() => {
   37. console.info('onStop')
   38. })
   39. // 出现错误触发。
   40. .onError(() => {
   41. console.error('onError');
   42. })
   43. // ...

   45. Row() {
   46. // 按钮：开始播放。
   47. Button('PLAY')
   48. .onClick(() => {
   49. this.controller.startPlayback()
   50. })
   51. .margin(5)
   52. // 按钮：停止播放。
   53. Button('STOP')
   54. .onClick(() => {
   55. this.controller.stopPlayback()
   56. })
   57. .margin(5)
   58. // ...
   59. }
   60. .alignItems(VerticalAlign.Center)
   61. .justifyContent(FlexAlign.Center)
   62. .height('15%')
   63. }
   64. // ...
   65. }
   66. }
   ```

## 效果展示

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/85/v3/lPM9SYa8RuSwO1gcZxpPrg/zh-cn_image_0000002592219040.gif?HW-CC-KV=V1&HW-CC-Date=20260611T065820Z&HW-CC-Expire=86400&HW-CC-Sign=49156DD917BA15B90354534C16E85349A51549266040B7C469CD78BFCCB5A39A)
