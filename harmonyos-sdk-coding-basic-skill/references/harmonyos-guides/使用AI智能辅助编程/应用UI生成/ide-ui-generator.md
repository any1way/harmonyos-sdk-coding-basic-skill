---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-ui-generator
title: 应用UI生成
breadcrumb: 指南 > 使用AI智能辅助编程 > 应用UI生成
category: harmonyos-guides
scraped_at: 2026-06-11T15:22:33+08:00
doc_updated_at: 2026-06-10
content_hash: sha256:e20e9cedcc0019ece0893f6a49241621a45f22ef56a535275d5e3cdb98500ef5
---

UI Generator用于快速生成可编译、可运行的HarmonyOS UI工程，支持基于已有UI布局文件（XML），快速生成对应的HarmonyOS UI代码，其中包含HarmonyOS基础工程、页面布局、组件及属性和资源文件等。

## 使用约束

建议使用DevEco Studio 5.0.3.700及以上版本。

## 启用插件

1. 在DevEco Studio菜单栏，点击**File > Setting****s...**（macOS为**DevEco Studio > Preferences****/Settings**）**> Plugins**，在Installed列表中找到UI Generator插件，点击**Enable**启用。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/82/v3/ks3HMH8MRYydSGtwIeOmug/zh-cn_image_0000002571547080.png?HW-CC-KV=V1&HW-CC-Date=20260611T072232Z&HW-CC-Expire=86400&HW-CC-Sign=7B9F3B7DC969CEAD7C4A26E3855244FE018AA01ABF8EF403F9E67D91F2856CAA)
2. 单击OK并关闭设置窗口，插件启用成功。

## 开始使用

1. 在DevEco Studio菜单栏点击**Tools > Generate Project From...**打开UI Generator工具，首次使用需要阅读并确认用户协议，确认后可继续使用。
2. 输入待配置项路径，点击**Next**进入下一步。

   | 待配置项 | 说明 |
   | --- | --- |
   | Installation package path | 待转换的APK应用包的路径，请提供未混淆的Debug版本应用包。 |
   | SDK path | 等于或高于编译应用包所使用版本的SDK路径。 |
   | Git Bash path | Git Bash工具存放路径。若本地已下载安装Git Bash，插件将自动获取其路径。 |

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5b/v3/UYytS-LuS5Sqv4fu-gM7YA/zh-cn_image_0000002602066555.png?HW-CC-KV=V1&HW-CC-Date=20260611T072232Z&HW-CC-Expire=86400&HW-CC-Sign=32DD15CE651FAC8706999914CC318627C7D64B36A79C681CBA3CAE88B7A0A943)
3. 选择将要生成的XML页面（可在搜索框进行搜索），勾选后点击向右箭头将选中的XML导入至右侧。点击**Next**开始生成。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/87/v3/x3a5U1d7TUyaONb_nn4xww/zh-cn_image_0000002602186607.png?HW-CC-KV=V1&HW-CC-Date=20260611T072232Z&HW-CC-Expire=86400&HW-CC-Sign=F3E1653D211A228C568853718E18B21A4CD07E45B9A86883123F0DFFA0690936)
4. 配置输出工程待配置项，点击**Finish**进行生成。

   | 待配置项 | 说明 |
   | --- | --- |
   | Destination Path | 生成新工程的保存路径（默认生成到用户目录下UIGenerationProjects，用户可根据需要自行更改） |
   | Compatible SDK | 生成的新工程所使用的SDK版本 |

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/df/v3/oQYKuldXSN6i9nqh0Hve8w/zh-cn_image_0000002571547074.png?HW-CC-KV=V1&HW-CC-Date=20260611T072232Z&HW-CC-Expire=86400&HW-CC-Sign=4CAF2420F537D7423C9A1E644BAA0BC84DE950333ECE1D8750E1D505FFBFB24E)
5. （可选）如果所选XML无有效根节点，需要选择根节点信息。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e2/v3/M23KCDmJSG6-jLrQwcPowg/zh-cn_image_0000002571547078.png?HW-CC-KV=V1&HW-CC-Date=20260611T072232Z&HW-CC-Expire=86400&HW-CC-Sign=4462EF72C181C63FB17B77A9A563AEF868B25C2FEA034AE32B1C22F37741F77C)
6. 点击**Finish**，在弹窗中点击确认，打开新工程。

   生成的页面位于entry > src > main > ets > pages目录下，可以点击Previewer查看页面预览效果。不支持生成的组件、属性会以注释的形式给出，方便后续定位修改。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c3/v3/oNtM3e_-Q6SG44k8IvqIAA/zh-cn_image_0000002602066559.png?HW-CC-KV=V1&HW-CC-Date=20260611T072232Z&HW-CC-Expire=86400&HW-CC-Sign=371C3FA7C05A74D556E433FDF5AC750870CBFF2B4D224D681B9CE76DA8A4378B)
7. 生成的新工程内的entry > src > main > resources目录包含文本、图像、颜色资源。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/db/v3/NBKWLNFAS-Gg5BL_dsmc2Q/zh-cn_image_0000002571387442.png?HW-CC-KV=V1&HW-CC-Date=20260611T072232Z&HW-CC-Expire=86400&HW-CC-Sign=F83D0D3A730C4980F62DDA017A4F56693A4A38687D24B6FE6796C2F6B14DC09D "点击放大")

   更多操作指导，请参考视频课程：[毕方HarmonyOS UI代码生成工具](https://developer.huawei.com/consumer/cn/training/course/live/C101731322888995220)。
