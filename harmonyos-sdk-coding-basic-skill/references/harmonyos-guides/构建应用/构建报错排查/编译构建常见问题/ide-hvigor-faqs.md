---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hvigor-faqs
title: 编译构建常见问题
breadcrumb: 指南 > 构建应用 > 构建报错排查 > 编译构建常见问题
category: harmonyos-guides
scraped_at: 2026-06-11T15:31:10+08:00
doc_updated_at: 2026-06-10
content_hash: sha256:398e71c9ec22351c0296f908b267cecf5cc36e863e72ba3152a397d8d7ba535c
---
## 如何解决编译过程内存过高

**问题现象**

编译构建时，内存或CPU占用过高，导致出现DevEco Studio运行卡顿、延迟等现象。

**解决措施**

* 在执行hvigor构建的过程中，通过减少内存中的缓存数据、减少线程数量，可以减少编译过程中的内存占用。

  可以在hvigor-config.json5中添加配置。

  ```
  1. "properties": {
  2. // 配置为0，表示不启用内存缓存配置，默认为4，数值越低，内存中缓存数据越少
  3. "hvigor.pool.cache.capacity": 0,
  4. // 默认配置为cpu核数-1， 包含ohos.arkCompile.maxSize，值越小，占用内存越少
  5. "hvigor.pool.maxSize" : 5,
  6. // 默认配置值为5, 值越小，占用内存越少
  7. "ohos.arkCompile.maxSize": 3,
  8. // 默认配置值为true, 表示开启内存缓存，占用内存较多，配置为false，关闭内存缓存，占用内存较少
  9. "hvigor.enableMemoryCache": false
  10. },
  ```

  说明

  当配置项"hvigor.pool.maxSize"和"ohos.arkCompile.maxSize"的值改小，"hvigor.enableMemoryCache"改为false后，可能会导致编译时长增加，请耐心等待。

* 如果以上修改没有取得明显的效果，可以使用非并行的模式来执行编译。
  + 在菜单栏点击“File > Settings（macOS为DevEco Studio > Preferences/Settings） > Build, Execution, Deployment > Build Tools > Hvigor”，取消勾选“Execute tasks in parallel mode (may require larger heap size)”。

    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/89/v3/Y3bqJjcXSj6l3hge_Ymd7Q/zh-cn_image_0000002602066477.png?HW-CC-KV=V1&HW-CC-Date=20260611T073108Z&HW-CC-Expire=86400&HW-CC-Sign=04E87CF516D809ACC8817805F67155D7E74D245EAB64100471E8CDAEE78F6F4E)
  + 流水线场景中，在命令行最后增加 --no-parallel，示例：

    ```
    1. hvigorw assembleHap --no-parallel
    ```

  说明

  使用非并行模式编译，内存占用会减少，但可能会导致编译时长增加，请耐心等待。

## 构建报错“Cannot read properties of undefined(reading 'XXX')”

请先根据XXX的值从以下场景排查，没解决问题再参考最终方案。

* **场景一：**

  **问题现象**

  编译构建时，出现报错“Cannot read properties of undefined(reading 'setEnabled')”。

  **问题确认**

  hvigorfile.ts里有如下代码：

  ```
  1. import { hvigor, getHvigorNode } from "@ohos/hvigor"
  2. import { hapTasks} from '@ohos/hvigor-ohos-plugin';
  3. // 问题代码
  4. getHvigorNode(__filename).getTaskByName('XXX').setEnabled(false);
  5. export default {
  6. system: hapTasks, /* Built-in plugin of Hvigor. It cannot be modified. */
  7. plugins: []         /* Custom plugin to extend the functionality of Hvigor. */
  8. }
  ```

  **处理措施**

  1. 确保XXX是当前的HvigorNode里存在的任务。

     假设是entry模块的hvigorfile.ts中的代码导致的问题 ，XXX的有效值就是下图中的“default@SignHap”、“default@CollectDebugSymbol”、“assembleHap”等值。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/02/v3/QK8YfOwgRXGgwCEz4msn4g/zh-cn_image_0000002602066539.png?HW-CC-KV=V1&HW-CC-Date=20260611T073108Z&HW-CC-Expire=86400&HW-CC-Sign=C77BDD46127BA4A3808DF5EE89CCA92704C816D6558A19FC45F07AF1CE60BE48)
  2. 确保getTaskByName的使用位置是在[Hvigor的配置阶段](../../概述/构建系统生命周期/ide-hvigor-life-cycle.md#section746253616316)及之后的生命周期里，包括beforeNodeEvaluate、afterNodeEvaluate、nodesEvaluated、taskGraphResolved、buildFinished。
* **场景二：**

  **问题现象**

  编译构建时，出现报错“Cannot read properties of undefined(reading 'isSO')”。

  **处理措施**

  升级到DevEco Studio 5.1.0.840及以上的版本。
* **场景三：**

  **问题现象**

  编译构建时，出现报错“Cannot read properties of undefined(reading 'getPluginId')”**。**

  **处理措施**

  确保hvigorfile.ts里export default的对象中的字段system的值是appTasks/hapTasks/hspTasks/harTasks之一。

  ```
  1. import { appTasks } from '@ohos/hvigor-ohos-plugin';

  3. export default {
  4. system: appTasks,  /* Built-in plugin of Hvigor. It cannot be modified. */
  5. plugins:[]         /* Custom plugin to extend the functionality of Hvigor. */
  6. }
  ```
* **场景四：**

  **问题现象**

  编译构建时，出现报错“Cannot read properties of undefined(reading 'getNeedExecTargetServiceList')”**。**

  **处理措施**

  确保模块下的module.json5的type字段的值和hvigorfile.ts中export default的对象的system字段符合以下对应关系：

  **表1**

  | module.json5的type字段 | hvigorfile.ts中export default的对象的system字段 |
  | --- | --- |
  | entry | hapTasks |
  | feature | hapTasks |
  | shared | hspTasks |
  | har | harTasks |
* **场景五：**

  **问题现象**

  编译构建时，出现报错“Cannot read properties of undefined(reading 'app')”。

  **处理措施**

  确保工程目录下AppScope/app.json5文件存在。
* **场景六：**

  **问题现象**

  Linux环境下，执行单元测试，出现报错“Cannot read properties of undefined(reading 'toString')”。

  **处理措施**

  Linux环境暂不支持单元测试。
* **场景七：**

  **问题现象**

  编译构建时，出现报错“Cannot read properties of undefined(reading 'kind')”。

  **处理措施**

  检查ArkTS代码是否有如下写法：

  ```
  1. // 错误写法：空数组
  2. class w {
  3. public a: [][] = []
  4. test() {
  5. console.log("1", this.a[0])
  6. }
  7. }
  8. // 正确写法
  9. class w {
  10. public a: string[][] = []
  11. test() {
  12. console.log("1", this.a[0])
  13. }
  14. }
  ```
* **场景八：**

  **问题现象**

  编译构建时，出现报错“Cannot read properties of undefined(reading 'clear')”。

  **问题确认**

  在工程根目录hvigor/hvigor-config.json5文件中配置如下内容打开堆栈。

  ```
  1. "debugging": {
  2. "stacktrace": true                /* Disable stacktrace compilation. Value: [ true | false ]. Default: false */
  3. },
  ```

  确认堆栈内容是否如下。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5a/v3/xp8mnqxWTa-yVhYXkobX0w/zh-cn_image_0000002571387378.png?HW-CC-KV=V1&HW-CC-Date=20260611T073108Z&HW-CC-Expire=86400&HW-CC-Sign=6212D92CDCFE924C24653E371DF8444A3B85D26EFA43FBB23E2066A6FCD05EDE)

  **处理措施**

  确认DevEco Studio是否有使用安全加固等三方插件。如果有，可以先禁用三方插件，看是否会复现问题，还能复现就参考下面的最终方案。
* **最终方案：**

  如果以上场景都不符合，打开堆栈后，根据堆栈信息排查代码。

  堆栈打开方法：工程根目录hvigor/hvigor-config.json5文件中配置如下内容。

  ```
  1. "debugging": {
  2. "stacktrace": true                /* Disable stacktrace compilation. Value: [ true | false ]. Default: false */
  3. },
  ```

  优先排查hvigorconfig.ts文件和hvigorfile.ts文件，其他代码次之。

  如果上述文件中并未排查出问题，请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。

## 构建报错“Duplicated files found in module xxx. This may cause unexpected errors at runtime”

**问题现象**

编译构建时，出现报错“Duplicated files found in module xxx. This may cause unexpected errors at runtime”。

问题原因是构建时存在不同版本的同名so文件。比如将har模块产物里的so文件拷贝到entry模块的libs目录下，这时har模块里有一个libhar.so，entry模块里也有一个libhar.so，再配置entry依赖har，构建entry就会出现报错。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7b/v3/QHdHMPbARlycuoH3WTz6Kg/zh-cn_image_0000002602186589.png?HW-CC-KV=V1&HW-CC-Date=20260611T073108Z&HW-CC-Expire=86400&HW-CC-Sign=4C621E37C2945AB809D59FE3140AC19A8E6A8565AAA355D94B0D7B337E7EB0CF)

**解决措施**

使用select、pickFirsts、pickLasts等配置选中要使用的so文件; select提供native产物的精准选择能力，优先级高于excludes、pickFirsts等配置项。pickFirsts、pickLasts按照.so文件的优先级顺序，打包最高优先级的.so文件，优先级顺序是指依赖收集的顺序，越晚被收集优先级越高。

具体可参考：[配置CPP](../../配置构建流程/配置CPP/ide-hvigor-cpp.md)。

基于上面的例子，可以在entry的build-profile.json5中添加配置select选中har模块中的so文件，package选中包名为“har”的模块, include选中“libhar.so”文件。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1b/v3/5K7YsowgTE68wdJiSqk8zg/zh-cn_image_0000002602066483.png?HW-CC-KV=V1&HW-CC-Date=20260611T073108Z&HW-CC-Expire=86400&HW-CC-Sign=8E8A9549EED58B366074A7568FF1D387B5C668DC64AAA23328F89CD370F7CA5F)

## 构建报错“input module releaseType is different”

**问题现象**

打包APP时，提示“input module releaseType is different”。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/95/v3/ecnfsoW2S8m_Dp6i9ZhckA/zh-cn_image_0000002602186587.png?HW-CC-KV=V1&HW-CC-Date=20260611T073108Z&HW-CC-Expire=86400&HW-CC-Sign=2903158F91DA9BF8CC0FA83ED8AC1B9F893E9266FED0E1CD20FB7E0B2F385C7D)

**解决措施**

根据报错日志的Warning信息所提示的模块名称，检查模块间的apiReleaseType字段是否一致。

该apiReleaseType字段由编译构建工具自动生成，保存在HAP/HSP包的module.json文件中。如下图所示，首先确认各模块间该字段是否一致，如果存在不一致的情况，需要将应用的各个模块，使用相同版本的SDK重新打包，然后打包APP。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cd/v3/WuUgvEpASMW-FetrEUwp0w/zh-cn_image_0000002602066449.png?HW-CC-KV=V1&HW-CC-Date=20260611T073108Z&HW-CC-Expire=86400&HW-CC-Sign=B45EF0B461866FE8A26FFABDF94FD38E58A99ECF59E6EBB286895A426B3744D7)

## 构建报错“debug is different”

**问题现象**

打包APP时，提示“debug is different”。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0/v3/DsxSYn6SS6WoRbcTs0a50g/zh-cn_image_0000002602186493.png?HW-CC-KV=V1&HW-CC-Date=20260611T073108Z&HW-CC-Expire=86400&HW-CC-Sign=17CF8392F5CD3555B8D7657E8CF25696018268FA8740ABC793E95D09B97C4D92)

**解决措施**

根据报错日志的Warning信息所提示的模块名称，检查模块间的debug字段是否一致，尤其需要关注本地模块和外部引用模块之间是否一致。

1.该debug字段由编译构建工具自动生成，保存在HAP/HSP包的module.json文件中，如下图所示，首先确认各模块间该字段是否一致。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/53/v3/G5_t5sxOTSyraNUcVIZOAA/zh-cn_image_0000002602066459.png?HW-CC-KV=V1&HW-CC-Date=20260611T073108Z&HW-CC-Expire=86400&HW-CC-Sign=678BEC096126862C99E949E59E13C220E925D677E2293639C985E9DE380646C2)

