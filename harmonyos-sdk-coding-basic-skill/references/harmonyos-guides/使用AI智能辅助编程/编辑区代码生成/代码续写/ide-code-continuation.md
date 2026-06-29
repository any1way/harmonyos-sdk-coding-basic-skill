---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-code-continuation
title: 代码续写
breadcrumb: 指南 > 使用AI智能辅助编程 > 编辑区代码生成 > 代码续写
category: harmonyos-guides
scraped_at: 2026-06-11T15:22:27+08:00
doc_updated_at: 2026-06-09
content_hash: sha256:68dd20584b2b08044d928dac8eba55a8451e2ae3e9a61eda48bf23a31c3548df
---
利用AI大模型分析并理解开发者在代码编辑区的上下文信息或自然语言描述信息，智能续写符合上下文的ArkTS或C++代码片段，减少重复编码工作。

## 使用约束

* 建议编辑区已有较丰富上下文，能够使AI模型对编程场景有一定理解的情况下进行续写。若编辑器中内容较少，AI模型可能无法有效理解用户的意图并生成相应的代码。
* AI模型反馈需满足规则：光标上文10行内，有效代码行数超过5行（排除单独{}、（）、[]括号行、空行、纯注释行场景）。

## 续写设置

### **DevEco Studio 6.1.0 Release及以上版本**

进入**File > Settings...**（macOS为**DevEco Studio > Preferences/Settings**）**>** **CodeGenie > Code Suggestion** **& Inline Chat**页面进行设置，若没登录华为开发者账号请先登录。

**快捷键和续写开启设置**选项**：**

* **Display hints for code suggestion inline chat**：在编辑区空行显示触发代码续写等功能的快捷键。
* **Enable**：启用代码续写能力。
* **Display hints for accept shortcuts**：在续写结果最后的位置显示采纳代码的快捷键。

**自动续写设置**选项**：**

* **Auto Suggestion**：自动续写开关，开启后将会根据代码上下文在合适位置自动触发代码续写。
* **Frequency**：控制自动续写的触发频率。
* **Allow auto suggestion for code completion**：是否允许自动续写与编辑器联想功能同时存在。取消勾选后，编辑器联想功能优先级更高。

**续写模型设置**选项**：**

CodeGenie为续写功能提供了内置的模型，也可使用三方模型和提示词进行续写。当前续写仅支持OpenAI和Ollama两种协议的模型，同时模型需支持FIM（Fill-in-Middle）补全能力。

* **Model**：选择代码续写的模型，模型内容请参考：[模型（Model）配置](../../自定义智能体配置/模型（Model）配置/ide-agent-model.md)。
* **Prompt format**：提示词格式，此处列出了主流的FIM提示词格式，并自动与模型选项联动。设置时需要选择与模型匹配的提示词格式，续写才能正常工作，开发者可在模型官网或者模型技术报告获取提示词格式。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/11/v3/VZT6e0x0QXqe-0kSf1gqzg/zh-cn_image_0000002602186829.png?HW-CC-KV=V1&HW-CC-Date=20260611T072227Z&HW-CC-Expire=86400&HW-CC-Sign=D86AD0B7218B64599CB8BD0EA4AAC2D42C86079E45831F79A2DED384BC0E8AAC)

### **DevEco Studio 6.1.0 Beta2**

进入**File > Settings...**（macOS为**DevEco Studio > Preferences/Settings**）**>** **CodeGenie > Code Completion** **& Inline Chat**页面进行设置，若没登录华为开发者账号请先登录。

**快捷键和续写开启设置**选项**：**

* **Show trigger shortcut tips**：在编辑区空行显示触发代码续写等功能的快捷键。
* **Enable code completion**：启用代码续写能力。
* **Show accept shortcut tips**：在续写结果最后的位置显示采纳代码的快捷键。

**自动续写设置**选项**：**

* **Enable code auto completion**：自动续写开关，开启后将会根据代码上下文在合适位置自动触发代码续写。
* **Frequency**：控制自动续写的触发频率。
* **Auto-completion is allowed when code completion is triggered**：是否允许自动续写与编辑器联想功能同时存在。取消勾选后，编辑器联想功能优先级更高。

**续写模型设置**选项**：**

CodeGenie为续写功能提供了内置的模型，也可使用三方模型和提示词进行续写。当前续写仅支持OpenAI和Ollama两种协议的模型，同时模型需支持FIM（Fill-in-Middle）补全能力。

* **Model**：选择代码续写的模型，模型内容请参考：[模型（Model）配置](../../自定义智能体配置/模型（Model）配置/ide-agent-model.md)。
* **Prompt format**：提示词格式，此处列出了主流的FIM提示词格式，并自动与模型选项联动。设置时需要选择与模型匹配的提示词格式，续写才能正常工作，开发者可在模型官网或者模型技术报告获取提示词格式。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a0/v3/bL2vJL7PQpWs5bUHkSHzeg/zh-cn_image_0000002602186827.png?HW-CC-KV=V1&HW-CC-Date=20260611T072227Z&HW-CC-Expire=86400&HW-CC-Sign=3E6E3A58298244B2177CF6CFB928E5598423D6D44623674DA0DE5857A1564060)

