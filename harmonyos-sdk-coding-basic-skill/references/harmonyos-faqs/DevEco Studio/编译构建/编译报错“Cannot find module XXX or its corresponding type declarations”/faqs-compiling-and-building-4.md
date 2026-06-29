---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-4
title: 编译报错“Cannot find module XXX or its corresponding type declarations”
breadcrumb: FAQ > DevEco Studio > 编译构建 > 编译报错“Cannot find module XXX or its corresponding type declarations”
category: harmonyos-faqs
scraped_at: 2026-06-12T10:41:01+08:00
doc_updated_at: 2026-06-05
content_hash: sha256:dd01ff8af6ccde0bccf2ebc9b655a8fce2e512a47c067993ad26cd19bcc34966
---

* **场景一：**

  **问题现象**

  Stage模板工程编译引用native文件(.so) 提示“Cannot find module XXX or its corresponding type declarations.”。

  **解决措施**

  当前Stage工程在编译构建阶段新增对native文件（.so）导出符号的语法校验。如果现有工程引用了没有对应声明文件（.d.ts）的native文件（.so），语法校验工具会报错，提示找不到对应的声明文件。

  如果出现类似问题，尝试以下解决方法：

  1. 在对应cpp目录下新建types/libxxx目录，并在该目录下新增index.d.ts用于声明native文件的类型符号；新增oh-package.json5配置文件用于校验工具的模块查询。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6f/v3/5MG9w2olRhC9R1qMtjCwkg/zh-cn_image_0000002229604373.png?HW-CC-KV=V1&HW-CC-Date=20260612T024100Z&HW-CC-Expire=86400&HW-CC-Sign=774D2A0DFDC7F0DD978E59DC687EA64BDCCD4073BC11EC998238DDBD2B035F91)

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f6/v3/NqgjezBKRAy83k9T3MBC1g/zh-cn_image_0000002194158980.png?HW-CC-KV=V1&HW-CC-Date=20260612T024100Z&HW-CC-Expire=86400&HW-CC-Sign=984056B42BECF4E2DB619B84A4DBB1B2F895A498A736EB00A5018CD56A34CD6A)
  2. 在native文件引用的模块内的oh-package.json5中添加native文件的本地依赖，并根据DevEco Studio提示点击\*\*Sync Now\*\*同步工程，下图以entry模块引用native文件为例。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/48/v3/2NTrWXR3TK2Oot6CoHHrDg/zh-cn_image_0000002194318572.png?HW-CC-KV=V1&HW-CC-Date=20260612T024100Z&HW-CC-Expire=86400&HW-CC-Sign=CF337293931E493871BBDD744A48AA0C1F2EF7218EE81B168B74169E270422AB)

* **场景二：**

  **问题现象**

  API 11 Stage模板工程编译失败，提示“Cannot find module '@kit.xxx' or its corresponding type declarations”。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/67/v3/nsokE9HWSyaSkQPA5via6Q/zh-cn_image_0000002229758849.png?HW-CC-KV=V1&HW-CC-Date=20260612T024100Z&HW-CC-Expire=86400&HW-CC-Sign=ECE7C8B9735C0F733790386EECB82499DCE053BB117A3EC5E00AD157B5CCFEE3)

  **问题原因**

  出现该问题的原因是使用DevEco Studio NEXT Developer Preview1及之后版本。新创建的API 11 Stage模型的模板文件中，import方式改为import xxx from '@kit.xxx'。若SDK使用的是HarmonyOS NEXT Developer Preview1之前的版本，将会出现编译报错，因为旧的SDK不支持此类方式导入。

  **解决措施**

  如果出现类似问题，需要对SDK进行更新或更新DevEco Studio。

  + 如果使用的是DevEco Studio NEXT Developer Preview1至HarmonyOS NEXT Developer Beta1（5.0.3.300）之间的版本，在菜单栏点击**Tool > SDK Manager**，将SDK更新至HarmonyOS NEXT Developer Preview1及以上版本后，重新进行编译。
  + 如果使用的是HarmonyOS NEXT Developer Beta1（5.0.3.300）及以上的版本，SDK随DevEco Studio软件包安装，无需单独下载，请在[下载中心](https://developer.huawei.com/consumer/cn/download/)下载并使用新版本DevEco Studio。
* **场景三：**

  **问题现象**

  引用第三方包，构建失败，提示“Cannot find module 'xxx' or its corresponding type declarations”。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2d/v3/sXJL8ps_TwyLqt1opGAtFg/zh-cn_image_0000002229758853.png?HW-CC-KV=V1&HW-CC-Date=20260612T024100Z&HW-CC-Expire=86400&HW-CC-Sign=63450A1AF7079701E2805693370F11CBA74F02751C949BCC2E153F621138A9D3)

  **解决措施**

  进入模块级或工程级的oh-package.json5文件，检查第三方包是否已安装。若未安装，执行ohpm install安装。若已安装，检查“main”字段是否配置正确。若未配置或配置错误，需配置为正确的入口文件。
