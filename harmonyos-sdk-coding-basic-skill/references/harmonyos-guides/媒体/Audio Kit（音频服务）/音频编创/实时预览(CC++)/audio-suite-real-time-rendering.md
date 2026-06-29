---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/audio-suite-real-time-rendering
title: 实时预览(C/C++)
breadcrumb: 指南 > 媒体 > Audio Kit（音频服务） > 音频编创 > 实时预览(C/C++)
category: harmonyos-guides
scraped_at: 2026-06-11T14:54:17+08:00
doc_updated_at: 2026-06-05
content_hash: sha256:82b4eb9a8f8e3e6695df50821cb95b7dd261fd3011a1cfcbbad385a320252726
---
从API version 22开始，[OHAudioSuite](<../../../../../harmonyos-references/Audio Kit（音频服务）/C API/模块/OHAudioSuite/capi-ohaudiosuite.md>)给开发者提供音频编创的实时预览能力（API version 22只支持均衡器效果，API version 23及以后支持其他效果）。例如，可以使用均衡器中预置的音效，改变音乐的风格。

## 开发基础配置

开发者使用[OHAudioSuite](<../../../../../harmonyos-references/Audio Kit（音频服务）/C API/模块/OHAudioSuite/capi-ohaudiosuite.md>)提供的实时预览能力，添加对应的头文件。

### 在CMake脚本中链接动态库

```
1. target_link_libraries(sample PUBLIC libohaudio.so libohaudiosuite.so)
```

### 添加头文件

开发者通过引入头文件<[native\_audio\_suite\_base.h](<../../../../../harmonyos-references/Audio Kit（音频服务）/C API/头文件/native_audio_suite_base.h/capi-native-audio-suite-base-h.md>)>、<[native\_audio\_suite\_engine.h](<../../../../../harmonyos-references/Audio Kit（音频服务）/C API/头文件/native_audio_suite_engine.h/capi-native-audio-suite-engine-h.md>)>、<[native\_audiostreambuilder.h](<../../../../../harmonyos-references/Audio Kit（音频服务）/C API/头文件/native_audiostreambuilder.h/capi-native-audiostreambuilder-h.md>)>和<[native\_audiorenderer.h](<../../../../../harmonyos-references/Audio Kit（音频服务）/C API/头文件/native_audiorenderer.h/capi-native-audiorenderer-h.md>)>使用音频编创和音频播放相关API。

```
1. #include <ohaudiosuite/native_audio_suite_base.h>
2. #include <ohaudiosuite/native_audio_suite_engine.h>
3. #include <ohaudio/native_audiorenderer.h>
4. #include <ohaudio/native_audiostreambuilder.h>
```

[real\_time\_rendering.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/Media/Audio/AudioSuiteSample/entry/src/main/cpp/real_time_rendering.cpp#L17-L22)

## 开发步骤

### 接口调用

详细的API说明请参考[OHAudioSuite](<../../../../../harmonyos-references/Audio Kit（音频服务）/C API/模块/OHAudioSuite/capi-ohaudiosuite.md>)。

### 均衡器效果

**图1**：实时预览示意图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ac/v3/KgL5GFCFT82Yd7ZfHRIolw/zh-cn_image_0000002622698529.png?HW-CC-KV=V1&HW-CC-Date=20260611T065416Z&HW-CC-Expire=86400&HW-CC-Sign=DEF552522815FD721251446D71E1056C1B2FE851CCCE89B6816E5D8CC7E8AF18)

开发者可以通过以下步骤来实现一个简单的均衡器效果节点实时预览功能。

