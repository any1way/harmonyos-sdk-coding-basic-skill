---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/devicesecurity-audit-acquirecodesign-c
title: 代码签名信息查询场景（C/C++）
breadcrumb: 指南 > 系统 > 安全 > Device Security Kit（设备安全服务） > 安全审计 > 代码签名信息查询场景（C/C++）
category: harmonyos-guides
scraped_at: 2026-06-11T14:44:23+08:00
doc_updated_at: 2026-04-30
content_hash: sha256:444177f4e48ba2ae125c8d5ff2052d49a716231ec758efd223627cb8cf3efd15
---
从6.1.1(24)开始，新增提供文件代码签名信息查询接口，可以获取设备上已签名的文件签名信息。

## 场景介绍

签名信息包括：应用ID、签发组织证书链、签名摘要、签名时间戳、签名使用的Hash算法。通过[HMS\_SecurityAudit\_AcquireCodeSign](<../../../../../../harmonyos-references/Device Security Kit（设备安全服务）/C API/模块/SecurityAudit/devicesecurity-capi-securityaudit.md#hms_securityaudit_acquirecodesign>)接口，应用可以获取代码签名信息，辅助应用判断运行代码的完整性和安全性，从而有效防止恶意软件的运行，提升设备安全防护能力。

## 约束和限制

1. 当前能力仅支持2in1设备。
2. 调用[HMS\_SecurityAudit\_AcquireCodeSign](<../../../../../../harmonyos-references/Device Security Kit（设备安全服务）/C API/模块/SecurityAudit/devicesecurity-capi-securityaudit.md#hms_securityaudit_acquirecodesign>)接口的应用程序需要具备读取目标代码签名文件的权限。

## 业务流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c9/v3/PCb6OHygSdqfV7XbbTnVGw/zh-cn_image_0000002592378754.png?HW-CC-KV=V1&HW-CC-Date=20260611T064422Z&HW-CC-Expire=86400&HW-CC-Sign=36D0100100397AA21F6F87910A0F51BB693485DC6D488FFA59DEB6AC234BC140)

**流程说明：**

1. 用户在hap应用上调用获取文件代码签名信息接口[HMS\_SecurityAudit\_AcquireCodeSign](<../../../../../../harmonyos-references/Device Security Kit（设备安全服务）/C API/模块/SecurityAudit/devicesecurity-capi-securityaudit.md#hms_securityaudit_acquirecodesign>)。
2. [HMS\_SecurityAudit\_AcquireCodeSign](<../../../../../../harmonyos-references/Device Security Kit（设备安全服务）/C API/模块/SecurityAudit/devicesecurity-capi-securityaudit.md#hms_securityaudit_acquirecodesign>)接口同步返回应用所传入的文件对应的代码签名信息。

## 接口说明

接口如下表，更多接口及使用方法请参见[API参考](<../../../../../../harmonyos-references/Device Security Kit（设备安全服务）/C API/模块/SecurityAudit/devicesecurity-capi-securityaudit.md#hms_securityaudit_acquirecodesign>)。

| 接口名 | 描述 |
| --- | --- |
| int32\_t [HMS\_SecurityAudit\_AcquireCodeSign](<../../../../../../harmonyos-references/Device Security Kit（设备安全服务）/C API/模块/SecurityAudit/devicesecurity-capi-securityaudit.md#hms_securityaudit_acquirecodesign>)(char\* path, char\*\* outOwnedResult) | 获取输入的文件路径的代码签名信息。 |

## 开发步骤

在开发准备过程中，需要申请权限：ohos.permission.QUERY\_AUDIT\_EVENT，只允许清单内的企业类应用申请该权限，申请方式请参考：[申请使用企业类应用可用权限](../../../程序访问控制/应用权限管控/应用权限列表/企业类应用可用权限/permissions-for-enterprise-apps.md)。

1. 在CMakeLists.txt中导入安全审计共享库，并链接该库。

   ```
   1. find_library(dsm-lib libsecurityaudit_ndk.z.so)
   2. target_link_libraries(entry PUBLIC libace_napi.z.so ${dsm-lib})
   ```
2. 导入安全审计的头文件。

   ```
   1. #include <DeviceSecurityKit/security_audit.h>
   2. #include <cstdio>
   ```
3. 开发者调用[HMS\_SecurityAudit\_AcquireCodeSign](<../../../../../../harmonyos-references/Device Security Kit（设备安全服务）/C API/模块/SecurityAudit/devicesecurity-capi-securityaudit.md#hms_securityaudit_acquirecodesign>)接口，获取所传入的文件对应的代码签名信息，并在处理完接口返回的代码签名信息后释放出入参内存。

   ```
   1. void AcquireCodeSignTest()
   2. {
   3. char *result = nullptr;
   4. char *path = "test";
   5. int32_t ret = HMS_SecurityAudit_AcquireCodeSign(path, &result);
   6. if (ret == 0 && result != nullptr) {
   7. printf("HMS_SecurityAudit_AcquireCodeSign result: %s\n", result);
   8. } else {
   9. printf("HMS_SecurityAudit_AcquireCodeSign failed with error: %d\n", ret);
   10. }
   11. if (result != nullptr) {
   12. delete[] result;
   13. result = nullptr;
   14. }
   15. }
   ```
