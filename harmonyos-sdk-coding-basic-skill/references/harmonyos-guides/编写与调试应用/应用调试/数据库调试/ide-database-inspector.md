---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-database-inspector
title: 数据库调试
breadcrumb: 指南 > 编写与调试应用 > 应用调试 > 数据库调试
category: harmonyos-guides
scraped_at: 2026-06-11T15:29:25+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:cf22e6d84a1ef221787c0057af1a71ad11f709af2aa10da9ae0e77fae7a5bb34
---
从DevEco Studio 6.0.2 Beta1版本开始，新增Database Inspector，支持在DevEco Studio上执行SQL语句查看、修改应用数据库，无需将应用数据库先导出到本地，提升开发调试效率，当前支持SQLite和向量数据库。

开发者也可以通过命令行工具调试数据库，具体操作方式请参考[vector-store数据库调试工具指导](../../../应用框架/ArkData（方舟数据管理）/arkdata数据库调试工具/vector-store数据库调试工具指导/vector-store-debug-tool.md)、[SQLite调试工具指导](../../../应用框架/ArkData（方舟数据管理）/SQLite调试工具指导/sqlite-database-debug-tool.md)。

## 使用场景

* 应用某个操作会修改数据库内容，可以实时查看修改后的内容是否符合预期。
* 可以实时修改数据库内数据，构造测试场景，提升测试效率。

## 使用约束

* 设备系统需要不低于API 22。低于API 22时，SQLite数据库仅支持查看，不支持修改，向量数据库无法使用。
* 不支持使用release签名的应用。
* 仅支持调试database目录下的数据库。
* 不支持调试加密数据库，建议使用非加密库。
* 不支持调试隐私用户、多用户数据库，建议使用默认用户。
* 不支持导入导出数据库。
* 执行SQL时，存在以下约束：
  + 不支持执行多条SQL。
  + 存在多条SQL时，不支持高亮选择后执行单条SQL。
  + SQL执行不支持历史记录。
  + SQL执行不支持事务。

## 操作步骤

1. 点击菜单栏**View > Tool Windows > Database Inspector**，打开Database Inspector。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d3/v3/o3QUa7yJRyWngmmKAfGs0A/zh-cn_image_0000002571546676.png?HW-CC-KV=V1&HW-CC-Date=20260611T072925Z&HW-CC-Expire=86400&HW-CC-Sign=84432DA1255273242C06DFB46EF8D49334D8FFC84CCA79CC583AC71324F09612)

   Database Inspector打开后，页面各区域作用如下：①选择设备，②选择应用包名，③数据库和表信息展示，④SQL执行和数据查看。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f2/v3/7RUesh7XQJyIl62P3OrNow/zh-cn_image_0000002571387042.png?HW-CC-KV=V1&HW-CC-Date=20260611T072925Z&HW-CC-Expire=86400&HW-CC-Sign=9A94360E1AD21849C983FE517FAF5C95EE30A30821D1F8AA0E45D0DF4A029A63)
2. 从设备下拉列表中选择设备（设备需已连接）。
3. 选择包名，点击右侧的**Connect to Databases**按钮，即可查看数据库相关信息。（如果使用DevEco Studio 6.0.2 Beta1版本，按钮名称是**Execute**）。

   说明

   设备系统版本低于API 22时，Database Inspector会将数据库下载到本地计算机，界面上显示的是本地计算机路径，设备系统为API 22及以上版本时，界面上显示的是设备上的数据库路径。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/aa/v3/_uRE15arT56AbXNvQVhbdg/zh-cn_image_0000002602066157.png?HW-CC-KV=V1&HW-CC-Date=20260611T072925Z&HW-CC-Expire=86400&HW-CC-Sign=859CC15A06020255F3F8CF214435C10FB798247A1D71683548CE03AE17228E01)
4. 双击数据库表名，右侧区域展示表数据，默认按照20条/页展示。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a2/v3/aT41LajEQaqB7pTulzBDJA/zh-cn_image_0000002571546672.png?HW-CC-KV=V1&HW-CC-Date=20260611T072925Z&HW-CC-Expire=86400&HW-CC-Sign=1D2837828AE0A76A1F91B8DBCAE21BC6BB4A73BDF4CEE58E794CD1E61BB34793)
5. 左侧区域点击**New Query**后，右侧会出现**SQL Editor**页签，根据需要选择数据库，并输入SQL后，点击**Execute**按钮即可查看或修改数据。

   修改数据后，点击SQL输入框下方的**Refresh Table**刷新页面上的数据。

   说明

   * 通过SQL修改数据或应用更新数据后，数据展示页面不支持自动刷新，需要重新执行查询语句或者点击刷新按钮。
   * 数据展示页面不支持可视化修改。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/42/v3/BCowja0KR7qEvzIafcksjw/zh-cn_image_0000002571546674.png?HW-CC-KV=V1&HW-CC-Date=20260611T072925Z&HW-CC-Expire=86400&HW-CC-Sign=60D388CAA055B2803DAD80C178D8A2041A19F717D1F1799756AE9E7C0288EE4A)
