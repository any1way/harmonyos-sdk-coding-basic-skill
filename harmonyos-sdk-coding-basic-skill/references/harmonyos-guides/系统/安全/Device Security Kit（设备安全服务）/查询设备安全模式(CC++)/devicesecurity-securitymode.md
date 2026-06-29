---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/devicesecurity-securitymode
title: 查询设备安全模式(C/C++)
breadcrumb: 指南 > 系统 > 安全 > Device Security Kit（设备安全服务） > 查询设备安全模式(C/C++)
category: harmonyos-guides
scraped_at: 2026-06-01T11:16:47+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:816b5766c6acbb5f743a3bd1d3f27d74bfc20b0889581a42cffe480c2f7bbd33
---
## 场景介绍

Device Security Kit提供了系统安全模式的查询能力。通过调用Device Security Kit的接口，可以判断设备当前的安全模式（包含普通模式、坚盾守护模式），应用可根据设备当前的安全模式提供差异化的服务。

* 普通模式：操作系统默认模式，适用于绝大部分用户使用。
* 坚盾守护模式：提供给高安全需求用户的系统级别安全模式。该模式通过限制设备基础功能，增强安全性，有效抵御远程攻击面的针对性攻击。

  坚盾守护模式下，操作系统禁止应用申请获取匿名内存可执行权限。

  应用应当根据系统安全模式进行自主适配，停用即时编译（JIT，Just-in-time compilation）功能或切换为解释执行。

## 开发步骤

1. 在CMakeLists.txt中导入设备安全模式共享库，并链接该库。

   ```
   1. find_library(dsm-lib libdevice_security_mode.z.so)
   2. target_link_libraries(entry PUBLIC libace_napi.z.so ${dsm-lib})
   ```
2. 导入设备安全模式的头文件。

   ```
   1. #include <DeviceSecurityKit/device_security_mode.h>
   ```
3. 调用接口查询设备当前的安全模式。

   ```
   1. int32_t IsSecureShieldModeOn(void)
   2. {
   3. DSM_DeviceSecurityMode mode = HMS_DSM_GetDeviceSecurityMode();
   4. return mode & DSM_SECURE_SHIELD_MODE;
   5. }
   ```

说明

若应用使用到ArkWeb组件，需进一步参考[说明](../../../../应用框架/ArkWeb（方舟Web）/管理Web组件的网络安全与隐私/坚盾守护模式/web-secure-shield-mode.md)，进行Web特性的兼容性评估。
