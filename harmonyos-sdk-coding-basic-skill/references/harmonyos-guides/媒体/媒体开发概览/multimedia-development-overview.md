---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/multimedia-development-overview
title: 媒体开发概览
breadcrumb: 指南 > 媒体 > 媒体开发概览
category: harmonyos-guides
scraped_at: 2026-06-11T14:53:33+08:00
doc_updated_at: 2026-05-26
content_hash: sha256:a59ba53e33526cf0451c4dfeea0904adea555656587fc95ea357bc25b37bd750
---
HarmonyOS提供丰富的一站式媒体业务开放能力，开发者能够在系统上快速开发主流的媒体业务，满足常规高频使用场景，并提供优秀的性能表现。

## 媒体系统架构

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/47/v3/sxNGrkEJS4izJTCN63LoCg/zh-cn_image_0000002622698517.png?HW-CC-KV=V1&HW-CC-Date=20260611T065332Z&HW-CC-Expire=86400&HW-CC-Sign=4E0260C96661DD0A7364AA82A8CF03A42A96D86AD6F6D8B17B7DB8281A6C4F7B)

媒体系统架构提供用户视觉、听觉信息的处理能力，例如音视频信息的采集、编码存储、解码播放等。操作系统实现中，根据不同的媒体信息处理内容，将媒体划分为不同的模块，包括音频、视频、图片等。

媒体系统面向应用开发提供音视频应用、图库应用、相机应用的编程框架接口；面向设备开发提供对接不同硬件芯片的适配加速功能；中间以服务形式提供媒体核心功能和管理机制。

* 音频服务（Audio Kit）：提供场景化音频播放和录制接口，助力开发者快速构建音频高清采集及沉浸式播放能力。
* 音视频编解码服务（AVCodec Kit）：提供音视频编解码、媒体文件解析、封装及媒体数据输入等原子能力。
* 音视频播控服务（AVSession Kit）：提供系统级音视频管控服务，统一管理系统中所有音视频行为。
* 相机服务（Camera Kit）：提供场景化相机控制管理接口，实现预览图像显示、拍照图片保存及视频录制功能。
* 数字版权保护服务（DRM Kit）：提供DRM加密音视频解密，支持设备DRM证书管理、许可证管理及内容解密功能。
* 图片处理服务（Image Kit）：提供全面图片处理能力，帮助开发者实现图片的解码、编码、编辑、元数据处理和图片接收等功能。
* 媒体服务（Media Kit）：提供端到端播放原始媒体资源，音视频录制与屏幕录制，获取媒体资源元数据、缩略图，视频转码等功能。
* 媒体文件管理服务（Media Library Kit）：提供管理相册和媒体文件的能力，包括照片和视频。
* 铃声服务（Ringtone Kit）：提供铃声设置功能，为用户提供简单一致、安全高品质的铃声设置体验。
* 统一扫码服务（Scan Kit）：提供系统级的扫码服务。

## 媒体应用开发综述

### 相机预览

相机预览是启动相机后实时的图像显示，通常在拍照和录像前执行。

**指南**

* [预览(ArkTS)](<../Camera Kit（相机服务）/开发相机应用基础能力(ArkTS)/预览(ArkTS)/camera-preview.md>)
* [双路预览(ArkTS)](<../Camera Kit（相机服务）/开发相机应用基础能力(ArkTS)/双路预览(ArkTS)/camera-dual-channel-preview.md>)
* [动态调整预览帧率(ArkTS)](<../Camera Kit（相机服务）/开发相机应用基础能力(ArkTS)/动态调整预览帧率(ArkTS)/camera-framerate.md>)
* [适配相机旋转角度(ArkTS)](<../Camera Kit（相机服务）/开发相机应用基础能力(ArkTS)/相机旋转/适配相机旋转角度(ArkTS)/camera-rotation-angle-adaptation.md>)
* [预览(C/C++)](<../Camera Kit（相机服务）/开发相机应用基础能力(CC++)/预览(CC++)/native-camera-preview.md>)
* [预览流二次处理(C/C++)](<../Camera Kit（相机服务）/开发相机应用基础能力(CC++)/预览流二次处理(CC++)/native-camera-preview-imagereceiver.md>)
* [动态调整预览帧率(C/C++)](<../Camera Kit（相机服务）/开发相机应用基础能力(CC++)/动态调整预览帧率(CC++)/camera-setframerate-native.md>)
* [适配相机旋转角度(C/C++)](<../Camera Kit（相机服务）/开发相机应用基础能力(CC++)/相机旋转/适配相机旋转角度(CC++)/camera-rotation-angle-adaptation-native.md>)

**API参考**

* ArkTS API：[camera](<../../../harmonyos-references/Camera Kit（相机服务）/ArkTS API/@ohos.multimedia.camera (相机管理)/js-apis-camera.md>)
* C API：[OH\_Camera](<../../../harmonyos-references/Camera Kit（相机服务）/C API/模块/OH_Camera/capi-oh-camera.md>)

**最佳实践**

* [相机预览花屏解决方案](../../../best-practices/媒体/相机/相机预览花屏解决方案/bpta-deal-stride-solution.md)

### 相机拍照

拍照是相机的最重要功能之一，Camera Kit提供多种拍照方式，开发者可以直接拉起系统相机拍照、采用系统预配置简化应用开发流程，或是根据开放接口开发一个专业的相机应用。

**指南**

