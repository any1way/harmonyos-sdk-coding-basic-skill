---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-186
title: 报错“ENOENT: no such file or directory, uv_cwd”
breadcrumb: FAQ > DevEco Studio > 编译构建 > 报错“ENOENT: no such file or directory, uv_cwd”
category: harmonyos-faqs
scraped_at: 2026-06-12T10:43:37+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:e34f109e6992855699ff9141ba24f03faab320004b6f30181eef4920c42c238d
---

**问题现象**

先构建一次项目，然后强制删除项目后手动恢复再重新构建，出现类似如下报错：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c0/v3/s2S5h3ybTVSTbyuSEolRTw/zh-cn_image_0000002342994341.png?HW-CC-KV=V1&HW-CC-Date=20260612T024336Z&HW-CC-Expire=86400&HW-CC-Sign=E09A0032B47B17D1C46702AF2ED32B4C6F8D372BF0D9CE0432D220B60A78D22D)

**问题原因**

在Node.js进程运行时，process.cwd()方法返回的是该进程启动时或通过process.chdir()更改后的当前工作目录。若此进程的当前工作目录被强制删除（如用户手动删除项目文件夹），那么后续所有依赖于该路径的操作（如文件读取、目录遍历等）都将失败并抛出错误，因为其引用的目录已不存在。

**解决措施一**

关闭所有Node.js进程再重新进行构建即可。

Linux系统执行:

```
1. pkill node
```

Mac系统执行:

```
1. killall node
```

Windows系统执行:

```
1. taskkill /F /IM node.exe
```

**解决措施二**

流水线打包推荐使用no-daemon模式:

运行hvigorw assemble app/hvigorw assemble hap时修改--daemon 为--no-daemon
