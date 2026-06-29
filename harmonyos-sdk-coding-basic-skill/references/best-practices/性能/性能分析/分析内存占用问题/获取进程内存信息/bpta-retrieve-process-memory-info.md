---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-retrieve-process-memory-info
title: 获取进程内存信息
breadcrumb: 最佳实践 > 性能 > 性能分析 > 分析内存占用问题 > 获取进程内存信息
category: best-practices
scraped_at: 2026-06-12T10:15:16+08:00
doc_updated_at: 2026-03-12
content_hash: sha256:68cb183ae9a57b0076ee855f9788eae3438f74881eed1defb33a7aed39a137c0
---
## 通过HiDumper查看内存信息

开发者可以通过以下步骤，获取到当前应用的内存信息。

1. 打开示例应用，运行 hdc shell "hidumper -s WindowManagerService -a '-a'"获取到当前应用的pid。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f6/v3/idrOSoZGSWSnOPQA-Oahkg/zh-cn_image_0000002404045153.png?HW-CC-KV=V1&HW-CC-Date=20260612T021515Z&HW-CC-Expire=86400&HW-CC-Sign=82155770DDD37FA7079EF86DC4329890D441CA049A1AE648889C25A07AED8B85 "点击放大")
2. 输入 hdc shell "hidumper --mem [Pid]" ，并将命令中的 [Pid] 换成当前应用的Pid，就可以获取到示例应用的内存信息了

一般情况下，开发者只需要关注PSS （Proportional Set Size，实际使用物理内存）Total一列的数据，即示例应用实际使用的物理内存。如下图所示，应用总共占用了26279KB的内存，主要包括ArkTS Heap（ArkTS堆内存）的4712KB以及Native Heap的13164KB。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ff/v3/75p4sxFCSGSrGPkE7AEMDw/zh-cn_image_0000002370565324.png?HW-CC-KV=V1&HW-CC-Date=20260612T021515Z&HW-CC-Expire=86400&HW-CC-Sign=C0F0BD7C255AA68DDEAF6F17F7B521575D77173A7BA6C3765CDC28FF20D91A67 "点击放大")

## 通过代码获取应用内存信息

开发者可使用[@ohos.hidebug (Debug调试)](<../../../../../harmonyos-references/Performance Analysis Kit（性能分析服务）/ArkTS API/@ohos.hidebug (Debug调试)/js-apis-hidebug.md>)接口获取应用进程的内存信息，使用指导详见[获取内存信息](<../../../../../harmonyos-guides/系统/调测调优/Performance Analysis Kit（性能分析服务）/系统调试信息获取/HiDebug能力概述/hidebug-guidelines.md#获取内存信息>)。

## 使用onMemoryLevel()监听内存变化

onMemoryLevel()是HarmonyOS提供监听系统内存变化的接口，开发者可以通过onMemoryLevel()监听内存变化，从而调整应用的内存。onMemoryLevel()回调包括三种方式，分别为[AbilityStage](<../../../../../harmonyos-references/Ability Kit（程序框架服务）/ArkTS API/Stage模型能力的接口/@ohos.app.ability.AbilityStage (AbilityStage组件管理器)/js-apis-app-ability-abilitystage.md#abilitystage>)、[UIAbility](<../../../../../harmonyos-references/Ability Kit（程序框架服务）/ArkTS API/Stage模型能力的接口/@ohos.app.ability.Ability (Ability基类)/js-apis-app-ability-ability.md#abilityonmemorylevel>)、[EnvironmentCallback](<../../../../../harmonyos-references/Ability Kit（程序框架服务）/ArkTS API/Stage模型能力的接口/@ohos.app.ability.EnvironmentCallback (系统环境变化监听器)/js-apis-app-ability-environmentcallback.md>)。

* AbilityStage：当HAP中的代码首次被加载到进程中的时候，系统会先创建AbilityStage实例，系统决定调整内存时，再回调AbilityStage实例的onMemoryLevel()方法。

* UIAbility：Ability是UIAbility的基类，在Ability中，提供系统内存变化的回调方法。
* EnvironmentCallback：EnvironmentCallback模块提供应用上下文ApplicationContext对系统环境变化监听回调的能力。

MemoryLevel分为MEMORY\_LEVEL\_MODERATE、MEMORY\_LEVEL\_LOW和MEMORY\_LEVEL\_CRITICAL三种。其中，MEMORY\_LEVEL\_MODERATE代表当前系统内存压力适中，应用可以正常运行而不会受到太大影响，MEMORY\_LEVEL\_LOW代表当前系统的内存已经比较低了，应用应该释放不必要的内存资源，避免造成系统卡顿，MEMORY\_LEVEL\_CRITICAL代表当前所剩的系统内存非常紧张，应用应该尽可能释放更多的资源，以确保系统的稳定性和性能。开发人员应该根据不同的内存级别来采取相应的措施，如释放资源、优化内存使用等，以确保应用在不同内存状态下都能正常运行。MemoryLevel具体等级定义如下所示：

**表1** onMemoryLevel等级定义

| 等级 | 值 | 说明 |
| --- | --- | --- |
| MEMORY\_LEVEL\_MODERATE | 0 | 系统内存适中。系统可能会开始根据LRU缓存规则杀死进程。 |
| MEMORY\_LEVEL\_LOW | 1 | 系统内存比较低。此时应该去释放掉一些不必要的资源以提升系统的性能。 |
| MEMORY\_LEVEL\_CRITICAL | 2 | 系统内存很低。此时应当尽可能地去释放任何不必要的资源，因为系统可能会杀掉所有缓存中的进程，并且开始杀掉应当保持运行的进程，比如后台运行的服务。 |

说明

后台已冻结的应用，AbilityStage、UIAbility、EnvironmentCallback的onMemoryLevel都不可以进行回调。
