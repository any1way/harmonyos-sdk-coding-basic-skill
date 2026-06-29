---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/start-local-pageability
title: 启动本地PageAbility
breadcrumb: 指南 > 应用框架 > Ability Kit（程序框架服务） > FA模型开发指导 > FA模型应用组件 > PageAbility组件开发指导 > 启动本地PageAbility
category: harmonyos-guides
scraped_at: 2026-06-01T10:58:52+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:6566e4c7bfedcd789f4ff10811f325057fabcf1bdbbfb0886134b31f3b909470
---
PageAbility相关的能力通过featureAbility提供，启动本地Ability通过featureAbility中的startAbility接口实现。

**表1** featureAbility接口说明

| 接口名 | 接口描述 |
| --- | --- |
| startAbility(parameter: StartAbilityParameter) | 启动Ability。 |
| startAbilityForResult(parameter: StartAbilityParameter) | 启动Ability，并在该Ability被销毁时返回执行结果。 |

如下示例通过startAbility显式启动PageAbility。启动Ability的参数包含want，关于want的说明详见[对象间信息传递载体Want](../../信息传递载体Want/want-fa.md)，相应的，隐式启动与显式启动也不在此赘述。

```
1. import featureAbility from '@ohos.ability.featureAbility';
2. import Want from '@ohos.app.ability.Want';
3. import hilog from '@ohos.hilog';

5. const TAG: string = 'PagePageAbilityFirst';
6. const domain: number = 0xFF00;
```

```
1. (async (): Promise<void> => {
2. try {
3. hilog.info(domain, TAG, 'Begin to start ability');
4. let want: Want = {
5. bundleName: 'com.samples.famodelabilitydevelop',
6. moduleName: 'entry',
7. abilityName: 'com.samples.famodelabilitydevelop.PageAbilitySingleton'
8. };
9. await featureAbility.startAbility({ want: want });
10. hilog.info(domain, TAG, `Start ability succeed`);
11. }
12. catch (error) {
13. hilog.error(domain, TAG, 'Start ability failed with ' + error);
14. }
15. })()
```