2.编译工具根据设置的Build Mode选项生成debug标识，如图所示，可以通过此处进行设置。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/48/v3/rpvjeUVIRIO-UQw7B2-Iaw/zh-cn_image_0000002571387330.png?HW-CC-KV=V1&HW-CC-Date=20260611T073108Z&HW-CC-Expire=86400&HW-CC-Sign=4F47A67EA2BBDA85209EFDE7B1D15312D305A1F29FB5AC4497A6126DF48B7919)

## 构建报错“proxy data is duplicated”

**问题现象**

打包APP时，提示“uri datashareproxy://bundleName/\*\* in proxy data is duplicated”。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f1/v3/bZS5xS9XTDqpKK547xk86w/zh-cn_image_0000002571546986.png?HW-CC-KV=V1&HW-CC-Date=20260611T073108Z&HW-CC-Expire=86400&HW-CC-Sign=79A9C0F82B4FEF4B4FC9A3223E1D70014599036F7099E683F07DA84EDEF2795C)

**解决措施**

proxyData标识模块提供的数据代理列表，只允许entry和feature配置，不同的proxyData中配置的URI不可重复。遇到此问题，检查模块间是否配置了相同uri的proxyData。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b8/v3/Kaa_3cPwTESlJxk3e4Eptg/zh-cn_image_0000002571387338.png?HW-CC-KV=V1&HW-CC-Date=20260611T073108Z&HW-CC-Expire=86400&HW-CC-Sign=A0388DDDEE8F8CCAD655AFDEFAB9DC1C5EFCBDB68174C1A540130D9BBE358B51)

## 编译报错“Init keystore failed: parseAlgParameters failed: ObjectIdentifier()”

**问题现象**

编译构建时，出现错误：Init keystore failed: parseAlgParameters failed: ObjectIdentifier()。

```
1. hap-sign-tool: error: ACCESS_ERROR, code: 109. Details:   Init keystore failed: parseAlgParameters failed: ObjectIdentifier() -- data isn't an object ID (tag = 48)   Detail: Please check the message from tools
```

**错误原因**

使用高版本JDK生成密钥对(p12)，再使用低版本的JDK执行签名命令时，会因为不兼容导致解析p12失败，从而签名失败。

**场景**

1. 使用DevEco Studio生产密钥对时，DevEco Studio默认会调用软件内预置的JDK17，而用户使用本地的低版本JDK进行签名时则会报错。
2. 用户本地使用高版本JDK生成密钥对时，又通过DevEco Studio进行签名，DevEco Studio中预置的JDK17版本低于用户的JDK，导致报错。

**解决方案**

请检查当前使用的JDK版本和生产密钥对使用的JDK版本，使用版本匹配的JDK执行签名命令。

## 编译报错“generate SignerBlock failed”

**问题现象**

编译构建时，出现错误：message:generate SignerBlock failed。

```
1. hap-sign-tool: error: {errorcode:0,message:generate SignerBlock failed}
```

**错误原因**

签名用的公私钥对不匹配，使用私钥签名后，用公钥验签失败。需保证私钥(keyalias)和公钥(appCertPath)配对使用。

**场景**

1. 本地生产签名材料时，未导出正确的keyalias对应的csr(证书请求文件)，导致生成证书时，公钥与keyalias对应的私钥不匹配。
2. 签名过程参数填写错误，使用了错误的keyalias或者appCertPath文件。

**解决方案**

请选择正确、配对的keyalias和appCertPath文件。

## 编译报错“java.io.IOException: DerValue.getOID, not an OID 49”

**问题现象**

编译构建时，出现错误：java.io.IOException: DerValue.getOID, not an OID 49。

```
1. hap-sign-tool: error: ACCESS_ERROR, code: 109. Details: java.io.IOException: DerValue.getOID, not an OID 49 Detail: Please check the message from tools
```

**报错原因**

证书文件解析失败，找不到证书的OID。

**场景**

1. 证书被篡改。
2. appCertPath参数中传入了非证书文件。

**解决方案**

请检查证书文件是否正确。

## 编译报错“JS heap out of memory”

**问题现象**

编译构建时，出现报错“JS heap out of memory“。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/47/v3/D5fUPL4FShigFJJJ16iTOA/zh-cn_image_0000002602186551.png?HW-CC-KV=V1&HW-CC-Date=20260611T073108Z&HW-CC-Expire=86400&HW-CC-Sign=59CA1877F7689606B7963C7D45042871ED89C5CF8E90EE392526A6EA076BD06F)

**解决措施**

出现该报错的原因是Hvigor运行时内存不足，在使用3.1.0及以上版本的Hvigor时，可通过以下方式修改Hvigor运行时内存的最大值。

勾选Enable the Daemon for tasks：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/92/v3/M76rQB_XT4aeCqfbzqkMfA/zh-cn_image_0000002602066491.png?HW-CC-KV=V1&HW-CC-Date=20260611T073108Z&HW-CC-Expire=86400&HW-CC-Sign=A9167575A7E60CFC6BC5F96BF0F0251C2E4EECCFAB34A28EC048E1DB238B9FF0)

在hvigor-config.json5中修改maxOldSpaceSize字段，根据工程的大小，适当将其增大（如设置为8192）：

```
1. "nodeOptions": {
2. "maxOldSpaceSize": 8192
3. }
```

## Linux环境下编译报错“JS heap out of memory”

**问题现象**

在Linux环境下，系统内存有64G，Hvigorw脚本中配置--max-old-space-size=40960，在编译构建时，实际在使用内存未达到配置的内存（例如使用到20G左右）就出现报错“JS heap out of memory“。

```
1. FATAL ERROR: NewSpace::Rebalance Allocation failed - JavaScript heap out of memory
2. Writing Node.js report to file: report.20200512.172528.47517.24.011.json
3. Node.js report completed
4. 1: 0xa295e0 node::Abort() [node]
5. 2: 0x9782df node::FatalError(char const*, char const*) [node]
6. 3: 0xb99c2e v8::Utils::ReportOOMFailure(v8::internal::Isolate*, char const*, bool) [node]
7. 4: 0xb99fa7 v8::internal::V8::FatalProcessOutOfMemory(v8::internal::Isolate*, char const*, bool) [node]
8. 5: 0xd3a3b5 [node]
9. 6: 0xd74f27 [node]
10. 7: 0xd84707 v8::internal::MarkCompactCollector::CollectGarbage() [node]
11. 8: 0xd481b9 v8::internal::Heap::MarkCompact() [node]
12. 9: 0xd48f0b v8::internal::Heap::PerformGarbageCollection(v8::internal::GarbageCollector, v8::GCCallbackFlags) [node]
13. 10: 0xd499a5 v8::internal::Heap::CollectGarbage(v8::internal::AllocationSpace, v8::internal::GarbageCollectionReason, v8::GCCallbackFlags) [node]
14. 11: 0xd4aebf v8::internal::Heap::HandleGCRequest() [node]
15. 12: 0xcf5f97 v8::internal::StackGuard::HandleInterrupts() [node]
16. 13: 0x104b803 v8::internal::Runtime_StackGuard(int, unsigned long*, v8::internal::Isolate*) [node]
17. 14: 0x13a5a99 [node]
18. Aborted (core dumped)
```

**问题原因**

vm.max\_map\_count是一个与内核虚拟内存子系统相关的参数，用于控制进程可以拥有的内存映射区域的最大数量。它通常用于限制一个进程可以打开的文件数量，特别是在使用大量内存映射文件的情况下。

在Linux系统上，vm.max\_map\_count参数的默认值通常是较小的数值，例如65530。然而，对于一些需要大量内存映射的应用程序或者特定的使用场景，可能需要增加该参数的值，以便支持更多的内存映射区域。

**解决措施**

修改vm.max\_map\_count的值：

* 临时修改：

  ```
  1. sysctl -w vm.max_map_count=新值
  ```
* 永久修改：如果希望永久修改参数的值，可以编辑/etc/sysctl.conf文件，并添加或修改以下行：

  ```
  1. vm.max_map_count=新值
  ```

  保存文件后，使用以下命令使更改生效：

  ```
  1. sysctl -p
  ```

## 编译报错“Cannot find module XXX or its corresponding type declarations”

* **场景一：**

  **问题现象**

  Stage模板工程编译引用native文件(.so) 提示 "Cannot find module XXX or its corresponding type declarations."。

  **处理措施**

  当前Stage工程在编译构建阶段新增对native文件(.so)导出符号的语法校验，如果引用了没有对应声明文件(.d.ts)的native文件(.so)的现有工程在编译构建阶段，语法校验工具便会报错提示找不到对应的声明文件。

  如果出现类似问题，可尝试通过如下方式进行解决：

  1. 在对应cpp目录下新建types/libxxx目录，并在该目录下新增index.d.ts用于声明native的类型符号；新增oh-package.json5配置文件用于校验工具的模块查询。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bd/v3/UoEoYHbxTHaee3E94toomg/zh-cn_image_0000002602066457.png?HW-CC-KV=V1&HW-CC-Date=20260611T073108Z&HW-CC-Expire=86400&HW-CC-Sign=E7A61CAAD1CBE12A866D24F62E35A3B733D33585BCEEEA1CF796BDB1F2709C95)

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ed/v3/-Zh1kzmXT_WoQRijv7enCQ/zh-cn_image_0000002571387376.png?HW-CC-KV=V1&HW-CC-Date=20260611T073108Z&HW-CC-Expire=86400&HW-CC-Sign=028B310E8D7A026F974B2E0FF71E55EC482599E29EDDD9E5CDA3E51BBAFA4B2B)
  2. 在native引用的模块内的oh-package.json5中添加native模块的本地依赖，并根据提示点击**Sync Now**同步工程，下图以entry模块引用native模块为例。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9b/v3/sQfxCrsLSBm1-qT6ThGmWg/zh-cn_image_0000002602186523.png?HW-CC-KV=V1&HW-CC-Date=20260611T073108Z&HW-CC-Expire=86400&HW-CC-Sign=28C9E65DABCF8FDA17B1CFCAD2E45BE4ED5A0398EAB044F6B0E8A3D2A684095D)

* 场景二：

  **问题现象**

  引用三方包，构建失败，提示“Cannot find module 'xxx' or its corresponding type declarations”。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7c/v3/J9sFT5l_QIeGNxSNvFkgVQ/zh-cn_image_0000002571547020.png?HW-CC-KV=V1&HW-CC-Date=20260611T073108Z&HW-CC-Expire=86400&HW-CC-Sign=B5BD56D9DC9419315FE4CC2C7A80282A324F291F9853AD34C5088FDFF224A9B3)

  **处理措施**

  进入对应模块级oh-package.json5文件或工程级oh-package.json5文件中查看三方包是否已安装，若未安装，需执行ohpm install安装；若已安装，需查看“main”字段是否配置正确，若未配置或配置错误，需配置为正确的入口文件。
* 场景三：

  **问题现象**

  引用的包路径被混淆，代码中又是在引用包后面拼接了路径，导致模块引用不到而报错。

  例如：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c6/v3/j7HzlQcKRFea8l-sN_7GbQ/zh-cn_image_0000002571387318.png?HW-CC-KV=V1&HW-CC-Date=20260611T073108Z&HW-CC-Expire=86400&HW-CC-Sign=A4BFD663ECD2B52A7EA2B468E7E0CE8B52E1A76D4A9EF0534BD9F6A108715562)

  代码中这样引用

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/49/v3/oHi4aSRcTj2Epszvo-hatw/zh-cn_image_0000002602186561.png?HW-CC-KV=V1&HW-CC-Date=20260611T073108Z&HW-CC-Expire=86400&HW-CC-Sign=66431C86B487C70F45211F3B8396E7768DAABCC65E33A2CAE4528EFB071F95F7)这样引用会找不到模块，导致报错。

  **处理措施**

  修改引用方式，改为推荐的引用方式

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/75/v3/eLksCGGeTia7nsKYdptK4w/zh-cn_image_0000002602066515.png?HW-CC-KV=V1&HW-CC-Date=20260611T073108Z&HW-CC-Expire=86400&HW-CC-Sign=FF882DE0C3132B0BCF7E7CA7444BED743760AA3AF9E4E80A63F44519BA654348)
* 场景四：

  **问题现象**

  被引用模块oh\_package.json5配置有误，执行了ohpm install 并且成功地安装了依赖，但是还报错模块找不到。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/60/v3/GrsmJc0PQPSPOdPU4YbAYA/zh-cn_image_0000002571547072.png?HW-CC-KV=V1&HW-CC-Date=20260611T073108Z&HW-CC-Expire=86400&HW-CC-Sign=D33214C647AFD0C2778C48F8CD319CFC8A49EF893427A76FC971187B37F33C1D)

  被引用模块的 oh\_package.json5 中配置了错误的types字段。

  该字段优先于main字段。 如果 types 字段配置的不存在，就会报错模块找不到。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/95/v3/EtZjDEy4Sl-hEWyz2ssTvg/zh-cn_image_0000002602066495.png?HW-CC-KV=V1&HW-CC-Date=20260611T073108Z&HW-CC-Expire=86400&HW-CC-Sign=9A5641E28F5FB7C468AC8A20D5A5C34D465ADAB6D700A9C0CFB9DCB5ADA1E2B2)

  **处理措施**

  如果该包中没有d.ets声明，则这个字段可以删除。配置不存在或者错误，会导致报错。
