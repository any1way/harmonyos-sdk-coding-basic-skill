---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-application-cold-start-optimization
title: 应用冷启动时延优化
breadcrumb: 最佳实践 > 性能 > 性能场景优化案例 > 应用启动与响应优化 > 应用冷启动时延优化
category: best-practices
scraped_at: 2026-06-12T10:15:51+08:00
doc_updated_at: 2026-05-30
content_hash: sha256:9ae1f0233e409e0da14515584c4ae79b4e9cc5c2119be241862e9009b050055b
---
## 概述

应用启动时延是影响用户体验的关键要素，是指从用户点击桌面应用图标、通知或其他入口启动应用，到应用界面内容成功加载并显示在屏幕上的时间间隔。如果这段时间超过3秒，将显著影响用户体验。

应用启动可分为冷启动、热启动和温启动三种类型:

* 冷启动是指当应用启动时，后台未存在该应用的进程，系统需为其创建新进程。完整的冷启动过程，指从用户点击桌面图标开始，至应用首页首帧渲染完成、数据完全展示。
* 热启动是指当应用已在后台运行且进程驻留在内存中时，用户再次打开应用，系统可直接从内存恢复应用状态，无需重新初始化加载资源。
* 温启动是指应用进程存在，但主实例或页面已被销毁。此时启动应用只需重新创建实例或页面，启动速度介于冷启动与热启动之间。

冷启动的启动过程最为复杂、整体耗时也最长，是影响应用启动体验的关键短板，因此本文将主要介绍冷启动时延问题的优化。

当应用冷启动时延大于1100ms时，可以认为是应用启动缓慢，体验标准可以参考[应用流畅体验设计](../../../性能体验设计/bpta-smooth-application-design.md)。

* [应用冷启动流程](bpta-application-cold-start-optimization.md#section196451814101216)
* [应用冷启动时延检测](bpta-application-cold-start-optimization.md#section860412154015)
* [应用冷启动时延问题分析](bpta-application-cold-start-optimization.md#section167931444111612)
* [识别启动缓慢问题](bpta-application-cold-start-optimization.md#section8516174361218)
* [提升应用冷启动速度](bpta-application-cold-start-optimization.md#section1770316268136)

## 应用冷启动流程

优化应用冷启动体验前，了解应用冷启动的流程和重要生命周期。应用冷启动分为5个阶段：应用进程创建&初始化、Application&Ability初始化、Ability/AbilityStage生命周期、加载绘制首页、网络数据二次刷新。

**图1** 应用冷启动流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/15/v3/2vj4FzJyS9yAJhcci2FGyg/zh-cn_image_0000002512014501.png?HW-CC-KV=V1&HW-CC-Date=20260612T021549Z&HW-CC-Expire=86400&HW-CC-Sign=75ED5BC6E5BD960D015A7329A933426389A8DA233CECB0329DE67DA54A3DAB42 "点击放大")

1. 应用进程创建和初始化阶段：此阶段系统完成应用进程的创建和初始化，包括启动页图标（startWindowIcon）的解码。
2. Application和Ability初始化：该阶段包括资源加载、虚拟机创建、Application&Ability 对象的创建与初始化、依赖模块加载等。
3. Ability/AbilityStage 生命周期：此阶段主要涉及 AbilityStage/Ability 的启动，执行相应的生命周期回调。
4. 加载首页内容，测量布局，刷新组件并绘制。
5. 网络数据二次刷新：此阶段应用根据业务需求对网络数据进行请求、处理和刷新。

若要提升应用冷启动速度，需缩短上述阶段的耗时。

## 应用冷启动时延检测

在应用开发中，网络请求时机、图片下载、页面资源加载、依赖模块的加载等，都会导致应用冷启动时延受到影响，合理处理代码逻辑可以提升应用冷启动速度。开发者可以通过[AppAnalyzer](../../../性能检测/开发态性能检测/bpta-performance-detection.md#section135451444171)对应用冷启动进行检测，针对诊断出的应用冷启动不达标问题进行分析和优化。

应用冷启动时延检测步骤如下：

1. 选择entry模块，暂时关闭模块build-profile中的混淆开关。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/49/v3/LxGz-ZXVRnms5E-uUmnmiw/zh-cn_image_0000002510840649.png?HW-CC-KV=V1&HW-CC-Date=20260612T021549Z&HW-CC-Expire=86400&HW-CC-Sign=890042765251B224CD27AA005716E1EA51F620E8FEA136AAD29B9B571470A72C "点击放大")
2. 检查一下build模式，改为release。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ec/v3/O6dfPpRaSYmkVfQOUkwtRA/zh-cn_image_0000002478640720.png?HW-CC-KV=V1&HW-CC-Date=20260612T021549Z&HW-CC-Expire=86400&HW-CC-Sign=B45E0ADF485E8BB8632A5CE5C9D17507B84F2248AEAC1E29DA7F9AD7D00E6506)
3. 点击菜单 -> tool -> AppAnalyzer，打开体检工具。
4. 选择“场景化体检”，点击“手动性能冷启动体检”。

   工具开始准备，会自动编译、安装、运行当前工程，此时需要“保持手机解锁状态”，当准备完成后，会提示点击开始按钮，开始体检。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/68/v3/_inb1FTISqmU4r-L5ekbQg/zh-cn_image_0000002478800706.png?HW-CC-KV=V1&HW-CC-Date=20260612T021549Z&HW-CC-Expire=86400&HW-CC-Sign=81A7411B6E9886005FEBE6D6DEF9CEC96D5C57CDFD205ACE930303AB3A658386 "点击放大")
5. 根据提示在设备上进行手动操作：
   1. 首先，在最近任务列表关闭应用。
   2. 进入手机设置 ，在顶部搜索栏中输入应用名并，点击进入应用设置界面，如果该应用还有进程存活，在应用设置界面可以点击强行停止按钮。
   3. 在桌面点击应用图标重新启动应用。
   4. 点击“结束”按钮停止体检任务，体检工具会将刚才的操作数据进行解析。

说明

冷启动体检需要强行停止应用：

1. 进入手机设置。
2. 在顶部搜索栏中输入应用名并点击进入应用设置界面。
3. 在应用设置界面点击强行停止。
4. 在桌面启动待检测的应用。

## 应用冷启动时延问题分析

AppAnalyzer详情报告中会显示动态检测可能导致冷启动完成时延不达标的故障原因，并提供相应的优化建议，此处列举以下冷启动时延不达标问题原因进行说明：

### **高耗时非UI操作**

高耗时函数可能会造成应用卡顿，对于执行次数较多的函数，应尽量减少调用次数，单次执行但总耗时较高的函数，可以考虑通过异步方式进行优化。

在检测结果中，开发者可以通过点击报告表格中的对应方法名，快速跳转至对应代码片段，同时体检工具也会给出相应的优化建议，如将耗时函数放到子线程或进行缓存、使用多线程能力等，详细流程及示例可参考文档：[主线程耗时操作优化--其他主线程优化思路](../../界面渲染性能优化/主线程耗时操作优化/bpta-time-optimization-of-the-main-thread.md#section4365993361)。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/56/v3/cJZjlnECTAu_jnhP49uW2g/zh-cn_image_0000002510841011.png?HW-CC-KV=V1&HW-CC-Date=20260612T021549Z&HW-CC-Expire=86400&HW-CC-Sign=0737FD416A65C2EF540C726966444CA2680858631225564F66389F88E9E7A3CD "点击放大")

### **import加载耗时**

体检工具可以检测出应用冷启动过程中累计加载的文件数量、未使用的文件数量和加载总耗时，开发者可参考以下优化思路和流程，对此类冷启动问题进行优化。

**import加载耗时问题优化思路**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fc/v3/fUs0sxCdSUKplTT_Zr5koQ/zh-cn_image_0000002510761277.png?HW-CC-KV=V1&HW-CC-Date=20260612T021549Z&HW-CC-Expire=86400&HW-CC-Sign=383B684422FD9737F330608CB5CB5F9700D96815C144890219032D8B199BB15B "点击放大")

1. 分析模块使用情况：查看总结信息和未使用文件import列表信息，包括加载文件总耗时，和未使用文件数量和总耗时，了解未使用文件import情况。
2. 查找依赖关系优化导入：点击第一个“下载”按钮下载全量依赖关系文件，使用调用链搜索框查找未使用文件依赖关系，结合代码逻辑对未使用文件进行延迟加载。
3. 标记优化状态：点击第二个“下载”按钮下载全量import清单文件，统计已优化和未优化的未使用文件，分析全量文件的依赖关系。
4. 再次进行冷启动检测：优化耗时最多的几个文件之后，再次进行冷启动检测，验证整改收益。在逐步优化未使用文件导入的过程中，收益会逐步降低，开发者需根据实际情况是否需要继续“lazy import”的整改。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a1/v3/LohY-RZaT_SWqO5cYdNUCw/zh-cn_image_0000002478801360.png?HW-CC-KV=V1&HW-CC-Date=20260612T021549Z&HW-CC-Expire=86400&HW-CC-Sign=58FD55A4ADD8F5D9869C1B61D9D86C766F57C402AC1697EB758BB2501C5BBA5F "点击放大")

**import加载耗时问题优化流程**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/54/v3/6eHbhTm1QdCQ1zHMzejt0g/zh-cn_image_0000002478641376.png?HW-CC-KV=V1&HW-CC-Date=20260612T021549Z&HW-CC-Expire=86400&HW-CC-Sign=2CB243E974A026ABA35F8CEEABAB377587E91047857C40D7051D7CC1B2F45504 "点击放大")

1. 查找耗时最高的未使用import文件。

   在本地浏览器中打开下载的依赖关系的文件full\_dependency.html，视图中左侧列表表示已加载未使用的文件，并且按照耗时从高到低排序；右侧表示已使用文件，开发者需要关注未使用文件中耗时较多的几个文件导入，例如DetailView文件的导入。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/64/v3/_ByuuqjBSFGv58N1oqhEwA/zh-cn_image_0000002510841309.png?HW-CC-KV=V1&HW-CC-Date=20260612T021549Z&HW-CC-Expire=86400&HW-CC-Sign=85DDE6B5680B8B56133C0870547271BB837E50F0EDEFC86B1AADD51DD9D27A1F "点击放大")
2. 根据文件名检索文件调用关系链。

   在搜索框中通过文件名DetailView进行检索，该文件的依赖关系则会在下方节点视图中展示，并且默认会展示其子节点的使用情况，未使用的文件会被标红显示。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/77/v3/2UXvNvHBSXeE9u3IJQ3IQQ/zh-cn_image_0000002510761285.png?HW-CC-KV=V1&HW-CC-Date=20260612T021549Z&HW-CC-Expire=86400&HW-CC-Sign=27FB196775ECDE83106945BC490BBCFD7D983A01002A13FED80C6B53F3E16645 "点击放大")