### **DevEco Studio 6.1.0 Beta2以下版本**

进入**File > Settings...**（macOS为****DevEco Studio > Preferences/Settings****）**>** **CodeGenie > Code Generation**页面勾选**Enable code generation**，开启代码续写功能。如果已经熟悉了CodeGenie常用的快捷键，想要更加沉浸的体验，可以在该页面勾选**Do not disturb** **mode**，隐藏代码生成工具栏及快捷键提示。

同时，根据编码习惯，选择**Enable snippet generation**（片段续写）和**Enable inline generation**（行内续写），以及设置续写时延。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e1/v3/ZNT30eV7TFKbqJ7Ax9EpAA/zh-cn_image_0000002602066775.png?HW-CC-KV=V1&HW-CC-Date=20260611T072227Z&HW-CC-Expire=86400&HW-CC-Sign=8045F58C473243BEC3C43C6D15D1E4ED1817A13DE31B39028D8E46F591150E5E)

## 续写触发和采纳

### 续写触发

**DevEco Studio 6.1.0 Release及以上版本**

Enable inline generation（行内续写）与Enable snippet generation（片段续写）合并为**Auto Suggestion**，取消了**Delay**设置项，通过设置**Frequency**调整自动续写的触发频次。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/80/v3/w3LFRTSVQX-7Gsw2ZEmT6Q/zh-cn_image_0000002571547296.png?HW-CC-KV=V1&HW-CC-Date=20260611T072227Z&HW-CC-Expire=86400&HW-CC-Sign=8827C8528A4AAD83AD3F8FFC1626C2BBC2F6273B3A85FF87516CB1A228EDA724)

**DevEco Studio 6.1.0 Beta2**

Enable inline generation（行内续写）与Enable snippet generation（片段续写）合并为**Enable code auto completion**，取消了**Delay**设置项，通过设置**Frequency**调整自动续写的触发频次。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/07/v3/eeu2rdNhSZeqvJsfF5F-3A/zh-cn_image_0000002602186825.png?HW-CC-KV=V1&HW-CC-Date=20260611T072227Z&HW-CC-Expire=86400&HW-CC-Sign=BB8C820FDBE667AD9B105FE4A0966AD8F24FD0AD817AD6369FA21830395E4E59)

**DevEco Studio 6.1.0 Beta2以下版本**

* **Enable inline generation**（行内续写）：在编码时稍作停顿，CodeGenie将在当前代码行即时续写代码。
* **Enable snippet generation**（片段续写）：输入回车，CodeGenie将根据上下文生成代码片段。
* 在编辑区输入**Alt+C**快捷键（macOS上为**Option+C**）触发代码续写。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e2/v3/hPPPHc1WQcK5DFiSTf2zpg/zh-cn_image_0000002571547294.png?HW-CC-KV=V1&HW-CC-Date=20260611T072227Z&HW-CC-Expire=86400&HW-CC-Sign=1C86F86D293EF8AE156EDEC10F6A0A2655847B4250F96B037B4B4E3AC9A5A0EC)

### 续写采纳

**续写内容采纳方式****：**

* 可通过按**Ta****b**键采纳该内容。
* **Ctrl + ↓（**macOS中为**Command + ↓****）**逐行采纳该内容。
* **Ctrl + →****（**macOS中为**Option + →****）**逐单词采纳该内容。
* 通过按**ESC**键忽略该内容。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8e/v3/NKafYXAxSSKLKF45Nod4_g/zh-cn_image_0000002571547292.png?HW-CC-KV=V1&HW-CC-Date=20260611T072227Z&HW-CC-Expire=86400&HW-CC-Sign=C81C77F0F8E10D9F24A1110128A6200B237F143DF922CD9C8C29BE4359BBC9B0)

**CodeGenie续写常用快捷键如下：**

|  |  |  |
| --- | --- | --- |
| **操作** | **macOS** | **Windows** |
| 触发多行代码续写 | Enter、Option+C | Enter、Alt+C |
| 触发单行代码续写 | Option+X | Alt+X |
| 采纳续写生成的代码 | Tab | Tab |
| 忽略续写生成的代码 | Esc | Esc |
| 查看上一个代码续写结果 | Option +[ | Alt + [ |
| 查看下一个代码续写结果 | Option + ] | Alt + ] |
| 重新生成代码内容（最多支持重新生成5次） | Option + R | Alt + R |
| 代码逐行采纳 | Command + ↓ | Ctrl + ↓ |
| 代码逐单词采纳 | Option + → | Ctrl + → |
