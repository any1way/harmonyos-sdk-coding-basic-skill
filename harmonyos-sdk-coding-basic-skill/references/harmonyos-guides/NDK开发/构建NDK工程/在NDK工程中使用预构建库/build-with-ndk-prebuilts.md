---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/build-with-ndk-prebuilts
title: 在NDK工程中使用预构建库
breadcrumb: 指南 > NDK开发 > 构建NDK工程 > 在NDK工程中使用预构建库
category: harmonyos-guides
scraped_at: 2026-06-11T15:19:47+08:00
doc_updated_at: 2026-06-09
content_hash: sha256:966526ec7fb535547b4c178969a8982fee2e334cc0485564d54b10b41a64c810
---
在NDK工程中，可以通过CMake语法规则引入并使用预构建库。在引用预构建库时，模块libs目录中的预构建库，以及在CMakeLists.txt编译脚本中声明的预构建库都会被打包。

## 预构建库使用约束

1.确保引入的SO动态库是通过[HarmonyOS NDK 编译工具链](../NDK工程构建概述/build-with-ndk-overview.md)编译生成，如何通过[HarmonyOS NDK 编译工具链](../NDK工程构建概述/build-with-ndk-overview.md)编译预构建库，请参考[CMake构建三方库适配流程](../../编译工具链/CMake构建工程配置HarmonyOS编译工具链/toolchain-cmake-build-project.md#cmake构建三方库适配流程)。

2.确保引入的SO动态库的依赖库也导入到工程中且通过[HarmonyOS NDK 编译工具链](../NDK工程构建概述/build-with-ndk-overview.md)编译生成。

## 直接引入预构建库

可以通过直接将预构建的库文件复制到项目文件中, 来使用预构建库。例如在项目中需要使用预构建库libavcodec\_ffmpeg.so，其开发态存放路径如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/85/v3/nDK0cd65Q2mnO9BaxhKLiw/zh-cn_image_0000002592219804.png?HW-CC-KV=V1&HW-CC-Date=20260611T071946Z&HW-CC-Expire=86400&HW-CC-Sign=75A2819308CA6A075F4EB28AAC90C47CF0279AA629778D94BBD91B296AEA0563)

在模块的CMakeLists.txt编译脚本中通过add\_library添加所需的预构建库，并声明预构建库路径等信息后，可以在target\_link\_libraries中声明链接该预构建库，脚本示例如下所示：

```
1. add_library(library SHARED hello.cpp)

3. add_library(avcodec_ffmpeg SHARED IMPORTED)
4. set_target_properties(avcodec_ffmpeg
5. PROPERTIES
6. IMPORTED_LOCATION ${CMAKE_CURRENT_SOURCE_DIR}/third_party/FFmpeg/libs/${OHOS_ARCH}/libavcodec_ffmpeg.so)

8. target_link_libraries(library PUBLIC libace_napi.z.so avcodec_ffmpeg)
```

在模块的CMakeLists.txt编译脚本中添加include\_directories：

```
1. include_directories(
2. # ...
3. ${CMAKE_CURRENT_SOURCE_DIR}/third_party/FFmpeg/include
4. )
```

当在HAR中使用预构建库时，当前编译的库和链接所需预构建库会打包到HAR中的libs目录下，如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/42/v3/ewiXAvK6SbGWRukXKxgPuQ/zh-cn_image_0000002592379738.png?HW-CC-KV=V1&HW-CC-Date=20260611T071946Z&HW-CC-Expire=86400&HW-CC-Sign=8BDA9CF3A45F5CB80BA28D51360248A43B62EBEBBCE051A5FE3487F6F12A1F61)

### 预构建库的SONAME问题

请确保引入的预构建动态库（so）正确设置了SONAME。

如果预构建so没有SONAME，链接器将会将so的绝对路径插入到依赖这个so的二进制文件的dynamic section中。当这些二进制文件随hap包发布运行时，动态加载器（dynamic loader）可能最终无法找到这个so而导致错误。

可以使用llvm-readelf工具查看so文件是否设置了SONAME。llvm-readelf工具路径为：${DevEco Studio安装目录}/sdk/default/openharmony/native/llvm/bin或者${command-line-tools安装目录}/sdk/default/openharmony/native/llvm/bin/llvm-readelf。

示例如下：

```
1. > ${YOUR_PATH}/command-line-tools/sdk/default/openharmony/native/llvm/bin/llvm-readelf -d libavcodec_ffmpeg.so | grep SONAME
2. 0x000000000000000e (SONAME)             Library soname: [libavcodec_ffmpeg.so]
```

若预构建so使用cmake进行构建，则所有的so默认会设置SONAME（只要目标平台支持）。

若预构建so使用其他构建工具，可以通过配置ldflags来设置。

```
1. ${...}/clang++ ${...} -Wl,-soname,libavcodec_ffmpeg.so
```

## 使用远程依赖HAR中集成的预构建库

当使用远程依赖HAR中集成的预构建库时，CMakeLists.txt文件中引用脚本如下所示：

```
1. set(DEPENDENCY_PATH ${CMAKE_CURRENT_SOURCE_DIR}/../../../oh_modules)
2. add_library(library SHARED IMPORTED)
3. set_target_properties(library
4. PROPERTIES
5. IMPORTED_LOCATION ${DEPENDENCY_PATH}/library/libs/${OHOS_ARCH}/liblibrary.so)
6. add_library(entry SHARED hello.cpp)
7. target_link_libraries(entry PUBLIC libace_napi.z.so library)
```

## 使用本地HAR中集成的预构建库

当使用本地HAR中集成的预构建库时，CMakeLists.txt文件中引用脚本如下所示：

```
1. set(LIBRARY_DIR "${NATIVERENDER_ROOT_PATH}/../../../../library/build/default/intermediates/libs/default/${OHOS_ARCH}/")
2. add_library(library SHARED IMPORTED)
3. set_target_properties(library
4. PROPERTIES
5. IMPORTED_LOCATION ${LIBRARY_DIR}/liblibrary.so)
6. add_library(entry SHARED hello.cpp)
7. target_link_libraries(entry PUBLIC libace_napi.z.so library)
```
