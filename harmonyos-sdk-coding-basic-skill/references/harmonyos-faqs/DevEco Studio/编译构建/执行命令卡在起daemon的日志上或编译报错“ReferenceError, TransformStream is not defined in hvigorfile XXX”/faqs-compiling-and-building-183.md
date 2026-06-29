---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-183
title: 执行命令卡在起daemon的日志上或编译报错“ReferenceError, TransformStream is not defined in hvigorfile: XXX”
breadcrumb: FAQ > DevEco Studio > 编译构建 > 执行命令卡在起daemon的日志上或编译报错“ReferenceError, TransformStream is not defined in hvigorfile: XXX”
category: harmonyos-faqs
scraped_at: 2026-06-12T10:43:35+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:b6f6dd0647c131ace3d3b4d4ffad531d3cc3a4088c09f43cfa9ce6009e9d7df2
---
**问题现象**

流水线或命令行中执行命令后在起daemon的日志上：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0a/v3/IKO5DBzYTAygrHAXj0o94A/zh-cn_image_0000002345811941.png?HW-CC-KV=V1&HW-CC-Date=20260612T024333Z&HW-CC-Expire=86400&HW-CC-Sign=B1F6654799577E68C0B0F3FF411A9C33D27D8B0FC488E7427501C75DB7B3AC58)

或者是流水线或命令行中编译报错：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f2/v3/qz1wPR3-RgKzXhlLGT3jRA/zh-cn_image_0000002312015854.png?HW-CC-KV=V1&HW-CC-Date=20260612T024333Z&HW-CC-Expire=86400&HW-CC-Sign=8E620228E97FE2BD4D97BE78FC8675BFA1ED55AC4FDD8F65C991076E23CADEA3)

**问题原因**

编译不支持低于v18.0.0的Node.js版本。相关配置查看[配置Node.js环境变量](../../../../harmonyos-guides/命令行工具/搭建流水线/ide-command-line-building-app.md#section159168531288)。

**解决措施**

1.确认流水线或计算机配置的Node.js的版本。

Windows通过cmd或Powershell运行， Mac或Linux系统通过终端（Terminal）运行：

```
1. node -v
```

查看输出：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1f/v3/irMenY-0RuKPUdeehDv8lg/zh-cn_image_0000002284561689.png?HW-CC-KV=V1&HW-CC-Date=20260612T024333Z&HW-CC-Expire=86400&HW-CC-Sign=1362C241BD7F5BA2084FE5EACB32ABAD09CA9BF1D5A353AAE03CFF71F220131C)

2.如果流水线或计算机配置的Node.js的版本低于v18.0.0，推荐使用DevEco Studio或Command Line Tools自带的Node.js包来配置系统变量。

Windows系统打开环境变量的配置，将DevEco或Command Line Tool自带的Node.js包的路径添加进系统变量的Path中。如果是通过NODE\_HOME配置的，可以直接修改NODE\_HOME配置的路径。若系统中已存在其他Node.js版本，需将工具自带的Node.js路径添加至Path变量的最前端，确保优先使用该版本；通过NODE\_HOME配置时，需检查Path中是否包含%NODE\_HOME%/bin（Windows）或$NODE\_HOME/bin（Mac/Linux）以确保生效。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/79/v3/qME4kvHyTAO3BhOaGJsiGw/zh-cn_image_0000002284693797.png?HW-CC-KV=V1&HW-CC-Date=20260612T024333Z&HW-CC-Expire=86400&HW-CC-Sign=F3947474DE67E57290F0EDC50333408AFA1AB2D03E5B57D16CC0F53636986DAB)

Mac或Linux系统参考[配置Node.js环境变量](../../../../harmonyos-guides/命令行工具/搭建流水线/ide-command-line-building-app.md#section159168531288)。

DevEco Studio的自带的Node.js的路径为DevEco Studio安装目录/DevEco Studio/tools/node。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e7/v3/VqPBGQXRRAStMweh5_3C2Q/zh-cn_image_0000002284546061.png?HW-CC-KV=V1&HW-CC-Date=20260612T024333Z&HW-CC-Expire=86400&HW-CC-Sign=A79D793FDAC80593690FA208207FCC304DA6CC6D2BF3337D7B0EF64F01CEE405)

Command Line Tools自带的Node.js的路径为Command Line Tools安装路径/command-line-tools/tool/node。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9e/v3/BYDkZ1S-SiKkXCMmO3Ee-w/zh-cn_image_0000002284672673.png?HW-CC-KV=V1&HW-CC-Date=20260612T024333Z&HW-CC-Expire=86400&HW-CC-Sign=D8720B5E77216D18BD0DEDE41F9A36DE3355D74322F5A3F5F00B75CE1EF621E6 "点击放大")

3.将自定义的Node.js版本升级为与DevEco Studio或Command Line Tools自带的Node.js版本一致。通过上述路径运行node -v查看版本，然后在Node.js官方网站中下载对应版本。下载地址为：https://nodejs.org/dist/v18.20.1/。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a8/v3/asJxTl6rQJaDEgjoD6Mk0Q/zh-cn_image_0000002277140989.png?HW-CC-KV=V1&HW-CC-Date=20260612T024333Z&HW-CC-Expire=86400&HW-CC-Sign=7CF0AFAAF1484A0231EF678A6E3331A0701474A2333916E07EC85394609BEFE2)
