---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-6
title: 编译报错“Module 'xxx' has no exported member 'yyy'”
breadcrumb: FAQ > DevEco Studio > 编译构建 > 编译报错“Module 'xxx' has no exported member 'yyy'”
category: harmonyos-faqs
scraped_at: 2026-06-12T10:41:03+08:00
doc_updated_at: 2026-06-05
content_hash: sha256:330af8c568d207658c815543d4e0cf4cf5939564a8a7ef4ada8087fe5c025521
---

**问题现象**

Stage模板工程编译构建失败，提示 “Module 'xxx' has no exported member 'yyy'” 并且“yyy”符号是由export \* from 'x.js'语法从js文件中导出。

**解决措施**

由于当前Stage工程编译构建期的语法校验工具对js文件不作检查，导致无法正确识别通过export \* from 'x.js'导出的符号，因此在引用这些符号时会提示“Module 'xxx' has no exported member 'yyy'”的错误信息。

如果遇到类似问题，尝试以下解决方法：

* 方法1（推荐使用）： 使用符号显式导出语法，从js文件中re-export符号 。

  export { yyy } from 'x.js'

* 方法2：新增x.js对应的声明文件（.d.ts），并在引用时不指定后缀。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8f/v3/8woq7-BnS5KeygH-ssy9DA/zh-cn_image_0000002229758485.png?HW-CC-KV=V1&HW-CC-Date=20260612T024102Z&HW-CC-Expire=86400&HW-CC-Sign=4BAA56C18446AE3676A0635B196A7DF89AA430DEFC246486E89B613521F1419A)
