---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-skills
title: 技能（Skills）配置
breadcrumb: 指南 > 使用AI智能辅助编程 > 自定义智能体配置 > 技能（Skills）配置
category: harmonyos-guides
scraped_at: 2026-06-11T15:22:40+08:00
doc_updated_at: 2026-06-09
content_hash: sha256:44081eaaf8bdc289d097505b0b1b6289dac81fff66e9305e6e2e3d7cce43dc4d
---

## 功能介绍

在日常工作中，我们经常需要处理重复性任务，如调整文档结构、撰写周报告等，每次都需要输入格式要求、偏好、操作流程，这种模式不仅耗时，也容易遗漏关键细节。Skills是一份标准化的教程，会指导CodeGenie面对任务时如何思考、遵循什么步骤、输出什么格式、注意事项是什么。开发者只需要定义一次，CodeGenie便能在后续的每次对话中自动识别并应用，实现“一次定义，长期稳定复用”效果。

Skills实际是一个包含SKILL.md文件（区分大小写）的文件夹，在SKILL.md文件中以自然语言描述技能的名称、触发条件和执行步骤，让开发者能快速定义自动化工作流。SKILL.md文件写作时，严格遵循业界YAML Frontmatter（元数据） + Markdown Body（正文） 的统一规范，以及要确保内容结构清晰、触发词准确、没有错误处理，提升Skill可维护和可复用性，使Agent能够稳定执行。

从DevEco Studio 6.1.0 Release（6.1.0.830）版本开始，CodeGenie支持导入Global Skills（全局技能）和Project Skills（项目技能）两种。其中，Global Skills支持当前用户在本地所有项目中使用，不可跨设备同步；Project Skills适用于当前项目。开发者根据业务需要导入对应的Skills。

### 使用约束

* 当前自定义Agent和HarmonyOS Act智能体支持使用Skills。
* SKILL.md中name的要求：长度不超过64个字符，由小写字母，数字和-组成，不能以-开头或结尾，不能包含连续的-，与所在文件夹命名一致。
* SKILL.md中description的要求：长度不超过1024个字符。
* SKILL.md中正文指令的要求：长度不超过32768个字符。
* SKILL.md所在文件夹的要求：大小不超过100MB。

## 操作步骤

1. 点击界面右上方![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bf/v3/Aes0hzseTtW058F_yRL8Ww/zh-cn_image_0000002571387374.png?HW-CC-KV=V1&HW-CC-Date=20260611T072239Z&HW-CC-Expire=86400&HW-CC-Sign=E98741EFB09A8C2EF0EBABA1086E695D86A26B4CB0435F7FDC5BDC7B33CAB008)按钮，或者点击界面右上方**Settings**![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a1/v3/mXo2ivWCS0mtwvcuDY45xg/zh-cn_image_0000002571546998.png?HW-CC-KV=V1&HW-CC-Date=20260611T072239Z&HW-CC-Expire=86400&HW-CC-Sign=B2645285404F3B1AD6DE3316FF49C547BF06E932E9CC55C9B957A41CA933E129)按钮，选择**Skills**，进入配置页面。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6a/v3/IA7PU1pPStClm5-mVZ7qtA/zh-cn_image_0000002571387360.png?HW-CC-KV=V1&HW-CC-Date=20260611T072239Z&HW-CC-Expire=86400&HW-CC-Sign=DA470943B810E53FA0E97AC6B213FE679E4AD2FC873AA15D6AD38B7F21BF7FB9 "点击放大")
2. 在**Global Skills**或**Project Skills**下，首次导入时，点击**Import**导入技能文件；若已存在技能文件，点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/13/v3/BvsEBaByQySS9893oIw_mA/zh-cn_image_0000002571547000.png?HW-CC-KV=V1&HW-CC-Date=20260611T072239Z&HW-CC-Expire=86400&HW-CC-Sign=4CFD38D892C2D041E3272148858CD899FDBB4253B8077EB74F41D6F8829C8CD7)按钮进行导入。

   说明

   * 若选择的文件夹中存在SKILL.md，则作为单个skill导入。
   * 若选择的文件夹中不存在SKILL.md，则遍历下一级文件夹，检查下一级文件夹中是否包含SKILL.md，遍历到的SKILL.md将作为skill导入。若下一级文件夹遍历出多个SKILL.md，将批量导入。仅支持遍历所选择文件夹的下一级，不支持更深层级的遍历。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dc/v3/L5a6NJYkTOyV6AC7nDG0WQ/zh-cn_image_0000002571547002.png?HW-CC-KV=V1&HW-CC-Date=20260611T072239Z&HW-CC-Expire=86400&HW-CC-Sign=FDC231B2C30EF04D7B49A300738CE4C1541E0B66FD26AEAD53E56855D509C4BD "点击放大")
3. 在**Global Skills**和**Project Skills**列表中，显示已导入的技能信息，包括技能名称（如openharmony-build）、描述信息、启用状态。同时，将鼠标悬浮在技能信息上会显示编辑和删除的操作按钮，点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7e/v3/JFtRUnsBT3yimD3EoAHGtg/zh-cn_image_0000002571547008.png?HW-CC-KV=V1&HW-CC-Date=20260611T072239Z&HW-CC-Expire=86400&HW-CC-Sign=4C986D1AE7A78821BA9AF0BD3E0D2CF6F1A4A967F7CFFAEC4B37066A3557EC32)可在代码编辑区打开SKILL.md文件。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/57/v3/vDi78OsFQ6yuyf03PHjDcQ/zh-cn_image_0000002571387368.png?HW-CC-KV=V1&HW-CC-Date=20260611T072239Z&HW-CC-Expire=86400&HW-CC-Sign=8F4D7BD7592139E1CAC590D080CFB91C76D7F8032CF6FA6448343DD087A49C3A "点击放大")
4. 返回CodeGenie对话框调用Skills，在对话框输入时需要带有技能的name（如openharmony-build）。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1a/v3/VK46iFGOTgqnmG4jntSZFw/zh-cn_image_0000002571387370.png?HW-CC-KV=V1&HW-CC-Date=20260611T072239Z&HW-CC-Expire=86400&HW-CC-Sign=C761FF570914D7EBE497A2DAA208BAF94B2BE5AF42117108958A7146001EB592)
