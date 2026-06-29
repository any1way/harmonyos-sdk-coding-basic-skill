---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-llm-onnx2cann
title: ONNX模型转换CANN模型
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > LLM大模型能力开放 > CANN LLM模型转换 > ONNX模型转换CANN模型
category: harmonyos-guides
scraped_at: 2026-06-01T15:13:12+08:00
doc_updated_at: 2026-05-26
content_hash: sha256:1b3bedcc0a86a4ccf740c5e81709d843282de6222a77f1857e3a4f73032c3e4d
---
开发者需利用CANN提供的tools工具完成从ONNX模型到CANN模型的转换，模型转换完成后，即可开始集成。

## 配置CANN LLM模型NPU亲和适配文件

NPU亲和改造的脚本文件已默认在/CANN\_LLM\_Engine\_Model/npu\_tuned\_export/npu\_tuned\_model下各个模型文件夹中，如果需要定制，请参见[CANN LLM模型NPU亲和适配说明](https://gitcode.com/HarmonyOS_Samples/cannkit_samplecode_lm_engine_cpp/blob/master/CANN_LLM/CANN_LLM_Engine_Model/npu_tuned_export/npu_tuned_model/qwen2/README.md)。

开发者只需要按照下文模型转换流程执行对应的脚本，即可完成亲和化改造。

## 环境准备

模型转换需要使用tools/tools\_omg/omg工具，继承量化环节的[DDK工具环境](<../../CANN LLM模型量化/量化使用步骤/环境准备/cannkit-llm-usage-environmental-preparation.md>)。

## 模型转换

1. 修改CANN\_LLM/CANN\_LLM\_Engine\_Model/scripts\_for\_omc/to\_omc.sh脚本，配置相应的omg\_type、模型文件路径modelpath和量化文件路径compress\_path，示例：

   ```
   1. omg_type=xxxxxx
   2. modelpath=./model.onnx
   3. compress_path=./quant_params_file
   4. outputpath=xxx  omgtoolpath=./tools/tools_omg/omg
   5. echo $PWDchmod 777 ./tools/tools_omg/omg export LD_LIBRARY_PATH=./tools/tools_omg/master/lib64
   6. if [ "$omg_type"=="Qwen25_1b5" ]; then
   7. echo ${omg_type} "trans start"
   8. ${omgtoolpath} --model ${modelpath} --framework 5 \
   9. --output ${outputpath} \
   10. --input_shape=
   11. "input_embed:1,-1,1536;attention_mask:1,1,-1,2048;position_ids:1,-1;past_key_in0:2048,2,1,128;past_value_in0:2048,2,1,128;past_key_in1:2048,2,1,128;past_value_in1:2048,2,1,128;past_key_in2:2048,2,1,128;past_value_in2:2048,2,1,128;past_key_in3:2048,2,1,128;past_value_in3:2048,2,1,128;past_key_in4:2048,2,1,128;past_value_in4:2048,2,1,128;past_key_in5:2048,2,1,128;past_value_in5:2048,2,1,128;past_key_in6:2048,2,1,128;past_value_in6:2048,2,1,128;past_key_in7:2048,2,1,128;past_value_in7:2048,2,1,128;past_key_in8:2048,2,1,128;past_value_in8:2048,2,1,128;past_key_in9:2048,2,1,128;past_value_in9:2048,2,1,128;past_key_in10:2048,2,1,128;past_value_in10:2048,2,1,128;past_key_in11:2048,2,1,128;past_value_in11:2048,2,1,128;past_key_in12:2048,2,1,128;past_value_in12:2048,2,1,128;past_key_in13:2048,2,1,128;past_value_in13:2048,2,1,128;past_key_in14:2048,2,1,128;past_value_in14:2048,2,1,128;past_key_in15:2048,2,1,128;past_value_in15:2048,2,1,128;past_key_in16:2048,2,1,128;past_value_in16:2048,2,1,128;past_key_in17:2048,2,1,128;past_value_in17:2048,2,1,128;past_key_in18:2048,2,1,128;past_value_in18:2048,2,1,128;past_key_in19:2048,2,1,128;past_value_in19:2048,2,1,128;past_key_in20:2048,2,1,128;past_value_in20:2048,2,1,128;past_key_in21:2048,2,1,128;past_value_in21:2048,2,1,128;past_key_in22:2048,2,1,128;past_value_in22:2048,2,1,128;past_key_in23:2048,2,1,128;past_value_in23:2048,2,1,128;past_key_in24:2048,2,1,128;past_value_in24:2048,2,1,128;past_key_in25:2048,2,1,128;past_value_in25:2048,2,1,128;past_key_in26:2048,2,1,128;past_value_in26:2048,2,1,128;past_key_in27:2048,2,1,128;past_value_in27:2048,2,1,128;new_kv_cache_pos:-1;embed_scales:1,-1,1" \
   12. --dynamic_dims="1,1,1,1,1;64,64,64,64,64" \
   13. --input_type=
   14. "past_key_in0:FP16;past_value_in0:FP16;past_key_in1:FP16;past_value_in1:FP16;past_key_in2:FP16;past_value_in2:FP16;past_key_in3:FP16;past_value_in3:FP16;past_key_in4:FP16;past_value_in4:FP16;past_key_in5:FP16;past_value_in5:FP16;past_key_in6:FP16;past_value_in6:FP16;past_key_in7:FP16;past_value_in7:FP16;past_key_in8:FP16;past_value_in8:FP16;past_key_in9:FP16;past_value_in9:FP16;past_key_in10:FP16;past_value_in10:FP16;past_key_in11:FP16;past_value_in11:FP16;past_key_in12:FP16;past_value_in12:FP16;past_key_in13:FP16;past_value_in13:FP16;past_key_in14:FP16;past_value_in14:FP16;past_key_in15:FP16;past_value_in15:FP16;past_key_in16:FP16;past_value_in16:FP16;past_key_in17:FP16;past_value_in17:FP16;past_key_in18:FP16;past_value_in18:FP16;past_key_in19:FP16;past_value_in19:FP16;past_key_in20:FP16;past_value_in20:FP16;past_key_in21:FP16;past_value_in21:FP16;past_key_in22:FP16;past_value_in22:FP16;past_key_in23:FP16;past_value_in23:FP16;past_key_in24:FP16;past_value_in24:FP16;past_key_in25:FP16;past_value_in25:FP16;past_key_in26:FP16;past_value_in26:FP16;past_key_in27:FP16;past_value_in27:FP16" \
   15. --output_type=
   16. "lm_logits:FP32;past_key0:FP16;past_value0:FP16;past_key1:FP16;past_value1:FP16;past_key2:FP16;past_value2:FP16;past_key3:FP16;past_value3:FP16;past_key4:FP16;past_value4:FP16;past_key5:FP16;past_value5:FP16;past_key6:FP16;past_value6:FP16;past_key7:FP16;past_value7:FP16;past_key8:FP16;past_value8:FP16;past_key9:FP16;past_value9:FP16;past_key10:FP16;past_value10:FP16;past_key11:FP16;past_value11:FP16;past_key12:FP16;past_value12:FP16;past_key13:FP16;past_value13:FP16;past_key14:FP16;past_value14:FP16;past_key15:FP16;past_value15:FP16;past_key16:FP16;past_value16:FP16;past_key17:FP16;past_value17:FP16;past_key18:FP16;past_value18:FP16;past_key19:FP16;past_value19:FP16;past_key20:FP16;past_value20:FP16;past_key21:FP16;past_value21:FP16;past_key22:FP16;past_value22:FP16;past_key23:FP16;past_value23:FP16;past_key24:FP16;past_value24:FP16;past_key25:FP16;past_value25:FP16;past_key26:FP16;past_value26:FP16;past_key27:FP16;past_value27:FP16"  \
   17. --compress_conf ${compress_path}  \
   18. --save_weights_as_external_data=true \
   19. --platform=xxxxxx \
   20. --target=omc
   ```

   脚本中的转换模型命令中的参数含义可参考[CANN Kit工具链文档说明](../../../模型转换/离线模型转换/OMG参数/cannkit-overall-parameter.md)。
2. 执行to\_omc.sh脚本即可转换出对应的CANN格式的模型。

   脚本的输入/输出说明：

   输入：ONNX模型和量化配置文件。

   输出：CANN格式的模型。

   模型转换完成后，即可开始集成。
