---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hvigor-so
title: 预构建库快速链接
breadcrumb: 指南 > 构建应用 > 配置构建流程 > 预构建库快速链接
category: harmonyos-guides
scraped_at: 2026-06-11T15:30:35+08:00
doc_updated_at: 2026-06-10
content_hash: sha256:6bf2a43e24e01ca1871cd6ed8a773e097e6fd682e1f17de65b371d0ced0154af
---

在工程中使用依赖模块时，如果希望使用依赖模块中native相关的so库与接口文件（.h/.hpp），Hvigor提供了快速链接功能。

## 头文件

* 对于共享包：

  在共享包中include目录下如存在.h等接口文件，Hvigor会自动将此目录添加到CMake接口目录中，无需手动添加。
* 对于本地依赖模块：

  在本地依赖模块中如存在.h等接口文件，可通过在build-profile.json5文件buildOption/nativeLib/headerPath中指定接口文件目录。

  ```
  1. "buildOption": {
  2. "nativeLib": {
  3. "headerPath": "src/main/cpp/include"
  4. }
  5. }
  ```

## 预构建库

在工程中引用了共享包/本地依赖模块中的so库，编译时，Hvigor会生成cmake [Config-file Packages](https://cmake.org/cmake/help/latest/manual/cmake-packages.7.html#config-file-packages)，自动通过cmake [find\_package](https://cmake.org/cmake/help/latest/command/find_package.html#find-package)引入这些so。开发者只需根据此依赖模块的模块名、so库名，在CMakeLists.txt脚本中以${moduleName::soName}库名称的形式来声明链接。

例如工程依赖了curl共享包，共享包中存在libcurl.so，在oh-package.json5中添加依赖。

```
1. // oh-package.json5
2. "dependencies": {
3. "curl": "1.0.0"
4. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a6/v3/qSYOuVEcTU-9BtWtnR1l-A/zh-cn_image_0000002602066211.png?HW-CC-KV=V1&HW-CC-Date=20260611T073034Z&HW-CC-Expire=86400&HW-CC-Sign=F54E806CD171F36E05B68F45FA53A2627C202324591E94C985B98020567098D9)

在工程的CMakeLists.txt脚本中声明链接：

```
1. // CMakeLists.txt
2. add_library(entry SHARED napi_init.cpp)
3. # ${moduleName::soName}.
4. target_link_libraries(entry PUBLIC curl::curl)
```

说明

对于本地模块，HAR仅暴露本模块构建的so库，HSP暴露本模块构建及所依赖的so库。
