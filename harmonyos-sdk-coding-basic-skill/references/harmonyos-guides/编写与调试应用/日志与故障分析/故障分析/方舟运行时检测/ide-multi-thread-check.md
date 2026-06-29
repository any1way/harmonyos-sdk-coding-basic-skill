---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-multi-thread-check
title: 方舟运行时检测
breadcrumb: 指南 > 编写与调试应用 > 日志与故障分析 > 故障分析 > 方舟运行时检测
category: harmonyos-guides
scraped_at: 2026-06-11T15:29:47+08:00
doc_updated_at: 2026-06-10
content_hash: sha256:601ec4763078dcdac42431743b5633826df507986a48a37e7590c064e4c9ebd1
---
## 方舟多线程检测

在JS运行时环境中，多线程的安全问题是一个重要的考虑因素。由于JavaScript主线程是单线程的，在主线程中创建的JS对象（尤其是DOM相关对象）只能在主线程上进行操作。如果违反了这一规则，就会导致多线程安全问题。针对该场景，DevEco Studio集成多线程检测能力，并通过FaultLog展示错误的堆栈详情及导致错误的代码行。关于多线程检测的原理请参考[原理介绍](../../../../../best-practices/稳定性/稳定性检测/开发态稳定性检测/方舟类问题检测/方舟运行时检测/bpta-stability-ark-runtime-detection.md#section18515155816101)。

开启多线程检测会有较大性能损耗，请开发者按需开启。

### 开启方舟多线程检测

可通过以下方式开启方舟多线程检测。

* **方式一**

  点击**Run > Edit Configurations >** **Diagnostics**，勾选**Multi Thread Check**。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f5/v3/6vIfeOICSWeQKnQl3V6WoQ/zh-cn_image_0000002571387658.png?HW-CC-KV=V1&HW-CC-Date=20260611T072946Z&HW-CC-Expire=86400&HW-CC-Sign=6B48B9FC7BFB8B7C5DAFBBA0FC02BD3055ECCA1B63BE375BD250EDFD15DA6A86)

* **方式二**

  通过命令行开启。

  ```
  1. hdc shell aa start -a {abilityName} -b {bundleName} -R
  ```

* **方式三**

  通过调用[setMultithreadingDetectionEnabled接口](<../../../../../harmonyos-references/ArkTS（方舟编程语言）/ArkTS API/@ohos.util (util工具函数)/js-apis-util.md#setmultithreadingdetectionenabled23>)开启。

### 使用方舟多线程检测

1. 运行或调试当前应用。
2. 当程序出现多线程安全问题时，会弹出Crash log信息，点击信息中的链接即可跳转至引起多线程安全问题的代码处。关于多线程安全问题的分析方法请参考[使用Node-API接口产生的异常日志/崩溃分析](../../../../NDK开发/代码开发/使用Node-API实现ArkTSJS与CC++语言交互/Node-API典型使用场景/使用Node-API接口产生的异常日志崩溃分析/use-napi-about-crash.md)。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4e/v3/cyDo9wU8TxCTsCHx6DAFsw/zh-cn_image_0000002602066771.png?HW-CC-KV=V1&HW-CC-Date=20260611T072946Z&HW-CC-Expire=86400&HW-CC-Sign=1097B5E4673638D185926EDBA2C40E873752E1713D026B85D8D3CD04B0921ED9)

## 方舟native模块加载异常信息增强

在进行ArkTS项目开发中可能存在需要加载native模块的场景，开启方舟native模块加载异常信息增强功能后，可以丰富ArkTS项目中因加载native模块导致的报错信息，以便更准确地进行native问题定位。

### 开启方舟native模块加载异常信息增强

可以通过以下两种方式开启方舟native模块加载异常信息增强。

* 方式一

  点击**Run > Edit Configurations >** **Diagnostics**，勾选**Enhanced Error Info**。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/93/v3/MfdktDyERVKGDzJDWpAOQQ/zh-cn_image_0000002571387656.png?HW-CC-KV=V1&HW-CC-Date=20260611T072946Z&HW-CC-Expire=86400&HW-CC-Sign=4C38DD708E7FEFA6F601CE707A6DDD985BAB1796B95457C0DC0B51B87B6FE263)

* 方式二

  通过命令行开启。

  ```
  1. hdc shell aa start {abilityName} {bundleName} -E
  ```

### 使用方舟native模块加载异常信息增强

1. 运行或调试当前应用。
2. 当程序出现因native模块加载导致的报错信息时，会显示更详细准确的错误信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fd/v3/A_645VYYR3iF9v0pUZtuRQ/zh-cn_image_0000002602066773.png?HW-CC-KV=V1&HW-CC-Date=20260611T072946Z&HW-CC-Expire=86400&HW-CC-Sign=003B2C33EC1395DC477AAE22864806B88E6B71535AA108ECFCF772D3A511ACC8)
