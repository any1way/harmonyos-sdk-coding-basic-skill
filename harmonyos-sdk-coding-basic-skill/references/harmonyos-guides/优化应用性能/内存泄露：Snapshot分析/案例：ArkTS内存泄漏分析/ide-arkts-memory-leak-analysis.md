---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-arkts-memory-leak-analysis
title: 案例：ArkTS内存泄漏分析
breadcrumb: 指南 > 优化应用性能 > 内存泄露：Snapshot分析 > 案例：ArkTS内存泄漏分析
category: harmonyos-guides
scraped_at: 2026-06-11T15:31:36+08:00
doc_updated_at: 2026-05-07
content_hash: sha256:eda28f7fb2da4527f15ee6ae188f57364d49eca70bc3d328aa4269faeb1ad5f0
---
本案例介绍如何判断应用存在ArkTS泄漏，以及如何通过快照对比找出ArkTS内存泄漏的原因。

## 初步识别内存问题

1. 使用[实时监控功能](../../使用Profiler进行性能调优/性能问题定界：实时监控/realtime-monitor.md)对应用的内存资源进行监控。正常操作应用，观察运行过程中Memory泳道的变化。

   当在一段时间内应用内存没有明显增加或者在内存上涨后又逐渐回落至正常水平，则基本可以排除应用存在内存问题；反之，在一段时间内不断上涨且无回落或者内存占用明显增长超出预期，那么则可初步判断应用可能存在内存问题。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/16/v3/nkJ3ek_-RfC1_bLDPhKtcA/zh-cn_image_0000002571387350.png?HW-CC-KV=V1&HW-CC-Date=20260611T073135Z&HW-CC-Expire=86400&HW-CC-Sign=51967D211C32CF0629F9967B5A8CE0D39CBA26DF0138D87A329485BB786F0B35 "点击放大")
2. 当从实时监控页面初步判断应用可能存在内存问题后，通过[深度录制](../../使用Profiler进行性能调优/性能问题定位：深度录制/deep-recording.md)抓取应用内存在问题场景下的详细数据，初步定界问题出现的位置。Memory泳道存在Allocation或Snapshot模板中，使用Allocation或Snapshot模板录制均可。
3. 以Allocation模板为例，创建模板后，将模板中的其余泳道去除勾选，仅录制Memory泳道的数据。

   说明

   其余泳道会抓取内存分配、内存对象等数据，为避免额外开销和影响分析，建议先排除录制。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/75/v3/s5u2L5erSkyq_w9EJk30sA/zh-cn_image_0000002571546988.png?HW-CC-KV=V1&HW-CC-Date=20260611T073135Z&HW-CC-Expire=86400&HW-CC-Sign=527F344F1317A62102589709EFA2FAE2BE6A518F746C397C63BAC1720BAFFFC9)
4. 点击三角按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e7/v3/J686077vTESSA_Cdr_G1QA/zh-cn_image_0000002602186535.png?HW-CC-KV=V1&HW-CC-Date=20260611T073135Z&HW-CC-Expire=86400&HW-CC-Sign=5C945706F4A3DF4662D922125ECB16D9EB066C9E5E6EAD211E848BBD6031869F)即开始录制。
5. 录制过程中，不断操作应用在问题场景的功能，将问题放大，便于快速定界问题点。
6. 点击下图中方块按钮或者左侧停止按钮结束录制。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6a/v3/qK1wzZPUTyOFaXOYqCvQfA/zh-cn_image_0000002602186539.png?HW-CC-KV=V1&HW-CC-Date=20260611T073135Z&HW-CC-Expire=86400&HW-CC-Sign=01CCCCA0AA1683B96396B7B0B9268B7F70ACC1F181A914B6D872AD001EB46E96 "点击放大")
7. 录制完成后，展开Memory泳道，其中ArkTS Heap表示方舟虚拟机内存，这部分内存受到方舟虚拟机的管控。当ArkTS Heap有明显的上涨，说明在方舟虚拟机内的堆内存上可能存在内存泄漏，可以使用Snapshot模板进行下一步分析。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/da/v3/NYr34QB8RjyxzyfUoHa-Fw/zh-cn_image_0000002602066475.png?HW-CC-KV=V1&HW-CC-Date=20260611T073135Z&HW-CC-Expire=86400&HW-CC-Sign=4E62615B29EA41629BB0C322D240A58287B175F39609A01112E0D5BEA5524EC8 "点击放大")

