---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-interaction-basic-principles
title: 交互基础机制说明
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (ArkTS声明式开发范式) > 添加交互响应 > 交互基础机制说明
category: harmonyos-guides
scraped_at: 2026-06-11T14:31:45+08:00
doc_updated_at: 2026-05-26
content_hash: sha256:95ae2d3c71afdeaa9293233f36cd0664126987cbb8093b47037c46ebc83de6fa
---
对于[触摸事件](../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/通用事件/基础输入事件/触摸事件/ts-universal-events-touch.md)、[鼠标事件](../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/通用事件/基础输入事件/鼠标事件/ts-universal-mouse-key.md)、[轴事件](../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/通用事件/基础输入事件/轴事件/ts-universal-events-axis.md)等指向性事件的交互，交互框架基于坐标信息进行命中测试确定事件和手势的响应目标，即收集形成响应链，系统会根据触控事件的坐标、类型等信息，结合UI布局，将事件发送给对应UI组件。多个事件可以组合触发手势或其他功能，如长按、点击、拖拽。

## 事件交互流程

事件交互流程是指当ArkUI接收上游发送的Touch类触控事件或Mouse类触控事件后，根据开发者设定的各类参数，收集事件响应链并分发至各组件以触发回调的整个过程。该流程可以概括为以下三个步骤：

1. 事件产生

   硬件输入设备通过驱动、多模等模块，将事件上报至目标的ArkUI实例。ArkUI在渲染管线中进行统一处理。
2. 收集事件响应链并分发事件

   事件响应链是事件交互流程的核心，管线在接收事件后，将通过触摸测试建立事件响应链，通过响应链决策事件分发以及手势合成。

   （1）触摸测试

   当管线接收到起始触控事件后，将根据起始触控事件的坐标和组件位置进行触摸测试，最终建立事件响应链。开发者可以通过设置属性影响事件响应链的形成。

   （2）分发事件至Touch事件响应链

   构建事件响应链后，触控事件将根据Touch事件响应链分发至目标组件。

   （3）分发事件至手势响应链并进行手势识别

   各组件上设置的手势在通过触摸测试后，还会形成手势响应链。触控事件送入手势响应链后会与其它事件组合产生手势，手势之间再经过竞争，最终触发符合条件的手势回调。

   （4）事件拦截

   事件响应链建立前，开发者可以配置触摸测试属性从而影响到事件响应链的形成。当事件响应链建立后，开发者可以通过设置接口实现事件拦截，从而改变事件分发的流程。

   当分发事件至Touch事件响应链时，开发者可以通过设置触摸事件拦截，防止触摸事件继续传递给响应链的后续节点。

   当分发事件至手势响应链时，开发者可以通过设置手势拦截阻止手势响应。
3. 触发回调

   在收集事件响应链时，开发者绑定的回调函数将被同步收集。完成事件响应链的收集及事件分发后，符合触发条件的事件和手势对应的回调函数将被触发。

## 事件响应链

事件响应链是指通过触摸测试收集到的、能够响应本次交互的所有组件组成的有序链条。当用户触摸屏幕时，系统会从触摸点位置开始，遵循右子树优先的后序遍历顺序（即从最内层组件开始，自下而上、从右到左逐层向外收集），形成完整的响应链。

下图展示了组件树的层级结构与事件响应链的收集过程。图中父、子节点分别对应父组件和子组件，左子树和右子树对应兄弟组件，右子树对应的组件会显示在左子树对应组件的上方。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3/v3/EtoCWFxcQyCZ4qSQLC051A/zh-cn_image_0000002622697897.png?HW-CC-KV=V1&HW-CC-Date=20260611T063143Z&HW-CC-Expire=86400&HW-CC-Sign=D527F4E75C8D57FB86A25DC635CC7BE0B869080BA83473C506D100DAF27EAE9E)

