---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-shellcmdresult
title: ShellCmdResult
breadcrumb: API参考 > 系统 > 调测调优 > Test Kit（应用测试服务） > ArkTS API > 接口依赖的元素及定义 > ShellCmdResult
category: harmonyos-references
scraped_at: 2026-06-11T16:25:44+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:d9043034c680099c33d56a5f464f9b2e26d4966b287e377d93ceb6193ae8320e
---
本模块提供Shell命令执行结果的能力。

说明

本模块首批接口从API version 8开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

本模块接口仅可在[单元测试框架](../../../../../harmonyos-guides/应用测试/单元测试和UI测试/自动化测试框架使用指导/单元测试框架使用指导/unittest-guidelines.md)中使用。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { abilityDelegatorRegistry } from '@kit.TestKit';
```

## 使用说明

PhonePC/2in1TabletTVWearable

通过abilityDelegator中的[executeShellCommand](../AbilityDelegator/js-apis-inner-application-abilitydelegator.md#executeshellcommand)方法来获取。

**示例：**

```
1. import { abilityDelegatorRegistry } from '@kit.TestKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let abilityDelegator: abilityDelegatorRegistry.AbilityDelegator;
5. let cmd = 'cmd';

7. abilityDelegator = abilityDelegatorRegistry.getAbilityDelegator();
8. abilityDelegator.executeShellCommand(cmd, (error: BusinessError, data) => {
9. if (error) {
10. console.error(`executeShellCommand fail, error: ${JSON.stringify(error)}`);
11. } else {
12. console.info(`executeShellCommand success, data: ${JSON.stringify(data)}`);
13. }
14. });
```

## ShellCmdResult

PhonePC/2in1TabletTVWearable

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| stdResult | string | 否 | 否 | Shell命令的标准输出内容。 |
| exitCode | number | 否 | 否 | Shell命令的结果码。 |