* **场景四：**

  **问题现象**

  包路径被混淆，代码中又是在引用包路径后面拼接了路径，导致模块引用不到而报错。

  例如：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cd/v3/7Sc_Q7BoR2qw6lC9gmaeqw/zh-cn_image_0000002194158984.png?HW-CC-KV=V1&HW-CC-Date=20260612T024100Z&HW-CC-Expire=86400&HW-CC-Sign=11A5C2ABEFDF6F6117D54F793F6D1CD79460DD1D370B145232CE6F2FCA385EBB)

  代码中这样引用

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8c/v3/-JdI8SAXT3OueqyCTMnd3A/zh-cn_image_0000002229758861.png?HW-CC-KV=V1&HW-CC-Date=20260612T024100Z&HW-CC-Expire=86400&HW-CC-Sign=64F8A468CC8C45D748767722FAE389B36EB74953C893744ED71FBE7A4526A878)这样引用会找不到模块，导致报错。

  **解决措施**

  修改引用方式，采用推荐的方式。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ab/v3/VjkI8-JBRn-4ttuCAylnVw/zh-cn_image_0000002194158972.png?HW-CC-KV=V1&HW-CC-Date=20260612T024100Z&HW-CC-Expire=86400&HW-CC-Sign=0BC30CDCF507136AAA63DA6902AAF06BDC740C550DA91F8B15EDBADD9D00AB79)
* **场景五：**

  **问题现象**

  被引用模块oh-package.json5配置有误，执行了ohpm install 并且成功地安装了依赖，但是还报错模块找不到。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d9/v3/6BUxLk46QmCUV7hSldrjBA/zh-cn_image_0000002194158976.png?HW-CC-KV=V1&HW-CC-Date=20260612T024100Z&HW-CC-Expire=86400&HW-CC-Sign=DE40B74DF662A16D43D5429DC3E5ED663C1E57172E9D67F2A087E6558EFA3D38)

  被引用模块的 oh-package.json5 中配置了错误的types字段。

  该字段优先于main字段。 如果 types 字段配置的不存在，就会报错模块找不到。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0a/v3/-VL_-rfvRcOmr0NmyqEULQ/zh-cn_image_0000002229604353.png?HW-CC-KV=V1&HW-CC-Date=20260612T024100Z&HW-CC-Expire=86400&HW-CC-Sign=5026F4E8046D6F4C44A8CE52FDF63C5A698EE15F3A808EA8EF129FCF9E668F76)

  **解决措施**

  如果该包中没有d.ets声明，可以删除这个字段。配置错误或不存在会导致报错。
* **场景六：**

  **问题现象**

  oh-package.json5中dependencies中引入模块的名称和实际使用时import的不一致。

  在代码中“import”时，应使用大写的“HAR”而不是“dependencies”里配置的“har”。务必保持完全一致，否则在Linux系统中会报错，提示模块找不到。

  **解决措施**

  引入和使用改成一致。
* **场景七：**

  **问题现象**

  引用模块的oh-package.json5中main字段值和实际的文件名称大小写不一致。

  **解决措施**

  将main字段和实际文件名称大小写改为一致。
* **场景八**：

  **问题现象**

  Stage模板工程编译构建失败，提示“Cannot find module '@bundle:rollup\_plugin\_ignore\_empty\_module\_placeholder' or its corresponding type declarations”。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f7/v3/e0fbDusqTbGaycv5PaeRug/zh-cn_image_0000002229758841.png?HW-CC-KV=V1&HW-CC-Date=20260612T024100Z&HW-CC-Expire=86400&HW-CC-Sign=D624A0FF43076BF95651551150CD5BB2F97A45C1E3FA34A63BBFF634D8F871A2)

  **解决措施**

  该问题源于工程引用了无对应实现文件的.d.ts声明文件。

  1. 在build目录搜索`rollup\_plugin\_ignore\_empty\_module\_placeholder`定位问题模块。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9d/v3/3gr1qnxETZWCkciVoTS5eg/zh-cn_image_0000002194158956.png?HW-CC-KV=V1&HW-CC-Date=20260612T024100Z&HW-CC-Expire=86400&HW-CC-Sign=482B9B76368BD0158F474B19C556629D05A991592BFC5139A9E5D578BC105F2D)

     在输入栏中输入“rollup\_plugin\_ignore\_empty\_module\_placeholder”，找到问题模块的中间文件。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e5/v3/xLF16U8RRDaZ1UPW5iRBTg/zh-cn_image_0000002194158964.png?HW-CC-KV=V1&HW-CC-Date=20260612T024100Z&HW-CC-Expire=86400&HW-CC-Sign=DBD792D1B45C09D90CE9245B11967A5FD5762E363227ABF0E118C449B7136F01)
  2. 在引用类型文件中通过添加type显式声明符号类型。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f1/v3/k2a2WZ6wRY28k5n3pvocXw/zh-cn_image_0000002229758865.png?HW-CC-KV=V1&HW-CC-Date=20260612T024100Z&HW-CC-Expire=86400&HW-CC-Sign=2B4946EF9C2106E12900C4D3A34A3E07C44B6F2F55354878D18CDAAA869389E2)
  3. 同时排查是否从d.ts/d.ets中引用值类型符号。禁止在声明文件中声明值变量。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/34/v3/QsEoHcl3ScC59_Qqg9ZhIg/zh-cn_image_0000002194158968.png?HW-CC-KV=V1&HW-CC-Date=20260612T024100Z&HW-CC-Expire=86400&HW-CC-Sign=8354D000819CC9F1BFDA38CDD5B69A3C067CAB3408AFFE635849886037B56F84)
