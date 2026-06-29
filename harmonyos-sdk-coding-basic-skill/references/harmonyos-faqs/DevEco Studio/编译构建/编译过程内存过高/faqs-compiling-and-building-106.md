---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-106
title: 编译过程内存过高
breadcrumb: FAQ > DevEco Studio > 编译构建 > 编译过程内存过高
category: harmonyos-faqs
scraped_at: 2026-06-12T10:42:25+08:00
doc_updated_at: 2026-06-05
content_hash: sha256:f31e374025ec282264c419d69b892d4a429c602c8e05512a26e5961f1e5ce533
---

**问题现象**

编译构建时，内存或CPU占用过高，导致DevEco Studio运行卡顿和延迟。

**解决措施**

* 在执行hvigor构建的过程中，通过减少内存中的缓存数据、减少线程数量，可以减少编译过程中的内存占用。

  可以在hvigor-config.json5中添加配置。

  ```
  1. {
  2. "modelVersion": "0.0.1",
  3. "dependencies": {},
  4. "properties": {
  5. // Set to 0, indicating that the memory cache configuration is not enabled. The default value is 4, and the lower the value, the less cached data in memory
  6. "hvigor.pool.cache.capacity": 0,
  7. // The default configuration is -1 CPU cores, including ohos.arkCompile.maxSize4. The smaller the value, the less memory it occupies
  8. "hvigor.pool.maxSize" : 5,
  9. // The default configuration value is 5, and the smaller the value, the less memory it occupies
  10. "ohos.arkCompile.maxSize": 3,
  11. // The default configuration value is true, indicating that the memory cache is turned on and occupies more memory. The configuration is false, and the memory cache is turned off and occupies less memory
  12. "hvigor.enableMemoryCache": false
  13. }
  14. }
  ```

  [hvigor-config.json5](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/CompilingAndBuilding/hvigor-config.json5#L3-L16)

  说明

  当配置项"hvigor.pool.maxSize"和"ohos.arkCompile.maxSize"的值改小，"hvigor.enableMemoryCache"改为false后，可能会导致编译时长增加，请耐心等待。

* 如果上述修改未能达到预期效果，可以尝试使用非并行模式执行编译。
  + 在菜单栏中依次点击“File > Settings > Build, Execution, Deployment > Build Tools > Hvigor”，取消勾选“Execute tasks in parallel mode”。

    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e5/v3/UTAc0hH7SHGD7DIcLsYwrQ/zh-cn_image_0000002229758673.png?HW-CC-KV=V1&HW-CC-Date=20260612T024224Z&HW-CC-Expire=86400&HW-CC-Sign=7B53A96CA115BABB3CBB079F640CEFCCBB97C161494D05E410738E343B6EBCAD)
  + 在命令行最后添加--no-parallel，示例：

    ```
    1. hvigorw assembleHap --no-parallel
    ```

  说明

  使用非并行模式编译，内存占用将减少，但编译时间会延长，请耐心等待。
