---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/toolchain-gn-build-project
title: GN构建工程配置HarmonyOS编译工具链
breadcrumb: 指南 > NDK开发 > 编译工具链 > GN构建工程配置HarmonyOS编译工具链
category: harmonyos-guides
scraped_at: 2026-06-11T15:21:39+08:00
doc_updated_at: 2026-05-07
content_hash: sha256:1e2e5ba4ec90a4ad76f23fb475b26b31a75bee73620fffc64cf192fb7c8dc297
---

## 概述

本文将介绍如何在GN工程中配置HarmonyOS工具链，然后通过HarmonyOS工具链编译出可以在HarmonyOS环境下使用的三方库。

HarmonyOS编译子系统是以GN和Ninja构建为基座，对构建和配置粒度进行部件化抽象、对内建模块进行功能增强、对业务模块进行功能扩展的系统，该系统提供以下基本功能：

* 以部件为最小粒度拼装产品和独立编译。
* 支持轻量、小型、标准三种系统的解决方案级版本构建，以及用于支撑应用开发者使用DevEco Studio开发的SDK开发套件的构建。
* 支持芯片解决方案厂商的灵活定制和独立编译。

**Ninja：** 是一个专注于快速编译的小型构建系统。

**GN：** Generate Ninja的缩写，用于产生Ninja文件。

## 编译环境配置

1. Linux编译环境搭建（如果已有对应版本的Linux开发环境，可跳过Linux环境搭建过程）：详细指导见以下链接。

   [使用 WSL 在 Windows 上安装 Linux](https://learn.microsoft.com/zh-cn/windows/wsl/install)。

   [Ubuntu分发版本获取及安装说明](https://learn.microsoft.com/zh-cn/windows/wsl/install-manual)。

   编译环境目前主要支持Ubuntu18.04和Ubuntu20.04。
2. HarmonyOS SDK镜像下载：

   从HarmonyOS官网门户选择Linux版本的Command Line Tools下载即可。

   [下载链接](https://developer.huawei.com/consumer/cn/download/)。
3. 安装构建工具depot\_tools并添加到环境变量。

   任意位置创建工作目录depot\_tools，cd到自己创建的目录，拉取工具（需要网络环境）：

   ```
   1. mkdir depot_tools
   2. cd depot_tools
   3. git clone https://chromium.googlesource.com/chromium/tools/depot_tools.git
   ```

   将depot\_tools的路径加到环境变量中：

   编辑.bashrc文件将depot\_tools路径信息加到最后一行。

   ```
   1. vi ~/.bashrc
   ```

   在.bashrc文件的最后添加下面一行代码。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a5/v3/UpQon8ETSCun4QvABljx7A/zh-cn_image_0000002622699393.png?HW-CC-KV=V1&HW-CC-Date=20260611T072138Z&HW-CC-Expire=86400&HW-CC-Sign=CB835A232E17A04C17CA1A99871810B4AD875F7FFE2349862A3816FE907E3118)

   ```
   1. export PATH="$PATH:/xxx/depot_tools"
   ```

   此处需配置绝对路径信息，例如这里创建的本地路径是/mnt/d/my\_code/depot\_tools，故此处配置如上图。

   刷新环境变量使其生效：

   ```
   1. source ~/.bashrc
   ```
4. 使用GN需要Python环境，安装Python环境。

   ```
   1. sudo apt update
   2. sudo apt install python
   ```

   直接输入指令sudo apt install python可能会安装失败，需要先输入sudo apt update更新一下可用包的最新列表。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bb/v3/2B1mCmATQ2yKYf__2kvUMg/zh-cn_image_0000002592219832.png?HW-CC-KV=V1&HW-CC-Date=20260611T072138Z&HW-CC-Expire=86400&HW-CC-Sign=4F7BAEBA31F1335C726DF31A9DE256CD8A50677D76FEB2E4B4A7736DBC3D5079)

   判断python是否安装成功：

   输入python显示python版本即可。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d6/v3/gqcNoHDpSQSW59oV7tTbcg/zh-cn_image_0000002592379766.png?HW-CC-KV=V1&HW-CC-Date=20260611T072138Z&HW-CC-Expire=86400&HW-CC-Sign=8CDE2D22FDC326DBBD1B7996287391D9DA00E926901F13CE8C1697130B9D0358)

