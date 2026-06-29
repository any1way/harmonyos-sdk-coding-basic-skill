---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-game-device
title: game_device.h
breadcrumb: API参考 > 应用服务 > Game Controller Kit（游戏控制器服务） > C API > 头文件和结构体 > 头文件 > game_device.h
category: harmonyos-references
scraped_at: 2026-06-01T16:33:56+08:00
doc_updated_at: 2026-04-30
content_hash: sha256:5c47d006beca9eaf77afdd8bed00d3a3c50cd8b113a988c8be620cbcd7ecd942
---
## 概述

PhonePC/2in1TabletTV

定义游戏设备的接口。

**引用文件：** <GameControllerKit/game\_device.h>

**库：** libohgame\_controller.z.so

**系统能力：** SystemCapability.Game.GameController

**起始版本：** 21

**相关模块：**[GameController](../../../模块/GameController/capi-game-controller.md)

## 汇总

PhonePC/2in1TabletTV

### 类型定义

PhonePC/2in1TabletTV

| 名称 | 描述 |
| --- | --- |
| typedef struct [GameDevice\_AllDeviceInfos](../../../模块/GameController/capi-game-controller.md#gamedevice_alldeviceinfos) [GameDevice\_AllDeviceInfos](../../../模块/GameController/capi-game-controller.md#gamedevice_alldeviceinfos) | 定义[OH\_GameDevice\_GetAllDeviceInfos](../../../模块/GameController/capi-game-controller.md#oh_gamedevice_getalldeviceinfos)接口的调用结果。 |

### 函数

PhonePC/2in1TabletTV

| 名称 | 描述 |
| --- | --- |
| [GameController\_ErrorCode](../../../模块/GameController/capi-game-controller.md#gamecontroller_errorcode) [OH\_GameDevice\_GetAllDeviceInfos](../../../模块/GameController/capi-game-controller.md#oh_gamedevice_getalldeviceinfos) ([GameDevice\_AllDeviceInfos](../../../模块/GameController/capi-game-controller.md#gamedevice_alldeviceinfos) \*\*allDeviceInfos) | 获取所有在线设备的信息。 |
| [GameController\_ErrorCode](../../../模块/GameController/capi-game-controller.md#gamecontroller_errorcode) [OH\_GameDevice\_RegisterDeviceMonitor](../../../模块/GameController/capi-game-controller.md#oh_gamedevice_registerdevicemonitor) ([GameDevice\_DeviceMonitorCallback](../../../模块/GameController/capi-game-controller.md#gamedevice_devicemonitorcallback) deviceMonitorCallback) | 注册设备状态变化事件的监听回调。 |
| [GameController\_ErrorCode](../../../模块/GameController/capi-game-controller.md#gamecontroller_errorcode) [OH\_GameDevice\_UnregisterDeviceMonitor](../../../模块/GameController/capi-game-controller.md#oh_gamedevice_unregisterdevicemonitor) (void) | 取消注册设备状态变化事件的监听回调。 |
| [GameController\_ErrorCode](../../../模块/GameController/capi-game-controller.md#gamecontroller_errorcode) [OH\_GameDevice\_DestroyAllDeviceInfos](../../../模块/GameController/capi-game-controller.md#oh_gamedevice_destroyalldeviceinfos) ([GameDevice\_AllDeviceInfos](../../../模块/GameController/capi-game-controller.md#gamedevice_alldeviceinfos) \*\*allDeviceInfos) | 当[GameDevice\_AllDeviceInfos](../../../模块/GameController/capi-game-controller.md#gamedevice_alldeviceinfos)实例不再使用，销毁该实例。 |
| [GameController\_ErrorCode](../../../模块/GameController/capi-game-controller.md#gamecontroller_errorcode) [OH\_GameDevice\_AllDeviceInfos\_GetCount](../../../模块/GameController/capi-game-controller.md#oh_gamedevice_alldeviceinfos_getcount) (const struct [GameDevice\_AllDeviceInfos](../../../模块/GameController/capi-game-controller.md#gamedevice_alldeviceinfos) \*allDeviceInfos, int32\_t \*count) | 获取设备数量。 |
| [GameController\_ErrorCode](../../../模块/GameController/capi-game-controller.md#gamecontroller_errorcode) [OH\_GameDevice\_AllDeviceInfos\_GetDeviceInfo](../../../模块/GameController/capi-game-controller.md#oh_gamedevice_alldeviceinfos_getdeviceinfo) (const struct [GameDevice\_AllDeviceInfos](../../../模块/GameController/capi-game-controller.md#gamedevice_alldeviceinfos) \*allDeviceInfos, const int32\_t index, [GameDevice\_DeviceInfo](../../../模块/GameController/capi-game-controller.md#gamedevice_deviceinfo) \*\*deviceInfo) | 从所有设备信息中获取指定序号的设备信息。 |
