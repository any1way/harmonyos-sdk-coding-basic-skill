---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-ocal-knowledge
title: 本地知识库配置
breadcrumb: 指南 > 使用AI智能辅助编程 > 本地知识库配置
category: harmonyos-guides
scraped_at: 2026-06-11T15:22:44+08:00
doc_updated_at: 2026-05-14
content_hash: sha256:2c8c7a19f5d62f5074c7bccfefa67639a4e627c7816dd111d09e1b68e8503d43
---
从DevEco Studio 6.0.0 Beta5开始，CodeGenie允许用户导入设计文档和代码等文件形成文档集，多个文档集组合成本地知识库。智能问答时，根据用户输入内容检索本地知识库以提升AI生成的能力。

## 操作步骤

1. 点击**File > Settings**（macOS为**DevEco Studio > Preferences/Settings**） **> CodeGenie****> Knowledge >** **Docs**，或在DevEco Studio右侧边栏点击**CodeGenie**（或输入快捷键**Alt/Option+U**） **>** **@****Add Context** **> Docs > Set Local Knowledge Base**，进入配置页面。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c0/v3/4SUF7VD-S_y1BB7BLq8BgQ/zh-cn_image_0000002602066349.png?HW-CC-KV=V1&HW-CC-Date=20260611T072243Z&HW-CC-Expire=86400&HW-CC-Sign=40C56ABF825211F0DD2F63334421AB71AD70B7AEC3B035E090CD72C52D5BDF2D)
2. 首次打开时，点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/45/v3/oX_JieR6QtSZgkzXL6dZlQ/zh-cn_image_0000002571387232.png?HW-CC-KV=V1&HW-CC-Date=20260611T072243Z&HW-CC-Expire=86400&HW-CC-Sign=24E4B30216E7C28D0F74EBD1D1BD10931F9FE3DB1D99220F7E5133A80591810C)按钮，填写相关信息，创建文档集。
   * **Knowledge Base Path**：知识库保存路径。在同一个路径下保存的文档集，会形成一个知识库。
   * **Document set name**：文档集名称。
   * **Description**：可选，文档集描述。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9e/v3/0YhJGZL6Q1-Geg9a7qvhkQ/zh-cn_image_0000002602186405.png?HW-CC-KV=V1&HW-CC-Date=20260611T072243Z&HW-CC-Expire=86400&HW-CC-Sign=FC3A247DA66D41B30E69395F70C36FFEB04EF69622874C948D5A130B0E74AA73)
3. 点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ba/v3/kUmU8xNrQiaEnvsLUtASAw/zh-cn_image_0000002571387236.png?HW-CC-KV=V1&HW-CC-Date=20260611T072243Z&HW-CC-Expire=86400&HW-CC-Sign=A4F7BC8FF30B28C30662D3EF980BBA49B279C61B11001CDB7E45A1C09B9B2B40)按钮，添加文档集中的文件，添加成功的文件在下方展示。

   说明

   1. 支持的文件格式：txt、md、json、html、cpp、ets、ts、js。
   2. 单个文档集中文件个数：不超过1000个。
   3. 单个文件大小：不超过10M。
   4. 单个知识库中文档集个数：不超过20个。
   5. 单个知识库大小：不超过50M。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/03/v3/RzOIGLD4TRudUe9C61zjGA/zh-cn_image_0000002602186407.png?HW-CC-KV=V1&HW-CC-Date=20260611T072243Z&HW-CC-Expire=86400&HW-CC-Sign=27B9700366BFE262EA89447C923E3921AD0ED3F95F413734C2CC07DEDB8E2635)
4. 点击“**OK**”，完成本地知识库配置和同步，在DevEco Studio页面下方**Storing document set**可查看同步进度。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/94/v3/JUDG3pggSFKmofchkbccPQ/zh-cn_image_0000002571546870.png?HW-CC-KV=V1&HW-CC-Date=20260611T072243Z&HW-CC-Expire=86400&HW-CC-Sign=D2310A645C3E6C77391450864111FE5C6A214615330906192D4B667FAE9956D3 "点击放大")
5. 同步完成后，在对话框中输入**@**符号选择**Docs** ，或点击上方**@****Add Context** **> Docs** ，选择需要的文档集。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f2/v3/LwlPD0seRf6sY3Z83NNxPg/zh-cn_image_0000002602066353.png?HW-CC-KV=V1&HW-CC-Date=20260611T072243Z&HW-CC-Expire=86400&HW-CC-Sign=7364305EAEB6F33AEA04191E029D715578715F3B604301A572452B3872D3EDF2)
6. 选择代码文件进行问答，具体请参考[智能问答](../智能问答/ide-harmonyos-ask.md)
