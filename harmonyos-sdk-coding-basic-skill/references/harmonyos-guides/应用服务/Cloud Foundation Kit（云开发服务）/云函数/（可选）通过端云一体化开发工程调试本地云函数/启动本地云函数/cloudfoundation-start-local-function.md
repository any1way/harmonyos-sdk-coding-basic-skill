---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cloudfoundation-start-local-function
title: 启动本地云函数
breadcrumb: 指南 > 应用服务 > Cloud Foundation Kit（云开发服务） > 云函数 > （可选）通过端云一体化开发工程调试本地云函数 > 启动本地云函数
category: harmonyos-guides
scraped_at: 2026-06-11T15:05:39+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:4b2724a8321e4322ffbe7f8e0cb356c9dfe5ed9aaea724899ece7cc08a8ed8f2
---
请按照如下步骤启动本地云函数：

1. [创建端云一体化开发工程](../../../../../开发环境搭建/工程创建/模块管理/端云一体化开发/开发端云工程/创建端云一体化开发工程/创建HarmonyOS应用工程/agc-harmonyos-create-appproject.md)：选择合适的云开发模板，根据工程向导创建端云一体化开发工程。
2. [开发云函数](../../../../../开发环境搭建/工程创建/模块管理/端云一体化开发/开发端云工程/开发云侧工程/开发云函数/开发流程/agc-harmonyos-clouddev-functionprocess.md)：使用DevEco Studio在端云一体化云侧工程下创建函数、开发函数、调试函数（通过本地调用方式调试函数）。

   调试函数过程中，如果下方通知栏的“cloudfunctions”窗口显示“Cloud Functions loaded successfully”，则表示本地云函数启动成功，将生成本地函数的Function URI。**请记录下该Function URI的域名和端口信息，例如下图中的http://localhost:18090，后续[调用本地云函数](../调用本地云函数/cloudfoundation-call-local-function.md)时需要使用这些信息。**

   注意

   由于本地云函数和部署至云端的函数获取请求体的方式不同，开发本地云函数时必须按照如下示例获取请求体，否则将无法成功获取请求体：

   let body = event.body ? JSON.parse(event.body) : event;

   完整示例代码请参见[函数示例](../../开发云函数/开发函数/Node.js/cloudfoundation-develop-function-nodejs.md#函数示例)。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/df/v3/FPFHYYaOQXS10lcoz66HWA/zh-cn_image_0000002592219296.png?HW-CC-KV=V1&HW-CC-Date=20260611T070538Z&HW-CC-Expire=86400&HW-CC-Sign=B1EF37E898891EE2F48A294740071460C1866AB552329CCD18FAEA5C29F66BE6)