* 场景五：

  **问题现象**

  oh\_package.json5 中 dependencies 中引入模块的 名称 和 实际使用时 import 的 不一致。

  例如 在 oh\_package.json5 中这样引入：

  ```
  1. "dependencies": {   "har": "file:../har" }
  ```

  但是实际上在代码中import 的时候是 大写 HAR 或者其他而不是 dependencies 里面配置的 ‘har’ 的值，要注意保持完全一致。（目前windows 没有问题，linux会报错模块找不到）

  **处理措施**

  引入和使用改成一致。
* 场景六：

  **问题现象**

  引用模块的 oh\_package.json5 中 main 字段值和实际的文件名称大小写不一致。

  **处理措施**

  将main字段和实际文件名称的大小写改为一致。
* 场景七：

  **问题现象**

  Stage模板工程编译构建失败，提示 "Cannot find module '@bundle:rollup\_plugin\_ignore\_empty\_module\_placeholder' or its corresponding type declarations"。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bd/v3/1WT9GM_fRLKe0Zgg_cZTXA/zh-cn_image_0000002602066549.png?HW-CC-KV=V1&HW-CC-Date=20260611T073108Z&HW-CC-Expire=86400&HW-CC-Sign=08BC1903D86FB739D0B6F9C846B3E9978C1BA0E7612B7D357690D11FA2EE4782)

  **解决措施**

  该问题是由于工程引用了无对应实现文件的.d.ts声明文件：

  1. 通过在build目录中搜索'rollup\_plugin\_ignore\_empty\_module\_placeholder'，找到报错的中间文件，并根据中间文件找到对应工程文件。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/66/v3/RME0-OMDTEKIwGdhSETkvQ/zh-cn_image_0000002602186559.png?HW-CC-KV=V1&HW-CC-Date=20260611T073108Z&HW-CC-Expire=86400&HW-CC-Sign=6B16FFD229AB33377286E952D92C133A9A177CCAE813F137E6909C32892883D7)

     在输入栏中输入rollup\_plugin\_ignore\_empty\_module\_placeholder，找到问题模块的中间文件。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e0/v3/j2IRL7fCR9ylLKOEV05KYA/zh-cn_image_0000002602066455.png?HW-CC-KV=V1&HW-CC-Date=20260611T073108Z&HW-CC-Expire=86400&HW-CC-Sign=0946ED23719AF9959349D5F2B8DB8BAE9CC73E526EE148EDB116173C1A87ED2A)
  2. 在引用类型文件中通过添加type显式声明符号类型引用：

     ```
     1. export type {T} from './type';
     ```

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/75/v3/xzoCjgqNQZmrc8Y0ZJSZcw/zh-cn_image_0000002602186599.png?HW-CC-KV=V1&HW-CC-Date=20260611T073108Z&HW-CC-Expire=86400&HW-CC-Sign=A1301ED37E84E2DD70EB3399C86233402E6D161F2E5E7F350B02AEC54C8C9CCC)
  3. 同时排查是否从d.ts/d.ets中引用值类型符号，禁止在声明文件中声明值变量。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d9/v3/UwX14kZ-SZ2ISeOKErxDhw/zh-cn_image_0000002571546990.png?HW-CC-KV=V1&HW-CC-Date=20260611T073108Z&HW-CC-Expire=86400&HW-CC-Sign=1ED82AE4FC14EF3C93C96F4F8903AF761985ADAD123C8F69FC39A90C415963D2)

## 编译报错“Module 'xxx' has no exported member 'yyy'”

**问题现象**

Stage模板工程编译构建失败，提示 "Module 'xxx' has no exported member 'yyy'" 并且"yyy"符号是由export \* from 'x.js'语法从js文件中导出。

**处理措施**

当前Stage工程编译构建期的语法校验工具对js文件不作检查，因此当使用export \* from 'x.js'导出js文件中的符号时，符号引用处便会提示"Module 'xxx' has no exported member 'yyy'"的错误信息。

如果出现类似问题，可尝试通过如下方式进行解决：

* 方法1（推荐使用）： 使用符号显式导出语法，从js文件中re-export符号 。

  ```
  1. export { yyy } from 'x.js'
  ```

* 方法2：新增x.js对应的声明文件(.d.ts)，并在引用时不指定后缀。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2/v3/1fkefLjHRLmQbg0QxHOnEA/zh-cn_image_0000002602186601.png?HW-CC-KV=V1&HW-CC-Date=20260611T073108Z&HW-CC-Expire=86400&HW-CC-Sign=6AC774524D4FF2FAE5350405EBF79F8358CA3E8951B9F57DB9FE70D106B6785B)

## 编译报错“Could not load ${file1} (imported by ${file2}): Maximum call stack size exceeded”

**问题现象**

Stage模板工程编译构建失败，提示 "ERROR: Could not load ${file1} (imported by ${file2}): Maximum call stack size exceeded"。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/91/v3/wx_OTpogRLmh11Y7A8KGAg/zh-cn_image_0000002602186605.png?HW-CC-KV=V1&HW-CC-Date=20260611T073108Z&HW-CC-Expire=86400&HW-CC-Sign=07A5BE9EF6314B73DBB9D6AEE8DB014D43DD3A7ABBCDBD7ED0481EED2215A632)

**处理措施**

该问题是由于file1为当前工程外的代码：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d7/v3/HM9qR8njTu-EHmANyvcfdQ/zh-cn_image_0000002571547062.png?HW-CC-KV=V1&HW-CC-Date=20260611T073108Z&HW-CC-Expire=86400&HW-CC-Sign=5FF570AC61F1BD627B57188E40C06FF399812B81B8DA0A62C6123A089F219873)

请新建Static Library模块，并将工程外的代码迁移至Static Library模块内，并使用HAP引用HAR方式进行模块间引用。

## 编译报错“Failed to get a resolved OhmUrl by filepath xx”

* **场景一：**

  **问题现象**

  三方包在配置依赖时，配置到devDependencies，源码中又有引用依赖中的API时，编译失败。如以下示例：三方包@hms-security/ucs-appauth将依赖@network/gr配置在devDependencies中，源码中使用了@network/grs的API时，编译失败，提示“ERROR: ArkTS:ERROR Failed to get a resolved OhmUrl by filepath xxx”。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5a/v3/5VzTTC31S--_pmgbY3RqBw/zh-cn_image_0000002571387436.png?HW-CC-KV=V1&HW-CC-Date=20260611T073108Z&HW-CC-Expire=86400&HW-CC-Sign=62C3A9E0AE1BAA640598547671FA37BFF6297B7D9A3F15252622F9892FCC5D64)

  **问题确认**
  1. 进入上面报黄色的源码文件中，可以看到依赖有红色告警信息。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a9/v3/9uPxIZxbTPCtJ3PsVPZfVA/zh-cn_image_0000002571546994.png?HW-CC-KV=V1&HW-CC-Date=20260611T073108Z&HW-CC-Expire=86400&HW-CC-Sign=0FF212C1EE9D84DE22DE1A6EC63150C373D2AD0505F45B60B75EFD228E6777B9 "点击放大")
  2. 进入包下的oh-package.json5文件，查看依赖配置为devDependencies。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/67/v3/3Wy7PHBBQiGmxWUN-nf8sw/zh-cn_image_0000002571387402.png?HW-CC-KV=V1&HW-CC-Date=20260611T073108Z&HW-CC-Expire=86400&HW-CC-Sign=5F27331DA78595DAD5EC13E951CFFCEB6351D8D5EE6EE54DC198BB1DEEBDE765)

  **处理措施**
  + 向此包开发团队提改进建议：运行时的依赖，不能配置在devDependencies中。
  + 可在依赖上层引入对应devDependencies中的三方包规避此问题。

* **场景二：**

  **问题现象**

  DevEco Studio编译失败，提示“ERROR: ArkTS:ERROR Failed to get a resolved OhmUrl by filepath xxx”。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8c/v3/g-DAY9I0SC2Hsh6FP3B6Gg/zh-cn_image_0000002571387334.png?HW-CC-KV=V1&HW-CC-Date=20260611T073108Z&HW-CC-Expire=86400&HW-CC-Sign=3F558385AC7C3DB581E01148EF4516225A04411A8BD13249A9B9FD24FF35B851)

  **问题确认**

  查看工程目录下的build-profile.json5文件中modules字段配置的srcPath路径是否与真实路径不相同，是否存在大小写不一致问题。

  **处理措施**

  将工程目录下的build-profile.json5文件中modules字段配置的srcPath路径与真实路径保持一致。
* **场景三：**

  **问题现象**

  工程A以相对路径引用了工程B的模块，这种引用会导致报错。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9e/v3/nOz0tmVsSEmgUmcvdrYYuA/zh-cn_image_0000002602186553.png?HW-CC-KV=V1&HW-CC-Date=20260611T073108Z&HW-CC-Expire=86400&HW-CC-Sign=A138F81724F136E594DF0F07B1EC1A4E040B5F5AA4BE57C460E618F7244702E4)

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b2/v3/KEX8nL6tTeO_7CdbFKzvgw/zh-cn_image_0000002571387390.png?HW-CC-KV=V1&HW-CC-Date=20260611T073108Z&HW-CC-Expire=86400&HW-CC-Sign=180AA839F5616B043CD5BBC06DDFE573CE43E95487633A03DEEABB5C450E0ADC)![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7f/v3/x8M2VJi9SjGM6feCy7bjRw/zh-cn_image_0000002571547024.png?HW-CC-KV=V1&HW-CC-Date=20260611T073108Z&HW-CC-Expire=86400&HW-CC-Sign=D5397946C236F2574EAD8A02763833981845E51020A07DDC284FD912E2E3CA19)**处理措施**

  + 把工程B这种的har转至工程A里，作为A的一个模块引用。
  + 把工程B的har提前打包，在A中 以.har的方式引用。
  + 上传到仓库，以版本号的方式引用。
* **场景四：**

  **问题现象**

  DevEco Studio编译失败，提示“Error Message: Failed to get a resolved OhmUrl for 'hvigor\_ignore\_xxxxx' imported by xxx”。

  **处理措施**

  如果hvigor\_ignore\_xxxxx所在的模块是一个har模块，需要排查oh\_package.json5中是否存在"packageType": "InterfaceHar"，如果存在，请删除"packageType": "InterfaceHar"。
* **场景五：**

  **问题现象**

  DevEco Studio编译失败，提示“Failed to get a resolved OhmUrl for 'xxx' imported by 'yyy'”。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c5/v3/PDIdF4YcRUSs2x_3LwdErg/zh-cn_image_0000002571546996.png?HW-CC-KV=V1&HW-CC-Date=20260611T073108Z&HW-CC-Expire=86400&HW-CC-Sign=8FA863764DE5F31C534BBEB6B924FAD2742B5C020D6BD7839B0FCA273CF7EDF2 "点击放大")

  **问题确认**

  1. 排查yyy所在模块是否为[字节码har](../../配置构建流程/构建HAR/ide-hvigor-build-har.md#section16598338112415)，查看工程级build-profile.json5的useNormalizedOHMUrl是否为true（缺省默认值为false），如果为true则默认构建字节码har。
  2. 如果yyy所在模块是字节码har，请排查xxx依赖是否被配置在工程级oh\_package.json5的dependencies，但没有配置在yyy模块级oh\_package.json5的dependencies中。

  **处理措施**

  + 将xxx依赖配置到yyy模块oh\_package.json5的dependencies中。

    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fc/v3/3dX3o7CST0SIDPdme_dBng/zh-cn_image_0000002602186529.png?HW-CC-KV=V1&HW-CC-Date=20260611T073108Z&HW-CC-Expire=86400&HW-CC-Sign=F02D69DFF56552247C2A549DDAD1F257ED26C560040A7849FECA0D848DCA5BCD "点击放大")
  + 将yyy模块改为非字节码har，在模块级build-profile.json5文件中添加byteCodeHar字段并设置为false。

    ```
    1. "buildOption": {
    2. "arkOptions": {
    3. "byteCodeHar": false
    4. }
    5. }
    ```
