---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-service-widget-common-customizing-font
title: 自定义字体样式
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > JS组件 > JS服务卡片UI组件 > 组件通用信息 > 自定义字体样式
category: harmonyos-references
scraped_at: 2026-06-01T15:48:08+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:1a82ec93acd66c2a4ac578ff79577e60f3488d375390ec72ccedad02f3850454
---
font-face用于定义字体样式。应用可以在style中定义font-face来指定相应的字体名和字体资源，然后在font-family样式中引用该字体。

自定义字体可以是从项目中的字体文件或网络字体文件中加载的字体。

说明

从API version 8 开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

字体格式支持ttf和otf。

## 定义font-face

PhonePC/2in1TabletTVWearable

```
1. @font-face {
2. font-family: HWfont;
3. src: url('/common/HWfont.ttf');
4. }
```

**font-family：** 自定义字体的名称。

**src：** 自定义字体的来源，支持如下类别。

* 项目中的字体文件：通过url指定项目中的字体文件路径(只支持绝对路径，详见[文件组织](../../框架说明/文件组织/js-service-widget-file.md))。
* 网络字体文件：通过url指定网络字体的地址。
* 不支持设置多个src。

## 使用font-face

PhonePC/2in1TabletTVWearable

可以在style中定义font-face，然后在font-family样式中指定该font-face的名称，从而应用font-face定义的字体。示例如下：

* 页面布局

  ```
  1. <div>
  2. <text class="demo-text">测试自定义字体</text>
  3. </div>
  ```
* 页面样式

  ```
  1. @font-face {
  2. font-family: HWfont;
  3. src: url("/common/HWfont.ttf");
  4. }
  5. .demo-text {
  6. font-family: HWfont;
  7. }
  ```
