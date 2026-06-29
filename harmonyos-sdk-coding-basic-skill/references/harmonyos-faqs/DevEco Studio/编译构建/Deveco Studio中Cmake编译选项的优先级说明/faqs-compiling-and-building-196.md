---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-196
title: Deveco Studio中Cmake编译选项的优先级说明
breadcrumb: FAQ > DevEco Studio > 编译构建 > Deveco Studio中Cmake编译选项的优先级说明
category: harmonyos-faqs
scraped_at: 2026-06-01T17:08:21+08:00
doc_updated_at: 2026-05-30
content_hash: sha256:462571203a8b33d32707cb45a0dada2ca715beccdfff7cf1089c644534d47aa8
---

1. 常见的Cmake编译选项如下：
   * Cmakelists.txt中通过CACHE FORCE设置的参数。
   * Cmakelists.txt中缓存的变量。
   * CmakeLists.txt中环境变量配置的缓存。

     ```
     1. #1、采用CACHE FORCE
     2. set(CMAKE_BUILD_TYPE debug CACHE STRING "Build type" FORCE)
     3. message(${CMAKE_BUILD_TYPE} "CMAKE_BUILD_TYPE_FORCE")

     5. #2、缓存变量
     6. set(CMAKE_BUILD_TYPE debug CACHE STRING "Build type")
     7. message(${CMAKE_BUILD_TYPE} "CMAKE_BUILD_TYPE")

     9. #3、缓存环境变量
     10. set(CMAKE_BUILD_TYPE $ENV{CMAKE_BUILD_TYPE} CACHE STRING "Build type")
     11. message($ENV{CMAKE_BUILD_TYPE} "ENV_CMAKE_BUILD_TYPE")
     ```
   * CmakePresets.json或CMakeUsersPersets.json中配置的参数。

     ```
     1. {
     2. "version":3,
     3. "configurePresets":[
     4. {
     5. "name":"debug",
     6. "displayName":"Build type",
     7. "description":"Build type debug preset",
     8. "cacheVariables":{
     9. "CMAKE_BUILD_TYPE":"Debug"
     10. }
     11. }
     12. ]
     13. }
     ```
2. DevEco Studio自定义Cmake编译选项如下：
   * 模块级build-profile.json5中"externalNativeOptions"->"arguments"显式配置的参数。

     ```
     1. "externalNativeOptions": {
     2. "path": "./src/main/cpp/CMakeLists.txt",
     3. "arguments": "-DCMAKE_BUILD_TYPE=debug",
     4. "cppFlags": "",
     5. "cFlags": "",
     6. "abiFilters": [
     7. "arm64-v8a",
     8. "x86_64"
     9. ]
     10. }
     ```
   * hvigor默认配置的-DCMAKE\_BUILD\_TYPE参数。

     ```
     1. //"debuggable"缺省或为true，或者buildMode为debug
     2. -DCMAKE_BUILD_TYPE=debug
     3. //"debuggable"为false，或者buildMode为release
     4. -DCMAKE_BUILD_TYPE=release
     ```

用户可根据实际需求动态配置CMake变量，使参数生效，DevEco Studio中Cmake缓存变量的优先级顺序如下所示（从高到低）：

1. Cmakelists.txt中通过CACHE FORCE设置的参数。
2. 模块级build-profile.json5中"externalNativeOptions"->"arguments"显式配置的参数。
3. hvigor默认配置的-DCMAKE\_BUILD\_TYPE参数。
4. CmakePresets.json或CMakeUsersPersets.json中配置的参数。
5. Cmakelists.txt中缓存的变量及环境变量配置的缓存。
