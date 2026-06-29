---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-arktsdoc-generation
title: 文档生成
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 生成ArkTSDoc文档 > 文档生成
category: harmonyos-guides
scraped_at: 2026-06-11T15:28:06+08:00
doc_updated_at: 2026-05-14
content_hash: sha256:ebad25d39c2b07a8e9719f76011ca7e15fa7b846a410051b75fc3681e7018d65
---
DevEco Studio支持通过Generate ArkTSDoc功能，将代码文件中变量、方法、接口、类等需要对外暴露的信息快速生成相应的参考文档。

从DevEco Studio 6.1.0 Beta1版本开始，ArkTSDoc功能支持多模块导出，以及导出时支持设置不需要被导出的目录。

说明

* 当前支持对工程或目录下.ets/.ts/.js/.md格式文件生成ArkTSDoc文档。
* 文件中export的变量、方法、接口、类等将生成相应的ArkTSDoc文档，未export的对象不支持生成。
* 若选择对工程/目录整体导出ArkTSDoc文档，生成后的ArkTSDoc文档目录和原目录结构一致。

## 生成步骤

1. 在菜单栏选择**Tools >** **Generate ArkTSDoc...**进入ArkTSDoc生成界面。
2. 设置生成ArkTSDoc的范围，可选择整个工程、单个模块或多个模块，某个目录或单个文件进行导出。

   点击**Modules**后的下拉箭头，会弹出所有模块，可以选择单个或多个模块作为导出范围。当模块数量较多时，可以使用检索功能，快速定位模块。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7a/v3/FPi0SQirRDWQcVCLrdABjQ/zh-cn_image_0000002571387444.png?HW-CC-KV=V1&HW-CC-Date=20260611T072758Z&HW-CC-Expire=86400&HW-CC-Sign=5D7CA6113394EDA317EF650958E59E9CA1FE8A9F28287BB03B0BD47C92A5C7B8)
3. 在导出时，可以在**Command line arguments**设置无需被导出的目录，使用"-e"子命令进行指定，多个目录使用英文";"分隔，使用"./"开头路径代表项目根路径。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/74/v3/PiA6MszASYG0CEosEYLLaQ/zh-cn_image_0000002602186615.png?HW-CC-KV=V1&HW-CC-Date=20260611T072758Z&HW-CC-Expire=86400&HW-CC-Sign=DB14684AFE2AF32254D8535637B7326C82DD8642DC0D1F9BE4DF01B4D7926864)

   说明

   从DevEco Studio 6.1.0 Release版本开始，**Command line arguments**填写时支持Ant风格的路径匹配模式。在Ant风格中，使用'?'匹配单字符、'\*'匹配单层目录/文件、'\*\*'匹配任意层目录等。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/20/v3/m9HRQReVTIOkXiWy8Sk1tg/zh-cn_image_0000002572141710.png?HW-CC-KV=V1&HW-CC-Date=20260611T072758Z&HW-CC-Expire=86400&HW-CC-Sign=834788C4B798B7EE33C48069F2F21C2A25CA2B932911F6AC596ECA822B03050F)
4. 在**Output directory**中输入导出ArkTSDoc的存储路径后，点击**Generate**。
5. 若勾选**Open generated documentation in browser**选项，在生成ArkTSDoc后，将自动打开相应页面查看生成的文档。配置完毕后点击Generate，开始扫描并生成ArkTSDoc文档。

   生成的ArkTSDoc左侧文档目录和原工程目录结构一致，右侧可点击跳转到当前文件包含的某个变量、方法、接口或类的文档位置。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/df/v3/n_Vv33-wTfiXRa9-FHJ_Nw/zh-cn_image_0000002571547082.png?HW-CC-KV=V1&HW-CC-Date=20260611T072758Z&HW-CC-Expire=86400&HW-CC-Sign=78AD30FE97D7674844AE715E9115C6EBEC371DF2F22CA4B4684336BA81631A8E "点击放大")

   若没有勾选**Open generated documentation in browser**选项，在生成ArkTSDoc后，DevEco Studio右下角弹出对应提示框，可以点击Go to Folder跳转到生成的ArkTSDoc文件夹，用浏览器打开文件夹中index.html文件即可查看ArkTSDoc文档。

## 生成效果示例

**注释格式要求：**当前仅支持“/\*\* \*/”文档注释格式；支持param等[标准标签](../标准标签/ide-arktsdocs-standard-label.md)和myTag等自定义标签生成相应文档。

```
1. /**
2. * Prints "log" logs.
3. *
4. * @param { string } message - Text to print.
5. * @myTag
6. * @since 11
7. */
```

**代码示例：**

```
1. /**
2. * Defines the demo class
3. *
4. * @since 11
5. */
6. export class Demo {
7. /**
8. * Prints "log" logs.
9. *
10. * @param { string } message - Text to print.
11. * @myTag
12. * @since 11
13. */
14. static log(message: string): void {

16. }
17. }
```

**ArkTSDoc文档生成结果：**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/31/v3/iE5haibTSLWO23XQgSOlCw/zh-cn_image_0000002602066561.png?HW-CC-KV=V1&HW-CC-Date=20260611T072758Z&HW-CC-Expire=86400&HW-CC-Sign=8E694654886ACE158F39B138CC50100A133EE467DD8F1901116048920C517CF2 "点击放大")