* **场景六：**

  请确认当前使用的DevEco Studio和SDK版本是配套的，点击菜单栏**Help > About DevEco Studio**，**Help > About HarmonyOS SDK**分别查看配套的DevEco Studio和SDK版本。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f5/v3/1zigz81RS3G-0C3TFaMVfw/zh-cn_image_0000002602186611.png?HW-CC-KV=V1&HW-CC-Date=20260611T073108Z&HW-CC-Expire=86400&HW-CC-Sign=DECD522D586C4C2C299742E16194836797382FFA77324028F9E62B0F6032BD27)
* **场景七：**

  **问题现象：**

  DevEco Studio编译失败，提示 "ERROR: ArkTS:ERROR failed to execute es2abc ERROR: ArkTS:ERROR Failed to get a resolved OhmUrl by filepath xxx"。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d2/v3/kj_QQgF-S4yTdiUkJ6bjxQ/zh-cn_image_0000002602066487.png?HW-CC-KV=V1&HW-CC-Date=20260611T073108Z&HW-CC-Expire=86400&HW-CC-Sign=B046694EA88B3B62572A8D18E9FE600964E6AD9035696F35D5E46BD5C8F57DEE)

  **处理措施**

  该问题是由于在工程中引用了非工程标准模块目录（即目录内无模块描述文件module.json5），如下图utils目录所示：请新建Static Library模块，并将utils/common里面的代码迁移至Static Library模块内，并使用HAP引用HAR方式进行模块间引用。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/71/v3/HQeeYSZATYa9-pnpmBLpKw/zh-cn_image_0000002571546978.png?HW-CC-KV=V1&HW-CC-Date=20260611T073108Z&HW-CC-Expire=86400&HW-CC-Sign=6E47A5D52058E762FD6074AF5BC2A2DF62D914791E248C99C620EAB659775C40)

## 编译报错“Property xxx does not exist on type 'typeof BuildProfile'.”

**问题现象****1**

使用了自定义参数BuildProfile，编译态无异常但编译构建失败，提示“Property xxx does not exist on type 'typeof BuildProfile'.”。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4d/v3/zHerqzGnR7uRssKjqa6bRw/zh-cn_image_0000002571387404.png?HW-CC-KV=V1&HW-CC-Date=20260611T073108Z&HW-CC-Expire=86400&HW-CC-Sign=125295F468DF12883720A7C0461DC1A0F4BBCBEABDDB6589B3463EF567FD6CDA)

**处理措施**

检查在当前模块下build-profile.json5中的targets > buildProfileFields配置的自定义参数中key值是否相同，如果不同请将targets内所有buildProfileFields中的key值保持相同。

以下为导致编译报错的**错误**配置示例：

```
1. "targets": [
2. {
3. "name": "default",
4. "config": {
5. "buildOption": {
6. "arkOptions": {
7. "buildProfileFields": {
8. "targetName": "default"
9. }
10. }
11. }
12. }
13. },
14. {
15. "name": "default1",
16. "config": {
17. "buildOption": {
18. "arkOptions": {
19. "buildProfileFields": {
20. "targetName1": "default1"
21. }
22. }
23. }
24. }
25. },
26. ]
```

请将targets内所有buildProfileFields中的key值修改一致，如以下示例：

```
1. "targets": [
2. {
3. "name": "default",
4. "config": {
5. "buildOption": {
6. "arkOptions": {
7. "buildProfileFields": {
8. "targetName": "default"
9. }
10. }
11. }
12. }
13. },
14. {
15. "name": "default1",
16. "config": {
17. "buildOption": {
18. "arkOptions": {
19. "buildProfileFields": {
20. "targetName": "default1"
21. }
22. }
23. }
24. }
25. },
26. ]
```

**问题现象2**

使用了自定义参数BuildProfile并且编译器标红且构建失败，提示“Property xxx does not exist on type 'typeof BuildProfile'.”。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/65/v3/9kpf4g65TC2RPDeVY607Tg/zh-cn_image_0000002602066437.png?HW-CC-KV=V1&HW-CC-Date=20260611T073108Z&HW-CC-Expire=86400&HW-CC-Sign=35AA803EDDF01258CFDC4B76A74509145F0EACCCDEA06B0E6058632B701CFD7A)

**处理措施**

请检查当前模块下build-profile.json5中buildProfileFields内是否添加了所使用的自定义参数，请确保该自定义参数已配置在buildProfileFields内。

## C++工程编译导致电脑卡顿的处理建议

**问题现象**

在执行代码规模较大的C++工程的编译时，由于C++编译时的CPU占用率较高，可能出现电脑卡顿、反应迟缓等现象。

**处理措施**

如果出现类似问题，可尝试通过如下方式进行解决：

打开模块下的build-profile.json5文件，在**arguments**参数中添加如下配置。并根据电脑CPU配置，修改compile和link的值。建议compile和link的值之和，设置为CPU核数的一半，如CPU为8核，则compile和link分别设置为2。

```
1. "arguments": "-DCMAKE_JOB_POOL_COMPILE:STRING=compile -DCMAKE_JOB_POOL_LINK:STRING=link -DCMAKE_JOB_POOLS:STRING=compile=2;link=2",
```

需要说明的是，修改了compile和link的值，可能会导致编译时长增加，请耐心等待。

## CPP编译报错"A 'undefined symbol' error has occurred"

**问题现象**

在编译HarmonyOS C++ 项目时，报错提示"A 'undefined symbol' error has occurred"。

**解决措施**

"undefined symbol"错误通常表示链接器找不到特定符号的定义。这通常是因为源文件没有正确编译或链接，或者因为缺少必要的库文件。以下是如何定位和解决这个问题的步骤：

1. 确保所有源文件都已包含在 CMake 构建中。

首先，检查您的 CMakeLists.txt 文件，确保所有相关的源文件都已包含在项目中。

**示例 CMakeLists.txt**

```
1. cmake_minimum_required(VERSION 3.10)
2. project(MyProject)
3. set(CMAKE_CXX_STANDARD 17)
4. include_directories(${CMAKE_CURRENT_SOURCE_DIR}
5. ${CMAKE_CURRENT_SOURCE_DIR}/include)
6. # 添加所有源文件
7. add_library(myProgram SHARED main.cpp myLibrary.cpp)
```

2. 确认源文件的符号定义。

确保在所有相关的源文件中正确定义了符号。例如，检查 myLibrary.cpp 是否包含 myFunction 的定义：

**myLibrary.cpp**

```
1. #include "myLibrary.h"
2. void myFunction() {
3. // Function implementation
4. }
```

**myLibrary.h**

```
1. #ifndef MY_LIBRARY_H
2. #define MY_LIBRARY_H
3. void myFunction();
4. #endif
```

3. 检查编译和链接顺序。

确保所有源文件和库文件按照正确的顺序进行编译和链接。CMake 和 Ninja 通常会处理这个问题，但在手动编译时可能会出现问题。

4. 清理和重新生成构建文件。

有时，构建文件可能会损坏或丢失符号定义。尝试清理构建目录并重新生成构建文件：

```
1. hvigorw clean 1
```

或手动删除模块下.cxx目录。

5. 检查库路径和链接器标志。

如果使用三方库，确保 CMakeLists.txt 中正确配置了库路径和链接器标志。例如：

```
1. cmake_minimum_required(VERSION 3.10)
2. project(MyProject)
3. set(CMAKE_CXX_STANDARD 17)
4. # 确保添加三方库的头文件
5. include_directories(${PATH_TO_EXTERNAL_LIBRARY}
6. ${PATH_TO_EXTERNAL_LIBRARY}/include)
7. # 添加源文件
8. add_library(myProgram SHARED main.cpp myLibrary.cpp)
9. # 链接三方库
10. target_link_libraries(myProgram PUBLIC /path/to/external/library)
```

6. 启用详细编译和链接输出。

为了解详细的编译和链接过程，可以启用更详细的输出。在 CMakeLists.txt 中添加以下内容：

```
1. set(CMAKE_VERBOSE_MAKEFILE ON)
```

7. 检查 Ninja 输出日志。

Ninja 默认生成 .ninja\_log 文件，其中包含构建过程的详细信息。您可以检查这个日志文件以了解构建过程中的问题。

```
1. cat {module}/.cxx/default/default/arm64-v8a/.ninja_log
```

检查编译日志中是否存在符号所在的源文件或头文件。

8. 使用 nm 工具检查符号。

使用 nm 工具检查目标文件和库文件中的符号，确保符号定义存在。

可使用sdk中内置的nm工具：sdk/default/openharmony/native/llvm/bin/llvm-nm。

**检查目标文件**

```
1. nm myLibrary.o | grep myFunction
```

**检查三方库文件**

```
1. nm /path/to/external/library | grep myFunction
```

**结论**

通过上述步骤，您可以定位和解决 error: undefined symbol 问题。在使用 CMake、Ninja 和 LLVM 编译 C++ 项目时，确保所有源文件和库文件正确包含在项目中，并正确配置编译和链接选项是关键。如果问题依旧存在，详细的编译和链接输出日志通常能提供更多线索，帮助您找到具体的原因。

## CPP编译报错"A 'unknown type name' error has occurred"

**问题现象**

在编译HarmonyOS C++ 项目时，报错提示"A 'unknown type name' error has occurred"。

**解决措施**

在编译HarmonyOS C++ 项目时，遇到"unknown type name"错误通常表示编译器无法识别某个类型。这可能是因为类型未定义、未包含相关的头文件，或者包含的头文件路径不正确。以下是定位和解决这个问题的步骤：

1. 检查是否包含头文件。

   确保所有必要的头文件都已正确包含在源文件中。例如，如果您正在使用某个自定义类型或库提供的类型，请确保在使用该类型的文件中包含了相关的头文件。

   **示例：**

   ```
   1. // main.cpp
   2. #include "myLibrary.h"
   3. int main() {
   4. MyType obj;
   5. // 使用自定义类型
   6. return 0;
   7. }

   9. // myLibrary.h
   10. #ifndef MY_LIBRARY_H
   11. #define MY_LIBRARY_H
   12. class MyType {
   13. public:
   14. MyType() {}
   15. void doSomething();
   16. };
   17. #endif
   ```
2. 检查头文件路径。

   确保 CMakeLists.txt 中正确设置了头文件的搜索路径。可以通过 include\_directories 添加头文件目录。

   **示例 CMakeLists.txt：**

   ```
   1. cmake_minimum_required(VERSION 3.10)
   2. project(MyProject)
   3. set(CMAKE_CXX_STANDARD 17)
   4. # 添加头文件目录
   5. include_directories(${CMAKE_SOURCE_DIR}/include)
   6. # 添加源文件
   7. add_library(myProgram SHARED src/main.cpp src/myLibrary.cpp)
   ```
3. 清理和重新生成构建文件。

   有时，构建文件可能会损坏或丢失符号定义。尝试清理构建目录并重新生成构建文件：

   ```
   1. hvigorw clean
   ```

   或手动删除模块下.cxx目录。
4. 启用详细编译输出。

   为了解详细的编译过程，可以启用更详细的输出。在 CMakeLists.txt 中添加以下内容：

   ```
   1. set(CMAKE_VERBOSE_MAKEFILE ON)
   ```
5. 检查编译输出日志。

   Ninja 默认生成 .ninja\_log 文件，其中包含构建过程的详细信息。你可以检查这个日志文件以了解构建过程中的问题。

   ```
   1. cat .cxx/default/default/arm64-v8a/.ninja_log
   ```
6. 使用 CMake 的 message 函数调试。

   可以在 CMakeLists.txt 文件中添加 message 函数来打印一些调试信息，以确保路径和变量正确设置。

   **示例：**

   ```
   1. message(STATUS "Source directory: ${CMAKE_SOURCE_DIR}")
   2. message(STATUS "Include directories: ${CMAKE_INCLUDE_PATH}")
   ```
7. 如果报错接口是系统API，请查阅对应API参考的起始版本，确认接口在当前版本是否可用。

**结论**

通过上述步骤，您可以定位和解决 unknown type name 问题。在使用 CMake、Ninja 和 LLVM 编译 C++ 项目时，确保所有头文件正确包含并设置正确的头文件路径是关键。如果问题依旧存在，详细的编译输出日志通常能提供更多线索，帮助您找到具体的原因。

## JDK版本不匹配导致编译失败

**问题现象**

