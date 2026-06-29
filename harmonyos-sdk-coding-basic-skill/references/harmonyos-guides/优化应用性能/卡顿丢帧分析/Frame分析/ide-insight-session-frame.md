---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-insight-session-frame
title: Frame分析
breadcrumb: 指南 > 优化应用性能 > 卡顿丢帧分析 > Frame分析
category: harmonyos-guides
scraped_at: 2026-06-11T15:31:29+08:00
doc_updated_at: 2026-06-10
content_hash: sha256:d35ceb0ec2c4a01d9d5355b9b9345e3262c580e745cb91d984f9a2c6e619d66f
---
开发应用或元服务过程中，如果发现有表单滑动不顺畅、页面交互延迟、动效不流畅等卡顿现象时，可以使用DevEco Profiler提供的Frame场景分析能力，录制卡顿过程中的关键数据进行分析，从而识别出导致卡顿丢帧的原因。

此外，Frame任务窗口还集成了Time、CPU、Network场景分析任务的功能，方便开发者在分析丢帧数据时同步对比同一时段的其他资源占用情况。

说明

* 在任务分析窗口中，可通过[快捷键](../../附录/快捷键/ide-shortcut-key.md)缩放时间轴、移动时间轴、添加时间标签等。
* Frame分析支持离线符号解析能力，请参见[离线符号解析](../../基础耗时：Time分析/ide-insight-session-time.md#section186881175012)。
* Frame分析支持Energy泳道，请参见[定位能耗问题](../../能耗诊断：Energy分析/ide-profiler-energy.md#section889733410010)。

## 查看GPU使用情况

1. 创建Frame分析任务并录制相关数据，操作方法可参考[性能问题定位：深度录制](../../使用Profiler进行性能调优/性能问题定位：深度录制/deep-recording.md)，或在会话区选择**Open File**，导入历史数据。
2. “Frame”泳道显示当前设备的GPU的使用率，将其展开，子泳道显示Render Service侧帧数据和App侧帧数据。

   说明

   * 一帧的绘制，一般需要由App侧提交渲染到Render Service侧，然后Render Service侧再提交给硬件进行合成渲染，因此App侧的帧和Render Service侧的帧存在关联的情况。并且可能多个APP侧的帧/同一APP侧的多个帧提交到同一个Render Service侧帧上，出现帧之间的一对多的关联情况。
   * 一帧绘制的期望耗时，与fps的大小有关，一般情况下fps为60，对应的Vsync周期为16.6ms，即App侧/Render Service侧的帧耗时，一般需要在16.6ms以内。App侧帧/Render Service侧帧判断卡顿的标准为帧的实际结束时间晚于帧的期望结束时间。
   * 在“RS Frame”和“App Frame”标签的泳道中，正常完成渲染的帧显示为绿色，出现卡顿的帧显示为红色。
   * 除“RS Frame”和“App Frame”泳道外的“ArkTS Callstack”、“Callstack”、“CPU Core”等泳道信息，请参考[基础耗时：Time分析](../../基础耗时：Time分析/ide-insight-session-time.md)、[CPU活动分析](../../CPU活动分析/ide-insight-session-cpu.md)。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/25/v3/7Q6CuyxFT4Wwf3C_8RZt2A/zh-cn_image_0000002602186189.png?HW-CC-KV=V1&HW-CC-Date=20260611T073128Z&HW-CC-Expire=86400&HW-CC-Sign=E4EEFD511633503BC7323DDAF9CFE1AB8A790454897FC724F085C89FA2695137 "点击放大")

## 查看指定时间段内所有进程的Frame数据统计信息

1. 在时间轴上拖拽鼠标选定要查看的时间段。
2. 框选Frame主泳道。

   窗口下方的“Statistics”区域中会以进程维度对选定时间段内的Frame信息进行统计，包括卡顿率、卡顿次数、最大连续卡顿次数、最大卡顿耗时、平均卡顿耗时以及平均正常耗时等。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/32/v3/T5CeaMgiTCKNYHieFcSXeg/zh-cn_image_0000002571387012.png?HW-CC-KV=V1&HW-CC-Date=20260611T073128Z&HW-CC-Expire=86400&HW-CC-Sign=256A9B25B786BD0C639ABDB49E890D3C68088914D330A295ECB5A2E8516C092A "点击放大")
