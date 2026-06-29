---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faq-basics-service-kit-10
title: 如何获取系统版本号
breadcrumb: FAQ > 系统开发 > 基础功能 > 基础服务（Basics Service） > 如何获取系统版本号
category: harmonyos-faqs
scraped_at: 2026-06-12T10:38:19+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:97c083970ddb4ee088b94be9232ad358b836fcc56553f8a4e7ae8666ae98b815
---
可通过[@ohos.deviceInfo (设备信息)](<../../../../../harmonyos-references/基础功能/Basic Services Kit（基础服务）/ArkTS API/设备管理/@ohos.deviceInfo (设备信息)/js-apis-device-info.md>)模块，查询设备信息。

示例如下：

```
1. import { deviceInfo } from '@kit.BasicServicesKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. let displayVersionInfo: string = deviceInfo.displayVersion; // product version
5. let osFullNameInfo: string = deviceInfo.osFullName; // system version
6. let versionIdInfo: string = deviceInfo.versionId; // version ID

8. @Entry
9. @Component
10. struct GetSysVersion {
11. build() {
12. Row() {
13. Column() {
14. Button('get device info')
15. .onClick(() => {
16. hilog.info(0x000, 'displayVersion TAG', `displayVersion:${displayVersionInfo}`);
17. hilog.info(0x000, 'osFullName TAG', `osFullName:${osFullNameInfo}`);
18. hilog.info(0x000, 'versionId TAG', `versionId:${versionIdInfo}`);
19. })
20. }
21. .width('100%')
22. }
23. .height('100%')
24. }
25. }
```

[GetSysVersion.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/BasicsServiceKit/entry/src/main/ets/pages/GetSysVersion.ets#L21-L46)
