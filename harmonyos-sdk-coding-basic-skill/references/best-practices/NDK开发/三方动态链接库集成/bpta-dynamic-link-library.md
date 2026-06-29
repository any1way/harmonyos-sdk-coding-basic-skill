---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-dynamic-link-library
title: 三方动态链接库集成
breadcrumb: 最佳实践 > NDK开发 > 三方动态链接库集成
category: best-practices
scraped_at: 2026-06-12T10:07:05+08:00
doc_updated_at: 2026-03-12
content_hash: sha256:a0183f1e488348276e59af7e28d546c87503defa3abda8dcc5a1108816a79d3d
---
## 概述

在实际项目中，业务功能可能由不同“团队/组织”提供，如：团队A开发功能编译生成so库，团队B引用so库进行后续开发。so库可以将项目的不同功能模块化，提升代码的复用性和工程的可维护性。团队开发过程中引用三方so库的场景可分为两种：

1. 在Native侧引用三方so库。
2. 在ArkTS侧引用三方so库。

下面针对这两种场景给出具体的实现方案。

## 在Native侧引用三方so库

按照实际开发场景可分为两部分：编译生成so库和在Native侧引用so库。

第一部分：开发功能函数，编译生成so库。具体操作可参考：[使用命令行CMake构建NDK工程](../../../harmonyos-guides/NDK开发/构建NDK工程/使用命令行CMake构建NDK工程/build-with-ndk-cmake.md)。

第二部分：在Native侧引用so库调用功能函数。可以采用如下两种方案：

* 方案一：通过编译动态链接库的方式引用。
* 方案二：通过调用dlopen的方式引用。

### 通过编译动态链接库的方式引用

**实现原理**

将so库加入到工程中，在Native侧使用CMake编译动态链接库，通过include引用头文件调用功能函数。

**开发步骤**

以引用一个加法计算so库为例，具体实现步骤如下：

