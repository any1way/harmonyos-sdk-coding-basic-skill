---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ability-resource-info-h
title: ability_resource_info.h
breadcrumb: API参考 > 应用框架 > Ability Kit（程序框架服务） > C API > 头文件 > ability_resource_info.h
category: harmonyos-references
scraped_at: 2026-06-11T15:37:03+08:00
doc_updated_at: 2026-06-03
content_hash: sha256:fde14584a12885effc4eb7d916646f2c9234b8e34c6d5815b1f660ea925e7ced
---
## 概述

PhonePC/2in1TabletTVWearable

提供组件资源信息的接口，用于获取组件的以下信息：包名、模块名、组件名、图标、分身索引、是否为默认应用等。

**引用文件：** <bundle/ability\_resource\_info.h>

**库：** libbundle\_ndk.z.so

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**起始版本：** 21

**相关模块：** [Native\_Bundle](../../模块/Native_Bundle/capi-native-bundle.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 结构体

PhonePC/2in1TabletTVWearable

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [OH\_NativeBundle\_AbilityResourceInfo](../../结构体/OH_NativeBundle_AbilityResourceInfo/capi-native-bundle-abilityresourceinfo.md) | OH\_NativeBundle\_AbilityResourceInfo | 表示组件资源信息。 |

### 函数

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| [BundleManager\_ErrorCode OH\_NativeBundle\_GetBundleName(OH\_NativeBundle\_AbilityResourceInfo\* abilityResourceInfo, char\*\* bundleName)](capi-ability-resource-info-h.md#oh_nativebundle_getbundlename) | 获取组件的包名。在使用该接口之后，为了防止内存泄漏，需要手动释放接口返回的指针。 |
| [BundleManager\_ErrorCode OH\_NativeBundle\_GetModuleName(OH\_NativeBundle\_AbilityResourceInfo\* abilityResourceInfo, char\*\* moduleName)](capi-ability-resource-info-h.md#oh_nativebundle_getmodulename) | 获取组件的模块名。在使用该接口之后，为了防止内存泄漏，需要手动释放接口返回的指针。 |
| [BundleManager\_ErrorCode OH\_NativeBundle\_GetAbilityName(OH\_NativeBundle\_AbilityResourceInfo\* abilityResourceInfo, char\*\* abilityName)](capi-ability-resource-info-h.md#oh_nativebundle_getabilityname) | 获取组件名。在使用该接口之后，为了防止内存泄漏，需要手动释放接口返回的指针。 |
| [BundleManager\_ErrorCode OH\_NativeBundle\_GetDrawableDescriptor(OH\_NativeBundle\_AbilityResourceInfo\* abilityResourceInfo, ArkUI\_DrawableDescriptor\*\* drawableIcon)](capi-ability-resource-info-h.md#oh_nativebundle_getdrawabledescriptor) | 获取组件图标资源对应的[DrawableDescriptor](<../../../../ArkUI（方舟UI框架）/C API/结构体/ArkUI_DrawableDescriptor/capi-arkui-nativemodule-arkui-drawabledescriptor.md>)对象。在使用该接口之后，为了防止内存泄漏，需要手动调用[OH\_AbilityResourceInfo\_Destroy](capi-ability-resource-info-h.md#oh_abilityresourceinfo_destroy)释放接口返回的指针。 |
| [BundleManager\_ErrorCode OH\_NativeBundle\_GetLabel(OH\_NativeBundle\_AbilityResourceInfo\* abilityResourceInfo, char\*\* label)](capi-ability-resource-info-h.md#oh_nativebundle_getlabel) | 获取组件的应用名称。在使用该接口之后，为了防止内存泄漏，需要手动释放接口返回的指针。 |
| [BundleManager\_ErrorCode OH\_NativeBundle\_GetAppIndex(OH\_NativeBundle\_AbilityResourceInfo\* abilityResourceInfo, int\* appIndex)](capi-ability-resource-info-h.md#oh_nativebundle_getappindex) | 获取组件的分身索引。 |
| [BundleManager\_ErrorCode OH\_NativeBundle\_CheckDefaultApp(OH\_NativeBundle\_AbilityResourceInfo\* abilityResourceInfo, bool\* isDefault)](capi-ability-resource-info-h.md#oh_nativebundle_checkdefaultapp) | 查询组件所属的应用是否为默认应用。 |
| [BundleManager\_ErrorCode OH\_AbilityResourceInfo\_Destroy(OH\_NativeBundle\_AbilityResourceInfo\* abilityResourceInfo, size\_t count)](capi-ability-resource-info-h.md#oh_abilityresourceinfo_destroy) | 该接口应在对[OH\_NativeBundle\_GetAbilityResourceInfo](../native_interface_bundle.h/capi-native-interface-bundle-h.md#oh_nativebundle_getabilityresourceinfo)的使用完成后调用，以避免内存泄漏。 |
| [int OH\_NativeBundle\_GetSize()](capi-ability-resource-info-h.md#oh_nativebundle_getsize) | 获取单个结构体[OH\_NativeBundle\_AbilityResourceInfo](../../结构体/OH_NativeBundle_AbilityResourceInfo/capi-native-bundle-abilityresourceinfo.md)的大小。 |

## 函数说明

PhonePC/2in1TabletTVWearable

### OH\_NativeBundle\_GetBundleName()

PhonePC/2in1TabletTVWearable

```
1. BundleManager_ErrorCode OH_NativeBundle_GetBundleName(OH_NativeBundle_AbilityResourceInfo* abilityResourceInfo, char** bundleName)
```

**描述**

获取组件的包名。在使用该接口之后，为了防止内存泄漏，需要手动释放接口返回的指针。

**起始版本：** 21

**参数：**

| 参数项 | 描述 |
| --- | --- |
| OH\_NativeBundle\_AbilityResourceInfo\* abilityResourceInfo | 指定组件资源信息。 |
| char\*\* bundleName | 获取的包名。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [BundleManager\_ErrorCode](../bundle_manager_common.h/capi-bundle-manager-common-h.md#bundlemanager_errorcode) | 执行结果。  如果获取成功，返回[BUNDLE\_MANAGER\_ERROR\_CODE\_NO\_ERROR](../bundle_manager_common.h/capi-bundle-manager-common-h.md#bundlemanager_errorcode)。  如果获取失败，返回[BUNDLE\_MANAGER\_ERROR\_CODE\_PARAM\_INVALID](../bundle_manager_common.h/capi-bundle-manager-common-h.md#bundlemanager_errorcode)，这是由于abilityResourceInfo为空指针所致。 |

### OH\_NativeBundle\_GetModuleName()

PhonePC/2in1TabletTVWearable

```
1. BundleManager_ErrorCode OH_NativeBundle_GetModuleName(OH_NativeBundle_AbilityResourceInfo* abilityResourceInfo, char** moduleName)
```

**描述**

获取组件的模块名。在使用该接口之后，为了防止内存泄漏，需要手动释放接口返回的指针。

**起始版本：** 21

**参数：**

| 参数项 | 描述 |
| --- | --- |
| OH\_NativeBundle\_AbilityResourceInfo\* abilityResourceInfo | 指定组件资源信息。 |
| char\*\* moduleName | 获取的模块名。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [BundleManager\_ErrorCode](../bundle_manager_common.h/capi-bundle-manager-common-h.md#bundlemanager_errorcode) | 执行结果。  如果获取成功，返回[BUNDLE\_MANAGER\_ERROR\_CODE\_NO\_ERROR](../bundle_manager_common.h/capi-bundle-manager-common-h.md#bundlemanager_errorcode)。  如果获取失败，返回[BUNDLE\_MANAGER\_ERROR\_CODE\_PARAM\_INVALID](../bundle_manager_common.h/capi-bundle-manager-common-h.md#bundlemanager_errorcode)，这是由于abilityResourceInfo为空指针所致。 |

### OH\_NativeBundle\_GetAbilityName()

PhonePC/2in1TabletTVWearable

```
1. BundleManager_ErrorCode OH_NativeBundle_GetAbilityName(OH_NativeBundle_AbilityResourceInfo* abilityResourceInfo, char** abilityName)
```

**描述**

获取组件名。在使用该接口之后，为了防止内存泄漏，需要手动释放接口返回的指针。

**起始版本：** 21

**参数：**

| 参数项 | 描述 |
| --- | --- |
| OH\_NativeBundle\_AbilityResourceInfo\* abilityResourceInfo | 指定组件资源信息。 |
| char\*\* abilityName | 获取的组件名。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [BundleManager\_ErrorCode](../bundle_manager_common.h/capi-bundle-manager-common-h.md#bundlemanager_errorcode) | 执行结果。  如果获取成功，返回[BUNDLE\_MANAGER\_ERROR\_CODE\_NO\_ERROR](../bundle_manager_common.h/capi-bundle-manager-common-h.md#bundlemanager_errorcode)。  如果获取失败，返回[BUNDLE\_MANAGER\_ERROR\_CODE\_PARAM\_INVALID](../bundle_manager_common.h/capi-bundle-manager-common-h.md#bundlemanager_errorcode)，这是由于abilityResourceInfo为空指针所致。 |

### OH\_NativeBundle\_GetDrawableDescriptor()

PhonePC/2in1TabletTVWearable

```
1. BundleManager_ErrorCode OH_NativeBundle_GetDrawableDescriptor(OH_NativeBundle_AbilityResourceInfo* abilityResourceInfo, ArkUI_DrawableDescriptor** drawableIcon)
```

**描述**

获取组件图标资源对应的[DrawableDescriptor](<../../../../ArkUI（方舟UI框架）/C API/结构体/ArkUI_DrawableDescriptor/capi-arkui-nativemodule-arkui-drawabledescriptor.md>)对象。在使用该接口之后，为了防止内存泄漏，需要手动调用[OH\_AbilityResourceInfo\_Destroy](capi-ability-resource-info-h.md#oh_abilityresourceinfo_destroy)释放接口返回的指针。

**起始版本：** 21

**参数：**

| 参数项 | 描述 |
| --- | --- |
| OH\_NativeBundle\_AbilityResourceInfo\* abilityResourceInfo | 指定组件资源信息。 |
| ArkUI\_DrawableDescriptor\*\* drawableIcon | 组件图标资源对应的[DrawableDescriptor](<../../../../ArkUI（方舟UI框架）/C API/结构体/ArkUI_DrawableDescriptor/capi-arkui-nativemodule-arkui-drawabledescriptor.md>)对象。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [BundleManager\_ErrorCode](../bundle_manager_common.h/capi-bundle-manager-common-h.md#bundlemanager_errorcode) | 执行结果。  如果获取成功，返回[BUNDLE\_MANAGER\_ERROR\_CODE\_NO\_ERROR](../bundle_manager_common.h/capi-bundle-manager-common-h.md#bundlemanager_errorcode)。  如果获取失败，返回[BUNDLE\_MANAGER\_ERROR\_CODE\_PARAM\_INVALID](../bundle_manager_common.h/capi-bundle-manager-common-h.md#bundlemanager_errorcode)，这是由于abilityResourceInfo为空指针所致。 |

### OH\_NativeBundle\_GetLabel()

PhonePC/2in1TabletTVWearable

```
1. BundleManager_ErrorCode OH_NativeBundle_GetLabel(OH_NativeBundle_AbilityResourceInfo* abilityResourceInfo, char** label)
```

**描述**

获取组件的应用名称。在使用该接口之后，为了防止内存泄漏，需要手动释放接口返回的指针。

**起始版本：** 21

**参数：**

| 参数项 | 描述 |
| --- | --- |
| OH\_NativeBundle\_AbilityResourceInfo\* abilityResourceInfo | 指定组件资源信息。 |
| char\*\* label | 获取的应用名称。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [BundleManager\_ErrorCode](../bundle_manager_common.h/capi-bundle-manager-common-h.md#bundlemanager_errorcode) | 执行结果。  如果获取成功，返回[BUNDLE\_MANAGER\_ERROR\_CODE\_NO\_ERROR](../bundle_manager_common.h/capi-bundle-manager-common-h.md#bundlemanager_errorcode)。  如果获取失败，返回[BUNDLE\_MANAGER\_ERROR\_CODE\_PARAM\_INVALID](../bundle_manager_common.h/capi-bundle-manager-common-h.md#bundlemanager_errorcode)，这是由于abilityResourceInfo为空指针所致。 |

### OH\_NativeBundle\_GetAppIndex()

PhonePC/2in1TabletTVWearable

```
1. BundleManager_ErrorCode OH_NativeBundle_GetAppIndex(OH_NativeBundle_AbilityResourceInfo* abilityResourceInfo, int* appIndex)
```

**描述**

获取组件的分身索引。

**起始版本：** 21

**参数：**

| 参数项 | 描述 |
| --- | --- |
| OH\_NativeBundle\_AbilityResourceInfo\* abilityResourceInfo | 指定组件资源信息。 |
| int\* appIndex | 获取的分身索引。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [BundleManager\_ErrorCode](../bundle_manager_common.h/capi-bundle-manager-common-h.md#bundlemanager_errorcode) | 执行结果。  如果获取成功，返回[BUNDLE\_MANAGER\_ERROR\_CODE\_NO\_ERROR](../bundle_manager_common.h/capi-bundle-manager-common-h.md#bundlemanager_errorcode)。  如果获取失败，返回[BUNDLE\_MANAGER\_ERROR\_CODE\_PARAM\_INVALID](../bundle_manager_common.h/capi-bundle-manager-common-h.md#bundlemanager_errorcode)，这是由于abilityResourceInfo为空指针所致。 |

### OH\_NativeBundle\_CheckDefaultApp()

PhonePC/2in1TabletTVWearable

```
1. BundleManager_ErrorCode OH_NativeBundle_CheckDefaultApp(OH_NativeBundle_AbilityResourceInfo* abilityResourceInfo, bool* isDefault)
```

**描述**

查询组件所属的应用是否为默认应用。

**起始版本：** 21

**参数：**

| 参数项 | 描述 |
| --- | --- |
| OH\_NativeBundle\_AbilityResourceInfo\* abilityResourceInfo | 指定组件资源信息。 |
| bool\* isDefault | 组件所属的应用是否为默认应用，默认应用是指用户为特定文件类型或操作设定的首选应用。取值true为默认应用，false为非默认应用。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [BundleManager\_ErrorCode](../bundle_manager_common.h/capi-bundle-manager-common-h.md#bundlemanager_errorcode) | 执行结果。  如果查询成功，返回[BUNDLE\_MANAGER\_ERROR\_CODE\_NO\_ERROR](../bundle_manager_common.h/capi-bundle-manager-common-h.md#bundlemanager_errorcode)。  如果查询失败，返回[BUNDLE\_MANAGER\_ERROR\_CODE\_PARAM\_INVALID](../bundle_manager_common.h/capi-bundle-manager-common-h.md#bundlemanager_errorcode)，这是由于abilityResourceInfo为空指针所致。 |

### OH\_AbilityResourceInfo\_Destroy()

PhonePC/2in1TabletTVWearable

```
1. BundleManager_ErrorCode OH_AbilityResourceInfo_Destroy(OH_NativeBundle_AbilityResourceInfo* abilityResourceInfo, size_t count)
```

**描述**

释放组件资源信息的内存。

**起始版本：** 21

**参数：**

| 参数项 | 描述 |
| --- | --- |
| OH\_NativeBundle\_AbilityResourceInfo\* abilityResourceInfo | 要释放的组件资源信息。 |
| size\_t count | 表示组件资源信息数组的大小。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [BundleManager\_ErrorCode](../bundle_manager_common.h/capi-bundle-manager-common-h.md#bundlemanager_errorcode) | 执行结果。  如果释放成功，返回[BUNDLE\_MANAGER\_ERROR\_CODE\_NO\_ERROR](../bundle_manager_common.h/capi-bundle-manager-common-h.md#bundlemanager_errorcode)。  如果释放失败，返回[BUNDLE\_MANAGER\_ERROR\_CODE\_PARAM\_INVALID](../bundle_manager_common.h/capi-bundle-manager-common-h.md#bundlemanager_errorcode)，这是由于abilityResourceInfo为空指针所致。 |

### OH\_NativeBundle\_GetSize()

PhonePC/2in1TabletTVWearable

```
1. int OH_NativeBundle_GetSize()
```

**描述**

获取单个结构体[OH\_NativeBundle\_AbilityResourceInfo](../../结构体/OH_NativeBundle_AbilityResourceInfo/capi-native-bundle-abilityresourceinfo.md)的大小。

**起始版本：** 21

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 返回单个结构体[OH\_NativeBundle\_AbilityResourceInfo](../../结构体/OH_NativeBundle_AbilityResourceInfo/capi-native-bundle-abilityresourceinfo.md)的大小。 |