3. 查看检索文件的上层和下层文件节点信息。

   查找上层文件节点信息，即目标文件被导入的位置；查找下层文件节点信息，目标文件的耗时是否由其子节点导致，如果下层文件耗时较长，则需要考虑优化子节点的导入。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a2/v3/CIOhoTc-R2GYet9yA2Nbyg/zh-cn_image_0000002478801366.png?HW-CC-KV=V1&HW-CC-Date=20260612T021549Z&HW-CC-Expire=86400&HW-CC-Sign=854B841A3D4B48EC2085844FD1894D3F6FDDA1BA39CC90179B97F8B07F2D0736 "点击放大")
4. 判断上层文件是否为为其他module的Index.ets文件导出。
   * 如果上层文件不为其他module的统一对外暴露接口文件（例如Index.ets），则可以在上层文件中使用对该模块使用lazy import进行优化。

     ```
     1. import lazy { DetailView } from '../view/DetailView';

     3. @Entry
     4. @Component
     5. struct Index {
     6. build() {
     7. // ...
     8. }
     9. }
     ```
   * 如果上层文件为其他module的统一对外暴露接口文件（例如Index.ets），则需要通过import路径展开性能优化。

     例如CustomLayout1上层模块为library模块的Index.ets，其中有多个文件导出。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3b/v3/jDc9NtHjQpqmFDz3o7HueA/zh-cn_image_0000002478641380.png?HW-CC-KV=V1&HW-CC-Date=20260612T021549Z&HW-CC-Expire=86400&HW-CC-Sign=77415C3B07F8898E713DD0B6AEEB10DF174A01017F59093F041CE09C25EE7207 "点击放大")

     在Entry的首页通过依赖对应模块引入，会导致冷启动阶段将CustomLayout2和CustomLayout3等冷启动阶段无用的文件导入。

     ```
     1. // entry/src/main/ets/pages/Index.ets
     2. import { CustomLayout1 } from 'library';
     ```

     具体优化方案，则是通过在import时，对路径展开进而优化性能。

     ```
     1. // entry/src/main/ets/pages/Index.ets
     2. import { CustomLayout1 } from 'library/src/main/ets/pages/CustomLayout1';
     ```
5. 在导出文件中标记已修改的文件。

   在下载全量import文件清单表格中，标记已优化的未使用文件，便于优化备忘，特别是当需要优化的文件比较多的时候。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/48/v3/2XjYTpU-SfeHn5BnPmJC7w/zh-cn_image_0000002510841315.png?HW-CC-KV=V1&HW-CC-Date=20260612T021549Z&HW-CC-Expire=86400&HW-CC-Sign=8E3DD2D842D96F2EBA28C8132955FD3EFD3E463472805825B8B7BA73672CF552 "点击放大")
6. 重新进行冷启动场景化检测。

   当优化完成后，重新进行冷启动场景化检测，查看优化收益是否达到预期，如未达到预期，则需要重新进行分析优化。

### **网络请求耗时**

应用首页内容需要通过网络请求获取数据并显示时，网络请求耗时和网络请求发起的时机，对应用冷启动时长会产生一定影响。使用AppAnalyzer能够检测出应用中请求URL的请求耗时和点击离手到请求发起间隔。

* 网络请求本身耗时长

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/17/v3/XyAbZH3JSTu3GiGEnn-0Iw/zh-cn_image_0000002478801796.png?HW-CC-KV=V1&HW-CC-Date=20260612T021549Z&HW-CC-Expire=86400&HW-CC-Sign=6CE1882B74C7D149822C8461F19F73D92D008687334863BB20DA102448090BE2 "点击放大")

  网络请求本身是否耗时可通过检测结果中的请求耗时时长来进行判断，时间越长，则网络请求本身耗时越久。详细分析请参考：[网络诊断：Network分析](../../../../../harmonyos-guides/优化应用性能/网络诊断：Network分析/ide-profiler-network.md)。

  网络请求本身耗时长，可对该URL请求进行预连接和预解析来优化网络传输速度，提前完成DNS查询和TCP/TLS握手，即在应用启动或空闲时提前建立并维护一个持久的连接池；还可以使用CDN来优化网络传输速度，即将静态资源部署到CDN上。
* 网络请求发起太晚

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/28/v3/KuVPf5N4Qg6R-3szo3_htw/zh-cn_image_0000002478641822.png?HW-CC-KV=V1&HW-CC-Date=20260612T021549Z&HW-CC-Expire=86400&HW-CC-Sign=8EE0D7CC8A581D5635B91731B61874DA59FD3C5A7EDBE781F943B7B3DDC06F85 "点击放大")

  点击离手到请求发起间隔则表示用户进行点击操作后，到真正向服务器发起网络请求的那一刻止，这中间所经过的时间。可通过检测结果中的点击离手到请求发起间隔时长来进行判断，时间越长，则表示网络请求发起的越晚。可通过提前发起网络请求，来进行优化。可参考：[网络请求提前发送](bpta-application-cold-start-optimization.md#section199911250658)。

如果开发者既无法优化网络请求本身耗时，也无法将网络请求提前发起，可以考虑提前将网络请求数据缓存，下次冷启动时候直接加载缓存数据，再通过发送网络请求二刷刷新数据。

### **首页组件复杂度高导致构建耗时**

首页组件复杂度较高会影响首页加载绘制耗时，AppAnalyzer工具能检测出页面中组件自身创建是否耗时过长。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a/v3/gjjeyvLlSdqhGe2AW6Vjpw/zh-cn_image_0000002478641864.png?HW-CC-KV=V1&HW-CC-Date=20260612T021549Z&HW-CC-Expire=86400&HW-CC-Sign=0C5F906755E772FC339F02ABC714716666BC68D7EA049FDF924E7CEA92F36877 "点击放大")

在静态检测可能故障原因表格中，可点击源文件定位到创建耗时的UI组件，根据提供的可能故障原因，去对UI组件进行相应优化修改，即可减少该UI组件自身创建耗时。

开发者可采用以下方式，控制UI的渲染范围，防止页面卡顿或掉帧：

* **合理控制元素显示与隐藏**

  在应用开发中，控制页面元素的显示与隐藏是一种常见的场景，通过Visibility.None、if条件判断等都能够实现该效果。visibility属性可以控制元素在布局阶段是否参与布局渲染，if条件判断控制的是组件的创建、布局阶段。
* **懒加载**

  懒加载LazyForEach是一种延迟加载的技术，通常应用于长列表优化、瀑布流优化等数据量较大、子组件可重复使用的场景，当用户滚动页面到相应位置时，才会触发资源的加载，以减少组件的加载时间，提高应用性能，提升用户体验。

### **异步线程阻塞主线程**

当主线程长时间等待子线程或异步函数返回，会造成主线程长时间被阻塞，可能导致时延不达标的情况。体检工具会对主线程长时间被阻塞进行检测，可以根据检测结果中主线程空闲时间判断主线程是否长时间被阻塞，空闲时间越长，则阻塞时间越久，详细请参考：[主线程长时间被阻塞](../../../性能分析/点击完成时延分析/bpta-click-to-complete-delay-analysis.md#section73671398291)。

## 识别启动缓慢问题

开发者需要分析启动过程的耗时瓶颈，优化应用或服务的冷启动速度时，可使用Profiler的Launch场景分析功能，录制启动过程中的关键数据，识别启动缓慢的原因。Profiler Launch可拆解应用冷启动过程，抓取各阶段的耗时数据，帮助开发者快速分析冷启动过程的耗时瓶颈。Launch的具体使用方法参见[冷启动分析：Launch分析](../../../../../harmonyos-guides/优化应用性能/冷启动：Launch分析/ide-launch-overview.md)。

已录制一段Launch任务，具体操作步骤请参考[性能问题定位：深度录制](../../../../../harmonyos-guides/优化应用性能/使用Profiler进行性能调优/性能问题定位：深度录制/deep-recording.md)。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3f/v3/oXaylPCMTuehbZGjzW3M-g/zh-cn_image_0000002193851180.png?HW-CC-KV=V1&HW-CC-Date=20260612T021549Z&HW-CC-Expire=86400&HW-CC-Sign=D003145F33619EB3AB22B64E31EA3D9BFE9FAA9B96C3AE0541DD5D7CA2A9128A "点击放大")

上图显示，Launch将应用的冷启动过程分为以下几个阶段：

1. Create Process：应用进程创建阶段，对应的trace打点为AppMgrServiceInner::StartProcess。
2. Application Launching：应用启动阶段，对应的trace打点为AppMgrServiceInner::AttachApplication##{bundleName}。
3. UIAbility Launching：UIAbility启动阶段，对应的trace打点为MainThread::HandleLaunchAbility##{bundleName}。
4. UI Ability OnForeground：应用进入前台阶段，对应的 trace 打点为 AbilityThread::HandleAbilityTransaction。
5. First Frame - App Phase：App首帧渲染提交阶段，对应的trace打点为H:ReceiveVsync，H:MarshRSTransactionData。
6. First Frame - Render Phase：RS首帧渲染提交阶段，对应的trace打点为H:ReceiveVsync和H:RSMainThread::ProcessCommandUni。
7. EntryAbility：应用启动之后的阶段，渲染完成，首页显示。

说明

阶段1对应图1中的第1阶段，阶段2对应图1中的第2阶段，阶段3和4对应图1中的第3阶段，阶段5和6对应图1中的第4阶段，阶段7对应图1中的第5阶段。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/de/v3/o9BXzOrAS5i68UXATQBCJQ/zh-cn_image_0000002194010752.png?HW-CC-KV=V1&HW-CC-Date=20260612T021549Z&HW-CC-Expire=86400&HW-CC-Sign=A63415F4872C6785FDA0FF4A84A0FBEAC4CC17A21092E2621A4EB35EEAAA622D "点击放大")

**冷启动缓慢示例分析**

运行以下示例代码，开发者可以明显感知到应用启动速度较慢。接下来，开发者可以通过此示例，结合 Launch 分析应用冷启动缓慢的问题。

```
1. const LARGE_NUMBER: number = 200000000;

3. @Entry
4. @Component
5. struct Index {
6. @State message: string = 'Hello World';

8. aboutToAppear(): void {
9. console.log('aboutToAppear');
10. this.computeTask();
11. }

13. computeTask(): void {
14. let count: number = 0;
15. while (count < LARGE_NUMBER) {
16. count++;
17. }
18. }

20. build() {
21. Row() {
22. Column() {
23. Text(this.message)
24. .fontSize(50)
25. .fontWeight(FontWeight.Bold)
26. }
27. .width('100%')
28. }
29. .height('100%')
30. }
31. }
```