3. 点击“Statistics”列表中任一进程的跳转按钮，在“Frame List”区域将展现该进程对应的Frame列表。体现各帧的起始时间、总耗时、GPU耗时以及卡顿丢帧类型。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ac/v3/IWUjTT8wTCKGQKW684Uu-w/zh-cn_image_0000002571546640.png?HW-CC-KV=V1&HW-CC-Date=20260611T073128Z&HW-CC-Expire=86400&HW-CC-Sign=D647F27AA4495BE2F08A5CC0F8CBAE72CAE70536370F0CA1F48529D7D5855EFE "点击放大")
4. 单击“Frame List”列表中任意一帧，右侧的“More”区域会中显示该帧更多关键信息。在获取该帧的预期起始时间、预期持续时间之外，您可以单击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/89/v3/cydllUDrQY2OMY3gHvFbBg/zh-cn_image_0000002571387006.png?HW-CC-KV=V1&HW-CC-Date=20260611T073128Z&HW-CC-Expire=86400&HW-CC-Sign=05AE1D3124D7A2CA00528D282B406A773B0676F52761DD8295E751D3EEFC8B83)跳转至关联的切片。

## 查看指定Frame页面布局信息

从DevEco Studio 5.1.0 Release版本开始，支持查看最新录制的Session中指定的Frame页面布局信息。

从DevEco Studio 6.1.0 Beta1版本开始，![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3c/v3/Tfjh-AijTaCiSHm3Q3Nikw/zh-cn_image_0000002571546648.png?HW-CC-KV=V1&HW-CC-Date=20260611T073128Z&HW-CC-Expire=86400&HW-CC-Sign=3FC704044C243D3F1C6C788564A3581B25DB75C5511C72C1B5FA47E37D7F78BE)按钮中新增Frame Layout开关，开发者可自行设置开关状态。开关关闭时，不支持查看最新录制的Session中指定的Frame页面布局信息，默认关闭。

暂不支持在Wearable设备上查看指定Frame页面布局信息。

1. 单击RS Frame泳道或APP Frame泳道中任意一帧，“Details”区域中会展示该帧具体信息。点击**Open Layout**按钮，将在ArkUI Inspector中直接打开相应arkli文件；点击**Download Layout**将arkli文件下载到指定目录，之后可手动导入[ArkUI Inspector](../../../编写与调试应用/应用调试/布局分析/ide-arkui-inspector.md)查看页面布局信息。

   说明

   单击“Download Layout”或 “Open Layout”前，需应用进程置于前台，才能正确回放全量渲染数据，获取arkli文件。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/91/v3/OKIClvpvQb6MpMYeGrex5Q/zh-cn_image_0000002602186171.png?HW-CC-KV=V1&HW-CC-Date=20260611T073128Z&HW-CC-Expire=86400&HW-CC-Sign=DA3C7D3141679BB1E7E72BA760322ED129C11C977124C98CB831260306325AF4 "点击放大")
2. 在ArkUI Inspector中可查看组件树和组件属性信息，当前支持BackgroundFilter、nodeGroup、nodeGroupReuseCache组件。
   * BackgroundFilter：背景滤波器。
   * nodeGroup：节点组类型，0表示非节点组节点，1表示被动画标记的节点组，2表示被UI标记的节点组，4表示被用户标记的节点组，8表示被前景滤波器标记的节点组。
   * nodeGroupReuseCache： 0表示在生成缓存或无需缓存，1表示在重用缓存。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fa/v3/zAeAO3UBTam_8Oyb5BztWw/zh-cn_image_0000002571387008.png?HW-CC-KV=V1&HW-CC-Date=20260611T073128Z&HW-CC-Expire=86400&HW-CC-Sign=95E2D3DE59C4FE9FFC6E72D3A5DD36DE29466C5F8CE569110ABE205F29DC27AD "点击放大")

## 查看指定时间段内指定进程的Frame数据统计信息

