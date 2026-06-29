---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-llm-onnx-model
title: 原始模型导出为友好结构ONNX模型
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > LLM大模型能力开放 > CANN LLM模型转换 > 原始模型导出为友好结构ONNX模型
category: harmonyos-guides
scraped_at: 2026-06-11T15:17:36+08:00
doc_updated_at: 2026-06-05
content_hash: sha256:c0ab2dae61f70619f5864279e0a457a104e5e30628dcc4c3525fd230d58aea47
---
在模型量化与NPU亲和性设计完成后，将原始模型转换为友好结构ONNX模型，提升后续CANN模型转换效率。

1. 进入目录/CANN\_LLM\_Engine\_Model/npu\_tuned\_export编辑model\_info\_target.yaml文件，在该文件中填写导出文件（model\_arch）与模型文件路径。

   ```
   1. model_arch: qwen2 #可选择qwen2/qwen3/zhipu
   2. # 原始模型路径
   3. hf_model_path: you hf_model absolute path
   ```

   配置export\_model\_single脚本中的info\_path参数，指向上述配置好的model\_info\_target.yaml路径。

   ```
   1. # info_path内填写model_info_target.yaml实际路径
   2. info_path = "model_info_target.yaml"
   3. if len(sys.argv) > 1: info_path = sys.argv[1]
   4. import yaml
   5. with open(info_path, "r") as f:
   6. config = yaml.load(f, Loader=yaml.FullLoader)
   7. print(config)
   8. if config.get("qlibs", None) is not None: import sys; sys.path.insert(0, config["qlibs"])
   9. for seq_len in config["seq_len"]:
   10. export_llama(
   11. export_config = config
   12. )
   ```
2. 运行export\_model\_single脚本（以Qwen2为例：export\_model\_single\_qwen2.py）。

   ```
   1. python export_model_single_qwen2.py
   ```

   执行成功后，在model\_info\_target.yaml中配置的output\_dir路径下会生成ONNX模型文件及pb权重文件。
3. ONNX模型与[量化参数](<../../CANN LLM模型量化/量化使用步骤/环境准备/cannkit-llm-usage-environmental-preparation.md>)结合，转换得到端侧部署的模型。