[ColdStartSlow.ets](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/AppColdStart/entry/src/main/ets/pages/ColdStartSlow.ets#L17-L47)

首先创建Launch分析录制，可以观察到整个启动时间较长。UI Ability OnForeground阶段在应用冷启动过程中耗时最多，达到了3.3秒。因此，需要重点分析该阶段的耗时。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f4/v3/NTjrPfiETVmFg4m3xapHrw/zh-cn_image_0000002375918437.png?HW-CC-KV=V1&HW-CC-Date=20260612T021549Z&HW-CC-Expire=86400&HW-CC-Sign=B899321B3892C66AB5AA387525C7B7E630807C1795C35C621F78973004BD984B "点击放大")

针对应用冷启动问题的性能分析，可以选择分析主线程的Trace数据或采样得到的函数热点。

**分析主线程的Trace数据**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/36/v3/xBMxPSGrSeS0NCtCEp2OOg/zh-cn_image_0000002341876318.png?HW-CC-KV=V1&HW-CC-Date=20260612T021549Z&HW-CC-Expire=86400&HW-CC-Sign=1890AEA32FA497EBB0C8BC128E71AC146DF7407A6AB8CCB139AF8D1B5ED02235 "点击放大")

1. 单击“Launch”泳道上的UI Ability OnForeground阶段，在下方“Details”面板中可查看所选阶段的耗时统计。
2. 展开UI Ability OnForeground统计信息折叠表，可查看各函数的具体耗时信息。
3. 根据Duration找到耗时最长的函数aboutToAppear。
4. 单击图标按钮，可直接跳转至主线程的打点任务，查看相关Trace数据。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/97/v3/Bqwam5DmTpyP7m4-zZp2HQ/zh-cn_image_0000002375834697.png?HW-CC-KV=V1&HW-CC-Date=20260612T021549Z&HW-CC-Expire=86400&HW-CC-Sign=23EE7CAEF0F9E2EED4AB7E18EDD86ED11A054096F20512DA4EC9703F6E3F6C32 "点击放大")

在UI Ability OnForeground阶段的耗时主要由aboutToAppear引起。通过分析aboutToAppear中的代码逻辑，可以确定计算任务computeTask是导致耗时的原因。

**分析采样得到的函数热点**

开发者也可以分析采样得到的函数热点直观的显示应用冷启动过程中具体函数的耗时，如下图：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f1/v3/tdMWcf1JSW-p_wMwE_nn9Q/zh-cn_image_0000002375915041.png?HW-CC-KV=V1&HW-CC-Date=20260612T021549Z&HW-CC-Expire=86400&HW-CC-Sign=A6C834896D8D626EE0BC23D33C2EE797708374D4A0BB9670760250DC08BEDEF4 "点击放大")

1. 单击“Launch”泳道的UI Ability OnForeground阶段。
2. 选择“ArkTS Callstack”泳道，它会基于时间轴展示CPU使用率和状态变化，以及当前调用栈名称和类型。
3. 在“Details”详情面板中，可以查看这段时间内的函数热点，以Top-Down形式的树状列表展示。computeTask函数在aboutToAppear函数中耗时最多，占整个阶段的97.9%。双击该函数可跳转到源码。
4. 此外，点击底部Flame Chart按钮打开火焰图可以更直观的看出热点函数的耗时情况，如下图所示。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/24/v3/-rZw0HcVQgu9DlcqiXgOqA/zh-cn_image_0000002342038042.png?HW-CC-KV=V1&HW-CC-Date=20260612T021549Z&HW-CC-Expire=86400&HW-CC-Sign=05A3A5E5EB6654FB1B97F9F4143493E414F20CF3A301F6F512A4086DBDCA72AD "点击放大")

**冷启动速度优化**

通过前面的分析，冷启动缓慢的原因是在aboutToAppear方法中执行了耗时计算任务。可以将computeTask以异步延时的方式处理，优化后的代码如下：

```
1. const LARGE_NUMBER: number = 100000000;
2. const DELAYED_TIME: number = 1000;

4. @Entry
5. @Component
6. struct Index {
7. @State message: string = 'Hello World';

9. aboutToAppear(): void {
10. console.log('aboutToAppear');
11. this.computeTaskAsync();
12. }

14. // ...

16. computeTask(): void {
17. let count: number = 0;
18. while (count < LARGE_NUMBER) {
19. count++;
20. }
21. }

23. // Asynchronous processing of operation tasks
24. private computeTaskAsync(): void {
25. setTimeout(() => { // SetTimeout is used here to realize asynchronous delayed operation.
26. this.computeTask();
27. }, DELAYED_TIME);
28. }
29. }
```

[ColdStartSpeedOptimization.ets](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/AppColdStart/entry/src/main/ets/pages/ColdStartSpeedOptimization.ets#L17-L57)

重新编译并运行程序，录制Launch过程。优化后，UI Ability OnForeground阶段的耗时显著缩短，如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dd/v3/2GKoLGjOQRCJdhElUW6rNA/zh-cn_image_0000002229450977.png?HW-CC-KV=V1&HW-CC-Date=20260612T021549Z&HW-CC-Expire=86400&HW-CC-Sign=C47B8AF79F62753185C397FC81B6EA2BD6D19316002EB009681CD571675B8973 "点击放大")

**查看首帧卡顿**

为了识别首帧是否卡顿，可以先查看Launch的Frame泳道。应用的首帧渲染提交在First Frame - App Phase阶段，APP侧的这一帧表示应用渲染的首帧。如下图所示，此处首帧为36号帧。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/47/v3/oMKhFjOWTkGFqDMKiXJ5BA/zh-cn_image_0000002229336561.png?HW-CC-KV=V1&HW-CC-Date=20260612T021549Z&HW-CC-Expire=86400&HW-CC-Sign=EFCC1F0A80A94435EE280D5F91CD902F79B2ED691F182CA5B5E0E097B2A1D0D0 "点击放大")

如上所示36号帧被标记为了红色，表示首帧出现了卡顿。鼠标左键36号帧，可以看到它的期望提交渲染时间为左边白色竖线区域所示，这里出现了比较严重的延时。发现问题后，开发者可以参考前面讲到的示例进行问题定位和优化。

## 提升应用冷启动速度

本文将通过公共类优化的方法，包括[非冷启动必需的服务或模块延迟加载](bpta-application-cold-start-optimization.md#section1351981113010)、[减少主线程非UI耗时操作](bpta-application-cold-start-optimization.md#section17543719239)和[网络请求提前发送](bpta-application-cold-start-optimization.md#section199911250658)，以及结合应用启动的几个阶段分别介绍提升应用冷启动速度的相关方法。

### 非冷启动必需的服务或模块延迟加载

应用在启动前加载过多不必要启动项，同时这些启动项在主线程串行执行，该阶段耗时为450ms。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/62/v3/7i6RqVNbQ0KP2ULD8xcdFA/zh-cn_image_0000002229451033.png?HW-CC-KV=V1&HW-CC-Date=20260612T021549Z&HW-CC-Expire=86400&HW-CC-Sign=A7EB137B617CF14A5AEE9864EC604C94F588EC2BB361735D932099DBDB85A480 "点击放大")

应用冷启动过程中，加载不必要的启动项会增加冷启动时间。建议延后加载或并行处理，具体可以参考[延迟加载Lazy-Import使用指导](../../../../应用框架/ArkTS语言/ArkTS高性能编程/bpta-arkts-high-performance.md#section12861143418213)。

### 减少主线程非UI耗时操作

在应用启动流程中，主要聚焦在执行UI相关操作中，为了更快的显示首页内容，不建议在主线程中执行非UI相关的耗时操作，建议通过异步任务进行异步处理或放到其他子线程中执行，线程并发方案详细请参见[TaskPool和Worker的对比实践](../../../../应用框架/ArkTS语言/TaskPool和Worker对比/bpta-comparative_practice_of_taskpool_and_worker.md)。

在冷启动过程中如果存在图片下载、网络请求前置数据、数据反序列化等非UI操作，开发者可以根据实际情况移至子线程中进行，详细请参见[应用并发设计](../../../../应用框架/ArkTS语言/应用并发设计/bpta-app-concurrency-design.md)。

### 网络请求提前发送

当前大多数应用的首页内容需从网络获取，发送网络请求的时机显得尤为重要。应用发送网络请求后等待网络数据的返回，网络请求的这段时间应用可以继续执行启动流程，直到网络数据返回后进行解析，反序列化之后就可以加载首页数据，因此网络请求的发起时机越早，整个冷启动的完成时延阶段越短。

将网络请求及初始化流程放置在AbilityStage/UIAbility的onCreate()生命周期中。仅执行网络相关预处理。等待网络请求发送后继续执行首页数据准备和UI操作。在服务端处理相同的情况下，应用可以更早获取网络数据并行展示。

**图2** 应用首页框架加载时进行网络数据请求

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3d/v3/XuH-MqLOSLqjv4rJx7NeKA/zh-cn_image_0000002420612214.png?HW-CC-KV=V1&HW-CC-Date=20260612T021549Z&HW-CC-Expire=86400&HW-CC-Sign=49A5AC2ED29241799C79B74CFC70EDA024D868D708848402F7720676F638828A "点击放大")

将网络请求提前至AbilityStage/UIAbility的onCreate()生命周期回调函数中。这可以将首刷或二刷时间提前，减少用户等待时间。为了体现性能收益，将网络请求放到了更早的AbilityStage的onCreate()生命周期回调中。

**图3** 网络请求提前至AbilityStage的onCreate()生命周期回调中

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/80/v3/PPhQdLY5SoywRTWQXgHk6A/zh-cn_image_0000002420772730.png?HW-CC-KV=V1&HW-CC-Date=20260612T021549Z&HW-CC-Expire=86400&HW-CC-Sign=6062E90B14ECC91C9636FBE5DF94A8B53D42B2E207BA4411D6A31CE004E954D5 "点击放大")

【优化前】：在首页根组件的onAppear()回调中发起网络请求。

```
1. // entry/src/main/ets/pages/Index.ets
2. import { httpRequest } from '../utils/NetRequest';

4. import { number } from '../utils/Calculator';

6. AppStorage.link('netData');
7. PersistentStorage.persistProp('netData', undefined);

9. @Entry
10. @Component
11. struct Index {
12. // In order to reflect the performance benefits, refer to the execution result number of the time-consuming function.
13. @State message: string = 'Hello World' + number;
14. @StorageLink('netData') netData: PixelMap | undefined = undefined;

16. build() {
17. Column() {
18. Text(this.message)
19. .fontSize(32)
20. Image(this.netData)
21. .objectFit(ImageFit.Contain)
22. .width('50%')
23. .height('50%')
24. }
25. .width('100%')
26. .height('100%')
27. .justifyContent(FlexAlign.Center)
28. .onAppear(() => {
29. // Send a network request
30. httpRequest();
31. })
32. }
33. }
```

