---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-game-pad-event
title: game_pad_event.h
breadcrumb: API参考 > 应用服务 > Game Controller Kit（游戏控制器服务） > C API > 头文件和结构体 > 头文件 > game_pad_event.h
category: harmonyos-references
scraped_at: 2026-06-01T16:33:58+08:00
doc_updated_at: 2026-04-30
content_hash: sha256:991849af4baf80fbc41cd5e6c40c1a6cb815d480a2106ec9efdfc3c20f085eea
---
## 概述

PhonePC/2in1TabletTV

定义游戏手柄事件的接口。

**引用文件：** <GameControllerKit/game\_pad\_event.h>

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
| typedef enum [GamePad\_AxisSourceType](../../../模块/GameController/capi-game-controller.md#gamepad_axissourcetype) [GamePad\_AxisSourceType](../../../模块/GameController/capi-game-controller.md#gamepad_axissourcetype) | 此枚举定义手柄轴事件来源类型。 |
| typedef enum [GamePad\_Button\_ActionType](../../../模块/GameController/capi-game-controller.md#gamepad_button_actiontype) [GamePad\_Button\_ActionType](../../../模块/GameController/capi-game-controller.md#gamepad_button_actiontype) | 此枚举定义手柄按键动作类型。 |
| typedef struct [GamePad\_ButtonEvent](../../../模块/GameController/capi-game-controller.md#gamepad_buttonevent) [GamePad\_ButtonEvent](../../../模块/GameController/capi-game-controller.md#gamepad_buttonevent) | 定义手柄按键事件。 |
| typedef struct [GamePad\_AxisEvent](../../../模块/GameController/capi-game-controller.md#gamepad_axisevent) [GamePad\_AxisEvent](../../../模块/GameController/capi-game-controller.md#gamepad_axisevent) | 定义手柄轴事件。 |
| typedef struct [GamePad\_PressedButton](../../../模块/GameController/capi-game-controller.md#gamepad_pressedbutton) [GamePad\_PressedButton](../../../模块/GameController/capi-game-controller.md#gamepad_pressedbutton) | 定义手柄按下的按键。 |
| typedef void(\*[GamePad\_ButtonInputMonitorCallback](../../../模块/GameController/capi-game-controller.md#gamepad_buttoninputmonitorcallback)) (const struct [GamePad\_ButtonEvent](../../../模块/GameController/capi-game-controller.md#gamepad_buttonevent) \*buttonEvent) | 定义在按键事件注册监听接口中使用的回调函数。当玩家按下按键时，该回调函数将被调用。 |
| typedef void(\*[GamePad\_AxisInputMonitorCallback](../../../模块/GameController/capi-game-controller.md#gamepad_axisinputmonitorcallback)) (const struct [GamePad\_AxisEvent](../../../模块/GameController/capi-game-controller.md#gamepad_axisevent) \*axisEvent) | 定义在轴事件注册监听接口中使用的回调函数。当玩家操作摇杆时，该回调函数将被调用。 |

### 枚举

PhonePC/2in1TabletTV

| 名称 | 描述 |
| --- | --- |
| [GamePad\_AxisSourceType](../../../模块/GameController/capi-game-controller.md#gamepad_axissourcetype) {  DPAD = 0,  LEFT\_THUMBSTICK = 1,  RIGHT\_THUMBSTICK = 2,  LEFT\_TRIGGER = 3,  RIGHT\_TRIGGER = 4  } | 手柄轴事件来源类型。 |
| [GamePad\_Button\_ActionType](../../../模块/GameController/capi-game-controller.md#gamepad_button_actiontype) {  DOWN = 0,  UP = 1  } | 手柄按键动作类型。 |

### 函数

PhonePC/2in1TabletTV

| 名称 | 描述 |
| --- | --- |
| [GameController\_ErrorCode](../../../模块/GameController/capi-game-controller.md#gamecontroller_errorcode) [OH\_GamePad\_ButtonEvent\_GetDeviceId](../../../模块/GameController/capi-game-controller.md#oh_gamepad_buttonevent_getdeviceid) (const struct [GamePad\_ButtonEvent](../../../模块/GameController/capi-game-controller.md#gamepad_buttonevent) \*buttonEvent, char \*\*deviceId) | 从按键事件[GamePad\_ButtonEvent](../../../模块/GameController/capi-game-controller.md#gamepad_buttonevent)中获取设备ID。 |
| [GameController\_ErrorCode](../../../模块/GameController/capi-game-controller.md#gamecontroller_errorcode) [OH\_GamePad\_ButtonEvent\_GetButtonAction](../../../模块/GameController/capi-game-controller.md#oh_gamepad_buttonevent_getbuttonaction) (const struct [GamePad\_ButtonEvent](../../../模块/GameController/capi-game-controller.md#gamepad_buttonevent) \*buttonEvent, [GamePad\_Button\_ActionType](../../../模块/GameController/capi-game-controller.md#gamepad_button_actiontype) \*actionType) | 从按键事件[GamePad\_ButtonEvent](../../../模块/GameController/capi-game-controller.md#gamepad_buttonevent)中获取按键动作类型。 |
| [GameController\_ErrorCode](../../../模块/GameController/capi-game-controller.md#gamecontroller_errorcode) [OH\_GamePad\_ButtonEvent\_GetButtonCode](../../../模块/GameController/capi-game-controller.md#oh_gamepad_buttonevent_getbuttoncode) (const struct [GamePad\_ButtonEvent](../../../模块/GameController/capi-game-controller.md#gamepad_buttonevent) \*buttonEvent, int32\_t \*code) | 从按键事件[GamePad\_ButtonEvent](../../../模块/GameController/capi-game-controller.md#gamepad_buttonevent)中获取按键编码。 |
| [GameController\_ErrorCode](../../../模块/GameController/capi-game-controller.md#gamecontroller_errorcode) [OH\_GamePad\_ButtonEvent\_GetButtonCodeName](../../../模块/GameController/capi-game-controller.md#oh_gamepad_buttonevent_getbuttoncodename) (const struct [GamePad\_ButtonEvent](../../../模块/GameController/capi-game-controller.md#gamepad_buttonevent) \*buttonEvent, char \*\*codeName) | 从按键事件[GamePad\_ButtonEvent](../../../模块/GameController/capi-game-controller.md#gamepad_buttonevent)中获取按键的名称。 |
| [GameController\_ErrorCode](../../../模块/GameController/capi-game-controller.md#gamecontroller_errorcode) [OH\_GamePad\_PressedButtons\_GetCount](../../../模块/GameController/capi-game-controller.md#oh_gamepad_pressedbuttons_getcount) (const struct [GamePad\_ButtonEvent](../../../模块/GameController/capi-game-controller.md#gamepad_buttonevent) \*buttonEvent, int32\_t \*count) | 从按键事件[GamePad\_ButtonEvent](../../../模块/GameController/capi-game-controller.md#gamepad_buttonevent)中获取按下的按键数量。 |
| [GameController\_ErrorCode](../../../模块/GameController/capi-game-controller.md#gamecontroller_errorcode) [OH\_GamePad\_PressedButtons\_GetButtonInfo](../../../模块/GameController/capi-game-controller.md#oh_gamepad_pressedbuttons_getbuttoninfo) (const struct [GamePad\_ButtonEvent](../../../模块/GameController/capi-game-controller.md#gamepad_buttonevent) \*buttonEvent, const int32\_t index, [GamePad\_PressedButton](../../../模块/GameController/capi-game-controller.md#gamepad_pressedbutton) \*\*pressedButton) | 从按键事件[GamePad\_ButtonEvent](../../../模块/GameController/capi-game-controller.md#gamepad_buttonevent)中获取指定序号的按下的按键。 |
| [GameController\_ErrorCode](../../../模块/GameController/capi-game-controller.md#gamecontroller_errorcode) [OH\_GamePad\_DestroyPressedButton](../../../模块/GameController/capi-game-controller.md#oh_gamepad_destroypressedbutton) ([GamePad\_PressedButton](../../../模块/GameController/capi-game-controller.md#gamepad_pressedbutton) \*\*pressedButton) | 当[GamePad\_PressedButton](../../../模块/GameController/capi-game-controller.md#gamepad_pressedbutton)实例不再使用， 销毁该实例。 |
| [GameController\_ErrorCode](../../../模块/GameController/capi-game-controller.md#gamecontroller_errorcode) [OH\_GamePad\_PressedButton\_GetButtonCode](../../../模块/GameController/capi-game-controller.md#oh_gamepad_pressedbutton_getbuttoncode) (const struct [GamePad\_PressedButton](../../../模块/GameController/capi-game-controller.md#gamepad_pressedbutton) \*pressedButton, int32\_t \*code) | 从按下的按键[GamePad\_PressedButton](../../../模块/GameController/capi-game-controller.md#gamepad_pressedbutton)中获取按键编码。 |
| [GameController\_ErrorCode](../../../模块/GameController/capi-game-controller.md#gamecontroller_errorcode) [OH\_GamePad\_PressedButton\_GetButtonCodeName](../../../模块/GameController/capi-game-controller.md#oh_gamepad_pressedbutton_getbuttoncodename) (const struct [GamePad\_PressedButton](../../../模块/GameController/capi-game-controller.md#gamepad_pressedbutton) \*pressedButton, char \*\*codeName) | 从按下的按键[GamePad\_PressedButton](../../../模块/GameController/capi-game-controller.md#gamepad_pressedbutton)中获取按键的名称。 |
| [GameController\_ErrorCode](../../../模块/GameController/capi-game-controller.md#gamecontroller_errorcode) [OH\_GamePad\_ButtonEvent\_GetActionTime](../../../模块/GameController/capi-game-controller.md#oh_gamepad_buttonevent_getactiontime) (const struct [GamePad\_ButtonEvent](../../../模块/GameController/capi-game-controller.md#gamepad_buttonevent) \*buttonEvent, int64\_t \*actionTime) | 从按键事件[GamePad\_ButtonEvent](../../../模块/GameController/capi-game-controller.md#gamepad_buttonevent)中获取按键动作的时间。 |
| [GameController\_ErrorCode](../../../模块/GameController/capi-game-controller.md#gamecontroller_errorcode) [OH\_GamePad\_AxisEvent\_GetDeviceId](../../../模块/GameController/capi-game-controller.md#oh_gamepad_axisevent_getdeviceid) (const struct [GamePad\_AxisEvent](../../../模块/GameController/capi-game-controller.md#gamepad_axisevent) \*axisEvent, char \*\*deviceId) | 从轴事件[GamePad\_AxisEvent](../../../模块/GameController/capi-game-controller.md#gamepad_axisevent)中获取设备ID。 |
| [GameController\_ErrorCode](../../../模块/GameController/capi-game-controller.md#gamecontroller_errorcode) [OH\_GamePad\_AxisEvent\_GetAxisSourceType](../../../模块/GameController/capi-game-controller.md#oh_gamepad_axisevent_getaxissourcetype) (const struct [GamePad\_AxisEvent](../../../模块/GameController/capi-game-controller.md#gamepad_axisevent) \*axisEvent, [GamePad\_AxisSourceType](../../../模块/GameController/capi-game-controller.md#gamepad_axissourcetype) \*axisSourceType) | 从轴事件[GamePad\_AxisEvent](../../../模块/GameController/capi-game-controller.md#gamepad_axisevent)中获取轴事件来源类型。 |
| [GameController\_ErrorCode](../../../模块/GameController/capi-game-controller.md#gamecontroller_errorcode) [OH\_GamePad\_AxisEvent\_GetXAxisValue](../../../模块/GameController/capi-game-controller.md#oh_gamepad_axisevent_getxaxisvalue) (const struct [GamePad\_AxisEvent](../../../模块/GameController/capi-game-controller.md#gamepad_axisevent) \*axisEvent, double \*axisValue) | 从轴事件[GamePad\_AxisEvent](../../../模块/GameController/capi-game-controller.md#gamepad_axisevent)中获取X轴的轴值。 |
| [GameController\_ErrorCode](../../../模块/GameController/capi-game-controller.md#gamecontroller_errorcode) [OH\_GamePad\_AxisEvent\_GetYAxisValue](../../../模块/GameController/capi-game-controller.md#oh_gamepad_axisevent_getyaxisvalue) (const struct [GamePad\_AxisEvent](../../../模块/GameController/capi-game-controller.md#gamepad_axisevent) \*axisEvent, double \*axisValue) | 从轴事件[GamePad\_AxisEvent](../../../模块/GameController/capi-game-controller.md#gamepad_axisevent)中获取Y轴的轴值。 |
| [GameController\_ErrorCode](../../../模块/GameController/capi-game-controller.md#gamecontroller_errorcode) [OH\_GamePad\_AxisEvent\_GetZAxisValue](../../../模块/GameController/capi-game-controller.md#oh_gamepad_axisevent_getzaxisvalue) (const struct [GamePad\_AxisEvent](../../../模块/GameController/capi-game-controller.md#gamepad_axisevent) \*axisEvent, double \*axisValue) | 从轴事件[GamePad\_AxisEvent](../../../模块/GameController/capi-game-controller.md#gamepad_axisevent)中获取Z轴的轴值。 |
| [GameController\_ErrorCode](../../../模块/GameController/capi-game-controller.md#gamecontroller_errorcode) [OH\_GamePad\_AxisEvent\_GetRZAxisValue](../../../模块/GameController/capi-game-controller.md#oh_gamepad_axisevent_getrzaxisvalue) (const struct [GamePad\_AxisEvent](../../../模块/GameController/capi-game-controller.md#gamepad_axisevent) \*axisEvent, double \*axisValue) | 从轴事件[GamePad\_AxisEvent](../../../模块/GameController/capi-game-controller.md#gamepad_axisevent)中获取RZ轴的轴值。 |
| [GameController\_ErrorCode](../../../模块/GameController/capi-game-controller.md#gamecontroller_errorcode) [OH\_GamePad\_AxisEvent\_GetHatXAxisValue](../../../模块/GameController/capi-game-controller.md#oh_gamepad_axisevent_gethatxaxisvalue) (const struct [GamePad\_AxisEvent](../../../模块/GameController/capi-game-controller.md#gamepad_axisevent) \*axisEvent, double \*axisValue) | 从轴事件[GamePad\_AxisEvent](../../../模块/GameController/capi-game-controller.md#gamepad_axisevent)中获取HatX轴的轴值。 |
| [GameController\_ErrorCode](../../../模块/GameController/capi-game-controller.md#gamecontroller_errorcode) [OH\_GamePad\_AxisEvent\_GetHatYAxisValue](../../../模块/GameController/capi-game-controller.md#oh_gamepad_axisevent_gethatyaxisvalue) (const struct [GamePad\_AxisEvent](../../../模块/GameController/capi-game-controller.md#gamepad_axisevent) \*axisEvent, double \*axisValue) | 从轴事件[GamePad\_AxisEvent](../../../模块/GameController/capi-game-controller.md#gamepad_axisevent)中获取HatY轴的轴值。 |
| [GameController\_ErrorCode](../../../模块/GameController/capi-game-controller.md#gamecontroller_errorcode) [OH\_GamePad\_AxisEvent\_GetBrakeAxisValue](../../../模块/GameController/capi-game-controller.md#oh_gamepad_axisevent_getbrakeaxisvalue) (const struct [GamePad\_AxisEvent](../../../模块/GameController/capi-game-controller.md#gamepad_axisevent) \*axisEvent, double \*axisValue) | 从轴事件[GamePad\_AxisEvent](../../../模块/GameController/capi-game-controller.md#gamepad_axisevent)中获取Brake轴的轴值。 |
| [GameController\_ErrorCode](../../../模块/GameController/capi-game-controller.md#gamecontroller_errorcode) [OH\_GamePad\_AxisEvent\_GetGasAxisValue](../../../模块/GameController/capi-game-controller.md#oh_gamepad_axisevent_getgasaxisvalue) (const struct [GamePad\_AxisEvent](../../../模块/GameController/capi-game-controller.md#gamepad_axisevent) \*axisEvent, double \*axisValue) | 从轴事件[GamePad\_AxisEvent](../../../模块/GameController/capi-game-controller.md#gamepad_axisevent)中获取Gas轴的轴值。 |
| [GameController\_ErrorCode](../../../模块/GameController/capi-game-controller.md#gamecontroller_errorcode) [OH\_GamePad\_AxisEvent\_GetActionTime](../../../模块/GameController/capi-game-controller.md#oh_gamepad_axisevent_getactiontime) (const struct [GamePad\_AxisEvent](../../../模块/GameController/capi-game-controller.md#gamepad_axisevent) \*axisEvent, int64\_t \*actionTime) | 从轴事件[GamePad\_AxisEvent](../../../模块/GameController/capi-game-controller.md#gamepad_axisevent)中获取动作时间。 |
