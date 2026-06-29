---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/audio-suite-manual-rendering
title: 离线编辑(C/C++)
breadcrumb: 指南 > 媒体 > Audio Kit（音频服务） > 音频编创 > 离线编辑(C/C++)
category: harmonyos-guides
scraped_at: 2026-06-11T14:54:16+08:00
doc_updated_at: 2026-06-09
content_hash: sha256:4f5ea3d890e054803c76060c3e3e527372f0c877cdb253bc40ffd80f407f01be
---
从API version 22开始，[OHAudioSuite](<../../../../../harmonyos-references/Audio Kit（音频服务）/C API/模块/OHAudioSuite/capi-ohaudiosuite.md>)给开发者提供音频离线编辑能力，允许在非实时预览场景下对音频数据进行处理，开发者可以组合多个音频节点实现复杂的音频处理流程。

## 开发基础配置

开发者使用[OHAudioSuite](<../../../../../harmonyos-references/Audio Kit（音频服务）/C API/模块/OHAudioSuite/capi-ohaudiosuite.md>)提供的离线编辑能力，添加对应的头文件。

### 在CMake脚本中链接动态库

```
1. target_link_libraries(sample PUBLIC libohaudiosuite.so)
```

### 添加头文件

开发者通过引入头文件<[native\_audio\_suite\_base.h](<../../../../../harmonyos-references/Audio Kit（音频服务）/C API/头文件/native_audio_suite_base.h/capi-native-audio-suite-base-h.md>)>和<[native\_audio\_suite\_engine.h](<../../../../../harmonyos-references/Audio Kit（音频服务）/C API/头文件/native_audio_suite_engine.h/capi-native-audio-suite-engine-h.md>)>，使用音频编创相关API。

```
1. #include <ohaudiosuite/native_audio_suite_base.h>
2. #include <ohaudiosuite/native_audio_suite_engine.h>
```