[Index.ets](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/AppColdStart/entry/src/main/ets/pages/Index.ets#L17-L49)

```
1. // NetRequest.ets
2. import { hiTraceMeter } from '@kit.PerformanceAnalysisKit';
3. import { http } from '@kit.NetworkKit';
4. import { BusinessError } from '@kit.BasicServicesKit';
5. import { image } from '@kit.ImageKit';
6. // Download picture resources from the Internet through the http request method
7. export function httpRequest(): void {
8. hiTraceMeter.startTrace('Http Request', 1);
9. http.createHttp()
10. // The actual development needs to "https://www.example1.com/POST?e=f&g=h"replaced with the real website address to visit
11. .request('https://www.example1.com/POST?e=f&g=h',
12. (error: BusinessError, data: http.HttpResponse) => {
13. if (error) {
14. // The follow-up logic is not executed when the download fails.
15. return;
16. }
17. // Processing the data returned by network requests
18. transcodePixelMap(data);
19. }
20. )
21. }

23. // Use createPixelMap to replace pictures of ArrayBuffer types with PixelMap types.
24. function transcodePixelMap(data: http.HttpResponse): void {
25. if (http.ResponseCode.OK === data.responseCode) {
26. const imageData: ArrayBuffer = data.result as ArrayBuffer;
27. // Create a picture source instance through ArrayBuffer
28. const imageSource: image.ImageSource = image.createImageSource(imageData);
29. const options: image.InitializationOptions = {
30. 'alphaType': 0, // Transparency
31. 'editable': false, // Is it editable?
32. 'pixelFormat': 3, // Pixel format
33. 'scaleMode': 1, // Abbreviation
34. 'size': { height: 100, width: 100 }
35. }; // Create the size of the picture
36. // Create PixelMap through properties
37. imageSource.createPixelMap(options).then((pixelMap: PixelMap) => {
38. AppStorage.set('netData', pixelMap);
39. hiTraceMeter.finishTrace('Http Request', 1);
40. });
41. }
42. }
```

[NetRequest.ets](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/AppColdStart/entry/src/main/ets/utils/NetRequest.ets#L2-L45)

```
1. // Calculator.ets
2. const LARGE_NUMBER: number = 100000000;

4. function computeTask(): number {
5. let count: number = 0;
6. while (count < LARGE_NUMBER) {
7. count++;
8. }
9. return count;
10. }

12. export let number = computeTask();
```

[Calculator.ets](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/AppColdStart/entry/src/main/ets/utils/Calculator.ets#L2-L13)

【优化后】

1. 在NetRequest.ets中进行网络请求以及数据处理。

   ```
   1. // NetRequest.ets
   2. import { hiTraceMeter } from '@kit.PerformanceAnalysisKit';
   3. import { http } from '@kit.NetworkKit';
   4. import { BusinessError } from '@kit.BasicServicesKit';
   5. import { image } from '@kit.ImageKit';
   6. // Download picture resources from the Internet through the http request method
   7. export function httpRequest(): void {
   8. hiTraceMeter.startTrace('Http Request', 1);
   9. http.createHttp()
   10. // The actual development needs to "https://www.example1.com/POST?e=f&g=h"replaced with the real website address to visit
   11. .request('https://www.example1.com/POST?e=f&g=h',
   12. (error: BusinessError, data: http.HttpResponse) => {
   13. if (error) {
   14. // The follow-up logic is not executed when the download fails.
   15. return;
   16. }
   17. // Processing the data returned by network requests
   18. transcodePixelMap(data);
   19. }
   20. )
   21. }

   23. // Use createPixelMap to replace pictures of ArrayBuffer types with PixelMap types.
   24. function transcodePixelMap(data: http.HttpResponse): void {
   25. if (http.ResponseCode.OK === data.responseCode) {
   26. const imageData: ArrayBuffer = data.result as ArrayBuffer;
   27. // Create a picture source instance through ArrayBuffer
   28. const imageSource: image.ImageSource = image.createImageSource(imageData);
   29. const options: image.InitializationOptions = {
   30. 'alphaType': 0, // Transparency
   31. 'editable': false, // Is it editable?
   32. 'pixelFormat': 3, // Pixel format
   33. 'scaleMode': 1, // Abbreviation
   34. 'size': { height: 100, width: 100 }
   35. }; // Create the size of the picture
   36. // Create PixelMap through properties
   37. imageSource.createPixelMap(options).then((pixelMap: PixelMap) => {
   38. AppStorage.set('netData', pixelMap);
   39. hiTraceMeter.finishTrace('Http Request', 1);
   40. });
   41. }
   42. }
   ```

   [NetRequest.ets](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/AppColdStart/entry/src/main/ets/utils/NetRequest.ets#L3-L44)
2. 在AbilityStage的onCreate()生命周期回调中发起网络请求。

   ```
   1. // MyAbilityStage.ets
   2. import { AbilityStage, Want } from '@kit.AbilityKit';
   3. import { httpRequest } from '../utils/NetRequest';
   4. export default class MyAbilityStage extends AbilityStage {
   5. onCreate(): void {
   6. // Send a network request
   7. httpRequest();
   8. }

   10. onAcceptWant(want: Want): string {
   11. // Triggered in specified mode only.
   12. return 'MyAbilityStage';
   13. }
   14. }
   ```

   [MyAbilityStage.ets](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/AppColdStart/entry/src/main/ets/entryability/MyAbilityStage.ets#L17-L30)
3. 在首页 Index.ets 中展示请求获取的图片。

   ```
   1. // Index.ets
   2. import { number } from '../utils/Calculator';

   4. AppStorage.link('netData');
   5. PersistentStorage.persistProp('netData', undefined);

   7. @Entry
   8. @Component
   9. struct Index {
   10. @State message: string = 'Hello World' + number; // In order to reflect the performance benefits, refer to the execution result number of the time-consuming function.
   11. @StorageLink('netData') netData: PixelMap | undefined = undefined;
   12. build() {
   13. Row() {
   14. Image(this.netData)
   15. .objectFit(ImageFit.Contain)
   16. .width('50%')
   17. .height('50%')
   18. }
   19. .onDisAppear(() => {
   20. AppStorage.set('netData', undefined);
   21. })
   22. .height('100%')
   23. .width('100%')
   24. }
   25. }
   ```

   [NewIndex.ets](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/AppColdStart/entry/src/main/ets/pages/NewIndex.ets#L17-L41)

使用Launch分析工具，对比优化前后启动性能。分析阶段从启动Ability（即H:void OHOS::AppExecFwk::MainThread::HandleLaunchAbility的开始点）到应用接收到网络数据返回后的首帧刷新（即H:ReceiveVsync dataCount:24Bytes now:timestamp expectedEnd:timestamp vsyncId:int的开始点）。

**图4** 优化网络请求时机前   
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d2/v3/xd1stOCgTKy4NOOdrsRnqQ/zh-cn_image_0000002194010676.png?HW-CC-KV=V1&HW-CC-Date=20260612T021549Z&HW-CC-Expire=86400&HW-CC-Sign=A28C062229C701196194A9E72C613BA424EF415C9190282A7EA322E963FBE6FF "点击放大")

**图5** 优化网络请求时机后   
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/51/v3/w48WAudpRVepcFoBxPbk8g/zh-cn_image_0000002229450941.png?HW-CC-KV=V1&HW-CC-Date=20260612T021549Z&HW-CC-Expire=86400&HW-CC-Sign=A77C7B9C4F2158FBD0B6758BEF1B1F83A42F583E601E0F155301D603E5793F87 "点击放大")

对比数据如下：

| 方案 | 阶段时长(毫秒) |
| --- | --- |
| 优化网络请求时机前 | 1700 |
| 优化网络请求时机后 | 885.3 |

因此，可以通过提前网络请求的方式减少应用冷启动耗时。

### 缩短应用进程创建和初始化阶段耗时

应用进程创建和初始化阶段包括系统完成应用进程的创建及初始化，以及启动页图标（startWindowIcon）的解码。建议使用不超过256×256分辨率的图标，以减少图片解码时延，提升体验。

说明

建议开发者优先使用[Code Linter扫描工具](<../../../../../harmonyos-guides/编写与调试应用/代码编辑/代码检查/Code Linter代码检查/ide-code-linter.md>)进行代码检查，重点关注[@performance/start-window-icon-check](<../../../../../harmonyos-guides/编写与调试应用/代码编辑/代码检查/Code Linter代码检查规则/性能规则@performance/@performancestart-window-icon-check/ide-start-window-icon-check.md>)规则。若扫描结果中出现该规则相关问题，可参考本章节提供的优化建议进行调整。

**设置合适分辨率的startWindowIcon**

如果启动页图标分辨率过大，解码耗时会影响应用的启动速度。建议启动页图标分辨率不超过256像素×256像素，如下所示。

```
1. {
2. // ...
3. "abilities": [
4. {
5. "name": "EntryAbility",
6. "srcEntry": "./ets/entryability/EntryAbility.ets",
7. "description": "$string:EntryAbility_desc",
8. "icon": "$media:layered_image",
9. "label": "$string:EntryAbility_label",
10. "startWindowIcon": "$media:startIcon",
11. "startWindowBackground": "$color:start_window_background",
12. // ...
13. }
14. ]
15. }
16. }
```

[module.json5](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/AppColdStart/entry/src/main/module.json5#L2-L55)

下面使用Launch分析对比优化前的startWindowIcon（4096像素\\*4096像素）及优化后的startWindowIcon（144像素\\*144像素）的启动性能。分析阶段的起点为Process Creating，阶段终点为First Frame - Render Phase，优化前后的启动耗时如下图：

**图6** 优化前使用4096px-4096px启动页图标应用启动耗时   
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/17/v3/2suQdV27TKK7-04mT3ltZw/zh-cn_image_0000002229451013.png?HW-CC-KV=V1&HW-CC-Date=20260612T021549Z&HW-CC-Expire=86400&HW-CC-Sign=F2956EFBCEA6D412DB0B16EEE2332EA4648443A1C935FD83C09510986842D2F9)

**图7** 优化后使用144px-144px启动页图标应用启动耗时   
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1d/v3/h4_F_-kJQnmL6VmBMS7AeA/zh-cn_image_0000002229450965.png?HW-CC-KV=V1&HW-CC-Date=20260612T021549Z&HW-CC-Expire=86400&HW-CC-Sign=EDA2EB5E78923EE5B61241D152B65A2D8A1C58A61DCDD6D8C66DD688C7F07C39)

优化后，应用启动时长缩短了37.2ms，设置合适的startWindowIcon分辨率能有效减少应用进程创建和初始化阶段的耗时。

### 缩短Application和Ability初始化阶段耗时

Application和Ability初始化包括资源加载、虚拟机创建、相关对象的创建与初始化及依赖模块的加载。

主要耗时点在资源加载阶段，分为以下几个步骤。

1. 文件加载：查找并解析所有的文件到模块中记录。
2. 依赖模块解析（实例化）：分配内存空间来存放模块所有导出的变量，此时内存中并没有分配变量的值。
3. 文件执行：运行.ets文件，将内存中之前未分配值的变量赋为真实的值。

本章节将详细说明这三个阶段的具体优化方法。

**减少import的模块**

应用程序在执行代码前，必须找到并加载所有导入的模块。每个加载的第三方框架或模块都会增加启动时间，具体耗时取决于模块的数量和大小。建议开发者优先使用系统提供的模块，并按需加载，以缩短应用程序的启动时间。

```
1. // Optimize modules that reduce import
2. /*import { ConfigurationConstant, contextConstant, wantConstant } from '@kit.AbilityKit';
3. import { GesturePath, GesturePoint } from '@kit.AccessibilityKit';
4. import { distributedAccount, osAccount } from '@kit.BasicServicesKit';
5. import { Configuration } from '@kit.ArkUI';
6. import { atomicService } from '@kit.ScenarioFusionKit';
7. import { sim } from '@kit.TelephonyKit';*/

10. import { UIAbility } from '@kit.AbilityKit';

13. export default class EntryAbility extends UIAbility {
14. // ...
15. }
```

[ReduceImport.ets](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/AppColdStart/entry/src/main/ets/pages/ReduceImport.ets#L17-L31)

下面使用Launch分析，对优化import的模块前（模块数量15个）及优化import的模块后（移除不必要的模块剩余5个）的启动性能进行对比分析。分析的trace点为H:SourceTextModule::Evaluate，优化前后的启动耗时如下图：

**图8** 优化前import 15个模块   
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/77/v3/xdbQK4H5TLW9b2fTOVA0Og/zh-cn_image_0000002229336481.png?HW-CC-KV=V1&HW-CC-Date=20260612T021549Z&HW-CC-Expire=86400&HW-CC-Sign=3F107F39E0B95D06CCB5781277F35B223C49FB87A8B147CF4F31673551439415 "点击放大")

**图9** 优化后import 5个模块   
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c0/v3/jY4R2KyYTWmN197VTKQFTw/zh-cn_image_0000002229336453.png?HW-CC-KV=V1&HW-CC-Date=20260612T021549Z&HW-CC-Expire=86400&HW-CC-Sign=589BF3592D9AB408D996275B2FF3766CBBF96C5BB426E3ED3923133628C339A8 "点击放大")

对比数据如下：

| 方案 | 阶段时长(微秒) |
| --- | --- |
| 减少import的模块前 | 6239.5 |
| 减少import的模块后 | 119.7 |

减少不必要的模块导入可以缩短应用的冷启动时间。如果某些必要模块的导入较为耗时，建议采用动态导入方式。具体方法可参考[动态加载](../../../../../harmonyos-guides/应用框架/ArkTS（方舟编程语言）/ArkTS运行时/ArkTS模块化/动态加载/arkts-dynamic-import.md)。

减少使用嵌套的export \*和import \*方式。

* 减少使用嵌套的export \*方式进行全量导出

  在应用冷启动过程中，`HandleLaunchAbility` 会执行冷启动相关的 `.ets` 文件。所有被主页面import的 `.ets` 文件均会被执行，包括数据结构、变量和全局函数的初始化。首页所需的变量和函数可能来自其他 `.ets` 文件，并通过export形式提供给首页使用。详细信息请参见[减少同文件大量export \*导出方式](../../../../应用框架/ArkTS语言/ArkTS高性能编程/bpta-arkts-high-performance.md#section1218510102815)。

  使用Launch分析，对比优化前（嵌套8层export \*）和优化后（直接从目标文件中import）的启动性能。分析阶段从开始加载abc文件（H:JSPandaFileExecutor::ExecuteFromAbcFile）到abc文件加载完成。

  **图10** （优化前）存在8层嵌套export \*   
  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/62/v3/trP7f5hBRyiChXRb-CnSIA/zh-cn_image_0000002193851128.png?HW-CC-KV=V1&HW-CC-Date=20260612T021549Z&HW-CC-Expire=86400&HW-CC-Sign=FE407498B89404FEF1D6E030214C06B0FD26804F2D63758DCF3AA283ED7DAA93 "点击放大")

  **图11** （优化后）不存在嵌套export \*，从目标文件中直接import   
  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0a/v3/jkyW82DmQUS4xcInxTOctw/zh-cn_image_0000002194010744.png?HW-CC-KV=V1&HW-CC-Date=20260612T021549Z&HW-CC-Expire=86400&HW-CC-Sign=C14903C02770985EC0D058FE20DDEA038950F554E2E26D9E0931DEA05FEAC2F5 "点击放大")

  对比数据如下：

  | 方案 | 阶段时长(微秒) |
  | --- | --- |
  | （优化前）存在8层嵌套export \* | 492.6 |
  | （优化后）不存在嵌套export \*，从目标文件中直接import | 388.7 |

  可见阶段时长已缩短。减少多层文件嵌套导出可以提升应用冷启动速度。
* 减少import \*的方式全量引用

  应用程序加载时，通常将相同类型的变量或函数放在同一个工具类文件中。使用时，通过import方式引入对应的模块。当工具类中存在较多暴露的函数或变量时，推荐按需引用具体的变量，以减少 `.ets` 文件的执行耗时和文件中所有export变量的初始化过程。详情请参见[减少同文件大量export \*导出方式](../../../../应用框架/ArkTS语言/ArkTS高性能编程/bpta-arkts-high-performance.md#section1218510102815)。

  对优化前（使用 `import \* as nm` 全量引用2000条数据）和优化后（使用import { One }按需引用）的启动性能进行对比分析。分析阶段从 `H:void OHOS::AppExecFwk::MainThread::HandleLaunchAbility(const std::shared\_ptr<AbilityLocalRecord> &)` 的开始点到结束点。

  **图12** 优化前，使用import \* as nm全量引用2000条数据   
  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/89/v3/xiM0dNq9SbiVBhP5PY_inw/zh-cn_image_0000002229450969.png?HW-CC-KV=V1&HW-CC-Date=20260612T021549Z&HW-CC-Expire=86400&HW-CC-Sign=9CD6682DD842DC6FD74DC9EDCFE22E7477C214332C6779A63589A4E90F5D05D4 "点击放大")

  **图13** 优化后，使用import { One }按需引用   
  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d8/v3/aEM9nVevTVqyh_djm1dNwQ/zh-cn_image_0000002229450953.png?HW-CC-KV=V1&HW-CC-Date=20260612T021549Z&HW-CC-Expire=86400&HW-CC-Sign=25376DD09295664D19B5ED0BF8E48673868880B143C61294840ACF949B672BB4 "点击放大")

  优化前后的对比数据如下：

  | 方案 | 阶段时长(毫秒) |
  | --- | --- |
  | （优化前）使用import \* as nm全量引用 | 16.7 |
  | （优化后）使用import { One }按需引用 | 7.1 |

  可见阶段的时长已减少。使用按需引用的方式，可以进一步缩短应用冷启动的完成时间。

  说明

  此优化方案仅可将冷启动阶段耗时缩短，但是可能导致其他场景耗时增长，即变量初始化过程从冷启动阶段分摊至其它使用阶段，例：当二级页面使用到Numbers.ets中Two变量，此方案会使二级页面跳转过程对比优化前耗时更长。