通过[hitTestBehavior](../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/通用属性/交互属性/触摸交互控制/触摸测试控制/ts-universal-attributes-hit-test-behavior.md#hittestbehavior)属性可以设置组件的触摸测试模式。在本示例中，所有组件的触摸测试模式均设置为[HitTestMode](../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/公共定义/枚举说明/ts-appendix-enums.md#hittestmode9).Default。如果用户点按的动作发生在组件5上，则响应链收集过程如下：

1. 系统检测到触摸点落在组件5上，组件5被收集。
2. 向上冒泡至父组件3，组件3被收集。
3. 由于组件3的触摸测试模式为HitTestMode.Default，收集到事件后会阻塞兄弟节点，因此组件2不会被收集。
4. 继续向上冒泡至根组件1，组件1被收集。

因此最终收集到的响应链以及组件先后关系是5、3、1。

## 触摸测试

触摸测试即touch test，也称为命中测试（hit test），是在用户交互开始前，系统确定哪些组件上的事件或手势能够参与此次交互响应的过程。

### 实现原理

对于指向性基础事件的派发，系统不会直接从页面根节点递归遍历所有组件节点，而是在首次事件发生时确定能够响应此次交互的组件范围，即识别用户点击的组件。对于未被点击的组件，在此次交互中将不会有任何响应。这一过程称为命中测试（hit test/touch test）。系统依据组件响应热区是否包含事件坐标来判定是否被点击。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a8/v3/m6lmmZ6XT5WMx2EIHsSg6Q/zh-cn_image_0000002592218336.png?HW-CC-KV=V1&HW-CC-Date=20260611T063143Z&HW-CC-Expire=86400&HW-CC-Sign=AC332C736972EAD7AFA105AE62574AF4513AD57B94EB878F3E8D8B31B598D538)

当用户触发按下事件时，系统将自上而下、自右向左遍历组件树，收集每个组件上绑定的手势和事件，然后将这些信息逐级向上冒泡至父组件进行整合，最终构建完整的事件响应链。

假设T点为用户按下的位置（Touch Down），则A、B、D组件将被判定为命中，这些组件组成的链条被称为本次交互的响应链。基础事件将在该响应链上进行传递，首先传递给叶子节点，随后传递给父节点，逐层向上传递，这一过程称为事件冒泡。

以下是描述命中测试过程的流程图：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3c/v3/QO0GcTRJQuS7xKTsvDiSkw/zh-cn_image_0000002592378270.png?HW-CC-KV=V1&HW-CC-Date=20260611T063143Z&HW-CC-Expire=86400&HW-CC-Sign=7C7AB42CB7328BEE57C00BB7B23D9097F585EA79FF7ECE0DE4DCF0B0B996E784)

如图所示，当起始事件被分发至组件时，组件会收集自身绑定的手势与事件，随后将收集结果传递给父组件，直至达到根节点。若组件透明、已从组件树中移除，或事件坐标不在组件响应热区范围内，将不会触发收集过程，父组件接收的反馈为空。除此之外，所有组件均会执行手势与事件的收集，并将结果反馈给父组件。

### 干预命中

应用可以通过以下几种方式对命中结果进行干预，从而影响最终的响应范围，即控制哪些组件能够被收集到。