## GN构建工程适配流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cb/v3/OBMh_PSGSyGIfI9VYxl8rw/zh-cn_image_0000002622859275.png?HW-CC-KV=V1&HW-CC-Date=20260611T072138Z&HW-CC-Expire=86400&HW-CC-Sign=C09BE6CEF4763068B877A85376BFCF5873609B2CC1A37EEF17983F75E893F9FC)

1. 新增HarmonyOS平台的宏定义。
2. 配置HarmonyOS平台的工具链核心信息，涵盖clang工具链路径，sysroot系统根目录以及clang版本等关键参数。
3. 在toolchain目录下，为各架构分别配置对应的ohos\_clang\_toolchain。
4. 扩充gcc\_toolchain模版功能，补充HarmonyOS启动引导程序所需的.o文件相关配置。
5. 设置HarmonyOS编译参数，重点配置基础编译选项、宏定义等核心内容。
6. 在BUILD.gn文件的各架构平台分支逻辑中，新增HarmonyOS平台对应的分支配置；对于暂未适配HarmonyOS的三方库，可暂时沿用Linux分支的编译配置。

## webRTC适配案例

本文将通过webRTC的GN构建工程案例来对上一章节的流程进行实操讲解。WebRTC (Web Real-Time Communications) 是一项实时通讯技术，它允许网络应用或者站点，在不借助中间媒介的情况下，建立浏览器之间点对点（Peer-to-Peer）的连接，实现视频流和（或）音频流或者其他任意数据的传输。下面了解下如何通过GN构建工程将webRTC适配到HarmonyOS系统上。

三方库获取地址：[下载链接](https://gitee.com/openharmony/build)。

### 适配流程

1. **添加HarmonyOS平台宏定义**

   这里主要在build/config/BUILDCONFIG.gn文件中适配HarmonyOS的default\_compiler\_configs和\_default\_toolchain。在GN工程里面，BUILDCONFIG.gn是第一位被解析的，里面定义的变量相当于全局变量，可以被后续所有的.gn文件使用。编译过程中可能会配置一些编译选项以及一些头文件搜索路径。default\_compiler\_configs指向的文件里面会包括一些默认的编译选项以及头文件搜索路径等等。\_default\_toolchain指向了一个工具链相关的函数。具体修改点如下：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/74/v3/mvjAimE3QeC_8RUbnK1emg/zh-cn_image_0000002622699395.png?HW-CC-KV=V1&HW-CC-Date=20260611T072138Z&HW-CC-Expire=86400&HW-CC-Sign=722F89E8EFA7D437BAC6AEFB847F7266B57B9027065A4899796CE3638DA9A4F0)
2. **设置HarmonyOS平台clang工具链相关路径**

   不同平台的工具链会有一些差别，所以需要使用HarmonyOS的工具链。这里主要修改config/clang/clang.gni文件。.gni文件类似于GN的头文件，会被import到各个.gn文件中使用其定义的一些变量。该文件中的核心修改点在于配置指向HarmonyOS SDK的工具链路径。另外还需修改clang\_use\_chrome\_plugins的值为false，HarmonyOS中默认clang\_use\_chrome\_plugins值为false，不设置可能会报错find-bad-constructs文件找不到。

   此处ohos\_sdk\_native\_root的值需要对应修改为自己本地HarmonyOS SDK中的native的路径。具体修改点如下：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/27/v3/O-mJU_NnTOSimnnrZ7p2Jw/zh-cn_image_0000002592219834.png?HW-CC-KV=V1&HW-CC-Date=20260611T072138Z&HW-CC-Expire=86400&HW-CC-Sign=D3EBB7A25A4A8F0A2183C580BFD0E2ACEB94D3A60802E7A46E3F6E27DA2ED793)