**合理拆分导出文件，减少冗余文件执行**

应用程序加载模块后，需执行应用侧的.ets文件，进行初始化并执行全局变量和函数的初始化。文件可分类为冷启动强相关文件（如首页展示界面及组件相关文件）和非冷启动强相关文件（如跳转后二级页面）。冷启动过程中仅执行冷启动强相关文件，以缩短应用启动时间。

【场景示例】

应用包含两个页面：首页Index和二级页面SecondPage。首页展示HAR包中MainPage.ets文件的Text组件，该文件中没有耗时操作。点击首页中的Text组件时，跳转至二级页面。二级页面引用HAR包中的SubPage.ets文件，该文件包含全局函数的耗时操作，这些操作在模块加载时执行。

HAR包中的导出文件Index.ets同时导出了MainPage.ets和SubPage.ets两个文件。当首页直接使用 “import { MainPage } from 'library/Index'” 的方式进行导入时，会导致应用在冷启动过程中执行非冷启动强相关文件SubPage.ets，增加了冷启动时间。

**图14** 优化前，加载模块时执行了非冷启动相关文件 SubPage.ets。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1c/v3/fyf0DHpOR4u230fDu1igow/zh-cn_image_0000002454292713.png?HW-CC-KV=V1&HW-CC-Date=20260612T021549Z&HW-CC-Expire=86400&HW-CC-Sign=F45A6A6ADC2C152FBC5594A8A00C63CA702A67641641EDC63D33CFDF51472A36 "点击放大")

以下为示例代码：

```
1. // entry/src/main/ets/pages/Index.ets
2. import { MainPage } from 'library/Index'; // Unrecommended usage: Direct import of subPage.ets files related to cold start non-strong
3. @Component
4. export struct Index{
5. @Provide pathStack: NavPathStack = new NavPathStack();
6. build() {
7. Navigation(this.pathStack) {
8. Row() {
9. // Refer to the custom components of HAR
10. MainPage()
11. }
12. }
13. }
14. }
```

