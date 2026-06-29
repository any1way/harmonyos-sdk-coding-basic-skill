---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cloudfoundation-database-add-object
title: 新增对象类型
breadcrumb: 指南 > 应用服务 > Cloud Foundation Kit（云开发服务） > 云数据库 > 新增对象类型
category: harmonyos-guides
scraped_at: 2026-06-11T15:05:42+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:8b91bbe4bee9fbad7580f4ad8c744d8b35774f7a103d37eafe8fb4bbd8d0b354
---
开发者需要基于AGC控制台创建对象类型。

## 前提条件

已[开通云数据库服务](../../开发准备/开通云数据库服务/cloudfoundation-enable-database.md)。

## 操作步骤

1. 登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)，点击“开发与服务”。
2. 在项目列表中点击需要创建对象类型的项目。
3. 在左侧导航栏选择“云开发（Serverless）> 云数据库”，进入云数据库页面。
4. 点击“新增”，创建新的对象类型。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/01/v3/Dq6ztK71RKGayjsd9OyCmw/zh-cn_image_0000002592379230.png?HW-CC-KV=V1&HW-CC-Date=20260611T070541Z&HW-CC-Expire=86400&HW-CC-Sign=A6802C8722DF9A45BC62FCB0811E93929CE26F5CA844B2F412780C494B8B2066)
5. 输入“对象类型名”为“BookInfo”后，点击“下一步”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/86/v3/7LIkpBe9RI6ASSWKhc7Iqw/zh-cn_image_0000002622858739.png?HW-CC-KV=V1&HW-CC-Date=20260611T070541Z&HW-CC-Expire=86400&HW-CC-Sign=CE5934A57986988CC65AEAFC837F14187056616F69EB3A2F6A974C7C94E58616)
6. 点击“+新增字段”，新增如下表字段后，点击“下一步”。

   | 字段名称 | 类型 | 主键 | 非空 | 加密 | 默认值 |
   | --- | --- | --- | --- | --- | --- |
   | id | Integer | ✓ | ✓ | – | – |
   | bookName | String | – | ✓ | – | – |
   | author | String | – | – | – | – |
   | price | Double | – | – | – | – |
   | borrowerId | Integer | – | – | – | – |
   | borrowerName | String | – | – | – | – |
   | borrowerTime | Date | – | – | – | – |
7. 点击“+”新增索引，设置“索引名”为“bookName”，点击“下一步”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cb/v3/XiHeGI-oTjWSJCmAeT4gyQ/zh-cn_image_0000002622698859.png?HW-CC-KV=V1&HW-CC-Date=20260611T070541Z&HW-CC-Expire=86400&HW-CC-Sign=B89866E5A19EB14B3CE441564B9CAC7B6202AD1D5C50FB611973BB340B8ACE1A)
8. 按照如下要求设置各角色权限后，点击“确定”。

   | 角色 | query | upsert | delete | 说明 |
   | --- | --- | --- | --- | --- |
   | 所有人 | ✓ | ✓ | ✓ | 代表所有用户，包含认证和非认证用户。  该角色默认拥有query权限，可自定义配置upsert和delete权限。如：角色勾选了upsert权限，该角色可在本对象类型中写入数据。  但是，不建议将upsert和delete权限配置给所有人角色。  当对象类型中设置了加密字段之后，表示开启全程加密功能，此时**所有人**角色将不会拥有query、upsert和delete权限，且不允许修改。 |
   | 认证用户 | ✓ | ✓ | ✓ | 经过AGC登录认证的用户。  该角色默认拥有query权限，可自定义配置upsert和delete权限。如：角色勾选了upsert权限，该角色可在本对象类型中写入数据。  当对象类型中设置了加密字段之后，表示开启全程加密功能，此时**认证用户**角色将不会拥有query、upsert和delete权限，且不允许修改。 |
   | 数据创建者 | ✓ | ✓ | ✓ | 经过认证的数据创建用户。  该角色默认拥有所有权限，且可自定义配置所有权限。如：角色勾选了upsert权限，该角色可在本对象类型中写入数据。  每条数据都有其对应的数据创建人（即应用用户），每个数据创建者仅可以upsert或者delete自己创建的数据，不能upsert或者delete他人创建的数据。  数据创建者的信息保存在数据记录的系统表中。 |
   | 管理员 | ✓ | ✓ | ✓ | 应用开发者，主要是指通过AGC控制台或FaaS（Function as a Service，函数即服务）侧访问云数据库的角色。  该角色默认拥有所有权限，且可自定义配置所有权限。如：角色勾选了upsert权限，该角色可在本对象类型中写入数据。  管理员可以管理并配置其他角色的权限。 |
9. 创建完成后返回对象类型列表，可以查看已创建的对象类型。
10. 勾选创建的BookInfo对象类型，点击“导出”。若不勾选对象类型，默认导出所有对象类型。

    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/94/v3/WfNdgFLxSDm4Jm2WptXR1w/zh-cn_image_0000002592219298.png?HW-CC-KV=V1&HW-CC-Date=20260611T070541Z&HW-CC-Expire=86400&HW-CC-Sign=AD224200778AF13ECDEAA0FBFD8399FD940D0DDE0042244D19C95D8AA0A6BD8C)
11. 导出“json格式”文件，点击“确定”。后续[引入对象类型文件](../引入对象类型文件/cloudfoundation-database-add-file.md)时，需要使用此文件。

    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4b/v3/AtorupC1RAWXaiW2Sb62SA/zh-cn_image_0000002592379232.png?HW-CC-KV=V1&HW-CC-Date=20260611T070541Z&HW-CC-Expire=86400&HW-CC-Sign=4DD62CF55A7008F9C22DE17C04D4F8AA3B72A94E8D1B14273F8515248A647B8A)
