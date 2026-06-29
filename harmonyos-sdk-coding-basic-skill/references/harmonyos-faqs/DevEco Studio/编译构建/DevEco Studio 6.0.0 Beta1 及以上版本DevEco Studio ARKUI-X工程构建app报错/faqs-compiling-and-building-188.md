---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-188
title: DevEco Studio 6.0.0 Beta1 及以上版本DevEco Studio ARKUI-X工程构建app报错
breadcrumb: FAQ > DevEco Studio > 编译构建 > DevEco Studio 6.0.0 Beta1 及以上版本DevEco Studio ARKUI-X工程构建app报错
category: harmonyos-faqs
scraped_at: 2026-06-12T10:43:39+08:00
doc_updated_at: 2026-03-25
content_hash: sha256:841287f194eca1898746a7561e296b8f1a297e41f693c2b6a185a887a98c980b
---

**问题现象**

构建app报错：“Could not open settings generic class cache for settings file”

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bf/v3/2AEaeSdVSCKrVDGzpwhU_g/zh-cn_image_0000002381980508.png?HW-CC-KV=V1&HW-CC-Date=20260612T024338Z&HW-CC-Expire=86400&HW-CC-Sign=C662EECFBD28405032B96A448ED75BC04D6B9F5D66276FBAFC9C8AA24C72FB3C)

**常见错误场景**

当前工程使用的是低于DevEco Studio 6.0.0 Beta1 版本的DevEco Studio创建的。

**问题原因**

DevEco Studio 6.0.0 Beta1版本DevEco Studio内置的Java版本为21，当前Gradle的版本低于Java21配套的版本。

**解决措施**：

* **方式一：升级gradle版本**

  修改Gradle-wrapper.properties中的distributionUrl，升级为8.4版本。

  ```
  1. distributionUrl=https\://repo.huaweicloud.com/gradle/gradle-8.4-bin.zip
  ```

* **方式二：指定使用Java17**

  如果本地有JDK17，可以在Gradle.properties中通过org.gradle.java.home变量指定使用Java17。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4e/v3/X7c7E7gRRqKKogO8l_AuJA/zh-cn_image_0000002415859685.png?HW-CC-KV=V1&HW-CC-Date=20260612T024338Z&HW-CC-Expire=86400&HW-CC-Sign=40F988376EA067B4CE253F7839148CD8DED5A189AD804F030A7FDBA0CAEC3E94)