[NotRecommendDemo.ets](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/AppColdStart/entry/src/main/ets/pages/NotRecommendDemo.ets#L17-L30)

```
1. // library/src/main/ets/components/mainpage/MainPage.ets
2. @Component
3. export struct MainPage {
4. @Consume pathStack: NavPathStack;
5. @State message: string = 'HAR MainPage';

7. build() {
8. Row() {
9. Text(this.message)
10. .fontSize(32)
11. .fontWeight(FontWeight.Bold)
12. }.onClick(() => {
13. this.pathStack.pushPath({ name: 'SecondPage' });
14. })
15. }
16. }
```

[MainPage.ets](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/AppColdStart/library/src/main/ets/components/mainpage/MainPage.ets#L17-L32)

```
1. // entry/src/main/ets/pages/SecondPage.ets
2. import { SubPage } from 'library/Index';
3. @Builder
4. export function SecondPageBuilder() {
5. SecondPage()
6. }
7. @Entry
8. @Component
9. struct SecondPage {
10. pathStack: NavPathStack = new NavPathStack();
11. build() {
12. NavDestination() {
13. Row() {
14. // Refer to the custom components of HAR
15. SubPage()
16. }
17. .height('100%')
18. }
19. .onReady((context: NavDestinationContext) => {
20. this.pathStack = context.pathStack;
21. })
22. }
23. }
```

[SecondPage.ets](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/AppColdStart/entry/src/main/ets/pages/SecondPage.ets#L17-L39)

```
1. // library/src/main/ets/components/mainpage/SubPage.ets
2. // Global time-consuming functions in SubPage
3. const LARGE_NUMBER: number = 10000000;

5. function computeTask(): number {
6. let count: number = 0;
7. while (count < LARGE_NUMBER) {
8. count++;
9. }
10. return count;
11. }

13. computeTask();
14. // ...
```

[SubPage.ets](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/AppColdStart/library/src/main/ets/components/mainpage/SubPage.ets#L2-L15)

```
1. export { MainPage } from './src/main/ets/components/mainpage/MainPage'; // Cold start strong related files
2. export { SubPage } from './src/main/ets/components/mainpage/SubPage'; // Non-cold start strong related files
```

[Index.ets](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/AppColdStart/library/Index.ets#L17-L18)

【优化方案一】

将HAR包的导出文件Index.ets进行拆分，IndexAppStart.ets文件仅导出首页相关文件，即MainPage.ets。IndexOthers.ets文件导出非首页相关文件，即SubPage.ets。

优点：使用此种方案优化后可以将冷启动阶段（加载首页文件）与非冷启动阶段（加载非首页文件）需要执行的.ets文件进行完全拆分，类比其他需优化的场景也可以使用本方案进行拆分。

缺点：拆分后，需确保IndexAppStart.ets中的导出文件不引用IndexOthers.ets中的导出文件。

**图15** 优化方案一，拆分HAR导出文件

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1b/v3/vZIG7yiFQS2cy3Hm1jtNrg/zh-cn_image_0000002454173657.png?HW-CC-KV=V1&HW-CC-Date=20260612T021549Z&HW-CC-Expire=86400&HW-CC-Sign=7209304083588973F6DB07C73DEBF447F23747AF808F02175323349AE23CB055 "点击放大")

示例代码如下：

1. 将HAR包的导出文件Index.ets进行拆分，IndexAppStart.ets文件仅导出首页相关文件，IndexOthers.ets文件导出非首页相关文件。

   ```
   1. // library/IndexAppStart.ets
   2. export { MainPage } from './src/main/ets/components/mainpage/MainPage';
   ```

   [IndexAppStart.ets](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/AppColdStart/library/IndexAppStart.ets#L2-L3)

   ```
   1. // library/IndexOthers.ets
   2. export { SubPage } from './src/main/ets/components/mainpage/SubPage';
   ```

   [IndexOthers.ets](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/AppColdStart/library/IndexOthers.ets#L2-L3)
2. 首页Index从IndexAppStart.ets导入MainPage。

   ```
   1. // Index.ets
   2. import { MainPage } from 'library/IndexAppStart';

   4. @Entry
   5. @Component
   6. struct Index {
   7. @Provide pathStack: NavPathStack = new NavPathStack();

   9. build() {
   10. Navigation(this.pathStack) {
   11. Row() {
   12. // Refer to the custom components of HAR
   13. MainPage()
   14. }
   15. }
   16. .height('100%')
   17. .width('100%')
   18. }
   19. }
   ```

   [ImportMainPage.ets](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/AppColdStart/entry/src/main/ets/pages/ImportMainPage.ets#L17-L35)
3. 跳转后的页面SecondPage从IndexOthers.ets导入SubPage。

   ```
   1. // SecondPage.ets
   2. import { SubPage } from 'library/IndexOthers';

   4. @Builder
   5. export function SecondPageBuilder() {
   6. SecondPage()
   7. }

   9. @Entry
   10. @Component
   11. struct SecondPage {
   12. pathStack: NavPathStack = new NavPathStack();

   14. build() {
   15. NavDestination() {
   16. Row() {
   17. // Refer to the custom components of HAR
   18. SubPage()
   19. }
   20. .height('100%')
   21. }
   22. .onReady((context: NavDestinationContext) => {
   23. this.pathStack = context.pathStack;
   24. })
   25. }
   26. }
   ```

   [ImportSubPage.ets](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/AppColdStart/entry/src/main/ets/pages/ImportSubPage.ets#L17-L42)

【优化方案二】

在首页的Index.ets文件中导入MainPage.ets时，使用全路径。

优点：无需新增文件即可汇总导出所有冷启阶段的文件。

缺点：引用时需对冷启阶段的所有文件路径进行展开，增加开发和维护成本。

**图16** 优化方案二，首页导入冷启动文件时使用全路径展开

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3c/v3/pEheE7jGQseJM3SYA-YuWw/zh-cn_image_0000002420614820.png?HW-CC-KV=V1&HW-CC-Date=20260612T021549Z&HW-CC-Expire=86400&HW-CC-Sign=391822EEDF7866DCF6CAEAA3711FB10BE09906453A5513881309CA9B7040898B "点击放大")

示例代码如下：

```
1. // Index.ets
2. import { MainPage } from 'library/src/main/ets/components/mainpage/MainPage';

4. @Entry
5. @Component
6. struct Index {
7. @Provide pathStack: NavPathStack = new NavPathStack();

9. build() {
10. Navigation(this.pathStack) {
11. Row() {
12. // Refer to the custom components of HAR
13. MainPage()
14. }
15. }
16. .height('100%')
17. .width('100%')
18. }
19. }
```

[ImportMainPageDemo.ets](https://gitcode.com/HarmonyOS_Samples/BestPracticeSnippets/blob/master/AppColdStart/entry/src/main/ets/pages/ImportMainPageDemo.ets#L17-L35)

说明

1. 上述两种优化方案假设MainPage中不存在对SubPage的import。

2. 当MainPage中存在对SubPage的直接import时，需使用[动态import](../../../../../harmonyos-guides/应用框架/ArkTS（方舟编程语言）/ArkTS运行时/ArkTS模块化/动态加载/arkts-dynamic-import.md)方法来进行优化。

3. 开发者可自行根据优化方案的优缺点权衡选择合适的优化方案。

使用Launch分析优化前后启动性能。阶段起点为UI Ability Launching，终点为应用首帧即First Frame - App Phase。

**图17** 优化前：加载模块时执行了非冷启动相关文件   
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/51/v3/rnlVCl4OT2GhRaPtPHVzxQ/zh-cn_image_0000002229336505.png?HW-CC-KV=V1&HW-CC-Date=20260612T021549Z&HW-CC-Expire=86400&HW-CC-Sign=9A1190DBFBEE6BA19E51B2B22E74416C16DFC584A296CEFD04D96DEAA529FFEB "点击放大")

**图18** 优化方案一：拆分HAR导出文件   
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f3/v3/USETaBwvRxOizu_ZblawaQ/zh-cn_image_0000002193851072.png?HW-CC-KV=V1&HW-CC-Date=20260612T021549Z&HW-CC-Expire=86400&HW-CC-Sign=A24F4045CF258C0B57047504EC2255DAA3EF1A41B51D374A8DAC36DEFBD45F1E "点击放大")

**图19** 优化方案二：导入冷启动文件时全路径展开   
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b5/v3/gCpBereFSy2rXu8PoPSuVQ/zh-cn_image_0000002194010672.png?HW-CC-KV=V1&HW-CC-Date=20260612T021549Z&HW-CC-Expire=86400&HW-CC-Sign=6EA34048CB0E9525CF1450A48AFBD5C2B399AA6148D7B35FD0917B81F533488C "点击放大")

优化前后的对比数据如下：

| 方案 | 阶段时长(毫秒) |
| --- | --- |
| 优化前 | 140.1 |
| 优化方案一（拆分HAR导出文件） | 62.9 |
| 优化方案二（导入冷启动文件时全路径展开） | 61.3 |

可见阶段的时长已减少。为减少应用冷启动时.ets文件的执行耗时，可以采取以下措施：拆分HAR包导出的Index.ets文件，或在导入冷启动文件时展开完整路径，从而提升应用冷启动速度。

**减少多个HAP/HSP对相同HAR的引用**

在应用开发的过程中，可以使用[HSP](../../../../../harmonyos-guides/基础入门/开发基础知识/应用程序包基础知识/应用程序包开发与使用/HSP/in-app-hsp.md)或[HAR](../../../../../harmonyos-guides/基础入门/开发基础知识/应用程序包基础知识/应用程序包开发与使用/HAR/har-package.md)的共享包方式，整合同类模块，实现多个模块或工程间共享ArkUI组件、资源等相关代码。同时，避免多个HAP/HSP引用相同HAR。详细信息请参见[多HAP/HSP引用相同HAR包的影响](../../../../应用架构/模块化设计/bpta-modular-design.md#section9492615385)。

**优化加载HSP时间过长**

对于单窗口应用的APP工程，其仅包含一个Entry类型的HAP。如果划分的模块没有按需加载的需求，建议业务组件和公共组件采用HAR的打包方式。最终构建应用HAP包时，这些被依赖的HAR将被编译进HAP包中。HSP采用动态加载，在启动过程中会将依赖的HSP加载进来，增加额外的IO与运行耗时。在单HAP场景下，如果使用多模块的话。推荐使用多HAR，不推荐使用HSP。

以下为示例代码：

```
1. import { add } from 'hsp1';
2. import { add2 } from 'hsp2';
3. import { add3 } from 'hsp3';
4. import { add4 } from 'hsp4';
5. import { add5 } from 'hsp5';
6. import { add6 } from 'hsp6';
7. import { add7 } from 'hsp7';
8. import { add8 } from 'hsp8';
9. import { add9 } from 'hsp9';
10. import { add10 } from 'hsp10';
11. import { add11 } from 'hsp11';
12. import { add12 } from 'hsp12';
13. import { add13 } from 'hsp13';
14. import { add14 } from 'hsp14';
15. import { add15 } from 'hsp15';
16. import { add16 } from 'hsp16';
17. import { add17 } from 'hsp17';
18. import { add18 } from 'hsp18';
19. import { add19 } from 'hsp19';
20. import { add20 } from 'hsp20';
```

下面使用Launch分析，对比HAP与20个HSP混合打包以及将20个HSP包设计成HAR包的启动性能。

**图20** HAP+20个HSP混合打包   
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0c/v3/8pv7h3hNSqGzqYkLqWZshQ/zh-cn_image_0000002229451061.png?HW-CC-KV=V1&HW-CC-Date=20260612T021549Z&HW-CC-Expire=86400&HW-CC-Sign=1D33FA3F444508F3E89B798640B286AD2689F80D6C998B03FC44E3FBB96F7F9F "点击放大")

**图21** 将20个HSP包设计成HAR包   
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4f/v3/Ry69pkjsRkGwo4tadPxdcQ/zh-cn_image_0000002229450981.png?HW-CC-KV=V1&HW-CC-Date=20260612T021549Z&HW-CC-Expire=86400&HW-CC-Sign=26048CDCDF7DF519F0787281A8BF46D14802D2096400EBE99F9F19CF3F630203 "点击放大")

对比数据如下：

| 方案 | 阶段时长(微秒) |
| --- | --- |
| HAP+20个HSP混合打包 | 34643.7 |
| 将20个HSP包设计成HAR包 | 36.4 |

在单HAP场景下，如果需要使用多模块，建议使用多HAR，不建议使用HSP。

### 缩短AbilityStage生命周期阶段耗时

AbilityStage生命周期阶段执行相应的生命周期回调。

**避免在AbilityStage生命周期回调接口进行耗时操作**

在应用启动流程中，系统会执行 AbilityStage 的生命周期回调函数。不建议在这些回调函数中执行耗时操作，例如 onCreate。建议将耗时操作通过异步任务延迟处理或放到其他线程执行。关于线程并发方案，可以参考 [TaskPool和Worker的对比实践](../../../../应用框架/ArkTS语言/TaskPool和Worker对比/bpta-comparative_practice_of_taskpool_and_worker.md)。在这些生命周期回调中，推荐仅执行必要的操作。关于 AbilityStage，可以参考 [AbilityStage组件管理器](<../../../../../harmonyos-guides/应用框架/Ability Kit（程序框架服务）/Stage模型开发指导/Stage模型应用组件/AbilityStage组件管理器/abilitystage.md>)，以下为示例代码：

```
1. const LARGE_NUMBER: number = 100000000;
2. const DELAYED_TIME: number = 1000;

4. @Entry
5. @Component
6. struct Index {
7. @State message: string = 'Hello World';

9. aboutToAppear(): void {
10. console.log('aboutToAppear');
11. this.computeTaskAsync();
12. }

14. // ...

16. computeTask(): void {
17. let count: number = 0;
18. while (count < LARGE_NUMBER) {
19. count++;
20. }
21. }

23. // Asynchronous processing of operation tasks
24. private computeTaskAsync(): void {
25. setTimeout(() => { // SetTimeout is used here to realize asynchronous delayed operation.
26. this.computeTask();
27. }, DELAYED_TIME);
28. }
29. }
```

[ColdStartSpeedOptimization.ets](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/AppColdStart/entry/src/main/ets/pages/ColdStartSpeedOptimization.ets#L17-L57)

使用Launch分析，对比优化前同步执行耗时操作和优化后异步执行耗时操作的启动性能。分析范围从Process Creating到First Frame - Render Phase，优化前后的启动耗时如下图所示。

**图22** 优化前同步执行操作（computeTask），应用冷启动耗时   
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/63/v3/z1VuZ_lSRrWz75vfP33CJg/zh-cn_image_0000002229336541.png?HW-CC-KV=V1&HW-CC-Date=20260612T021549Z&HW-CC-Expire=86400&HW-CC-Sign=7D0380E305F361FBB4EC5FE5C8C5EC1B3747239BD494448E40E814162A728AAD)

**图23** 优化后异步执行操作（computeTaskAsync），应用冷启动耗时   
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/43/v3/vGn8Xm8pTt-2Zn6xdk0QYQ/zh-cn_image_0000002229450973.png?HW-CC-KV=V1&HW-CC-Date=20260612T021549Z&HW-CC-Expire=86400&HW-CC-Sign=698A8D58ED459A19072B3100B3370DBE79798E692A2E42DC972770E490BF1A7F)

使用异步后，应用冷启动时间从2.2秒减少到220.9毫秒，速度提升显著。

### 缩短Ability生命周期阶段耗时

Ability生命周期阶段执行相应的生命周期回调。

**避免在Ability生命周期回调接口进行耗时操作**

在应用启动流程中，系统会执行Ability的生命周期回调函数。因此，不建议在这些回调函数中执行耗时操作，建议通过异步任务延迟处理或者放到其他线程执行。线程并发方案可以参考 [TaskPool和Worker的对比实践](../../../../应用框架/ArkTS语言/TaskPool和Worker对比/bpta-comparative_practice_of_taskpool_and_worker.md)。

在这些生命周期回调里，推荐开发者只做必要的操作，下面以UIAbility为例进行说明。比如在生命周期回调函数onCreate、onWindowStageCreate、onForeground等中执行耗时操作都会导致启动缓慢问题，关于UIAbility组件生命周期的详细说明，参见[UIAbility组件生命周期](<../../../../../harmonyos-guides/应用框架/Ability Kit（程序框架服务）/Stage模型开发指导/Stage模型应用组件/UIAbility组件/UIAbility组件生命周期/uiability-lifecycle.md>)。

**图24** UIAbility生命周期状态

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9e/v3/mR3x89jVRnOxPua4x_AC6w/zh-cn_image_0000002454294977.png?HW-CC-KV=V1&HW-CC-Date=20260612T021549Z&HW-CC-Expire=86400&HW-CC-Sign=86AFD10E5259F3805AD206F53B3DD87C8E40E70EA76D76314C799082EE0FCBA6 "点击放大")

下面示例代码在UIAbility的回调函数onCreate()中分别执行了同步和异步操作：

```
1. import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
2. import { window } from '@kit.ArkUI'

4. const LARGE_NUMBER: number = 100000000;
5. const DELAYED_TIME: number = 1000;

8. export default class EntryAbility extends UIAbility {
9. onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
10. // Time-consuming operation
11. // this.computeTask();
12. this.computeTaskAsync(); // Asynchronous tasks
13. }

15. onWindowStageCreate(windowStage: window.WindowStage): void {
16. windowStage.loadContent('pages/Index', (err, data) => {
17. if (err.code) {
18. console.error('Failed to load the content. Cause: ' + JSON.stringify(err) ?? '');
19. return;
20. }
21. console.info('Succeeded in loading the content. Data: ' + JSON.stringify(data) ?? '');
22. });

24. // Time-consuming operation
25. // this.computeTask();
26. // this.computeTaskAsync(); // Asynchronous mission
27. }

29. onForeground(): void {
30. // Time-consuming operation
31. // this.computeTask();
32. // this.computeTaskAsync(); // Asynchronous mission
33. }

35. private computeTask(): void {
36. let count: number = 0;
37. while (count < LARGE_NUMBER) {
38. count++;
39. }
40. }

42. private computeTaskAsync(): void {
43. setTimeout(() => { // SetTimeout is used here to achieve asynchronous delayed operation.
44. this.computeTask();
45. }, DELAYED_TIME);
46. }
47. }
```

[EntryAbility.ets](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/AppColdStart/entry/src/main/ets/entryability/EntryAbility.ets#L17-L63)

下面使用Launch分析，对比优化前同步执行耗时操作和优化后异步执行耗时操作的启动性能。分析从Process Creating阶段开始，到First Frame - Render Phase阶段结束。优化前后的启动耗时如下图所示。

**图25** 优化前同步执行操作（computeTask），应用冷启动耗时   
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b/v3/AnfBm3y3Sa2IMBX8VGk3hw/zh-cn_image_0000002193851092.png?HW-CC-KV=V1&HW-CC-Date=20260612T021549Z&HW-CC-Expire=86400&HW-CC-Sign=879293B64D1414AC8265943AE05F749F31F70B311529A33E19B229F965C7C965)

**图26** 优化后异步执行操作（computeTaskAsync），应用冷启动耗时   
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/08/v3/FMflJw-oTxWmhnag_TUUFw/zh-cn_image_0000002194010748.png?HW-CC-KV=V1&HW-CC-Date=20260612T021549Z&HW-CC-Expire=86400&HW-CC-Sign=7DCF21F6DE0BE623C706968FAEEF958F7F9AB637603FFEC41FE06CF499763FC7)

使用延时异步后，应用冷启动时间显著提升，耗时从2.1秒减少到220毫秒。

### 缩短加载绘制首页阶段耗时

首页加载绘制阶段主要包含加载首页内容、测量布局、刷新组件和绘制。处理页面生命周期时，避免耗时操作，优先创建首页需要显示的组件，使用if分支语句隐藏不需要显示的组件，减少创建过程的耗时。耗时操作建议通过异步任务或放到其他线程执行，线程并发方案可参考 [TaskPool和Worker的对比实践](../../../../应用框架/ArkTS语言/TaskPool和Worker对比/bpta-comparative_practice_of_taskpool_and_worker.md)。

**自定义组件生命周期回调接口里避免耗时操作**

自定义组件的生命周期变更会调用相应的回调函数，aboutToAppear()函数会在创建自定义组件实例后，页面绘制之前执行，而onPageShow则是在页面进入前台的时候显示，因此避免在这两个回调函数中执行该耗时操作，不阻塞页面绘制。关于自定义组件生命周期的详细说明，参见[页面和自定义组件生命周期](<../../../../../harmonyos-guides/应用框架/ArkUI（方舟UI框架）/UI开发 (ArkTS声明式开发范式)/学习UI范式基本语法/自定义组件/自定义组件生命周期/arkts-page-custom-components-lifecycle.md>)。

**图27** 被@Entry装饰的组件（页面）生命周期

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1e/v3/cW_CKcr7QTmc_-9cDSlwsQ/zh-cn_image_0000002420776488.png?HW-CC-KV=V1&HW-CC-Date=20260612T021549Z&HW-CC-Expire=86400&HW-CC-Sign=661266298C33D3B7473B34FDD85989D4133F0DD78E73A80E975B25219818240C "点击放大")

