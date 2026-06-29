---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-web-develop-optimization
title: Web加载性能优化
breadcrumb: 最佳实践 > 性能 > 性能场景优化案例 > Web性能优化 > Web加载性能优化
category: best-practices
scraped_at: 2026-06-12T10:16:04+08:00
doc_updated_at: 2026-05-22
content_hash: sha256:fd7ba17574c9bd625f51ec90cfd3cdf01023a48ce1ce861a1159243004be2665
---
## 概述

ArkWeb是一个Web组件平台，旨在为应用程序提供展示Web页面内容的功能，并为开发者提供丰富的能力，如页面加载、页面交互和页面调试。在当前的数字化时代，页面加载速度直接影响应用的流畅性，进而影响用户对应用的印象和体验。迅速加载并展示页面，可以吸引用户留在应用上，减少等待时间，从而提升用户满意度。

Web页面显示过程包含DNS解析、建立连接等阶段，其速度受网络延迟、资源大小等因素影响。为提升Web页面显示速度，开发者可以从Web页面加载、资源下载和页面渲染等方面进行优化，提高性能和用户体验。

本文将介绍以下常见的优化方式。

* Web页面加载优化：提高页面加载速度能直接提升应用的流畅性。
* JSBridge：通过JSBridge通信，可以解决ArkTS环境的冗余切换，避免造成UI阻塞。
* 同层渲染：将页面元素分层渲染，减少页面重绘和重排次数，提升页面渲染效率。

ArkWeb（方舟Web）为开发者提供了优化页面显示速度的方法。采取这些优化方式可以改善应用性能和用户体验，提升用户满意度和留存率。

## Web页面加载性能优化指导

### Web页面加载流程

Web页面加载流程包括网络连接、资源下载（包括等待网络资源下载）、DOM解析、JavaScript代码编译执行、渲染等。页面加载中，比较关键的节点有网络连接、资源下载和完整的页面渲染，本文将主要对以下关键节点的耗时进行优化。

* 预启动Web渲染进程：预启动Web渲染进程指在业务需要的Web页面启动前，加载一个空白Web组件。当至少一个Web组件存活时，Web渲染进程将一直存在，从而节省后续启动Web组件时拉起渲染进程的时间，加快页面加载速度。
* 预解析：预解析是预先对DNS进行解析，以节省解析时间，优化Web加载速度。

* 预连接：预连接包含预解析步骤，可在用户请求页面前完成DNS解析和socket连接建立。这样，用户真正请求页面时，服务器与浏览器之间已建立连接，可直接传输数据，减少网络延迟，提升页面加载速度。
* 预下载：预下载是指在页面加载之前提前下载所需的资源，以避免资源下载导致的阻塞和延迟。通过预下载，浏览器可以在加载页面时提前获取所需的资源，如图片、CSS文件和JavaScript文件。提前下载这些资源可以避免页面渲染因资源未加载完成而延迟的情况。合理使用预下载技术，可以加快页面加载速度，提升用户体验。
* 预渲染：预渲染是指在后台提前渲染需要加载的页面，完成整个页面加载流程。当访问该页面时，可直接切换至前台展示，实现页面“秒开”。预渲染需在DOM解析、JavaScript执行和页面渲染前完成所需资源的下载，否则可能导致页面内容不完整或渲染错误。预渲染可显著减少页面加载时间，尤其适用于资源密集型或交互复杂的页面。
* 预取POST：当即将加载的Web页面中存在POST请求且该请求耗时较长时，可以预先获取POST请求的数据，从而消除等待POST请求数据下载完成的耗时。当用户实际发起POST请求时，系统将拦截并替换预取的数据，从而加快页面加载速度，提升用户体验。
* 预编译JavaScript文件生成字节码缓存：将JavaScript文件编译成字节码并缓存到本地，首次加载页面时可节省编译时间。
* 资源拦截替换时，JavaScript生成字节码缓存（Code Cache）将JavaScript文件编译成字节码并缓存到本地，节省页面非首次加载时的编译时间。
* 离线资源免拦截注入：在页面加载前，将所需的图片、样式表和脚本资源注入内存缓存，以减少首次加载时的网络请求时间。
* 资源拦截替换加速：资源拦截替换加速支持ArrayBuffer格式的入参，开发者可直接使用ArrayBuffer格式的数据进行拦截替换，无需在应用侧进行格式转换。

**图1** Web页面加载流程   
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/27/v3/c7SpHoGKRVOjNbP20S4Jjg/zh-cn_image_0000002229451093.png?HW-CC-KV=V1&HW-CC-Date=20260612T021559Z&HW-CC-Expire=86400&HW-CC-Sign=23A5A07927761C7562248E86819BA7D9BF42E2DCBB2E9E95921E49815D3AD402 "点击放大")

**由于所有的关键点都是建立在预处理的思路上，因此如果用户实际并未打开预处理的Web页面，将会造成额外的资源消耗。**下表列出了各优化方法的具体效果、代价和适用场景对比。

**表1** 优化方法对比表格

| 优化方法 | **效果**（优化数据仅供参考） | 适配难度 | 影响 | **适用场景** |
| --- | --- | --- | --- | --- |
| 预启动Web渲染进程 | 消除拉起Web渲染进程的耗时，约140ms。 | 低 | 额外的内存、算力。 | 高概率被使用的Web页面。 |
| 预解析 | 消除用户真正启动的Web网页域名解析的耗时，约66ms。 | 低 | 可能存在提前解析了用户未启动的Web网页域名。 | 中高概率被使用的Web页面。 |
| 预连接 | 消除用户真正启动的Web网页域名解析、网络连接耗时，约80ms。 | 低 | 可能存在提前连接了用户未启动Web网页资源。 | 中高概率被使用的Web页面。 |
| 预下载 | 消除网络GET请求下载带来的耗时及阻塞DOM解析、JavaScript执行的耗时，约641ms。 | 低 | 额外的网络连接、下载、存储资源。 | 高概率被使用的Web页面。 |
| 预渲染 | 能实现页面“秒开”效果，将页面加载时延降到最低，约486ms。 | 中 | 额外的网络连接、下载、存储和渲染消耗。 | 超高概率被使用的Web页面。 |
| 预取POST | 消除网络POST请求下载带来的耗时及阻塞DOM解析、JavaScript执行的耗时，约313ms。 | 中 | 额外的网络连接、下载、存储资源。 | 高概率被使用的Web页面。 |
| 预编译JavaScript生成字节码缓存 | 消除JavaScript编译的耗时，优化数据根据JS资源大小而定，5.76MB资源预编译时约有2915ms收益。 | 中 | 额外的存储资源。 | 加载HTTP/HTTPS协议JavaScript的Web页面，在前两次优化加载性能。 |
| 资源拦截替换的JavaScript生成字节码缓存 | 消除JavaScript编译的耗时，优化数据根据JS资源大小而定，2.4MB资源拦截替换时约有67ms收益。 | 高 | 额外的存储资源。 | 加载自定义协议JavaScript的Web页面，在第三次及以后优化加载性能。 |
| 离线资源免拦截注入 | 消除资源加载到内存的耗时，优化数据根据资源大小而定，25MB资源注入时约有1240ms收益。 | 中 | 额外的存储资源。 | 高概率被使用的资源。 |
| 资源拦截替换加速 | 节省了转换时间，同时对ArrayBuffer格式的数据传输方式进行了优化，优化数据根据资源大小而定，10Kb资源拦截替换时约有20ms收益。 | 低 | - | ArrayBuffer格式的数据传输。 |

### 预启动Web渲染进程

**原理介绍**

预启动Web渲染进程指用户可以在业务需要的Web页面启动前，加载一个空白的Web组件，在至少一个Web组件存活时，Web渲染进程会一直存在，节省了用户后续启动Web组件拉起渲染进程的时间，加快页面加载速度。

建议在Web页面启动前执行预启动Web渲染进程，例如在应用冷启动阶段或广告展示阶段。如果无法在冷启动期间预启动Web渲染进程，建议在系统空闲时间进行预启动。

**图2** 预启动Web渲染流程   
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1f/v3/0iEe6wXOQUqyr-WNip9O4g/zh-cn_image_0000002229451109.png?HW-CC-KV=V1&HW-CC-Date=20260612T021559Z&HW-CC-Expire=86400&HW-CC-Sign=44B188752EED1D66766D195FBF3AF9FF1117300A4A27BF66B87AA8A1CC4858BF "点击放大")

说明

1. 该方案通过创建一个空白的ArkWeb组件来预启动Web渲染进程。额外创建ArkWeb组件会消耗内存和算力，预创建一个空白的Web组件大约消耗200MB内存。因此，建议后续页面加载复用预创建的Web组件。
2. 应用全局共享一个Web渲染进程，仅在所有Web组件销毁时，该进程才会终止。因此，建议应用确保至少有一个Web组件处于活动状态。

**实践案例**

【不推荐用法】

点击跳转到下一页，直接加载Web页面。

说明

该示例涉及网络地址访问，需配置网络权限。

```
1. // Index.ets
2. @Entry
3. @Component
4. struct Index {
5. pageInfos: NavPathStack = new NavPathStack()

7. build() {
8. Navigation(this.pageInfos) {
9. Column() {
10. Button('加载测试页面', { stateEffect: true, type: ButtonType.Capsule })
11. .width('80%')
12. .height(40)
13. .margin(20)
14. .onClick(() => {
15. // Put the NavDestination page information specified by name on the stack.
16. this.pageInfos.pushPath({ name: 'pageOne' })
17. })
18. }
19. }.title('NavIndex')
20. }
21. }
```