1. 在时间轴上拖拽鼠标选定要查看的时间段。
2. 选择要观察的子泳道（例如带“RS Frame”标签的泳道）。

   窗口下方的“Details”区域中会显示选定时间段内的RS帧统计信息列表，体现各帧的起始时间、总耗时、GPU耗时以及卡顿丢帧类型。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/be/v3/W0ui3k2SRhqv9OvlkcmkLg/zh-cn_image_0000002571546646.png?HW-CC-KV=V1&HW-CC-Date=20260611T073128Z&HW-CC-Expire=86400&HW-CC-Sign=9F5B984CC53D56FCAA2E7F57F202397F222DF012CB64263269AAF9127FE7DDBD "点击放大")
3. 单击列表中任意一帧，右侧的“More”区域会中显示该帧更多关键信息。在获取该帧的预期起始时间、预期持续时间之外，您可以单击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a0/v3/rl1zz7OmTmW0vVOMPevZHA/zh-cn_image_0000002571546632.png?HW-CC-KV=V1&HW-CC-Date=20260611T073128Z&HW-CC-Expire=86400&HW-CC-Sign=E656F0707BC20B6A4635C59C254DDF8AC71377C1F134D72F88089E1187CE400C)跳转至关联的切片。

## 查看指定Frame信息

在子泳道（例如带“APP Frame”标签的泳道）中选中要查看的Frame，该泳道上方是耗时最长的非UI函数，下方是UI主线程泳道。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bc/v3/Zz3IO9RTQ9aS1iR7AzmcMA/zh-cn_image_0000002571546638.png?HW-CC-KV=V1&HW-CC-Date=20260611T073128Z&HW-CC-Expire=86400&HW-CC-Sign=6A4F927773F8448D82820C561C418CA5E384243A2663CFD4B687DB946F26EDE2 "点击放大")

窗口下方的“Frame”区域中会显示选定帧的关键信息，如VSync编号、开始时间、App应用侧持续时间、App应用侧业务逻辑耗时、Render Service侧持续时间、GPU持续时间、总持续时间、卡顿丢帧类型以及可能出现卡顿的原因等。“Non UI”区域中会显示非UI耗时最大的函数，如开始时间、结束时间、持续时间，函数名等。

说明

* 在选定观察对象后，DevEco Profiler会自动关联与其相关的切片，用箭头连接。
* 如果该帧是由于超出期望结束时间引起的，则显示两条线，对应期望开始时间（Expected Start）和期望结束时间（Expected End），用于关联分析同一时刻Trace或者函数采样信息。
* 将鼠标悬浮在任意帧上，会冒泡显示该帧的Jank信息。
* 卡顿丢帧类型（Jank Type）：No Jank（不卡顿）、AppDeadlineMissed（App侧的卡顿）、RenderDeadlineMissed（Render Service侧的卡顿）。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/69/v3/r7--nXEUSKC3HcVW9x8xzA/zh-cn_image_0000002602186173.png?HW-CC-KV=V1&HW-CC-Date=20260611T073128Z&HW-CC-Expire=86400&HW-CC-Sign=C1E8DDD0CF1BB35FC0CBE48EC1AAD3071455F81100B174D86535B238060980D3 "点击放大")

## 查看屏幕帧率动态变化场景下丢帧和卡顿信息

Frame泳道下新增Lost Frames和Hitch Time两类子泳道，用于识别和优化卡顿和丢帧现象。

* Hitch Time：展示当前时间段内卡顿时长。计算方式为渲染前后两帧的间隔减去单帧耗时，若计算结果大于单帧耗时\*70%，则视为出现卡顿现象。
* Lost Frames：展示当前时间段内丢帧数。Lost Frames计算出的结果，六舍七入统计取整。