1. 在初始化时，创建[OHAudioSuite](<../../../../../harmonyos-references/Audio Kit（音频服务）/C API/模块/OHAudioSuite/capi-ohaudiosuite.md>)管线（包括输入节点、均衡器节点、输出节点）。

   ```
   1. struct AudioDataInfo {
   2. uint8_t *buffer = nullptr;   // 音频数据。
   3. int32_t bufferSize = 0;      // 音频数据总大小。
   4. int32_t totalWriteSize = 0;  // 处理过的音频数据总大小。
   5. int32_t totalReadSize = 0;  // 已读取的音频数据总大小。
   6. };
   ```

   [pcm\_file\_utils.h](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/Media/Audio/AudioSuiteSample/entry/src/main/cpp/pcm_file_utils.h#L21-L28)

   ```
   1. // 示例接口未包含返回值校验，实际使用时请务必添加校验逻辑。
   2. // 输入节点请求数据的回调函数。
   3. static int32_t InputNodeWriteDataCallBack(OH_AudioNode *audioNode, void *userData, void *audioData,
   4. int32_t audioDataSize, bool *finished)
   5. {
   6. if ((audioNode == nullptr) || (userData == nullptr) || (audioData == nullptr) || (audioDataSize <= 0) ||
   7. (finished == nullptr)) {
   8. return -1;
   9. }

   11. struct AudioDataInfo *info = static_cast<struct AudioDataInfo *>(userData);
   12. // 要处理的音频大小。
   13. int32_t actualDataSize = std::min(audioDataSize, info->bufferSize - info->totalWriteSize);
   14. // 将PCM音频数据写入audioData。
   15. if (actualDataSize > 0) {
   16. std::copy(info->buffer + info->totalWriteSize, info->buffer + info->totalWriteSize + actualDataSize,
   17. static_cast<uint8_t *>(audioData));
   18. }
   19. info->totalWriteSize += actualDataSize;

   21. // 音频数据全部处理完。
   22. if (info->totalWriteSize >= info->bufferSize) {
   23. *finished = true;
   24. }
   25. return actualDataSize;
   26. }
   ```

   [real\_time\_rendering.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/Media/Audio/AudioSuiteSample/entry/src/main/cpp/real_time_rendering.cpp#L31-L58)

   ```
   1. // 示例接口未包含返回值校验，实际使用时请务必添加校验逻辑。
   2. // 创建引擎。
   3. OH_AudioSuiteEngine_Create(&audioSuiteEngine);

   5. // 创建实时预览的管线。
   6. OH_AudioSuiteEngine_CreatePipeline(audioSuiteEngine, &audioSuitePipeline,
   7. OH_AudioSuite_PipelineWorkMode::AUDIOSUITE_PIPELINE_REALTIME_MODE);
   8. // 创建节点构造器。
   9. OH_AudioNodeBuilder *nodeBuilder = nullptr;
   10. OH_AudioSuiteNodeBuilder_Create(&nodeBuilder);
   11. OH_AudioSuiteNodeBuilder_SetNodeType(nodeBuilder, OH_AudioNode_Type::INPUT_NODE_TYPE_DEFAULT);

   13. // 配置音频数据格式，开发者根据要处理的音频数据格式设置采样率、声道分布、声道数、位深、编码格式参数。
   14. OH_AudioFormat audioFormatInput;
   15. audioFormatInput.samplingRate = OH_Audio_SampleRate::SAMPLE_RATE_48000;
   16. audioFormatInput.channelLayout = OH_AudioChannelLayout::CH_LAYOUT_STEREO;
   17. audioFormatInput.channelCount = CHANNEL_COUNT;
   18. audioFormatInput.sampleFormat = OH_Audio_SampleFormat::AUDIO_SAMPLE_S16LE;
   19. audioFormatInput.encodingType = OH_Audio_EncodingType::AUDIO_ENCODING_TYPE_RAW;
   20. OH_AudioSuiteNodeBuilder_SetFormat(nodeBuilder, audioFormatInput);
   21. // 设置音频流的回调。
   22. void *userData = static_cast<void *>(audioInfo);
   23. OH_AudioSuiteNodeBuilder_SetRequestDataCallback(nodeBuilder, InputNodeWriteDataCallBack, userData);
   24. // 创建输入节点。
   25. OH_AudioSuiteEngine_CreateNode(audioSuitePipeline, nodeBuilder, &inputNode);

   27. // 重置构造器配置并设置为均衡器节点类型。
   28. OH_AudioSuiteNodeBuilder_Reset(nodeBuilder);
   29. OH_AudioSuiteNodeBuilder_SetNodeType(nodeBuilder, OH_AudioNode_Type::EFFECT_NODE_TYPE_EQUALIZER);
   30. // 创建均衡器节点。
   31. OH_AudioSuiteEngine_CreateNode(audioSuitePipeline, nodeBuilder, &eqNode);
   32. // 设置均衡器节点效果为默认。
   33. OH_AudioSuiteEngine_SetEqualizerFrequencyBandGains(eqNode, OH_EQUALIZER_PARAM_DEFAULT);

   35. // 重置构造器配置并设置为输出节点类型。
   36. OH_AudioSuiteNodeBuilder_Reset(nodeBuilder);
   37. OH_AudioSuiteNodeBuilder_SetNodeType(nodeBuilder, OH_AudioNode_Type::OUTPUT_NODE_TYPE_DEFAULT);
   38. // 配置音频数据格式，开发者根据预期输出的音频格式设置采样率、声道分布、声道数、位深、编码格式参数。
   39. OH_AudioFormat audioFormatOutput;
   40. audioFormatOutput.samplingRate = OH_Audio_SampleRate::SAMPLE_RATE_48000;
   41. audioFormatOutput.channelLayout = OH_AudioChannelLayout::CH_LAYOUT_STEREO;
   42. audioFormatOutput.channelCount = CHANNEL_COUNT;
   43. audioFormatOutput.sampleFormat = OH_Audio_SampleFormat::AUDIO_SAMPLE_S16LE;
   44. audioFormatOutput.encodingType = OH_Audio_EncodingType::AUDIO_ENCODING_TYPE_RAW;
   45. OH_AudioSuiteNodeBuilder_SetFormat(nodeBuilder, audioFormatOutput);
   46. // 创建输出节点。
   47. OH_AudioSuiteEngine_CreateNode(audioSuitePipeline, nodeBuilder, &outputNode);

   49. // 销毁节点构造器。
   50. OH_AudioSuiteNodeBuilder_Destroy(nodeBuilder);

   52. // 连接各个节点组成组网。
   53. OH_AudioSuiteEngine_ConnectNodes(inputNode, eqNode);
   54. OH_AudioSuiteEngine_ConnectNodes(eqNode, outputNode);
   ```

   [real\_time\_rendering.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/Media/Audio/AudioSuiteSample/entry/src/main/cpp/real_time_rendering.cpp#L96-L151)

   注意

   离线编辑和实时预览在创建管线时有区别。

   * 实时预览：OH\_AudioSuite\_PipelineWorkMode::AUDIOSUITE\_PIPELINE\_REALTIME\_MODE
   * 离线编辑：OH\_AudioSuite\_PipelineWorkMode::AUDIOSUITE\_PIPELINE\_EDIT\_MODE
2. 创建[OH\_AudioRendererStruct](<../../../../../harmonyos-references/Audio Kit（音频服务）/C API/结构体/OH_AudioRendererStruct/capi-ohaudio-oh-audiorendererstruct.md>)实例，并在其AudioRendererOnWriteData()回调函数中调用[OHAudioSuite](<../../../../../harmonyos-references/Audio Kit（音频服务）/C API/模块/OHAudioSuite/capi-ohaudiosuite.md>)管线的[OH\_AudioSuiteEngine\_RenderFrame()](<../../../../../harmonyos-references/Audio Kit（音频服务）/C API/头文件/native_audio_suite_engine.h/capi-native-audio-suite-engine-h.md#oh_audiosuiteengine_renderframe>)接口来处理数据。

   注意

   [OH\_AudioSuiteEngine\_RenderFrame()](<../../../../../harmonyos-references/Audio Kit（音频服务）/C API/头文件/native_audio_suite_engine.h/capi-native-audio-suite-engine-h.md#oh_audiosuiteengine_renderframe>)接口的处理时长和管线中连接的效果节点数量有关，需要注意接口处理时长，以避免实时预览卡顿。

   请参考音频播放完成音频播放功能开发：[使用OHAudio开发音频播放功能(C/C++)](../../音频播放/推荐使用OHAudio开发音频播放功能(CC++)/using-ohaudio-for-playback.md)。
3. 在播放器的回调函数中，将处理后的数据复制到OH\_AudioRenderer实例的缓冲区中，实现音频播放过程中实时预览。

   ```
   1. // 示例接口未包含返回值校验，实际使用时请务必添加校验逻辑。
   2. static OH_AudioData_Callback_Result AudioRendererOnWriteData(OH_AudioRenderer *renderer, void *userData,
   3. void *audioData, int32_t audioDataSize)
   4. {
   5. bool finishedFlag = false;
   6. int32_t writeSize = 0;
   7. OH_AudioSuite_Result result = OH_AudioSuiteEngine_RenderFrame(static_cast<OH_AudioSuitePipeline *>(userData),
   8. audioData, audioDataSize, &writeSize, &finishedFlag);
   9. if (result != OH_AudioSuite_Result::AUDIOSUITE_SUCCESS) {
   10. // 音频编创渲染失败。
   11. return AUDIO_DATA_CALLBACK_RESULT_INVALID;
   12. }
   13. // 音频编创渲染完成。
   14. if (finishedFlag) {
   15. // 开发者自定义的行为。
   16. }

   18. return AUDIO_DATA_CALLBACK_RESULT_VALID;
   19. }
   ```

   [real\_time\_rendering.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/Media/Audio/AudioSuiteSample/entry/src/main/cpp/real_time_rendering.cpp#L60-L80)

   ```
   1. // 示例接口未包含返回值校验，实际使用时请务必添加校验逻辑。
   2. // 创建构建器。
   3. OH_AudioStreamBuilder_Create(&rendererBuilder, OH_AudioStream_Type::AUDIOSTREAM_TYPE_RENDERER);
   4. OH_AudioStreamBuilder_SetSamplingRate(rendererBuilder, OH_Audio_SampleRate::SAMPLE_RATE_48000);
   5. OH_AudioStreamBuilder_SetChannelCount(rendererBuilder, CHANNEL_COUNT);
   6. OH_AudioStreamBuilder_SetSampleFormat(rendererBuilder, AUDIOSTREAM_SAMPLE_S16LE);
   7. OH_AudioStreamBuilder_SetEncodingType(rendererBuilder, AUDIOSTREAM_ENCODING_TYPE_RAW);
   8. OH_AudioStreamBuilder_SetRendererInfo(rendererBuilder, AUDIOSTREAM_USAGE_MUSIC);

   10. // 如果samplingRate为11025请使用40ms来计算。
   11. int32_t frameSize = RENDER_FRAME_DURATION_MS * audioFormatOutput.samplingRate * audioFormatOutput.channelCount *
   12. SAMPLE_FORMAT_S16LE_BYTE_SIZE / MS_PER_SECOND;
   13. // 设置audioDataSize长度（待播放的数据大小）。
   14. OH_AudioStreamBuilder_SetFrameSizeInCallback(rendererBuilder, frameSize);
   15. // 配置写入音频数据回调函数。
   16. OH_AudioStreamBuilder_SetRendererWriteDataCallback(rendererBuilder, AudioRendererOnWriteData,
   17. static_cast<void *>(audioSuitePipeline));

   19. // 启动管线。
   20. OH_AudioSuiteEngine_StartPipeline(audioSuitePipeline);

   22. // 开发者可以自行创建renderer流，播放音频。
   23. // ...

   25. // ...
   26. // 停止管线。
   27. OH_AudioSuiteEngine_StopPipeline(audioSuitePipeline);
   ```

   [real\_time\_rendering.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/Media/Audio/AudioSuiteSample/entry/src/main/cpp/real_time_rendering.cpp#L152-L151)
4. 资源销毁。

   ```
   1. // 示例接口未包含返回值校验，实际使用时请务必添加校验逻辑。
   2. // 销毁流构造器。
   3. OH_AudioStreamBuilder_Destroy(rendererBuilder);

   5. // 销毁节点。
   6. OH_AudioSuiteEngine_DestroyNode(inputNode);
   7. OH_AudioSuiteEngine_DestroyNode(eqNode);
   8. OH_AudioSuiteEngine_DestroyNode(outputNode);

   10. // 销毁管线。
   11. OH_AudioSuiteEngine_DestroyPipeline(audioSuitePipeline);

   13. // 销毁引擎。
   14. OH_AudioSuiteEngine_Destroy(audioSuiteEngine);
   ```

   [real\_time\_rendering.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/Media/Audio/AudioSuiteSample/entry/src/main/cpp/real_time_rendering.cpp#L194-L209)

## 注意事项

* 音频实时预览过程中，不支持重新创建新的效果节点，只支持修改效果节点的参数。
* 音频编创错误码具体报错信息请参考：[OH\_AudioSuite\_Result](<../../../../../harmonyos-references/Audio Kit（音频服务）/C API/头文件/native_audio_suite_base.h/capi-native-audio-suite-base-h.md#oh_audiosuite_result>)。

## 完整示例代码

* [音频编创示例代码](https://gitcode.com/openharmony/applications_app_samples/tree/master/code/DocsSample/Media/Audio/AudioSuiteSample)
