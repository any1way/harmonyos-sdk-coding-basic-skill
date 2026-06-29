---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/network-boost-c-files-boost
title: network_boost.h
breadcrumb: API参考 > 系统 > 网络 > Network Boost Kit（网络加速服务） > C API > 头文件 > network_boost.h
category: harmonyos-references
scraped_at: 2026-06-11T16:15:18+08:00
doc_updated_at: 2026-05-19
content_hash: sha256:18d749ba4091935b46b0935869725ec1776b35be7127abaefcca87133d44dcb4
---
## 概述

PhonePC/2in1Tablet

声明用于网络加速的API。提供基本的函数、结构体和const定义。

**引用文件：** <NetworkBoostKit/network\_boost.h>

**库：** libnetwork\_boost.so

**系统能力：** SystemCapability.Communication.NetworkBoost.Core

**起始版本：** 6.0.2(22)

**相关模块：** [NetworkBoost](../../模块/NetworkBoost/network-boost-c-overview.md)

## 汇总

PhonePC/2in1Tablet

## 结构体

PhonePC/2in1Tablet

| 名称 | 描述 |
| --- | --- |
| struct [NetworkBoost\_SceneDesc](../../结构体/NetworkBoost_SceneDesc/network-boost-c-struct-scene_desc.md) | 业务场景描述信息。 |

## 枚举

PhonePC/2in1Tablet

| 名称 | 描述 |
| --- | --- |
| struct [NetworkBoost\_SceneEvent](../../模块/NetworkBoost/network-boost-c-overview.md#networkboost_sceneevent){  NB\_SCENE\_EVENT\_ENTER = 0, NB\_SCENE\_EVENT\_UPDATE = 1, NB\_SCENE\_EVENT\_LEAVE = 2  } | 业务事件枚举。 |

## 函数

PhonePC/2in1Tablet

| 名称 | 描述 |
| --- | --- |
| int32\_t [HMS\_NetworkBoost\_SetSceneDesc](../../模块/NetworkBoost/network-boost-c-overview.md#hms_networkboost_setscenedesc)([NetworkBoost\_SceneDesc](../../结构体/NetworkBoost_SceneDesc/network-boost-c-struct-scene_desc.md) sceneDesc) | 设置业务场景。 |
