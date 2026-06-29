---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-project-management-7
title: 如何将HAR（静态共享包）转为HSP（动态共享包）
breadcrumb: FAQ > DevEco Studio > 工程管理 > 如何将HAR（静态共享包）转为HSP（动态共享包）
category: harmonyos-faqs
scraped_at: 2026-06-01T17:05:04+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:77d3d9a3c89b6d038c7676b6ab1c6656f6f260f304bb61834aae01657f0bfaee
---
[HAR](../../../../harmonyos-guides/基础入门/开发基础知识/应用程序包基础知识/应用程序包开发与使用/HAR/har-package.md)转换成[HSP](../../../../harmonyos-guides/基础入门/开发基础知识/应用程序包基础知识/应用程序包开发与使用/HSP/in-app-hsp.md)可参考如下步骤：

1. 新建一个HSP，将HAR包拷贝到lib目录，并在HSP的oh-package.json5文件的dependencies下配置HAR包。

   ```
   1. "dependencies": {
   2. "myhar": "file:./lib/myHar.har" // MyHar.Har path: oh-package.json5 file in the same directory as the lib folder
   3. },
   ```

   [oh-package.json5](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/ProjectManager/library/oh-package.json5#L14-L16)
2. 在HSP的Index.ets中直接导出HAR内容。

   ```
   1. export * as myhar from 'myhar';
   ```

   [Index.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/ProjectManager/library/Index.ets#L6-L6)
3. 最后编译该HSP。