| 干预方式 | 功能描述 | 对应接口 | 说明 |
| --- | --- | --- | --- |
| 触摸热区设置 | 设置组件能够响应用户交互的热区范围。 | [responseRegion](../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/通用属性/交互属性/触摸交互控制/触摸热区设置/ts-universal-attributes-touch-target.md#responseregion) | 1.热区会被用来识别用户手指落下的位置是否在热区范围内，只有在范围内的才会被收集；  2. 热区也会影响一些手势的判定，比如点击，只有当在热区范围抬手时才会被触发。 |
| 触摸热区设置 | 设置组件能够响应鼠标交互的热区范围。 | [mouseResponseRegion](../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/通用属性/交互属性/触摸交互控制/触摸热区设置/ts-universal-attributes-touch-target.md#mouseresponseregion10) | 设置一个或多个鼠标触摸热区。功能与responseRegion类似，但仅对鼠标事件生效。 |
| 触摸热区设置 | 设置组件的触摸热区列表。 | [responseRegionList](../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/通用属性/交互属性/触摸交互控制/触摸热区设置/ts-universal-attributes-touch-target.md#responseregionlist22) | 设置组件的触摸热区列表，可指定每个热区适用的输入工具类型（如鼠标、触摸等）。调用该接口时，responseRegion与mouseResponseRegion接口不再生效。从API version 22开始支持。 |
| 触摸测试控制 | 干预自身及其他组件收集结果。 | [hitTestBehavior](../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/通用属性/交互属性/触摸交互控制/触摸测试控制/ts-universal-attributes-hit-test-behavior.md#hittestbehavior) | 与onTouchIntercept效果相同，但是hitTestBehavior是静态配置。 |
| 自定义事件拦截 | 干预自身及其他组件收集结果。 | [onTouchIntercept](../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/通用事件/交互事件分发控制/自定义事件拦截/ts-universal-attributes-on-touch-intercept.md#ontouchintercept) | 当用户触发按下事件时，系统开始收集当前位置下所有需要参与事件处理的组件时触发，应用可通过该回调返回一个HitTestMode值，进而影响系统收集子节点或兄弟节点的行为。可以通过该回调达到动态控制交互响应的效果，如某些组件，根据业务状态的变化，可能有时候需要参与交互，有时候不需要参与交互。  与hitTestBehavior效果相同，但是onTouchIntercept是动态回调。 |

1. 触摸热区设置

   默认情况下，组件的响应热区即为组件自身的位置和大小，这与用户看到的范围相一致，从而最大程度地保证用户操作的手眼一致性。在极少数情况下，应用需调整热区大小以限制或扩大组件响应的操作范围。

   ArkUI提供了以下三个接口来设置组件的触摸热区：

   * **responseRegion**：设置一个或多个触摸热区，适用于所有输入设备类型（如触摸、鼠标等）。从API version 8开始支持。
   * **mouseResponseRegion**：设置一个或多个鼠标触摸热区，仅对鼠标事件生效。从API version 10开始支持。
   * **responseRegionList**：设置组件的触摸热区列表，可为每个热区指定适用的输入工具类型。调用该接口时，responseRegion与mouseResponseRegion接口不再生效。从API version 22开始支持。

   响应热区影响指向性事件的派发，通过与组件自身区域的相对关系进行指定，可以指定一个或多个区域，将组件的响应热区分割为多个部分。

   说明

   x和y可以设置正负值百分比。当x设置为'100%'时表示热区往右偏移组件本身宽度大小，当x设置为'-100%'时表示热区往左偏移组件本身宽度大小。当y设置为'100%'时表示热区往下偏移组件本身高度大小，当y设置为'-100%'时表示热区往上偏移组件本身高度大小。

   width和height只能设置正值百分比。width：'100%'表示热区宽度设置为该组件本身的宽度。比如组件本身宽度是100vp，那么'100%'表示热区宽度也为100vp。height：'100%'表示热区高度设置为该组件本身的高度。

   百分比相对于组件自身宽高进行计算。

   以下是一个绑定多个热区范围的示例：

   ```
   1. @Entry
   2. @Component
   3. struct FocusOnclickExample {
   4. @State text: string = '';
   5. @State number: number = 0;

   7. build() {
   8. Column() {
   9. Text(this.text)
   10. .margin({ bottom: 20 })
   11. // 请将$r('app.string.button')替换为实际资源文件，在本示例中该资源文件的value值为"按钮"
   12. Button($r('app.string.button'))
   13. .responseRegion([
   14. {
   15. x: 0,
   16. y: 0,
   17. width: '30%',
   18. height: '100%'
   19. }, // 第一个热区为按钮的左侧1/3区域
   20. {
   21. x: '70%',
   22. y: 0,
   23. width: '30%',
   24. height: '100%'
   25. },// 第二个热区为按钮的右侧1/3区域
   26. ])
   27. .onClick(() => {
   28. this.number++;
   29. this.text = 'button' + this.number + 'clicked';
   30. })
   31. .width(200)
   32. }.width('100%').justifyContent(FlexAlign.Center)
   33. }
   34. }
   ```

   [FocusOnclickExample.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkUISample/InterAction/entry/src/main/ets/pages/FocusOnclickExample/FocusOnclickExample.ets#L16-L51)

   上面的代码可以将按钮切分成了3部分，中间40%的区域不响应点击，而两侧的剩下部分可响应。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/10/v3/j5BPHyGXRLOj8fY30uzLFg/zh-cn_image_0000002622857777.png?HW-CC-KV=V1&HW-CC-Date=20260611T063143Z&HW-CC-Expire=86400&HW-CC-Sign=9BB67DC507E3F8199EABD28A44919A389FBBC5C11B6F7A3476AB5FC99FEF6C7C)
2. 触摸测试控制

   在组件上绑定[触摸测试控制](../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/通用属性/交互属性/触摸交互控制/触摸测试控制/ts-universal-attributes-hit-test-behavior.md)时，可能影响兄弟节点和父子节点的触摸测试。子组件对父组件的触摸测试影响程度取决于最后一个未被阻塞触摸测试的子组件状态。

   开发者可以通过配置触摸测试控制，来实现阻塞组件自身或其他组件的触摸测试。

   * HitTestMode.Default：默认不配hitTestBehavior属性，自身如果命中会阻塞兄弟组件，但是不阻塞子组件。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ce/v3/u-bmhjh1QRilnC9Ma2P7lg/zh-cn_image_0000002622697899.png?HW-CC-KV=V1&HW-CC-Date=20260611T063143Z&HW-CC-Expire=86400&HW-CC-Sign=B9536BF2923A4A2DD40B0FE3B485A2E94A0F77AA8AC512BF9202482BD69BDC50)
   * HitTestMode.None：自身不接收事件，但不会阻塞兄弟组件或子组件继续做触摸测试。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/eb/v3/xz5Lrgm4R66HeNIJolBwMQ/zh-cn_image_0000002592218338.png?HW-CC-KV=V1&HW-CC-Date=20260611T063143Z&HW-CC-Expire=86400&HW-CC-Sign=FBB5018895FE578D7D9D1119D7728B2F2472BC8013B6DA96B8107BF475CA073F)
   * HitTestMode.Block：阻塞子组件的触摸测试，如果自身触摸测试命中，会阻塞兄弟组件及父组件的触摸测试。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/76/v3/shQlviGDRReUe1P6PNb7Vw/zh-cn_image_0000002592378272.png?HW-CC-KV=V1&HW-CC-Date=20260611T063143Z&HW-CC-Expire=86400&HW-CC-Sign=F9FBE23F2520370D47468A9B5296CBF63D14C90EE94E777BE568D3688525E8F0)
   * HitTestMode.Transparent：自身进行触摸测试，同时不阻塞兄弟组件及父组件。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2e/v3/ecOHqKkzR8OcDuxxlIF-RQ/zh-cn_image_0000002622857779.png?HW-CC-KV=V1&HW-CC-Date=20260611T063143Z&HW-CC-Expire=86400&HW-CC-Sign=7F766FA196FEE44BBE72D017101148BEB31DE6982C486CC2CE03997BF90A6FB7)
   * HitTestMode.BLOCK\_HIERARCHY（从API version 20开始支持）: 自身和子节点响应触摸测试，阻止所有优先级较低的兄弟节点和父节点参与触摸测试。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a4/v3/bta4bA7dT3CJVnHArJS0zA/zh-cn_image_0000002622697901.png?HW-CC-KV=V1&HW-CC-Date=20260611T063143Z&HW-CC-Expire=86400&HW-CC-Sign=2AC2B93736EBD768FFDD86E505172075B302732A1A52EEA3B97A8F158A637087)
   * HitTestMode.BLOCK\_DESCENDANTS（从API version 20开始支持）: 自身不响应触摸测试，并且所有的后代（孩子，孙子等）也不响应触摸测试，不会影响祖先节点的触摸测试。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1c/v3/8B6f2tLtRjenBLFQs66PRw/zh-cn_image_0000002592218340.png?HW-CC-KV=V1&HW-CC-Date=20260611T063143Z&HW-CC-Expire=86400&HW-CC-Sign=8654849E63DE8480946FCF38D8DED180A923AC4741B6E5C9A7E620DEBB8AE77F)