3. **设置HarmonyOS平台sysroot路径**

   这里主要修改build/config/sysroot.gni文件，sysroot里面包含了许多头文件搜索路径，配置了sysroot之后，编译过程中会去该目录下搜索需要的头文件。SDK里面会提供大量的头文件，这些头文件都会放在sysroot目录下，所以需要引入HarmonyOS对应的sysroot。具体修改点如下：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/eb/v3/wuW6jRJKRCaA4HLoHiWA5g/zh-cn_image_0000002592379768.png?HW-CC-KV=V1&HW-CC-Date=20260611T072138Z&HW-CC-Expire=86400&HW-CC-Sign=C673584E90125CE2C0D6FE45706C83B0F7179228F455EAE3132217CB9F256367)
4. **修改HarmonyOS平台clang版本**

   这里主要修改build/toolchain/toolchain.gni文件，在该文件中配置HarmonyOS对应的clang版本号。具体修改点如下：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a0/v3/jGYW6EEZTTKTiOJwuYecTw/zh-cn_image_0000002622859277.png?HW-CC-KV=V1&HW-CC-Date=20260611T072138Z&HW-CC-Expire=86400&HW-CC-Sign=3F758AFC82EEA7064D7D2FC37AC5B4B37EC589F1376CBAB86D1D4A0571A1E21F)
5. **设置各个架构的ohos\_clang\_toolchain**

   这里主要是在build/toolchain路径下新建一个ohos/BUILD.gn文件，用于配置ohos\_clang\_toolchain，里面主要配置了HarmonyOS用于启动引导程序的.o文件。同时设置HarmonyOS不同架构(主要包括ohos\_clang\_arm、ohos\_clang\_arm64、ohos\_clang\_x86\_64)的ohos\_clang\_toolchain配置信息。具体添加内容如下：

   ```
   1. import("//build/config/sysroot.gni")
   2. import("//build/toolchain/gcc_toolchain.gni")

   4. declare_args() {
   5. # Whether unstripped binaries, i.e. compiled with debug symbols, should be
   6. # considered runtime_deps rather than stripped ones.
   7. ohos_unstripped_runtime_outputs = true
   8. ohos_extra_cflags = ""
   9. ohos_extra_cppflags = ""
   10. ohos_extra_cxxflags = ""
   11. ohos_extra_asmflags = ""
   12. ohos_extra_ldflags = ""
   13. }

   15. # The ohos clang toolchains share most of the same parameters, so we have this
   16. # wrapper around gcc_toolchain to avoid duplication of logic.
   17. #
   18. # Parameters:
   19. #  - toolchain_root
   20. #      Path to cpu-specific toolchain within the ndk.
   21. #  - sysroot
   22. #      Sysroot for this architecture.
   23. #  - lib_dir
   24. #      Subdirectory inside of sysroot where libs go.
   25. #  - binary_prefix
   26. #      Prefix of compiler executables.
   27. template("ohos_clang_toolchain") {
   28. gcc_toolchain(target_name) {
   29. assert(defined(invoker.toolchain_args),
   30. "toolchain_args must be defined for ohos_clang_toolchain()")
   31. toolchain_args = invoker.toolchain_args
   32. toolchain_args.current_os = "ohos"

   34. # Output linker map files for binary size analysis.
   35. enable_linker_map = true

   37. ohos_libc_dir =
   38. rebase_path(invoker.sysroot + "/" + invoker.lib_dir, root_build_dir)
   39. libs_section_prefix = "${ohos_libc_dir}/Scrt1.o"
   40. libs_section_prefix += " ${ohos_libc_dir}/crti.o"
   41. libs_section_postfix = "${ohos_libc_dir}/crtn.o"

   43. if (invoker.target_name == "ohos_clang_arm") {
   44. abi_target = "arm-linux-ohos"
   45. } else if (invoker.target_name == "ohos_clang_arm64") {
   46. abi_target = "aarch64-linux-ohos"
   47. } else if (invoker.target_name == "ohos_clang_x86_64") {
   48. abi_target = "x86_64-linux-ohos"
   49. }

   51. clang_rt_dir =
   52. rebase_path("${clang_lib_path}/${abi_target}/nanlegacy",
   53. root_build_dir)
   54. print("ohos_libc_dir :", ohos_libc_dir)
   55. print("clang_rt_dir :", clang_rt_dir)
   56. solink_libs_section_prefix = "${ohos_libc_dir}/crti.o"
   57. solink_libs_section_prefix += " ${clang_rt_dir}/clang_rt.crtbegin.o"
   58. solink_libs_section_postfix = "${ohos_libc_dir}/crtn.o"
   59. solink_libs_section_postfix += " ${clang_rt_dir}/clang_rt.crtend.o"

   61. _prefix = rebase_path("${clang_base_path}/bin", root_build_dir)
   62. cc = "${_prefix}/clang"
   63. cxx = "${_prefix}/clang++"
   64. ar = "${_prefix}/llvm-ar"
   65. ld = cxx
   66. readelf = "${_prefix}/llvm-readobj"
   67. nm = "${_prefix}/llvm-nm"
   68. if (!is_debug) {
   69. strip = rebase_path("${clang_base_path}/bin/llvm-strip", root_build_dir)
   70. use_unstripped_as_runtime_outputs = ohos_unstripped_runtime_outputs
   71. }
   72. extra_cflags = ohos_extra_cflags
   73. extra_cppflags = ohos_extra_cppflags
   74. extra_cxxflags = ohos_extra_cxxflags
   75. extra_asmflags = ohos_extra_asmflags
   76. extra_ldflags = ohos_extra_ldflags
   77. }
   78. }

   80. ohos_clang_toolchain("ohos_clang_arm") {
   81. sysroot = "${sysroot}"
   82. lib_dir = "usr/lib/arm-linux-ohos"
   83. toolchain_args = {
   84. current_cpu = "arm"
   85. }
   86. }

   88. ohos_clang_toolchain("ohos_clang_arm64") {
   89. sysroot = "${sysroot}"
   90. lib_dir = "usr/lib/aarch64-linux-ohos"
   91. toolchain_args = {
   92. current_cpu = "arm64"
   93. }
   94. }

   96. ohos_clang_toolchain("ohos_clang_x86_64") {
   97. sysroot = "${sysroot}"
   98. lib_dir = "usr/lib/x86_64-linux-ohos"
   99. toolchain_args = {
   100. current_cpu = "x86_64"
   101. }
   102. }
   ```