通过命令行方式构建HarmonyOS应用或元服务过程中出现构建失败，现象如下图所示。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/af/v3/140GEYnXR0ugFCOK-bWOpQ/zh-cn_image_0000002602066533.png?HW-CC-KV=V1&HW-CC-Date=20260611T073108Z&HW-CC-Expire=86400&HW-CC-Sign=2EC2164E45DD8F677CD68348A4712B0F6A4EEAF87D8D450FFB3341D4D92F912A)

**解决措施**

该问题是由于JDK版本不匹配导致，当前配套的版本为JDK 17。因此，请根据如下方法进行修正：

1. 下载并安装JDK 17版本。
2. 修改JAVA\_HOME环境变量，取值修改为JDK 17。如果是Linux系统，可参考使用命令行方式构建元服务或应用的[配置JDK章节](../../../命令行工具/搭建流水线/ide-command-line-building-app.md#section195447475220)。

## LABEL\_VALUE\_ERROR处理指导

**问题现象**

在工程同步、编译构建过程中，提示**LABEL\_VALUE\_ERROR**错误信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a8/v3/iWtb3n0sQyyNyOOGUcFSYA/zh-cn_image_0000002602186609.png?HW-CC-KV=V1&HW-CC-Date=20260611T073108Z&HW-CC-Expire=86400&HW-CC-Sign=14C0805F60A02D2270E5254F5E18CD120BB65AECA449CD59DFE2BCA778060C6C)

**解决措施**

该问题是由于config.json文件的资源引用规则变更导致，需要将“label”字段的取值，修改为资源引用方式。

1. 在**resources > base > element**中的string.json中添加对应的字符串信息。
2. 然后在config.json中重新引用该字符串资源。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e8/v3/ROnw4gLyTWOTeOYuJrnVSw/zh-cn_image_0000002571547066.png?HW-CC-KV=V1&HW-CC-Date=20260611T073108Z&HW-CC-Expire=86400&HW-CC-Sign=69700AA49227268F0287AFC1C3BFE5868A139EFC37EFD60D6357131403D3790D)

## 应用/元服务的启动界面信息缺失，提示"Schema validate failed"报错

**问题现象**

在工程同步或者编译构建时出现错误，提示“Schema validate failed”。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dd/v3/tAN0qUgHQbaohib_-ujG0w/zh-cn_image_0000002571387326.png?HW-CC-KV=V1&HW-CC-Date=20260611T073108Z&HW-CC-Expire=86400&HW-CC-Sign=31A1E0CAB0813E34A977D301D5E7AE004DF59620508E5CA7DF91BF3D32D2BE1D)

**解决措施**

在开发应用/元服务时，可以设置应用/元服务的启动界面的图标及背景颜色，创建工程后自动设置了默认的启动界面信息，但若开发者误删其中某个字段后将导致报错。下面以重新设置启动界面信息为例，开发者可自定义启动界面的图标及背景颜色。

在开发应用/元服务时，为了提升应用/元服务冷启动的性能，您可以通过如下方式设置应用/元服务的启动界面的图标及背景颜色。

1. 在模块下的**resources > base > element**下，点击右键选择**New > Element Resource File**创建资源文件。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6c/v3/et5OatwCToaNKi4b1H8JJQ/zh-cn_image_0000002602066431.png?HW-CC-KV=V1&HW-CC-Date=20260611T073108Z&HW-CC-Expire=86400&HW-CC-Sign=8C7D910FED33C739059DB4CF393D5251852DC67FDCA87719C550151F6187B923)
2. 在弹出的对话框中，“File name”开发者可自定义，如color；“Root element”请选择**color。**

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/52/v3/JgLl0R4qSCmeXg7y7qlDLw/zh-cn_image_0000002602066489.png?HW-CC-KV=V1&HW-CC-Date=20260611T073108Z&HW-CC-Expire=86400&HW-CC-Sign=D7284B7C679006BD718D7AAE176B7F0D1932E5475B7675E297FF23C19FA4B80E)

   创建完成后，color.json文件如下图所示：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f5/v3/ZWrDih0LQ3OmLVR94YqrSg/zh-cn_image_0000002571387328.png?HW-CC-KV=V1&HW-CC-Date=20260611T073108Z&HW-CC-Expire=86400&HW-CC-Sign=64E60280996382EA55B81ED0DAE35E2317C7ED4DB11A8459BCD7FF39FEE43A24)
3. 将[2](ide-hvigor-faqs.md#li124901748185712)创建的color.json文件拷贝至模块的**ohosTest > resources > base > element**目录下。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/eb/v3/a9qvPNcYR3SzjCG3WmgxQw/zh-cn_image_0000002602066481.png?HW-CC-KV=V1&HW-CC-Date=20260611T073108Z&HW-CC-Expire=86400&HW-CC-Sign=25DD7E5494A7F1079AE577DAFAB7BEA24496E34BF886AF65DB3AB6BE37F6092A)
4. 在模块的**src > main > module.json5**文件的abilities数组中，添加startWindowIcon和startWindowBackground字段（若缺少任一字段，将出现ERROR: Schema validate failed报错）。其中，startWindowIcon字段索引模块下**resources > base > media**中的图标资源，startWindowBackground字段索引**resources > base > element** **> color.json**中的color。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7e/v3/Stpu9xCTSdKeJx89R-bdvg/zh-cn_image_0000002571547068.png?HW-CC-KV=V1&HW-CC-Date=20260611T073108Z&HW-CC-Expire=86400&HW-CC-Sign=7FE38809521D984C458B267F22B1A94E00723A436417FF56AF2B42632A2AB6FD)
5. 在**src > ohosTest > module.json5**文件的abilities数组中，加startWindowIcon和startWindowBackground字段。其中，startWindowIcon字段索引模块ohosTest下**resources > base > media**中的图标资源， startWindowBackground字段索引**resources > base > element** **> color.json**中的color。

## 编译报错“Schema validate failed”

**问题现象**

DevEco Studio编译时出现错误，提示“Schema validate failed”错误信息。

**解决措施**

出现该问题的原因是配置文件中字段缺失或拼写错误，可根据报错的详细信息进行问题定位。

如将module.json5文件中abilities标签中的“name”错写为“nam”，报错信息如下：

```
1. Detail: Please check the following fields.
2. {
3. instancePath: 'module.abilities[0]',
4. keyword: 'required',
5. params: { missingProperty: 'name' },
6. message: "must have required property 'name'",
7. location: 'D:/MyApplication/entry/src/main/module.json5:15:8'
8. }
9. {
10. instancePath: 'module.abilities[0]',
11. keyword: 'required',
12. params: { missingProperty: 'srcEntrance' },
13. message: "must have required property 'srcEntrance'",
14. location: 'D:/MyApplication/entry/src/main/module.json5:15:8'
15. }
16. {
17. instancePath: 'module.abilities[0]',
18. keyword: 'required',
19. params: { missingProperty: 'name' },
20. message: "must have required property 'name'",
21. location: 'D:/MyApplication/entry/src/main/module.json5:15:8'
22. }
23. {
24. instancePath: 'module.abilities[0]',
25. keyword: 'oneOf',
26. params: { passingSchemas: null },
27. message: 'must match exactly one schema in oneOf',
28. location: 'D:/MyApplication/entry/src/main/module.json5:15:8'
29. }
30. {
31. instancePath: 'module.abilities[0]',
32. keyword: 'enum',
33. params: {
34. allowedValues: [
35. 'priority',
36. 'name',
37. 'srcEntrance',
38. 'srcEntry',
39. 'launchType',
40. 'description',
41. 'icon',
42. 'label',
43. 'permissions',
44. 'metadata',
45. 'visible',
46. 'exported',
47. 'skills',
48. 'backgroundModes',
49. 'continuable',
50. 'startWindowIcon',
51. 'startWindowBackground',
52. 'removeMissionAfterTerminate',
53. 'orientation',
54. 'supportWindowMode',
55. 'maxWindowRatio',
56. 'minWindowRatio',
57. 'maxWindowWidth',
58. 'minWindowWidth',
59. 'maxWindowHeight',
60. 'minWindowHeight',
61. 'excludeFromMissions'
62. ]
63. },
64. message: 'must be equal to one of the allowed values',
65. location: 'D:/MyApplication/entry/src/main/module.json5:15:8'
66. }
67. {
68. instancePath: 'module.abilities[0]',
69. keyword: 'propertyNames',
70. params: { propertyName: 'nam' },
71. message: 'property name must be valid',
72. location: 'D:/MyApplication/entry/src/main/module.json5:15:8'
73. }
```

以上述报错为例，说明报错中关键词的含义，便于开发者理解报错信息，完成问题定位及修改。

* instancePath：错误所在的文件位置。'module.abilities[0]'表示在module.json5文件中的第一个abilities。
* keyword：标识当前报错字段的可选配属性，当前报错中包括'required'、'oneOf'、'enum'、'propertyNames'。
  + required：表示该字段为必选配置项。由于缺失或拼写错误导致该属性未配置。
  + oneOf：表示当前配置不符合oneOf要求。通过instancePath已经确认报错出现在abilities标签，在DevEco Studio中，按住Ctrl点击"abilities"跳转到对应的module.json文件，可以查看到必须配置以下两组中的一组。根据对比排查，可识别到因拼写错误导致"name"属性未配置。

    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4c/v3/_mgSbP8yQN6bGqfYExVF-g/zh-cn_image_0000002602066523.png?HW-CC-KV=V1&HW-CC-Date=20260611T073108Z&HW-CC-Expire=86400&HW-CC-Sign=80C7CCC88F2930D0CD3983D2FD1C93970DCCC9281344EB236985F8BCB1B09BBC)
  + enum：该标签内所有可配置的属性。开发者可根据枚举值确认属性的正确写法。
  + propertyNames：如果字段拼写错误将出现propertyNames，propertyName: 'nam'指明“nam”为错误属性。
* params：不同keyword对应不同的详细说明，如keyword为'required'时，params的missingProperty: 'name' 表示缺失的属性为“name”。
* message：修改要求的说明，如keyword为'required'时，message表示必须配置name属性。
* location：错误的具体位置，点击可以跳转。

## 编译报错“No available entry module found”

**问题现象**

DevEco Studio编译时出现错误，提示“No available entry module found”错误信息。

**解决措施**

feature模块中需要配置依赖的entry模块，DevEco Studio在编译时会校验feature模块所依赖的entry模块是否存在，出现该问题的原因可能为以下情况：

1. 在feature模块的build-profile.json5文件中，entryModules字段配置的名称与实际entry模块的名称不一致。请将entryModules字段的值修改为entry模块的名称；
2. 在项目级build-profile.json5文件的modules字段中，feature模块位于entry模块之前。由于DevEco Studio在进行编译时会按照从前往后的顺序进行配置，当配置feature模块时，尚未读取和配置entry模块，则会报entry模块不存在的错误。请在modules字段中将feature模块置于所依赖的entry模块之后。

## 编译报错“keystore password was incorrect”

**问题现象**

DevEco Studio编译时出现错误，提示“keystore password was incorrect”错误信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5c/v3/mobXBhj4RJiAeCwxkh-8DA/zh-cn_image_0000002571546956.png?HW-CC-KV=V1&HW-CC-Date=20260611T073108Z&HW-CC-Expire=86400&HW-CC-Sign=B891192D2D650E96A34EEEF8CF87D20708821F523A2D22B6767017EB033ED8DA)

**报错原因**

密钥库(p12)密码错误。

注意

**密钥库密码**和**密钥密码**是在创建p12文件时由开发者自行输入的，请牢记该密码。DevEco Studio工程的build-profile.json5文件中有记录密码的密文，但签名工具需要输入密码明文，不能直接将build-profile.json5中的值用到签名工具中。

**常见场景**

1. 密码输入错误。
2. 命令行中需要输入真实密码，误输入了加密后的密码。
3. 密钥(keyAlias)密码和密钥库(p12)密码记混。

**解决措施**

出现该问题的原因是签名文件中签名密码错误。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/75/v3/w0AJz_6KQA6-FJVRKEfiRg/zh-cn_image_0000002602066467.png?HW-CC-KV=V1&HW-CC-Date=20260611T073108Z&HW-CC-Expire=86400&HW-CC-Sign=FB083084A9A2E4C6E94060018EEEEDA296C55CCE0A03CB7318744C52C8AEBC35)

开发者可通过重新自动签名解决该问题：

1. 点击**File > Project Structure > Project > Signing Configs**，打开签名配置页面。