1. 创建Frame模板并录制会话，如存在卡顿和丢帧现象，会在Lost Frames和Hitch Time泳道对应时间显示矩形图。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/96/v3/rehQ0YamSVSP0PM6WwxTAA/zh-cn_image_0000002571546654.png?HW-CC-KV=V1&HW-CC-Date=20260611T073128Z&HW-CC-Expire=86400&HW-CC-Sign=1B860450713DFA83E3C75A87C296EBE802CEF90402ACACBE4F0BFABCEB12CFE0 "点击放大")
2. 鼠标点选某一时间点，提示信息会显示该点所属时间段内的丢帧数以及卡顿时间。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b2/v3/h-EGeQxISAeNj2W1u6-6lw/zh-cn_image_0000002602066129.png?HW-CC-KV=V1&HW-CC-Date=20260611T073128Z&HW-CC-Expire=86400&HW-CC-Sign=A2DEC579B326FA21AFB2D2CC860DE7FE8C6445CB875C1F2B338CBCA37C49803F "点击放大")

## 支持动效场景调优

开发者在开发应用时，会使用到动效，动效的卡顿影响到用户的使用体验。DevEco Profiler提供动效场景的调优，能帮助开发者优化动效场景。

鼠标放置在某个动效上，显示该动效的详细信息，包括响应时延、动效持续时间、完成时延、期望帧率、FPS。

说明

* 响应时延：<=85ms 绿色，85ms~150ms 浅绿色，150ms ~250ms 浅红色，>250ms深红色。
* 期望帧率：当前系统运行满帧帧率，如60HZ、90HZ、120HZ。智能刷新率模式下，不展示期望帧率。
* 动效持续时间：根据帧率展示颜色，FPS大于达标帧率即为绿色，小于则为深红色。智能刷新率模式下，帧率可变，颜色为灰色。达标帧率与期望帧率的大小有关，一般情况下期望帧率为60HZ，则达标帧率= 60HZ \* 91.7%。
* 完成时延：响应时延和动效持续时间只要有一个为深红色，完成时延为深红色。
* Launch模板中Frame泳道点击detail区启动动效详情信息，more区域展示动效帧Animation Data List信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/33/v3/Cl6zMV0VTO6-GlCxyHftcQ/zh-cn_image_0000002602186167.png?HW-CC-KV=V1&HW-CC-Date=20260611T073128Z&HW-CC-Expire=86400&HW-CC-Sign=72C8D0290656AA7EFDE3CEBE6A2B836921F8F150B29A7D883732F97A3F881708 "点击放大")

## 查看组件动画信息

从DevEco Studio 6.0.0.828版本开始，Frame泳道下新增Component Animation子泳道，用于从组件的角度展示应用中包含的各种动画类型，包括属性动画 (animation)、显式动画 (animateTo)、关键帧动画 (keyframeAnimateTo)以及页面间转场 (pageTransition)。

在Details页签中，可以查看每个动画的详细信息，包括起止时间、帧率、动画曲线类型以及影响的组件属性等。

单击列表中任意一动画，右侧的“More”区域会中显示该动画所影响的组件属性的具体变化过程。![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e1/v3/r985bVtmQRWWJZf1Ge1c-Q/zh-cn_image_0000002571387010.png?HW-CC-KV=V1&HW-CC-Date=20260611T073128Z&HW-CC-Expire=86400&HW-CC-Sign=1DEDF6D778B1686DEC059A96A9D0842BF851E4635E851FCF9DCFD0BEEDF22171 "点击放大")

## 查看组件帧率信息

Frame泳道下新增两类子泳道，分别为Display Vsync与DisplaySync\_cb(tid)，用于对可变帧率的检测调优。

* Display Vsync：该泳道显示对应时间段的屏幕刷新率，支持对框选的时间段内的vsync进行分布统计。区分“<=30HZ”、“30~60HZ”、“60~90HZ”、“>90HZ”。统计值包括框选时间段内各区间的分布比率、最小/最大/平均时长以及平均HZ。如果某场景满足了帧率改变的要求，当底层系统根据机制进行变帧，相应的情况会展现在对应的泳道，帮助开发者了解vsync的变化情况是否符合预期。该泳道仅支持在配备硬件屏幕的设备上进行数据采集。
* DisplaySync\_cb(tid)：该泳道显示对应组件的帧率，如DisplaySync、XComponent两类接口组件动画对应的帧率。调测时，不同场景下由于帧率可变，系统实际表现是否符合预期，需要有实际的检测手段。尤其是由于DisplaySync的渲染均在UI主线程执行，当存在多个需要渲染的组件需要同时执行时，只能在UI主线程排队，此时任何一个组件的延迟都会对其他组件的渲染产生影响，导致UI卡顿。

  如下图所示，vsync2和vsync4中，vsync周期内的组件由于渲染耗时长，导致以下两个vsync周期挤掉下一个vsync周期的渲染时间，导致掉帧的情况产生。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ee/v3/k31UaXXYRPKwuxQntLRMJw/zh-cn_image_0000002571546634.png?HW-CC-KV=V1&HW-CC-Date=20260611T073128Z&HW-CC-Expire=86400&HW-CC-Sign=F319F48E539B0CE79A3F25E519DD5FB24F03EDAB48F296830FA82A5608C08B80 "点击放大")

