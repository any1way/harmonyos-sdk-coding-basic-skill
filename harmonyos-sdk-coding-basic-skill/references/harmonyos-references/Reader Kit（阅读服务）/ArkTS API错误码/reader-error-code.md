---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/reader-error-code
title: ArkTS API错误码
breadcrumb: API参考 > 应用服务 > Reader Kit（阅读服务） > ArkTS API错误码
category: harmonyos-references
scraped_at: 2026-06-01T16:39:20+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:47a8d906f10bd72fc7ce034758401ac2b7cefb87e4b44becfed586357437d281
---
说明

以下仅介绍本模块特有错误码，通用错误码请参考[通用错误码说明文档](../../通用错误码/errorcode-universal.md)。

## 1016900002

PhonePC/2in1Tablet

**错误信息**

Read Page Component is not initialized.

**错误描述**

ReadPageComponent没有初始化。

**处理步骤**

1. 请先初始化ReadPageComponent组件，再调用组件的能力。
2. 尝试重试操作或请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。

## 1016900003

PhonePC/2in1Tablet

**错误信息**

Invalid request.

**错误描述**

无效请求。

**处理步骤**

尝试重试操作或请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。

## 1016900999

PhonePC/2in1Tablet

**错误信息**

Other error.

**错误描述**

其他错误。

**处理步骤**

尝试重试操作或请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。

## 1016910001

PhonePC/2in1Tablet

**错误信息**

Invalid spine item.

**错误描述**

无效的内容。

**处理步骤**

尝试重试操作或请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。

## 1016910002

PhonePC/2in1Tablet

**错误信息**

Unexpected spine item resource data.

**错误描述**

异常的内容资源数据。

**处理步骤**

尝试重试操作或请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。

## 1016910003

PhonePC/2in1Tablet

**错误信息**

Spine item resource data out of range.

**错误描述**

没有找到spineIndex参数对应的SpineItem内容资源。

**处理步骤**

1. 请先检查资源数据是否是解析后的数据。
2. 尝试重试操作或请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。

## 1016910004

PhonePC/2in1Tablet

**错误信息**

Invalid caller.

**错误描述**

无效的调用者。

**处理步骤**

尝试重试操作或请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。

## 1017000001

PhonePC/2in1Tablet

**错误信息**

Book parser is not initialized

**错误描述**

书籍解析器未初始化。

**处理步骤**

检查[getDefaultHandler](<../ArkTS API/bookParser（书籍解析能力）/reader-book-parser.md#getdefaulthandler>)是否调用并且成功，且需要在[startPlay](<../ArkTS API/readerCore（阅读核心能力）/reader-read-core.md#startplay>)之前调用[registerBookParser](<../ArkTS API/readerCore（阅读核心能力）/reader-read-core.md#registerbookparser>)注册handler。

## 1017000999

PhonePC/2in1Tablet

**错误信息**

Other error.

**错误描述**

其他错误。

**处理步骤**

尝试重试操作或请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。

## 1017010001

PhonePC/2in1Tablet

**错误信息**

Invalid spine item.

**错误描述**

无效的内容。

**处理步骤**

1. 请先检查资源数据是否是解析后的数据。
2. 尝试重试操作或请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。

## 1017010002

PhonePC/2in1Tablet

**错误信息**

Invalid request.

**错误描述**

请求无效。

**处理步骤**

尝试重试操作或请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。

## 1017010003

PhonePC/2in1Tablet

**错误信息**

Book file format is unexpected.

**错误描述**

书籍格式异常。

**处理步骤**

1. 请检查书籍类型是否为'txt'、'epub'、'mobi'、'azw3'、'azw'。
2. 尝试重试操作或请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。

## 1017010004

PhonePC/2in1Tablet

**错误信息**

File is not existed.

**错误描述**

文件不存在。

**处理步骤**

1. 请先检查[应用沙箱目录](<../../../harmonyos-guides/应用框架/Core File Kit（文件基础服务）/应用文件/应用沙箱目录/app-sandbox-directory.md>)下（'/haps/entry/files/'）是否有导入的书籍。
2. 尝试重试操作或请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。
