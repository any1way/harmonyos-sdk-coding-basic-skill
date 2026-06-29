---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/load-module-base-nodeapi
title: 基于Node-API加载模块
breadcrumb: 指南 > 应用框架 > ArkTS（方舟编程语言） > ArkTS运行时 > ArkTS模块化 > 基于Node-API加载模块
category: harmonyos-guides
scraped_at: 2026-06-01T11:01:39+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:3a5d582a2fcc8dbe7c2557f4ef3a803a892f6b1b29d76d1df5fd58bade673130
---
Node-API中有多种方式支持开发者在C++侧加载工程内模块及文件。推荐使用napi\_load\_module\_with\_info接口。

## napi\_load\_module\_with\_info

在主线程或子线程内加载hap/hsp/har/native模块，使用时必须标记所加载的包的信息，支持多种场景。

具体参考：[napi\_load\_module\_with\_info](../../../../../NDK开发/代码开发/使用Node-API实现ArkTSJS与CC++语言交互/Node-API典型使用场景/使用Node-API接口进行模块加载/use-napi-load-module-with-info.md)。

## napi\_load\_module

在主线程内加载hap/hsp/har/native模块，参数传递简便。加载场景有限制，例如无法在子线程中使用该接口。

具体参考：[napi\_load\_module](../../../../../NDK开发/代码开发/使用Node-API实现ArkTSJS与CC++语言交互/Node-API典型使用场景/使用Node-API接口在主线程中进行模块加载/use-napi-load-module.md)。