在Page的回调函数aboutToAppear()中分别执行同步和异步操作的示例代码如下：

```
1. const LARGE_NUMBER: number = 100000000;
2. const DELAYED_TIME: number = 1000;

4. @Entry
5. @Component
6. struct Index {
7. @State message: string = 'Hello World';

9. aboutToAppear(): void {
10. // Time-consuming operation
11. // this.computeTask();
12. this.computeTaskAsync(); // Asynchronous tasks
13. }

15. build() {
16. Row() {
17. Column() {
18. Text(this.message)
19. .fontSize(50)
20. .fontWeight(FontWeight.Bold)
21. }
22. .width('100%')
23. }
24. .height('100%')
25. }

27. private computeTask(): void {
28. let count: number = 0;
29. while (count < LARGE_NUMBER) {
30. count++;
31. }
32. }

34. // Asynchronous processing of computing tasks
35. private computeTaskAsync(): void {
36. setTimeout(() => { // SetTimeout is used here to achieve asynchronous delayed operation.
37. this.computeTask();
38. }, DELAYED_TIME);
39. }
40. }
```

[ComputeTaskAsync.ets](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/AppColdStart/entry/src/main/ets/pages/ComputeTaskAsync.ets#L17-L56)

下面使用Launch分析，对优化前同步执行耗时操作及优化后异步执行耗时操作的启动性能进行对比分析。分析阶段的起点Process Creating，阶段终点为First Frame - Render Phase。

如下图所示，优化前后的启动耗时对比：

**图28** 优化前同步执行操作（computeTask），应用冷启动耗时   
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2a/v3/rIU1nBbhSUODjz4PPW9NCA/zh-cn_image_0000002229336521.png?HW-CC-KV=V1&HW-CC-Date=20260612T021549Z&HW-CC-Expire=86400&HW-CC-Sign=BDE1F80AAC55970AC5CF848C923998122CCF904E8FFAC37C2DAC7245A1EB3A9C)

