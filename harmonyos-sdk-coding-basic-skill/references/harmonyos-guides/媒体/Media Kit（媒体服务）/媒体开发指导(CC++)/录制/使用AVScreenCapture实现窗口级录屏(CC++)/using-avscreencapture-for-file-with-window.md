---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/using-avscreencapture-for-file-with-window
title: 使用AVScreenCapture实现窗口级录屏(C/C++)
breadcrumb: 指南 > 媒体 > Media Kit（媒体服务） > 媒体开发指导(C/C++) > 录制 > 使用AVScreenCapture实现窗口级录屏(C/C++)
category: harmonyos-guides
scraped_at: 2026-06-01T11:30:45+08:00
doc_updated_at: 2026-05-26
content_hash: sha256:e7ae706d6a02595822d8f14887b5cb0d9f2e49d1518fe55c0b431654d6c40ad4
---
从API version 10开始，开发者可通过AVScreenCapture模块的C API接口实现窗口/屏幕录制，采集麦克风和设备的音视频源数据。

本开发指导以指定窗口录制为例，介绍如何使用AVScreenCapture的C API实现精准窗口捕获。该方案聚焦特定窗口内容，避免全屏干扰，适用于教学演示、在线课程、会议记录及特定内容采集等场景。

* 方式一：录制某个指定窗口，需要设置指定窗口ID。该场景下，启动录屏后，会弹出共享内容选择对话框。详细的API声明请参考[OH\_CaptureMode](<../../../../../../harmonyos-references/Media Kit（媒体服务）/C API/头文件/native_avscreen_capture_base.h/capi-native-avscreen-capture-base-h.md#oh_capturemode>)中的OH\_CAPTURE\_SPECIFIED\_WINDOW模式。
* 方式二（推荐）：使用系统Picker列表弹窗，选择期望录制的窗口。使用[OH\_AVScreenCapture\_StrategyForPickerPopUp](<../../../../../../harmonyos-references/Media Kit（媒体服务）/C API/头文件/native_avscreen_capture.h/capi-native-avscreen-capture-h.md#oh_avscreencapture_strategyforpickerpopup>)设置是否弹出屏幕捕获Picker。从API version 20开始，支持在PC/2in1设备上设置弹出屏幕捕获Picker；从API version 23开始，支持在Phone/Tablet设备上设置弹出屏幕捕获Picker。

## 申请权限

在开发此功能前，开发者应根据实际需求申请相关权限：

* 如果配置了采集麦克风音频数据，需[向用户申请授权](../../../../../系统/安全/程序访问控制/应用权限管控/申请应用权限/向用户申请授权/request-user-authorization.md)配置麦克风权限**ohos.permission.MICROPHONE**和申请[长时任务(ArkTS)](<../../../../../应用框架/Background Tasks Kit（后台任务开发服务）/长时任务(ArkTS)/continuous-task.md>)。
* 从API version 22开始，在PC/2in1设备上对应用进行录屏时，可通过申请权限**ohos.permission.TIMEOUT\_SCREENOFF\_DISABLE\_LOCK**，实现在屏幕熄灭但不锁屏的场景下，继续保持录制的效果。配置方式请参见[声明权限](../../../../../系统/安全/程序访问控制/应用权限管控/申请应用权限/声明权限/declare-permissions.md)。
* 从API version 22开始，在PC/2in1设备上对应用进行录屏时，可通过申请权限**ohos.permission.CUSTOM\_SCREEN\_RECORDING**，实现在录制屏幕时不再弹出隐私警告弹窗。配置方式请参见[受限开放权限](../../../../../系统/安全/程序访问控制/应用权限管控/应用权限列表/受限开放权限/restricted-permissions.md)。

## 开发步骤及注意事项

**在CMake脚本中链接动态库**

```
1. target_link_libraries(entry PUBLIC libnative_avscreen_capture.so)
```

1. 添加头文件。

   ```
   1. #include "napi/native_api.h"
   2. #include <multimedia/player_framework/native_avscreen_capture.h>
   3. #include <multimedia/player_framework/native_avscreen_capture_base.h>
   4. #include <multimedia/player_framework/native_avbuffer.h>
   5. #include <multimedia/player_framework/native_avscreen_capture_errors.h>
   6. #include "hilog/log.h"
   7. #include <unistd.h>
   8. #include <fcntl.h>
   9. #include <string>
   ```

   [main.h](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/Media/ScreenCapture/ScreenCaptureSample/entry/src/main/cpp/main.h#L19-L29)
2. 调用[OH\_AVScreenCapture\_Create](<../../../../../../harmonyos-references/Media Kit（媒体服务）/C API/头文件/native_avscreen_capture.h/capi-native-avscreen-capture-h.md#oh_avscreencapture_create>)方法创建AVScreenCapture实例capture。

   ```
   1. g_avCapture = OH_AVScreenCapture_Create();
   ```

   [napi\_init.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/Media/ScreenCapture/ScreenCaptureSample/entry/src/main/cpp/napi_init.cpp#L472-L474)
3. 调用[OH\_AVScreenCapture\_Init](<../../../../../../harmonyos-references/Media Kit（媒体服务）/C API/头文件/native_avscreen_capture.h/capi-native-avscreen-capture-h.md#oh_avscreencapture_init>)方法配置屏幕录制参数。

   创建AVScreenCapture实例capture后，可以设置屏幕录制所需要的参数。

   ```
   1. void SetConfig(OH_AVScreenCaptureConfig &config)
   2. {
   3. OH_AudioCaptureInfo micCapInfo = {
   4. .audioSampleRate = 48000,
   5. .audioChannels = 2,
   6. .audioSource = OH_MIC
   7. };

   9. OH_AudioCaptureInfo innerCapInfo = {
   10. .audioSampleRate = 48000,
   11. .audioChannels = 2,
   12. .audioSource = OH_ALL_PLAYBACK
   13. };

   15. OH_AudioEncInfo audioEncInfo = {
   16. .audioBitrate = 48000,
   17. .audioCodecformat = OH_AAC_LC
   18. };

   20. OH_VideoCaptureInfo videoCapInfo = {
   21. .videoFrameWidth = 720,
   22. .videoFrameHeight = 1280,
   23. .videoSource = OH_VIDEO_SOURCE_SURFACE_RGBA
   24. };

   26. OH_VideoEncInfo videoEncInfo = {
   27. .videoCodec = OH_H264,
   28. .videoBitrate = 2000000,
   29. .videoFrameRate = 30
   30. };

   32. OH_AudioInfo audioInfo = {
   33. .micCapInfo = micCapInfo,
   34. .innerCapInfo = innerCapInfo,
   35. .audioEncInfo = audioEncInfo
   36. };

   38. OH_VideoInfo videoInfo = {
   39. .videoCapInfo = videoCapInfo,
   40. .videoEncInfo = videoEncInfo
   41. };

   43. config = {
   44. .captureMode = OH_CAPTURE_HOME_SCREEN,
   45. .dataType = OH_ORIGINAL_STREAM, // 录屏数据类型，原始码流或文件
   46. .audioInfo = audioInfo,
   47. .videoInfo = videoInfo
   48. };
   49. }
   ```

   [napi\_init.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/Media/ScreenCapture/ScreenCaptureSample/entry/src/main/cpp/napi_init.cpp#L63-L113)

   方式一：需传入期望录制的窗口ID进行录屏。

   ```
   1. // 如果期望录制单个窗口，需传入单个窗口ID；如果期望同时录制多个窗口，需传入期望录制的窗口ID列表。
   2. std::vector<int32_t> missionIds = {88}; // 指定录制的窗口ID。
   3. config.videoInfo.videoCapInfo.missionIDs = missionIds.data();
   4. config.videoInfo.videoCapInfo.missionIDsLen = static_cast<int32_t>(missionIds.size());
   5. config.captureMode = OH_CAPTURE_SPECIFIED_WINDOW; // 设置录屏模式为录制指定窗口。

   7. // 设置为false，代表录屏启动后不弹出系统Picker，弹出隐私提示弹窗。
   8. OH_AVScreenCapture_CaptureStrategy* strategy = OH_AVScreenCapture_CreateCaptureStrategy();
   9. OH_AVScreenCapture_StrategyForPickerPopUp(strategy, false);
   10. OH_AVScreenCapture_SetCaptureStrategy(capture, strategy);
   ```

   方式二（推荐）：通过弹出屏幕捕获Picker列表方式，选择已打开的应用窗口进行窗口级录屏。

   ```
   1. // 通过弹出屏幕捕获Picker列表方式，选择已打开的应用窗口进行窗口级录屏。
   2. OH_AVScreenCapture_CaptureStrategy *strategy = OH_AVScreenCapture_CreateCaptureStrategy();
   3. OH_AVScreenCapture_StrategyForPickerPopUp(strategy, true);
   4. OH_AVScreenCapture_SetCaptureStrategy(g_avCapture, strategy);
   ```

   [napi\_init.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/Media/ScreenCapture/ScreenCaptureSample/entry/src/main/cpp/napi_init.cpp#L495-L500)
4. 调用[OH\_AVScreenCapture\_StartScreenRecording](<../../../../../../harmonyos-references/Media Kit（媒体服务）/C API/头文件/native_avscreen_capture.h/capi-native-avscreen-capture-h.md#oh_avscreencapture_startscreenrecording>)方法开始进行窗口级录制。

   ```
   1. result = OH_AVScreenCapture_StartScreenRecording(g_avCapture);
   ```

   [napi\_init.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/Media/ScreenCapture/ScreenCaptureSample/entry/src/main/cpp/napi_init.cpp#L511-L513)
5. 调用[OH\_AVScreenCapture\_StopScreenRecording](<../../../../../../harmonyos-references/Media Kit（媒体服务）/C API/头文件/native_avscreen_capture.h/capi-native-avscreen-capture-h.md#oh_avscreencapture_stopscreenrecording>)方法停止录制。

   ```
   1. result = OH_AVScreenCapture_StopScreenRecording(g_avCapture);
   ```

   [napi\_init.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/Media/ScreenCapture/ScreenCaptureSample/entry/src/main/cpp/napi_init.cpp#L551-L553)
6. 调用[OH\_AVScreenCapture\_Release](<../../../../../../harmonyos-references/Media Kit（媒体服务）/C API/头文件/native_avscreen_capture.h/capi-native-avscreen-capture-h.md#oh_avscreencapture_release>)方法销毁实例，释放资源。

   ```
   1. OH_AVScreenCapture_Release(g_avCapture);
   2. g_avCapture = nullptr;
   ```

   [napi\_init.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/Media/ScreenCapture/ScreenCaptureSample/entry/src/main/cpp/napi_init.cpp#L516-L519)
