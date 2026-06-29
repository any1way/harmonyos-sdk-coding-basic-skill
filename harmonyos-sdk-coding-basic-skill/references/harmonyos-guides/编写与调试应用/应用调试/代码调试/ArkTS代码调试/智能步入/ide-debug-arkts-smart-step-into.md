---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-debug-arkts-smart-step-into
title: 智能步入
breadcrumb: 指南 > 编写与调试应用 > 应用调试 > 代码调试 > ArkTS代码调试 > 智能步入
category: harmonyos-guides
scraped_at: 2026-06-11T15:29:04+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:42c284c9af5fd23c66ec85e98fb23b796988e0ee2b3e7a484c7f0fcd790d3b20
---

当编辑器上一行存在多个函数嵌套或调用时，开发者可以通过Smart Step Into的能力来步入到想要调试的函数内，如果在调试时想跳过某些文件，也可以自定义需要跳过的文件列表。

## 智能步入

1. 启动调试，如果断点所在的一行内存在多个方法调用，可以通过点击调试窗口的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3e/v3/ZIuAuPgwRv6naAEvyRtfgg/zh-cn_image_0000002602066667.png?HW-CC-KV=V1&HW-CC-Date=20260611T072903Z&HW-CC-Expire=86400&HW-CC-Sign=D014788FC18CF9E8F1EB17E19C2DC91F0F6F4AA7593887E5D40399F947B34635)按钮或快捷键Shift + F7高亮展示可进入函数。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/32/v3/PX5Y0ze7QPe8RgCr0L9kQw/zh-cn_image_0000002602186723.png?HW-CC-KV=V1&HW-CC-Date=20260611T072903Z&HW-CC-Expire=86400&HW-CC-Sign=58E6186E4BA9B0F2DBD1A09FCCD522558D78973C47C00889356281E996E92E31)
2. 点击其中一个函数即可步入。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/93/v3/MWE8NNvkTPWX0ytl8ERwVg/zh-cn_image_0000002571387548.png?HW-CC-KV=V1&HW-CC-Date=20260611T072903Z&HW-CC-Expire=86400&HW-CC-Sign=0D6724B1E41072A92B60A9BCB7A3DCB489DAA2AAD30D2AA8DC2FEE698F31837F)

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/df/v3/Y8HBQN2BShOfDE2P6-en9g/zh-cn_image_0000002571387550.png?HW-CC-KV=V1&HW-CC-Date=20260611T072903Z&HW-CC-Expire=86400&HW-CC-Sign=6E0DC3DDE0A5A1A639E7048B9FACFCC33687D1D77FA224EFEE5C4521A30E753D)

## 过滤脚本文件

1. 点击**File > Settings**（macOS为**DevEco Studio > Preferences/Settings**） **>** **Build, Execution, Deployment > Debugger > Stepping**，勾选**Do not step into ArkTS scripts**， 可在调试时禁止智能步入某些脚本。使用工具栏按钮管理要跳过的脚本列表。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ed/v3/SAFy8kYbRwClR13CkoQx9A/zh-cn_image_0000002602066665.png?HW-CC-KV=V1&HW-CC-Date=20260611T072903Z&HW-CC-Expire=86400&HW-CC-Sign=57413B6FAFF7B9D4DBC466840E94E6D4D798971759E33E4B9BEF9E7EABEB6FE4)
2. 单击 **+** 按钮可添加新的脚本过滤器。在打开的对话框中，输入要跳过的文件名称或使用通配符。例如，如果要始终跳过 JavaScript文件，请输入 \*.js。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6d/v3/xKz2dW9RQLWEoBUoB4m8dg/zh-cn_image_0000002571547188.png?HW-CC-KV=V1&HW-CC-Date=20260611T072903Z&HW-CC-Expire=86400&HW-CC-Sign=713C7733F9F793640813CA868AC2AFE673C914119F5E788F902630A6EEC33ABB)