6. **扩充原本的gcc\_toolchain模版功能**

   主要修改/build/toolchain/gcc\_toolchain.gni文件。GN工程里面默认会配置gcc\_toolchain，里面会包括一些tool，例如tool("cc")、tool("cxx")、tool("tolink")等等，编译不同的内容时调用其对应的配置项。这里主要是需要修改tool("solink")、tool("solink\_module")中的rspfile\_content配置以及tool("link")中的link\_comand配置。需要在gcc\_toolchain.gni中template("gcc\_toolchain")下添加几个参数（libs\_section\_prefix、libs\_section\_postfix 、solink\_libs\_section\_prefix、solink\_libs\_section\_postfix ）的识别。这几个参数是指向了上一步骤中配置的用于启动引导程序的.o文件。这些参数会在需要修改的rspfile\_content、link\_comand参数中用到。具体修改如下：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/52/v3/i_LrjtMqRWCEDMnPUtrrJA/zh-cn_image_0000002622699397.png?HW-CC-KV=V1&HW-CC-Date=20260611T072138Z&HW-CC-Expire=86400&HW-CC-Sign=D46633CA9D0F2E8F9CC20F02D87D40FAE9F66360C43D7FD5DFED4D5780B2EEED)

   修改tool("solink")和tool("solink\_module")中的rspfile\_content为rspfile\_content = "-Wl,--whole-archive {{inputs}} {{solibs}} -Wl,--no-whole-archive $solink\_libs\_section\_prefix {{libs}} $solink\_libs\_section\_postfix"，这里需要用到刚刚定义的参数信息。具体修改如下：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/10/v3/ujlf4p8AT4iAOTv4Mnyx0Q/zh-cn_image_0000002592219836.png?HW-CC-KV=V1&HW-CC-Date=20260611T072138Z&HW-CC-Expire=86400&HW-CC-Sign=3A2DBD50A57BBECF69EBF3AB318EE59DA37EAA11C2E40BCB5894FEEC75C9E977)

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c3/v3/U3Xhxe-uQgKyloOn1Pv6Lg/zh-cn_image_0000002592379770.png?HW-CC-KV=V1&HW-CC-Date=20260611T072138Z&HW-CC-Expire=86400&HW-CC-Sign=8F3730B688800B08BE5F290B05050ABAA66D3981990459234F91152DE462D417)

   修改tool("link")中link\_command为link\_command = "$ld {{ldflags}}${extra\_ldflags} -o \"$unstripped\_outfile\" $libs\_section\_prefix $start\_group\_flag @\"$rspfile\" {{solibs}} {{libs}} $end\_group\_flag $libs\_section\_postfix"，这里需要用到刚刚定义的参数信息。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f4/v3/AcKc3PRxST61l06t1yMCFA/zh-cn_image_0000002622859279.png?HW-CC-KV=V1&HW-CC-Date=20260611T072138Z&HW-CC-Expire=86400&HW-CC-Sign=62C59AFE0F47FEF0F1B435FE257521376FA37CB65AC1F4A58690160BFC1E2672)