## 使用Snapshot模板分析ArkTS内存问题

分析内存泄漏问题步骤如下：

1. 使用Snapshot模板录制数据；
2. 在问题场景前拍摄快照；
3. 触发问题场景后，再次拍摄快照；
4. 对比两次快照的数据，可快速找到泄漏对象并做进一步分析；
5. 当有多个对象在比较视图都存在时，可以重复多次触发问题场景后拍摄快照，分别和问题场景前拍摄的快照进行对比，观察是否有对象出现明显的线性变化趋势，进一步缩小泄漏对象的范围。

### 录制模板数据

1. 连接设备后启动应用，点击应用选择框选择需要录制的应用，选择**Snapshot**模板，点击Create Session或双击Snapshot图标即可创建一个Snapshot的录制模板。
2. 创建模板后，点击三角按钮即开始录制。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/25/v3/9txmGwN9Qh-NGgzDFjik5g/zh-cn_image_0000002571387358.png?HW-CC-KV=V1&HW-CC-Date=20260611T073135Z&HW-CC-Expire=86400&HW-CC-Sign=1B7834130318FDA72BCDE9491E8108CBBF32B07E5403A86458EFD8251E622680 "点击放大")
3. 待右侧泳道全部显示recording后则表明正在录制中。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2c/v3/5O0ZgIOaR_OKh8UCBvkPCw/zh-cn_image_0000002602186541.png?HW-CC-KV=V1&HW-CC-Date=20260611T073135Z&HW-CC-Expire=86400&HW-CC-Sign=0A956028BDA719F61B0DAF670C9C4C8E42FFD0D3D646C612B51B372351577FA4 "点击放大")
4. 拍摄第一次堆快照作为基准（点击图中①处拍摄按钮，待②处显示出紫色条块表示快照拍摄完成）。

   说明

   方舟虚拟机提供了在获取快照前自动GC（Garbage Collection，对堆内存进行垃圾回收）的能力，因此拍摄快照之前不用主动触发GC。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/33/v3/aR0zOTnSSv-p3FY_wMYR1Q/zh-cn_image_0000002602186533.png?HW-CC-KV=V1&HW-CC-Date=20260611T073135Z&HW-CC-Expire=86400&HW-CC-Sign=74F28E2DABD35A344A3C2CF84CB6D46705DB314748522FD3A0A4716C76469F82 "点击放大")
5. 多次触发内存泄漏操作。可以操作5，7，11等这种特殊的次数。比如操作了5次对比两个快照发现有很多创建了5次没释放的场景，则可能存在内存泄漏，再操作7次，如果创建了7次那就可以确认发生了泄漏。
6. 拍摄第二次堆快照。
7. 点击下图中方块按钮或者左侧停止按钮结束录制。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/30/v3/zNS8TAp9RKKpTyiqQJYd5g/zh-cn_image_0000002571387372.png?HW-CC-KV=V1&HW-CC-Date=20260611T073135Z&HW-CC-Expire=86400&HW-CC-Sign=101CF01D0213A4C3BE0592464B573406C010B9E16A9024165D05D5FFCE290862 "点击放大")

### 分析ArkTS Heap

1. 在每次拍摄堆快照之前，虚拟机都会触发GC，所以理论上堆快照内存在的对象都是当前虚拟机已经无法GC掉的对象。我们可以将两个堆快照进行比较，来查看哪些对象是在触发问题场景时新增了且不能释放的。切换到窗口下方详情区域的“Comparison”页签，将两次快照进行对比。图中数据的含义是以Snapshot2作为基准，Snapshot2对比Snapshot1的数据变化量。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/31/v3/rhEsyG4zSnqkbHyLVp5hig/zh-cn_image_0000002571547010.png?HW-CC-KV=V1&HW-CC-Date=20260611T073135Z&HW-CC-Expire=86400&HW-CC-Sign=BFB06E922A84E53B39AC666457211242697042AC68CE9C422AFB475096B1098D "点击放大")
2. 优先寻找与触发内存泄漏操作次数强相关、与业务代码强相关的Constructor，首先来分析这些对象是否正常。主要是按照Distance逐渐减小的方式找引用链，可以从references里面一层层去寻找，排查引用链上的可疑对象（一般指与业务代码关联的对象）。

   说明

   选择一个实例节点，系统会计算从GC Roots到选定对象的最短路径，并在右侧Shortest Paths页签实时切换和展示。

## 分析Snapshot数据

### 常见对象介绍

**JSArray**