2. 勾选“Automatically generate signature”，等待重新签名，然后点击**OK**即可。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ac/v3/ejrXQw0UQZm0WThxLaCNjg/zh-cn_image_0000002571387384.png?HW-CC-KV=V1&HW-CC-Date=20260611T073108Z&HW-CC-Expire=86400&HW-CC-Sign=20F875BB1D23E02B8489B26BCFB2884EFDB189B510E480DC953052632E1FE9E1)

## 编译报错“please check deviceType or distroFilter of the module”

**问题现象**

DevEco Studio编译时出现错误，出现如下提示之一：

* Module: (xxx) and Module: (xxx) are entry, please check deviceType or distroFilter of the module.

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3d/v3/Dkx3DsICTzyFv9Ea0tTdkw/zh-cn_image_0000002602066537.png?HW-CC-KV=V1&HW-CC-Date=20260611T073108Z&HW-CC-Expire=86400&HW-CC-Sign=B34318F0D4EA4C4263EC53FF7A43569108D9EC8E30FF7FB949389FE6F5DD661C)
* Module: (xxx) and Module: (xxx) have the same moduleName, please check deviceType or distroFilter of the module.

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ef/v3/takOPDbkThyxaLnazIZZ6w/zh-cn_image_0000002571387394.png?HW-CC-KV=V1&HW-CC-Date=20260611T073108Z&HW-CC-Expire=86400&HW-CC-Sign=217B5046BDB3B7FAB55D67B2883B0EDD87CD0552F4E3C64F7D516CF82E37A501)
* Module: (xxx) and Module: (xxx) have the same packageName, please check deviceType or distroFilter of the module.

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d5/v3/4Dmm60_aRHe2tl67yjQvjA/zh-cn_image_0000002602186575.png?HW-CC-KV=V1&HW-CC-Date=20260611T073108Z&HW-CC-Expire=86400&HW-CC-Sign=5C7336263301C1EF6E849E5E7E3CF0CF1B8839AF923DB07DE47D207F4B6DD04C)
* Module: (xxx) and Module: (xxx) have the same ability name.

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/78/v3/mZPtqmkuRLufQzHWlAEcvA/zh-cn_image_0000002602066453.png?HW-CC-KV=V1&HW-CC-Date=20260611T073108Z&HW-CC-Expire=86400&HW-CC-Sign=8EFB801B005CD68C8FB803E3E6B80B34DCB4ECDBF400C9B9CE5DE725BED201CF)

**解决措施**

出现该问题的原因是打包时工程未满足HAP唯一性校验逻辑，请根据[HAP唯一性校验逻辑](../../配置构建流程/HAP唯一性校验逻辑/ide-hvigor-verification-rule.md)修改工程，满足校验逻辑即可正常打包。

## 编译报错“Failed to generate test project build system”

**问题现象**

执行多模块native模块构建时，提示“Failed to generate test project build system.”错误信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f6/v3/tB8XALNGR02cowYeYx0ujg/zh-cn_image_0000002571387410.png?HW-CC-KV=V1&HW-CC-Date=20260611T073108Z&HW-CC-Expire=86400&HW-CC-Sign=0B2A5D77476303DB5D837B716F4E9FA9E4EEA633E9BDF3D0E0CFACA395F8AA1D)

**解决措施**

请删除报错模块下的.cxx文件夹，然后选中需要构建的模块，执行**Make Module** **${moduleName}**完成单独构建，避免同时构建多个模块。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4f/v3/riPkAELZROeaVNnzQrUz_g/zh-cn_image_0000002571387348.png?HW-CC-KV=V1&HW-CC-Date=20260611T073108Z&HW-CC-Expire=86400&HW-CC-Sign=437FC6DDEF03AEC573B65EA42D8B70694DBBD154AE041727000E0858E7735626)

## C/C++项目三方依赖库未打包入HAP

**问题现象**

C/C++项目依赖三方so时，在打包生成HAP后，发现三方so未打包到HAP中。

**解决措施**

当前DevEco Studio对C/C++项目三方so的寻址方式有限，如出现三方so未打包到HAP中，请尝试修改so引入方式。

1. 定义一个别名（如jsbind\_shared\_lib\_tracing），代表将要引入的三方so。
2. 使用SHARED IMPORT将三方so定义为动态引入。
3. 使用IMPORTED\_LOCATION定义引入so的具体位置。
4. 将定义的三方so声明给目标。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/61/v3/igtAO2ToRq-1lvm4HLRLqw/zh-cn_image_0000002602066485.png?HW-CC-KV=V1&HW-CC-Date=20260611T073108Z&HW-CC-Expire=86400&HW-CC-Sign=67369768E8238AB5FCC61C9AC29E1F52FAD2119D75E4F3708165375FA577D4BC)
5. 再次打包生成HAP，确认三方so是否打包到HAP中。

## Static Library模块中src/main/cpp目录下的文件未打包进HAR

**问题现象**

点击**Build > Make Module ${libraryName}**编译构建生成HAR后，发现构建产物中未出现cpp目录下的文件。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5/v3/gK_MQrPdSg6ItyLzx7HbvA/zh-cn_image_0000002571547054.png?HW-CC-KV=V1&HW-CC-Date=20260611T073108Z&HW-CC-Expire=86400&HW-CC-Sign=CDD42EAF06093AE3EBF29F52A0EB9FDCB32B4C9BEA7398F09AD93C3E736D587E)

**解决措施**

如果使用的Hvigor为2.5.0-s及以上版本，在编译构建HAR的过程中，只会将dependencies内处于本模块路径下的本地依赖也打包进.har文件中，devDependencies里的依赖不会打包进.har文件中。

请将相应的本地依赖移至dependencies中后重新编译。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0/v3/dyJbTlDQQpCLybWBY1cfjA/zh-cn_image_0000002602066479.png?HW-CC-KV=V1&HW-CC-Date=20260611T073108Z&HW-CC-Expire=86400&HW-CC-Sign=478B222B827D128B7B5F793D4CC749FE779AF87F1A8C1E9F37E9A3A1AB8E0C6F)

## 工程编译告警提示“ArkTS:WARN: For details about ArkTS syntax errors”

**问题现象**

工程构建时，提示“ArkTS:WARN: For details about ArkTS syntax errors, see FAQs”。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f6/v3/vO42VsMfSF-8Ie_S5uT9kA/zh-cn_image_0000002571387392.png?HW-CC-KV=V1&HW-CC-Date=20260611T073108Z&HW-CC-Expire=86400&HW-CC-Sign=27EC7E02D7DEB288C48840AE6BB6CC08B4AB8FB857DA20FDF91DB4A8DC3AF884)

**解决措施**

出现该告警说明当前工程存在不符合ArkTS语法规范的写法，请根据ERROR报错中括号内的语法规则如(arkts-no-var)，查看[从TypeScript到ArkTS的适配规则](../../../基础入门/学习ArkTS语言/从TypeScript到ArkTS的适配指导/从TypeScript到ArkTS的适配规则/typescript-to-arkts-migration-guide.md#使用let而非var)中对应的说明，修改为ArkTS规范写法。

## 编译报错“ninja: error: mkdir(xxx): No such file or directory”

**问题现象**

Native工程编译报错，同时出现以下告警和报错信息。

出现工程目录长度超过250字符的告警，示例如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/da/v3/2QzBfZ6NRPyqHs8uWdvH-w/zh-cn_image_0000002602186581.png?HW-CC-KV=V1&HW-CC-Date=20260611T073108Z&HW-CC-Expire=86400&HW-CC-Sign=A7E156F20F13BDF0CC0BC9BE926604322714CDD0620D6D14AE9C4DCAE3EC25CF "点击放大")

出现编译报错“ninja: error: mkdir(xxx): No such file or directory”，示例如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8e/v3/NAsrueCUS5KRi6Yx4hXZbQ/zh-cn_image_0000002571547032.png?HW-CC-KV=V1&HW-CC-Date=20260611T073108Z&HW-CC-Expire=86400&HW-CC-Sign=407A094686D5ECF99CB14C10A9CE5CA32627A3DEBBE2FDA02172996D447CE7C9 "点击放大")

**解决措施**

CMAKE\_OBJECT\_PATH\_MAX默认大小为250，如果工程中object file实际路径长度超出该大小，将导致编译报错。

开发者需要根据object file实际路径长度在工程CMakeLists.txt中设置CMAKE\_OBJECT\_PATH\_MAX大小，具体方法如下：

* 方法一： 通常在CMAKE\_OBJECT\_PATH\_MAX默认值基础上增加一个文件名长度即可。

  示例中告警文件为TextMeasureCache.cpp.obj，长度为24字符，在默认值250的基础上增加24，即设置set(CMAKE\_OBJECT\_PATH\_MAX 274)
* 方法二：根据object file实际路径长度计算CMAKE\_OBJECT\_PATH\_MAX大小。

  计算公式：CMAKE\_OBJECT\_PATH\_MAX = 总路径长度 - object file中目录部分长度 + cmake哈希值字符数（固定为32）

  + 总路径长度 = object file directory长度 + object file长度，object file directory、object file如下图所示，两个长度之和为297字符，以实际为准

    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2/v3/nRO_-y15T1aoI_1meKdpRA/zh-cn_image_0000002571387356.png?HW-CC-KV=V1&HW-CC-Date=20260611T073108Z&HW-CC-Expire=86400&HW-CC-Sign=81F8382CEE6B6CCA73BA8DDC7E8855E814E172D3E83BB7FD98747975B5C1EF35 "点击放大")
  + object file中目录部分长度：示例中“\_\_/\_\_/\_\_/\_\_/\_\_/third-party/rn/ReactCommon/react/renderer/textlayoutmanager”长度为74字符，以实际为准
  + cmake哈希值字符数：cmake将长路径转换为哈希值时哈希值的长度，固定为32

  代入示例中的长度后，计算可得：CMAKE\_OBJECT\_PATH\_MAX = 297 - 74 + 32 = 255，即设置set(CMAKE\_OBJECT\_PATH\_MAX 255)

## 编译报错“(is the command line too long?)”

**问题现象**

Native工程编译报错，同时出现以下告警和报错信息。

出现工程目录长度超过250字符的告警，示例如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/91/v3/WpPWTHrMQmWhk9kXXQWYxw/zh-cn_image_0000002602186563.png?HW-CC-KV=V1&HW-CC-Date=20260611T073108Z&HW-CC-Expire=86400&HW-CC-Sign=2C89400F6D770BF2B674DFA26815286A7F89C63D7B73E218C9027522A6B09FDF "点击放大")

出现编译报错“(is the command line too long?)”，示例如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ed/v3/7QwskmQWRjeEPK9eMjMsJw/zh-cn_image_0000002571387412.png?HW-CC-KV=V1&HW-CC-Date=20260611T073108Z&HW-CC-Expire=86400&HW-CC-Sign=01778E33B5D54EC720E9E8B8055F48A085BC419A06439AEEA0BF40211BC0272C)

**解决措施**

CMAKE\_OBJECT\_PATH\_MAX默认大小为250，如果工程中object file实际路径长度超出该大小，将导致编译报错。

开发者需要根据object file实际路径长度在工程CMakeLists.txt中设置CMAKE\_OBJECT\_PATH\_MAX大小，具体方法如下：

* 方法一： 通常在CMAKE\_OBJECT\_PATH\_MAX默认值基础上增加一个文件名长度即可。

  示例中告警文件为TextMeasureCache.cpp.obj，长度为24字符，在默认值250的基础上增加24，即设置set(CMAKE\_OBJECT\_PATH\_MAX 274)
* 方法二：根据object file实际路径长度计算CMAKE\_OBJECT\_PATH\_MAX大小。

  计算公式：CMAKE\_OBJECT\_PATH\_MAX = 总路径长度 - object file中目录部分长度 + cmake哈希值字符数（固定为32）

  + 总路径长度 = object file directory长度 + object file长度，object file directory、object file如下图所示，两个长度之和为297字符，以实际为准

    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e0/v3/bPv2BMc6QNuI96lk9uSfuQ/zh-cn_image_0000002571387398.png?HW-CC-KV=V1&HW-CC-Date=20260611T073108Z&HW-CC-Expire=86400&HW-CC-Sign=A90365EFDC05D290A636A0F3EC53D71046E608B140C74AB9FCD0DBD73FB840B7 "点击放大")
  + object file中目录部分长度：示例中“\_\_/\_\_/\_\_/\_\_/\_\_/third-party/rn/ReactCommon/react/renderer/textlayoutmanager”长度为74字符，以实际为准
  + cmake哈希值字符数：cmake将长路径转换为哈希值时哈希值的长度，固定为32

  代入示例中的长度后，计算可得：CMAKE\_OBJECT\_PATH\_MAX = 297 - 74 + 32 = 255，即设置set(CMAKE\_OBJECT\_PATH\_MAX 255)