1. 选择Display Vsync泳道，在时间轴上拖拽鼠标选定要查看的时间段。
2. 详情区显示当前时间段的屏幕刷新率，当前帧最大持续时间、最小持续时间、平均持续时间以及该时间段内平均帧数。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/be/v3/xrZynl7BTaWqzrlUNwjA3g/zh-cn_image_0000002602066131.png?HW-CC-KV=V1&HW-CC-Date=20260611T073128Z&HW-CC-Expire=86400&HW-CC-Sign=5EC9497CA41454E61574717F0A53FB007FB9EC2C61741010FA7A7FE6102E030E "点击放大")
3. 点选Display Vsync泳道，可以查看当前帧的耗时和帧率。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/43/v3/ohh4iw06Q_etw-vZzlje1w/zh-cn_image_0000002571387016.png?HW-CC-KV=V1&HW-CC-Date=20260611T073128Z&HW-CC-Expire=86400&HW-CC-Sign=F5746A683E061DD88E800A82EECF81140EFF0942E611F610ACAC392362D07440 "点击放大")
4. 框选DisplaySync\_cb泳道，可以查看应用侧对应组件的帧率，渲染时间等信息。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d1/v3/UNqNiSSXSmSt1e2vvughxQ/zh-cn_image_0000002602186181.png?HW-CC-KV=V1&HW-CC-Date=20260611T073128Z&HW-CC-Expire=86400&HW-CC-Sign=8CC67740606312235D39DE88BF453B6166A28880AE5326FD13412EC3F5A95939 "点击放大")
5. 同时如果组件有可能的掉帧情况，DisplaySync\_cb泳道显示对应的掉帧情况并标红展示。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6b/v3/fgqvSInYRkiuMUJd9_8mUw/zh-cn_image_0000002602186169.png?HW-CC-KV=V1&HW-CC-Date=20260611T073128Z&HW-CC-Expire=86400&HW-CC-Sign=AF185870D0FCF371204EF85F423DC4E2644EA6E6739E7E5F7505BA88F56E3FB1 "点击放大")

## 查看帧率统计信息

Frame泳道中的App Frame泳道和RS Frame泳道在框选时新增fps标记。RS泳道新增过滤按钮，用于过滤ArkWeb数据。

1. 展开Frame泳道，框选一段数据。
2. 泳道出现fps标记，展示当前框选范围内的帧率统计信息。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/71/v3/5t6GJl5ZTOqI_7QwXm60GA/zh-cn_image_0000002602066123.png?HW-CC-KV=V1&HW-CC-Date=20260611T073128Z&HW-CC-Expire=86400&HW-CC-Sign=C8B9E862B65AD854E610049EA06773881850DA6AEA960B8E6DFBC8D1B66FDCE7 "点击放大")
3. 打开Only ArkWeb data开关，筛选过滤出包含ArkWeb帧的数据。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e9/v3/9V6QCes8SpCttgebgbv0ZQ/zh-cn_image_0000002571546636.png?HW-CC-KV=V1&HW-CC-Date=20260611T073128Z&HW-CC-Expire=86400&HW-CC-Sign=502905346F7F502C29BD48CF56929E4B87B90338445D691D6ED699AABE4EB1EC "点击放大")

## Anomaly泳道：查看解码过度耗时和超过阈值的序列化、反序列化操作