目前所有JSArray展开后为数组里的各个元素：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4b/v3/GS-0FQWkRsGlpORvt8y-5Q/zh-cn_image_0000002571387346.png?HW-CC-KV=V1&HW-CC-Date=20260611T073135Z&HW-CC-Expire=86400&HW-CC-Sign=9A024264798D032CB6E2486CDE5A32FAFEA88A212E11C8D009F8B58696E36EF4)

其中\_\_proto\_\_：原型对象，所有数组的\_\_proto\_\_应该是一致的；length：内置属性访问器，可以访问数组长度。

**TaggedDict**

位于(array)标签中，一般为虚拟机内部创建的字典，ArkTS代码层面不可见。

**TaggedArray**

位于(array)标签中，一般为虚拟机内部创建的数组，ArkTS代码层面不可见。

**COWArray**

位于(array)标签中，一般为虚拟机内部创建的数组，ArkTS代码层面不可见。

**JSObject**

JSObject展开后为内部的各个属性如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/13/v3/jP68pJeqQoaCPWjGBFokFg/zh-cn_image_0000002602066463.png?HW-CC-KV=V1&HW-CC-Date=20260611T073135Z&HW-CC-Expire=86400&HW-CC-Sign=07FEB504FC127B7BD750C85EE8A5849603633A20C167B94A1984C4F981FE8CBC)

以下通过具体代码来介绍下实例化对象、声明对象、构造函数间的关系：

```
1. // HelloWorldPage.ets
2. class People {
3. old: number
4. name: string
5. constructor(old: number, name: string) {
6. this.old = old;
7. this.name = name;
8. }
9. printOld() {
10. console.log("old = ", this.old);
11. }
12. printName() {
13. console.log("name = ", this.name);
14. }
15. }

17. @Entry
18. @Component
19. struct HelloWorldPage {
20. @State message: string = 'Hello World';
21. private people: People = new People(20, "Tom");

23. build() {
24. Row() {
25. Column() {
26. Text(this.message)
27. .fontSize(50)
28. .fontWeight(FontWeight.Bold)
29. }
30. .width('100%')
31. }
32. .height('100%')
33. }
34. }
```

采集到的snapshot数据如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/30/v3/tjtwm7UpRBOuW-6SMy-qhA/zh-cn_image_0000002571546992.png?HW-CC-KV=V1&HW-CC-Date=20260611T073135Z&HW-CC-Expire=86400&HW-CC-Sign=BC033D16EA63FB2A676D67DFE652958E7EE06571026303B4C2279A4B72F923DD)

202169对象对应的是People，其主要声明了对象的属性和方法。

实例化对象的\_\_proto\_\_属性指向声明时的对象，声明对象里则会有constructor构造函数。当实例化多个对象时，实例化对象会有多个，但是声明对象和构造函数只有一个。

**JSFunction**

目前所有JSFunction都在(closure)标签中，展开即可看到所有JSFunction：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/73/v3/BjMoDoVYScG0L2QMGKCHzQ/zh-cn_image_0000002602186531.png?HW-CC-KV=V1&HW-CC-Date=20260611T073135Z&HW-CC-Expire=86400&HW-CC-Sign=0025A01BC46C79FA1A04B7AEEC9A91C41E3708D3C8C8A44A85EB8CB0842EDC80 "点击放大")

每个函数展开后为函数内的各个属性：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ac/v3/Vuxt5Jp3SxqVYtWFpvG1rg/zh-cn_image_0000002571547012.png?HW-CC-KV=V1&HW-CC-Date=20260611T073135Z&HW-CC-Expire=86400&HW-CC-Sign=A59C9CA79305538053819C0366288C02A6CEB74A1C0B874709FAE22C6D19E2AF)

其中HomeObject表示父类对象，即该方法属于哪个对象；\_proto\_表示原型对象；LexicalEnv表示该函数的闭包上下文；name是内置属性访问器，可获取函数名；FunctionExtraInfo表示额外信息，比如一些napi接口会在这里记录函数地址；ProtoOrHClass表示原型或者隐藏类。

如果函数显示为anonymous()，则表示为匿名函数；如果函数显示为JSFunction()，则表示该函数可能为框架层函数，创建函数的时候未设置函数名。对于这两种函数名不可见的情况，可以通过查看其引用来间接确认其名称：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f4/v3/oy6odPFOS4ygPJDlvK1nng/zh-cn_image_0000002602066469.png?HW-CC-KV=V1&HW-CC-Date=20260611T073135Z&HW-CC-Expire=86400&HW-CC-Sign=48BB07599F2640EFC91E4B59485F06E2F6200CCBCA101B22FEEE12232E2E5F18)

