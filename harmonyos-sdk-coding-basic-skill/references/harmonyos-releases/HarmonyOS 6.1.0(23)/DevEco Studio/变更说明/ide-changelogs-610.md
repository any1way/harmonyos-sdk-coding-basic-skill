---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/ide-changelogs-610
title: 变更说明
breadcrumb: 版本说明 > HarmonyOS 6.1.0(23) > DevEco Studio > 变更说明
category: harmonyos-releases
scraped_at: 2026-06-12T11:38:26+08:00
doc_updated_at: 2026-05-18
content_hash: sha256:83d1bd558905318407f1a949e345d25731016ccb600d61056464d2d1f363a3b8
---

## DevEco Studio 6.1.0 Release引入的变更

### 编辑器新版本暂不支持C API兼容性告警的Quick Fix功能

从DevEco Studio 6.1.0 Release（6.1.0.850）版本开始，DevEco Studio不支持Quick Fix自动快速修复C API兼容性告警。

**变更影响**

如用户编写如下代码：

工程级build.profile.json5配置为，"compatibleSdkVersion": "5.1.1(19)",

同时，用户使用API 20的接口。

```
1. #include <ohaudio/native_audio_stream_manager.h>

3. void test()
4. {
5. OH_AudioStreamManager_IsFastPlaybackSupported(nullptr, nullptr, AUDIOSTREAM_USAGE_UNKNOWN);
6. }
```

此时，老版本存在C API兼容性告警和使用APIAVAILABLE的Quick Fix能力。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/78/v3/uZ6q5jipS6W4i5UbmdvMBw/zh-cn_image_0000002603735633.png?HW-CC-KV=V1&HW-CC-Date=20260612T033825Z&HW-CC-Expire=86400&HW-CC-Sign=A9F48F107BB200599A81D011A9E920139658E88E307F5F9A764D251657D9A882)

新版本保留C API告警，去掉自动修改代码的Quick Fix功能，并新增指导文档跳转链接。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/58/v3/jibliOhQR-OZvM5U5WTHjw/zh-cn_image_0000002603737439.png?HW-CC-KV=V1&HW-CC-Date=20260612T033825Z&HW-CC-Expire=86400&HW-CC-Sign=B8E0141D701FE83238ACE5A4F94B7232745323FE09705F50FC1895EB5686460F)

**适配指导**

参考[CAPI兼容性保护高阶用法](https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/c-api-compatibility-warning)手动进行告警修复。

### 编辑器新版本修改为不支持自动传递COMPATIBLESDKVERSION参数给编译器

从DevEco Studio 6.1.0 Release（6.1.0.850）版本开始，DevEco Studio不自动传递 "arguments": "-DOHOS\_COMPATIBLE\_SDK\_VERSION=x.x.x" 参数给cmake，不默认开启弱引用功能 。

**变更影响**

注意

在DevEco Studio版本：6.1.0.830(API 23 Release) 上使用了C API兼容性保护，如果在高版本需要继续使用，必须参考[CAPI兼容性保护高阶用法](https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/c-api-compatibility-warning)的步骤重新配置。

**适配指导**

参考[CAPI兼容性保护高阶用法](https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/c-api-compatibility-warning)步骤重新配置。