[manual\_rendering.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/Media/Audio/AudioSuiteSample/entry/src/main/cpp/manual_rendering.cpp#L18-L21)

## 开发步骤

详细的API说明请参考：[OHAudioSuite](<../../../../../harmonyos-references/Audio Kit（音频服务）/C API/模块/OHAudioSuite/capi-ohaudiosuite.md>)。

开发者参考本节内容实现音频离线编辑功能。

### 指定音频节点类型

开发者需要根据业务场景，调用[OH\_AudioSuiteNodeBuilder\_SetNodeType()](<../../../../../harmonyos-references/Audio Kit（音频服务）/C API/头文件/native_audio_suite_engine.h/capi-native-audio-suite-engine-h.md#oh_audiosuitenodebuilder_setnodetype>)接口，指定对应的[OH\_AudioNode\_Type](<../../../../../harmonyos-references/Audio Kit（音频服务）/C API/头文件/native_audio_suite_base.h/capi-native-audio-suite-base-h.md#oh_audionode_type>)。

### 指定音频节点格式

开发者需要根据业务场景，调用[OH\_AudioSuiteNodeBuilder\_SetFormat()](<../../../../../harmonyos-references/Audio Kit（音频服务）/C API/头文件/native_audio_suite_engine.h/capi-native-audio-suite-engine-h.md#oh_audiosuitenodebuilder_setformat>)或者[OH\_AudioSuiteEngine\_SetAudioFormat()](<../../../../../harmonyos-references/Audio Kit（音频服务）/C API/头文件/native_audio_suite_engine.h/capi-native-audio-suite-engine-h.md#oh_audiosuiteengine_setaudioformat>)接口，设置音频格式（位深（[OH\_Audio\_SampleFormat](<../../../../../harmonyos-references/Audio Kit（音频服务）/C API/头文件/native_audio_suite_base.h/capi-native-audio-suite-base-h.md#oh_audio_sampleformat>)）、采样率（[OH\_Audio\_SampleRate](<../../../../../harmonyos-references/Audio Kit（音频服务）/C API/头文件/native_audio_suite_base.h/capi-native-audio-suite-base-h.md#oh_audio_samplerate>)）、声道数（[OH\_AudioChannelLayout](<../../../../../harmonyos-references/AVCodec Kit（音视频编解码服务）/C API/头文件/native_audio_channel_layout.h/capi-native-audio-channel-layout-h.md#oh_audiochannellayout>)）等）。

### 基础离线编辑

使用效果节点（如均衡器效果节点）处理输入的PCM（Pulse Code Modulation）音频数据，输出带有该音效的PCM音频数据。

**图1**：基础离线编辑示意图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/db/v3/6u5z2R6PSHKlyt7mcE4V5g/zh-cn_image_0000002592218966.png?HW-CC-KV=V1&HW-CC-Date=20260611T065414Z&HW-CC-Expire=86400&HW-CC-Sign=EF0463D15AC4EE14DC480E0E31A69E4D1F1811B90636725709FF5209F1CE0DBD)

1. 创建引擎和管线。

   ```
   1. // 示例接口未包含返回值校验，实际使用时请务必添加校验逻辑。
   2. // 创建引擎。
   3. OH_AudioSuiteEngine *audioSuiteEngine = nullptr;
   4. OH_AudioSuiteEngine_Create(&audioSuiteEngine);

   6. // 创建管线。
   7. OH_AudioSuitePipeline *audioSuitePipeline = nullptr;
   8. OH_AudioSuiteEngine_CreatePipeline(audioSuiteEngine, &audioSuitePipeline,
   9. OH_AudioSuite_PipelineWorkMode::AUDIOSUITE_PIPELINE_EDIT_MODE);
   ```

   [manual\_rendering.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/Media/Audio/AudioSuiteSample/entry/src/main/cpp/manual_rendering.cpp#L502-L512)
2. 创建输入、输出、均衡器节点并连接组网。

   创建输入节点需要实现自定义回调函数InputNodeWriteDataCallBack，函数类型为[OH\_InputNode\_RequestDataCallback()](<../../../../../harmonyos-references/Audio Kit（音频服务）/C API/头文件/native_audio_suite_engine.h/capi-native-audio-suite-engine-h.md#oh_inputnode_requestdatacallback>)，调用[OH\_AudioSuiteNodeBuilder\_SetRequestDataCallback()](<../../../../../harmonyos-references/Audio Kit（音频服务）/C API/头文件/native_audio_suite_engine.h/capi-native-audio-suite-engine-h.md#oh_audiosuitenodebuilder_setrequestdatacallback>)接口设置回调函数。

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
   10. struct AudioDataInfo *info = static_cast<struct AudioDataInfo *>(userData);
   11. // 要处理的音频大小。
   12. int32_t actualDataSize = std::min(audioDataSize, info->bufferSize - info->totalWriteSize);
   13. // 将PCM音频数据写入audioData。
   14. if (actualDataSize > 0) {
   15. std::copy(info->buffer + info->totalWriteSize, info->buffer + info->totalWriteSize + actualDataSize,
   16. static_cast<uint8_t *>(audioData));
   17. }
   18. info->totalWriteSize += actualDataSize;
   19. // 音频数据全部处理完。
   20. if (info->totalWriteSize >= info->bufferSize) {
   21. *finished = true;
   22. }
   23. return actualDataSize;
   24. }
   ```

   [manual\_rendering.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/Media/Audio/AudioSuiteSample/entry/src/main/cpp/manual_rendering.cpp#L55-L80)

   ```
   1. // 示例接口未包含返回值校验，实际使用时请务必添加校验逻辑。
   2. // 创建节点构造器。
   3. OH_AudioNodeBuilder *nodeBuilder = nullptr;
   4. OH_AudioSuiteNodeBuilder_Create(&nodeBuilder);
   5. OH_AudioSuiteNodeBuilder_SetNodeType(nodeBuilder, OH_AudioNode_Type::INPUT_NODE_TYPE_DEFAULT);
   6. // 配置音频数据格式，开发者根据要处理的音频数据格式设置采样率、声道分布、声道数、位深、编码格式参数。
   7. OH_AudioFormat audioFormatInput;
   8. audioFormatInput.samplingRate = OH_Audio_SampleRate::SAMPLE_RATE_48000;
   9. audioFormatInput.channelLayout = OH_AudioChannelLayout::CH_LAYOUT_STEREO;
   10. audioFormatInput.channelCount = CHANNEL_COUNT;
   11. audioFormatInput.sampleFormat = OH_Audio_SampleFormat::AUDIO_SAMPLE_S16LE;
   12. audioFormatInput.encodingType = OH_Audio_EncodingType::AUDIO_ENCODING_TYPE_RAW;
   13. OH_AudioSuiteNodeBuilder_SetFormat(nodeBuilder, audioFormatInput);
   14. // 设置音频流的回调。
   15. void *userData = static_cast<void *>(audioInfo);
   16. OH_AudioSuiteNodeBuilder_SetRequestDataCallback(nodeBuilder, InputNodeWriteDataCallBack, userData);
   17. // 创建输入节点。
   18. OH_AudioSuiteEngine_CreateNode(audioSuiteEngine, nodeBuilder, &nodes.inputNode);

   20. // 重置构造器配置并设置为均衡器节点类型。
   21. OH_AudioSuiteNodeBuilder_Reset(nodeBuilder);
   22. OH_AudioSuiteNodeBuilder_SetNodeType(nodeBuilder, OH_AudioNode_Type::EFFECT_NODE_TYPE_EQUALIZER);
   23. // 创建均衡器节点。
   24. OH_AudioSuiteEngine_CreateNode(audioSuiteEngine, nodeBuilder, &nodes.eqNode);
   25. // 设置均衡器节点效果为默认。
   26. OH_AudioSuiteEngine_SetEqualizerFrequencyBandGains(nodes.eqNode, OH_EQUALIZER_PARAM_DEFAULT);

   28. // 重置构造器配置并设置为输出节点类型。
   29. OH_AudioSuiteNodeBuilder_Reset(nodeBuilder);
   30. OH_AudioSuiteNodeBuilder_SetNodeType(nodeBuilder, OH_AudioNode_Type::OUTPUT_NODE_TYPE_DEFAULT);
   31. // 配置音频数据格式，开发者根据预期输出的音频格式设置采样率、声道分布、声道数、位深、编码格式参数。
   32. OH_AudioFormat audioFormatOutput;
   33. audioFormatOutput.samplingRate = OH_Audio_SampleRate::SAMPLE_RATE_48000;
   34. audioFormatOutput.channelLayout = OH_AudioChannelLayout::CH_LAYOUT_STEREO;
   35. audioFormatOutput.channelCount = CHANNEL_COUNT;
   36. audioFormatOutput.sampleFormat = OH_Audio_SampleFormat::AUDIO_SAMPLE_S16LE;
   37. audioFormatOutput.encodingType = OH_Audio_EncodingType::AUDIO_ENCODING_TYPE_RAW;
   38. OH_AudioSuiteNodeBuilder_SetFormat(nodeBuilder, audioFormatOutput);
   39. // 创建输出节点。
   40. OH_AudioSuiteEngine_CreateNode(audioSuiteEngine, nodeBuilder, &nodes.outputNode);

   42. // 销毁节点构造器。
   43. OH_AudioSuiteNodeBuilder_Destroy(nodeBuilder);

   45. // 连接各个节点组成组网。
   46. OH_AudioSuiteEngine_ConnectNodes(nodes.inputNode, nodes.eqNode);
   47. OH_AudioSuiteEngine_ConnectNodes(nodes.eqNode, nodes.outputNode);
   ```

   [manual\_rendering.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/Media/Audio/AudioSuiteSample/entry/src/main/cpp/manual_rendering.cpp#L85-L133)
3. 渲染音频数据。

   开发者调用[OH\_AudioSuiteEngine\_RenderFrame()](<../../../../../harmonyos-references/Audio Kit（音频服务）/C API/头文件/native_audio_suite_engine.h/capi-native-audio-suite-engine-h.md#oh_audiosuiteengine_renderframe>)接口渲染并获取PCM音频数据。

   ```
   1. // 示例接口未包含返回值校验，实际使用时请务必添加校验逻辑。
   2. // 根据输出节点的格式计算单帧处理数据大小。如果samplingRate为11025请使用40ms来计算。
   3. int32_t frameSize = RENDER_FRAME_DURATION_MS * OH_Audio_SampleRate::SAMPLE_RATE_48000 * CHANNEL_COUNT *
   4. SAMPLE_FORMAT_S16LE_BYTE_SIZE / MS_PER_SECOND;
   5. // 用于接收渲染后的输出音频数据。
   6. uint8_t *audioData = (uint8_t *)malloc(frameSize);
   7. int32_t responseSize = 0;
   8. bool finished = false;
   9. // 渲染。
   10. OH_AudioSuiteEngine_StartPipeline(audioSuitePipeline);
   11. // ...
   12. do {
   13. OH_AudioSuite_Result result = OH_AudioSuiteEngine_RenderFrame(
   14. audioSuitePipeline, static_cast<void *>(audioData), frameSize, &responseSize, &finished);
   15. if ((result != OH_AudioSuite_Result::AUDIOSUITE_SUCCESS) || (responseSize <= 0)) {
   16. // 本次音频编创渲染失败。
   17. break;
   18. } else {
   19. // audioData是渲染过后的音频数据，音频数据长度为responseSize，开发者根据业务场景自行使用或者保存。
   20. // ...
   21. }
   22. } while (!finished);
   23. // ...
   24. OH_AudioSuiteEngine_StopPipeline(audioSuitePipeline);
   25. free(audioData);
   26. audioData = nullptr;
   ```

   [manual\_rendering.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/Media/Audio/AudioSuiteSample/entry/src/main/cpp/manual_rendering.cpp#L140-L133)
4. 资源销毁。

   ```
   1. // 示例接口未包含返回值校验，实际使用时请务必添加校验逻辑。
   2. // 销毁节点。
   3. OH_AudioSuiteEngine_DestroyNode(nodes.inputNode);
   4. OH_AudioSuiteEngine_DestroyNode(nodes.eqNode);
   5. OH_AudioSuiteEngine_DestroyNode(nodes.outputNode);

   7. // 销毁管线。
   8. OH_AudioSuiteEngine_DestroyPipeline(audioSuitePipeline);

   10. // 销毁引擎。
   11. OH_AudioSuiteEngine_Destroy(audioSuiteEngine);
   ```

   [manual\_rendering.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/Media/Audio/AudioSuiteSample/entry/src/main/cpp/manual_rendering.cpp#L189-L201)

### 音源分离场景

使用音源分离节点分离输入的PCM音频数据为人声和背景声，然后通过输出节点分别输出这两路数据。

**图2**：音源分离编辑示意图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/76/v3/Xzg4C60eSUqMywv-uzNC5g/zh-cn_image_0000002592378900.png?HW-CC-KV=V1&HW-CC-Date=20260611T065414Z&HW-CC-Expire=86400&HW-CC-Sign=DC6EF22CF2DD153EB2AF7F9C509C811CDB7E184448092782BB04E9CA676779E8)

示例代码如下：

1. 创建引擎和管线。

   ```
   1. // 示例接口未包含返回值校验，实际使用时请务必添加校验逻辑。
   2. // 创建引擎。
   3. OH_AudioSuiteEngine *audioSuiteEngine = nullptr;
   4. OH_AudioSuiteEngine_Create(&audioSuiteEngine);

   6. // 创建管线。
   7. OH_AudioSuitePipeline *audioSuitePipeline = nullptr;
   8. OH_AudioSuiteEngine_CreatePipeline(audioSuiteEngine, &audioSuitePipeline,
   9. OH_AudioSuite_PipelineWorkMode::AUDIOSUITE_PIPELINE_EDIT_MODE);
   ```

   [manual\_rendering.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/Media/Audio/AudioSuiteSample/entry/src/main/cpp/manual_rendering.cpp#L529-L539)
2. 创建输入、输出、音源分离节点并连接。

   创建输入节点需要实现自定义回调函数InputNodeWriteDataCallBack，函数类型为[OH\_InputNode\_RequestDataCallback()](<../../../../../harmonyos-references/Audio Kit（音频服务）/C API/头文件/native_audio_suite_engine.h/capi-native-audio-suite-engine-h.md#oh_inputnode_requestdatacallback>)，调用[OH\_AudioSuiteNodeBuilder\_SetRequestDataCallback()](<../../../../../harmonyos-references/Audio Kit（音频服务）/C API/头文件/native_audio_suite_engine.h/capi-native-audio-suite-engine-h.md#oh_audiosuitenodebuilder_setrequestdatacallback>)接口设置回调函数。

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
   10. struct AudioDataInfo *info = static_cast<struct AudioDataInfo *>(userData);
   11. // 要处理的音频大小。
   12. int32_t actualDataSize = std::min(audioDataSize, info->bufferSize - info->totalWriteSize);
   13. // 将PCM音频数据写入audioData。
   14. if (actualDataSize > 0) {
   15. std::copy(info->buffer + info->totalWriteSize, info->buffer + info->totalWriteSize + actualDataSize,
   16. static_cast<uint8_t *>(audioData));
   17. }
   18. info->totalWriteSize += actualDataSize;
   19. // 音频数据全部处理完。
   20. if (info->totalWriteSize >= info->bufferSize) {
   21. *finished = true;
   22. }
   23. return actualDataSize;
   24. }
   ```

   [manual\_rendering.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/Media/Audio/AudioSuiteSample/entry/src/main/cpp/manual_rendering.cpp#L55-L80)

   ```
   1. // 示例接口未包含返回值校验，实际使用时请务必添加校验逻辑。
   2. // 创建节点构造器。
   3. OH_AudioNodeBuilder *nodeBuilder = nullptr;
   4. OH_AudioSuiteNodeBuilder_Create(&nodeBuilder);
   5. OH_AudioSuiteNodeBuilder_SetNodeType(nodeBuilder, OH_AudioNode_Type::INPUT_NODE_TYPE_DEFAULT);

   7. // 配置音频数据格式，开发者根据要处理的音频数据格式设置采样率、声道分布、声道数、位深、编码格式参数。
   8. OH_AudioFormat audioFormatInput;
   9. audioFormatInput.samplingRate = OH_Audio_SampleRate::SAMPLE_RATE_48000;
   10. audioFormatInput.channelLayout = OH_AudioChannelLayout::CH_LAYOUT_STEREO;
   11. audioFormatInput.channelCount = CHANNEL_COUNT;
   12. audioFormatInput.sampleFormat = OH_Audio_SampleFormat::AUDIO_SAMPLE_S16LE;
   13. audioFormatInput.encodingType = OH_Audio_EncodingType::AUDIO_ENCODING_TYPE_RAW;
   14. OH_AudioSuiteNodeBuilder_SetFormat(nodeBuilder, audioFormatInput);
   15. void *userData = static_cast<void *>(audioInfo);
   16. // 设置音频流的回调。
   17. OH_AudioSuiteNodeBuilder_SetRequestDataCallback(nodeBuilder, InputNodeWriteDataCallBack, userData);

   19. // 创建输入节点。
   20. OH_AudioSuiteEngine_CreateNode(audioSuitePipeline, nodeBuilder, &nodes.inputNode);

   22. // 重置构造器配置并设置为音源分离节点类型。
   23. OH_AudioSuiteNodeBuilder_Reset(nodeBuilder);
   24. OH_AudioSuiteNodeBuilder_SetNodeType(nodeBuilder,
   25. OH_AudioNode_Type::EFFECT_MULTII_OUTPUT_NODE_TYPE_AUDIO_SEPARATION);

   27. // 创建音源分离节点。
   28. OH_AudioSuiteEngine_CreateNode(audioSuitePipeline, nodeBuilder, &nodes.aissNode);

   30. // 重置构造器配置并设置为输出节点类型。
   31. OH_AudioSuiteNodeBuilder_Reset(nodeBuilder);
   32. OH_AudioSuiteNodeBuilder_SetNodeType(nodeBuilder, OH_AudioNode_Type::OUTPUT_NODE_TYPE_DEFAULT);
   33. // 配置音频数据格式，开发者根据预期输出的音频格式设置采样率、声道分布、声道数、位深、编码格式参数。
   34. OH_AudioFormat audioFormatOutput;
   35. audioFormatOutput.samplingRate = OH_Audio_SampleRate::SAMPLE_RATE_48000;
   36. audioFormatOutput.channelLayout = OH_AudioChannelLayout::CH_LAYOUT_STEREO;
   37. audioFormatOutput.channelCount = CHANNEL_COUNT;
   38. audioFormatOutput.sampleFormat = OH_Audio_SampleFormat::AUDIO_SAMPLE_S16LE;
   39. audioFormatOutput.encodingType = OH_Audio_EncodingType::AUDIO_ENCODING_TYPE_RAW;
   40. OH_AudioSuiteNodeBuilder_SetFormat(nodeBuilder, audioFormatOutput);

   42. // 创建输出节点。
   43. OH_AudioSuiteEngine_CreateNode(audioSuitePipeline, nodeBuilder, &nodes.outputNode);

   45. // 销毁节点构造器。
   46. OH_AudioSuiteNodeBuilder_Destroy(nodeBuilder);

   48. // 连接各个节点组成组网。
   49. OH_AudioSuiteEngine_ConnectNodes(nodes.inputNode, nodes.aissNode);
   50. OH_AudioSuiteEngine_ConnectNodes(nodes.aissNode, nodes.outputNode);
   ```

   [manual\_rendering.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/Media/Audio/AudioSuiteSample/entry/src/main/cpp/manual_rendering.cpp#L207-L258)
3. 渲染音频数据。

   包含音源分离节点的管线使用[OH\_AudioSuiteEngine\_MultiRenderFrame()](<../../../../../harmonyos-references/Audio Kit（音频服务）/C API/头文件/native_audio_suite_engine.h/capi-native-audio-suite-engine-h.md#oh_audiosuiteengine_multirenderframe>)接口渲染并获取两路PCM音频数据。

   ```
   1. // 示例接口未包含返回值校验，实际使用时请务必添加校验逻辑。
   2. // 根据输出节点的格式计算单帧处理数据大小。如果samplingRate为11025请使用40ms来计算。
   3. int32_t frameSize = RENDER_FRAME_DURATION_MS * OH_Audio_SampleRate::SAMPLE_RATE_48000 * CHANNEL_COUNT *
   4. SAMPLE_FORMAT_S16LE_BYTE_SIZE / MS_PER_SECOND;
   5. // 用于接收渲染后的输出音频数据。
   6. OH_AudioDataArray audioDataArray;
   7. int32_t outputNum = 2;
   8. audioDataArray.audioDataArray = (void **)malloc(outputNum * sizeof(void *));
   9. for (int32_t i = 0; i < outputNum; i++) {
   10. audioDataArray.audioDataArray[i] = (void *)malloc(frameSize);
   11. }
   12. audioDataArray.arraySize = outputNum;
   13. audioDataArray.requestFrameSize = frameSize;
   14. int32_t responseSize = 0;
   15. bool finished = false;

   17. // 渲染。
   18. OH_AudioSuiteEngine_StartPipeline(audioSuitePipeline);
   19. // ...
   20. do {
   21. OH_AudioSuite_Result result =
   22. OH_AudioSuiteEngine_MultiRenderFrame(audioSuitePipeline, &audioDataArray, &responseSize, &finished);
   23. if ((result != OH_AudioSuite_Result::AUDIOSUITE_SUCCESS) || (responseSize <= 0)) {
   24. // 本次音频编创渲染失败。
   25. break;
   26. } else {
   27. // audioDataArray.audioDataArray[0]是提取的人声。
   28. // audioDataArray.audioDataArray[1]是提取的背景声。
   29. // 音频数据长度为responseSize，开发者根据业务场景自行使用或者保存。
   30. // ...
   31. }
   32. } while (!finished);
   33. // ...
   34. OH_AudioSuiteEngine_StopPipeline(audioSuitePipeline);

   36. for (int32_t i = 0; i < outputNum; i++) {
   37. free(audioDataArray.audioDataArray[i]);
   38. audioDataArray.audioDataArray[i] = nullptr;
   39. }
   40. free(audioDataArray.audioDataArray);
   41. audioDataArray.audioDataArray = nullptr;
   ```

   [manual\_rendering.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/Media/Audio/AudioSuiteSample/entry/src/main/cpp/manual_rendering.cpp#L266-L258)
4. 资源销毁。

   ```
   1. // 示例接口未包含返回值校验，实际使用时请务必添加校验逻辑。
   2. // 销毁节点。
   3. OH_AudioSuiteEngine_DestroyNode(nodes.inputNode);
   4. OH_AudioSuiteEngine_DestroyNode(nodes.aissNode);
   5. OH_AudioSuiteEngine_DestroyNode(nodes.outputNode);

   7. // 销毁管线。
   8. OH_AudioSuiteEngine_DestroyPipeline(audioSuitePipeline);

   10. // 销毁引擎。
   11. OH_AudioSuiteEngine_Destroy(audioSuiteEngine);
   ```

   [manual\_rendering.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/Media/Audio/AudioSuiteSample/entry/src/main/cpp/manual_rendering.cpp#L337-L349)

### 混音与级联

输入多路PCM音频数据，使用混音节点进行混音，输出混音后的PCM音频数据。

**图3**：级联编辑示意图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/24/v3/czCHfh2NRMu07SWy-cTNAg/zh-cn_image_0000002622858407.png?HW-CC-KV=V1&HW-CC-Date=20260611T065414Z&HW-CC-Expire=86400&HW-CC-Sign=5DC4854D529457E2BD5BAC908F1A10B89C45D0647755131101ABC9ED38D01399)

示例代码如下：

1. 创建引擎和管线。

   ```
   1. // 示例接口未包含返回值校验，实际使用时请务必添加校验逻辑。
   2. // 创建引擎。
   3. OH_AudioSuiteEngine *audioSuiteEngine = nullptr;
   4. OH_AudioSuiteEngine_Create(&audioSuiteEngine);

   6. // 创建管线。
   7. OH_AudioSuitePipeline *audioSuitePipeline = nullptr;
   8. OH_AudioSuiteEngine_CreatePipeline(audioSuiteEngine, &audioSuitePipeline,
   9. OH_AudioSuite_PipelineWorkMode::AUDIOSUITE_PIPELINE_EDIT_MODE);
   ```

   [manual\_rendering.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/Media/Audio/AudioSuiteSample/entry/src/main/cpp/manual_rendering.cpp#L558-L568)
2. 创建输入、输出、效果类节点并连接。

   由于混音功能有多个输入节点，需单独设置回调函数InputNodeWriteDataCallBack中的userData参数来区分多个输入节点，从而实现多个PCM音频数据的输入。InputNodeWriteDataCallBack函数类型为[OH\_InputNode\_RequestDataCallback()](<../../../../../harmonyos-references/Audio Kit（音频服务）/C API/头文件/native_audio_suite_engine.h/capi-native-audio-suite-engine-h.md#oh_inputnode_requestdatacallback>)。

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
   10. struct AudioDataInfo *info = static_cast<struct AudioDataInfo *>(userData);
   11. // 要处理的音频大小。
   12. int32_t actualDataSize = std::min(audioDataSize, info->bufferSize - info->totalWriteSize);
   13. // 将PCM音频数据写入audioData。
   14. if (actualDataSize > 0) {
   15. std::copy(info->buffer + info->totalWriteSize, info->buffer + info->totalWriteSize + actualDataSize,
   16. static_cast<uint8_t *>(audioData));
   17. }
   18. info->totalWriteSize += actualDataSize;
   19. // 音频数据全部处理完。
   20. if (info->totalWriteSize >= info->bufferSize) {
   21. *finished = true;
   22. }
   23. return actualDataSize;
   24. }
   ```

   [manual\_rendering.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/Media/Audio/AudioSuiteSample/entry/src/main/cpp/manual_rendering.cpp#L55-L80)

   ```
   1. // 示例接口未包含返回值校验，实际使用时请务必添加校验逻辑。
   2. // 创建节点构造器。
   3. OH_AudioNodeBuilder *nodeBuilder = nullptr;
   4. OH_AudioSuiteNodeBuilder_Create(&nodeBuilder);
   5. OH_AudioSuiteNodeBuilder_SetNodeType(nodeBuilder, OH_AudioNode_Type::INPUT_NODE_TYPE_DEFAULT);
   6. // 配置音频数据格式，开发者根据要处理的音频数据格式设置采样率、声道分布、声道数、位深、编码格式参数。
   7. OH_AudioFormat audioFormatInput;
   8. audioFormatInput.samplingRate = OH_Audio_SampleRate::SAMPLE_RATE_48000;
   9. audioFormatInput.channelLayout = OH_AudioChannelLayout::CH_LAYOUT_STEREO;
   10. audioFormatInput.channelCount = CHANNEL_COUNT;
   11. audioFormatInput.sampleFormat = OH_Audio_SampleFormat::AUDIO_SAMPLE_S16LE;
   12. audioFormatInput.encodingType = OH_Audio_EncodingType::AUDIO_ENCODING_TYPE_RAW;
   13. OH_AudioSuiteNodeBuilder_SetFormat(nodeBuilder, audioFormatInput);
   14. // 设置第一个音频流的回调。
   15. void *userData = static_cast<void *>(audioInfoForField);
   16. OH_AudioSuiteNodeBuilder_SetRequestDataCallback(nodeBuilder, InputNodeWriteDataCallBack, userData);
   17. // 创建第一个输入节点。
   18. OH_AudioSuiteEngine_CreateNode(audioSuitePipeline, nodeBuilder, &nodes.inputNodeForField);

   20. // 重置构造器配置并设置为输入节点类型。
   21. OH_AudioSuiteNodeBuilder_Reset(nodeBuilder);
   22. OH_AudioSuiteNodeBuilder_SetNodeType(nodeBuilder, OH_AudioNode_Type::INPUT_NODE_TYPE_DEFAULT);
   23. OH_AudioSuiteNodeBuilder_SetFormat(nodeBuilder, audioFormatInput);
   24. // 设置第二个音频流的回调。
   25. userData = static_cast<void *>(audioInfoForMix);
   26. OH_AudioSuiteNodeBuilder_SetRequestDataCallback(nodeBuilder, InputNodeWriteDataCallBack, userData);
   27. // 创建第二个输入节点。
   28. OH_AudioSuiteEngine_CreateNode(audioSuitePipeline, nodeBuilder, &nodes.inputNodeForMix);

   30. // 重置构造器配置并设置为声场节点类型。
   31. OH_AudioSuiteNodeBuilder_Reset(nodeBuilder);
   32. OH_AudioSuiteNodeBuilder_SetNodeType(nodeBuilder, OH_AudioNode_Type::EFFECT_NODE_TYPE_SOUND_FIELD);
   33. // 创建声场节点并设置声场模式为聆听。
   34. OH_AudioSuiteEngine_CreateNode(audioSuitePipeline, nodeBuilder, &nodes.fieldNode);
   35. OH_AudioSuiteEngine_SetSoundFieldType(nodes.fieldNode, SOUND_FIELD_FRONT_FACING);

   37. // 重置构造器配置并设置为混音节点类型。
   38. OH_AudioSuiteNodeBuilder_Reset(nodeBuilder);
   39. OH_AudioSuiteNodeBuilder_SetNodeType(nodeBuilder, OH_AudioNode_Type::EFFECT_NODE_TYPE_AUDIO_MIXER);
   40. // 创建混音节点。
   41. OH_AudioSuiteEngine_CreateNode(audioSuitePipeline, nodeBuilder, &nodes.mixerNode);

   43. // 重置构造器配置并设置为输出节点类型。
   44. OH_AudioSuiteNodeBuilder_Reset(nodeBuilder);
   45. OH_AudioSuiteNodeBuilder_SetNodeType(nodeBuilder, OH_AudioNode_Type::OUTPUT_NODE_TYPE_DEFAULT);
   46. // 配置音频数据格式，开发者根据预期输出的音频格式设置采样率、声道分布、声道数、位深、编码格式参数。
   47. OH_AudioFormat audioFormatOutput;
   48. audioFormatOutput.samplingRate = OH_Audio_SampleRate::SAMPLE_RATE_48000;
   49. audioFormatOutput.channelLayout = OH_AudioChannelLayout::CH_LAYOUT_STEREO;
   50. audioFormatOutput.channelCount = CHANNEL_COUNT;
   51. audioFormatOutput.sampleFormat = OH_Audio_SampleFormat::AUDIO_SAMPLE_S16LE;
   52. audioFormatOutput.encodingType = OH_Audio_EncodingType::AUDIO_ENCODING_TYPE_RAW;
   53. OH_AudioSuiteNodeBuilder_SetFormat(nodeBuilder, audioFormatOutput);
   54. // 创建输出节点。
   55. OH_AudioSuiteEngine_CreateNode(audioSuitePipeline, nodeBuilder, &nodes.outputNode);

   57. // 销毁输出节点构造器。
   58. OH_AudioSuiteNodeBuilder_Destroy(nodeBuilder);

   60. // 连接各个节点组成组网。
   61. OH_AudioSuiteEngine_ConnectNodes(nodes.inputNodeForField, nodes.fieldNode);
   62. OH_AudioSuiteEngine_ConnectNodes(nodes.fieldNode, nodes.mixerNode);
   63. OH_AudioSuiteEngine_ConnectNodes(nodes.inputNodeForMix, nodes.mixerNode);
   64. OH_AudioSuiteEngine_ConnectNodes(nodes.mixerNode, nodes.outputNode);
   ```

   [manual\_rendering.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/Media/Audio/AudioSuiteSample/entry/src/main/cpp/manual_rendering.cpp#L356-L421)
3. 渲染音频数据。

   开发者调用[OH\_AudioSuiteEngine\_RenderFrame()](<../../../../../harmonyos-references/Audio Kit（音频服务）/C API/头文件/native_audio_suite_engine.h/capi-native-audio-suite-engine-h.md#oh_audiosuiteengine_renderframe>)接口渲染并获取PCM音频数据。

   ```
   1. // 示例接口未包含返回值校验，实际使用时请务必添加校验逻辑。
   2. // 根据输出节点的格式计算单帧处理数据大小。如果samplingRate为11025请使用40ms来计算。
   3. int32_t frameSize = RENDER_FRAME_DURATION_MS * OH_Audio_SampleRate::SAMPLE_RATE_48000 * CHANNEL_COUNT *
   4. SAMPLE_FORMAT_S16LE_BYTE_SIZE / MS_PER_SECOND;
   5. // 用于接收渲染后的输出音频数据。
   6. uint8_t *audioData = (uint8_t *)malloc(frameSize);
   7. int32_t responseSize = 0;
   8. bool finished = false;

   10. // 渲染。
   11. OH_AudioSuiteEngine_StartPipeline(audioSuitePipeline);
   12. // ...
   13. do {
   14. OH_AudioSuite_Result result = OH_AudioSuiteEngine_RenderFrame(
   15. audioSuitePipeline, static_cast<void *>(audioData), frameSize, &responseSize, &finished);
   16. if ((result != OH_AudioSuite_Result::AUDIOSUITE_SUCCESS) || (responseSize <= 0)) {
   17. // 本次音频编创渲染失败。
   18. break;
   19. } else {
   20. // audioData是渲染过后的音频数据，音频数据长度为responseSize，开发者根据业务场景自行使用或者保存。
   21. // ...
   22. }
   23. } while (!finished);
   24. // ...
   25. OH_AudioSuiteEngine_StopPipeline(audioSuitePipeline);
   26. free(audioData);
   27. audioData = nullptr;
   ```

   [manual\_rendering.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/Media/Audio/AudioSuiteSample/entry/src/main/cpp/manual_rendering.cpp#L428-L421)
4. 资源销毁。

   ```
   1. // 示例接口未包含返回值校验，实际使用时请务必添加校验逻辑。
   2. // 销毁节点。
   3. OH_AudioSuiteEngine_DestroyNode(nodes.inputNodeForMix);
   4. OH_AudioSuiteEngine_DestroyNode(nodes.inputNodeForField);
   5. OH_AudioSuiteEngine_DestroyNode(nodes.fieldNode);
   6. OH_AudioSuiteEngine_DestroyNode(nodes.mixerNode);
   7. OH_AudioSuiteEngine_DestroyNode(nodes.outputNode);

   9. // 销毁管线。
   10. OH_AudioSuiteEngine_DestroyPipeline(audioSuitePipeline);

   12. // 销毁引擎。
   13. OH_AudioSuiteEngine_Destroy(audioSuiteEngine);
   ```

   [manual\_rendering.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/Media/Audio/AudioSuiteSample/entry/src/main/cpp/manual_rendering.cpp#L478-L492)

## 完整示例代码

* [音频编创示例代码](https://gitcode.com/openharmony/applications_app_samples/tree/master/code/DocsSample/Media/Audio/AudioSuiteSample)