* [通过系统相机拍照和录像(CameraPicker)](<../Camera Kit（相机服务）/开发相机应用基础能力(ArkTS)/通过系统相机拍照和录像(CameraPicker)/camera-picker.md>)
* [拍照(ArkTS)](<../Camera Kit（相机服务）/开发相机应用基础能力(ArkTS)/拍照(ArkTS)/camera-shooting.md>)
* [分段式拍照(ArkTS)](<../Camera Kit（相机服务）/开发相机应用基础能力(ArkTS)/分段式拍照(ArkTS)/camera-deferred-capture.md>)
* [动态照片拍摄(ArkTS)](<../Camera Kit（相机服务）/开发相机应用基础能力(ArkTS)/动态照片拍摄(ArkTS)/camera-moving-photo.md>)
* [使用相机预配置(ArkTS)](<../Camera Kit（相机服务）/开发相机应用基础能力(ArkTS)/使用相机预配置(ArkTS)/camera-preconfig.md>)
* [HDR Vivid相机拍照(ArkTS)](<../Camera Kit（相机服务）/开发相机应用基础能力(ArkTS)/HDR Vivid相机拍照(ArkTS)/camera-hdr-shooting.md>)
* [适配相机旋转角度(ArkTS)](<../Camera Kit（相机服务）/开发相机应用基础能力(ArkTS)/相机旋转/适配相机旋转角度(ArkTS)/camera-rotation-angle-adaptation.md>)
* [拍照(C/C++)](<../Camera Kit（相机服务）/开发相机应用基础能力(CC++)/拍照(CC++)/native-camera-shooting.md>)
* [分段式拍照(C/C++)](<../Camera Kit（相机服务）/开发相机应用基础能力(CC++)/分段式拍照(CC++)/native-camera-deferred-capture.md>)
* [使用相机预配置(C/C++)](<../Camera Kit（相机服务）/开发相机应用基础能力(CC++)/使用相机预配置(CC++)/camera-preconfig-native.md>)
* [适配相机旋转角度(C/C++)](<../Camera Kit（相机服务）/开发相机应用基础能力(CC++)/相机旋转/适配相机旋转角度(CC++)/camera-rotation-angle-adaptation-native.md>)

**API参考**

* ArkTS API：[camera](<../../../harmonyos-references/Camera Kit（相机服务）/ArkTS API/@ohos.multimedia.camera (相机管理)/js-apis-camera.md>)
* ArkTS组件：[cameraPicker](<../../../harmonyos-references/Camera Kit（相机服务）/ArkTS API/@ohos.multimedia.cameraPicker (相机选择器)/js-apis-camerapicker.md>)
* C API：[OH\_Camera](<../../../harmonyos-references/Camera Kit（相机服务）/C API/模块/OH_Camera/capi-oh-camera.md>)

**最佳实践**

* [相机分段式拍照性能优化实践](../../../best-practices/媒体/相机/相机分段式拍照性能优化/bpta-camera-shot2see.md)

**示例代码**

