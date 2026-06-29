---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkgraphics-editor
title: ArkGraphics Editor插件及编辑器的下载与安装
breadcrumb: 指南 > 图形 > ArkGraphics 3D（方舟3D图形） > ArkGraphics Editor插件及编辑器的下载与安装
category: harmonyos-guides
scraped_at: 2026-06-11T15:01:09+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:a2dbf2d71eea8401dd2e2bef328af17d4a325a32d2db1337a649d7f072cd92c3
---

3D编辑器ArkGraphics Editor提供3D模型、动画、ShaderGraph等核心编辑能力，可供设计师、开发者快速接入使用。支持通过拖拽等操作，利用3D编辑器可视化能力，完成3D场景开发，3D设计效果所见即所得。无需代码编写，支持从PC到移动端设备的快速流转， 可大幅提升3D应用开发效率。

## 主要功能

ArkGraphics Editor编辑器当前主要支持功能如下：

* 编辑器工程的新建、打开、保存功能。
* 支持导入gltf格式的3D模型和image图片。
* 支持相机新增、修改、删除。
* 支持3D场景里模型的缩放、移动、旋转等拖动操作。
* 支持3D场景节点新增、修改、删除功能。
* 支持3D场景节点的属性设置，包括位置、颜色，旋转、缩放功能。
* 支持3D模型的动画新增、修改、删除功能。
* 支持3D模型的材质新增、修改、删除功能。
* 支持3D模型的ShaderGraph新增、修改、删除功能。
* 支持环境光的添加和设置。

ArkGraphics Editor插件支持的主要功能如下：

* 支持在DevEco中预览3D场景文件(.Scene)。
* 可点击“Open ArkGraphicsEditor”打开编辑器程序编辑3D资源。

## 插件的安装及编辑器的使用

1. 前往[下载中心](https://developer.huawei.com/consumer/cn/download/)下载最新版本ArkGraphics Editor插件。
2. 点击DevEco Studio菜单项的File，选择Settings，选择左边列表的Plugins。
3. 点击Plugins窗口的顶部设置按钮，选择Install Plugin from Disk...。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/88/v3/UMn9ouv_SnqMItZ9cDZLEg/zh-cn_image_0000002622698697.png?HW-CC-KV=V1&HW-CC-Date=20260611T070108Z&HW-CC-Expire=86400&HW-CC-Sign=D610B1BCA362118A88A8A42B19B7EC56D38D5201606C4936FDAE87711FD29D59)
4. 选择下载的插件，进行安装。
5. 安装成功后，关闭DevEco Studio，再重新打开，选择3D工程里的\*.scene文件，可在DevEco Studio里打开显示3D场景内容。
6. 前往[下载中心](https://developer.huawei.com/consumer/cn/download/)下载最新版本ArkGraphics Editor编辑器，并进行安装。

   插件主要用来预览，当开发者需要进行3D编辑开发时，可点击“Open Ark Graphics Editor”打开3D编辑器对3D模型进行编辑。

   说明

   * 要使用ArkGraphics Editor编辑器，需要满足以下条件：

     + 对应设备已安装Visual Studio 2022 Community。
     + Visual Studio 2022 Community已安装使用C++ 进行桌面开发的选项。
   * 编辑器生成的3D资源文件，目前只支持在HarmonyOS 6.0.0及以上版本的设备上加载呈现。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/82/v3/p99aJAj4Tt2SfV7VNUZ59w/zh-cn_image_0000002592219136.png?HW-CC-KV=V1&HW-CC-Date=20260611T070108Z&HW-CC-Expire=86400&HW-CC-Sign=5E36ACB3E1546BB1380CC984360AC8A11D1B64584116B7A970A8E76825F88A62)

## 创建使用3D编辑器资源的工程