**图29** 优化后异步执行操作（computeTaskAsync），应用冷启动耗时   
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/96/v3/IFHGhl7HQ-a_1UaTisA2Ng/zh-cn_image_0000002229336501.png?HW-CC-KV=V1&HW-CC-Date=20260612T021549Z&HW-CC-Expire=86400&HW-CC-Sign=1775CA612156B5FABF6288DC09116BCA29E4C6310EA55ECC1F3F5513D6BAB5B7 "点击放大")

使用异步处理后，应用冷启动时间显著提升，耗时从2.4秒减少到238.3毫秒。

**使用本地存储加载首页数据**

在应用启动流程中，大部分应用的首页数据信息需要等待网络请求返回的数据解析结果，因此可以将首页数据通过应用数据持久化的方式进行本地存储，再次冷启动时优先展示已存储数据，网络请求后再次刷新首页数据。

**图30** 使用本地存储首页数据流程图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/db/v3/E1TWCLm-QnGOuFjCbcdWww/zh-cn_image_0000002420776904.png?HW-CC-KV=V1&HW-CC-Date=20260612T021549Z&HW-CC-Expire=86400&HW-CC-Sign=4C1081B8D14495182F28F99ED5EA88B27A431D1D15669A28E42C4C983374E401 "点击放大")

使用本地**存储**优先展示，可减少首帧展示延迟，缩短用户可见白屏时间，提升冷启动体验。

说明

应用需根据自身对于数据的时效性要求，来决定是否使用**本地存储**数据。例如时效性要求为一天时，一天前保存的数据就不适合进行展示，需从网络获取新数据进行展示，并更新本地存储数据。

【场景示例】

应用首页需展示从网站获取的图片信息。在aboutToAppear()中发起网络请求，数据返回并解析后展示在首页。图片信息存储在本地应用沙箱内。再次冷启动时，首先从沙箱获取图片信息，若存在则解析并展示。网络请求返回时，更新图片信息。

以下为关键示例代码：

```
1. import { http } from '@kit.NetworkKit';
2. import { image } from '@kit.ImageKit';
3. import { BusinessError } from '@kit.BasicServicesKit';
4. import { abilityAccessCtrl, common, Permissions } from '@kit.AbilityKit';
5. import { fileIo } from '@kit.CoreFileKit';

7. const PERMISSIONS: Array<Permissions> = [
8. 'ohos.permission.READ_MEDIA',
9. 'ohos.permission.WRITE_MEDIA'
10. ];
11. AppStorage.link('net_picture');
12. PersistentStorage.persistProp('net_picture', '');

14. @Entry
15. @Component
16. struct Index {
17. @State image: PixelMap | undefined = undefined;
18. @State imageBuffer: ArrayBuffer | undefined = undefined; // Picture ArrayBuffer

20. /**
21. * Download picture resources from the Internet through the http request method
22. */
23. async getPicture(): Promise<void> {
24. http.createHttp()
25. .request('https://www.example1.com/POST?e=f&g=h',
26. (error: BusinessError, data: http.HttpResponse) => {
27. if (error) {
28. return;
29. }
30. // Determine whether the resources obtained by the network are of the ArrayBuffer type.
31. if (data.result instanceof ArrayBuffer) {
32. this.imageBuffer = data.result as ArrayBuffer;
33. }
34. this.transcodePixelMap(data);
35. }
36. )
37. }

39. /**
40. * Use createPixelMap to replace pictures of ArrayBuffer type with PixelMap type
41. * @param data：Resources obtained from the network
42. */
43. transcodePixelMap(data: http.HttpResponse): void {
44. if (http.ResponseCode.OK === data.responseCode) {
45. const imageData: ArrayBuffer = data.result as ArrayBuffer;
46. // Create a picture source instance through ArrayBuffer
47. const imageSource: image.ImageSource = image.createImageSource(imageData);
48. const options: image.InitializationOptions = {
49. 'alphaType': 0, // Transparency
50. 'editable': false, // Is it editable?
51. 'pixelFormat': 3, // Pixel format
52. 'scaleMode': 1, // Abbreviation
53. 'size': { height: 100, width: 100 }
54. }; // Create the size of the picture

56. // Create PixelMap through attributes
57. imageSource.createPixelMap(options).then((pixelMap: PixelMap) => {
58. this.image = pixelMap;
59. setTimeout(() => {
60. if (this.imageBuffer !== undefined) {
61. this.saveImage(this.imageBuffer);
62. }
63. }, 0)
64. });
65. }
66. }

68. async saveImage(buffer: ArrayBuffer | string): Promise<void> {
69. try {
70. const context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
71. const filePath: string = context.cacheDir + '/test.jpg';
72. AppStorage.set('net_picture', filePath);
73. const file: fileIo.File = await fileIo.open(filePath, fileIo.OpenMode.READ_WRITE | fileIo.OpenMode.CREATE);
74. await fileIo.write(file.fd, buffer);
75. await fileIo.close(file.fd);
76. } catch (err) {
77. let error = err as BusinessError;
78. console.error(`onAddForm err, code: ${error.code}, message: ${error.message}`);
79. }
80. }

82. async useCachePic(): Promise<void> {
83. if (AppStorage.get('net_picture') !== '') {
84. // Get the ArrayBuffer of the picture
85. const imageSource: image.ImageSource = image.createImageSource(AppStorage.get('net_picture'));
86. const options: image.InitializationOptions = {
87. 'alphaType': 0, // transparency
88. 'editable': false, // Is it editable?
89. 'pixelFormat': 3, // pixel format
90. 'scaleMode': 1, // Abbreviated value
91. 'size': { height: 100, width: 100 }
92. };
93. imageSource.createPixelMap(options).then((pixelMap: PixelMap) => {
94. this.image = pixelMap;
95. });
96. }
97. }

99. async aboutToAppear(): Promise<void> {
100. const context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
101. const atManager: abilityAccessCtrl.AtManager = abilityAccessCtrl.createAtManager();
102. await atManager.requestPermissionsFromUser(context, PERMISSIONS);
103. this.useCachePic(); // Get data from local storage
104. this.getPicture(); // Obtain data from the network side
105. }

107. build() {
108. Column() {
109. Image(this.image)
110. .objectFit(ImageFit.Contain)
111. .width('50%')
112. .height('50%')
113. }
114. }
115. }
```

[ScenariosExample.ets](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/AppColdStart/entry/src/main/ets/pages/ScenariosExample.ets#L17-L131)

下面对比优化前后的启动性能。分析阶段从启动Ability开始，到首次解析Pixelmap后的第一个vsync结束。

**图31** 优化前未使用本地存储数据   
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cb/v3/vuIlOMpLRESp3VeiXQrxHA/zh-cn_image_0000002229336461.png?HW-CC-KV=V1&HW-CC-Date=20260612T021549Z&HW-CC-Expire=86400&HW-CC-Sign=61AC7F06CD9D40911EB5A48287AA8137E4266121721E27451F660C8EC7AED3B0 "点击放大")

**图32** 优化后使用本地存储数据   
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5c/v3/dp2AHfI7RbecX7mFTd-o4Q/zh-cn_image_0000002194010688.png?HW-CC-KV=V1&HW-CC-Date=20260612T021549Z&HW-CC-Expire=86400&HW-CC-Sign=CE69232CFC437C0C033800D8FBEC3BCB4468C0D966E67FA74324F1627D225357 "点击放大")

对比数据如下：

| 方案 | 阶段时长(毫秒) |
| --- | --- |
| （优化前）未使用本地存储 | 641.8 |
| （优化后）使用本地存储 | 68.9 |

使用本地存储后，应用冷启动时从Ability启动到图片显示的阶段耗时明显减少。

针对应用冷启动过程中网络请求耗时久的问题，提供了一个三方库供开发者使用，优化方式是首页内容复用，先使用本地缓存的数据。三方库链接：[首页数据缓存](https://ohpm.openharmony.cn/#/cn/detail/@hadss%2Fdatacache)。加速应用冷启动的使用方法可参考：[基于DataCache提升应用冷启动速度](https://gitcode.com/harmonyos_samples/DataCache)。

**优化首页显示速度**

启动过程从用户点击应用入口到首页数据显示在屏幕上，这是对用户点击事件响应的过程。开发者可以通过UI优化、并发优化、代码逻辑优化及IPC通信优化等方法来提升首页的响应速度，具体可参考：[点击响应时延分析](../../../性能分析/点击响应时延分析/bpta-click-to-click-response-optimization.md)。

## 总结

本文介绍了应用冷启动的流程，如何识别和分析冷启动缓慢问题，以及针对冷启动各阶段的注意事项和优化方法。

* 非冷启动所需的服务或模块可以延迟加载。
* 将网络请求提前至AbilityStage/UIAbility的onCreate()生命周期回调函数中，提前首刷或二刷时间，减少用户等待时间。
* 建议将启动页图标startWindowIcon的分辨率设置为不超过256px\*256px。
* 在AbilityStage、UIAbility和自定义组件的生命周期回调函数中，不建议直接执行复杂的计算任务、同步文件读写等耗时任务。建议通过异步任务或在其他线程中处理。
* 按需导入模块，移除初始化阶段不必要的模块导入，动态加载耗时的模块。
* 减少使用嵌套的export \*全量导出和import \*全量引用。
* 拆分HAR包导出文件或导入冷启动相关文件时，使用全路径，减少应用冷启动的.ets文件执行耗时。
* 避免多个HAP/HSP对相同HAR的引用。
* 在单HAP场景下，建议模块使用多HAR，而不推荐使用HSP。
* 建议通过使用合理的布局结构和懒加载等UI优化方法来减少首帧绘制时间。
* 建议使用本地存储首页数据，以减少首帧展示完成的时延，并减少用户可见的白屏或白块时间。

希望通过本文的学习，开发者可以了解和识别应用启动耗时的问题，有助于开发者提升应用冷启动速度，提升用户体验。
