---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/audio-suite-space-render
title: 空间渲染(C/C++)
breadcrumb: 指南 > 媒体 > Audio Kit（音频服务） > 音频编创 > 空间渲染(C/C++)
category: harmonyos-guides
scraped_at: 2026-06-11T14:54:18+08:00
doc_updated_at: 2026-06-09
content_hash: sha256:e69c0c19c10006c0fa97323d2afae2e78e2e2859c25c99e19a8b2e740ade09f9
---
从API version 23开始，[OHAudioSuite](<../../../../../harmonyos-references/Audio Kit（音频服务）/C API/模块/OHAudioSuite/capi-ohaudiosuite.md>)给开发者提供空间渲染效果节点[EFFECT\_NODE\_TYPE\_SPACE\_RENDER](<../../../../../harmonyos-references/Audio Kit（音频服务）/C API/头文件/native_audio_suite_base.h/capi-native-audio-suite-base-h.md#oh_audionode_type>)，用于实现三维空间音频渲染能力。空间渲染效果节点提供固定摆位、旋转及扩展三种[工作模式](audio-suite-space-render.md#工作模式)，将音频源在三维空间中进行定位、旋转和扩展处理，助力开发者高效构建沉浸式空间音频体验。

## 坐标系说明

空间渲染采用左手坐标系，即伸出左手，用拇指和食指形成一个"L"形。

* 拇指指向右侧表示：X轴正方向。
* 食指向上表示：Y轴正方向。
* 其余手指指向前表示：Z轴正方向。

坐标系参数说明：

* X坐标：左右方向。负值表示左侧，正值表示右侧。取值范围为[-5.0, 5.0]，单位为米（m）。
* Y坐标：上下方向。负值表示下方，正值表示上方。取值范围为[-5.0, 5.0]，单位为米（m）。
* Z坐标：前后方向。负值表示后方，正值表示前方。取值范围为[-5.0, 5.0]，单位为米（m）。

## 工作模式

### 固定摆位模式

固定摆位模式用于将音频源放置在特定空间的固定位置，适用于需要固定音源位置的场景，用户可通过调用[OH\_AudioSuiteEngine\_SetSpaceRenderPositionParams](<../../../../../harmonyos-references/Audio Kit（音频服务）/C API/头文件/native_audio_suite_engine.h/capi-native-audio-suite-engine-h.md#oh_audiosuiteengine_setspacerenderpositionparams>)对空间渲染节点进行参数配置。固定摆位示意图如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/36/v3/4nUmOjgqQcWBjiiGlChefw/zh-cn_image_0000002592218968.png?HW-CC-KV=V1&HW-CC-Date=20260611T065416Z&HW-CC-Expire=86400&HW-CC-Sign=6D8BA2A50FA667ADEFFDFD1C9C33EC6108B3796D0F52AA07B704A0D4E3FA3558)

### 旋转模式

旋转模式让音频源在指定位置设定单周环绕时间与时针方向进行动态渲染，用户可通过调用[OH\_AudioSuiteEngine\_SetSpaceRenderRotationParams](<../../../../../harmonyos-references/Audio Kit（音频服务）/C API/头文件/native_audio_suite_engine.h/capi-native-audio-suite-engine-h.md#oh_audiosuiteengine_setspacerenderrotationparams>)对空间渲染节点进行参数配置。旋转模式示意图如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e1/v3/p4o4KFkZSxmVw7eKIDz4bg/zh-cn_image_0000002592378902.png?HW-CC-KV=V1&HW-CC-Date=20260611T065416Z&HW-CC-Expire=86400&HW-CC-Sign=7B7843B540FCA006710B02D5099093EE5CC936074DFBED6DD6ACF3DA25EC0867)

### 扩展模式

扩展模式将音频源按照半径和角度进行扩展，用户可通过调用[OH\_AudioSuiteEngine\_SetSpaceRenderExtensionParams](<../../../../../harmonyos-references/Audio Kit（音频服务）/C API/头文件/native_audio_suite_engine.h/capi-native-audio-suite-engine-h.md#oh_audiosuiteengine_setspacerenderextensionparams>)对空间渲染节点进行参数配置。扩展模式示意图如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3e/v3/I-vg1UGdTjuBNWgaY_QuiA/zh-cn_image_0000002622858409.png?HW-CC-KV=V1&HW-CC-Date=20260611T065416Z&HW-CC-Expire=86400&HW-CC-Sign=08171594F7608C427354A5D32C30053DEF97F0B8F28532B99444B4E4A7398E32)

## 开发基础配置

开发者使用[OHAudioSuite](<../../../../../harmonyos-references/Audio Kit（音频服务）/C API/模块/OHAudioSuite/capi-ohaudiosuite.md>)提供的空间渲染效果节点，需要添加对应的头文件并链接动态库。

### 在CMake脚本中链接动态库

```
1. target_link_libraries(sample PUBLIC libohaudio.so libohaudiosuite.so)
```

### 添加头文件

通过引入头文件使用音频编创相关API。

```
1. #include <ohaudiosuite/native_audio_suite_base.h>
2. #include <ohaudiosuite/native_audio_suite_engine.h>
3. #include <ohaudio/native_audiorenderer.h>
4. #include <ohaudio/native_audiostreambuilder.h>
```

[space\_render\_rotation.h](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/Media/Audio/AudioSuiteSample/entry/src/main/cpp/space_render_rotation.h#L19-L24)

## 开发步骤

### 接口调用

详细的API说明请参考[OHAudioSuite](<../../../../../harmonyos-references/Audio Kit（音频服务）/C API/模块/OHAudioSuite/capi-ohaudiosuite.md>)。

### 空间渲染固定摆位效果

1. 创建引擎和管线。

   ```
   1. // 示例接口未包含返回值校验，实际使用时请务必添加校验逻辑。
   2. // 创建引擎。
   3. OH_AudioSuiteEngine_Create(&g_audioSuiteEngine);

   5. // 创建实时播放空间渲染的管线。
   6. OH_AudioSuiteEngine_CreatePipeline(g_audioSuiteEngine, &g_audioSuitePipeline,
   7. OH_AudioSuite_PipelineWorkMode::AUDIOSUITE_PIPELINE_REALTIME_MODE);
   ```

   [space\_render\_rotation.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/Media/Audio/AudioSuiteSample/entry/src/main/cpp/space_render_rotation.cpp#L262-L270)
2. 创建输入、输出、空间渲染等节点并连接组网。

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

   [space\_render\_rotation.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/Media/Audio/AudioSuiteSample/entry/src/main/cpp/space_render_rotation.cpp#L37-L64)

   ```
   1. // 示例接口未包含返回值校验，实际使用时请务必添加校验逻辑。
   2. // 创建节点构造器。
   3. OH_AudioNodeBuilder *nodeBuilder = nullptr;
   4. OH_AudioSuiteNodeBuilder_Create(&nodeBuilder);

   6. // 配置音频数据格式，开发者根据要处理的音频数据格式设置采样率、声道分布、声道数、位深、编码格式参数。
   7. OH_AudioFormat audioFormatInput;
   8. ConfigureAudioFormat(audioFormatInput);
   9. OH_AudioSuiteNodeBuilder_SetFormat(nodeBuilder, audioFormatInput);
   10. OH_AudioSuiteNodeBuilder_SetNodeType(nodeBuilder, OH_AudioNode_Type::INPUT_NODE_TYPE_DEFAULT);
   11. // 用户可根据自己的音频源情况设置一个或者多个输入节点。
   12. // 设置第一个音频流的回调。
   13. void *userData = static_cast<void *>(audioInfoForVocals);
   14. OH_AudioSuiteNodeBuilder_SetRequestDataCallback(nodeBuilder, InputNodeWriteDataCallBack, userData);
   15. // 创建第一个输入节点。
   16. OH_AudioSuiteEngine_CreateNode(g_audioSuitePipeline, nodeBuilder, &g_inputNodeForVocals);

   18. // 重置构造器配置并设置为输入节点类型。
   19. OH_AudioSuiteNodeBuilder_Reset(nodeBuilder);
   20. OH_AudioSuiteNodeBuilder_SetNodeType(nodeBuilder, OH_AudioNode_Type::INPUT_NODE_TYPE_DEFAULT);
   21. OH_AudioSuiteNodeBuilder_SetFormat(nodeBuilder, audioFormatInput);
   22. // 设置第二个音频流的回调。
   23. userData = static_cast<void *>(audioInfoForAccompaniment);
   24. OH_AudioSuiteNodeBuilder_SetRequestDataCallback(nodeBuilder, InputNodeWriteDataCallBack, userData);
   25. // 创建第二个输入节点。
   26. OH_AudioSuiteEngine_CreateNode(g_audioSuitePipeline, nodeBuilder, &g_inputNodeForAccompaniment);

   28. // 用户设置空间渲染固定摆位的空间音频后也可实时更新空间音频的位置，来实现周期性的变化。
   29. // 重置构造器配置并设置为空间渲染节点类型。
   30. OH_AudioSuiteNodeBuilder_Reset(nodeBuilder);
   31. OH_AudioSuiteNodeBuilder_SetNodeType(nodeBuilder, OH_AudioNode_Type::EFFECT_NODE_TYPE_SPACE_RENDER);
   32. // 创建第一个空间渲染节点。
   33. OH_AudioSuiteEngine_CreateNode(g_audioSuitePipeline, nodeBuilder, &g_spaceNodeForVocals);
   34. // 设置空间渲染节点为固定摆位。
   35. OH_AudioSuiteEngine_SetSpaceRenderPositionParams(
   36. g_spaceNodeForVocals,
   37. OH_AudioSuite_SpaceRenderPositionParams{-SPACE_RENDER_RADIUS, POSITION_ORIGIN, -SPACE_RENDER_RADIUS});

   39. // 重置构造器配置并设置为空间渲染节点类型。
   40. OH_AudioSuiteNodeBuilder_Reset(nodeBuilder);
   41. OH_AudioSuiteNodeBuilder_SetNodeType(nodeBuilder, OH_AudioNode_Type::EFFECT_NODE_TYPE_SPACE_RENDER);
   42. // 创建第二个空间渲染节点。
   43. OH_AudioSuiteEngine_CreateNode(g_audioSuitePipeline, nodeBuilder, &g_spaceNodeForAccompaniment);
   44. // 设置空间渲染节点为固定摆位。
   45. OH_AudioSuiteEngine_SetSpaceRenderPositionParams(
   46. g_spaceNodeForAccompaniment,
   47. OH_AudioSuite_SpaceRenderPositionParams{SPACE_RENDER_RADIUS, POSITION_ORIGIN, SPACE_RENDER_RADIUS});

   49. // 重置构造器配置并设置为混音节点类型。
   50. OH_AudioSuiteNodeBuilder_Reset(nodeBuilder);
   51. OH_AudioSuiteNodeBuilder_SetNodeType(nodeBuilder, OH_AudioNode_Type::EFFECT_NODE_TYPE_AUDIO_MIXER);
   52. // 创建混音节点。
   53. OH_AudioSuiteEngine_CreateNode(g_audioSuitePipeline, nodeBuilder, &g_mixerNode);

   55. // 重置构造器配置并设置为输出节点类型。
   56. OH_AudioSuiteNodeBuilder_Reset(nodeBuilder);
   57. OH_AudioSuiteNodeBuilder_SetNodeType(nodeBuilder, OH_AudioNode_Type::OUTPUT_NODE_TYPE_DEFAULT);
   58. // 配置音频数据格式，开发者根据预期输出的音频格式设置采样率、声道分布、声道数、位深、编码格式参数。
   59. OH_AudioFormat audioFormatOutput;
   60. ConfigureAudioFormat(audioFormatOutput);
   61. OH_AudioSuiteNodeBuilder_SetFormat(nodeBuilder, audioFormatOutput);
   62. // 创建输出节点。
   63. OH_AudioSuiteEngine_CreateNode(g_audioSuitePipeline, nodeBuilder, &g_outputNode);

   65. // 销毁节点构造器。
   66. OH_AudioSuiteNodeBuilder_Destroy(nodeBuilder);

   68. // 连接各个节点组成组网。
   69. OH_AudioSuiteEngine_ConnectNodes(g_inputNodeForVocals, g_spaceNodeForVocals);
   70. OH_AudioSuiteEngine_ConnectNodes(g_spaceNodeForVocals, g_mixerNode);
   71. OH_AudioSuiteEngine_ConnectNodes(g_inputNodeForAccompaniment, g_spaceNodeForAccompaniment);
   72. OH_AudioSuiteEngine_ConnectNodes(g_spaceNodeForAccompaniment, g_mixerNode);
   73. OH_AudioSuiteEngine_ConnectNodes(g_mixerNode, g_outputNode);
   ```

   [space\_render\_rotation.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/Media/Audio/AudioSuiteSample/entry/src/main/cpp/space_render_rotation.cpp#L115-L189)
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

   [space\_render\_rotation.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/Media/Audio/AudioSuiteSample/entry/src/main/cpp/space_render_rotation.cpp#L66-L86)

   ```
   1. // 示例接口未包含返回值校验，实际使用时请务必添加校验逻辑。
   2. // 创建构建器。
   3. OH_AudioStreamBuilder_Create(&g_rendererBuilder, OH_AudioStream_Type::AUDIOSTREAM_TYPE_RENDERER);
   4. OH_AudioStreamBuilder_SetSamplingRate(g_rendererBuilder, OH_Audio_SampleRate::SAMPLE_RATE_48000);
   5. OH_AudioStreamBuilder_SetChannelCount(g_rendererBuilder, CHANNEL_COUNT);
   6. OH_AudioStreamBuilder_SetSampleFormat(g_rendererBuilder, AUDIOSTREAM_SAMPLE_S16LE);
   7. OH_AudioStreamBuilder_SetEncodingType(g_rendererBuilder, AUDIOSTREAM_ENCODING_TYPE_RAW);
   8. OH_AudioStreamBuilder_SetRendererInfo(g_rendererBuilder, AUDIOSTREAM_USAGE_MUSIC);

   10. // 如果samplingRate为11025请使用40ms来计算。
   11. OH_AudioFormat audioFormatOutput;
   12. ConfigureAudioFormat(audioFormatOutput);
   13. int32_t frameSize = RENDER_FRAME_DURATION_MS * audioFormatOutput.samplingRate * audioFormatOutput.channelCount *
   14. SAMPLE_FORMAT_S16LE_BYTE_SIZE / MS_PER_SECOND;
   15. // 设置audioDataSize长度（待播放的数据大小）。
   16. OH_AudioStreamBuilder_SetFrameSizeInCallback(g_rendererBuilder, frameSize);
   17. // 配置写入音频数据回调函数。
   18. OH_AudioStreamBuilder_SetRendererWriteDataCallback(g_rendererBuilder, AudioRendererOnWriteData,
   19. static_cast<void *>(g_audioSuitePipeline));

   21. // 启动管线。
   22. OH_AudioSuiteEngine_StartPipeline(g_audioSuitePipeline);
   23. // ...
   24. // 停止管线。
   25. OH_AudioSuiteEngine_StopPipeline(g_audioSuitePipeline);
   ```

   [space\_render\_rotation.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/Media/Audio/AudioSuiteSample/entry/src/main/cpp/space_render_rotation.cpp#L194-L189)
4. 资源销毁。

   ```
   1. // 示例接口未包含返回值校验，实际使用时请务必添加校验逻辑。
   2. // 销毁流构造器。
   3. OH_AudioStreamBuilder_Destroy(g_rendererBuilder);

   5. // 销毁节点。
   6. OH_AudioSuiteEngine_DestroyNode(g_inputNodeForVocals);
   7. OH_AudioSuiteEngine_DestroyNode(g_inputNodeForAccompaniment);
   8. OH_AudioSuiteEngine_DestroyNode(g_spaceNodeForVocals);
   9. OH_AudioSuiteEngine_DestroyNode(g_spaceNodeForAccompaniment);
   10. OH_AudioSuiteEngine_DestroyNode(g_mixerNode);
   11. OH_AudioSuiteEngine_DestroyNode(g_outputNode);

   13. // 销毁管线。
   14. OH_AudioSuiteEngine_DestroyPipeline(g_audioSuitePipeline);

   16. // 销毁引擎。
   17. OH_AudioSuiteEngine_Destroy(g_audioSuiteEngine);
   ```

   [space\_render\_rotation.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/Media/Audio/AudioSuiteSample/entry/src/main/cpp/space_render_rotation.cpp#L236-L254)

## 完整示例代码

* [音频编创示例代码](https://gitcode.com/openharmony/applications_app_samples/tree/master/code/DocsSample/Media/Audio/AudioSuiteSample)
