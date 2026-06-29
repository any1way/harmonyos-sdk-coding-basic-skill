---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/cannkit-llm-engine
title: llm_engine.h
breadcrumb: API参考 > AI > CANN Kit（CANN异构计算框架服务） > C API > 头文件和结构体 > 头文件 > llm_engine.h
category: harmonyos-references
scraped_at: 2026-06-11T16:51:10+08:00
doc_updated_at: 2026-06-05
content_hash: sha256:a322c70188dd4d8501cafc43bc3418975250505c915adb33b3307bcb5220e791
---
## 概述

PC/2in1

定义用于LLM模型推理的API。

**引用文件：** <CANNKit/llm\_engine.h>

**库：** 新增libcann\_llm\_engine.so

**系统能力：** SystemCapability.AI.CANN.LLMEngine

**起始版本：** 6.1.1(24)

**相关模块：** [CANN](../../../模块/CANN/cannkit.md)

## 汇总

PC/2in1

### 类型定义

PC/2in1

| 名称 | 描述 |
| --- | --- |
| typedef struct [HMS\_LLMEngine\_Context](../../../模块/CANN/cannkit.md#hms_llmengine_context) [HMS\_LLMEngine\_Context](../../../模块/CANN/cannkit.md#hms_llmengine_context) | 定义LLM引擎上下文的别名。 |
| typedef struct [HMS\_LLMEngine\_Executor](../../../模块/CANN/cannkit.md#hms_llmengine_executor) [HMS\_LLMEngine\_Executor](../../../模块/CANN/cannkit.md#hms_llmengine_executor) | LLM 引擎执行器。 |
| typedef struct [HMS\_LLMEngine\_Prompt](../../../模块/CANN/cannkit.md#hms_llmengine_prompt) [HMS\_LLMEngine\_Prompt](../../../模块/CANN/cannkit.md#hms_llmengine_prompt) | LLM引擎文本输入。 |
| typedef void(\* [callbackFunctionType](../../../模块/CANN/cannkit.md#callbackfunctiontype)) (const [HMS\_LLMEngine\_Context](../../../模块/CANN/cannkit.md#hms_llmengine_context) \*) | 生成回调函数。 |

### 枚举

PC/2in1

| 名称 | 描述 |
| --- | --- |
| [HMS\_LLMEngine\_InferPerfMode](../../../模块/CANN/cannkit.md#hms_llmengine_inferperfmode) {  [HMS\_LLMENGINE\_INFERPERF\_UNSET](../../../模块/CANN/cannkit.md) = 0, [HMS\_LLMENGINE\_INFERPERF\_LOW](../../../模块/CANN/cannkit.md), [HMS\_LLMENGINE\_INFERPERF\_MIDDLE](../../../模块/CANN/cannkit.md), [HMS\_LLMENGINE\_INFERPERF\_HIGH](../../../模块/CANN/cannkit.md),  [HMS\_LLMENGINE\_INFERPERF\_EXTREME\_HIGH](../../../模块/CANN/cannkit.md)  } | 推断性能模式。 |

### 函数

PC/2in1

| 名称 | 描述 |
| --- | --- |
| [HMS\_LLMEngine\_Executor](../../../模块/CANN/cannkit.md#hms_llmengine_executor) \* [HMS\_LLMEngineExecutor\_CreateFromExecutorJson](../../../模块/CANN/cannkit.md#hms_llmengineexecutor_createfromexecutorjson) (const char \*jsonFile) | 通过JSON配置文件创建LLM引擎执行器句柄。 |
| void [HMS\_LLMEngine\_Context\_Destroy](../../../模块/CANN/cannkit.md#hms_llmengine_context_destroy) ([HMS\_LLMEngine\_Context](../../../模块/CANN/cannkit.md#hms_llmengine_context) \*\*ctx) | 销毁LLM引擎上下文。 |
| [HMS\_LLMEngine\_Context](../../../模块/CANN/cannkit.md#hms_llmengine_context) \* [HMS\_LLMEngineContext\_CreateFromContextJson](../../../模块/CANN/cannkit.md#hms_llmenginecontext_createfromcontextjson) (const char \*jsonFile) | 通过JSON配置文件创建LLM引擎上下文句柄。 |
| void [HMS\_LLMEngineExecutor\_Destroy](../../../模块/CANN/cannkit.md#hms_llmengineexecutor_destroy) ([HMS\_LLMEngine\_Executor](../../../模块/CANN/cannkit.md#hms_llmengine_executor) \*\*executor) | 销毁一个LLM引擎执行器，该执行器内存释放。 |
| [HMS\_LLMEngine\_Prompt](../../../模块/CANN/cannkit.md#hms_llmengine_prompt) \* [HMS\_LLMEnginePrompt\_Create](../../../模块/CANN/cannkit.md#hms_llmengineprompt_create) (void) | 创建一个LLM引擎提示句柄。 |
| OH\_NN\_ReturnCode [HMS\_LLMEnginePrompt\_SetText](../../../模块/CANN/cannkit.md#hms_llmengineprompt_settext) ([HMS\_LLMEngine\_Prompt](../../../模块/CANN/cannkit.md#hms_llmengine_prompt) \*prompt, const char \*text) | 设置文本输入。 |
| OH\_NN\_ReturnCode [HMS\_LLMEnginePrompt\_SetTokenId](../../../模块/CANN/cannkit.md#hms_llmengineprompt_settokenid) ([HMS\_LLMEngine\_Prompt](../../../模块/CANN/cannkit.md#hms_llmengine_prompt) \*prompt, int32\_t \*tokenIds, uint32\_t tokenNum) | 设置输入的token ID。 |
| void [HMS\_LLMEnginePrompt\_Destroy](../../../模块/CANN/cannkit.md#hms_llmengineprompt_destroy) ([HMS\_LLMEngine\_Prompt](../../../模块/CANN/cannkit.md#hms_llmengine_prompt) \*\*prompt) | 销毁LLM引擎提示词句柄。 |
| OH\_NN\_ReturnCode [HMS\_LLMEngineContext\_SetOnOneTokenGenerateDoneFunc](../../../模块/CANN/cannkit.md#hms_llmenginecontext_setononetokengeneratedonefunc) ([HMS\_LLMEngine\_Context](../../../模块/CANN/cannkit.md#hms_llmengine_context) \*ctx, [callbackFunctionType](../../../模块/CANN/cannkit.md#callbackfunctiontype) func) | 设置生成token时触发的回调函数。 |
| OH\_NN\_ReturnCode [HMS\_LLMEngineContext\_SetOnAllTokensGenerateDoneFunc](../../../模块/CANN/cannkit.md#hms_llmenginecontext_setonalltokensgeneratedonefunc) ([HMS\_LLMEngine\_Context](../../../模块/CANN/cannkit.md#hms_llmengine_context) \*ctx, [callbackFunctionType](../../../模块/CANN/cannkit.md#callbackfunctiontype) func) | 设置所有token生成完毕时触发的回调函数。 |
| OH\_NN\_ReturnCode [HMS\_LLMEngineContext\_SetOnGenerateAsyncFailed](../../../模块/CANN/cannkit.md#hms_llmenginecontext_setongenerateasyncfailed) ([HMS\_LLMEngine\_Context](../../../模块/CANN/cannkit.md#hms_llmengine_context) \*ctx, [callbackFunctionType](../../../模块/CANN/cannkit.md#callbackfunctiontype) func) | 设置生成失败时的回调函数。 |
| OH\_NN\_ReturnCode [HMS\_LLMEngineContext\_GetOneGenerationLen](../../../模块/CANN/cannkit.md#hms_llmenginecontext_getonegenerationlen) (const [HMS\_LLMEngine\_Context](../../../模块/CANN/cannkit.md#hms_llmengine_context) \*ctx, uint32\_t \*len) | 获取生成文本片段的长度。 |
| OH\_NN\_ReturnCode [HMS\_LLMEngineContext\_GetOneGeneration](../../../模块/CANN/cannkit.md#hms_llmenginecontext_getonegeneration) (const [HMS\_LLMEngine\_Context](../../../模块/CANN/cannkit.md#hms_llmengine_context) \*ctx, char \*generation, uint32\_t len) | 获取生成的文本片段。 |
| OH\_NN\_ReturnCode [HMS\_LLMEngineContext\_GetAllGenerationLen](../../../模块/CANN/cannkit.md#hms_llmenginecontext_getallgenerationlen) (const [HMS\_LLMEngine\_Context](../../../模块/CANN/cannkit.md#hms_llmengine_context) \*ctx, uint32\_t \*len) | 获取所有生成文本的总长度。 |
| OH\_NN\_ReturnCode [HMS\_LLMEngineContext\_GetAllGeneration](../../../模块/CANN/cannkit.md#hms_llmenginecontext_getallgeneration) (const [HMS\_LLMEngine\_Context](../../../模块/CANN/cannkit.md#hms_llmengine_context) \*ctx, char \*generation, uint32\_t len) | 获取所有生成的文本。 |
| OH\_NN\_ReturnCode [HMS\_LLMEngineContext\_GetOneTokenGeneration](../../../模块/CANN/cannkit.md#hms_llmenginecontext_getonetokengeneration) (const [HMS\_LLMEngine\_Context](../../../模块/CANN/cannkit.md#hms_llmengine_context) \*ctx, int32\_t \*genToken) | 获取生成的tokenid。 |
| OH\_NN\_ReturnCode [HMS\_LLMEngineContext\_GetAllTokenGenerationLen](../../../模块/CANN/cannkit.md#hms_llmenginecontext_getalltokengenerationlen) (const [HMS\_LLMEngine\_Context](../../../模块/CANN/cannkit.md#hms_llmengine_context) \*ctx, uint32\_t \*len) | 获取所有已生成tokenid的长度。 |
| OH\_NN\_ReturnCode [HMS\_LLMEngineContext\_GetAllTokenGeneration](../../../模块/CANN/cannkit.md#hms_llmenginecontext_getalltokengeneration) (const [HMS\_LLMEngine\_Context](../../../模块/CANN/cannkit.md#hms_llmengine_context) \*ctx, int32\_t \*genToken, uint32\_t len) | 获取所有已生成的tokenid。 |
| OH\_NN\_ReturnCode [HMS\_LLMEngineExecutor\_Generate](../../../模块/CANN/cannkit.md#hms_llmengineexecutor_generate) ([HMS\_LLMEngine\_Executor](../../../模块/CANN/cannkit.md#hms_llmengine_executor) \*executor, [HMS\_LLMEngine\_Context](../../../模块/CANN/cannkit.md#hms_llmengine_context) \*ctx, const [HMS\_LLMEngine\_Prompt](../../../模块/CANN/cannkit.md#hms_llmengine_prompt) \*prompt) | 执行同步LLM推理。 |
| OH\_NN\_ReturnCode [HMS\_LLMEngineExecutor\_GenerateAsync](../../../模块/CANN/cannkit.md#hms_llmengineexecutor_generateasync) ([HMS\_LLMEngine\_Executor](../../../模块/CANN/cannkit.md#hms_llmengine_executor) \*executor, [HMS\_LLMEngine\_Context](../../../模块/CANN/cannkit.md#hms_llmengine_context) \*ctx, const [HMS\_LLMEngine\_Prompt](../../../模块/CANN/cannkit.md#hms_llmengine_prompt) \*prompt) | 异步执行LLM推理。 |
| OH\_NN\_ReturnCode [HMS\_LLMEngineExecutor\_SetInferencePerfMode](../../../模块/CANN/cannkit.md#hms_llmengineexecutor_setinferenceperfmode) ([HMS\_LLMEngine\_Executor](../../../模块/CANN/cannkit.md#hms_llmengine_executor) \*executor, [HMS\_LLMEngine\_InferPerfMode](../../../模块/CANN/cannkit.md#hms_llmengine_inferperfmode) inferPerfMode) | 设置推理性能模式。 |
| OH\_NN\_ReturnCode [HMS\_LLMEngineContext\_GetTotalTimeMs](../../../模块/CANN/cannkit.md#hms_llmenginecontext_gettotaltimems) (const [HMS\_LLMEngine\_Context](../../../模块/CANN/cannkit.md#hms_llmengine_context) \*ctx, double \*ms) | 生成总耗时（单位：ms）。 |
| OH\_NN\_ReturnCode [HMS\_LLMEngineContext\_GetPrefillTimeMs](../../../模块/CANN/cannkit.md#hms_llmenginecontext_getprefilltimems) (const [HMS\_LLMEngine\_Context](../../../模块/CANN/cannkit.md#hms_llmengine_context) \*ctx, double \*ms) | 预填充时间（单位：ms）。 |
| OH\_NN\_ReturnCode [HMS\_LLMEngineContext\_GetDecodeTimeMs](../../../模块/CANN/cannkit.md#hms_llmenginecontext_getdecodetimems) (const [HMS\_LLMEngine\_Context](../../../模块/CANN/cannkit.md#hms_llmengine_context) \*ctx, double \*ms) | 解码耗时（单位：ms）。 |
| OH\_NN\_ReturnCode [HMS\_LLMEngineContext\_GetInputTokenCount](../../../模块/CANN/cannkit.md#hms_llmenginecontext_getinputtokencount) (const [HMS\_LLMEngine\_Context](../../../模块/CANN/cannkit.md#hms_llmengine_context) \*ctx, uint64\_t \*count) | 输入token数量。 |
| OH\_NN\_ReturnCode [HMS\_LLMEngineContext\_GetOutputTokenCount](../../../模块/CANN/cannkit.md#hms_llmenginecontext_getoutputtokencount) (const [HMS\_LLMEngine\_Context](../../../模块/CANN/cannkit.md#hms_llmengine_context) \*ctx, uint64\_t \*count) | 输出token数量。 |
