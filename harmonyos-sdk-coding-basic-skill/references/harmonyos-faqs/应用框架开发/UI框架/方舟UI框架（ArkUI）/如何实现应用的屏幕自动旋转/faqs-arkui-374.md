---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-374
title: 如何实现应用的屏幕自动旋转
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > 如何实现应用的屏幕自动旋转
category: harmonyos-faqs
scraped_at: 2026-06-12T10:31:58+08:00
doc_updated_at: 2026-06-05
content_hash: sha256:320703765abb63cb1c48a2aca1fa7f614d5337d09e268b3285d0803fe3d20b80
---
1. 在module.json5添加属性"orientation": "auto\_rotation"。

   如下所示：

   ```
   1. "abilities": [
   2. {
   3. "name": "EntryAbility",
   4. "srcEntry": "./ets/entryability/EntryAbility.ets",
   5. "description": "$string:EntryAbility_desc",
   6. "icon": "$media:icon",
   7. "label": "$string:EntryAbility_label",
   8. "startWindowIcon": "$media:startIcon",
   9. "startWindowBackground": "$color:start_window_background",
   10. "exported": true,
   11. "skills": [
   12. // ...
   13. ],
   14. "orientation": "auto_rotation", // Rotate with the sensor
   15. }
   16. ],
   ```

   [auto\_rotation.json5](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/entryability/auto_rotation.json5#L20-L44)
2. 打开手机自动旋转功能，操作步骤：进入手机控制中心 > 关闭旋转锁定。

**参考链接**

[abilities标签](../../../../../harmonyos-guides/基础入门/开发基础知识/应用配置文件（Stage模型）/module.json5配置文件/module-configuration-file.md#abilities标签)
