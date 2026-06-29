---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-llm-quantization-effect-evaluation
title: 量化效果评估
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > LLM大模型能力开放 > CANN LLM模型量化 > 量化效果评估
category: harmonyos-guides
scraped_at: 2026-06-11T15:17:34+08:00
doc_updated_at: 2026-06-05
content_hash: sha256:465f3a4ffaaab691a9c1dc0085ba4b2d327dd3f2df5e3e4250e9ab92efb002bb
---

用户如果要测试量化后模型效果，可参考插件方法，对浮点模型插入量化算子进行推理即可。 模型推理框架和输入不变。

**插件方法：**

以下为推理时对浮点模型插入量化算子，转换浮点数到量化模型的示例：

```
1. import sys
2. import torch

4. sys.path.append("path/to/dopt_torch_py3")

6. def get_quanted_model(base_model, dopt_config, quanted_ckpt):
7. from dopt.dopt_lm.opt_main import (optimize_model, set_quant_state, set_calibrate_state, set_run_mode,)
8. model = optimize_model(base_model, dopt_config)
9. model.load_state_dict(torch.load(quanted_ckpt, map_location=torch.device('cpu')), strict=True)
10. set_quant_state(model, weight_state=True, input_state=True)
11. set_calibrate_state(model, False)
12. model.eval()
13. return model
```

其中，参数的定义分别为：

* base\_model：浮点模型定义，加载自AutoModelForCausalLM等接口。
* dopt\_config：量化配置文件。
* quanted\_ckpt：量化后的pth文件。

**插件方法推理完整示例**：

以下提供qwen2量化推理完整示例供用户参考，在该示例中添加了插件方法去验证量化效果，以量化工具包和量化文件作为输入，进行仿真推理，如果推理结果正常，说明量化成功。

```
1. import os
2. import sys
3. import torch
4. from transformers import AutoModelForCausalLM, AutoTokenizer

6. # 填写DDK_tools工具包中tools_dopt/dopt_pytorch_py3的真实路径
7. sys.path.append('path/to.dopt')
8. os.environ["CUDA_VISIBLE_DEVICES"] = "0"

10. def get_quanted_model(base_model, dopt_config, quanted_ckpt):
11. from dopt.dopt_lm.opt_main import (optimize_model, set_quant_state, set_calibrate_state, set_run_mode,)
12. model = optimize_model(base_model, dopt_config)
13. model.load_state_dict(torch.load(quanted_ckpt, map_location=torch.device('cpu')), strict=True)
14. set_quant_state(model, weight_state=True, input_state=True)
15. set_calibrate_state(model, False)
16. model.eval()
17. return model

19. def generate(prompt="Give me a short introduction to large language model."):
20. messages = [
21. {"role": "system", "content": "You are Qwen, created by Alibaba Cloud. You are a helpful assistant"},
22. {"role": "user", "content": prompt}
23. ]
24. text = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
25. model_inputs = tokenizer([text], return_tensors="pt").to(model.device)
26. print(model_inputs)
27. generated_ids = model.generate(**model_inputs, max_new_tokens=512)
28. generated_ids = [
29. output_ids[len(input_ids):] for input_ids, output_ids in zip(model_inputs.input_ids, generated_ids)
30. ]
31. response = tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0]
32. return response

34. if __name__ == '__main__':
35. # 填写原模型的真实路径
36. model_name = "path/to/model"
37. model = AutoModelForCausalLM.from_pretrained(
38. model_name,
39. torch_dtype=torch.float16,
40. device_map="auto"
41. )
42. tokenizer = AutoTokenizer.from_pretrained(model_name)
43. quant_res_root = 'you_output_path'
44. # 量化配置
45. dopt_config = f"/{quant_res_root}/dopt_config.json"
46. # 量化权重
47. quanted_ckpt = f"/{quant_res_root}/train_output/trained.pth"
48. model = get_quanted_model(
49. model,
50. dopt_config,
51. quanted_ckpt
52. )
53. prompt = "who are you?"
54. response = generate(prompt)
55. print(response)
```
