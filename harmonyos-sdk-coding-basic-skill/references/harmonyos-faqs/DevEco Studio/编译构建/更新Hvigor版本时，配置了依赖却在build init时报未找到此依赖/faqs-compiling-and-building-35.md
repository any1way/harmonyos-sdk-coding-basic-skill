---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-35
title: 更新Hvigor版本时，配置了依赖却在build init时报未找到此依赖
breadcrumb: FAQ > DevEco Studio > 编译构建 > 更新Hvigor版本时，配置了依赖却在build init时报未找到此依赖
category: harmonyos-faqs
scraped_at: 2026-06-12T10:41:26+08:00
doc_updated_at: 2026-06-05
content_hash: sha256:ac055a8e773b65b17447804ddc3f708b2e8a94c2c1962f20aa8607e1f08aa8cd
---

**问题现象**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b6/v3/ciuYAAyHSNuoufMetYDH1g/zh-cn_image_0000002194158852.png?HW-CC-KV=V1&HW-CC-Date=20260612T024125Z&HW-CC-Expire=86400&HW-CC-Sign=77663125DA91D4409736110787EF93B613428B84814EB638A88B5873842FE926)

**解决措施**

出现该问题的原因是工程中使用了3.3.0及后续版本的Hvigor，但Hvigor-wrapper.js版本较旧，两者不兼容。不兼容的场景包括：

* 场景一：使用4.0 Canary2之前的DevEco Studio时，同步只会下载Hvigor，不会下载dependencies下的内容（即hvigor-ohos-plugin）。如果需要更新Hvigor版本且不更新DevEco Studio，只能下载Hvigor，无法下载hvigor-ohos-plugin。建议更新至DevEco Studio NEXT Developer Preview1及以上版本
* 场景二：对于4.0 Beta1之前的DevEco Studio创建的工程，需要更新Hvigor版本。使用DevEco Studio NEXT Developer Preview1及以上版本的DevEco Studio打开历史工程，修改hvigor-config.json5中的Hvigor和plugin版本号，然后Sync。同步时会提示更新，点击按钮后将自动完成Hvigor和plugin的下载。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/db/v3/ejLtO46lT0COk9517G5zEQ/zh-cn_image_0000002229758729.png?HW-CC-KV=V1&HW-CC-Date=20260612T024125Z&HW-CC-Expire=86400&HW-CC-Sign=5C680D321D59E2034B488A3E32E463B0631B90EECD6E471236482ED3E64CAFED)