* [基于系统相机实现拍照功能](https://gitcode.com/HarmonyOS_Samples/camera-picker)
* [实现相机数据采集保存功能](https://gitcode.com/HarmonyOS_Samples/camera)
* [实现相机数据采集保存功能（C++）](https://gitcode.com/HarmonyOS_Samples/camera-data-collection)

### 视频播放

AVPlayer提供功能齐全的一体化播放能力，支持多种音视频格式和流媒体协议。应用使用AVPlayer不仅可以实现基础的播放控制，还可以通过外挂字幕、画中画、自定义UI控件、内容版权保护等功能，为用户提供优良的影音体验。

**指南**

* [AVPlayer简介（含支持的格式与协议）](<../Media Kit（媒体服务）/Media Kit简介/media-kit-intro.md#avplayer>)
* [使用AVPlayer播放视频(ArkTS)](<../Media Kit（媒体服务）/媒体开发指导(ArkTS)/播放/使用AVPlayer播放视频(ArkTS)/video-playback.md>)
* [使用AVPlayer设置播放URL(ArkTS)](<../Media Kit（媒体服务）/媒体开发指导(ArkTS)/播放/使用AVPlayer设置播放URL(ArkTS)/playback-url-setting-method.md>)
* [使用AVPlayer播放流媒体(ArkTS)](<../Media Kit（媒体服务）/媒体开发指导(ArkTS)/播放/使用AVPlayer播放流媒体(ArkTS)/streaming-media-playback-development-guide.md>)
* [使用AVPlayer添加视频外挂字幕(ArkTS)](<../Media Kit（媒体服务）/媒体开发指导(ArkTS)/播放/使用AVPlayer添加视频外挂字幕(ArkTS)/video-subtitle.md>)
* [使用AVPlayer播放视频(C/C++)](<../Media Kit（媒体服务）/媒体开发指导(CC++)/播放/使用AVPlayer播放视频(CC++)/using-ndk-avplayer-for-video-playback.md>)
* [HDR Vivid视频播放](<../AVCodec Kit（音视频编解码服务）/音视频编解码/HDR Vivid能力/HDR Vivid视频播放/hdr-vivid-video-player.md>)
* [接入Background Tasks Kit长时任务实现后台播放](<../../应用框架/Background Tasks Kit（后台任务开发服务）/长时任务(ArkTS)/continuous-task.md>)
* [应用接入AVSession](<../AVSession Kit（音视频播控服务）/本地媒体会话/应用接入AVSession场景介绍/avsession-access-scene.md>)
* [应用接入播控自检](<../AVSession Kit（音视频播控服务）/应用接入播控自检/playback-control-access-selfcheck.md>)
* [基于AVPlayer播放DRM节目(ArkTS)](<../DRM Kit（数字版权保护服务）/基于AVPlayer播放DRM节目(ArkTS)/drm-avplayer-arkts-integration.md>)
* [视频转码(ArkTS)](<../Media Kit（媒体服务）/媒体开发指导(ArkTS)/视频转码/media-transcoder-arkts.md>)
* [在应用程序中使用画中画功能](../../应用框架/ArkUI（方舟UI框架）/窗口管理/在应用程序中使用画中画功能/window-pipwindow.md)

**API参考**

* ArkTS API：[AVPlayer](<../../../harmonyos-references/Media Kit（媒体服务）/ArkTS API/@ohos.multimedia.media (媒体服务)/Interface (AVPlayer)/arkts-apis-media-avplayer.md>)
* C API：[AVPlayer](<../../../harmonyos-references/Media Kit（媒体服务）/C API/模块/AVPlayer/capi-avplayer.md>)

**最佳实践**

* [在线视频播放卡顿优化实践](../../../best-practices/媒体/音频和视频/在线视频播放卡顿优化/bpta-online-video-playback-lags-practice.md)
* [音画同步最佳实践](../../../best-practices/媒体/音频和视频/音画同步/bpta-audio-video-synchronization.md)
* [基于系统能力获取视频缩略图](../../../best-practices/媒体/音频和视频/基于系统能力获取视频缩略图/bpta-video-thumbnail.md)

**示例代码**

* [实现视频播放功能](https://gitcode.com/HarmonyOS_Samples/video-play)
* [实现视频边缓存边播放功能](https://gitcode.com/HarmonyOS_Samples/video-cache)
* [实现视频流畅播放且支持后台与焦点打断功能](https://gitcode.com/HarmonyOS_Samples/video-player)
* [基于系统能力获取视频缩略图](https://gitcode.com/HarmonyOS_Samples/VideoThumbnail)
* [实现流畅切换短视频](https://gitcode.com/HarmonyOS_Samples/SmoothSwitchShortVideos)
* [实现音画同步播放效果](https://gitcode.com/HarmonyOS_Samples/AudioToVideoSync)

**设计体验**

* [播控中心](https://developer.huawei.com/consumer/cn/doc/design-guides/broadcasting-control-0000001957017133)
* [画中画](https://developer.huawei.com/consumer/cn/doc/design-guides/pip-0000001927422624)

### 视频录制

AVRecorder提供音视频录制的能力，AVScreenCapture提供屏幕录制的能力，支持多源输入，可灵活配置录制参数，帮助开发者轻松实现音视频录制功能。

**指南**

* [AVRecorder简介（含支持的格式）](<../Media Kit（媒体服务）/Media Kit简介/media-kit-intro.md#avrecorder>)
* [使用AVRecorder录制视频(ArkTS)](<../Media Kit（媒体服务）/媒体开发指导(ArkTS)/录制/使用AVRecorder录制视频(ArkTS)/video-recording.md>)
* [AVScreenCapture简介（含支持的格式）](<../Media Kit（媒体服务）/Media Kit简介/media-kit-intro.md#avscreencapture>)
* [使用AVScreenCaptureRecorder录屏写文件(ArkTS)](<../Media Kit（媒体服务）/媒体开发指导(ArkTS)/录制/使用AVScreenCaptureRecorder录屏写文件(ArkTS)/using-avscreencapture-arkts.md>)
* [使用AVScreenCapture录屏取码流(C/C++)](<../Media Kit（媒体服务）/媒体开发指导(CC++)/录制/使用AVScreenCapture录屏取码流(CC++)/using-avscreencapture-for-buffer.md>)
* [使用AVScreenCapture录屏写文件(C/C++)](<../Media Kit（媒体服务）/媒体开发指导(CC++)/录制/使用AVScreenCapture录屏写文件(CC++)/using-avscreencapture-for-file.md>)
* [HDR Vivid相机录像](<../Camera Kit（相机服务）/开发相机应用基础能力(ArkTS)/HDR Vivid相机录像(ArkTS)/camera-hdr-recording.md>)
* [HDR Vivid视频录制](<../AVCodec Kit（音视频编解码服务）/音视频编解码/HDR Vivid能力/HDR Vivid视频录制/hdr-vivid-video-recorder.md>)
* [使用Camera Kit录像(ArkTS)](<../Camera Kit（相机服务）/开发相机应用基础能力(ArkTS)/录像(ArkTS)/camera-recording.md>)

**API参考**

* ArkTS API：[AVRecorder](<../../../harmonyos-references/Media Kit（媒体服务）/ArkTS API/@ohos.multimedia.media (媒体服务)/Interface (AVRecorder)/arkts-apis-media-avrecorder.md>)
* C API：[AVRecorder](<../../../harmonyos-references/Media Kit（媒体服务）/C API/模块/AVRecorder/capi-avrecorder.md>)
* ArkTS API：[AVScreenCaptureRecorder](<../../../harmonyos-references/Media Kit（媒体服务）/ArkTS API/@ohos.multimedia.media (媒体服务)/Interface (AVScreenCaptureRecorder)/arkts-apis-media-avscreencapturerecorder.md>)
* C API：[AVScreenCapture](<../../../harmonyos-references/Media Kit（媒体服务）/C API/模块/AVScreenCapture/capi-avscreencapture.md>)

**示例代码**

* [基于CameraKit通过AVRecorder录像](https://gitcode.com/HarmonyOS_Samples/camera-kit-avrecorder)

### 视频投播

使用媒体播控，可以简单高效地将音视频投放到其他HarmonyOS设备上播放，如在手机上播放的音视频，可以投到2in1设备上继续播放。

**指南**

* [使用通话设备切换组件](<../AVSession Kit（音视频播控服务）/分布式媒体会话/使用组件切换通话设备/using-switch-call-devices.md>)
* [投播组件开发指导](<../AVSession Kit（音视频播控服务）/分布式媒体会话/使用投播组件/投播开发指导/distributed-playback-guide.md>)
* [扩展屏投播开发指导](<../AVSession Kit（音视频播控服务）/分布式媒体会话/使用投播组件/扩展屏投播开发指导/avsession-extended-screen.md>)

**API参考**

* ArkTS API：[avsession](<../../../harmonyos-references/AVSession Kit（音视频播控服务）/ArkTS API/@ohos.multimedia.avsession (媒体会话管理)/js-apis-avsession.md>)
* ArkTS组件：[AVCastPicker](<../../../harmonyos-references/AVSession Kit（音视频播控服务）/ArkTS组件/@ohos.multimedia.avCastPicker (投播组件)/ohos-multimedia-avcastpicker.md>)

**示例代码**

* [实现视频投播功能](https://gitcode.com/HarmonyOS_Samples/VideoCast)

### 音频播放

开发者可以使用AVPlayer播放媒体资源，如mp4/mp3/mkv/mpeg-ts等，也可以使用AudioRenderer播放PCM音频数据。

**AVPlayer指南**

* [使用AVPlayer播放音频(ArkTS)](<../Media Kit（媒体服务）/媒体开发指导(ArkTS)/播放/使用AVPlayer播放音频(ArkTS)/using-avplayer-for-playback.md>)
* [使用AVPlayer设置播放URL(ArkTS)](<../Media Kit（媒体服务）/媒体开发指导(ArkTS)/播放/使用AVPlayer设置播放URL(ArkTS)/playback-url-setting-method.md>)
* [使用AVPlayer播放流媒体(ArkTS)](<../Media Kit（媒体服务）/媒体开发指导(ArkTS)/播放/使用AVPlayer播放流媒体(ArkTS)/streaming-media-playback-development-guide.md>)
* [使用SoundPool播放短音频(ArkTS)](<../Media Kit（媒体服务）/媒体开发指导(ArkTS)/播放/使用SoundPool播放短音频(ArkTS)/using-soundpool-for-playback.md>)
* [使用AVPlayer播放音频(C/C++)](<../Media Kit（媒体服务）/媒体开发指导(CC++)/播放/使用AVPlayer播放音频(CC++)/using-ndk-avplayer-for-playback.md>)

**AVPlayer API参考**

* ArkTS API：[AVPlayer](<../../../harmonyos-references/Media Kit（媒体服务）/ArkTS API/@ohos.multimedia.media (媒体服务)/Interface (AVPlayer)/arkts-apis-media-avplayer.md>)
* C API：[AVPlayer](<../../../harmonyos-references/Media Kit（媒体服务）/C API/模块/AVPlayer/capi-avplayer.md>)

**AudioRenderer指南**

* [使用AudioRenderer开发音频播放功能](<../Audio Kit（音频服务）/音频播放/使用AudioRenderer开发音频播放功能(ArkTs)/using-audiorenderer-for-playback.md>)
* [响应音频流输出设备变更](<../Audio Kit（音频服务）/音频设备路由管理/响应输出设备变更时合理暂停/audio-output-device-change.md>)
* [使用OHAudio开发音频播放功能(C/C++)](<../Audio Kit（音频服务）/音频播放/推荐使用OHAudio开发音频播放功能(CC++)/using-ohaudio-for-playback.md>)
* [使用AudioHaptic开发音振协同播放功能](<../Audio Kit（音频服务）/音频播放/使用AudioHaptic开发音振协同播放功能(ArkTs)/using-audiohaptic-for-playback.md>)

**AudioRenderer API参考**

* ArkTS API：[AudioRenderer](<../../../harmonyos-references/Audio Kit（音频服务）/ArkTS API/@ohos.multimedia.audio (音频管理)/Interface (AudioRenderer)/arkts-apis-audio-audiorenderer.md>)
* ArkTS API：[audioHaptic](<../../../harmonyos-references/Audio Kit（音频服务）/ArkTS API/@ohos.multimedia.audioHaptic (音振协同)/js-apis-audiohaptic.md>)
* C API：[OHAudio](<../../../harmonyos-references/Audio Kit（音频服务）/C API/模块/OHAudio/capi-ohaudio.md>)

**通用指南**

* [接入Background Tasks Kit长时任务实现后台播放](<../../应用框架/Background Tasks Kit（后台任务开发服务）/长时任务(ArkTS)/continuous-task.md>)
* [应用接入AVSession](<../AVSession Kit（音视频播控服务）/本地媒体会话/应用接入AVSession场景介绍/avsession-access-scene.md>)
* [应用接入播控自检](<../AVSession Kit（音视频播控服务）/应用接入播控自检/playback-control-access-selfcheck.md>)
* [使用合适的音频流类型](<../Audio Kit（音频服务）/使用合适的音频流类型/using-right-streamusage-and-sourcetype.md>)
* [音频焦点和音频会话介绍](<../Audio Kit（音频服务）/音频焦点和音频会话管理/音频焦点介绍/audio-playback-concurrency.md>)
* [使用AudioSession管理应用音频焦点(ArkTS)](<../Audio Kit（音频服务）/音频焦点和音频会话管理/音频会话管理(ArkTS)/audio-session-management.md>)
* [使用AudioSession管理应用音频焦点(C/C++)](<../Audio Kit（音频服务）/音频焦点和音频会话管理/使用OHAudio开发音频会话功能(CC++)/using-ohaudio-for-session.md>)

**最佳实践**

* [音频焦点管理解决方案](../../../best-practices/媒体/音频和视频/音频焦点管理解决方案/bpta-audio-focus-management.md)
* [音乐服务卡片](../../../best-practices/应用框架/服务卡片/音乐服务卡片/bpta-music-card.md)

**示例代码**

* [实现音频应用作为媒体会话提供方接入媒体会话](https://gitcode.com/HarmonyOS_Samples/media-provider)
* [实现音频低时延录制与播放](https://gitcode.com/HarmonyOS_Samples/audio-native)

**设计体验**

* [播控中心](https://developer.huawei.com/consumer/cn/doc/design-guides/broadcasting-control-0000001957017133)

### 音频采集

AudioCapture提供了音频采集能力，为开发者提供PCM原始数据。

**指南**

* [使用AudioCapturer开发音频录制功能](<../Audio Kit（音频服务）/音频录制/使用AudioCapturer开发音频录制功能(ArkTS)/using-audiocapturer-for-recording.md>)
* [使用OHAudio开发音频录制功能(C/C++)](<../Audio Kit（音频服务）/音频录制/推荐使用OHAudio开发音频录制功能(CC++)/using-ohaudio-for-recording.md>)

**API参考**

* ArkTS API：[AudioCapturer](<../../../harmonyos-references/Audio Kit（音频服务）/ArkTS API/@ohos.multimedia.audio (音频管理)/Interface (AudioCapturer)/arkts-apis-audio-audiocapturer.md>)
* C API：[OHAudio](<../../../harmonyos-references/Audio Kit（音频服务）/C API/模块/OHAudio/capi-ohaudio.md>)

**示例代码**

* [实现音频低时延录制与播放](https://gitcode.com/HarmonyOS_Samples/audio-native)

### 音频录制

AVRecorder提供音频录制的能力，帮助开发者录制纯音频文件。

**指南**

* [使用AVRecorder录制音频(ArkTS)](<../Media Kit（媒体服务）/媒体开发指导(ArkTS)/录制/使用AVRecorder录制音频(ArkTS)/using-avrecorder-for-recording.md>)

**API参考**

* ArkTS API：[AVRecorder](<../../../harmonyos-references/Media Kit（媒体服务）/ArkTS API/@ohos.multimedia.media (媒体服务)/Interface (AVRecorder)/arkts-apis-media-avrecorder.md>)
* C API：[AVRecorder](<../../../harmonyos-references/Media Kit（媒体服务）/C API/模块/AVRecorder/capi-avrecorder.md>)

### 媒体资源的选择和保存

**指南**

* [使用Picker选择媒体库资源](<../Media Library Kit（媒体文件管理服务）/使用Picker选择媒体库资源/photoaccesshelper-photoviewpicker.md>)
* [使用PhotoPicker组件访问图片/视频](<../Media Library Kit（媒体文件管理服务）/使用PhotoPicker组件访问图片视频/component-guidelines-photoviewpicker.md>)
* [保存媒体库资源](<../Media Library Kit（媒体文件管理服务）/保存媒体库资源/photoaccesshelper-savebutton.md>)

**API参考**

* ArkTS API：[photoAccessHelper](<../../../harmonyos-references/Media Library Kit（媒体文件管理服务）/ArkTS API/@ohos.file.photoAccessHelper (相册管理模块)/js-apis-photoaccesshelper.md>)
* ArkTS组件：[AlbumPickerComponent](<../../../harmonyos-references/Media Library Kit（媒体文件管理服务）/ArkTS组件/@ohos.file.AlbumPickerComponent (Album Picker组件)/ohos-file-albumpickercomponent.md>)
* ArkTS组件：[PhotoPickerComponent](<../../../harmonyos-references/Media Library Kit（媒体文件管理服务）/ArkTS组件/@ohos.file.PhotoPickerComponent (PhotoPicker组件)/ohos-file-photopickercomponent.md>)
* ArkTS组件：[RecentPhotoComponent](<../../../harmonyos-references/Media Library Kit（媒体文件管理服务）/ArkTS组件/@ohos.file.RecentPhotoComponent (最近图片组件)/ohos-file-recentphotocomponent.md>)

**最佳实践**

* [图片获取与保存实践](../../../best-practices/媒体/图片/图片获取与保存实践/bpta-image_get_and_save.md)

**示例代码**

* [实现图片获取与保存功能](https://gitcode.com/HarmonyOS_Samples/ImageGetAndSave)
* [基于PhotoPicker实现图片推荐功能](https://gitcode.com/HarmonyOS_Samples/SmartPhotoPicker)

### 隐私安全

在进行媒体应用开发过程中，应用需要访问个人数据（如用户照片、视频、音频文件等）和设备数据（如相机、麦克风等）。这些资源受系统保护，使用时需通过Picker或申请相关权限。

**访问个人数据**

* [使用Picker选择媒体库资源](<../Media Library Kit（媒体文件管理服务）/使用Picker选择媒体库资源/photoaccesshelper-photoviewpicker.md>)
* [保存资源到媒体库](<../Media Library Kit（媒体文件管理服务）/保存媒体库资源/photoaccesshelper-savebutton.md>)
* [选择音频类文件](<../../应用框架/Core File Kit（文件基础服务）/用户文件/选择与保存用户文件/选择用户文件/select-user-file.md#选择音频类文件>)
* [保存音频类文件](<../../应用框架/Core File Kit（文件基础服务）/用户文件/选择与保存用户文件/保存用户文件/save-user-file.md#保存音频类文件>)

应用需要克隆、备份或同步图片/视频类文件时，可[申请受限权限读写媒体库](<../Media Library Kit（媒体文件管理服务）/受限开放能力/开发准备/photoaccesshelper-preparation.md#申请相册管理模块功能相关权限>)。

**访问设备数据**

麦克风权限ohos.permission.MICROPHONE、相机权限ohos.permission.CAMERA、媒体地理位置信息权限ohos.permission.MEDIA\_LOCATION，均为用户授权权限，申请方式见[向用户申请授权](../../系统/安全/程序访问控制/应用权限管控/申请应用权限/向用户申请授权/request-user-authorization.md)。

## 更多资源

**Audio Kit**

| 分类 | 资源链接 |
| --- | --- |
| 音频焦点 | - 开发指南：[使用合适的音频流类型](<../Audio Kit（音频服务）/使用合适的音频流类型/using-right-streamusage-and-sourcetype.md>)  - 开发指南：[音频焦点和音频会话](<../Audio Kit（音频服务）/音频焦点和音频会话管理/音频焦点介绍/audio-playback-concurrency.md>)  - ArkTS API参考：[AudioSession](<../../../harmonyos-references/Audio Kit（音频服务）/ArkTS API/@ohos.multimedia.audio (音频管理)/Interface (AudioSessionManager)/arkts-apis-audio-audiosessionmanager.md>)  - ArkTS API参考：[StreamUsage](<../../../harmonyos-references/Audio Kit（音频服务）/ArkTS API/@ohos.multimedia.audio (音频管理)/Enums/arkts-apis-audio-e.md#streamusage>) |
| 音频通话 | - 开发指南：[使用AudioRenderer播放对端的通话声音](<../Audio Kit（音频服务）/音频通话/开发音频通话功能/audio-call-development.md#使用audiorenderer播放对端的通话声音>)  - 开发指南：[使用AudioCapturer录制本端的通话声音](<../Audio Kit（音频服务）/音频通话/开发音频通话功能/audio-call-development.md#使用audiocapturer录制本端的通话声音>) |
| 更多 | [Audio Kit开发指南](<../Audio Kit（音频服务）/audio-kit.md>)  [Audio Kit API参考](<../../../harmonyos-references/Audio Kit（音频服务）/audio-api.md>) |

**AVCodec Kit**

| 分类 | 资源链接 |
| --- | --- |
| 音频编解码 | - 开发指南：[音频编码](<../AVCodec Kit（音视频编解码服务）/音视频编解码/音频编码/audio-encoding.md>)  - 开发指南：[音频解码](<../AVCodec Kit（音视频编解码服务）/音视频编解码/音频解码/audio-decoding.md>)  - 示例代码：[AudioEncoder（音频编码）](https://gitcode.com/HarmonyOS_Samples/AVCodecVideo/blob/master/entry/src/main/cpp/capbilities/AudioEncoder.cpp)  - 示例代码：[AudioDecoder（音频解码）](https://gitcode.com/HarmonyOS_Samples/AVCodecVideo/blob/master/entry/src/main/cpp/capbilities/AudioDecoder.cpp)  - C API参考：[AudioCodec（音频编解码）](<../../../harmonyos-references/AVCodec Kit（音视频编解码服务）/C API/头文件/native_avcodec_audiocodec.h/capi-native-avcodec-audiocodec-h.md>) |
| 视频编解码 | - 开发指南：[视频编码](<../AVCodec Kit（音视频编解码服务）/音视频编解码/视频编码/video-encoding.md>)  - 示例代码：[VideoEncoder（视频编码）](https://gitcode.com/openharmony/applications_app_samples/blob/master/code/BasicFeature/Media/AVCodec/entry/src/main/cpp/capbilities/video_encoder.cpp)  - C API参考：[VideoEncoder（视频编码）](<../../../harmonyos-references/AVCodec Kit（音视频编解码服务）/C API/头文件/native_avcodec_videoencoder.h/capi-native-avcodec-videoencoder-h.md>)  - 开发指南：[视频解码](<../AVCodec Kit（音视频编解码服务）/音视频编解码/视频解码/video-decoding.md>)  - 示例代码：[VideoDecoder（视频解码）](https://gitcode.com/openharmony/applications_app_samples/blob/master/code/BasicFeature/Media/AVCodec/entry/src/main/cpp/capbilities/video_decoder.cpp)  - C API参考：[VideoDecoder（视频解码）](<../../../harmonyos-references/AVCodec Kit（音视频编解码服务）/C API/头文件/native_avcodec_videodecoder.h/capi-native-avcodec-videodecoder-h.md>) |
| 更多 | [AVCodec Kit开发指南](<../AVCodec Kit（音视频编解码服务）/avcodec-kit.md>)  [AVCodec Kit API参考](<../../../harmonyos-references/AVCodec Kit（音视频编解码服务）/avcodec-api.md>) |

**AVSession Kit**

| 分类 | 资源链接 |
| --- | --- |
| 本地媒体会话 | - ArkTS API参考：[媒体会话管理](<../../../harmonyos-references/AVSession Kit（音视频播控服务）/ArkTS API/@ohos.multimedia.avsession (媒体会话管理)/js-apis-avsession.md>)  - 开发指南：[应用接入AVSession场景介绍](<../AVSession Kit（音视频播控服务）/本地媒体会话/应用接入AVSession场景介绍/avsession-access-scene.md>)  - 示例代码：[基于AVPlayer实现播放接入](https://gitcode.com/HarmonyOS_Samples/media-provider) |
| 更多 | [AVSession Kit开发指南](<../AVSession Kit（音视频播控服务）/avsession-kit.md>)  [AVSession Kit API参考](<../../../harmonyos-references/AVSession Kit（音视频播控服务）/avsession-api.md>) |

**Camera Kit**

| 分类 | 资源链接 |
| --- | --- |
| 视频录制 | - ArkTS API参考：[Camera API(相机管理)](<../../../harmonyos-references/Camera Kit（相机服务）/ArkTS API/@ohos.multimedia.camera (相机管理)/js-apis-camera.md>)  - 开发指南：[录像(ArkTS)](<../Camera Kit（相机服务）/开发相机应用基础能力(ArkTS)/录像(ArkTS)/camera-recording.md>)  - 开发指南：[录像(C/C++)](<../Camera Kit（相机服务）/开发相机应用基础能力(CC++)/录像(CC++)/native-camera-recording.md>)  - 示例实现：[录像实践(ArkTS)](<../Camera Kit（相机服务）/开发相机应用基础能力(ArkTS)/录像实践(ArkTS)/camera-recording-case.md>) |
| 安全相机 | - ArkTS API参考：[SecureSession](<../../../harmonyos-references/Camera Kit（相机服务）/ArkTS API/@ohos.multimedia.camera (相机管理)/Interface (SecureSession)/arkts-apis-camera-securesession.md>)  - 开发指南：[安全相机(ArkTS)](<../Camera Kit（相机服务）/开发相机应用基础能力(ArkTS)/安全相机(ArkTS)/camera-secure-photo.md>) |
| 更多 | [Camera Kit开发指南](<../Camera Kit（相机服务）/camera-kit.md>)  [Camera Kit API参考](<../../../harmonyos-references/Camera Kit（相机服务）/camera-api.md>) |

**DRM Kit**

| 分类 | 资源链接 |
| --- | --- |
| AVPlayer播放DRM节目 | - ArkTS API参考：[DRM](<../../../harmonyos-references/DRM Kit（数字版权保护服务）/ArkTS API/@ohos.multimedia.drm (数字版权保护)/js-apis-drm.md>)  - 开发指南：[数字版权保护(ArkTS)](<../DRM Kit（数字版权保护服务）/数字版权保护(ArkTS)/drm-arkts-dev-guide.md>)  - 示例实现：[基于AVPlayer播放DRM节目(ArkTS)](<../DRM Kit（数字版权保护服务）/基于AVPlayer播放DRM节目(ArkTS)/drm-avplayer-arkts-integration.md>) |
| AVCodec播放DRM节目 | - C API参考：[数字版权保护API(C/C++)](<../../../harmonyos-references/DRM Kit（数字版权保护服务）/C API/模块/Drm/capi-drm.md>)  - 开发指南：[数字版权保护(C/C++)](<../DRM Kit（数字版权保护服务）/数字版权保护(CC++)/drm-c-dev-guide.md>)  - 示例实现：[基于AVCodec播放DRM节目(C/C++)](<../DRM Kit（数字版权保护服务）/基于AVCodec播放DRM节目(CC++)/drm-avcodec-integration.md>) |
| 更多 | [DRM Kit开发指南](<../DRM Kit（数字版权保护服务）/drm-kit.md>)  [DRM Kit API参考](<../../../harmonyos-references/DRM Kit（数字版权保护服务）/drm-api.md>) |

**Image Kit**

| 分类 | 资源链接 |
| --- | --- |
| 图片解码 | 支持HEIF、JPEG、PNG、WebP、GIF、BMP、SVG、ICO、DNG格式图片的解码。  - ArkTS指南：[使用ImageSource完成图片解码](<../Image Kit（图片处理服务）/图片开发指导(ArkTS)/图片解码/使用ImageSource完成图片解码/image-decoding.md>)  - C/C++指南：[使用Image\_NativeModule完成图片解码](<../Image Kit（图片处理服务）/图片开发指导(CC++)/图片解码/使用Image_NativeModule完成图片解码/image-source-c.md>)  支持自定义申请内存类型，优化解码效率。  - ArkTS指南：[申请图片解码内存(ArkTS)](<../Image Kit（图片处理服务）/图片开发指导(ArkTS)/图片解码/图片解码内存优化(ArkTS)/image-allocator-type.md>)  - C/C++指南：[申请图片解码内存(C/C++)](<../Image Kit（图片处理服务）/图片开发指导(CC++)/图片解码/图片解码内存优化(CC++)/image-allocator-type-c.md>) |
| 图片编码 | 支持编码为HEIF、JPEG、PNG、WebP、GIF格式图片。  - ArkTS指南：[使用ImagePacker完成图片编码](<../Image Kit（图片处理服务）/图片开发指导(ArkTS)/图片编码/使用ImagePacker完成图片编码/image-encoding.md>)  - C/C++指南：[使用Image\_NativeModule完成图片编码](<../Image Kit（图片处理服务）/图片开发指导(CC++)/图片编码/使用Image_NativeModule完成图片编码/image-packer-c.md>) |
| 图片接收 | 支持作为消费者接收和处理图片。  - ArkTS指南：[使用ImageReceiver完成图片接收](<../Image Kit（图片处理服务）/图片开发指导(ArkTS)/图片接收/使用ImageReceiver完成图片接收/image-receiver.md>)  - C/C++指南：[使用Image\_NativeModule完成图片接收](<../Image Kit（图片处理服务）/图片开发指导(CC++)/图片接收/使用Image_NativeModule完成图片接收/image-receiver-c.md>) |
| 图片编辑和处理 | 支持裁剪、缩放、偏移、旋转、翻转、设置透明度等图像变换，以及对图片部分区域做像素数据写入的位图操作。  - ArkTS指南：[使用PixelMap完成图像变换](<../Image Kit（图片处理服务）/图片开发指导(ArkTS)/图片编辑和处理/使用PixelMap完成图像变换/image-transformation.md>)  - ArkTS指南：[使用PixelMap完成位图操作](<../Image Kit（图片处理服务）/图片开发指导(ArkTS)/图片编辑和处理/使用PixelMap完成位图操作/image-pixelmap-operation.md>)  - C/C++指南：[使用Image\_NativeModule完成位图操作](<../Image Kit（图片处理服务）/图片开发指导(CC++)/图片编辑和处理/使用Image_NativeModule完成位图操作/pixelmap-c.md>)  支持读取和编辑图片的EXIF信息。  - ArkTS指南：[编辑图片EXIF信息](<../Image Kit（图片处理服务）/图片开发指导(ArkTS)/图片编辑和处理/编辑图片Exif信息/image-tool.md>)  - C/C++指南：[使用Image\_NativeModule编辑图片EXIF信息](<../Image Kit（图片处理服务）/图片开发指导(CC++)/图片编辑和处理/使用Image_NativeModule编辑图片Exif信息/image-tool-c.md>)  支持为图片添加个性化的滤镜效果。  - C/C++指南：[使用ImageEffect编辑图片](<../Image Kit（图片处理服务）/图片开发指导(CC++)/图片编辑和处理/使用ImageEffect编辑图片/image-effect-guidelines.md>)  支持对图片做清晰度增强、色彩空间转换、HDR效果转换。  - C/C++指南：[图片缩放](<../Image Kit（图片处理服务）/图片开发指导(CC++)/图片编辑和处理/使用ImageProcessing处理图片/图片缩放/image-scaling.md>)  - C/C++指南：[图片色彩空间转换](<../Image Kit（图片处理服务）/图片开发指导(CC++)/图片编辑和处理/使用ImageProcessing处理图片/图片色彩空间转换/image-csc.md>)  - C/C++指南：[图片动态元数据生成](<../Image Kit（图片处理服务）/图片开发指导(CC++)/图片编辑和处理/使用ImageProcessing处理图片/图片动态元数据生成/image-dynamic-metadata-generation.md>)  - C/C++指南：[单层HDR图片转换双层](<../Image Kit（图片处理服务）/图片开发指导(CC++)/图片编辑和处理/使用ImageProcessing处理图片/单层HDR图片转换双层/hdr-single-to-dual.md>)  - C/C++指南：[双层HDR图片转换单层](<../Image Kit（图片处理服务）/图片开发指导(CC++)/图片编辑和处理/使用ImageProcessing处理图片/双层HDR图片转换单层/hdr-dual-to-single.md>) |
| 更多 | [Image Kit开发指南](<../Image Kit（图片处理服务）/image-kit.md>)  [Image Kit API参考](<../../../harmonyos-references/Image Kit（图片处理服务）/image-api.md>) |

**Media Kit**

| 分类 | 资源链接 |
| --- | --- |
| 视频转码 | - ArkTS API参考：[AVTranscoder](<../../../harmonyos-references/Media Kit（媒体服务）/ArkTS API/@ohos.multimedia.media (媒体服务)/Interface (AVTranscoder)/arkts-apis-media-avtranscoder.md>)  - 开发指南：[使用AVTranscoder实现视频转码(ArkTS)](<../Media Kit（媒体服务）/媒体开发指导(ArkTS)/视频转码/使用AVTranscoder实现视频转码(ArkTS)/using-avtranscoder-for-transcodering.md>)  - 开发指南：[创建异步线程执行AVTranscoder视频转码(ArkTS)](<../Media Kit（媒体服务）/媒体开发指导(ArkTS)/视频转码/创建异步线程执行AVTranscoder视频转码(ArkTS)/avtranscoder-practice.md>) |
| 元数据 | - ArkTS API参考：[AVMetadataExtractor](<../../../harmonyos-references/Media Kit（媒体服务）/ArkTS API/@ohos.multimedia.media (媒体服务)/Interface (AVMetadataExtractor)/arkts-apis-media-avmetadataextractor.md>)  - C API参考：[AVMetadataExtractor](<../../../harmonyos-references/Media Kit（媒体服务）/C API/模块/AVMetadataExtractor/capi-avmetadataextractor.md>)  - 开发指南：[使用AVMetadataExtractor提取音视频元数据信息(ArkTS)](<../Media Kit（媒体服务）/媒体开发指导(ArkTS)/媒体信息查询/使用AVMetadataExtractor提取音视频元数据信息(ArkTS)/avmetadataextractor.md>)  - 开发指南：[使用AVMetadataExtractor获取元数据(C/C++)](<../Media Kit（媒体服务）/媒体开发指导(CC++)/媒体信息查询/使用AVMetadataExtractor获取元数据(CC++)/using-ndk-avmetadataextractor-for-media.md>) |
| 缩略图 | - ArkTS API参考：[AVImageGenerator](<../../../harmonyos-references/Media Kit（媒体服务）/ArkTS API/@ohos.multimedia.media (媒体服务)/Interface (AVImageGenerator)/arkts-apis-media-avimagegenerator.md>)  - C API参考：[AVImageGenerator](<../../../harmonyos-references/Media Kit（媒体服务）/C API/模块/AVImageGenerator/capi-avimagegenerator.md>)  - 开发指南：[使用AVImageGenerator提取视频指定时间图像(ArkTS)](<../Media Kit（媒体服务）/媒体开发指导(ArkTS)/媒体信息查询/使用AVImageGenerator提取视频指定时间图像(ArkTS)/avimagegenerator.md>)  - 开发指南：[使用AVImageGenerator获取视频帧(C/C++)](<../Media Kit（媒体服务）/媒体开发指导(CC++)/媒体信息查询/使用AVImageGenerator获取视频帧(CC++)/using-ndk-avimagegenerator-for-video.md>)  - 最佳实践：[基于系统能力获取视频缩略图](../../../best-practices/媒体/音频和视频/基于系统能力获取视频缩略图/bpta-video-thumbnail.md) |
| 更多 | [Media Kit开发指南](<../Media Kit（媒体服务）/media-kit.md>)  [Media Kit API参考](<../../../harmonyos-references/Media Kit（媒体服务）/media-api.md>) |

**Media Library Kit**

| 分类 | 资源链接 |
| --- | --- |
| 管理动态照片 | - 指南：[访问和管理动态照片资源](<../Media Library Kit（媒体文件管理服务）/动态照片/访问和管理动态照片资源/photoaccesshelper-movingphoto.md>)  - 指南：[使用MovingPhotoView播放动态照片](<../Media Library Kit（媒体文件管理服务）/动态照片/使用MovingPhotoView播放动态照片/movingphotoview-guidelines.md>) |
| 更多 | [Media Library Kit开发指南](<../Media Library Kit（媒体文件管理服务）/medialibrary-kit.md>)  [Media Library Kit API参考](<../../../harmonyos-references/Media Library Kit（媒体文件管理服务）/media-library-api.md>) |

**Ringtone Kit**

| 分类 | 资源链接 |
| --- | --- |
| 铃声设置服务 | - ArkTS API参考：[铃声服务](<../../../harmonyos-references/Ringtone Kit（铃声服务）/ArkTS API/ringtone（铃声服务）/ringtone-ringtone.md>)  - 指南：[设置铃声](<../Ringtone Kit（铃声服务）/设置铃声/ringtone-preparations.md>) |

**Scan Kit**

| 分类 | 资源链接 |
| --- | --- |
| 默认界面扫码 | - ArkTS API参考：[默认界面扫码](<../../../harmonyos-references/Scan Kit（统一扫码服务）/ArkTS API/scanBarcode (默认界面扫码)/scan-scanbarcode-api.md>)  - 指南：[默认界面扫码](<../Scan Kit（统一扫码服务）/默认界面扫码/scan-scanbarcode.md>) |
| 自定义界面扫码 | - ArkTS API参考：[自定义界面扫码](<../../../harmonyos-references/Scan Kit（统一扫码服务）/ArkTS API/customScan (自定义界面扫码)/scan-customscan-api.md>)  - 指南：[自定义界面扫码](<../Scan Kit（统一扫码服务）/自定义界面扫码/scan-customscan.md>) |
| 图像识码 | - ArkTS API参考：[图像识码](<../../../harmonyos-references/Scan Kit（统一扫码服务）/ArkTS API/detectBarcode (图像识码)/scan-imagedecode.md>)  - 指南：[识别本地图片](<../Scan Kit（统一扫码服务）/图像识码/识别本地图片/scan-detectbarcode.md>)  - 指南：[识别图像数据](<../Scan Kit（统一扫码服务）/图像识码/识别图像数据/scan-decodeimage.md>) |
| 码图生成 | - ArkTS API参考：[码图生成](<../../../harmonyos-references/Scan Kit（统一扫码服务）/ArkTS API/generateBarcode (码图生成)/scan-generatebarcode.md>)  - 指南：[通过文本生成码图](<../Scan Kit（统一扫码服务）/码图生成/通过文本生成码图/scan-barcodegenerate.md>)  - 指南：[通过字节数组生成码图](<../Scan Kit（统一扫码服务）/码图生成/通过字节数组生成码图/scan-generatearray.md>) |