3. 自定义事件拦截

   当用户执行按下操作时，将触发组件上绑定的[自定义事件拦截](../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/通用事件/交互事件分发控制/自定义事件拦截/ts-universal-attributes-on-touch-intercept.md)的回调。开发者可根据应用状态，动态调整组件的hitTestBehavior属性，进而影响触控测试的流程。

## 禁用控制

设置了[禁用控制](../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/通用属性/交互属性/禁用控制/ts-universal-attributes-enable.md)的组件及其子组件不会发起触摸测试过程，而是直接返回组件的父组件继续触摸测试。

## 安全组件

ArkUI包含的安全组件有：[使用粘贴控件](../../../../../系统/安全/程序访问控制/使用安全控件/使用粘贴控件/pastebutton.md)、[使用保存控件](../../../../../系统/安全/程序访问控制/使用安全控件/使用保存控件/savebutton.md)等。

安全组件当前对触摸测试影响：如果有组件的[z序](../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/通用属性/基础属性/Z序控制/ts-universal-attributes-z-order.md)比安全组件的z序靠前，且遮盖安全组件，则安全组件事件直接返回到父节点继续触摸测试。

## 事件冒泡

基础事件在响应链上的传递遵循冒泡机制，即最内层组件优先处理，再逐层往父组件传递该事件，任意一层组件可主动终止本次事件的继续传递，即终止冒泡。但需要注意的是，终止冒泡并不会中断父组件对手势的响应处理。