1. 将第一部分生成的so库文件置于entry/libs对应的架构目录下，将其对应的头文件置于src/main/cpp目录下。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/93/v3/o1K6uCjUS6KbsAARSFklqQ/zh-cn_image_0000002193852148.png?HW-CC-KV=V1&HW-CC-Date=20260612T020704Z&HW-CC-Expire=86400&HW-CC-Sign=37FF2BE2846154C42D3BA994C42E1A49A5C190E1C470EEEE6E9EE91F88D14CFA)

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d8/v3/9mGD4cjrQuuBfNyKsZdg6Q/zh-cn_image_0000002193852140.png?HW-CC-KV=V1&HW-CC-Date=20260612T020704Z&HW-CC-Expire=86400&HW-CC-Sign=F9F418ED622B91284928D050FE97636917D6600DC1806268C03AD0A7BDDC8FE1)
2. 修改src/main/cpp目录下CMakeLists.txt文件配置，使用target\_link\_libraries命令将需要预加载的加法so库链接到项目中。

   ```
   1. # Compile and link third-party SO libraries
   2. target_link_libraries(entry PUBLIC ${NATIVERENDER_ROOT_PATH}/../../../libs/${OHOS_ARCH}/libnativeAdd.so)
   ```

   [CMakeLists.txt](https://gitcode.com/HarmonyOS_Samples/NativeSoIntegration/blob/master/entry/src/main/cpp/CMakeLists.txt#L18-L19)
3. 在Native侧通过头文件引用加法so库。

   ```
   1. static napi_value NAPI_Global_nativeAdd(napi_env env, napi_callback_info info) {
   2. size_t argc = 2;
   3. napi_value args[2] = {nullptr};

   5. napi_get_cb_info(env, info, &argc, args, nullptr, nullptr);

   7. napi_valuetype valuetype0;
   8. napi_typeof(env, args[0], &valuetype0);

   10. napi_valuetype valuetype1;
   11. napi_typeof(env, args[1], &valuetype1);

   13. double value0;
   14. napi_get_value_double(env, args[0], &value0);

   16. double value1;
   17. napi_get_value_double(env, args[1], &value1);

   19. napi_value ret;
   20. napi_create_double(env, add(value0, value1), &ret);

   22. return ret;
   23. }

   25. // ...

   27. EXTERN_C_START
   28. static napi_value Init(napi_env env, napi_value exports) {
   29. napi_property_descriptor desc[] = {
   30. {"nativeAdd", nullptr, NAPI_Global_nativeAdd, nullptr, nullptr, nullptr, napi_default, nullptr},
   31. // ...
   32. napi_define_properties(env, exports, sizeof(desc) / sizeof(desc[0]), desc);
   33. return exports;
   34. }
   35. EXTERN_C_END
   ```

   [napi\_init.cpp](https://gitcode.com/HarmonyOS_Samples/NativeSoIntegration/blob/master/entry/src/main/cpp/napi_init.cpp#L29-L103)
4. 在index.d.ts文件中导出Native侧提供的接口，在ArkTS侧进行结果验证。

   ```
   1. // Export the addition calculation APIs provided on the Native side
   2. export const nativeAdd: (a: number, b: number) => number;
   ```

   [Index.d.ts](https://gitcode.com/HarmonyOS_Samples/NativeSoIntegration/blob/master/entry/src/main/cpp/types/libentry/Index.d.ts#L16-L17)

   在ArkTS侧调用Native侧提供的接口进行加法计算。

   ```
   1. // Integrate the SO library on the Native side directly to complete the addition operation
   2. let result = testNapi.nativeAdd(Number(this.paramX), Number(this.paramY));
   ```

   [Index.ets](https://gitcode.com/HarmonyOS_Samples/NativeSoIntegration/blob/master/entry/src/main/ets/pages/Index.ets#L80-L81)

**图1** 在Native侧通过编译动态链接库的方式引用so库完成加法运算效果展示  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4f/v3/PTHcGGLRQe6wFZhOpFEXpA/zh-cn_image_0000002194011732.png?HW-CC-KV=V1&HW-CC-Date=20260612T020704Z&HW-CC-Expire=86400&HW-CC-Sign=166C0BBF3153AE511FECAD67B8BFD06489AE441D37A2EEB478FB61315531E425 "点击放大")

### 通过调用dlopen的方式引用

**实现原理**

将so库加入到工程中，在ArkTS侧将so库的沙箱路径传递至Native侧，在Native侧使用dlopen解析so库调用功能函数。但是需要注意，该方案只能引用C语言编译模式生成的so库，因此用于生成so库的.h头文件需要用extern "C" {}包裹。

**开发步骤**

以引用一个减法计算so库为例，具体实现步骤如下：

1. 将第一部分生成的so库文件置于entry/libs对应的架构目录下。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0c/v3/DY0QKKbkThug2ivmm4vDMQ/zh-cn_image_0000002194011724.png?HW-CC-KV=V1&HW-CC-Date=20260612T020704Z&HW-CC-Expire=86400&HW-CC-Sign=3908077856E4B88AAE3E0B61EB8CBAD163B4F287563627922CD7255141F3240C)
2. 在ArkTS侧将so库的[沙箱路径](<../../../harmonyos-guides/应用框架/Core File Kit（文件基础服务）/应用文件/应用沙箱目录/app-sandbox-directory.md>)传递至Native侧。

   说明

   此处需要使用so库的沙箱路径，而不是其真实路径。

   为保障用户隐私安全，dlopen具有命名空间隔离能力，应用可以加载的动态库受到命名空间的限制。一般应用只能够加载应用安装包目录/data/storage/el1/bundle下的动态库，以及系统内置对外开放的动态库，若加载自定义路径动态库会报错：MUSL-LDSO bundlename E Open absolute\_path library: check ns accessible failed, pathname libxxx.so namespace moduleNs\_default。

   ```
   1. let projectPath = this.getUIContext().getHostContext()!.bundleCodeDir; // Get the project path
   2. let abiPath = deviceInfo.abiList === 'x86_64' ? 'x86_64' : 'arm64';
   3. let soLibPath = `${projectPath}/libs/${abiPath}/libnativeSub.so`;
   ```

   [Index.ets](https://gitcode.com/HarmonyOS_Samples/NativeSoIntegration/blob/master/entry/src/main/ets/pages/Index.ets#L96-L98)
3. 在Native侧引入dlfcn.h，通过调用dlopen解析so库实现减法计算。

   ```
   1. typedef double (*Sub)(double, double);
   2. static napi_value NAPI_Global_nativeSub(napi_env env, napi_callback_info info) {
   3. size_t argc = 3;
   4. napi_value args[3] = {nullptr};
   5. napi_get_cb_info(env, info, &argc, args, nullptr, nullptr);
   6. double value0;
   7. napi_get_value_double(env, args[0], &value0);
   8. double value1;
   9. napi_get_value_double(env, args[1], &value1);
   10. size_t length = 0;
   11. napi_status status = napi_get_value_string_utf8(env, args[2], nullptr, 0, &length);
   12. if (status != napi_ok) {
   13. return nullptr;
   14. }
   15. char *path = new char[length + 1];
   16. std::memset(path, 0, length + 1);
   17. napi_get_value_string_utf8(env, args[2], path, length + 1, &length); // Get the SO library path information
   18. void *handle = dlopen(path, RTLD_LAZY);                              // Open a SO library and get the path
   19. napi_value result = nullptr;
   20. Sub sub_func = (Sub)dlsym(handle, "sub"); // Get the function named sub
   21. status = napi_create_double(env, sub_func(value0, value1), &result);
   22. delete[] path;
   23. dlclose(handle); // Remember to close the SO library
   24. if (status != napi_ok) {
   25. return nullptr;
   26. }
   27. return result;
   28. }

   30. EXTERN_C_START
   31. static napi_value Init(napi_env env, napi_value exports) {
   32. napi_property_descriptor desc[] = {
   33. // ...
   34. {"nativeSub", nullptr, NAPI_Global_nativeSub, nullptr, nullptr, nullptr, napi_default, nullptr}};
   35. napi_define_properties(env, exports, sizeof(desc) / sizeof(desc[0]), desc);
   36. return exports;
   37. }
   38. EXTERN_C_END
   ```

   [napi\_init.cpp](https://gitcode.com/HarmonyOS_Samples/NativeSoIntegration/blob/master/entry/src/main/cpp/napi_init.cpp#L61-L104)
4. 在index.d.ts文件中导出Native侧提供的接口，在ArkTS侧进行结果验证。

   ```
   1. // Export the subtraction calculation interface provided by the Native side
   2. export const nativeSub: (a: number, b: number, path: string) => number;
   ```

   [Index.d.ts](https://gitcode.com/HarmonyOS_Samples/NativeSoIntegration/blob/master/entry/src/main/cpp/types/libentry/Index.d.ts#L21-L22)

   在ArkTS侧调用Native侧提供的接口进行减法计算。

   ```
   1. // Integrate the SO library on the Native side by dlopen to complete the subtraction operation
   2. let result = testNapi.nativeSub(Number(this.paramX), Number(this.paramY), soLibPath);
   ```

   [Index.ets](https://gitcode.com/HarmonyOS_Samples/NativeSoIntegration/blob/master/entry/src/main/ets/pages/Index.ets#L101-L102)

**图2** 在Native侧通过调用dlopen引用三方so库完成减法运算效果展示  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8b/v3/iW7los2hQHmdfpaBmWkv7w/zh-cn_image_0000002193852144.png?HW-CC-KV=V1&HW-CC-Date=20260612T020704Z&HW-CC-Expire=86400&HW-CC-Sign=BD2A99EFC10B3E494522D5BBA8E488F8FF61DFAAAA4B04E648E5E1EF1C3ADEDA "点击放大")

## 在ArkTS侧引用三方so库

按照实际开发场景可分为两部分：生成适配Native的so库和在ArkTS侧引用so库。

第一部分：开发功能函数，编译生成so库并适配Native。具体操作可参考：[使用命令行CMake构建NDK工程](../../../harmonyos-guides/NDK开发/构建NDK工程/使用命令行CMake构建NDK工程/build-with-ndk-cmake.md)。

第二部分：在ArkTS侧通过配置模块动态依赖的方式引用so库。

### 通过配置模块动态依赖引用

**实现原理**

将so库和对应的Native侧接口文件加入到工程中，在工程中配置so库对应的模块动态依赖，在ArkTS侧通过import引入依赖接口调用so库。但是需要注意该方案只能引用适配Native的so库，因此在编译生成so库时需要实现功能函数并[向Napi注册其Native侧接口](../../../harmonyos-guides/NDK开发/代码开发/使用Node-API实现ArkTSJS与CC++语言交互/使用Node-API实现跨语言交互开发流程/use-napi-process.md#native侧方法的实现)，提供对应的Native侧接口文件index.d.ts和配置文件oh-package.json5。

**开发步骤**

以引用一个乘法计算so库为例，具体实现步骤如下：

1. 将第一部分生成的so库文件置于entry/libs对应的架构目录下。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/13/v3/2kbD9JBKS4eJD7cTIQbSfA/zh-cn_image_0000002193852156.png?HW-CC-KV=V1&HW-CC-Date=20260612T020704Z&HW-CC-Expire=86400&HW-CC-Sign=0BACE8E390A1B7352D19245BBB294C461E6D4E40BEBE208374444FE2DD91244E)
2. 在src/main/cpp/types下新建目录并将so库模块src/main/cpp/types目录下的index.d.ts、oh-package.json5移动到该目录下。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d2/v3/yAo9xpsRQu2pOeaywj-eiw/zh-cn_image_0000002194011736.png?HW-CC-KV=V1&HW-CC-Date=20260612T020704Z&HW-CC-Expire=86400&HW-CC-Sign=83E3160051F051E75E93F1B47EB73BADDEE88527A0392D5DA7AE022FD69B6A30)
3. 在模块级oh-package.json5中声明乘法so库根目录路径。

   ```
   1. {
   2. // ...
   3. "dependencies": {
   4. // ...
   5. // The declared dependency name should match the name of the referenced SO library
   6. "libmultiply.so": "file:./src/main/cpp/types/libmultiply"
   7. }
   8. }
   ```

   [oh-package.json5](https://gitcode.com/HarmonyOS_Samples/NativeSoIntegration/blob/master/entry/oh-package.json5#L2-L18)
4. 在ArkTS侧使用import引用oh-package.json5中声明的依赖并进行结果验证。

   ```
   1. // Integrate the SO library that has been adapted to Native On the ArkTS side to complete the multiplication operation
   2. let result = multiplyNapi.multiply(Number(this.paramX), Number(this.paramY));
   ```

   [Index.ets](https://gitcode.com/HarmonyOS_Samples/NativeSoIntegration/blob/master/entry/src/main/ets/pages/Index.ets#L117-L118)

**图3** 在ArkTS侧引用已经适配Native的三方so库完成乘法运算效果展示  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7a/v3/cIlzYGfcRvuiu1M-Ews-6Q/zh-cn_image_0000002194011728.png?HW-CC-KV=V1&HW-CC-Date=20260612T020704Z&HW-CC-Expire=86400&HW-CC-Sign=0F53806C94A151501721D290474E9F76400769BD779EAC22F979AA94B9910382 "点击放大")

## 常见问题

### 如何在同一个工程中实现三方so库的编译和引用

可以在工程中创建两个Module，通过其中一个Module编译生成加法、减法和乘法运算so库，通过另外一个Module引用三方so库，进行结果验证。

**参考链接**

* [使用命令行CMake构建NDK工程](../../../harmonyos-guides/NDK开发/构建NDK工程/使用命令行CMake构建NDK工程/build-with-ndk-cmake.md)
* [在NDK工程中使用预构建库](../../../harmonyos-guides/NDK开发/构建NDK工程/在NDK工程中使用预构建库/build-with-ndk-prebuilts.md)

### 在集成三方so库时，.so库文件和.h头文件一定要置于上述方法的路径下吗

不一定。原则上.so库文件和.h头文件可以置于需要引用so库的工程目录的任意位置，但是需要在工程的CMakeLists.txt文件中修改文件配置。如：将add.h头文件和libnativeAdd.so库文件放置在entry的根目录下，需要在CMakeLists.txt文件中通过include\_directories命令添加entry的根目录作为头文件路径，并修改target\_link\_libraries命令中需要预加载的加法so库的路径，才能保证so库链接成功。

**代码示例**

```
1. # src/main/cpp/CMakeLists.txt
2. include_directories(${NATIVERENDER_ROOT_PATH}/../../..)
3. target_link_libraries(entry PUBLIC ${NATIVERENDER_ROOT_PATH}/../../../libnativeAdd.so)
```

### 在纯ArkTS工程中如何引用三方so库

纯ArkTS工程可以通过配置模块动态依赖的方式引用so库。但是需要注意，在引用过程中除了将已经适配Native的xxx.so库文件置于entry/libs对应的架构目录下外，还需要将编译三方so库时配套产生的libc++\_xxx.so库文件置于该目录下。

**示例如下**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/43/v3/v750qY3pTjKxR8QPDCA3HQ/zh-cn_image_0000002193852152.png?HW-CC-KV=V1&HW-CC-Date=20260612T020704Z&HW-CC-Expire=86400&HW-CC-Sign=8824039AAFDF09CE7451159903CA8EAE3A501A8A639CD7548765FBFDFFD04A15)![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c8/v3/pLg0gTt4RMCiB--q1khqtw/zh-cn_image_0000002194011740.png?HW-CC-KV=V1&HW-CC-Date=20260612T020704Z&HW-CC-Expire=86400&HW-CC-Sign=645E5C91C596C8218074BDAF1FDC61B2B450864F742FF5D0292F672F016B251D)

## 示例代码

* [实现动态链接库（.so）的引用](https://gitcode.com/harmonyos_samples/NativeSoIntegration)
