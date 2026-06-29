---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-scroll
title: 滚动类组件错误码
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > 错误码 > UI界面 > 滚动类组件错误码
category: harmonyos-references
scraped_at: 2026-06-01T15:53:56+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:4e29938c3f7f29f68ac2cf00b6f571bff8fa7c8580e1bc1cae8b7566ab61a9ce
---
说明

以下仅介绍本模块特有错误码，通用错误码请参考[通用错误码说明文档](../../../../通用错误码/errorcode-universal.md)。

## 100004 控制器未绑定组件

PhonePC/2in1TabletTVWearable

**错误信息**

Controller not bound to component.

**错误描述**

控制器未绑定组件，通过控制器调用接口时，系统会产生此错误码。该错误码为string类型。

**可能原因**

控制器未绑定组件，通过控制器调用接口。

**处理步骤**

请检查控制器是否绑定了组件，或者控制器绑定的组件是否已经被释放。