1. 创建一个新工程或在已有工程下，右键工程名，选择New，选择Ark Graphics Editor Project。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cd/v3/VJs136ctQ3isz9jTgvl_gw/zh-cn_image_0000002592379070.png?HW-CC-KV=V1&HW-CC-Date=20260611T070108Z&HW-CC-Expire=86400&HW-CC-Sign=322209208456D93857DDD7456DE25B4E870B8F52802A69827B4D52E3AEF61DA3)
2. 输入3D资源工程名。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6c/v3/GoGj71GaRmC2_BucrxvedA/zh-cn_image_0000002622858577.png?HW-CC-KV=V1&HW-CC-Date=20260611T070108Z&HW-CC-Expire=86400&HW-CC-Sign=0E0B55CF7175F474C4117B6AB3DEF92FEE6071665BA4F92091F1E9BEB26BEEB6)
3. 双击default.scene，可显示创建的3D场景资源。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7f/v3/GNwv1tApTSq3lgl_Fa-6-A/zh-cn_image_0000002622698699.png?HW-CC-KV=V1&HW-CC-Date=20260611T070108Z&HW-CC-Expire=86400&HW-CC-Sign=34E0114AA709EDAA95F23C306E5B7A483EA543875E634832213C2E000DEF097E)
4. 点击右下角Editor，可打开编辑器编辑3D资源，编辑保存后，可显示编辑后的资源。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6e/v3/hq8jm5pYQR-LcLdKjyCMhA/zh-cn_image_0000002592219138.png?HW-CC-KV=V1&HW-CC-Date=20260611T070108Z&HW-CC-Expire=86400&HW-CC-Sign=B660AFEC65F51336591DDC3AAC41C23373F5E80C7079A1AB1128D17122640A3D)
5. 修改复制资源脚本文件。

   脚本文件路径：xxx/MyApplication/entry/hvigorfile.ts

   运行工程时会执行该脚本将3D资源复制到assets目录下。

   ```
   1. // entry/hvigorfile.ts
   2. import { hapTasks } from '@ohos/hvigor-ohos-plugin';

   4. import { getNode } from '@ohos/hvigor';
   5. import * as MyEditorProject  from '../ArkGraphics/package-assets';
   6. MyEditorProject.packageAssetsToModule(getNode(__filename));

   8. export default {
   9. system: hapTasks,  /* Built-in plugin of Hvigor. It cannot be modified. */
   10. plugins:[]         /* Custom plugin to extend the functionality of Hvigor. */
   11. }
   ```
6. 修改Index.ets，加载3D资源。

   注意Index.ets代码内容中加载的目录名与3D资源工程名保持一致。

   ```
   1. // Index.ets
   2. import * as scene3d from '@ohos.graphics.scene'

   4. @Entry
   5. @Component
   6. struct Index {
   7. scene: scene3d.Scene | null = null;
   8. cam: scene3d.Camera | null = null;
   9. @State sceneOpts: SceneOptions | null = null;
   10. @State statusText: string = "";

   12. onPageShow(): void {
   13. this.Init();
   14. }

   16. Init(): void {
   17. if (this.scene == null) {
   18. this.statusText = 'Loading scene. Please wait.'
   19. const resource = $rawfile('ArkGraphics/assets/default.scene');

   21. scene3d.Scene.load(resource).then(async (scene: Scene) => {
   22. this.scene = scene;

   24. this.cam = this.scene.root?.getNodeByPath("Perspective Camera") as scene3d.Camera;
   25. this.cam.enabled = true;

   27. this.sceneOpts = { scene: this.scene, modelType: ModelType.SURFACE };
   28. this.statusText = 'Done.'
   29. }).catch(() => {
   30. this.statusText = 'Failed to load scene.'
   31. })
   32. }
   33. }

   35. build() {
   36. Row() {
   37. Column() {
   38. Text('Ark Graphics Scene Example 3')
   39. if (this.sceneOpts) {
   40. Component3D(this.sceneOpts).width('70%').height('70%')
   41. }
   42. if (this.statusText) {
   43. Text(this.statusText)
   44. }
   45. }.width('100%')
   46. }
   47. .height('100%')
   48. }
   49. }
   ```
7. 完成以上操作后，可在真机运行工程，观察3D资源加载效果。

   说明

   编辑器生成的3D资源文件，目前只支持在HarmonyOS 6.0.0及以上版本的设备上加载呈现。
