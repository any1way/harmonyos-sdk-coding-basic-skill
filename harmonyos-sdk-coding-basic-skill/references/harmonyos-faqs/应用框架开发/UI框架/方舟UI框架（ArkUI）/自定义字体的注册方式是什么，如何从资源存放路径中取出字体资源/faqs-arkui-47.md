---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-47
title: 自定义字体的注册方式是什么，如何从资源存放路径中取出字体资源
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > 自定义字体的注册方式是什么，如何从资源存放路径中取出字体资源
category: harmonyos-faqs
scraped_at: 2026-06-12T10:26:44+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:9840ac143d55709a5630a9e350ad05aad7c9a6a0a50709b30d683542e0dcd820
---
在工程中存放自定义字体资源文件，通过代码中的registerFont接口注册这些字体，然后在文本组件中使用fontFamily属性引用。

推荐使用 $rawfile 方式引用自定义字体资源，资源应放置在 resources/rawfile 目录下。

获取字体资源可参考如下代码：

```
1. this.getUIContext().getFont().registerFont({
2. familyName: 'Gealova',
3. familySrc: $rawfile('font/gealova.otf')
4. })
```

[FontResources.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/FontResources.ets#L12-L15)

**参考链接**

[@ohos.font (注册自定义字体)](<../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS API/UI界面/@ohos.font (注册自定义字体)/js-apis-font.md>)