[Index.ets](https://gitcode.com/HarmonyOS_Samples/BestPracticeSnippets/blob/master/LoadPerformanceInWeb/entry/src/main/ets/pages/Index.ets#L6-L26)

```
1. // Second.ets
2. import { webview } from '@kit.ArkWeb'
3. import { hilog } from '@kit.PerformanceAnalysisKit';

5. const DOMAIN = 0x0000;
6. const TAG = 'Sample';

8. @Builder
9. export function PageOneBuilder() {
10. Second()
11. }

13. @Component
14. export struct Second {
15. webviewController: webview.WebviewController = new webview.WebviewController();

17. aboutToAppear(): void {
18. // Output Web page start loading time
19. hilog.info(DOMAIN, TAG, `load page start time: ${Date.now()}`);
20. }

22. build() {
23. NavDestination() {
24. Row() {
25. Column() {
26. // Please replace the URL with the real address.
27. Web({ src: 'https://www.example.com', controller: this.webviewController })
28. .height('100%')
29. .width('100%')
30. .onPageEnd((event) => {
31. // Output Web page loading completion time
32. hilog.info(DOMAIN, TAG, `load page end time: ${Date.now()}`);
33. })
34. }
35. .width('100%')
36. }
37. .height('100%')
38. }
39. }
40. }
```

[Second.ets](https://gitcode.com/HarmonyOS_Samples/BestPracticeSnippets/blob/master/LoadPerformanceInWeb/entry/src/main/ets/view/Second.ets#L2-L41)

点击“加载测试页面”按钮，页面加载完成耗时82ms，具体如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/24/v3/bAURdHEOTX2cfbs7vPCybw/zh-cn_image_0000002229336649.png?HW-CC-KV=V1&HW-CC-Date=20260612T021559Z&HW-CC-Expire=86400&HW-CC-Sign=16606DB499EB9BCE4E755DFD88F5988ECFCF1E8740B1BBDC1BBFF60C60C0C619 "点击放大")

【推荐用法】

在后台创建一个ArkWeb组件来预先启动用于渲染的Web渲染进程。

1. 创建Node和对应的NodeController。在后台创建ArkWeb组件。

   ```
   1. // Create NodeController
   2. // common.ets
   3. import { UIContext } from '@kit.ArkUI';
   4. import { webview } from '@kit.ArkWeb';
   5. import { NodeController, BuilderNode, Size, FrameNode }  from '@kit.ArkUI';
   6. import { hilog } from '@kit.PerformanceAnalysisKit';

   8. const DOMAIN = 0x0000;
   9. const TAG = 'Sample';

   11. // Specific component contents of dynamic components in @Builder
   12. // Data is a parameter encapsulation class.
   13. class Data{
   14. url: string = 'https://www.example.com';
   15. controller: WebviewController = new webview.WebviewController();
   16. }

   18. let shouldInactive: boolean = true;
   19. @Builder
   20. function WebBuilder(data:Data) {
   21. Column() {
   22. Web({ src: data.url, controller: data.controller })
   23. .domStorageAccess(true)
   24. .zoomAccess(true)
   25. .fileAccess(true)
   26. .mixedMode(MixedMode.All)
   27. .width('100%')
   28. .height('100%')
   29. .onPageBegin(() => {
   30. data.controller.onActive();
   31. })
   32. .onPageEnd(() => {
   33. hilog.info(DOMAIN, TAG, `load page end time: ${Date.now()}`);
   34. })
   35. .onFirstMeaningfulPaint(() =>{
   36. if (!shouldInactive) {
   37. return;
   38. }
   39. // stop render
   40. data.controller.onInactive();
   41. shouldInactive = false;
   42. })
   43. }
   44. }

   47. // Used to control and feedback the behavior of nodes on the corresponding NodeContainer, which needs to be used together with NodeContainer
   48. export class MyNodeController extends NodeController {
   49. private rootNode: BuilderNode<Data[]> | null = null;
   50. private root: FrameNode | null = null;

   52. // The method that must be overridden is used to build the number of nodes and return the nodes to be mounted in the corresponding NodeContainer.
   53. // //Called when the corresponding NodeContainer is created, or refreshed by calling the rebuild method.
   54. makeNode(uiContext: UIContext): FrameNode | null {
   55. hilog.info(DOMAIN, TAG, ' uicontext is undefined : '+ (uiContext === undefined));
   56. if (this.rootNode != null) {
   57. const parent: FrameNode = this.rootNode.getFrameNode()?.getParent() as FrameNode;
   58. if (parent) {
   59. let inspectorInfo: string = JSON.stringify(parent.getInspectorInfo());
   60. hilog.info(DOMAIN, TAG, inspectorInfo);
   61. parent.removeChild(this.rootNode.getFrameNode());
   62. this.root = null;
   63. }
   64. this.root = new FrameNode(uiContext);
   65. this.root.appendChild(this.rootNode.getFrameNode());
   66. // Returns the FrameNode node
   67. return this.root;
   68. }
   69. // Returns a null node that controls the dynamic component to be unbound.
   70. return null;
   71. }
   72. // Callback when layout size changes.
   73. aboutToResize(size: Size): void {
   74. hilog.info(DOMAIN, TAG, 'aboutToResize width : ' + size.width  +  ' height : ' + size.height);

   76. }

   78. // Call back when the NodeContainer corresponding to the controller is in Appear.
   79. aboutToAppear(): void {
   80. hilog.info(DOMAIN, TAG, 'aboutToAppear');
   81. }

   83. // Call back when the NodeContainer corresponding to the controller is Disappear.
   84. aboutToDisappear(): void {
   85. hilog.info(DOMAIN, TAG, 'aboutToDisappear');
   86. }

   88. // This function is a user-defined function and can be used as an initialization function.
   89. // Initialize builderNode through UIContext, and then initialize the contents in @Builder through the Build interface in BuilderNode.
   90. initWeb(url:string, uiContext:UIContext, control:WebviewController): void {
   91. if(this.rootNode != null)
   92. {
   93. return;
   94. }
   95. // Creating a node requires uiContext.
   96. this.rootNode = new BuilderNode(uiContext)
   97. // Create dynamic Web components
   98. this.rootNode.build(wrapBuilder<Data[]>(WebBuilder), { url:url, controller:control })
   99. }
   100. }

   102. // Create the NodeController needed for Map saving.
   103. let NodeMap:Map<string, MyNodeController | undefined> = new Map();
   104. // Create WebViewController needed for Map saving.
   105. let controllerMap:Map<string, WebviewController | undefined> = new Map();

   107. // Initialization requires UIContext to be obtained in Ability.
   108. export const createNWeb = (url: string, uiContext: UIContext) => {
   109. // Create NodeController
   110. let baseNode: MyNodeController = new MyNodeController();
   111. let controller: WebviewController = new webview.WebviewController() ;
   112. // Initialize a custom web component
   113. baseNode.initWeb(url, uiContext, controller);
   114. controllerMap.set(url, controller)
   115. NodeMap.set(url, baseNode);
   116. }

   118. // Customize to get the NodeController interface.
   119. export const getNWeb = (url : string) : MyNodeController | undefined => {
   120. return NodeMap.get(url);
   121. }
   ```

   [CreateNodeController.ets](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/LoadPerformanceInWeb/entry/src/main/ets/pages/CreateNodeController.ets#L2-L122)
2. 创建载体，并创建ArkWeb组件，加载一个blank页面。

   ```
   1. // Carrier Ability
   2. import { UIAbility } from '@kit.AbilityKit';
   3. import { window } from '@kit.ArkUI';
   4. import { createNWeb } from '../pages/common';

   6. export default class EntryAbility extends UIAbility {
   7. onWindowStageCreate(windowStage: window.WindowStage): void {
   8. windowStage.loadContent('pages/Index', (err) => {
   9. // Create an empty ArkWeb dynamic component in advance (need to pass in UIContext) and start the rendering process.
   10. createNWeb('about://blank', windowStage.getMainWindowSync().getUIContext());
   11. });
   12. }
   13. }
   ```

   [EntryAbility.ets](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/LoadPerformanceInWeb/entry/src/main/ets/entryability/EntryAbility.ets#L2-L14)
3. 创建需要加载的ArkWeb组件。

   首页：

   ```
   1. // Index.ets
   2. @Entry
   3. @Component
   4. struct Index {
   5. pageInfos: NavPathStack = new NavPathStack()

   7. build() {
   8. Navigation(this.pageInfos) {
   9. Column() {
   10. Button('加载测试页面', { stateEffect: true, type: ButtonType.Capsule })
   11. .width('80%')
   12. .height(40)
   13. .margin(20)
   14. .onClick(() => {
   15. // Put the NavDestination page information specified by name on the stack.
   16. this.pageInfos.pushPath({ name: 'pageOne' })
   17. })
   18. }
   19. }.title('NavIndex')
   20. }
   21. }
   ```

   [Index.ets](https://gitcode.com/HarmonyOS_Samples/BestPracticeSnippets/blob/master/LoadPerformanceInWeb/entry/src/main/ets/pages/Index.ets#L6-L26)

   跳转测试页面：

   ```
   1. // Second.ets
   2. import { webview } from '@kit.ArkWeb';
   3. import { getNWeb } from './common';
   4. import { hilog } from '@kit.PerformanceAnalysisKit';

   6. const DOMAIN = 0x0000;
   7. const TAG = 'Sample';

   9. @Builder
   10. export function PageOneBuilder() {
   11. Second()
   12. }

   14. @Component
   15. export struct Second {
   16. webviewController: webview.WebviewController = new webview.WebviewController();
   17. aboutToAppear(): void {
   18. // Output Web page start loading time
   19. hilog.info(DOMAIN, TAG, `load page start time: ${Date.now()}`);
   20. }
   21. build() {
   22. NavDestination() {
   23. Row() {
   24. Column() {
   25. // Please replace the URL with the real address.
   26. NodeContainer(getNWeb('https://www.example.com'))
   27. .height('100%')
   28. .width('100%')
   29. }
   30. .width('100%')
   31. }
   32. .height('100%')
   33. }
   34. }
   35. }
   ```

   [Second.ets](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/LoadPerformanceInWeb/entry/src/main/ets/pages/Second.ets#L2-L36)

点击“加载测试页面”按钮，页面加载完成耗时44ms，具体如图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/88/v3/fqxo10ENSvuN0NoFpSQSIQ/zh-cn_image_0000002229336617.png?HW-CC-KV=V1&HW-CC-Date=20260612T021559Z&HW-CC-Expire=86400&HW-CC-Sign=DC8E89B8A6223A833CD27706101C39860B95A84F32B6FBC5A644A93AB262564B "点击放大")

说明

开发者可以在后续页面操作中选择是否复用ArkWeb组件。

**总结**

| 下一页加载方式 | 耗时(局限不同设备和场景，数据仅供参考) | 说明 |
| --- | --- | --- |
| 直接加载Web页面 | 82ms | 页面加载时拉起渲染进程，增加加载时间 |
| 使用预启动Web渲染进程方案 | 44ms | 在闲时提前拉起渲染进程，优化启动时间 |

### 预解析和预连接优化

**原理介绍**

应用启动和UIAbility的onCreate生命周期完成后，Web组件才能初始化和运行。ArkWeb组件运行阶段包括onAppear、load、onPageBegin、onPageEnd步骤。预解析、预连接优化适用于Web页面启动和跳转场景，例如应用启动时加载Web首页。创建ArkWeb组件实例后，开发者可以选择不同时机设置URL并进行预解析、预连接。

* 如下图中a节点所示，如果是应用首页，推荐在ArkWeb组件初始化后设置首页URL，进行预解析和预连接。
* 如下图中b节点所示，对于应用内页面，推荐在ArkWeb组件的onAppear阶段设置当前页面的URL，进行预解析和预连接。
* 如下图中c节点所示，页面加载完成后，设置用户下一步可能点击页面的URL，进行预解析和预连接，推荐在onPageEnd及后续时机执行。

**图3** 预连接优化原理图   
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/86/v3/oG624stNRde2Nda4Lee_sQ/zh-cn_image_0000002194010808.png?HW-CC-KV=V1&HW-CC-Date=20260612T021559Z&HW-CC-Expire=86400&HW-CC-Sign=D6B7309B654C8A369D6125CB3C1BB76CAFAD7ABE1AC64F309F25FAF33B7315A2 "点击放大")

说明

在设置预解析和预连接进行优化时，需要注意：

* 预连接存在时效性，建议在5分钟内复用已建立的连接，超时后连接将被关闭。
* 预连接存在耗时，建议预加载时间比页面实际时间提前150ms以上。
* 当前页面加载完成后，即onPageEnd回调后，可复用当前ArkWeb组件预连接新的页面或预下载资源。

**实践案例**

案例一：如果需要提前对应用的首页进行操作，可以调用initializeWebEngine()初始化ArkWeb组件的内核，然后调用prepareForPageLoad()预连接即将加载的页面。在prepareForPageLoad中，将第二个参数设为true以进行预连接，设为false时仅进行DNS预解析。具体代码如下所示。

```
1. import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
2. import { webview } from '@kit.ArkWeb';
3. import { hilog } from '@kit.PerformanceAnalysisKit';

5. const DOMAIN = 0x0000;
6. const TAG = 'Sample';

8. export default class EntryAbility extends UIAbility {
9. onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) {
10. hilog.info(DOMAIN, TAG, 'EntryAbility onCreate');
11. webview.WebviewController.initializeWebEngine();
12. // When pre-connecting, you need to replace' https://www.example.com' with the actual website address to visit
13. // Specify that the second parameter is true, which means to pre-connect. If it is false, the interface will only pre-resolve the URL.
14. // The third parameter, numSockets, has a value range of 1-6. If it exceeds 6, the parameter will be treated as 6.
15. webview.WebviewController.prepareForPageLoad('https://www.example.com/', true, 2);
16. AppStorage.setOrCreate('abilityWant', want);
17. hilog.info(DOMAIN, TAG, 'EntryAbility onCreate done');
18. }
19. }
```

[CaseOne.ets](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/LoadPerformanceInWeb/entry/src/main/ets/pages/CaseOne.ets#L2-L20)

说明

prepareForPageLoad预解析和预连接只和host相关，URL带参数的情况下也能进行预解析和预连接。

案例二：如果需要提前连接当前页面的Web页面，可以在Web组件的 `onAppear` 方法中预连接要加载的页面。具体代码如下所示：

```
1. import { webview } from '@kit.ArkWeb';

3. @Entry
4. @Component
5. struct WebComponent {
6. webviewController: webview.WebviewController = new webview.WebviewController();
7. build() {
8. Column() {
9. Button('loadData')
10. .onClick(() => {
11. if (this.webviewController.accessBackward()) {
12. this.webviewController.backward();
13. }
14. })
15. Web({ src: 'https://www.example.com/cn/', controller: this.webviewController})
16. .onAppear(() => {
17. // Specify that the second parameter is true, which means to pre-connect. If it is false, the interface will only pre-resolve the URL.
18. // The third parameter is the number of socket to be pre-connected. A maximum of six are allowed.
19. webview.WebviewController.prepareForPageLoad('https://www.example.com/cn/', true, 2);
20. })
21. }
22. }
23. }
```

[CaseTwo.ets](https://gitcode.com/HarmonyOS_Samples/BestPracticeSnippets/blob/master/LoadPerformanceInWeb/entry/src/main/ets/pages/CaseTwo.ets#L2-L24)

案例三：当前页面显示完成后，可以在onPageEnd()中预连接下一个页面。

```
1. import { webview } from '@kit.ArkWeb';

3. @Entry
4. @Component
5. struct WebComponent {
6. webviewController: webview.WebviewController = new webview.WebviewController();
7. build() {
8. Column() {
9. Web({ src: 'https://www.example.com/', controller: this.webviewController})
10. .onPageEnd(() => {
11. // Pre-connected https://www.example1.com/
12. // The third parameter, numSockets, has a value range of 1-6. If it exceeds 6, the parameter will be treated as 6.
13. webview.WebviewController.prepareForPageLoad('https://www.example.com/', true, 2);
14. })
15. }
16. }
17. }
```

[CaseThree.ets](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/LoadPerformanceInWeb/entry/src/main/ets/pages/CaseThree.ets#L2-L18)

### 预下载优化

**原理介绍**

如下图所示，ArkWeb组件运行包含onAppear、load、onPageBegin、onPageEnd。开发者可以在onPageEnd设置下一步访问的URL，提前下载所需资源。这种方式适用于Web页面启动和跳转场景，例如，在引导流程完成后，预下载需要跳转的页面。创建ArkWeb组件实例后，可以在当前页面加载完成后，设置URL并进行预下载。本方案可以消除资源下载耗时及资源下载导致的页面DOM解析、JS代码编译执行的阻塞耗时，预估收益在数百毫秒（具体时间依赖当前网络环境）。

**图4** 预下载优化原理图   
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3b/v3/mRqZBwBfQgKCTh4Ia_BJJA/zh-cn_image_0000002194010844.png?HW-CC-KV=V1&HW-CC-Date=20260612T021559Z&HW-CC-Expire=86400&HW-CC-Sign=43838554BE675CF2981911DFD2DC6C3A44571F985659EA5CB31D6F4997DEFB7F "点击放大")

说明

* 预下载行为包括连接和资源下载，耗时可能超过700毫秒（取决于当前网络环境），建议开发者为预下载预留充足的时间。
* 预下载行为会消耗额外的流量和内存，建议针对高频页面使用。
* 预下载完成后，当前ArkWeb组件的连接将被关闭。如果要进行下一个页面的预连接，需要显式调用预连接接口。

**实践案例**

如下示例所示，在onPageEnd阶段，调用[prefetchPage()](<../../../../../harmonyos-references/ArkWeb（方舟Web）/ArkTS API/@ohos.web.webview (Webview)/Class (WebviewController)/arkts-apis-webview-webviewcontroller.md#prefetchpage10>)方法，即可提前下载页面所需的资源，包括主资源子资源，但不会执行网页JavaScript代码或呈现网页，以加快加载速度。

```
1. import { webview } from '@kit.ArkWeb';

3. @Entry
4. @Component
5. struct WebComponent {
6. webviewController: webview.WebviewController = new webview.WebviewController();
7. build() {
8. Column() {
9. Web({ src: 'https://www.example.com/', controller: this.webviewController})
10. .onPageEnd(() => {
11. // Pre-connected https://www.iana.org/help/example-domains
12. this.webviewController.prefetchPage('https://www.iana.org/help/example-domains');
13. })
14. }
15. }
16. }
```

[CaseFour.ets](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/LoadPerformanceInWeb/entry/src/main/ets/pages/CaseFour.ets#L2-L17)

说明

prefetchPage会缓存下载的资源，缓存时效为5分钟。

### 预渲染优化

**原理介绍**

预渲染优化适用于Web页面启动和跳转场景，例如首页跳转到子页。与预连接、预下载不同，预渲染需创建新的ArkWeb组件并进行后台预渲染，此时组件不会挂载到组件树上（状态为Hidden和InActive）。开发者可在后续按需动态挂载。

具体原理如下图所示。首先，需要定义一个自定义组件封装 ArkWeb 组件，该组件被离线创建，并包含在一个无状态的节点 NodeContainer 中，与相应的 NodeController 绑定。ArkWeb 组件在后台完成预渲染后，需要展示时，再通过 NodeController 将其挂载到 ViewTree 的 NodeContainer 中，即通过 NodeController 绑定到对应的 NodeContainer 组件。预渲染通用实现的步骤如下：

1. 创建自定义ArkWeb组件：根据实际场景创建封装，组件被离线创建。
2. 创建并绑定[NodeController](<../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS API/UI界面/arkui/NodeController/js-apis-arkui-nodecontroller.md>)：实现NodeController接口，管理节点的创建、显示、更新等操作。将NodeController对象放入容器中，等待调用。
3. 绑定[NodeContainer](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/自定义占位组件/NodeContainer/ts-basic-components-nodecontainer.md)组件：与NodeController绑定，实现动态页面显示。

**图5** 预渲染优化原理图   
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a0/v3/i53bQ3YKQLW8pwnsmxGQCw/zh-cn_image_0000002194010800.png?HW-CC-KV=V1&HW-CC-Date=20260612T021559Z&HW-CC-Expire=86400&HW-CC-Sign=B85C4378A6EA73ABE53CBDB8A9DF76115E203FF771C4641D044646BB669CB421 "点击放大")

说明

预渲染相比预下载和预连接方案，会消耗更多内存和算力，建议仅用于高频页面。单个应用后台创建的ArkWeb组件数量应少于200个。

另外，为了方便实现Web组件预渲染，开发者可以引用三方库[nodepool](https://ohpm.openharmony.cn/#/cn/detail/@hadss%2Fnodepool/v/1.0.2-rc.0)。nodepool提供了全局自定义组件复用的能力，能够更高效、更简单的实现Web组件预渲染。

**实践案例**

创建载体，并创建ArkWeb组件。

```
1. import { UIAbility } from '@kit.AbilityKit';
2. import { window } from '@kit.ArkUI';
3. // Carrier Ability
4. // EntryAbility.ets
5. import {createNWeb} from './common';
6. export default class EntryAbility extends UIAbility {
7. onWindowStageCreate(windowStage: window.WindowStage): void {
8. windowStage.loadContent('pages/Index', (err, data) => {
9. // Create ArkWeb dynamic components (need to pass in UIContext), which can be created at any time after loadContent.
10. createNWeb('https://www.example.com', windowStage.getMainWindowSync().getUIContext());
11. if (err.code) {
12. return;
13. }
14. });
15. }
16. }
```

[CreateCarrier.ets](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/LoadPerformanceInWeb/entry/src/main/ets/pages/CreateCarrier.ets#L2-L17)

创建NodeContainer和对应的NodeController，渲染后台ArkWeb组件。

```
1. // Create NodeController
2. // common.ets
3. import { UIContext } from '@kit.ArkUI';
4. import { webview } from '@kit.ArkWeb';
5. import { NodeController, BuilderNode, Size, FrameNode }  from '@kit.ArkUI';
6. import { hilog } from '@kit.PerformanceAnalysisKit';

8. const DOMAIN = 0x0000;
9. const TAG = 'Sample';

11. // Specific component contents of dynamic components in @Builder
12. // Data is a parameter encapsulation class.
13. class Data{
14. url: string = 'https://www.example.com';
15. controller: WebviewController = new webview.WebviewController();
16. }

18. let shouldInactive: boolean = true;
19. @Builder
20. function WebBuilder(data:Data) {
21. Column() {
22. Web({ src: data.url, controller: data.controller })
23. .domStorageAccess(true)
24. .zoomAccess(true)
25. .fileAccess(true)
26. .mixedMode(MixedMode.All)
27. .width('100%')
28. .height('100%')
29. .onPageBegin(() => {
30. data.controller.onActive();
31. })
32. .onPageEnd(() => {
33. hilog.info(DOMAIN, TAG, `load page end time: ${Date.now()}`);
34. })
35. .onFirstMeaningfulPaint(() =>{
36. if (!shouldInactive) {
37. return;
38. }
39. // stop render
40. data.controller.onInactive();
41. shouldInactive = false;
42. })
43. }
44. }

47. // Used to control and feedback the behavior of nodes on the corresponding NodeContainer, which needs to be used together with NodeContainer
48. export class MyNodeController extends NodeController {
49. private rootNode: BuilderNode<Data[]> | null = null;
50. private root: FrameNode | null = null;

52. // The method that must be overridden is used to build the number of nodes and return the nodes to be mounted in the corresponding NodeContainer.
53. // //Called when the corresponding NodeContainer is created, or refreshed by calling the rebuild method.
54. makeNode(uiContext: UIContext): FrameNode | null {
55. hilog.info(DOMAIN, TAG, ' uicontext is undefined : '+ (uiContext === undefined));
56. if (this.rootNode != null) {
57. const parent: FrameNode = this.rootNode.getFrameNode()?.getParent() as FrameNode;
58. if (parent) {
59. let inspectorInfo: string = JSON.stringify(parent.getInspectorInfo());
60. hilog.info(DOMAIN, TAG, inspectorInfo);
61. parent.removeChild(this.rootNode.getFrameNode());
62. this.root = null;
63. }
64. this.root = new FrameNode(uiContext);
65. this.root.appendChild(this.rootNode.getFrameNode());
66. // Returns the FrameNode node
67. return this.root;
68. }
69. // Returns a null node that controls the dynamic component to be unbound.
70. return null;
71. }
72. // Callback when layout size changes.
73. aboutToResize(size: Size): void {
74. hilog.info(DOMAIN, TAG, 'aboutToResize width : ' + size.width  +  ' height : ' + size.height);

76. }

78. // Call back when the NodeContainer corresponding to the controller is in Appear.
79. aboutToAppear(): void {
80. hilog.info(DOMAIN, TAG, 'aboutToAppear');
81. }

83. // Call back when the NodeContainer corresponding to the controller is Disappear.
84. aboutToDisappear(): void {
85. hilog.info(DOMAIN, TAG, 'aboutToDisappear');
86. }

88. // This function is a user-defined function and can be used as an initialization function.
89. // Initialize builderNode through UIContext, and then initialize the contents in @Builder through the Build interface in BuilderNode.
90. initWeb(url:string, uiContext:UIContext, control:WebviewController): void {
91. if(this.rootNode != null)
92. {
93. return;
94. }
95. // Creating a node requires uiContext.
96. this.rootNode = new BuilderNode(uiContext)
97. // Create dynamic Web components
98. this.rootNode.build(wrapBuilder<Data[]>(WebBuilder), { url:url, controller:control })
99. }
100. }

102. // Create the NodeController needed for Map saving.
103. let NodeMap:Map<string, MyNodeController | undefined> = new Map();
104. // Create WebViewController needed for Map saving.
105. let controllerMap:Map<string, WebviewController | undefined> = new Map();

107. // Initialization requires UIContext to be obtained in Ability.
108. export const createNWeb = (url: string, uiContext: UIContext) => {
109. // Create NodeController
110. let baseNode: MyNodeController = new MyNodeController();
111. let controller: WebviewController = new webview.WebviewController() ;
112. // Initialize a custom web component
113. baseNode.initWeb(url, uiContext, controller);
114. controllerMap.set(url, controller)
115. NodeMap.set(url, baseNode);
116. }

118. // Customize to get the NodeController interface.
119. export const getNWeb = (url : string) : MyNodeController | undefined => {
120. return NodeMap.get(url);
121. }
```

[CreateNodeController.ets](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/LoadPerformanceInWeb/entry/src/main/ets/pages/CreateNodeController.ets#L2-L122)

通过NodeContainer使用已经预渲染的页面。

```
1. // Use the Page page of NodeController.
2. // Index.ets
3. import {getNWeb} from './common';

5. @Entry
6. @Component
7. struct Index {
8. build() {
9. Row() {
10. Column() {
11. // NodeContainer is used to bind with NodeController node, and rebuild will trigger makeNode.
12. // Page page is bound to NodeController through NodeContainer interface to realize dynamic component page display.
13. NodeContainer(getNWeb('https://www.example.com'))
14. .height('90%')
15. .width('100%')
16. }
17. .width('100%')
18. }
19. .height('100%')
20. }
21. }
```

[UseNodeController.ets](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/LoadPerformanceInWeb/entry/src/main/ets/pages/UseNodeController.ets#L2-L22)

### 预取POST请求优化

**原理介绍**

预取POST请求适用于Web页面启动和跳转场景。当即将加载的Web页面中存在耗时较长的POST请求时，可以选择在不同时机进行预取，以消除等待POST请求数据下载完成的耗时。具体有以下两种场景可供参考：

1. 如果是应用首页，推荐在ArkWeb组件创建后或提前初始化Web内核后，对首页的POST请求进行预取，例如在XComponent.onCreate()或自定义组件的生命周期函数aboutToAppear()中。
2. 当前页面加载完成后，可以对用户下一步可能点击的页面的POST请求进行预取，推荐在Web组件的生命周期函数onPageEnd()及后续时机进行。

说明

1. 本方案能消除POST请求下载的耗时，预计收益在100毫秒左右，具体取决于POST请求的数据内容和当前网络环境。
2. 预取POST请求行为包括连接和资源下载。连接和资源加载耗时可能达到数百毫秒，具体取决于POST请求的数据内容和当前网络环境。建议为预下载留出足够的时间。
3. 预取POST请求会消耗额外的流量和内存，建议仅用于高频页面。
4. POST请求具有即时性，预取POST请求需指定有效期。
5. 目前仅支持预取Content-Type为application/x-www-form-urlencoded的POST请求，最多预取6个。预取第7个时，会自动清除最早预取的POST缓存。也可以通过clearPrefetchedResource()接口主动清除不再使用的预取资源缓存。
6. 如果要使用预获取的资源缓存，开发者需要在正式发起的POST请求的请求头中添加“ArkWebPostCacheKey”，其值为对应缓存的cacheKey。

**实践案例**

案例一：加载包含POST请求的首页。

说明

预取POST不会影响首页加载时间。

【不推荐用法】

当首页包含POST请求，并且该请求耗时较长时，不建议直接加载Web页面。

```
1. import { webview } from '@kit.ArkWeb';

3. @Entry
4. @Component
5. struct WebComponent {
6. webviewController: webview.WebviewController = new webview.WebviewController();

8. build() {
9. Column() {
10. Web({ src: 'https://www.example.com/', controller: this.webviewController })
11. }
12. }
13. }
```

[WebComponent.ets](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/LoadPerformanceInWeb/entry/src/main/ets/pages/WebComponent.ets#L2-L14)

【推荐用法】

预取POST请求以加载首页，具体步骤如下：

1. 通过initializeWebEngine()来提前初始化Web组件的内核，然后在初始化内核后调用prefetchResource()预获取将要加载页面中的POST请求。

   ```
   1. import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
   2. import { webview } from '@kit.ArkWeb';
   3. import { hilog } from '@kit.PerformanceAnalysisKit';

   5. const DOMAIN = 0x0000;
   6. const TAG = 'Sample';

   8. export default class EntryAbility extends UIAbility {
   9. // EntryAbility.ets
   10. onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
   11. hilog.info(DOMAIN, TAG, 'EntryAbility onCreate.');
   12. webview.WebviewController.initializeWebEngine();
   13. // When pre-acquiring, 'https://www.example1.com/POST? E=f&g=h' is replaced by the actual website address to be visited.
   14. webview.WebviewController.prefetchResource(
   15. {
   16. url: 'https://www.example.com/POST?e=f&g=h',
   17. method: 'POST',
   18. formData: 'a=x&b=y'
   19. },
   20. [{
   21. headerKey: 'c',
   22. headerValue: 'z'
   23. }],
   24. 'KeyX', 500
   25. );
   26. AppStorage.setOrCreate('abilityWant', want);
   27. hilog.info(DOMAIN, TAG, 'EntryAbility onCreate done.');
   28. }
   29. // ...
   30. }
   ```

   [PrefetchResource.ets](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/LoadPerformanceInWeb/entry/src/main/ets/pages/PrefetchResource.ets#L2-L31)
2. 通过Web组件加载包含POST请求的页面。

   ```
   1. import { webview } from '@kit.ArkWeb';

   3. @Entry
   4. @Component
   5. struct WebComponent {
   6. webviewController: webview.WebviewController = new webview.WebviewController();

   8. build() {
   9. Column() {
   10. Web({ src: 'https://www.example.com/', controller: this.webviewController })
   11. .onPageEnd(() => {
   12. // Clear the cache of pre-acquired resources that are no longer used in the future.
   13. webview.WebviewController.clearPrefetchedResource(['KeyX']);
   14. })
   15. }
   16. }
   17. }
   ```

   [ClearResourceCache.ets](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/LoadPerformanceInWeb/entry/src/main/ets/pages/ClearResourceCache.ets#L2-L18)
3. 在页面加载的JavaScript文件中，发起POST请求，并将请求响应头ArkWebPostCacheKey设置为预取时的cachekey值'KeyX'。

   ```
   1. const xhr = new XMLHttpRequest();
   2. xhr.open('POST', 'https://www.example.com/POST?e=f&g=h', true);
   3. xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
   4. xhr.setRequestHeader('ArkWebPostCacheKey', 'KeyX');
   5. xhr.onload = function () {
   6. if (xhr.status >= 200 && xhr.status < 300) {
   7. console.log('成功', xhr.responseText);
   8. } else {
   9. console.error('请求失败');
   10. }
   11. }
   12. const formData = new FormData();
   13. formData.append('a', 'x');
   14. formData.append('b', 'y');
   15. xhr.send(formData);
   ```

   [HttpRequestPost.js](https://gitcode.com/HarmonyOS_Samples/BestPracticeSnippets/blob/master/LoadPerformanceInWeb/entry/src/main/ets/utils/HttpRequestPost.js#L2-L16)

案例二：加载包含POST请求的下一页。

【不推荐用法】

当即将加载的Web页面中包含POST请求，并且POST请求耗时较长时，不建议直接加载Web页面。

```
1. import { webview } from '@kit.ArkWeb';

3. @Entry
4. @Component
5. struct WebComponent {
6. webviewController: webview.WebviewController = new webview.WebviewController();

8. build() {
9. Column() {
10. Button('加载页面')
11. .onClick(() => {
12. this.webviewController.loadUrl('https://www.example1.com/');
13. })
14. Web({ src: 'https://www.example.com/', controller: this.webviewController })
15. }
16. }
17. }
```

[WebComponentLoad.ets](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/LoadPerformanceInWeb/entry/src/main/ets/pages/WebComponentLoad.ets#L2-L18)

【推荐用法】

通过预取POST加载包含POST请求的下一个跳转页面。

1. 当前页面显示完成后，使用onPageEnd()预获取即将加载页面中的POST请求。

   ```
   1. import { hiTraceMeter } from '@kit.PerformanceAnalysisKit';
   2. import { webview } from '@kit.ArkWeb';

   4. @Entry
   5. @Component
   6. struct WebComponent {
   7. controller: webview.WebviewController = new webview.WebviewController();
   8. webviewController: webview.WebviewController = new webview.WebviewController();

   10. build() {
   11. Column() {
   12. // Load the business Web component at an appropriate time. This example takes the Button click trigger as an example.
   13. Button('加载页面')
   14. .onClick(() => {
   15. // Performance dot
   16. hiTraceMeter.startTrace('getMessageData', 1);
   17. // Please replace the URL with the real address.
   18. this.controller.loadUrl('https://www.example1.com/');
   19. })
   20. Web({ src: 'https://www.example.com/', controller: this.webviewController })
   21. .onPageEnd(() => {
   22. // When pre-acquiring, 'https://www.example1.com/POST? E=f&g=h' is replaced by the actual website address to be visited.
   23. webview.WebviewController.prefetchResource(
   24. {
   25. url: 'https://www.example1.com/POST?e=f&g=h',
   26. method: 'POST',
   27. formData: 'a=x&b=y'
   28. },
   29. [{
   30. headerKey: 'c',
   31. headerValue: 'z'
   32. }],
   33. 'KeyX', 500
   34. );
   35. })
   36. }
   37. }
   38. }
   ```

   [LoadWebComponentRight.ets](https://gitcode.com/HarmonyOS_Samples/BestPracticeSnippets/blob/master/LoadPerformanceInWeb/entry/src/main/ets/pages/LoadWebComponentRight.ets#L2-L39)
2. 在将要加载的页面中，JavaScript发起POST请求，并将请求响应头ArkWebPostCacheKey设置为预取时设置的cachekey值'KeyX'。

   ```
   1. const xhr = new XMLHttpRequest();
   2. xhr.open('POST', 'https://www.example.com/POST?e=f&g=h', true);
   3. xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
   4. xhr.setRequestHeader('ArkWebPostCacheKey', 'KeyX');
   5. xhr.onload = function () {
   6. if (xhr.status >= 200 && xhr.status < 300) {
   7. console.log('成功', xhr.responseText);
   8. } else {
   9. console.error('请求失败');
   10. }
   11. }
   12. const formData = new FormData();
   13. formData.append('a', 'x');
   14. formData.append('b', 'y');
   15. xhr.send(formData);
   ```

   [HttpRequestPost.js](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/LoadPerformanceInWeb/entry/src/main/ets/utils/HttpRequestPost.js#L2-L16)

### 预编译JavaScript生成字节码缓存（Code Cache）

**原理介绍**

预编译JavaScript生成字节码缓存，可以在页面加载前将即将使用的JavaScript文件编译为字节码并缓存到本地，从而在页面首次加载时减少编译时间。

创建一个无需渲染的离线Web组件，用于预编译。预编译结束后，使用其他Web组件加载业务网页。

说明

建议开发者优先使用[Code Linter扫描工具](<../../../../../harmonyos-guides/编写与调试应用/代码编辑/代码检查/Code Linter代码检查/ide-code-linter.md>)进行代码检查，重点关注[@performance/js-code-cache-by-precompile-check](<../../../../../harmonyos-guides/编写与调试应用/代码编辑/代码检查/Code Linter代码检查规则/性能规则@performance/@performancejs-code-cache-by-precompile-check/ide-js-code-cache-by-precompile-check.md>)规则。若扫描结果中出现该规则相关问题，可参考本章节提供的优化建议进行调整。

1. 仅HTTP或HTTPS协议请求的JavaScript文件可以预编译。
2. 不支持ES6 Module语法的JavaScript文件生成预编译字节码缓存。
3. 通过配置响应头中的E-Tag和Last-Modified值来标记JavaScript缓存版本，当这些值发生变化时，更新字节码缓存。
4. 不支持本地JavaScript文件预编译缓存。

**实践案例**

案例一：在未使用预编译JavaScript前提下，启动加载Web页面

```
1. import { webview } from '@kit.ArkWeb';
2. import { hilog, hiTraceMeter } from '@kit.PerformanceAnalysisKit';

4. const DOMAIN = 0x0000;
5. const TAG = 'Sample';

7. @Entry
8. @Component
9. struct Index {
10. controller: webview.WebviewController = new webview.WebviewController();

12. build() {
13. Column() {
14. // Load the business Web component at an appropriate time. This example takes the Button click trigger as an example.
15. Button('加载页面')
16. .onClick(() => {
17. // Performance dot
18. hiTraceMeter.startTrace('unPrecompileJavaScript', 1);
19. // Please replace the URL with the real address.
20. this.controller?.loadUrl('https://www.example.com/b.html');
21. })
22. Web({ src: 'https://www.example.com/a.html', controller: this.controller })
23. .fileAccess(true)
24. .onPageBegin((event) => {
25. hilog.info(DOMAIN, TAG, `load page begin: ${event?.url}`);
26. })
27. .onPageEnd((event) => {
28. // Performance dot
29. hiTraceMeter.finishTrace('unPrecompileJavaScript', 1);
30. hilog.info(DOMAIN, TAG, `load page end: ${event?.url}`);
31. })
32. }
33. }
34. }
```

[PracticalCaseOne.ets](https://gitcode.com/HarmonyOS_Samples/BestPracticeSnippets/blob/master/LoadPerformanceInWeb/entry/src/main/ets/pages/PracticalCaseOne.ets#L2-L35)

点击“加载页面”按钮，[性能打点](<../../../../../harmonyos-references/Performance Analysis Kit（性能分析服务）/ArkTS API/@ohos.hiTraceMeter (性能打点)/js-apis-hitracemeter.md>)数据如下，getMessageData进程中的Duration为加载页面开始到结束的耗时：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/09/v3/eXfUzRWRS-i__l38wZvWIw/zh-cn_image_0000002193851232.png?HW-CC-KV=V1&HW-CC-Date=20260612T021559Z&HW-CC-Expire=86400&HW-CC-Sign=6F2606F6378F0F84755B9E06CE116673C5334115416A1E1D16C184D6972F7660 "点击放大")

说明

JavaScript的编译时间受文件大小和逻辑复杂度的影响。

案例二：使用预编译JavaScript生成字节码缓存，具体步骤如下：

1. 配置预编译的JavaScript文件信息。

   ```
   1. import { webview } from '@kit.ArkWeb';
   2. import { hilog } from '@kit.PerformanceAnalysisKit';

   4. const DOMAIN = 0x0000;
   5. const TAG = 'Sample';

   7. interface Config {
   8. url: string,
   9. localPath: string, // local resource path
   10. options: webview.CacheOptions
   11. }

   13. @Entry
   14. @Component
   15. struct Index {
   16. controller: webview.WebviewController = new webview.WebviewController();
   17. // Configure precompiled JavaScript file information
   18. configs: Array<Config> = [
   19. {
   20. url: 'https://www.example.com/example.js',
   21. localPath: 'example.js',
   22. options: {
   23. responseHeaders: [
   24. { headerKey: 'E-Tag', headerValue: 'xxx' },
   25. { headerKey: 'Last-Modified', headerValue: 'Web, 21 Mar 2024 10:38:41 GMT' }
   26. ]
   27. }
   28. }
   29. ]

   31. // ...
   32. }
   ```

   [PracticalCaseTwo.ets](https://gitcode.com/HarmonyOS_Samples/BestPracticeSnippets/blob/master/LoadPerformanceInWeb/entry/src/main/ets/pages/PracticalCaseTwo.ets#L2-L58)
2. 读取配置，进行预编译。

   ```
   1. Web({ src: 'https://www.example.com/a.html', controller: this.controller })
   2. .onControllerAttached(async () => {
   3. // Read the configuration and precompile.
   4. for (const config of this.configs) {
   5. this.getUIContext()
   6. .getHostContext()?.resourceManager.getRawFileContent(config.localPath)
   7. .then((content: Uint8Array) => {
   8. this.controller.precompileJavaScript(config.url, content, config.options)
   9. .then(() => {
   10. hilog.info(DOMAIN, TAG, 'precompile successfully!');
   11. }).catch((errCode: number) => {
   12. hilog.error(DOMAIN, TAG, 'precompile failed.' + errCode);
   13. })
   14. }).catch(() => {
   15. hilog.error(DOMAIN, TAG, 'precompile failed!.');
   16. })
   17. }
   18. })
   ```

   [PracticalCaseTwo.ets](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/LoadPerformanceInWeb/entry/src/main/ets/pages/PracticalCaseTwo.ets#L36-L53)

   点击“加载页面”按钮，性能打点数据如下：getMessageData进程中的Duration表示加载页面从开始到结束的耗时。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c7/v3/zkZeI9uLQMC1N5Q6Kr9zQw/zh-cn_image_0000002229336625.png?HW-CC-KV=V1&HW-CC-Date=20260612T021559Z&HW-CC-Expire=86400&HW-CC-Sign=11888AD5BF34FF7453873971ECC2E1AAAC66ECC7B53BDAB6ABFB40F3C8054D76)

   说明

   当需要更新本地已生成的编译字节码时，修改cacheOptions参数中responseHeaders的E-Tag或Last-Modified响应头对应的值，再次调用接口即可。

**总结**

**表2**

| 页面加载方式 | 耗时(局限不同设备和场景，数据仅供参考) | 说明 |
| --- | --- | --- |
| 直接加载Web页面 | 3183ms | 页面加载时才进行JavaScript编译，从而增加了加载时间 |
| 预编译JavaScript生成字节码缓存 | 268ms | 在加载页面前完成JavaScript预编译，从而节省了首次加载的编译时间 |

### 资源拦截替换的JavaScript生成字节码缓存（Code Cache）

**原理介绍**

资源拦截替换的JavaScript生成字节码缓存适用于页面加载时需要加载网络JavaScript文件并进行拦截替换的场景。此功能支持将字节码缓存到本地，从而在页面非首次加载时节省编译时间。

说明

建议开发者优先使用[Code Linter扫描工具](<../../../../../harmonyos-guides/编写与调试应用/代码编辑/代码检查/Code Linter代码检查/ide-code-linter.md>)进行代码检查，重点关注[@performance/js-code-cache-by-interception-check](<../../../../../harmonyos-guides/编写与调试应用/代码编辑/代码检查/Code Linter代码检查规则/性能规则@performance/@performancejs-code-cache-by-interception-check/ide-js-code-cache-by-interception-check.md>)规则。若扫描结果中出现该规则相关问题，可参考本章节提供的优化建议进行调整

**图6** JS资源编译执行流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/65/v3/qS4qsKp7TCqr-8cV0NykhQ/zh-cn_image_0000002193851224.png?HW-CC-KV=V1&HW-CC-Date=20260612T021559Z&HW-CC-Expire=86400&HW-CC-Sign=42E2781EB36E7E1E34604E02F1ADDBE8BA65EB85CAA1287257217F75E847BFEE "点击放大")

**图7** 资源拦截替换后JS资源编译执行流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1e/v3/X5p9cQ9TSQCJt-Wt1rZuOg/zh-cn_image_0000002194010828.png?HW-CC-KV=V1&HW-CC-Date=20260612T021559Z&HW-CC-Expire=86400&HW-CC-Sign=42CFC1DFFAE964DA8DA377EACFFDA89C26D274EB4CCCE8D1A2E8511ED665F7DF "点击放大")

Web组件默认支持HTTP协议和自定义协议的JavaScript生成字节码缓存。具体步骤如下：

1. 开发者需要在Web组件运行前注册自定义协议。
2. 拦截自定义协议的JavaScript，设置ResponseData和ResponseDataID。

说明

ResponseData为JavaScript内容，ResponseDataID用于区分内容是否变更。内容变更时，ResponseDataID也需要变更。

**实践案例**

案例一：拦截HTTP协议的JavaScript文件，生成字节码缓存。

【不推荐用法】

不设置ResponseDataID，直接加载Web界面。

1. 构造前端H5界面

   ```
   1. <!DOCTYPE html>
   2. <html lang="en">
   3. <head>
   4. <meta charset="UTF-8">
   5. <meta name="viewport"
   6. content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
   7. <meta http-equiv="X-UA-Compatible" content="ie=edge">
   8. <title>Document</title>
   9. </head>
   10. <body>
   11. <div id="div-1">this is a test div</div>
   12. <div id="div-2">this is a test div</div>
   13. <div id="div-3">this is a test div</div>
   14. <div id="div-4">this is a test div</div>
   15. <div id="div-5">this is a test div</div>
   16. <div id="div-6">this is a test div</div>
   17. <div id="div-7">this is a test div</div>
   18. <div id="div-8">this is a test div</div>
   19. <div id="div-9">this is a test div</div>
   20. <div id="div-10">this is a test div</div>
   21. <div id="div-11">this is a test div</div>
   22. </body>
   23. <script src="https://www.example.com/test.js"></script>
   24. </html>
   ```

   [index.html](https://gitcode.com/HarmonyOS_Samples/BestPracticeSnippets/blob/master/LoadPerformanceInWeb/entry/src/main/resources/rawfile/index.html#L2-L25)
2. 不设置ResponseDataID，进行界面请求拦截替换

   ```
   1. import { webview } from '@kit.ArkWeb';
   2. import { hiTraceMeter } from '@kit.PerformanceAnalysisKit';

   4. @Entry
   5. @Component
   6. struct Index {
   7. webViewController: webview.WebviewController = new webview.WebviewController();
   8. responseResource: WebResourceResponse = new WebResourceResponse();
   9. // The developer defines the response data, and the length of the response data must be greater than or equal to 1024 to generate CodeCache.
   10. @State jsData: string = 'JavaScript Data';

   12. build() {
   13. Column() {
   14. Web({ src: $rawfile('index.html'), controller: this.webViewController })
   15. .onInterceptRequest(event => {
   16. // Intercept page requests
   17. if (event?.request.getRequestUrl() === 'https://www.example.com/test.js') {
   18. // Construct response data
   19. this.responseResource.setResponseData(this.jsData);
   20. this.responseResource.setResponseEncoding('utf-8');
   21. this.responseResource.setResponseMimeType('application/javascript');
   22. this.responseResource.setResponseCode(200);
   23. this.responseResource.setReasonMessage('OK');
   24. return this.responseResource;
   25. }
   26. return null;
   27. })
   28. .onPageBegin(() => {
   29. hiTraceMeter.startTrace('getMessageData', 0);
   30. })
   31. .onPageEnd(() => {
   32. hiTraceMeter.finishTrace('getMessageData', 0);
   33. })
   34. }
   35. .width('100%')
   36. }
   37. }
   ```

   [PageRequestInterception.ets](https://gitcode.com/HarmonyOS_Samples/BestPracticeSnippets/blob/master/LoadPerformanceInWeb/entry/src/main/ets/pages/PageRequestInterception.ets#L2-L38)

打开应用后关闭，重复两次，然后查看第三次页面加载的耗时。性能打点数据如下：getMessageData 进程中的 Duration 表示页面加载从开始到结束的耗时。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/47/v3/WguNFEibRVyNbSWfh64Eyg/zh-cn_image_0000002229451101.png?HW-CC-KV=V1&HW-CC-Date=20260612T021559Z&HW-CC-Expire=86400&HW-CC-Sign=FE56A91477B9DD7DBA15409A0B53BDFC498A2304E1CB47D6AEF2F23B40ED80DB)

【推荐用法】

在进行资源拦截替换时，设置请求头中的ResponseData和ResponseDataID。

```
1. import { webview } from '@kit.ArkWeb';
2. import { hiTraceMeter } from '@kit.PerformanceAnalysisKit';

4. @Entry
5. @Component
6. struct Index {
7. controller: webview.WebviewController = new webview.WebviewController();
8. responseResource: WebResourceResponse = new WebResourceResponse();
9. // Construct response data
10. @State jsData: string = 'JavaScript Data';

12. build() {
13. Column() {
14. Web({ src: $rawfile('index.html'), controller: this.controller })
15. .onInterceptRequest((event) => {
16. // Intercept page requests
17. if (event?.request.getRequestUrl() === 'https://www.example.com/test.js') {
18. // Construct response data
19. this.responseResource.setResponseHeader([
20. {
21. // Format: No more than 13 digits. Js ID, this field must be updated when Js is updated.
22. headerKey: 'ResponseDataID',
23. headerValue: '0000000000001'
24. }]);
25. this.responseResource.setResponseData(this.jsData);
26. this.responseResource.setResponseEncoding('utf-8');
27. this.responseResource.setResponseMimeType('application/javascript');
28. this.responseResource.setResponseCode(200);
29. this.responseResource.setReasonMessage('OK');
30. return this.responseResource;
31. }
32. return null;
33. })
34. .onPageBegin(() => {
35. hiTraceMeter.startTrace('getMessageData', 0);
36. })
37. .onPageEnd(() => {
38. hiTraceMeter.finishTrace('getMessageData', 0);
39. })
40. }
41. }
42. }
```

[SetResposeData.ets](https://gitcode.com/HarmonyOS_Samples/BestPracticeSnippets/blob/master/LoadPerformanceInWeb/entry/src/main/ets/pages/SetResposeData.ets#L2-L43)

打开应用后关闭，重复两次，然后查看第三次页面加载的耗时。性能打点数据如下：getMessageData 进程中的 Duration 表示页面加载从开始到结束的耗时。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a0/v3/ymdZku3YTHiCAV8EHjphUQ/zh-cn_image_0000002193851248.png?HW-CC-KV=V1&HW-CC-Date=20260612T021559Z&HW-CC-Expire=86400&HW-CC-Sign=6310C93D0C7AC4424CC834DFA34415B0E434E75F10DE64CAED1BA4C20D49499B)

案例二：调用ArkTS接口customizeSchemes()，在注册自定义协议的情况下，实现JavaScript生成字节码缓存，具体步骤如下：

1. 将scheme对象的isCodeCacheSupported属性设置为true，支持自定义协议的JavaScript生成字节码缓存

   ```
   1. scheme1: webview.WebCustomScheme = { schemeName: "scheme1", isSupportCORS: true, isSupportFetch: true, isCodeCacheSupported: true }
   ```

   [ByteCodeCache.ets](https://gitcode.com/HarmonyOS_Samples/BestPracticeSnippets/blob/master/LoadPerformanceInWeb/entry/src/main/ets/pages/ByteCodeCache.ets#L11-L11)
2. 在Web组件运行前，向Web组件注册自定义协议。

   说明

   请确保自定义协议不与Web内核内置协议相同。

   ```
   1. aboutToAppear(): void {
   2. try {
   3. webview.WebviewController.customizeSchemes([this.scheme1])
   4. } catch (error) {
   5. let e: business_error.BusinessError = error as business_error.BusinessError;
   6. hilog.error(DOMAIN, TAG, `ErrorCode: ${e.code},  Message: ${e.message}`);
   7. }
   8. }
   ```

   [ByteCodeCache.ets](https://gitcode.com/HarmonyOS_Samples/BestPracticeSnippets/blob/master/LoadPerformanceInWeb/entry/src/main/ets/pages/ByteCodeCache.ets#L18-L25)
3. 拦截自定义协议的JavaScript，设置ResponseData和ResponseDataID。ResponseData包含JavaScript内容，ResponseDataID用于标识JavaScript内容是否发生变化。

   说明

   若JavaScript内容变更，ResponseDataID需要一起变更

   ```
   1. Web({
   2. src: $rawfile('index.html'),
   3. controller: this.webController
   4. })
   5. .fileAccess(true)
   6. .javaScriptAccess(true)
   7. .width('100%')
   8. .height('100%')
   9. .onConsole((event) => {
   10. hilog.info(DOMAIN, TAG, 'ets onConsole:' + event?.message.getMessage());
   11. return false
   12. })
   13. .onInterceptRequest((event) => {
   14. let responseResource = new WebResourceResponse()
   15. // Intercept page requests
   16. if (event?.request.getRequestUrl() == 'https://www.intercept.com/test-cc.js') {
   17. // Construct response data
   18. responseResource.setResponseHeader([
   19. {
   20. headerKey: 'ResponseDataID',
   21. headerValue: '0000000000002'
   22. // Format: No more than 13 digits. Js ID, this field must be updated when Js is updated.
   23. }]);
   24. responseResource.setResponseData(this.jsData);
   25. responseResource.setResponseEncoding('utf-8');
   26. responseResource.setResponseMimeType('application/javascript');
   27. responseResource.setResponseCode(200);
   28. responseResource.setReasonMessage('OK');
   29. return responseResource;

   32. }
   33. if (event?.request.getRequestUrl() == 'scheme1://www.intercept.com/test-cc2.js') {
   34. // Construct response data
   35. responseResource.setResponseHeader([
   36. {
   37. headerKey: 'ResponseDataID',
   38. headerValue: '0000000000001'
   39. // Format: No more than 13 digits. Js ID, this field must be updated when Js is updated.
   40. }]);
   41. responseResource.setResponseData(this.jsData2);
   42. responseResource.setResponseEncoding('utf-8');
   43. responseResource.setResponseMimeType('application/javascript');
   44. responseResource.setResponseCode(200);
   45. responseResource.setReasonMessage('OK');
   46. return responseResource;
   47. }
   48. return null;
   49. })
   ```

   [ByteCodeCache.ets](https://gitcode.com/HarmonyOS_Samples/BestPracticeSnippets/blob/master/LoadPerformanceInWeb/entry/src/main/ets/pages/ByteCodeCache.ets#L31-L79)

案例三：调用Native接口 `int32\_t OH\_ArkWeb\_RegisterCustomSchemes(const char \*scheme, int32\_t option)`，实现自定义协议的JavaScript生成字节码缓存。通过网络拦截接口拦截Web组件发出的请求。示例代码请参考[拦截Web组件发起的网络请求](../../../../../harmonyos-guides/应用框架/ArkWeb（方舟Web）/管理网页加载与浏览记录/拦截Web组件发起的网络请求/web-scheme-handler.md)。具体步骤如下：

1. 注册三方协议配置时，传入 `ARKWEB\_SCHEME\_OPTION\_CODE\_CACHE\_ENABLED` 参数。

   ```
   1. // register Custom Schemes before web initialized
   2. static napi_value RegisterCustomSchemes(napi_env env, napi_callback_info info) {
   3. OH_LOG_INFO(LOG_APP, "register custom schemes");
   4. OH_ArkWeb_RegisterCustomSchemes("custom", ARKWEB_SCHEME_OPTION_STANDARD | ARKWEB_SCHEME_OPTION_CORS_ENABLED | ARKWEB_SCHEME_OPTION_CODE_CACHE_ENABLED);
   5. return nullptr;
   6. }
   ```

   [nnapi\_init.cpp](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/LoadPerformanceInWeb/entry/src/main/cpp/nnapi_init.cpp#L2-L7)
2. 设置ResponseDataID。

   ```
   1. // Read Rawfile Data On Worker Thread
   2. void RawfileRequest::ReadRawfileDataOnWorkerThread() {
   3. OH_LOG_INFO(LOG_APP, "read rawfile in worker thread.");
   4. const struct UrlInfo {
   5. std::string resource;
   6. std::string mimeType;
   7. } urlInfos[] = {{"local.html", "text/html"},
   8. {"local_script.js", "text/javascript"},
   9. {"test-cc.js", "text/javascript"}
   10. };

   13. if (!resourceManager()) {
   14. OH_LOG_ERROR(LOG_APP, "read rawfile error, resource manager is nullptr.");
   15. return;
   16. }

   19. RawFile *rawfile = OH_ResourceManager_OpenRawFile(resourceManager(), rawfilePath().c_str());
   20. if (!rawfile) {
   21. OH_ArkWebResponse_SetStatus(response(), 404);
   22. } else {
   23. OH_ArkWebResponse_SetStatus(response(), 200);
   24. }

   27. for (auto &urlInfo : urlInfos) {
   28. if (urlInfo.resource == rawfilePath()) {
   29. OH_ArkWebResponse_SetMimeType(response(), urlInfo.mimeType.c_str());
   30. break;
   31. }
   32. }

   35. if ("test-cc.js" == rawfilePath()) {
   36. OH_LOG_ERROR(LOG_APP, "OH_ArkWebResponse_SetHeaderByName ResponseDataID");
   37. OH_ArkWebResponse_SetHeaderByName(response(), "ResponseDataID", "0000000000001", true);
   38. }
   39. OH_ArkWebResponse_SetCharset(response(), "UTF-8");
   40. }
   ```

   [nnapi\_init.cpp](https://gitcode.com/HarmonyOS_Samples/BestPracticeSnippets/blob/master/LoadPerformanceInWeb/entry/src/main/cpp/nnapi_init.cpp#L11-L50)
3. 注册三方协议并设置SchemeHandler。

   ```
   1. // EntryAbility.ets
   2. onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
   3. // register CustomSchemes
   4. testNapi.registerCustomSchemes();
   5. // initializeWebEngine
   6. webview.WebviewController.initializeWebEngine();
   7. // set SchemeHandler。
   8. testNapi.setSchemeHandler();
   9. }
   ```

   [SetSchemeHandler.ets](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/LoadPerformanceInWeb/entry/src/main/ets/pages/SetSchemeHandler.ets#L8-L16)

   性能打点数据如下，getMessageData进程中的Avg Wall Duration为两次加载页面开始到结束的平均耗时：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ec/v3/ujRAovpfTfC_2q8wHKvz9Q/zh-cn_image_0000002193851216.png?HW-CC-KV=V1&HW-CC-Date=20260612T021559Z&HW-CC-Expire=86400&HW-CC-Sign=3E444794761D4762CB2BB90B22A090382AD79816B378B06C6D9EAB7C82760717 "点击放大")

**总结****（以拦截替换HTTP协议的JavaScript生成字节码缓存场景性能数据举例）**

构造2.4MB大小的JavaScript文件，进行资源拦截替换，多次测试取平均耗时，具体数据如下：

| 资源拦截替换方式 | 耗时（数据基于特定设备和场景，仅供参考） | 说明 |
| --- | --- | --- |
| 在资源拦截替换中不设置ResponseDataID | 1469.7ms | 每次页面加载时，编译并缓存JavaScript资源，会增加加载时间。 |
| 在资源拦截替换中设置ResponseDataID | 1402.9ms | 在页面加载时，将字节码缓存至本地并设置ResponseDataID，避免后续重复缓存，节省非首次加载时间。 |

### 离线资源免拦截注入

**原理介绍**

页面加载前，离线资源免拦截注入会将图片、样式表和脚本资源注入内存缓存，节省首次加载的网络请求时间。

说明

1. 开发者需创建一个离线Web组件，用于将资源注入内存缓存，以便其他Web组件加载对应的业务网页。
2. 仅使用HTTP或HTTPS协议请求的资源可被注入进内存缓存。
3. 内存缓存中的资源由内核自动管理。当注入的资源数量过多导致内存压力增大时，内核会自动释放未使用的资源。应避免注入过多资源到内存缓存中。
4. 正常情况下，资源的有效期由提供的Cache-Control或Expires响应头控制。默认的有效期为86400秒，即1天。
5. 资源的MIMEType通过提供的参数中的Content-Type响应头配置，Content-Type需符合标准，否则无法正常使用，MODULE\_JS必须提供有效的MIMEType，其他类型可不提供。
6. 仅支持通过HTML标签加载。
7. 如果业务网页中的script标签使用了crossorigin属性，需在接口的responseHeaders参数中设置Cross-Origin响应头的值为anonymous或use-credentials。
8. 当调用 `webview.WebviewController.SetRenderProcessMode(web\_webview.RenderProcessMode.MULTIPLE)` 接口后，应用会启动多渲染进程模式，此方案在该场景下无效。
9. 单次调用最大支持注入30个资源，单个资源最大支持10MB。

**实践案例**

案例一：直接加载Web页面

```
1. import { webview } from '@kit.ArkWeb';
2. import { hiTraceMeter } from '@kit.PerformanceAnalysisKit';

4. @Entry
5. @Component
6. struct Index {
7. controller: webview.WebviewController = new webview.WebviewController();

10. build() {
11. Column() {
12. // Load business web components at the right time. This example is the example of Button click trigger.
13. Button('加载页面')
14. .onClick(() => {
15. // Performance hit point
16. hiTraceMeter.startTrace('getMessageData', 1);
17. this.controller.loadUrl('https://www.example.com/b.html');
18. })
19. Web({ src: 'https://www.example.com/a.html', controller: this.controller })
20. .fileAccess(true)
21. .onPageEnd(() => {
22. // Performance hit point
23. hiTraceMeter.finishTrace('getMessageData', 1);
24. })
25. }
26. }
27. }
```

[LoadWebPage.ets](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/LoadPerformanceInWeb/entry/src/main/ets/pages/LoadWebPage.ets#L2-L28)

性能打点数据如下，getMessageData进程中的Duration为加载页面开始到结束的耗时：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/83/v3/UIba6BA9RBmmJb9YYjx6rg/zh-cn_image_0000002229336641.png?HW-CC-KV=V1&HW-CC-Date=20260612T021559Z&HW-CC-Expire=86400&HW-CC-Sign=792495C65FAA07585970FF480578C3CBC3C45260DB2B78F27662FB79FD5AA091)

案例二：使用资源免拦截注入加载Web页面，请参考以下步骤：

1. 创建资源配置

   ```
   1. import { webview } from '@kit.ArkWeb';
   2. import { hilog } from '@kit.PerformanceAnalysisKit';

   4. const DOMAIN = 0x0000;
   5. const TAG = 'Sample';

   7. export interface ResourceConfig {
   8. urlList: Array<string>,
   9. type: webview.OfflineResourceType,
   10. responseHeaders: Array<Header>,
   11. localPath: string,
   12. }

   15. export interface ExceptionResource {
   16. console: string,
   17. urlList: Array<string> | undefined | null;
   18. type: webview.OfflineResourceType  | undefined | null,
   19. responseHeaders: Array<Header> | undefined | null,
   20. resource?: Uint8Array | undefined | null
   21. localPath?: string,
   22. }

   25. export const baseURL: string = 'http://localhost:8083/resource/';
   26. export const baseURL1: string = 'http://localhost:8083/resource/';

   29. export const basicResources: Array<ResourceConfig> = [
   30. {
   31. localPath: "in_cache_middle.png",
   32. urlList: [
   33. baseURL,
   34. baseURL + "request.png",
   35. baseURL1 + "request.png",
   36. ],
   37. type: webview.OfflineResourceType.IMAGE,
   38. responseHeaders: []
   39. },
   40. {
   41. localPath: "in_cache.js",
   42. urlList: [
   43. baseURL,
   44. baseURL + "request.js",
   45. baseURL1 + "request.js"
   46. ],
   47. type: webview.OfflineResourceType.CLASSIC_JS,
   48. responseHeaders: [
   49. {headerKey: "Content-Type", headerValue: "text/javascript" },
   50. {headerKey: "Cache-Control", headerValue: "max-age=100000" },
   51. ]
   52. },
   53. {
   54. localPath: "in_cache_module1.js",
   55. urlList: [
   56. baseURL + "request_module1.js",
   57. ],
   58. type: webview.OfflineResourceType.MODULE_JS,
   59. responseHeaders: [
   60. {headerKey: "Content-Type", headerValue: "application/javascript" },
   61. {headerKey: "Access-Control-Allow-Origin" , headerValue: "*"},
   62. {headerKey: "Cache-Control", headerValue: "max-age=100000" },
   63. ]
   64. },
   65. {
   66. localPath: "in_cache_module2.js",
   67. urlList: [
   68. baseURL + "request_module2.js",
   69. ],
   70. type: webview.OfflineResourceType.MODULE_JS,
   71. responseHeaders: [
   72. {headerKey: "Content-Type", headerValue: "application/javascript" },
   73. {headerKey: "Access-Control-Allow-Origin" , headerValue: "*"},
   74. {headerKey: "Cache-Control", headerValue: "max-age=100000" },
   75. ]
   76. },
   77. {
   78. localPath: "in_cache.css",
   79. urlList: [
   80. baseURL,
   81. baseURL + "request.css",
   82. baseURL1 + "request.css",
   83. ],
   84. type: webview.OfflineResourceType.CSS,
   85. responseHeaders: [
   86. {headerKey: "resource-Type", headerValue: "text/css" },
   87. {headerKey: "Cache-Control", headerValue: "max-age=100000" },
   88. ]
   89. },
   90. ];
   ```

   [CreateResourceConfig.ets](https://gitcode.com/HarmonyOS_Samples/BestPracticeSnippets/blob/master/LoadPerformanceInWeb/entry/src/main/ets/utils/CreateResourceConfig.ets#L2-L91)
2. 读取配置并注入资源

   ```
   1. // Call the offline resource injection cache interface
   2. export async function injectOfflineResource(controller: WebviewController, resourceMapArr: Array<webview.OfflineResourceMap>): Promise<void> {
   3. try {
   4. controller.injectOfflineResources(resourceMapArr);
   5. } catch (err) {
   6. hilog.error(DOMAIN, TAG, 'qqq injectOfflineResource error: ' + err.code + ' ' + err.message);
   7. }
   8. }
   ```

   [CreateResourceConfig.ets](https://gitcode.com/HarmonyOS_Samples/BestPracticeSnippets/blob/master/LoadPerformanceInWeb/entry/src/main/ets/utils/CreateResourceConfig.ets#L95-L102)

   性能打点数据如下：getMessageData进程中的Duration表示加载页面的总耗时。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c9/v3/mlpwOXsLQDq0w572eQu3EQ/zh-cn_image_0000002229451121.png?HW-CC-KV=V1&HW-CC-Date=20260612T021559Z&HW-CC-Expire=86400&HW-CC-Sign=EDEA7FE5B017B899C0923FCDB6A774D1636AA9A9750F59E0622C2FCC534981D9)

**总结**

**表3**

| 页面加载方式 | 耗时（数据仅供参考） | 说明 |
| --- | --- | --- |
| 直接加载Web页面 | 1312ms | 在触发页面加载时才发起资源请求，这会延长页面加载时间。 |
| 使用离线资源免拦截注入加载Web页面 | 74ms | 将资源预置在内存中，节省网络请求时间。 |

### 资源拦截替换加速

**原理介绍**

资源拦截替换加速在资源拦截替换接口基础上新增支持了ArrayBuffer格式的入参，开发者无需在应用侧进行ArrayBuffer到String格式的转换，可直接使用ArrayBuffer格式的数据进行拦截替换。

说明

本方案与原有接口使用相同，开发者只需在调用WebResourceResponse.setResponseData()接口时传入ArrayBuffer格式的数据。

**实践案例**

案例一：使用字符串格式的数据做拦截替换

```
1. import { webview } from '@kit.ArkWeb';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. const DOMAIN = 0x0000;
5. const TAG = 'Sample';

7. @Entry
8. @Component
9. struct Index {
10. controller: webview.WebviewController = new webview.WebviewController();
11. responseResource: WebResourceResponse = new WebResourceResponse();
12. // Here is the string format data.
13. resourceStr: string = 'xxxxxxxxxxxxxxx';

15. build() {
16. Column() {
17. Button('1 MB')
18. .fontSize(12)
19. .margin(5)
20. .onClick(() => {
21. const chunk = 'x'.repeat(1024);
22. let result = '';
23. for (let i = 0; i < 1000; i++) {
24. result += chunk;
25. }
26. this.resourceStr = JSON.stringify({
27. status: 200,
28. result: result,
29. });
30. hilog.info(DOMAIN, TAG, `Generated string data, size: ${this.resourceStr.length} bytes (${1000} KB)`);
31. })
32. Web({ src: $rawfile("intercept.html"), controller: this.controller })
33. .onConsole((event) => {
34. hilog.error(DOMAIN, TAG, `getMessageData ${event?.message?.getMessage()}`);
35. return true;
36. })
37. .onInterceptRequest(event => {
38. if (event) {
39. if (!event.request.getRequestUrl().startsWith('http://bridge')) {
40. return null;
41. }
42. }
43. // Use string format data for interception and replacement
44. this.responseResource.setResponseData(this.resourceStr);
45. this.responseResource.setResponseEncoding('utf-8');
46. this.responseResource.setResponseMimeType('text/json');
47. this.responseResource.setResponseCode(200);
48. this.responseResource.setReasonMessage('OK');
49. this.responseResource.setResponseHeader([{ headerKey: 'Access-Control-Allow-Origin', headerValue: '*' }]);
50. hilog.info(DOMAIN, TAG, 'getMessageData return reponse');
51. return this.responseResource;
52. })
53. }
54. }
55. }
```

[UseStringInterceptReplace.ets](https://gitcode.com/HarmonyOS_Samples/BestPracticeSnippets/blob/master/LoadPerformanceInWeb/entry/src/main/ets/pages/UseStringInterceptReplace.ets#L2-L56)

资源替换耗时如图所示。getMessageData和someFunction的执行时间表示页面加载资源的耗时。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7/v3/O5oc-MXLTHayxw0IF6WI4g/zh-cn_image_0000002194010852.png?HW-CC-KV=V1&HW-CC-Date=20260612T021559Z&HW-CC-Expire=86400&HW-CC-Sign=494E415FEAE81CD42A00C0177BEF5F1BCA0A8D506C503D3D0927BB128D26F9C6 "点击放大")

案例二：使用ArrayBuffer格式的数据做拦截替换

```
1. import { webview } from '@kit.ArkWeb';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. const DOMAIN = 0x0000;
5. const TAG = 'Sample';

7. @Entry
8. @Component
9. struct WebComponent {
10. controller: webview.WebviewController = new webview.WebviewController()
11. scheme1: webview.WebCustomScheme = { schemeName: "imeituan", isSupportCORS: true, isSupportFetch: true }
12. responseResource: WebResourceResponse = new WebResourceResponse()
13. // Developer Custom Response Data
14. data: string = "";
15. buffer: ArrayBuffer = new ArrayBuffer(this.data.length);
16. usingLen: number = 1;

18. aboutToAppear(): void {
19. // Configure the Web to open the debugging mode
20. webview.WebviewController.setWebDebuggingAccess(true);

22. try {
23. webview.WebviewController.customizeSchemes([this.scheme1])
24. hilog.info(DOMAIN, TAG, `customizeSchemes`)
25. } catch (error) {
26. hilog.error(DOMAIN, TAG, error);
27. }

29. this.initArrayBufferData(1);
30. }

32. onPageShow(): void {

34. }

36. initStringData(size: Number): void {
37. switch (size){
38. case 1:
39. this.usingLen = 10; //10k
40. break;
41. case 2:
42. this.usingLen = 1024; //1M
43. break;
44. case 3:
45. this.usingLen = 1024 * 10; //10M
46. break;
47. default:
48. this.usingLen = 1;
49. }

51. let str: string = "";
52. let str_1k: string = "";
53. for (let i = 0 ; i < 1024; i++) {
54. str_1k = str_1k.concat("x");
55. }
56. for (let j = 0; j < this.usingLen; j++) {
57. str = str.concat(str_1k);
58. }

60. this.data = JSON.stringify({
61. status: 200,
62. result: str,
63. });
64. hilog.info(DOMAIN, TAG, 'init data length: ' + this.data.length);
65. }

67. // size - 1:10k, 2:1M, 3:10M
68. initArrayBufferData(size:Number): void {
69. this.initStringData(size);
70. hilog.error(DOMAIN, TAG, 'target string: ' + this.data);
71. this.buffer = new ArrayBuffer(this.data.length);
72. const uint8Array: Uint8Array = new Uint8Array(this.buffer);
73. for (let i = 0; i < this.data.length; i++) {
74. uint8Array[i] = this.data.charCodeAt(i);
75. }
76. }

78. build() {
79. Column() {
80. Button('set to 10K')
81. .onClick(() => {
82. this.initArrayBufferData(1);
83. hilog.info(DOMAIN, TAG, 'datalen set to length '+ this.buffer.byteLength);
84. })
85. Button('set to 1M')
86. .onClick(() => {
87. this.initArrayBufferData(2);
88. hilog.info(DOMAIN, TAG, 'datalen set to length '+ this.buffer.byteLength);
89. })
90. Button('set to 10M')
91. .onClick(() => {
92. this.initArrayBufferData(3);
93. hilog.info(DOMAIN, TAG, 'datalen set to length '+ this.buffer.byteLength);
94. })
95. Web({ src: $rawfile("intercept.html"), controller: this.controller })
96. .onConsole((event) => {
97. hilog.error(DOMAIN, TAG, `getMessageData ${event?.message?.getMessage()}`);
98. return true;
99. })
100. .onInterceptRequest((event) => {
101. if (event) {
102. hilog.error(DOMAIN, TAG, 'url:' + event.request.getRequestUrl());
103. // Block Page Request
104. if (!event.request.getRequestUrl().startsWith('http://bridge')) {
105. return null;
106. }
107. }
108. // Construct response data
109. // const str: string = buffer.from(this.buffer).toString();
110. hilog.error(DOMAIN, TAG, 'response data length: ' + this.data.length);
111. this.responseResource.setResponseData(this.buffer);
112. this.responseResource.setResponseEncoding('utf-8');
113. this.responseResource.setResponseMimeType('text/json');
114. this.responseResource.setResponseCode(200);
115. this.responseResource.setReasonMessage('OK');
116. this.responseResource.setResponseHeader([{ headerKey: 'Access-Control-Allow-Origin', headerValue: '*' }]);
117. hilog.info(DOMAIN, TAG, 'getMessageData return reponse');
118. return this.responseResource;
119. })
120. }
121. }
122. }
```

[UseArrayBufferInterceptReplace.ets](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/LoadPerformanceInWeb/entry/src/main/ets/pages/UseArrayBufferInterceptReplace.ets#L2-L123)

资源替换耗时如图所示。getMessageData和william someFunction的执行时间表示页面加载资源的耗时。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8a/v3/K_EDT3krRL-qZZfKG7F1Dw/zh-cn_image_0000002229451125.png?HW-CC-KV=V1&HW-CC-Date=20260612T021559Z&HW-CC-Expire=86400&HW-CC-Sign=5F56D05D2F384F97AA268E8036AC6443DD5854F3A5155719EF66831F20575D60 "点击放大")

**总结**

**表4**

| 页面加载方式 | 耗时(局限不同设备和场景，数据仅供参考) | 说明 |
| --- | --- | --- |
| 使用String格式的数据做拦截替换 | 15ms | Web组件内部数据传输需要转换为ArrayBuffer，这会增加数据处理步骤和启动耗时 |
| 使用ArrayBuffer格式的数据做拦截替换 | 6ms | 接口支持ArrayBuffer格式，优化了数据传输方式，减少转换和传输时间 |

## JSBridge

### JSBridge优化解决方案

**适用场景**

应用使用ArkTS或C++语言混合开发，或应用架构接近小程序架构，自带C++环境，推荐使用ArkWeb在Native侧提供的ArkWeb\_ControllerAPI和ArkWeb\_ComponentAPI实现JSBridge功能。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a1/v3/Y9qqhnZBS1-4n_4g8PtgBA/zh-cn_image_0000002458691281.png?HW-CC-KV=V1&HW-CC-Date=20260612T021559Z&HW-CC-Expire=86400&HW-CC-Sign=BD1D654B11D39B012ED3268018A229A0905F07889D14ADA3653B5F64F4FA3F93 "点击放大")

上图展示了小程序的一般架构，逻辑层使用自带的JavaScript运行时，现有C++环境通过Native接口直接与视图层（ArkWeb渲染器）通信，无需返回ArkTS环境调用JSBridge接口。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5d/v3/yM7nE_8zTp-kaEqfMQ7Rsw/zh-cn_image_0000002229451137.png?HW-CC-KV=V1&HW-CC-Date=20260612T021559Z&HW-CC-Expire=86400&HW-CC-Sign=BD656AE59569DE5F74C06572973806DD99F290E895C481A8B9AACEF0D833C678 "点击放大")

Native JSBridge方案解决ArkTS环境的冗余切换，允许回调在非UI线程上报，避免UI阻塞。

**实践案例**

案例一：使用ArkTS接口实现JSBridge通信。

应用侧代码：

```
1. import { webview } from '@kit.ArkWeb';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. const DOMAIN = 0x0000;
5. const TAG = 'Sample';

7. @Entry
8. @Component
9. struct WebComponent {
10. webviewController: webview.WebviewController = new webview.WebviewController();

12. aboutToAppear(): void {
13. // Configure the Web to open the debugging mode
14. webview.WebviewController.setWebDebuggingAccess(true);
15. }

17. build() {
18. Column() {
19. Button('runJavaScript')
20. .onClick(() => {
21. hilog.info(DOMAIN, TAG, '现在时间是:' + new Date().getTime());
22. // When the front-end page function has no parameters, delete the param.
23. this.webviewController.runJavaScript('htmlTest(param)');
24. })
25. Button('runJavaScriptCodePassed')
26. .onClick(() => {
27. // Pass runJavaScript side code method
28. this.webviewController.runJavaScript(`function changeColor(){document.getElementById('text').style.color = 'red'}`);
29. })
30. Web({ src: $rawfile('index.html'), controller: this.webviewController })
31. }
32. }
33. }
```

[JsBridgeOfArkTS.ets](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/LoadPerformanceInWeb/entry/src/main/ets/pages/JsBridgeOfArkTS.ets#L2-L34)

前端页面代码：

```
1. <!DOCTYPE html>
2. <html>
3. <body>
4. <button type="button" onclick="callArkTS()">Click Me!</button>
5. <h1 id="text">这是一个测试信息，默认字体为黑色，调用runJavaScript方法后字体为绿色，调用runJavaScriptCodePassed方法后字体为红色</h1>
6. <script>
7. var param = "param: JavaScript Hello World!";
8. function htmlTest(param) {
9. document.getElementById('text').style.color = 'green';
10. document.getElementById('text').innerHTML = '现在时间：'+new Date().getTime()
11. console.log(param);
12. }
13. function htmlTest() {
14. document.getElementById('text').style.color = 'green';
15. document.getElementById('text').innerHTML = '现在时间：'+new Date().getTime();
16. }
17. function callArkTS() {
18. changeColor();
19. }
20. </script>
21. </body>
22. </html>
```

[test.html](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/LoadPerformanceInWeb/entry/src/main/resources/rawfile/test.html#L2-L23)

点击runJavaScript按钮后，触发h5页面的htmlTest方法，页面内容将变更为当前时间戳。如下图所示。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/54/v3/2l3HlWHSTaKEF6hgaEPd6w/zh-cn_image_0000002420463960.png?HW-CC-KV=V1&HW-CC-Date=20260612T021559Z&HW-CC-Expire=86400&HW-CC-Sign=EED122A876993F6E3AF2F4CC20BDA61C269416BEACA02BD8EF703B2425933CB5 "点击放大")

经过多轮测试，从点击ArkTS侧的Button到触发H5侧的htmlTest方法，耗时7到9毫秒。

案例二：使用NDK接口实现JSBridge通信。

应用侧代码：

```
1. import testNapi from 'libentry.so';
2. import { webview } from '@kit.ArkWeb';
3. import { hilog } from '@kit.PerformanceAnalysisKit';

5. const DOMAIN = 0x0000;
6. const TAG = 'Sample';

8. class testObj {
9. constructor() {
10. }

12. test(): string {
13. hilog.info(DOMAIN, TAG, 'ArkUI Web Component');
14. return "ArkUI Web Component";
15. }

17. toString(): void {
18. hilog.info(DOMAIN, TAG, 'Web Component toString');
19. }
20. }

22. @Entry
23. @Component
24. struct Index {
25. webTag: string = 'ArkWeb1';
26. controller: webview.WebviewController = new webview.WebviewController(this.webTag);
27. @State testObjtest: testObj = new testObj();

29. aboutToAppear(): void {
30. hilog.info(DOMAIN, TAG, 'aboutToAppear');
31. // init web ndk
32. testNapi.nativeWebInit(this.webTag);
33. }

35. build() {
36. Column() {
37. Row() {
38. Button('runJS hello')
39. .fontSize(12)
40. .onClick(() => {
41. hilog.info(DOMAIN, TAG, 'start:---->'+new Date().getTime());
42. testNapi.runJavaScript(this.webTag, "runJSRetStr(\"" + "hello" + "\")");
43. })
44. }.height('20%')

46. Row() {
47. Web({ src: $rawfile('runJS.html'), controller: this.controller })
48. .javaScriptAccess(true)
49. .fileAccess(true)
50. .onControllerAttached(() => {
51. hilog.error(DOMAIN, TAG, 'ndk onControllerAttached webId: ' + this.controller.getWebId());
52. })
53. }.height('80%')
54. }
55. }
56. }
```

[JsBridgeOfNdk.ets](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/LoadPerformanceInWeb/entry/src/main/ets/pages/JsBridgeOfNdk.ets#L2-L57)

hello.cpp作为应用C++侧业务逻辑代码：

```
1. // Registration objects and methods, sending scripts to callbacks after H5 execution, parsing instances passed from the side of the storage application and other code logics are not displayed here, and developers realize them by themselves according to their own business scenarios.
2. // Send the JS script to the H5 side for execution
3. #include "napi/native_api.h"
4. #include <bits/alltypes.h>
5. #include <memory>
6. #include <string>
7. #include <sys/types.h>
8. #include <thread>

10. #include "hilog/log.h"
11. #include "web/arkweb_interface.h"
12. #include "jsbridge_object.h"

14. constexpr unsigned int LOG_PRINT_DOMAIN = 0xFF00;
15. std::shared_ptr<JSBridgeObject> jsbridge_object_ptr = nullptr;
16. static ArkWeb_ControllerAPI *controller = nullptr;
17. static ArkWeb_ComponentAPI *component = nullptr;

19. static void RunJavaScriptCallback(const char *webTag, const char *result, void *userData) {
20. OH_LOG_Print(LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, "ArkWeb", "ndk RunJavaScriptCallback webTag:%{public}s", webTag);
21. if (!userData) {
22. OH_LOG_Print(LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, "ArkWeb", "ndk RunJavaScriptCallback userData is nullptr");
23. return;
24. }
25. std::weak_ptr<JSBridgeObject> jsb_weak_ptr = *static_cast<std::weak_ptr<JSBridgeObject> *>(userData);
26. if (auto jsb_ptr = jsb_weak_ptr.lock()) {
27. jsb_ptr->RunJavaScriptCallback(result);
28. } else {
29. OH_LOG_Print(LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, "ArkWeb",
30. "ndk RunJavaScriptCallback jsb_weak_ptr lock failed");
31. }
32. }

34. static void ProxyMethod1(const char *webTag, const ArkWeb_JavaScriptBridgeData *dataArray, size_t arraySize, void *userData) {
35. OH_LOG_Print(LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, "ArkWeb", "ndk ProxyMethod1 webTag:%{public}s", webTag);
36. if (!userData) {
37. OH_LOG_Print(LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, "ArkWeb", "ndk ProxyMethod1 userData is nullptr");
38. return;
39. }
40. std::weak_ptr<JSBridgeObject> jsb_weak_ptr = *static_cast<std::weak_ptr<JSBridgeObject> *>(userData);
41. if (auto jsb_ptr = jsb_weak_ptr.lock()) {
42. jsb_ptr->ProxyMethod1(dataArray, arraySize);
43. } else {
44. OH_LOG_Print(LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, "ArkWeb", "ndk ProxyMethod1 jsb_weak_ptr lock failed");
45. }
46. }

48. static void ProxyMethod2(const char *webTag, const ArkWeb_JavaScriptBridgeData *dataArray, size_t arraySize, void *userData) {
49. OH_LOG_Print(LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, "ArkWeb", "ndk ProxyMethod2 webTag:%{public}s", webTag);
50. if (!userData) {
51. OH_LOG_Print(LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, "ArkWeb", "ndk ProxyMethod2 userData is nullptr");
52. return;
53. }
54. std::weak_ptr<JSBridgeObject> jsb_weak_ptr = *static_cast<std::weak_ptr<JSBridgeObject> *>(userData);

56. std::string jsCode = "runJSRetStr()";
57. ArkWeb_JavaScriptObject object = {(uint8_t *)jsCode.c_str(), jsCode.size(),
58. &JSBridgeObject::StaticRunJavaScriptCallback,
59. static_cast<void *>(jsbridge_object_ptr->GetWeakPtr())};
60. controller->runJavaScript(webTag, &object);

62. if (auto jsb_ptr = jsb_weak_ptr.lock()) {
63. jsb_ptr->ProxyMethod2(dataArray, arraySize);
64. } else {
65. OH_LOG_Print(LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, "ArkWeb", "ndk ProxyMethod2 jsb_weak_ptr lock failed");
66. }
67. }

69. void ValidCallback(const char *webTag, void *userData) {
70. OH_LOG_Print(LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, "ArkWeb", "ndk ValidCallback webTag: %{public}s", webTag);
71. if (!userData) {
72. OH_LOG_Print(LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, "ArkWeb", "ndk ValidCallback userData is nullptr");
73. return;
74. }
75. std::weak_ptr<JSBridgeObject> jsb_weak_ptr = *static_cast<std::weak_ptr<JSBridgeObject> *>(userData);
76. if (auto jsb_ptr = jsb_weak_ptr.lock()) {
77. jsb_ptr->SaySomething("ValidCallback");
78. } else {
79. OH_LOG_Print(LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, "ArkWeb", "ndk ValidCallback jsb_weak_ptr lock failed");
80. }

82. OH_LOG_Print(LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, "ArkWeb", "ndk RegisterJavaScriptProxy begin");
83. ArkWeb_ProxyMethod method1 = {"method1", ProxyMethod1, static_cast<void *>(jsbridge_object_ptr->GetWeakPtr())};
84. ArkWeb_ProxyMethod method2 = {"method2", ProxyMethod2, static_cast<void *>(jsbridge_object_ptr->GetWeakPtr())};
85. ArkWeb_ProxyMethod methodList[2] = {method1, method2};
86. ArkWeb_ProxyObject proxyObject = {"ndkProxy", methodList, 2};
87. controller->registerJavaScriptProxy(webTag, &proxyObject);

89. OH_LOG_Print(LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, "ArkWeb", "ndk RegisterJavaScriptProxy end");
90. }

92. void LoadStartCallback(const char *webTag, void *userData) {
93. OH_LOG_Print(LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, "ArkWeb", "ndk LoadStartCallback webTag: %{public}s", webTag);
94. if (!userData) {
95. OH_LOG_Print(LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, "ArkWeb", "ndk LoadStartCallback userData is nullptr");
96. return;
97. }
98. std::weak_ptr<JSBridgeObject> jsb_weak_ptr = *static_cast<std::weak_ptr<JSBridgeObject> *>(userData);
99. if (auto jsb_ptr = jsb_weak_ptr.lock()) {
100. jsb_ptr->SaySomething("LoadStartCallback");
101. } else {
102. OH_LOG_Print(LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, "ArkWeb", "ndk LoadStartCallback jsb_weak_ptr lock failed");
103. }
104. }

106. void LoadEndCallback(const char *webTag, void *userData) {
107. OH_LOG_Print(LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, "ArkWeb", "ndk LoadEndCallback webTag: %{public}s", webTag);
108. if (!userData) {
109. OH_LOG_Print(LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, "ArkWeb", "ndk LoadEndCallback userData is nullptr");
110. return;
111. }
112. std::weak_ptr<JSBridgeObject> jsb_weak_ptr = *static_cast<std::weak_ptr<JSBridgeObject> *>(userData);
113. if (auto jsb_ptr = jsb_weak_ptr.lock()) {
114. jsb_ptr->SaySomething("LoadEndCallback");
115. } else {
116. OH_LOG_Print(LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, "ArkWeb", "ndk LoadEndCallback jsb_weak_ptr lock failed");
117. }
118. }

120. void DestroyCallback(const char *webTag, void *userData) {
121. OH_LOG_Print(LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, "ArkWeb", "ndk DestroyCallback webTag: %{public}s", webTag);
122. if (!userData) {
123. OH_LOG_Print(LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, "ArkWeb", "ndk DestroyCallback userData is nullptr");
124. return;
125. }
126. std::weak_ptr<JSBridgeObject> jsb_weak_ptr = *static_cast<std::weak_ptr<JSBridgeObject> *>(userData);
127. if (auto jsb_ptr = jsb_weak_ptr.lock()) {
128. jsb_ptr->SaySomething("DestroyCallback");
129. } else {
130. OH_LOG_Print(LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, "ArkWeb", "ndk DestroyCallback jsb_weak_ptr lock failed");
131. }
132. }

134. void SetComponentCallback(ArkWeb_ComponentAPI * component, const char* webTagValue) {
135. if (!ARKWEB_MEMBER_MISSING(component, onControllerAttached)) {
136. component->onControllerAttached(webTagValue, ValidCallback,
137. static_cast<void *>(jsbridge_object_ptr->GetWeakPtr()));
138. } else {
139. OH_LOG_Print(LOG_APP, LOG_ERROR, LOG_PRINT_DOMAIN, "ArkWeb", "component onControllerAttached func not exist");
140. }

142. if (!ARKWEB_MEMBER_MISSING(component, onPageBegin)) {
143. component->onPageBegin(webTagValue, LoadStartCallback,
144. static_cast<void *>(jsbridge_object_ptr->GetWeakPtr()));
145. } else {
146. OH_LOG_Print(LOG_APP, LOG_ERROR, LOG_PRINT_DOMAIN, "ArkWeb", "component onPageBegin func not exist");
147. }

149. if (!ARKWEB_MEMBER_MISSING(component, onPageEnd)) {
150. component->onPageEnd(webTagValue, LoadEndCallback,
151. static_cast<void *>(jsbridge_object_ptr->GetWeakPtr()));
152. } else {
153. OH_LOG_Print(LOG_APP, LOG_ERROR, LOG_PRINT_DOMAIN, "ArkWeb", "component onPageEnd func not exist");
154. }

156. if (!ARKWEB_MEMBER_MISSING(component, onDestroy)) {
157. component->onDestroy(webTagValue, DestroyCallback,
158. static_cast<void *>(jsbridge_object_ptr->GetWeakPtr()));
159. } else {
160. OH_LOG_Print(LOG_APP, LOG_ERROR, LOG_PRINT_DOMAIN, "ArkWeb", "component onDestroy func not exist");
161. }
162. }

164. static napi_value NativeWebInit(napi_env env, napi_callback_info info) {
165. OH_LOG_Print(LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, "ArkWeb", "ndk NativeWebInit start");
166. size_t argc = 1;
167. napi_value args[1] = {nullptr};
168. napi_get_cb_info(env, info, &argc, args, nullptr, nullptr);
169. size_t webTagSize = 0;
170. napi_get_value_string_utf8(env, args[0], nullptr, 0, &webTagSize);
171. char *webTagValue = new (std::nothrow) char[webTagSize + 1];
172. size_t webTagLength = 0;
173. napi_get_value_string_utf8(env, args[0], webTagValue, webTagSize + 1, &webTagLength);
174. OH_LOG_Print(LOG_APP, LOG_ERROR, LOG_PRINT_DOMAIN, "ArkWeb", "ndk NativeWebInit webTag:%{public}s", webTagValue);

176. jsbridge_object_ptr = std::make_shared<JSBridgeObject>(webTagValue);
177. if (jsbridge_object_ptr)
178. jsbridge_object_ptr->Init();

180. controller = reinterpret_cast<ArkWeb_ControllerAPI *>(OH_ArkWeb_GetNativeAPI(ARKWEB_NATIVE_CONTROLLER));
181. component = reinterpret_cast<ArkWeb_ComponentAPI *>(OH_ArkWeb_GetNativeAPI(ARKWEB_NATIVE_COMPONENT));
182. SetComponentCallback(component, webTagValue);

184. OH_LOG_Print(LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, "ArkWeb", "ndk NativeWebInit end");
185. delete[] webTagValue;
186. return nullptr;
187. }

189. static napi_value RunJavaScript(napi_env env, napi_callback_info info) {
190. size_t argc = 2;
191. napi_value args[2] = {nullptr};
192. napi_get_cb_info(env, info, &argc, args, nullptr, nullptr);

194. size_t webTagSize = 0;
195. napi_get_value_string_utf8(env, args[0], nullptr, 0, &webTagSize);
196. char *webTagValue = new (std::nothrow) char[webTagSize + 1];
197. size_t webTagLength = 0;
198. napi_get_value_string_utf8(env, args[0], webTagValue, webTagSize + 1, &webTagLength);
199. OH_LOG_Print(LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, "ArkWeb", "ndk OH_NativeArkWeb_RunJavaScript webTag:%{public}s",
200. webTagValue);

202. size_t bufferSize = 0;
203. napi_get_value_string_utf8(env, args[1], nullptr, 0, &bufferSize);
204. char *jsCode = new (std::nothrow) char[bufferSize + 1];
205. size_t byteLength = 0;
206. napi_get_value_string_utf8(env, args[1], jsCode, bufferSize + 1, &byteLength);

208. OH_LOG_Print(LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, "ArkWeb",
209. "ndk OH_NativeArkWeb_RunJavaScript jsCode len:%{public}zu", strlen(jsCode));

211. ArkWeb_JavaScriptObject object = {(uint8_t *)jsCode, bufferSize, &JSBridgeObject::StaticRunJavaScriptCallback,
212. static_cast<void *>(jsbridge_object_ptr->GetWeakPtr())};
213. controller->runJavaScript(webTagValue, &object);
214. delete[] webTagValue;
215. delete[] jsCode;
216. return nullptr;
217. }

219. EXTERN_C_START
220. static napi_value Init(napi_env env, napi_value exports) {
221. napi_property_descriptor desc[] = {
222. {"nativeWebInit", nullptr, NativeWebInit, nullptr, nullptr, nullptr, napi_default, nullptr},
223. {"runJavaScript", nullptr, RunJavaScript, nullptr, nullptr, nullptr, napi_default, nullptr},
224. };
225. napi_define_properties(env, exports, sizeof(desc) / sizeof(desc[0]), desc);
226. return exports;
227. }
228. EXTERN_C_END

230. static napi_module demoModule = {
231. .nm_version = 1,
232. .nm_flags = 0,
233. .nm_filename = nullptr,
234. .nm_register_func = Init,
235. .nm_modname = "entry",
236. .nm_priv = ((void *)0),
237. .reserved = {0},
238. };

240. extern "C" __attribute__((constructor)) void RegisterEntryModule(void) { napi_module_register(&demoModule); }
```

[hello.cpp](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/LoadPerformanceInWeb/entry/src/main/cpp/hello.cpp#L2-L241)

Native侧业务代码entry/src/main/cpp/jsbridge\_object.h和entry/src/main/cpp/jsbridge\_object.cpp详见[应用侧与前端页面的相互调用(C/C++)](../../../../../harmonyos-guides/应用框架/ArkWeb（方舟Web）/在应用中使用前端页面JavaScript/应用侧与前端页面的相互调用(CC++)/arkweb-ndk-jsbridge.md)。

runJS.html作为应用前端页面：

```
1. <!DOCTYPE html>
2. <html lang="en-gb">
3. <head>
4. <meta name="viewport" content="width=device-width, initial-scale=1.0">
5. <title>run javascript demo</title>
6. </head>
7. <body>
8. <h1>run JavaScript Ext demo</h1>
9. <p id="webDemo"></p>
10. <br>
11. <button type="button" style="height:30px;width:200px" onclick="testNdkProxyObjMethod1()">test ndk method1 ! </button>
12. <br>
13. <br>
14. <button type="button" style="height:30px;width:200px" onclick="testNdkProxyObjMethod2()">test ndk method2 ! </button>
15. <br>
16. </body>
17. <script type="text/javascript">
18. function testNdkProxyObjMethod1() {
19. // Verify whether the ndk method has been registered in window
20. if (window.ndkProxy == undefined) {
21. document.getElementById("webDemo").innerHTML = "ndkProxy undefined";
22. return "objName undefined";
23. }
24. if (window.ndkProxy.method1 == undefined) {
25. document.getElementById("webDemo").innerHTML = "ndkProxy method1 undefined";
26. return "objName  test undefined";
27. }
28. if (window.ndkProxy.method2 == undefined) {
29. document.getElementById("webDemo").innerHTML = "ndkProxy method2 undefined";
30. return "objName  test undefined";
31. }
32. // Call the method1 method of ndk registered to window and display the results back to the p tag.
33. var retStr = window.ndkProxy.method1("hello", "world", [1.2, -3.4, 123.456], ["Saab", "Volvo", "BMW", undefined], 1.23456, 123789, true, false, 0,  undefined);
34. document.getElementById("webDemo").innerHTML  = "ndkProxy and method1 is ok, " + retStr;
35. }
36. function testNdkProxyObjMethod2() {
37. // Verify whether the ndk method has been registered in window
38. if (window.ndkProxy == undefined) {
39. document.getElementById("webDemo").innerHTML = "ndkProxy undefined";
40. return "objName undefined";
41. }
42. if (window.ndkProxy.method1 == undefined) {
43. document.getElementById("webDemo").innerHTML = "ndkProxy method1 undefined";
44. return "objName  test undefined";
45. }
46. if (window.ndkProxy.method2 == undefined) {
47. document.getElementById("webDemo").innerHTML = "ndkProxy method2 undefined";
48. return "objName  test undefined";
49. }
50. var student = {
51. name:"zhang",
52. sex:"man",
53. age:25
54. };
55. var cars = [student, 456, false, 4.567];
56. let params = "[\"{\\\"scope\\\"]";
57. // Call the method2 method of ndk registration to the windows and display the results back to the p tag
58. var retStr = window.ndkProxy.method2("hello", "world", false, cars, params);
59. document.getElementById("webDemo").innerHTML  = "ndkProxy and method2 is ok, " + retStr;
60. }
61. function runJSRetStr(data) {
62. const d = new Date();
63. let time = d.getTime();
64. document.getElementById("webDemo").innerHTML = new Date().getTime();
65. return JSON.stringify(time);
66. }
67. </script>
68. </html>
```

[runJS.html](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/LoadPerformanceInWeb/entry/src/main/resources/rawfile/runJS.html#L2-L69)

点击“runJS hello”按钮后，触发H5页面的`runJSRetStr`方法，页面内容更新为当前时间戳。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5a/v3/5WtAn5HGSUKbtPD-p-ezBw/zh-cn_image_0000002229336597.png?HW-CC-KV=V1&HW-CC-Date=20260612T021559Z&HW-CC-Expire=86400&HW-CC-Sign=4F45770699BC36E3C627FED3A3998B7F43E3DC189D5DBCD977DE36A49AA6401A "点击放大")

经过多轮测试，从点击ArkTS侧的Button到触发H5侧的runJSRetStr方法，耗时2到6毫秒。

**总结**

| 通信方式 | 耗时(局限不同设备和场景，数据仅供参考) | 说明 |
| --- | --- | --- |
| ArkWeb实现与前端页面通信 | 7ms~9ms | ArkTS环境冗余切换,耗时较长 |
| ArkWeb、c++实现与前端页面通信 | 2ms~6ms | 避免ArkTS环境冗余切换，耗时短 |

JSBridge优化方案适用于ArkWeb应用与前端网页通信，开发者可根据应用架构选择合适的通信机制。

1. 应用使用ArkTS语言开发，推荐使用ArkWeb的runJavaScriptExt接口实现应用侧与前端页面的通信，并使用registerJavaScriptProxy接口实现前端页面与应用侧的通信。
2. 应用使用ArkTS和C++语言混合开发，或应用结构类似于小程序架构，自带C++环境，推荐使用ArkWeb在NDK侧提供的OH\_NativeArkWeb\_RunJavaScript和OH\_NativeArkWeb\_RegisterJavaScriptProxy接口实现JSBridge功能。

说明

开发者需根据当前业务区分是否存在C++侧环境（较为显著标志点为当前应用是否使用了Node API技术进行开发，若是则该应用具备C++侧环境）。 具备C++侧环境的应用开发，可使用ArkWeb提供的NDK侧JSBridge接口。 不具备C++侧环境的应用开发，可使用ArkWeb侧JSBridge接口。

### 异步JSBridge调用

**原理介绍**

异步JSBridge调用适用于H5侧调用ArkTS侧或C++侧注册的JSBridge函数。调用后不等待执行结果，避免在ArkUI主线程负载重时JSBridge同步调用导致Web线程等待IPC时间过长，从而造成阻塞。

**实践案例**

案例一：使用ArkTS接口实现JSBridge通信，具体步骤如下：

1. 只注册同步函数

   ```
   1. import { webview } from '@kit.ArkWeb';
   2. import { BusinessError } from '@kit.BasicServicesKit';
   3. import { hilog } from '@kit.PerformanceAnalysisKit';

   5. const DOMAIN = 0x0000;
   6. const TAG = 'Sample';

   8. // Define ETS side objects and functions
   9. class TestObj {
   10. constructor() {}
   11. test(testStr:string): string {
   12. let start: number = Date.now();
   13. // Simulate time-consuming operations
   14. for(let i = 0; i < 500000; i++) {}
   15. let end: number = Date.now();
   16. hilog.info(DOMAIN, TAG, 'objName.test start: ' + start);
   17. return 'objName.test Sync function took ' + (end - start) + 'ms';
   18. }
   19. asyncTestBool(testBol:boolean): Promise<string> {
   20. return new Promise((resolve, reject) => {
   21. let start: number = Date.now();
   22. // Simulate time-consuming operation (asynchronous)
   23. setTimeout(() => {
   24. for(let i = 0; i < 500000; i++) {}
   25. let end: number = Date.now();
   26. hilog.info(DOMAIN, TAG, 'objAsyncName.asyncTestBool start: ' + start);
   27. resolve('objName.asyncTestBool Async function took ' + (end - start) + 'ms');
   28. }, 0); // Use 0 ms delay to simulate an asynchronous operation that starts immediately
   29. });
   30. }
   31. }

   33. class WebObj {
   34. constructor() {}
   35. webTest(): string {
   36. let start: number = Date.now();
   37. // Simulate time-consuming operations
   38. for(let i = 0; i < 500000; i++) {}
   39. let end: number = Date.now();
   40. hilog.info(DOMAIN, TAG, 'objTestName.webTest start: ' + start);
   41. return 'objTestName.webTest Sync function took ' + (end - start) + 'ms';
   42. }
   43. webString(): string {
   44. let start: number = Date.now();
   45. // Simulate time-consuming operations
   46. for(let i = 0; i < 500000; i++) {}
   47. let end: number = Date.now();
   48. hilog.info(DOMAIN, TAG, 'objTestName.webString start: ' + start);
   49. return 'objTestName.webString Sync function took ' + (end - start) + 'ms';
   50. }
   51. }

   53. class AsyncObj {
   54. constructor() {
   55. }

   57. asyncTest(): Promise<string> {
   58. return new Promise((resolve, reject) => {
   59. let start: number = Date.now();
   60. // Simulate time-consuming operation (asynchronous)
   61. setTimeout(() => {
   62. for (let i = 0; i < 500000; i++) {
   63. }
   64. let end: number = Date.now();
   65. hilog.info(DOMAIN, TAG, 'objAsyncName.asyncTest start: ' + start);
   66. resolve('objAsyncName.asyncTest Async function took ' + (end - start) + 'ms');
   67. }, 0); // Use 0 ms delay to simulate an asynchronous operation that starts immediately
   68. });
   69. }

   71. asyncString(testStr:string): Promise<string> {
   72. return new Promise((resolve, reject) => {
   73. let start: number = Date.now();
   74. // Simulate time-consuming operation (asynchronous)
   75. setTimeout(() => {
   76. for (let i = 0; i < 500000; i++) {
   77. }
   78. let end: number = Date.now();
   79. hilog.info(DOMAIN, TAG, 'objAsyncName.asyncString start: ' + start);
   80. resolve('objAsyncName.asyncString Async function took ' + (end - start) + 'ms');
   81. }, 0); // Use 0 millisecond delay to simulate immediate asynchronous operation
   82. });
   83. }
   84. }

   86. @Entry
   87. @Component
   88. struct Index {
   89. controller: webview.WebviewController = new webview.WebviewController();
   90. @State testObjtest: TestObj = new TestObj();
   91. @State webTestObj: WebObj = new WebObj();
   92. @State asyncTestObj: AsyncObj = new AsyncObj();
   93. build() {
   94. Column() {
   95. Button('refresh')
   96. .onClick(()=>{
   97. try{
   98. this.controller.refresh();
   99. } catch (error) {
   100. hilog.error(DOMAIN, TAG, `ErrorCode:${(error as BusinessError).code},Message:${(error as BusinessError).message}`);
   101. }
   102. })
   103. Button('Register JavaScript To Window')
   104. .onClick(()=>{
   105. try {
   106. // Only register synchronization functions
   107. this.controller.registerJavaScriptProxy(this.webTestObj,"objTestName",["webTest","webString"]);
   108. } catch (error) {
   109. hilog.error(DOMAIN, TAG, `ErrorCode:${(error as BusinessError).code},Message:${(error as BusinessError).message}`);
   110. }
   111. })
   112. Web({src: $rawfile('index.html'),controller: this.controller}).javaScriptAccess(true)
   113. }
   114. }
   115. }
   ```

   [RegisterSyncFunction.ets](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/LoadPerformanceInWeb/entry/src/main/ets/pages/RegisterSyncFunction.ets#L2-L116)
2. H5侧调用JSBridge函数

   ```
   1. <!DOCTYPE html>
   2. <html lang="en">
   3. <head>
   4. <meta charset="UTF-8">
   5. <meta name="viewport" content="width=device-width, initial-scale=1.0">
   6. <title>Document</title>
   7. </head>
   8. <body>
   9. <button type="button" onclick="htmlTest()"> Click Me!</button>
   10. <p id="demo"></p>
   11. <p id="webDemo"></p>
   12. <p id="asyncDemo"></p>
   13. </body>
   14. <script type="text/javascript">
   15. async function htmlTest() {
   16. document.getElementById("demo").innerHTML = '测试开始:' + new Date().getTime() + '\n';
   17. const time1 = new Date().getTime();
   18. objTestName.webString();
   19. const time2 = new Date().getTime();
   20. objAsyncName.asyncString();
   21. const time3 = new Date().getTime();
   22. objName.asyncTestBool();
   23. const time4 = new Date().getTime();
   24. objName.test();
   25. const time5 = new Date().getTime();
   26. objTestName.webTest();
   27. const time6 = new Date().getTime();
   28. objAsyncName.asyncTest();
   29. const time7 = new Date().getTime();
   30. const result = [
   31. 'objTestName.webString()耗时：'+ (time2 - time1),
   32. 'objAsyncName.asyncString()耗时：'+ (time3 - time2),
   33. 'objName.asyncTestBool()耗时：'+ (time4 - time3),
   34. 'objName.test()耗时：'+ (time5 - time4),
   35. 'objTestName.webTest()耗时：'+ (time6 - time5),
   36. 'objAsyncName.asyncTest()耗时：'+ (time7 - time6)
   37. ]
   38. document.getElementById("demo").innerHTML = document.getElementById("demo").innerHTML + '\n' + result.join('\n');
   39. }
   40. </script>
   41. </html>
   ```

   [demo.html](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/LoadPerformanceInWeb/entry/src/main/resources/rawfile/demo.html#L2-L42)

案例二：使用 `registerJavaScriptProxy` 或 `javaScriptProxy` 注册异步函数或异步同步共存函数。H5 侧调用 JSBridge 函数时，建议避免使用不推荐的用法。

```
1. Button('refresh')
2. .onClick(()=>{
3. try{
4. this.controller.refresh();
5. } catch (error) {
6. hilog.error(DOMAIN, TAG, `ErrorCode:${(error as BusinessError).code},Message:${(error as BusinessError).message}`);
7. }
8. })
9. Button('Register JavaScript To Window')
10. .onClick(()=>{
11. try {
12. // Only register synchronization functions
13. this.controller.registerJavaScriptProxy(this.webTestObj,"objTestName",["webTest","webString"]);
14. } catch (error) {
15. hilog.error(DOMAIN, TAG, `ErrorCode:${(error as BusinessError).code},Message:${(error as BusinessError).message}`);
16. }
17. })
18. Web({src: $rawfile('index.html'),controller: this.controller}).javaScriptAccess(true)

20. // Registration by javaScriptProxy
21. // javaScriptProxy only supports the registration of one object. If you need to register multiple objects, please use registerJavaScriptProxy.
22. Web({src: $rawfile('index.html'),controller: this.controller})
23. .javaScriptAccess(true)
24. .javaScriptProxy({
25. object: this.testObjtest,
26. name:"objName",
27. methodList: ["test","toString"],
28. // Specify the list of asynchronous functions
29. asyncMethodList: ["test","toString"],
30. controller: this.controller
31. })
```

[RegisterJavaScriptProxy.ets](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/LoadPerformanceInWeb/entry/src/main/ets/pages/RegisterJavaScriptProxy.ets#L96-L126)

**总结**

数据运行结果如下表所示。

| 注册方法类型 | 耗时(局限不同设备和场景，数据仅供参考) | 说明 |
| --- | --- | --- |
| 同步方法 | 1398ms，2707ms，2705ms | 同步函数调用会阻塞JavaScript线程 |
| 异步方法 | 2ms，2ms，4ms | 异步函数调用不阻塞JavaScript线程 |

运行数据显示，`async`异步方法在JavaScript单线程任务队列中不会长时间占用，因为它们不需要等待结果。而同步方法则需要等待ArkTS侧主线程同步执行后才能返回结果。

说明

JSBridge接口在注册时，即会根据注册调用的接口决定其调用方式（同步/异步）。开发者需根据当前业务区分， 是否将其注册为异步函数。

* 同步函数调用会阻塞JavaScript执行，等待JSBridge函数执行结束，适用于需要返回值或存在时序问题的场景。
* 异步函数调用时不会等待JSBridge函数执行结束，后续JavaScript可在特定时间后继续执行。JSBridge函数无法直接返回值。
* 注册在ETS侧的JSBridge函数调用时需要在主线程上执行；NDK侧注册的函数将在其他线程中执行。
* 异步JSBridge接口与同步接口在JavaScript侧的调用方式一致，仅注册方式不同，本部分调用方式仅作简要示范。

附 NDK 接口实现 JSBridge 通信（C++ 侧注册异步函数）：

```
1. // Define the JSBridge function
2. static void ProxyMethod1(const char* webTag, void* userData) {
3. OH_LOG_Print(LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, "ArkWeb", "Method1 webTag :%{public}s",webTag);
4. }

6. static void ProxyMethod2(const char* webTag, void* userData) {
7. OH_LOG_Print(LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, "ArkWeb", "Method2 webTag :%{public}s",webTag);
8. }

10. static void ProxyMethod3(const char* webTag, void* userData) {
11. OH_LOG_Print(LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, "ArkWeb", "Method3 webTag :%{public}s",webTag);
12. }

14. void RegisterCallback(const char *webTag) {
15. int myUserData = 100;
16. //Create function method structure
17. ArkWeb_ProxyMethod m1 = {
18. .methodName = "method1",
19. .callback = ProxyMethod1,
20. .userData = (void *)&myUserData
21. };
22. ArkWeb_ProxyMethod m2 = {
23. .methodName = "method2",
24. .callback = ProxyMethod2,
25. .userData = (void *)&myUserData
26. };
27. ArkWeb_ProxyMethod m3 = {
28. .methodName = "method3",
29. .callback = ProxyMethod3,
30. .userData = (void *)&myUserData
31. };
32. ArkWeb_ProxyMethod methodList[2] = {m1,m2};

34. //Create a JSBridge object structure
35. ArkWeb_ProxyObject obj = {
36. .objName = "ndkProxy",
37. .methodList = methodList,
38. .size = 2
39. };
40. // Get the ArkWeb_Controller API structure
41. ArkWeb_AnyNativeAPI* apis = OH_ArkWeb_GetNativeAPI(ArkWeb_NativeAPIVariantKind::ARKWEB_NATIVE_CONTROLLER);
42. ArkWeb_ControllerAPI* ctrlApi = reinterpret_cast<ArkWeb_ControllerAPI*>(apis);

44. // Call the registration interface, registration function
45. ctrlApi->registerJavaScriptProxy(webTag, &obj);

47. ArkWeb_ProxyMethod asyncMethodList[1] = {m3};
48. ArkWeb_ProxyObject obj2 = {
49. .objName = "ndkProxy",
50. .methodList = asyncMethodList,
51. .size = 1
52. };
53. ctrlApi->registerAsyncJavaScriptProxy(webTag, &obj2);
54. }
```

[DefineJSBridge.cpp](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/LoadPerformanceInWeb/entry/src/main/cpp/DefineJSBridge.cpp#L2-L55)

## 同层渲染

同层渲染是一种优化技术，用于提高Web页面的渲染性能。同层渲染会将位于同一个图层的元素一起渲染，以减少重绘和重排的次数，从而提高页面的渲染效率。关于同层渲染的内容，可以参考[使用同层渲染在Web组件上渲染原生组件](../../../../应用框架/ArkWeb/同层渲染原生组件/bpta-render-web-using-same-layer-render.md)。

## 总结

本文深入探讨Web页面加载原理及优化方法，为开发者提供重要指导。互联网时代，用户对网页加载速度和体验要求提高，页面加载优化成为开发者必须重视的环节。理解Web页面加载原理，有助于开发者处理加载优化问题，提升应用质量。

文中介绍了预连接、预下载、预渲染、预取POST、预编译等优化方法，指导开发者提高Web页面的加载速度。这些方法能够显著提升应用的流畅度和用户体验。然而，这些优化方法均依赖预处理，因此会带来一定的成本。

在实际开发中，开发者应根据具体情况进行权衡，确定合适的方案与策略。此外，提供JSBridge和资源加速优化方案，帮助提高Web加载性能。除了上述方法，开发者还可以通过压缩资源和减少HTTP请求来进一步优化页面加载速度。压缩资源可减小文件大小，减少加载时间；减少HTTP请求可降低网络延迟，加快页面加载速度，提升用户体验。

Web页面加载优化对提升用户体验、网站性能、页面浏览量和转化率至关重要。开发者应重视并持续探索优化方法，以实现商业目标。采用文章中介绍的优化方法，可以改善页面加载速度，增强用户体验，增加页面浏览量，提升应用活跃度和用户粘性。持续优化页面加载速度，能够更好地满足用户需求，提升应用价值。
