---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ndk-navigation-query
title: 使用导航类组件
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (基于NDK构建UI) > 使用导航类组件
category: harmonyos-guides
scraped_at: 2026-06-01T11:07:06+08:00
doc_updated_at: 2026-05-28
content_hash: sha256:0f92d1afd707bbdd4d889f0b643cd5d0d842a68f0ba9fa1272be05772d8f3907
---
NDK提供一系列[Navigation](<../../UI开发 (ArkTS声明式开发范式)/设置组件导航和页面路由/组件导航(Navigation) (推荐)/Navigation基础架构介绍/arkts-navigation-architecture.md#navigation整体架构>)和[页面路由](<../../UI开发 (ArkTS声明式开发范式)/设置组件导航和页面路由/页面路由 (@ohos.router)(不推荐)/arkts-routing.md>)状态查询接口，开发者可以通过[OH\_ArkUI\_GetNavDestinationName](<../../../../../harmonyos-references/ArkUI（方舟UI框架）/C API/头文件/native_node_napi.h/capi-native-node-napi-h.md#oh_arkui_getnavdestinationname>)、[OH\_ArkUI\_GetNavDestinationParam](<../../../../../harmonyos-references/ArkUI（方舟UI框架）/C API/头文件/native_node_napi.h/capi-native-node-napi-h.md#oh_arkui_getnavdestinationparam>)、[OH\_ArkUI\_GetNavDestinationState](<../../../../../harmonyos-references/ArkUI（方舟UI框架）/C API/头文件/native_node_napi.h/capi-native-node-napi-h.md#oh_arkui_getnavdestinationstate>)、[OH\_ArkUI\_GetNavigationId](<../../../../../harmonyos-references/ArkUI（方舟UI框架）/C API/头文件/native_node_napi.h/capi-native-node-napi-h.md#oh_arkui_getnavigationid>)、[OH\_ArkUI\_GetNavDestinationIndex](<../../../../../harmonyos-references/ArkUI（方舟UI框架）/C API/头文件/native_node_napi.h/capi-native-node-napi-h.md#oh_arkui_getnavdestinationindex>)等查询页面的状态、索引、名称等信息，并根据查询结果进行对应的操作，如显示不同的页面信息。

本文提供页面状态查询开发指导，查询之前需要先接入ArkTS页面，具体请参考[接入ArkTS页面](../接入ArkTS页面/ndk-access-the-arkts-page.md)。

## 查询页面信息

查询页面信息，需要先确保目标节点已作为子节点挂载到页面中，若节点未挂载则操作会失败，例如在[aboutToAppear](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/自定义组件/自定义组件的生命周期/ts-custom-component-lifecycle.md#abouttoappear)生命周期中查询不到对应信息。页面详细生命周期以及组件挂载生命周期参考[页面生命周期](<../../UI开发 (ArkTS声明式开发范式)/设置组件导航和页面路由/组件导航(Navigation) (推荐)/Navigation子页面/arkts-navigation-navdestination.md#页面生命周期>)。开发者可以根据查询到的页面信息加载不同的页面组件。

本示例仅展示核心功能代码，完整示例请参考[NDK使用页面查询接口示例](https://gitcode.com/HarmonyOS_Samples/guide-snippets/tree/master/ArkUISample/NDKNavigation)。

1. 查询当前页面名称。

   使用[OH\_ArkUI\_GetNavDestinationName](<../../../../../harmonyos-references/ArkUI（方舟UI框架）/C API/头文件/native_node_napi.h/capi-native-node-napi-h.md#oh_arkui_getnavdestinationname>)可以查询NavDestination页面名称。router页面名称可以通过[OH\_ArkUI\_GetRouterPageName](<../../../../../harmonyos-references/ArkUI（方舟UI框架）/C API/头文件/native_node_napi.h/capi-native-node-napi-h.md#oh_arkui_getrouterpagename>)接口查询。

   ```
   1. // 获取页面名称
   2. char pageName[NUM_50];
   3. int32_t bufferLen = 0;
   4. OH_ArkUI_GetNavDestinationName(node, pageName, NUM_50, &bufferLen);
   ```

   [QueryNavigation.h](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkUISample/NDKNavigation/entry/src/main/cpp/QueryNavigation.h#L82-L87)
2. 查询页面跳转参数。

   使用[OH\_ArkUI\_GetNavDestinationParam](<../../../../../harmonyos-references/ArkUI（方舟UI框架）/C API/头文件/native_node_napi.h/capi-native-node-napi-h.md#oh_arkui_getnavdestinationparam>)可以查询[NavDestination](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/导航与切换/NavDestination/ts-basic-components-navdestination.md)页面跳转参数。

   ```
   1. // 获取页面跳转参数
   2. napi_value param = OH_ArkUI_GetNavDestinationParam(node);
   3. napi_value nameVal = nullptr;
   4. napi_get_named_property(env, param, "name", &nameVal);
   5. size_t len = 0;
   6. napi_get_value_string_utf8(env, nameVal, nullptr, 0, &len);
   7. std::unique_ptr<char[]> viewName = std::make_unique<char[]>(len + 1);
   8. napi_get_value_string_utf8(env, nameVal, viewName.get(), len + 1, &len);
   9. ArkUI_NodeHandle targetNode = nullptr;
   10. std::string view = viewName.get();
   11. if (view == "QueryNavigation") {
   12. InitNavigationNode(column, pageName);
   13. } else if (view == "QueryRouter") {
   14. InitRouterNode(column);
   15. }
   16. nativeApi->addChild(node, column);
   ```

   [QueryNavigation.h](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkUISample/NDKNavigation/entry/src/main/cpp/QueryNavigation.h#L88-L105)

## 查询页面状态

使用[OH\_ArkUI\_GetNavDestinationState](<../../../../../harmonyos-references/ArkUI（方舟UI框架）/C API/头文件/native_node_napi.h/capi-native-node-napi-h.md#oh_arkui_getnavdestinationstate>)可以查询当前占位组件所属的NavDestination页面状态。router页面可以通过[OH\_ArkUI\_GetRouterPageState](<../../../../../harmonyos-references/ArkUI（方舟UI框架）/C API/头文件/native_node_napi.h/capi-native-node-napi-h.md#oh_arkui_getrouterpagestate>)接口查询，根据查询结果进行对应的适配，如设置组件visible属性、视频播放状态。

本示例仅展示核心功能代码，完整示例请参考[NDK使用页面查询接口示例](https://gitcode.com/HarmonyOS_Samples/guide-snippets/tree/master/ArkUISample/NDKNavigation)。

```
1. ArkUI_NodeHandle targetNode = nullptr;
2. OH_ArkUI_NodeUtils_GetAttachedNodeHandleById("navDestinationState", &targetNode);
3. auto entry = NativeEntry::GetInstance();
4. entry->ReportError(targetNode, "event clicked");
5. ArkUI_NavDestinationState state;
6. OH_ArkUI_GetNavDestinationState(targetNode, &state);
7. if (state == NUM_8) {
8. entry->SetColor(targetNode, 0x80808080);
9. } else if (state == NUM_9) {
10. entry->SetColor(targetNode, 0xFF000000);
11. }
```

[EntryModule.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkUISample/NDKNavigation/entry/src/main/cpp/EntryModule.cpp#L70-L82)

## 查询页面栈信息

使用[OH\_ArkUI\_GetNavDestinationIndex](<../../../../../harmonyos-references/ArkUI（方舟UI框架）/C API/头文件/native_node_napi.h/capi-native-node-napi-h.md#oh_arkui_getnavdestinationindex>)可以查询当前占位组件所属NavDestination在栈中的位置。router页面状态可以通过[OH\_ArkUI\_GetRouterPageIndex](<../../../../../harmonyos-references/ArkUI（方舟UI框架）/C API/头文件/native_node_napi.h/capi-native-node-napi-h.md#oh_arkui_getrouterpageindex>)接口查询。根据返回的页面栈信息，可在应用开发中实现DFX功能，例如性能监控与用户行为分析等参数的收集，用于数据上报和分析。

本示例仅展示核心功能代码，完整示例请参考[NDK使用页面查询接口示例](https://gitcode.com/HarmonyOS_Samples/guide-snippets/tree/master/ArkUISample/NDKNavigation)。

```
1. char navigationId[NUM_50];
2. int32_t bufferLen = 0;
3. OH_ArkUI_GetNavigationId(handle, navigationId, NUM_50, &bufferLen);

5. char name[NUM_50];
6. int32_t nameLen = OH_ArkUI_GetNavDestinationName(handle, name, NUM_50, &nameLen);

8. int32_t index = -1;
9. OH_ArkUI_GetNavDestinationIndex(handle, &index);
10. OH_LOG_Print(LOG_APP, LOG_ERROR, 0xFF00, "NAPI",
11. "navigation id: %{public}s, name: %{public}s, index: %{public}d, error: %{public}s",
12. navigationId, name, index, info.c_str());
```

[EntryModule.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkUISample/NDKNavigation/entry/src/main/cpp/EntryModule.cpp#L88-L101)
