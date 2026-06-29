---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-nativeanimateapi-1
title: ArkUI_NativeAnimateAPI_1
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > C API > 结构体 > ArkUI_NativeAnimateAPI_1
category: harmonyos-references
scraped_at: 2026-06-11T15:55:21+08:00
doc_updated_at: 2026-06-03
content_hash: sha256:a7e84cabf5192ab0e1e5539f0962fdfa70575a83748727a7a138355a027f832c
---
```
1. typedef struct {...} ArkUI_NativeAnimateAPI_1
```

## 概述

PhonePC/2in1TabletTVWearable

ArkUI提供的Native侧动画接口集合。

**起始版本：** 12

**相关模块：** [ArkUI\_NativeModule](../../模块/ArkUI_NativeModule/capi-arkui-nativemodule.md)

**所在头文件：** [native\_animate.h](../../头文件/native_animate.h/capi-native-animate-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员函数

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| [int32\_t (\*animateTo)(ArkUI\_ContextHandle context, ArkUI\_AnimateOption\* option, ArkUI\_ContextCallback\* update,ArkUI\_AnimateCompleteCallback\* complete)](capi-arkui-nativemodule-arkui-nativeanimateapi-1.md#animateto) | 显式动画接口。 |
| [int32\_t (\*keyframeAnimateTo)(ArkUI\_ContextHandle context, ArkUI\_KeyframeAnimateOption\* option)](capi-arkui-nativemodule-arkui-nativeanimateapi-1.md#keyframeanimateto) | 关键帧动画接口。 |
| [ArkUI\_AnimatorHandle (\*createAnimator)(ArkUI\_ContextHandle context, ArkUI\_AnimatorOption\* option)](capi-arkui-nativemodule-arkui-nativeanimateapi-1.md#createanimator) | 创建animator动画对象。 |
| [void (\*disposeAnimator)(ArkUI\_AnimatorHandle animatorHandle)](capi-arkui-nativemodule-arkui-nativeanimateapi-1.md#disposeanimator) | 销毁animator动画对象。 |

## 成员函数说明

PhonePC/2in1TabletTVWearable

### animateTo()

PhonePC/2in1TabletTVWearable

```
1. int32_t (*animateTo)(ArkUI_ContextHandle context, ArkUI_AnimateOption* option, ArkUI_ContextCallback* update,ArkUI_AnimateCompleteCallback* complete)
```

**描述：**

显式动画接口。

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_ContextHandle](../ArkUI_Context/capi-arkui-nativemodule-arkui-context8h.md) context | UIContext实例。 |
| [ArkUI\_AnimateOption](../ArkUI_AnimateOption/capi-arkui-nativemodule-arkui-animateoption.md)\* option | 设置动画效果相关参数。 |
| [ArkUI\_ContextCallback](../ArkUI_ContextCallback/capi-arkui-nativemodule-arkui-contextcallback.md)\* update | 指定动效的闭包函数，在闭包函数中导致的状态变化系统会自动插入过渡动画。  **说明**：在闭包函数中要设置的组件属性，必须在其之前设置过。 |
| [ArkUI\_AnimateCompleteCallback](../ArkUI_AnimateCompleteCallback/capi-arkui-arkui-animatecompletecallback.md)\* complete | 设置动画播放完成回调参数。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](../../头文件/native_type.h/capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../../头文件/native_type.h/capi-native-type-h.md#arkui_errorcode) 函数参数异常。 |

### keyframeAnimateTo()

PhonePC/2in1TabletTVWearable

```
1. int32_t (*keyframeAnimateTo)(ArkUI_ContextHandle context, ArkUI_KeyframeAnimateOption* option)
```

**描述：**

关键帧动画接口。

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_ContextHandle](../ArkUI_Context/capi-arkui-nativemodule-arkui-context8h.md) context | UIContext实例。 |
| [ArkUI\_KeyframeAnimateOption](../ArkUI_KeyframeAnimateOption/capi-arkui-arkui-keyframeanimateoption.md)\* option | 关键帧动画参数。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](../../头文件/native_type.h/capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../../头文件/native_type.h/capi-native-type-h.md#arkui_errorcode) 函数参数异常。 |

### createAnimator()

PhonePC/2in1TabletTVWearable

```
1. ArkUI_AnimatorHandle (*createAnimator)(ArkUI_ContextHandle context, ArkUI_AnimatorOption* option)
```

**描述：**

创建animator动画对象。

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_ContextHandle](../ArkUI_Context/capi-arkui-nativemodule-arkui-context8h.md) context | UIContext实例。 |
| [ArkUI\_AnimatorOption](../ArkUI_AnimatorOption/capi-arkui-nativemodule-arkui-animatoroption.md)\* option | animator动画参数。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_AnimatorHandle](../ArkUI_Animator/capi-arkui-nativemodule-arkui-animator8h.md) | animator动画对象指针。函数参数异常时返回NULL。 |

### disposeAnimator()

PhonePC/2in1TabletTVWearable

```
1. void (*disposeAnimator)(ArkUI_AnimatorHandle animatorHandle)
```

**描述：**

销毁animator动画对象。

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_AnimatorHandle](../ArkUI_Animator/capi-arkui-nativemodule-arkui-animator8h.md) animatorHandle | animator动画对象。 |
