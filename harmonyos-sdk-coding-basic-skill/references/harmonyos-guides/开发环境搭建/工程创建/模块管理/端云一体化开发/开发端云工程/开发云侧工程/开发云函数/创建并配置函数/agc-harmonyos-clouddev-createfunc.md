---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/agc-harmonyos-clouddev-createfunc
title: 创建并配置函数
breadcrumb: 指南 > 开发环境搭建 > 工程创建 > 模块管理 > 端云一体化开发 > 开发端云工程 > 开发云侧工程 > 开发云函数 > 创建并配置函数
category: harmonyos-guides
scraped_at: 2026-06-01T15:18:20+08:00
doc_updated_at: 2026-05-07
content_hash: sha256:2c45c5cd2b76db76f59acec436e131c6e604fcf27845892b6fc8cd7f00f7a21f
---
您可直接在DevEco Studio创建函数、为函数配置调用的触发器等。

## 创建函数

1. 右击“cloudfunctions”目录，选择“New > Cloud Function”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b4/v3/B4r_fWvqTDekcvzfye5SGQ/zh-cn_image_0000002383015060.png?HW-CC-KV=V1&HW-CC-Date=20260601T071821Z&HW-CC-Expire=86400&HW-CC-Sign=2205A543298F8DDDF9DAFBAAB9A2DB0C36F7A82596555E6745D55FF46FE57751)
2. 在“Select the Cloud Function Type”栏选择“Cloud Function”，输入云函数名称（如“my-cloud-function”），点击“OK”。

   函数名称长度2-63个字符，仅支持小写英文字母、数字、中划线（-），首字符必须为小写字母，结尾不能为中划线（-）。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b1/v3/p9FgbXDdTjCRvEmExkpDSQ/zh-cn_image_0000002214858969.png?HW-CC-KV=V1&HW-CC-Date=20260601T071821Z&HW-CC-Expire=86400&HW-CC-Sign=B872F163AAD3CA974DA40DD92D9F8FBB175594B3B444630D6617C777CD904866)

   “cloudfunctions”目录下生成新建的“my-cloud-function”函数目录，目录下主要包含如下文件：

   * 函数配置文件“function-config.json”
   * 函数入口文件“myCloudFunction.ts”
   * 依赖配置文件“package.json”

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ec/v3/pesHo4zzTb2eTGua4JNQ-Q/zh-cn_image_0000002179338652.png?HW-CC-KV=V1&HW-CC-Date=20260601T071821Z&HW-CC-Expire=86400&HW-CC-Sign=D2D1BA39A06D4A435397ACF47A831FF60C64D65AE8B493FF448A4AD76550E6CA)

## 配置函数

函数创建完毕后，您可在配置文件“function-config.json”的“triggers”下配置触发器，通过触发器暴露的触发条件来实现函数调用。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7/v3/S0lq7ajASxSFM-OEjXuMaQ/zh-cn_image_0000002296067548.png?HW-CC-KV=V1&HW-CC-Date=20260601T071821Z&HW-CC-Expire=86400&HW-CC-Sign=B729810658B0C677EB7BE842AA65376030F3BEA0B80CEADC5EF21EABE4F569BD)

说明

* “functionType”表示函数类型，值为创建时自动生成。“0”表示云函数，“1”表示云对象。

* 如您需在函数部署完成后更新触发器，请先删除之前的触发器配置，再添加新的触发器配置，否则您的更新将不生效。

* HTTP触发器

  “function-config.json”文件中已为您自动完成HTTP触发器配置。配置了HTTP触发器的函数被部署到云端后，您的应用即可通过Cloud Foundation Kit调用函数。关于如何使用HTTP触发器调用函数，请参见[调用函数](<../../../../../../../../应用服务/Cloud Foundation Kit（云开发服务）/云函数/开发云函数/调用函数/cloudfoundation-call-function.md>)。

  ```
  1. {
  2. "type": "http",
  3. "properties": {
  4. "enableUrlDecode": true,
  5. "authFlag": "true",
  6. "authAlgor": "HDA-SYSTEM",
  7. "authType": "apigw-client"
  8. }
  9. }
  ```

  + type：触发器类型，配置为“http”。
  + properties：触发器属性，属性参数如下表所示。

    | 参数 | 说明 |
    | --- | --- |
    | enableUrlDecode | 通过HTTP触发器触发函数时，对于contentType为“application/x-www-form-urlencoded”的触发请求，是否使用URLDecoder对请求body进行解码再转发到函数中。  - true：启用。 - false：不启用。 |
    | authFlag | 是否鉴权，默认为true。 |
    | authAlgor | 鉴权算法，默认为HDA-SYSTEM。 |
    | authType | HTTP触发器的认证类型。  - apigw-client：端侧网关认证，适用于来自APP客户端侧（即本地应用或者项目）的函数调用。 - cloudgw-client：云侧网关认证，适用于来自APP服务器侧（即云函数）的函数调用。 |

* CLOUDDB触发器

  您需在“function-config.json”文件中手动为函数配置CLOUDDB触发器。配置CLOUDDB完成后，当云数据库发生插入或者更新数据、删除数据、清空数据等变更操作时将触发云函数。

  ```
  1. {
  2. "type": "clouddb",
  3. "properties": {
  4. "eventSourceId": "9***-test-user",
  5. "eventType": "onUpsert",
  6. "enabled": "true"
  7. }
  8. }
  ```

  + type：触发器类型，配置为“clouddb”。
  + properties：触发器属性，属性参数如下表所示。

    | 参数 | 说明 |
    | --- | --- |
    | eventSourceId | CLOUDDB触发器的数据源。  格式为：项目ID-CloudDB存储区名称-CloudDB对象类型名称，例如**“**99034201568569469-StorageArea-student**”**。  - CloudDB存储区名称以字母开头，可选范围为[0-9A-Za-z]，不带下划线，长度为1~20个字符。 - CloudDB对象类型名称以字母开头，可选范围为[0-9A-Za-z\_]，不允许以sqlite\_开头，不允许以下划线结尾，长度为1~30个字符。 |
    | eventType | 触发器支持的事件类型。  - onUpsert：数据表插入或更新数据。 - onDelete：数据表删除数据。 - onDeleteAll：数据表清空。 - onWrite：数据插入或更新事件、数据删除事件、数据表清空事件。 |
    | enabled | 标识触发器的状态。默认为启用（true），可设置。 |
