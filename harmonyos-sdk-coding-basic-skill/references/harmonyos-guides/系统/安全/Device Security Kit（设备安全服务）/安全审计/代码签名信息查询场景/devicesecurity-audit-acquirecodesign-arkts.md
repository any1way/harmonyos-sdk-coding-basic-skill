---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/devicesecurity-audit-acquirecodesign-arkts
title: 代码签名信息查询场景
breadcrumb: 指南 > 系统 > 安全 > Device Security Kit（设备安全服务） > 安全审计 > 代码签名信息查询场景
category: harmonyos-guides
scraped_at: 2026-06-11T14:44:16+08:00
doc_updated_at: 2026-04-30
content_hash: sha256:640d87a843041e445f54f8c3c4818334014395bfdd0d40e26592aeb4837a06c4
---
从6.1.1(24)开始，新增提供文件代码签名信息查询接口，可以获取设备上已签名的文件签名信息。

## 场景介绍

签名信息包括：应用ID、签发组织证书链、签名摘要、签名时间戳、签名使用的Hash算法。通过[acquireCodeSign](<../../../../../../harmonyos-references/Device Security Kit（设备安全服务）/ArkTS API/SecurityAudit（安全审计）/devicesecurity-securityaudit-api.md#acquirecodesign>)接口，应用可以获取代码签名信息，辅助应用判断运行代码的完整性和安全性，从而有效防止恶意软件的运行，提升设备安全防护能力。

## 约束和限制

1. 当前能力仅支持2in1设备。
2. 调用[acquireCodeSign](<../../../../../../harmonyos-references/Device Security Kit（设备安全服务）/ArkTS API/SecurityAudit（安全审计）/devicesecurity-securityaudit-api.md#acquirecodesign>)接口的应用程序需要具备读取目标代码签名文件的权限。

## 业务流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/68/v3/1lbik_2wRSKOwFX362IkGg/zh-cn_image_0000002592378754.png?HW-CC-KV=V1&HW-CC-Date=20260611T064415Z&HW-CC-Expire=86400&HW-CC-Sign=09DBAA8EB0D532339754D4EDCAD3B9306BBA786FEB864E08E712C081EBBCD870)

**流程说明：**

1. 用户在hap应用上调用文件代码签名信息查询接口[acquireCodeSign](<../../../../../../harmonyos-references/Device Security Kit（设备安全服务）/ArkTS API/SecurityAudit（安全审计）/devicesecurity-securityaudit-api.md#acquirecodesign>)。
2. [acquireCodeSign](<../../../../../../harmonyos-references/Device Security Kit（设备安全服务）/ArkTS API/SecurityAudit（安全审计）/devicesecurity-securityaudit-api.md#acquirecodesign>)接口同步返回应用所传入的文件对应的代码签名信息。

## 接口说明

接口如下表，更多接口及使用方法请参见[API参考](<../../../../../../harmonyos-references/Device Security Kit（设备安全服务）/ArkTS API/SecurityAudit（安全审计）/devicesecurity-securityaudit-api.md#acquirecodesign>)。

| 接口名 | 描述 |
| --- | --- |
| [acquireCodeSign](<../../../../../../harmonyos-references/Device Security Kit（设备安全服务）/ArkTS API/SecurityAudit（安全审计）/devicesecurity-securityaudit-api.md#acquirecodesign>)(path: string): string | 获取输入的文件路径的代码签名信息。 |

## 开发步骤

说明

在开发准备过程中，需要申请权限：ohos.permission.QUERY\_AUDIT\_EVENT，只允许清单内的企业类应用申请该权限，申请方式请参考：[申请使用企业类应用可用权限](../../../程序访问控制/应用权限管控/应用权限列表/企业类应用可用权限/permissions-for-enterprise-apps.md)。

1. 导入Device Security Kit模块及相关公共模块。

   ```
   1. import { securityAudit } from '@kit.DeviceSecurityKit';
   2. import { BusinessError} from '@kit.BasicServicesKit';
   3. import { hilog } from '@kit.PerformanceAnalysisKit';
   ```
2. 开发者调用[acquireCodeSign](<../../../../../../harmonyos-references/Device Security Kit（设备安全服务）/ArkTS API/SecurityAudit（安全审计）/devicesecurity-securityaudit-api.md#acquirecodesign>)接口，获取所传入的文件对应的代码签名信息。

   ```
   1. const TAG = "SecurityAuditJsTest";
   2. let path = 'test';
   3. try {
   4. hilog.info(0x0000, TAG, 'acquireCodeSign begin.');
   5. const result = securityAudit.acquireCodeSign(path);
   6. hilog.info(0x0000, TAG, 'Succeeded in queryCodeSign.');
   7. } catch (err) {
   8. let e: BusinessError = err as BusinessError;
   9. hilog.error(0x0000, TAG, 'acquireCodeSign failed: %{public}d %{public}s', e.code, e.message);
   10. }
   ```