* 方法三：若设置CMAKE\_OBJECT\_PATH\_MAX后，仍然报相同错误，需要修改工程存放目录，将其存放在较短的目录下。

  设置CMAKE\_OBJECT\_PATH\_MAX后，cmake会将长路径转换为32字符的哈希值以缩短路径长度，如果转换后的路径依然过长，只能缩短工程的存放路径。

## 编译报错“CMake Error: The following variables are used in this project, but they are set to NOTFOUND”

**问题现象**

Native工程中使用find\_path时出现以下报错信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1b/v3/_9YhCCP9TIuy4yCcA2smQQ/zh-cn_image_0000002571387324.png?HW-CC-KV=V1&HW-CC-Date=20260611T073108Z&HW-CC-Expire=86400&HW-CC-Sign=CD137F6A0E68D2F11A0129E6F7263A13D43C1A9EC979B2F53CE81A774D1AF7BA "点击放大")

**解决措施**

OpenHarmony SDK提供的CMake交叉编译配置文件（ohos.toolchain.cmake）中，限制了搜索路径为CMAKE\_SYSROOT。

如果开发者需要添加搜索路径，可在CMakeLists.txt中使用list接口添加自定义路径，如将"D:demo"添加至搜索路径：

```
1. list(APPEND CMAKE_FIND_ROOT_PATH_MODE_INCLUDE "D:demo")
```

添加后，即可使用find\_path查找"D:demo"目录下的文件。

## 编译报错 “Unknown resource name”

* 场景一

**问题现象**

工程中模块A引用了模块B，编译模块A时出现错误，提示 "Unknown resource name 'xxxx'"，找不到模块B的资源。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c/v3/2hJrfhmkS9-WaCwSitmrqA/zh-cn_image_0000002571387440.png?HW-CC-KV=V1&HW-CC-Date=20260611T073108Z&HW-CC-Expire=86400&HW-CC-Sign=52897438BA1E204639C7AD85E175A270A8877F136C43661650C7B41526544FDF "点击放大")

**解决措施**

请确保符合以下条件：

1. 资源需放置在目录resource/base路径下。
2. 模块B已安装。
3. 模块A中不能使用相对路径引用模块B的资源，应直接通过定义的模块名称来引用。

* 场景二

**问题现象**

引用模块的方式不对，如果引用的是一个其他模块的代码，也会报资源找不到。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7/v3/cduT3jWETyGAuRM_H6k--Q/zh-cn_image_0000002571547018.png?HW-CC-KV=V1&HW-CC-Date=20260611T073108Z&HW-CC-Expire=86400&HW-CC-Sign=437F753DB8CC832BD42BCADE0B801829141B7FA54F6E9146F746B5677F84CDD5)![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/41/v3/iGWrYQ2xSc2axyMset6W-A/zh-cn_image_0000002571546982.png?HW-CC-KV=V1&HW-CC-Date=20260611T073108Z&HW-CC-Expire=86400&HW-CC-Sign=0D9B7930F8946C939C9C662DB498194FF603A6CEA446398F4C66DBF7A30984FE)

**解决措施**

在oh\_package.json5中引入该模块。通过定义的模块名称来引用。

如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/12/v3/46P216TNSI23Fq9c4xv8zw/zh-cn_image_0000002571546968.png?HW-CC-KV=V1&HW-CC-Date=20260611T073108Z&HW-CC-Expire=86400&HW-CC-Sign=1CAA86F7093A59BC9EAA9517B3ABF695B14BB9630AAF406B8154713010D0EC0C)

* 场景三

**问题现象**

HSP A 申请了某个权限，这个权限进行了资源的引用，在所有依赖A的组件进行构建时，报错 A 引用的资源找不到。

**解决措施**

手动在引用方配置对应资源可以解决此问题。

## 构建报错“Task xxx was not found in the project xxx”

**问题现象**

命令行手动执行构建命令时，构建失败，提示“Task xxx was not found in the project xxx”

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3d/v3/VsFwvPJWT9qhQkcY1WGn8g/zh-cn_image_0000002602066493.png?HW-CC-KV=V1&HW-CC-Date=20260611T073108Z&HW-CC-Expire=86400&HW-CC-Sign=8F7A304B2CDB8C532EC2F198152A1B6E12AC043FC80C475C9D186909482B5847)**问题确认**

1. 执行hvigorw tasks命令，查看对应命令是否存在。
2. 查看对应工程中module.json5文件中“type”字段是否为命令执行模块。比如图中执行assembleHar命令，是对工程中的har模块进行打包，若module.json5文件中的“type”字段不是"har"类型，则会出现上述错误提示。

**解决措施**

1. 执行正确命令。
2. 查看对应工程中module.json5文件中“type”字段类型，执行对应命令。

## 编译报错“The reason and usedScene attributes are mandatory for user\_grant permissions”

**问题现象**

DevEco Studio编译失败，提示“The reason and usedScene attributes are mandatory for user\_grant permissions”。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/31/v3/gewXxJp_QmG_jgU-_Z6zHQ/zh-cn_image_0000002571547064.png?HW-CC-KV=V1&HW-CC-Date=20260611T073108Z&HW-CC-Expire=86400&HW-CC-Sign=172A6FA5D420C4B0CF3EDAEE15BD53B79D68322CE1D710F8F8C624A4D52115AF "点击放大")

**问题原因**

从DevEco Studio NEXT Developer Preview2版本开始新增规则：APP包中，所有entry和feature hap的module下的requestPermissions权限清单必须指定(可以缺省为空，若非空则name必填,user\_grant权限则必填reason、usedScene字段)。

**解决措施**

进入对应module.json5文件中，补齐requestPermissions字段下的reason和usedScene字段。如以下示例：

```
1. "requestPermissions": [
2. {
3. "name": "ohos.permission.READ_IMAGEVIDEO",
4. "reason": "$string:module_desc",
5. "usedScene": {
6. "abilities": [
7. "EntryAbility"
8. ],
9. "when": "inuse"
10. }
11. }
12. ]
```

## 编译报错“Only one default card can be configured in the form\_config.json file”

**问题现象**

DevEco Studio编译失败，提示“Only one default card can be configured in the form\_config.json file”。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3e/v3/6xLZ-HYyTtOuQYQ2yXUtqw/zh-cn_image_0000002571387382.png?HW-CC-KV=V1&HW-CC-Date=20260611T073108Z&HW-CC-Expire=86400&HW-CC-Sign=EFCF7664DA4BC0E021980448BEAB7D071F6A4C41F658A1D2D3EDD8E96C6134C9 "点击放大")

**问题原因**

从DevEco Studio NEXT Developer Preview2版本开始新增规则：卡片的配置文件中isDefault不可缺省，每个UIAbility有且只有一个默认卡片。

**解决措施**

进入对应module.json5文件中，选择唯一默认卡片，将其他卡片的isDefault字段设置为false。

## 编译报错“In the form\_config.json file, if the value of the updateEnabled field is true, the updateDuration and scheduleUpdateTime fields cannot be both empty”

**问题现象**

DevEco Studio编译失败，提示“In the form\_config.json file, if the value of the updateEnabled field is true, the updateDuration and scheduleUpdateTime fields cannot be both empty.”。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/71/v3/mY06Znk-S7CQsg6MvSphJA/zh-cn_image_0000002602186525.png?HW-CC-KV=V1&HW-CC-Date=20260611T073108Z&HW-CC-Expire=86400&HW-CC-Sign=4BD77634D58538F2326FEEA08AF9A81E3ED714698E40F503CBAE7F17B0E3DFAB "点击放大")

**问题原因**

从DevEco Studio NEXT Developer Preview2版本开始新增规则：卡片的配置文件中updateEnabled不可缺省，为true时可以在定时刷新（updateDuration）和定点刷新（scheduledUpdateTime）两种方式任选其一，当两者同时配置时，定时刷新优先生效。

**解决措施**

进入对应module.json5文件中，按照需求，选择配置updateEnabled为false，或者增加定时刷新（updateDuration）和定点刷新（scheduledUpdateTime）两种方式配置。

## 编译报错“The path XX is not writable. please choose a new location”

**问题现象**

在mac上，通过直接打开dmg中的DevEco Studio，构建报错 The path XX is not writable. please choose a new location.”。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/78/v3/Q6ncS6pQTISsKYTkIG3XDA/zh-cn_image_0000002571387420.png?HW-CC-KV=V1&HW-CC-Date=20260611T073108Z&HW-CC-Expire=86400&HW-CC-Sign=166BAE9EDD72E185F7296BD102313B636D78ABF9A3188DA672FEBB3BE9A3DB1B)

**问题原因**

在mac上直接打开dmg 中的DevEco Studio，是会以只读的方式打开的，内置到DevEco Studio里面的文件是没有写权限的。

**解决措施**

将“DevEco-Studio.app”拖拽到“Applications”中，先安装再使用。

## 编译报错“Property 'XX' does not exist on type 'typeof BuildProfile'”

**问题现象**

本地HSP模块对外提供的接口中使用了HAP未定义的自定义参数BuildProfileFileds，且HAP引用了HSP中的该接口，导致编译失败，提示“Property 'XX' does not exist on type 'typeof BuildProfile'”。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5/v3/LrIjVEkcQS68fhlvnFIHAQ/zh-cn_image_0000002571387406.png?HW-CC-KV=V1&HW-CC-Date=20260611T073108Z&HW-CC-Expire=86400&HW-CC-Sign=36007278B4DD13A15DF46A46EB95C74D2DD4AA05B1513E5F5919FD6DC8D8C47E)

**解决措施**

可采用以下两种方式解决该问题：

* 在HAP中配置与HSP相同的自定义参数BuildProfileFileds。
* 将与HSP相同的自定义参数BuildProfileFields配置到工程级build-profile.json5中，该方法会使HSP中的自定义参数在全局生效。

## 编译报错“The useNormalizedOHMUrl settings of packages xxx and the project useNormalizedOHMUrl: xxx do not match”

**问题现象**

编译报错“The useNormalizedOHMUrl settings of packages xxx and the project useNormalizedOHMUrl: xxx do not match”。

**解决措施**

