---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-game-controller-type
title: game_controller_type.h
breadcrumb: API参考 > 应用服务 > Game Controller Kit（游戏控制器服务） > C API > 头文件和结构体 > 头文件 > game_controller_type.h
category: harmonyos-references
scraped_at: 2026-06-01T16:33:55+08:00
doc_updated_at: 2026-04-30
content_hash: sha256:3956ae09f3a7b317fd9802bfd9716fbff735b94dcc1f4f4b64b800057571bf3d
---
## 概述

PhonePC/2in1TabletTV

定义GameController模块的通用枚举类型。

**引用文件：** <GameControllerKit/game\_controller\_type.h>

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
| typedef enum [GameController\_ErrorCode](../../../模块/GameController/capi-game-controller.md#gamecontroller_errorcode) [GameController\_ErrorCode](../../../模块/GameController/capi-game-controller.md#gamecontroller_errorcode) | 此枚举定义游戏控制器的错误码。 |

### 枚举

PhonePC/2in1TabletTV

| 名称 | 描述 |
| --- | --- |
| [GameController\_ErrorCode](../../../模块/GameController/capi-game-controller.md#gamecontroller_errorcode) {  GAME\_CONTROLLER\_SUCCESS = 0,  GAME\_CONTROLLER\_PARAM\_ERROR = 401,  GAME\_CONTROLLER\_MULTIMODAL\_INPUT\_ERROR = 32200001,  GAME\_CONTROLLER\_NO\_MEMORY = 32200002  } | 游戏控制器错误码。 |