7. **设置HarmonyOS的一些编译参数，将其加入到BUILDCONFIG.gn中**

   这里需要在build/config路径下新建一个ohos/BUILD.gn文件，该文件主要是定义了一个config("compiler")，该config会被注册到所有的编译目标，该config里面主要设置了基础的编译选项、宏定义等。

   此处ohos\_clang\_base\_path 的值需要对应修改为自己本地HarmonyOS SDK中的llvm的路径。具体添加内容如下：

   ```
   1. import("//build/config/sysroot.gni")
   2. assert(is_ohos)

   4. ohos_clang_base_path = "/mnt/d/ohos/ohos-sdk/linux/native/llvm"
   5. ohos_clang_version = "15.0.4"

   7. if (is_ohos) {
   8. if (current_cpu == "arm") {
   9. abi_target = "arm-linux-ohos"
   10. } else if (current_cpu == "x86") {
   11. abi_target = ""
   12. } else if (current_cpu == "arm64") {
   13. abi_target = "aarch64-linux-ohos"
   14. } else if (current_cpu == "x86_64") {
   15. abi_target = "x86_64-linux-ohos"
   16. } else {
   17. assert(false, "Architecture not supported")
   18. }
   19. }

   21. config("compiler") {
   22. cflags = [
   23. "-ffunction-sections",
   24. "-fno-short-enums",
   25. "-fno-addrsig",
   26. ]

   28. cflags += [
   29. "-Wno-unknown-warning-option",
   30. "-Wno-int-conversion",
   31. "-Wno-unused-variable",
   32. "-Wno-misleading-indentation",
   33. "-Wno-missing-field-initializers",
   34. "-Wno-unused-parameter",
   35. "-Wno-c++11-narrowing",
   36. "-Wno-unneeded-internal-declaration",
   37. "-Wno-undefined-var-template",
   38. "-Wno-implicit-int-float-conversion",
   39. ]
   40. defines = [
   41. # The NDK has these things, but doesn't define the constants to say that it
   42. # does. Define them here instead.
   43. "HAVE_SYS_UIO_H",
   44. ]

   46. defines += [
   47. "OHOS",
   48. "__MUSL__",
   49. "_LIBCPP_HAS_MUSL_LIBC",
   50. "__BUILD_LINUX_WITH_CLANG",
   51. "__GNU_SOURCE",
   52. "_GNU_SOURCE",
   53. ]

   55. ldflags = [
   56. "-Wl,--no-undefined",
   57. "-Wl,--exclude-libs=libunwind_llvm.a",
   58. "-Wl,--exclude-libs=libc++_static.a",

   60. # Don't allow visible symbols from libraries that contain
   61. # assembly code with symbols that aren't hidden properly.
   62. # http://crbug.com/448386
   63. "-Wl,--exclude-libs=libvpx_assembly_arm.a",
   64. ]

   66. cflags += [ "--target=$abi_target" ]
   67. include_dirs = [
   68. "${sysroot}/usr/include/${abi_target}",
   69. "${ohos_clang_base_path}/lib/clang/${ohos_clang_version}/include",
   70. ]

   72. ldflags += [ "--target=$abi_target" ]

   74. # Assign any flags set for the C compiler to asmflags so that they are sent
   75. # to the assembler.
   76. asmflags = cflags
   77. }
   ```