**ArkInternalConstantPool**

虚拟机创建的常量池，ArkTS代码层面不可见，涉及到的字符串常量会在(array)标签中展示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/64/v3/mCsvulSnSlWG9FqPqP2gQA/zh-cn_image_0000002602066473.png?HW-CC-KV=V1&HW-CC-Date=20260611T073135Z&HW-CC-Expire=86400&HW-CC-Sign=50EF741F02284791723BC2358036AB45646C959B8681E74EAA496A5A7C37692F "点击放大")

**LexicalEnv**

闭包变量上下文；闭包是一个链状结构，如下所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/16/v3/BXH4_0a6Q8ufEQONi4bZIQ/zh-cn_image_0000002602186519.png?HW-CC-KV=V1&HW-CC-Date=20260611T073135Z&HW-CC-Expire=86400&HW-CC-Sign=E861F36177C3BA94E15AF45B41F7DF0CA1A2C5690F178FACAB72218EBCC14A91)

733这个节点本身是一个闭包数组，其中0号元素是调用者（或者再往上的调用者，以此类推）的闭包；1号元素存储的是调试信息；2号及以后的元素存储的就是闭包传递的变量，上例传递了一个变量。

**InternalAccessor**

内置属性访问器，会有getter和setter方法，通过getter、setter可以获取、设置该属性。

**LocalHandleRoot**

DevEco Studio 6.1.0 Release版本新增，位于(handle)标签中，用于管理JS对象生命周期的引用句柄（napi\_value）。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/89/v3/iAsJtGTiRBOVLB4xKJulfQ/zh-cn_image_0000002602186537.png?HW-CC-KV=V1&HW-CC-Date=20260611T073135Z&HW-CC-Expire=86400&HW-CC-Sign=DF3E805AA4C9D343A44EB0CB59C545917D0DC0B6FD98F098D0077F03E7839FEF)

**GlobalHandleRoot**

DevEco Studio 6.1.0 Release版本新增，位于(handle)标签中，允许用户管理ArkTS/JS值的生命周期的引用句柄（napi\_ref）。

### 常见属性介绍

| 属性 | 含义 |
| --- | --- |
| \_\_proto\_\_ | 原型对象 |
| (object elements) | 对象元素 |
| (object properties) | 对象属性 |
| hclass | 隐藏类 |
| ArkInternalHash | ArkTS运行时内部的哈希值 |
| ProtoOrHClass | 原型或隐藏类指针 |
| RawProfileTypeInfo | 运行时类型剖析信息 |
| HomeObject | 父类对象 |
| FunctionKind | 函数类型标识 |
| FunctionExtraInfo | 函数附加信息 |
| prototype | 构造函数或类对象关联的原型对象 |
| Inlineproperty | 内联属性 |

### 分析方法

**查看对象名称**

对于声明对象，可以通过constructor属性来确定对象名称。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e7/v3/nX8EUitgTX2syJSmsuvxrg/zh-cn_image_0000002602186547.png?HW-CC-KV=V1&HW-CC-Date=20260611T073135Z&HW-CC-Expire=86400&HW-CC-Sign=09675F810151FA08EE8ADF9F39388405FA0F615E1E0CB099469069D56CB9EBD7)

对于实例化对象，一般没有constructor，则需要展开\_\_proto\_\_属性后查找constructor；

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/18/v3/4q-IM4OyQK2hgcNYc_zOKQ/zh-cn_image_0000002602186549.png?HW-CC-KV=V1&HW-CC-Date=20260611T073135Z&HW-CC-Expire=86400&HW-CC-Sign=D075824EADE600521A0F743836BA553917DB83D1944F5C2D838983164638725E)

若对象里有一些标志性属性，可以通过在代码里搜索属性名称来找到具体是哪个对象。

如果对象间有继承关系，则可以继续展开\_\_proto\_\_：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/be/v3/z7jp5iAjQTGfdpgGHiu6sA/zh-cn_image_0000002571547014.png?HW-CC-KV=V1&HW-CC-Date=20260611T073135Z&HW-CC-Expire=86400&HW-CC-Sign=FE432CB69368BCE81686AFBFECAD3FDF79B3BA2DBE8A7C329F212815E82DD6D3)

如上图则表明Man对象继承自People对象。