stopPropagation可终止冒泡。如下图所示，以Touch事件为例，当一个Touch事件传递至C节点时，如果调用了该事件上的stopPropagation接口，则B节点和root节点将不再接收到此事件，但B节点上的手势对象仍能接收和处理该Touch事件。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/60/v3/VmZ_Oc4mTIiq7gIXW4-xnA/zh-cn_image_0000002592378274.png?HW-CC-KV=V1&HW-CC-Date=20260611T063143Z&HW-CC-Expire=86400&HW-CC-Sign=C8554AC5911D7F35F896A63FF3E5F20F5CC2C5F09D979159AB29281C5A7D9E51)

说明

stopPropagation干预事件冒泡时，应注意对同一事件的不同类型（如Down/Move/Up）采用一致的规则，避免上层节点仅接收到部分类型事件，导致事件不闭环的情况，例如B节点仅接收到Down事件，而未接收到Up事件，这会影响B节点上的事件完整性（对于指向性按下操作类交互产生的事件，确保事件的完整性是必要的）。

## Cancel事件

当处理基础事件时，会发现存在多种具有Cancel类型的事件，如[TouchType](../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/公共定义/枚举说明/ts-appendix-enums.md#touchtype).Cancel、[MouseAction](../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/公共定义/枚举说明/ts-appendix-enums.md#mouseaction8).CANCEL等。系统在特定场景下发送此类事件，例如在拖拽操作中，当通过手指或鼠标拖动一个支持拖拽（onDragStart）的对象时，由于拖拽动作需达到一定位移阈值才能触发，因此在触发[onDragStart](../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/通用事件/交互响应事件/拖拽事件/ts-universal-events-drag-drop.md#ondragstart)之前，应用将正常接收到Touch或Mouse事件。一旦拖拽动作开始，系统将发送Cancel事件，告知应用普通基础事件已结束。

Cancel的含义与Up相同，均表示事件处理结束。若在处理Up/Release的场景中，亦应同时处理Cancel。