8. **build/config/compiler/BUILD.gn中增加对is\_ohos的判断**

   保证可以正确走HarmonyOS支持的编译分支。这里主要是为了防止clang版本号校验失败导致异常。具体修改如下：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d6/v3/xnltHzDiSoaCmXYN7AiUTA/zh-cn_image_0000002622699399.png?HW-CC-KV=V1&HW-CC-Date=20260611T072138Z&HW-CC-Expire=86400&HW-CC-Sign=304BCD46F021F5862A583AF994F96E45227ED6584501F628EE2E02D1ED08C86E)
9. **未适配HarmonyOS的三方库走linux编译配置**

   当前部分三方库还未适配HarmonyOS，涉及到时可以先走linux的编译配置，例如：需要获取config.h文件时。

   修改modules/video\_capture的BUILD.gn。具体修改如下：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/72/v3/19EjcGMsRhmYiFN1uyi8qw/zh-cn_image_0000002592219838.png?HW-CC-KV=V1&HW-CC-Date=20260611T072138Z&HW-CC-Expire=86400&HW-CC-Sign=7861CD3400ABE6835FFA288DFE16C3F4382C814B7FA7ED0FE19DAB803717ADF2)

   修改third\_party/zlib的BUILD.gn。具体修改如下：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fa/v3/u2kYQDcMS-yc0vCnhwTWFQ/zh-cn_image_0000002592379772.png?HW-CC-KV=V1&HW-CC-Date=20260611T072138Z&HW-CC-Expire=86400&HW-CC-Sign=586A55C9C27CEEA14CE8E82F04885A560DF629DCA62D14E8DAEBCB79224C2CF2)

   修改third\_party/libevent中的BUILD.gn。HarmonyOS SDK中没有queue.h头文件，需要使用compat dir目录下的queue.h头文件。具体修改如下：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/86/v3/jhcpsoypQzy3El3uB9t8pQ/zh-cn_image_0000002622859281.png?HW-CC-KV=V1&HW-CC-Date=20260611T072138Z&HW-CC-Expire=86400&HW-CC-Sign=CBA165AFBD12FF43EC6F2A4D8DD2BA5C873EE20555248B8A71F96D5900500C0A)
10. **编译**

    先通过GN命令生成对应的ninja文件，然后使用ninja编译命令进行编译。

    ```
    1. gn gen ../out/xxx --args='is_clang=true target_os="ohos" target_cpu="arm64" xxx'
    2. ninja -v -C ../out/xxx ${target_name} -j16
    ```

    可以根据需要在编译指令中添加对应参数信息。

    查看具体编译命令：

    可以在gn gen命令中添加--ninja-args="-v -dkeeprsp"用于查看具体编译命令，这个命令将会在编译过程中打印详细的编译命令，并且保留编译过程中生成的rsp文件。

    查看一个目标被谁依赖：

    例如gn refs out/intermediate/arm64\_72 //pc:rtc\_pc\_base。这个命令将显示与目标//pc:rtc\_pc\_base相关的所有依赖项并列出所有引用了该目标的其他目标或文件。

### 常见问题总结

在对webRTC的GN工程进行HarmonyOS工具链适配过程中，遇到了一些常见问题场景。下面针对这些问题做一个具体分析。

