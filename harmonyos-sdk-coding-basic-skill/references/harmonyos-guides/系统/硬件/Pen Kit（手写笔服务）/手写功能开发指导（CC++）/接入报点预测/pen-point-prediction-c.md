---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/pen-point-prediction-c
title: 接入报点预测
breadcrumb: 指南 > 系统 > 硬件 > Pen Kit（手写笔服务） > 手写功能开发指导（C/C++） > 接入报点预测
category: harmonyos-guides
scraped_at: 2026-06-11T14:51:29+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:9ea9f364ebbf11d480228b69c46d26674ba3f80dada4b2b8ed99258aada1dd1d
---
从6.0.0(20)开始，报点预测新增C API接口。

接入报点预测功能，可以优化应用中手写效果的绘制跟手性，提升应用中手写笔书写场景的跟手体验。

## 场景介绍

在应用的自定义界面中，获取到界面的触摸事件，通过调用报点预测的接口，可以得到预测的下一个报点的位置信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/88/v3/9s4BH5gXRLqulqQNWKOPdQ/zh-cn_image_0000002622858347.png?HW-CC-KV=V1&HW-CC-Date=20260611T065128Z&HW-CC-Expire=86400&HW-CC-Sign=91FA93E470F7C3617C42E84DE333BC203E47A537AF6555A55DD3C4CAB41A97E0)

## 接口说明

| 名称 | 描述 |
| --- | --- |
| int32\_t [HMS\_HandWrite\_GetPredictPoint](<../../../../../../harmonyos-references/Pen Kit（手写笔服务）/C API/模块/HandWrite/pen-handwrite-c.md#hms_handwrite_getpredictpoint>)(const [HandWrite\_HistoricalPoint](<../../../../../../harmonyos-references/硬件/Pen Kit（手写笔服务）/C API/头文件和结构体/结构体/HandWrite_HistoricalPoint/pen-handwrite-struct-historicalpoint.md>) \*event, int32\_t size, float \*predictPointX, float \*predictPointY) | 获取预测点。 |

## 接入步骤

报点预测功能的历史点，通常需要在自定义渲染（XComponent）上注册触摸事件回调获得，请参考[自定义渲染开发指南](<../../../../../应用框架/ArkUI（方舟UI框架）/UI开发 (ArkTS声明式开发范式)/添加组件/自定义渲染 (XComponent)/napi-xcomponent-guidelines.md>)，获得历史触摸点。

### 在CMake脚本中链接动态库

```
1. target_include_directories(entry PUBLIC ${HMOS_SDK_NATIVE}/sysroot/usr/include) # 当编译过程中报点预测头文件缺失时尝试加入此命令
2. target_link_directories(entry PUBLIC ${HMOS_SDK_NATIVE}/sysroot/usr/lib/aarch64-linux-ohos) # 当编译过程中报点预测API链接异常时尝试加入此命令
3. target_link_libraries(entry PUBLIC libace_napi.z.so libhilog_ndk.z.so libhandwrite_ndk.z.so)
```

### 导入模块

```
1. #include <ace/xcomponent/native_interface_xcomponent.h>
2. #include <handwrite/native_handwrite_api.h>
3. #include <hilog/log.h>
```

### 示例代码

[native\_handwrite\_api.h](<../../../../../../harmonyos-references/硬件/Pen Kit（手写笔服务）/C API/头文件和结构体/头文件/native_handwrite_api.h/pen-handwrite-headerfile-declare.md>)提供HMS\_HandWrite\_GetPredictPoint()接口获取预测点。

```
1. #include <ace/xcomponent/native_interface_xcomponent.h>
2. #include <handwrite/native_handwrite_api.h>
3. #include <hilog/log.h>

5. void DispatchTouchEvent(OH_NativeXComponent *xcomponent, void *window)
6. {
7. int32_t historicalPointSize = 0;
8. OH_NativeXComponent_HistoricalPoint *historicalPoints = nullptr;
9. if (OH_NativeXComponent_GetHistoricalPoints(xcomponent, window, &historicalPointSize, &historicalPoints) !=
10. OH_NATIVEXCOMPONENT_RESULT_SUCCESS) {
11. OH_LOG_Print(LOG_APP, LOG_ERROR, 0x0000, "PenKit", "failed to get historical points");
12. return;
13. }

15. std::vector<HandWrite_HistoricalPoint> handWriteHisPoints(historicalPointSize);
16. for (int32_t i = 0; i < historicalPointSize; ++i) {
17. handWriteHisPoints[i].x = historicalPoints[i].x;
18. handWriteHisPoints[i].y = historicalPoints[i].y;
19. handWriteHisPoints[i].timeStamp = historicalPoints[i].timeStamp;
20. handWriteHisPoints[i].force = historicalPoints[i].force;
21. }

23. float predictPointX = 0.0f;
24. float predictPointY = 0.0f;
25. int32_t errcode = HMS_HandWrite_GetPredictPoint(handWriteHisPoints.data(), historicalPointSize, &predictPointX, &predictPointY);

27. OH_LOG_Print(LOG_APP, LOG_INFO, 0x0000, "PenKit", "error code is %{public}d", errcode);
28. OH_LOG_Print(LOG_APP, LOG_INFO, 0x0000, "PenKit", "predict point is (%{public}f, %{public}f)", predictPointX, predictPointY);
29. }
```