如果工程中存在图片资源，并感知到解码绘制/渲染过程存在卡顿，可以通过Anomaly泳道查看主线程解码过程中是否存在解码过度耗时告警，并确认发生告警的时段。

如果应用中使用了worker、Taskpool工作线程等场景，通常会触发跨线程对象传递，并触发序列化和反序列化的操作。对于耗时超过阈值的序列化、反序列化操作，Anomaly也会给出对应的耗时告警，并给出发送这个操作的开始时间和耗时时间。

1. 在时间轴上拖拽鼠标选定出现告警的时间段。当耗时超过VSync周期的50%时，将在Anomaly泳道中出现红色告警，提示“Image decoding has exceeded 50% of the VSync time”。
2. 详情区给出录制时段内解码过度耗时的统计情况，包括类型，图片名，计数，总耗时，最小耗时、平均耗时、最大耗时，耗时标准差、 图源尺寸大小，目标尺寸大小等。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4e/v3/Dlz8G_wdSIeTdz0s1jkvFg/zh-cn_image_0000002602186175.png?HW-CC-KV=V1&HW-CC-Date=20260611T073128Z&HW-CC-Expire=86400&HW-CC-Sign=91A9A24D40232E9336A3E5A7E09D1BF0F1A2F39CE06843285EEBD2160FA019EB "点击放大")
3. 对于耗时超过阈值的序列化、反序列化操作，Anomaly也会给出对应的耗时告警。其中可以通过泳道启动配置按钮配置检测阈值，默认配置阈值为8ms。
4. 详情区给出录制时段内序列化、反序列化耗时情况统计信息，包括类型、计数、总耗时、最小耗时、平均耗时、最大耗时、耗时标准差等。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8c/v3/UyRr5HoVSJSjXIEmdQ7Cyg/zh-cn_image_0000002602186165.png?HW-CC-KV=V1&HW-CC-Date=20260611T073128Z&HW-CC-Expire=86400&HW-CC-Sign=B6CD771DB6F680684C5731694B8072E41A2EB884F2E3DF6987B29764608B2824 "点击放大")

   说明

   已上架应用市场的应用不支持录制Anomaly泳道。

## User Events泳道：查看用户事件耗时

开发者在卡顿丢帧场景可通过User Event用户事件，查看用户事件开始时间、应用开始处理时间以及应用处理耗时等情况。

1. 选择User Event泳道，在时间轴上拖拽鼠标选定要查看的时间段。
2. 详情区列表给出录制时间段内用户事件详情，包括用户事件ID、事件开始时间Input Time、应用开始处理时间Processing Start、应用处理耗时Duration和事件类型User Event Type。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/aa/v3/YXrJVb4nRbiAlYmZi_YAtA/zh-cn_image_0000002602066117.png?HW-CC-KV=V1&HW-CC-Date=20260611T073128Z&HW-CC-Expire=86400&HW-CC-Sign=B50A82081F6BEBE3C9DB87FB27D690ADC9AF5C861AEBE345B36AFBD7C200C243 "点击放大")
3. 点选User Event泳道中的条块，Slice详情区展示该事件的详情信息。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/12/v3/N5iGvV7dTj6qkEpD6w2edQ/zh-cn_image_0000002571546656.png?HW-CC-KV=V1&HW-CC-Date=20260611T073128Z&HW-CC-Expire=86400&HW-CC-Sign=8FD277852967F7FE2465AF46A173CDF6C0550A553DC8FA9763FE32206B69161B "点击放大")

更多性能调优最佳实践，请参考[点击响应时延分析](../../../../best-practices/性能/性能分析/点击响应时延分析/bpta-click-to-click-response-optimization.md)、[点击完成时延分析](../../../../best-practices/性能/性能分析/点击完成时延分析/bpta-click-to-complete-delay-analysis.md)、[帧率问题分析](../../../../best-practices/性能/性能分析/帧率问题分析/bpta-zhenlv.md)、[Web点击响应时延分析](../../../../best-practices/性能/性能分析/Web点击响应时延分析/bpta-web-click-response-delay-analysis.md)、[Web加载完成时延分析](../../../../best-practices/性能/性能分析/Web加载完成时延分析/bpta-web-completion-delay-analysis.md)。
