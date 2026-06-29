---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-local-file-manager-24
title: 使用request.uploadFile上传文件后，没有回调可以获取到服务器返回的message信息，不能明确知道文件是否上传成功
breadcrumb: FAQ > 应用框架开发 > 本地数据和文件 > 本地文件管理 > 使用request.uploadFile上传文件后，没有回调可以获取到服务器返回的message信息，不能明确知道文件是否上传成功
category: harmonyos-faqs
scraped_at: 2026-06-12T10:35:04+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:d9bcc862609be28cc5e109d93a654d00c8c3337a83d8461b1fe5c8d042695792
---
使用request.uploadFile上传文件时，on('complete')回调在成功后触发。如果需要获取服务端的响应信息并处理判断逻辑，还可以使用on('headerReceive')回调。

**参考链接**

[on('complete' | 'fail')](<../../../../../harmonyos-references/基础功能/Basic Services Kit（基础服务）/ArkTS API/数据文件处理/@ohos.request (上传下载)/js-apis-request.md#oncomplete--fail9>)

[on('headerReceive')](<../../../../../harmonyos-references/基础功能/Basic Services Kit（基础服务）/ArkTS API/数据文件处理/@ohos.request (上传下载)/js-apis-request.md#onheaderreceive7>)
