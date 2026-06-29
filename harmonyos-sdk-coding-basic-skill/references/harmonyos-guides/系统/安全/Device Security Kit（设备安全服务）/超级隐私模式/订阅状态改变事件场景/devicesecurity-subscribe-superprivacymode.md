---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/devicesecurity-subscribe-superprivacymode
title: 订阅状态改变事件场景
breadcrumb: 指南 > 系统 > 安全 > Device Security Kit（设备安全服务） > 超级隐私模式 > 订阅状态改变事件场景
category: harmonyos-guides
scraped_at: 2026-06-11T14:44:36+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:3aa9ce8664ffdb53608dffaaa6917e8e3565f162e386633f1d3bf64ba1d72fe6
---
## 场景介绍

从6.0.2(22)开始，新增订阅超级隐私模式状态改变事件。

超级隐私模式为用户提供一键关闭敏感器件的能力，管控范围包括位置、相机和麦克风，且随着版本演进，超级隐私模式管控的敏感器件范围会相应调整。应用可通过Device Security Kit提供的接口监听当前超级隐私模式开关状态。

## 约束与限制

本特性需要设备上存在超级隐私模式选项。开发者可通过在设备上选择“设置 > 隐私和安全 > 超级隐私模式”查看超级隐私模式选项。

## 业务流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4b/v3/1vDvlhI2S36aNn59XJvHeA/zh-cn_image_0000002622858267.png?HW-CC-KV=V1&HW-CC-Date=20260611T064435Z&HW-CC-Expire=86400&HW-CC-Sign=85B19815B1ADF018BA76D95506B51DE4C6D3598E49BA7FAD802A12543D8E7EC4)

**流程说明：**

1. 开发者应用订阅超级隐私模式状态改变事件。
2. Device Security Kit调用回调函数通知开发者应用，
3. 开发者应用根据当前超级隐私模式的状态进行业务处理。
4. 当开发者应用不需要使用超级隐私模式状态时，取消订阅超级隐私模式状态改变事件。

## 接口说明

以下是超级隐私模式状态改变订阅与取消订阅接口，更多接口及使用方法请参见[API参考](<../../../../../../harmonyos-references/Device Security Kit（设备安全服务）/ArkTS API/SuperPrivacyMode（超级隐私模式）/devicesecurity-superprivacymode-api.md>)。

| 接口名 | 描述 |
| --- | --- |
| on(type: 'superPrivacyModeChange', callback: Callback<[SuperPrivacyMode](<../../../../../../harmonyos-references/Device Security Kit（设备安全服务）/ArkTS API/SuperPrivacyMode（超级隐私模式）/devicesecurity-superprivacymode-api.md#superprivacymode>)>): void | 订阅超级隐私模式状态改变事件 |
| off(type: 'superPrivacyModeChange', callback?: Callback<[SuperPrivacyMode](<../../../../../../harmonyos-references/Device Security Kit（设备安全服务）/ArkTS API/SuperPrivacyMode（超级隐私模式）/devicesecurity-superprivacymode-api.md#superprivacymode>)>): void | 取消订阅超级隐私模式状态改变事件 |

## 开发步骤

1. 导入超级隐私模块及相关公共模块。

   ```
   1. import { superPrivacyMode } from '@kit.DeviceSecurityKit';
   2. import { hilog } from '@kit.PerformanceAnalysisKit';
   ```
2. 订阅超级隐私模式状态改变事件。

   ```
   1. const DOMAIN = 0x0000;
   2. const TAG = "SuperPrivacyModeTest";

   4. const superPrivacyChangedCallback = (superPrivacyMode: superPrivacyMode.SuperPrivacyMode): void => {
   5. hilog.info(DOMAIN, TAG, `super privcy mode changed, mode = ${superPrivacyMode}`);
   6. }
   7. hilog.info(DOMAIN, TAG, 'start register super privacy mode changed listener');
   8. try {
   9. superPrivacyMode.on('superPrivacyModeChange', superPrivacyChangedCallback);
   10. hilog.info(DOMAIN, TAG, 'register super privacy mode change listener success');
   11. } catch (err) {
   12. hilog.error(DOMAIN, TAG, `register super privacy changed listener failed, errCode:${err?.code}, errMessage:${err?.message}`);
   13. }
   ```
3. 取消订阅超级隐私模式状态改变事件。

   ```
   1. hilog.info(DOMAIN, TAG, 'start unregister super privacy mode changed listener');
   2. try {
   3. superPrivacyMode.off('superPrivacyModeChange', superPrivacyChangedCallback);
   4. } catch (err) {
   5. hilog.error(DOMAIN, TAG, `unregister super privacy changed listener failed, errCode:${err?.code}, errMessage:${err?.message}`);
   6. }
   ```