1. **Assertion failed. Unsupported ARM OS**

   **问题详情：**

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/45/v3/4X064EgYRjyN9ZlhIHJ80Q/zh-cn_image_0000002622699401.png?HW-CC-KV=V1&HW-CC-Date=20260611T072138Z&HW-CC-Expire=86400&HW-CC-Sign=7ECEB416BA79D192F6C2AC7D29DC3840716909F3927D7A75E03FD0A28AFBF155)

   **问题原因/解决措施：**

   三方库内部没有做对is\_ohos的判断，导致走到错误分支。当前很多业务模块还未适配HarmonyOS，暂时可以走linux分支以保证正常编译。

   **具体修改：**

   修改third\_party/zlib的BUILD.gn文件。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2d/v3/BiFDjwshSHS9auLYtq6mKA/zh-cn_image_0000002592219840.png?HW-CC-KV=V1&HW-CC-Date=20260611T072138Z&HW-CC-Expire=86400&HW-CC-Sign=9AAC263B44831917674EC9FEF399FE414B5583A834E029E35A79621E7F0A2378)
2. **python找不到pkg-config文件：No such file or directory: 'pkg-config'**

   **问题详情：**

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/50/v3/HUkPYtUfRHaHaPLXklp97g/zh-cn_image_0000002592379774.png?HW-CC-KV=V1&HW-CC-Date=20260611T072138Z&HW-CC-Expire=86400&HW-CC-Sign=7AB4F18E21304AF73959F1DF8AD28CC31836BA1763AE586DC178A4F846A3B9A8)

   **问题原因/解决措施：**

   缺少pkg-config插件，安装该插件。

   **具体指令：**

   ```
   1. sudo apt-get install pkg-config
   ```
3. **Unknown command line argument '-split-threshold-for-reg-with-hint=0'**

   **问题详情：**

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ff/v3/3eSO7tUwRimfAAzPPj5CSw/zh-cn_image_0000002622859283.png?HW-CC-KV=V1&HW-CC-Date=20260611T072138Z&HW-CC-Expire=86400&HW-CC-Sign=20C7C43A2EFA189A7C8F09BDE480072810C2220D263A07743E95F35813A32F9B)

   **问题原因/解决措施：**

   编译过程中会提示部分配置不识别，需要将这些配置项删除。

   **具体修改：**

   在build/config/compiler/BUILD.gn中删除以下配置。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d5/v3/pYINWxBhTiCN82Y9k-6K8g/zh-cn_image_0000002622699403.png?HW-CC-KV=V1&HW-CC-Date=20260611T072138Z&HW-CC-Expire=86400&HW-CC-Sign=EC77187B5BC386FEBFA4CDB1203E08E724B0EFCFDA9EACE18EA48B8174ACA751)
4. **WARN类型导致的ERROR**

   **问题详情：**

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6a/v3/Tdvr8MyPRIGubt9gggQTmw/zh-cn_image_0000002592219842.png?HW-CC-KV=V1&HW-CC-Date=20260611T072138Z&HW-CC-Expire=86400&HW-CC-Sign=7800A9B6ABFD353F432F140B1715D339C61CD84220409DEB5AA6B3886A2891BD)

   **问题原因/解决措施：**

   编译器驱动程序有时（很少）会在调用之前发出警告。实际的链接器需要确保这些警告是否也被视为致命错误。为了避免编译中出现因警告而造成出错，可以添加编译参数treat\_warnings\_as\_errors = false，或者去除config(treat\_warnings\_as\_errors)中配置的“-Werror”，详情如下：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4c/v3/CEc8_aoLQmOjkgzOeE1AYw/zh-cn_image_0000002592379776.png?HW-CC-KV=V1&HW-CC-Date=20260611T072138Z&HW-CC-Expire=86400&HW-CC-Sign=48CD8173F4F9E8F0174D7D5C1820581710FDF0574AD8BED89B731EAE8DF779AB)

   **具体修改：**

   * 添加编译指令配置项treat\_warnings\_as\_errors （建议使用）

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/58/v3/BJjXe_MEQPKeOpJ12QzCpw/zh-cn_image_0000002622859285.png?HW-CC-KV=V1&HW-CC-Date=20260611T072138Z&HW-CC-Expire=86400&HW-CC-Sign=C242198A0FA9BE39839EEB5240526357B4FBB770BD9F0DEF24FAA6BD6E6595F0)
   * 修改源代码，在build/config/compiler/BUILD.gn中删除以下配置。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/88/v3/Otx0lpM3QgijjaHEjMLbTQ/zh-cn_image_0000002622699405.png?HW-CC-KV=V1&HW-CC-Date=20260611T072138Z&HW-CC-Expire=86400&HW-CC-Sign=7392993B5EE7058EEE5144B2A946D27E1F6F83241CF5F4A060E75FD28F8156BB)