[useNormalizedOHMUrl](../../配置文件/工程级build-profile.json5文件/ide-hvigor-build-profile-app.md#section13181758123312) 为true的时候ohmurl使用的是新的拼接和解析方式，不能和旧的ohmurl混用，会导致运行时无法识别。

可采用以下两种方式解决该问题：

* 将报错的依赖包的工程级build-profile.json5中的useNormalizedOHMUrl修改为与当前工程一致，重新生成依赖包并替换（useNormalizedOHMUrl缺省默认值为false）。

  ```
  1. {
  2. "app": {
  3. "products": [
  4. {
  5. "buildOption": {
  6. "strictMode": {
  7. "useNormalizedOHMUrl": true
  8. }
  9. }
  10. }
  11. ]
  12. }
  13. }
  ```
* 如果与工程不一致的依赖包较多，建议修改工程的工程级build-profile.json5中的useNormalizedOHMUrl值以及替换其它的不一致的依赖包。

如果修改了useNormalizedOHMUrl仍无法解决，表明当前hsp包是本地包，需要以本地hsp包的形式引入，请在工程下的build-profile.json5中的modules中添加报错hsp模块，示例如下：

```
1. "modules": [
2. {
3. name: "hsp",   // 引用的hsp包依赖
4. srcPath: "../MyApplication_stageB/hsp",   // 引用的hsp包的路径（绝对和相对都可以）
5. }
6. ]
```

## 如何配置oh-package.json5动态依赖

oh-package.json5文件中：

* dependencies（生产依赖）：声明需要在代码中import的三方库（参与编译/运行阶段使用的依赖）。
* devDependencies（开发依赖）：参与项目的开发或测试阶段。
* dynamicDependencies（动态依赖）：动态依赖的HSP模块。在开发者需要动态加载HSP的时候配置使用。

示例如下，详细内容可参考[oh-package.json5文件](../../../命令行工具/三方依赖管理工具（ohpm）/oh-package.json5/ide-oh-package-json5.md)和[添加依赖项](../../配置构建流程/添加依赖项/ide-hvigor-dependencies.md)。

```
1. {
2. "name": "parameter-test",
3. "version": "@param:version",
4. "description": "test desc.",
5. "main": "index.ets",
6. "author": "test author",
7. "license": "ISC",
8. "dependencies": {
9. "libtest1": "@param:dependencies.libtest1"
10. },
11. "devDependencies": {
12. "libtest2": "@param:devDependencies.libtest2"
13. },
14. "dynamicDependencies": {
15. "libtest3": "@param:dynamicDependencies.libtest3"
16. },
17. "parameterFile": '.parameterFile/parameterFile.json5' // 开启参数化并指定参数化配置文件路径
18. }
```

## 如何解决SDK与镜像不匹配导致abc文件无法正常运行的问题

**问题现象**

当SDK版本与镜像版本不匹配时，应用将会闪退，出现jscrash，同时hilog出现日志。

**解决措施**

现象根本原因是SDK工具与镜像版本不匹配。推荐使用匹配的SDK与镜像版本。

查看SDK版本方法：

在DevEco Studio安装路径下的sdk路径中，执行 {sdk.dir}/openharmony/ets/build-tools/ets-loader/bin/ark/build-win/bin/es2abc.exe --bc-version可查看SDK版本号。用于检验SDK与镜像版本是否匹配。

## 如何解决编译报错“Could not resolve 'xxx' from”，但'xxx'目录存在的问题

**问题现象**

编译报错：“Could not resolve 'xxx' from”，但'xxx'目录存在，目录下存在Index文件。

**问题原因**

在引用目录时，编译时自动拼接小写的index文件，而目录中是大写的Index文件，在编译大小写敏感时，找不到index文件，则报错。

**解决措施**

在引用'xxx'目录时，明确写明引用到'xxx/Index'文件。

## 用户目录下没有npmrc文件

**问题现象**

新建项目报错 Error: The hvigor depends on the npmrc file. Configure the npmrc file first。

**问题原因**

在用户目录下没有 .npmrc 文件。

**解决措施**

在用户目录下创建.npmrc文件，配置如下信息：

```
1. registry=https://repo.huaweicloud.com/repository/npm/
2. @ohos:registry=https://repo.harmonyos.com/npm/
```

## 如何解决编译报错“ Error: 'icon' value `$media:icons` invalid value.”的问题

**问题现象**

编译报错“ Error: 'icon' value `$media:icons` invalid value”。

```
1. ERROR: Failed :entry:default@CompileResource...
2. ERROR: Tools execution failed.
3. Error: ref `$media:icons` don`t be defined.
4. Error: 'icon' value `$media:icons` invalid value.
5. at D:\project\process_profile\default\module.json
6. Detail: Please check the message from tools.
```

**报错原因**

引用的资源不存在时，编译报错指向的文件路径是build目录。

**常见场景**

1. 资源文件未添加。
2. 资源文件被意外删除。

**解决方案**

根据报错的资源id全局搜索，查看报错的资源是否存在。

## 如何解决编译报错“Error: cJSON\_Parse failed, please check the JSON file.”的问题

**问题现象**

编译报错“Error: cJSON\_Parse failed, please check the JSON file”。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ad/v3/2cD1hXleR_ih6P-v0SF7Tw/zh-cn_image_0000002571387380.png?HW-CC-KV=V1&HW-CC-Date=20260611T073108Z&HW-CC-Expire=86400&HW-CC-Sign=7913E0742BD92292806A5984A9FB84F18D80522D2C349FAA37FFDBECB1D40A95 "点击放大")

**报错原因**

module.json文件格式不正确。

**常见场景**

1. json文件内末尾多了逗号。

2. 根标签不是大括号{}。

**解决方案**

检查报错指向的json文件格式，比如是否末尾多了逗号，根标签是否为大括号{}。

## 如何解决编译报错“Error: the name 'XXX' can only contain [a-zA-Z0-9\_].”的问题

**问题现象**

编译报错“Error: the name 'XXX' can only contain [a-zA-Z0-9\_]”。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e1/v3/Ysh91e7-Sm2B_aX1jaUK-g/zh-cn_image_0000002602186515.png?HW-CC-KV=V1&HW-CC-Date=20260611T073108Z&HW-CC-Expire=86400&HW-CC-Sign=9C3C7FE847050122BD618A339F4E269068F149E418EC11FF65BC451A4A648DF6)

**解决方案**

检查文件名是否合法，文件名只能包含大小写字母、数字、下划线。

## 如何解决三方包require语句报错

**问题现象**

当引入三方包时编译报错。

**报错原因**

部分三方包由npm迁移而来，其开发环境为node， 其中的require语法arkcompiler不完全支持，出现运行报错情况。

**场景1**：

```
1. // Module/src/test.json
2. {a: 1, b: 2}
3. //use.js
4. let test = require("Module/src/test.json")
```

**需修改为：**

```
1. // Module/src/test.js
2. module.exports = {a: 1, b: 2}
3. //use.js
4. let test = require("Module/src/test")
```

**场景2：**

```
1. // Module/package.json
2. ...
3. main: "./src"
4. ...
5. // use.js
6. let module = require("Module")
```

**需修改为：**

```
1. // Module/package.json
2. ...
3. main: "./src/index.js"
4. ...
5. // use.js
6. let module = require("Module")
```

**场景3：**

编译出现warning信息：

```
1. Plugin node-resolve: preferring built-in module 'util' over local alternative at '/Users/~/Documents/fe-module/demo/node_modules/util/util.js', pass 'preferBuiltins: false' to disable this behavior or 'preferBuiltins: true' to disable this warning
```

**解决方案**

修改rollup 配置文件，rollup.config.js中修改 preferBuiltins 字段：

```
1. plugins: [
2. resolve({
3. preferBuiltins: false,    // true 或 false
4. mainFields: ['module', 'main'],
5. extensions
6. })
7. ];
```

**场景4：**

```
1. import {Buffer} from 'buffer'
```

**需修改为：**

```
1. import {Buffer} from 'buffer/'
```

## 如何解决编译报错“Indexed access is not supported for fields(arkts-no-props-by-index)”的问题

**问题现象**

动态调用类或者接口的字段，导致编译报错出现：Indexed access is not supported for fields(arkts-no-props-by-index)。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d7/v3/TvFrQag5TWOGqka68CxxkA/zh-cn_image_0000002602186517.png?HW-CC-KV=V1&HW-CC-Date=20260611T073108Z&HW-CC-Expire=86400&HW-CC-Sign=38CF0FC78D2DBB68489D9E38A38C4F29727D9D70E84591ED5C366E7878BCD2B7)

**解决方案**

修改代码：

```
1. getValue(breakpoint: string): T {
2. return Reflect.get(this.options, breakpoint) as T;
3. }
```

## 04077396

**问题现象**

在不同的文件中声明相同变量或者interface、enum等类型，DevEco Studio不报错，但是编译报错。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/32/v3/KxIIxwKDQhKKTYoANxaGHw/zh-cn_image_0000002571387414.png?HW-CC-KV=V1&HW-CC-Date=20260611T073108Z&HW-CC-Expire=86400&HW-CC-Sign=BF91844EE2266761F2429FB219FFDEFB97E821A04638D26AE3A3A47062827308)

**解决方案**

如果文件中不包含export关键字，该文件将视作全局命名空间的一部分，相当于两个文件实质为同一个文件。请添加export关键字使其成为独立命名空间，或者将声明的内容添加到自定义的命名空间中。

## 如何解决编译报错“ The inferred type of 'xxx' cannot be named without a reference to 'xxx'. This is likely not portable. A type annotation is necessary**.**”的问题

**问题现象**

编译报错"The inferred type of 'xxx' cannot be named without a reference to 'xxx'. This is likely not portable. A type annotation is necessary"。

**问题原因**

HSP会生成.d.ts声明文件，由于原始文件中未注明类型，导致生成的.d.ts文件缺少类型注解。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/05/v3/tPKrlde8SSi9clAxHQyKuA/zh-cn_image_0000002571387340.png?HW-CC-KV=V1&HW-CC-Date=20260611T073108Z&HW-CC-Expire=86400&HW-CC-Sign=7D9E87B3FDEBA4C6E2DB456FB8D6B0BDA620B2E5E4B8366E1B7658C0DEFD3168 "点击放大")

**解决方案**

报错位置添加类型注解。

## 如何解决编译报错“ERROR: ArkTS Compiler Error ERROR: /bin/sh: "xxxx/es2abc": Operation not permitted”的问题

**问题现象**

编译报错“ERROR: ArkTS Compiler Error ERROR: /bin/sh: "xxxx/es2abc": Operation not permitted”。

**问题原因**

由于获取SDK的方式是从网络上下载，mac的安全设置会给可执行文件添加来源于网络的标识（com.apple.quarantine），导致无法执行。

**解决方案**

执行命令删除可执行文件的com.apple.quarantine标识。

```
1. xattr -d com.apple.quarantine /path/to/es2abc
```

## 如何解决编译报错“Cannot add xxxx items to index”的问题

**问题现象**

编译报错“Cannot add xxxx items to index”。

**问题原因**

被编译文件中某函数内部有大量object literal, array literal和string，导致item的数量超过了上限（65536）。

**解决方案**

排查相关文件，将存在上述原因的函数进行拆分。

## 编译初始化报错“resource busy or locked, open 'xxx\outputs\build-logs\build.log'”

**问题现象**

在升级DevEco Studio至5.0.3.403版本后，打开旧工程概率性报错：resource busy or locked, open 'xxx\outputs\build-logs\build.log'。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/71/v3/s_mWdHIVQF-j0fzZ97cF0Q/zh-cn_image_0000002602186487.png?HW-CC-KV=V1&HW-CC-Date=20260611T073108Z&HW-CC-Expire=86400&HW-CC-Sign=DBC1444176B5C60823FD03406F62BD96467F0C5ACB3A29768141645D732947B7)

**问题原因**

初始化时日志写入存在冲突，.hvigor目录中的build-log文件被占用导致了该报错。

**解决方案**

* 方法一：点击编辑器窗口上方的Sync Now。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/77/v3/3hrJIiPwS3GXNFldWdeb9Q/zh-cn_image_0000002571547022.png?HW-CC-KV=V1&HW-CC-Date=20260611T073108Z&HW-CC-Expire=86400&HW-CC-Sign=1DFCE72F09FE0B68E8A0E21FBC0128D8C80E8C134C65408C7F98900014D9A5BD)
* 方法二：点击工具栏**File > Sync and Refresh Project**。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/87/v3/l6cak_pdRzOZ-4Ftk8a1OA/zh-cn_image_0000002571547052.png?HW-CC-KV=V1&HW-CC-Date=20260611T073108Z&HW-CC-Expire=86400&HW-CC-Sign=2F0C0C05DF14F4A8E234DED163A82C74A9E663478BD4839D50261A009D08A806)
* 方法三：如果方法1、2无法解决问题，可以手动删除工程目录下的.hvigor目录后重启执行Sync。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/28/v3/axtTfbGOT164uFZhIF3x0A/zh-cn_image_0000002571387336.png?HW-CC-KV=V1&HW-CC-Date=20260611T073108Z&HW-CC-Expire=86400&HW-CC-Sign=178FACF8E74CDB41F6CF8AD9F4ED504B0AA0E1479FCC2F30CF66F35C1F4AFF98)

## Mac环境下加载动态库，签名拦截导致未生效

**问题现象**

Mac环境下，在DevEco项目开发时，build-profile.json5中添加了如下的插桩配置，但是插桩功能未生效。

```
1. "transformLib": "<相对模块根路径的动态库路径，以./开头>"
```

**判断与验证**

1. 进入sdk中es2abc所在目录：[DevEco-Studio安装目录]/Contents/sdk/default/openharmony/ets/build-tools/ets-loader/bin/ark/build-mac/bin。
2. 执行下列命令：

   ```
   1. ./es2abc --merge-abc --transform-lib <动态库路径> <测试js文件路径>
   ```
3. 如果提示类似如下报错信息，原因可能是es2abc和动态库文件不属于一个签名组。

   ```
   1. os::library_loader::Load error: dlopen(..., 0x0001):
   2. tried: '...' (code signature in <...> '...' not valid for use in process: mapped file has no cdhash, completely unsigned? Code has to be at least ad-hoc signed.)
   ```
4. 用下面命令查看es2abc和动态库文件的签名组信息，如果两个文件，一个有签名信息，一个没有签名信息，或者都有签名信息，但是签名信息中属性'TeamIdentifier'的值是不一样的，那就说明问题是签名组不一致导致的，可以使用"解决方案"提供的方式处理。

   ```
   1. codesign -dv --verbose=1 <es2abc路径>
   2. codesign -dv --verbose=1 <动态库路径>
   ```

**解决方案**

执行下列命令，将es2abc文件的签名替换成和动态库文件一样的用户签名。

```
1. codesign --remove-signature <es2abc路径>
2. codesign -s - -v <es2abc路径>
```
