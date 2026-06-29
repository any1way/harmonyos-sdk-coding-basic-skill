---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-23
title: 如何选择图文混排的实现方案
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > 如何选择图文混排的实现方案
category: harmonyos-faqs
scraped_at: 2026-06-12T10:26:23+08:00
doc_updated_at: 2026-03-17
content_hash: sha256:b92931f41726ef796ad5daf79f61b7433be00434e3c1a1fdd513764f3860cf24
---
1. 轻量级Span和ImageSpan图文混排：可通过[Text](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/文本与输入/Text/ts-basic-components-text.md)组件中嵌套[ImageSpan](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/文本与输入/ImageSpan/ts-basic-components-imagespan.md)子组件和[Span](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/文本与输入/Span/ts-basic-components-span.md)子组件的方式，实现图文混排。具体实现可参考ImageSpan中的[示例1（设置对齐方式）](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/文本与输入/ImageSpan/ts-basic-components-imagespan.md#示例1设置对齐方式)。
2. 富文本[RichEditor](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/文本与输入/RichEditor/ts-basic-components-richeditor.md)支持文本交互式编辑和图文混排，通过[addTextSpan()](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/文本与输入/RichEditor/ts-basic-components-richeditor.md#addtextspan)方法添加文本内容，通过[addImageSpan()](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/文本与输入/RichEditor/ts-basic-components-richeditor.md#addimagespan)方法添加图片内容。具体实现可参考RichEditor中的[示例1（更新文本样式）](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/文本与输入/RichEditor/ts-basic-components-richeditor.md#示例1更新文本样式)。