5. **error: reinterpret\_cast from 'pthread\_t' (aka 'unsigned long') to 'rtc::PlatformThreadId' (aka 'int') is not allowed**

   **问题详情：**

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e3/v3/Lbhj7pQZS-uLsVEeUQsxMA/zh-cn_image_0000002592219844.png?HW-CC-KV=V1&HW-CC-Date=20260611T072138Z&HW-CC-Expire=86400&HW-CC-Sign=960DB1E23A04215BD8583F3791DCEB08611CDBE9FE79EC526999782C01B64036)

   **问题原因/解决措施：**

   rtc\_base/platform\_thread\_types.cc未识别到is\_ohos导致内部走错分支导致异常。目前HarmonyOS支持的接口是gettid()，rtc\_base/platform\_thread\_types.cc需要识别到is\_ohos然后调用gettid()。由于当前很多业务模块还未进行识别，暂时需要走linux分支，故需要保留linux的定义。

   **具体修改：**

   * 首先需要在根目录的BUILD.gn中配置识别HarmonyOS系统的变量is\_ohos：

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/de/v3/jTUbzJvHSr6__p_ZWuPO-A/zh-cn_image_0000002592379778.png?HW-CC-KV=V1&HW-CC-Date=20260611T072138Z&HW-CC-Expire=86400&HW-CC-Sign=4CCC3CB5B3A7A298EA5B5C48C64335F4684CD829C1E278FB79C1ED8DB1335B9E)
   * 修改rtc\_base/platform\_thread\_types.cc业务代码：

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c0/v3/6l2-rsXlQuql46djKNQtJw/zh-cn_image_0000002622859287.png?HW-CC-KV=V1&HW-CC-Date=20260611T072138Z&HW-CC-Expire=86400&HW-CC-Sign=8CEB238155A9D8568BB6C91DE1C8A25F4F58E2F0A32CEB6F8F55A14D9298B2B5)
6. **fatal error: 'config.h' file not found**

   **fatal error: 'sys/queue.h' file not found**

   **问题详情：**

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f/v3/au771JcjRnua4N3-rttjpw/zh-cn_image_0000002622699407.png?HW-CC-KV=V1&HW-CC-Date=20260611T072138Z&HW-CC-Expire=86400&HW-CC-Sign=2B3D2E1F5D263CFFB0C3CA2FAAC08F52A26DCBBB469F865384EE55F7E58DB503)![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/91/v3/oc87UcdsRVu13eBoRrCrtg/zh-cn_image_0000002592219846.png?HW-CC-KV=V1&HW-CC-Date=20260611T072138Z&HW-CC-Expire=86400&HW-CC-Sign=81B3FBCDAEFF1E3980D5F992A3531ABF2C6B25A114377A84D2F5C9AA7F7FBE12)

   **问题原因/解决措施：**

   找不到config.h头文件，libevent尚未适配HarmonyOS，需要添加is\_ohos的判断并走linux的文件路径寻找config.h。

   找不到'sys/queue.h'文件，HarmonyOS SDK中没有queue.h头文件，需要使用compat dir目录下的queue.h头文件。

   **具体修改：**

   修改third\_party/libevent中的BUILD.gn。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ca/v3/skmlY9EKSrSRpg7yB4-OEg/zh-cn_image_0000002592379780.png?HW-CC-KV=V1&HW-CC-Date=20260611T072138Z&HW-CC-Expire=86400&HW-CC-Sign=3BF913257CD453E56DA9BD84C80D4755C780F0D3DE9B4B847B9074E53C2251E8)
