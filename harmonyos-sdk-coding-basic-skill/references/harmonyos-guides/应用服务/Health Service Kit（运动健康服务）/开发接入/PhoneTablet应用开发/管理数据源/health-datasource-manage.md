---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/health-datasource-manage
title: 管理数据源
breadcrumb: 指南 > 应用服务 > Health Service Kit（运动健康服务） > 开发接入 > Phone/Tablet应用开发 > 管理数据源
category: harmonyos-guides
scraped_at: 2026-06-01T15:04:15+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:e430a2821c80187f2646ad86f5e43d22f161a85646d0d12e321f10ff565b3ec8
---
## 场景介绍

数据源提供了应用或者设备的信息，每一个运动健康数据必须关联数据源信息，通过DataSourceId进行关联。

说明

DataSourceId在插入数据源信息时由平台生成，无法更改。

## 接口说明

| 接口名 | 描述 |
| --- | --- |
| [insertDataSource](<../../../../../../harmonyos-references/Health Service Kit（运动健康服务）/ArkTS API/healthStore (运动健康数据服务)/health-api-healthstore.md#healthstoreinsertdatasource>)(dataSource: [DataSourceBase](<../../../../../../harmonyos-references/Health Service Kit（运动健康服务）/ArkTS API/healthStore (运动健康数据服务)/health-api-healthstore.md#datasourcebase>)): Promise<string> | 插入数据源，入参为数据源基类[DataSourceBase](<../../../../../../harmonyos-references/Health Service Kit（运动健康服务）/ArkTS API/healthStore (运动健康数据服务)/health-api-healthstore.md#datasourcebase>)。 |
| [readDataSource](<../../../../../../harmonyos-references/Health Service Kit（运动健康服务）/ArkTS API/healthStore (运动健康数据服务)/health-api-healthstore.md#healthstorereaddatasource>)(request: [DataSourceReadRequest](<../../../../../../harmonyos-references/Health Service Kit（运动健康服务）/ArkTS API/healthStore (运动健康数据服务)/health-api-healthstore.md#datasourcereadrequest>)): Promise<[DataSource](<../../../../../../harmonyos-references/Health Service Kit（运动健康服务）/ArkTS API/healthStore (运动健康数据服务)/health-api-healthstore.md#datasource>)[]> | 查询数据源，通过[DataSourceReadRequest](<../../../../../../harmonyos-references/Health Service Kit（运动健康服务）/ArkTS API/healthStore (运动健康数据服务)/health-api-healthstore.md#datasourcereadrequest>)设置查询条件，可按DataSourceId/包名/设备UniqueId查询数据源。 |
| [updateDataSource](<../../../../../../harmonyos-references/Health Service Kit（运动健康服务）/ArkTS API/healthStore (运动健康数据服务)/health-api-healthstore.md#healthstoreupdatedatasource>)(dataSource: [DataSource](<../../../../../../harmonyos-references/Health Service Kit（运动健康服务）/ArkTS API/healthStore (运动健康数据服务)/health-api-healthstore.md#datasource>)): Promise<void> | 更新数据源，其中数据源的dataSourceId和uniqueId字段无法更新。 |

## 开发前检查

* 完成[申请运动健康服务](../../开发准备/申请运动健康服务/health-apply.md)与[配置Client ID](<../../开发准备/配置Client ID/health-configuration-client-id.md>)。
* 接口首次调用前，需先使用[init](<../../../../../../harmonyos-references/Health Service Kit（运动健康服务）/ArkTS API/healthStore (运动健康数据服务)/health-api-healthstore.md#healthstoreinit>)方法进行初始化。
* 需先通过[用户授权](../管理用户授权/health-add-permissions.md#用户授权)接口引导用户授权，用户授权任意数据类型权限后，才有权限调用数据源相关接口。
* 错误码请参考[ArkTS API错误码](<../../../../../../harmonyos-references/Health Service Kit（运动健康服务）/ArkTS API错误码/errorcode-healthservice.md>)，常见问题请参考[Health Service Kit常见问题](<../../../Health Service Kit常见问题/health-faqs.md>)。

## 开发步骤

### 插入数据源

1.导入运动健康服务功能模块及相关公共模块。

```
1. import { healthStore } from '@kit.HealthServiceKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
```

2.创建数据源。

```
1. let dataSource: healthStore.DataSourceBase = {
2. deviceInfo: {
3. uniqueId: 'test',
4. name: 'test', // 插入数据源时此字段必填
5. category: healthStore.DeviceCategory.WEARABLE_BAND, // 插入数据源时此字段必填
6. productId: '0554', // 插入数据源时此字段必填
7. model: 'lotana',
8. manufacturer: 'HUAWEI',
9. mac: 'testDeviceMac',
10. sn: 'testDeviceSn',
11. hardwareVersion: '1',
12. softwareVersion: '2',
13. firmwareVersion: '3',
14. udid: ''
15. }
16. }
```

3.调用[insertDataSource](<../../../../../../harmonyos-references/Health Service Kit（运动健康服务）/ArkTS API/healthStore (运动健康数据服务)/health-api-healthstore.md#healthstoreinsertdatasource>)方法执行插入请求，并处理返回结果。

```
1. try {
2. const dataSourceId = await healthStore.insertDataSource(dataSource);
3. hilog.info(0x0000, 'testTag', `Succeeded in inserting dataSource, the dataSourceId is ${dataSourceId}.`);
4. } catch (err) {
5. hilog.error(0x0000, 'testTag', `Failed to insert dataSource. Code: ${err.code}, message: ${err.message}`);
6. }
```

### 读取数据源

1.导入运动健康服务功能模块及相关公共模块。

```
1. import { healthStore } from '@kit.HealthServiceKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
```

2.创建数据源读取请求。

```
1. let readSourceRequest: healthStore.DataSourceReadRequest = {
2. deviceUniqueId: 'testudidupdate'
3. }
```

3.调用[readDataSource](<../../../../../../harmonyos-references/Health Service Kit（运动健康服务）/ArkTS API/healthStore (运动健康数据服务)/health-api-healthstore.md#healthstorereaddatasource>)方法执行查询请求，并处理返回结果。

```
1. try {
2. let dataSources = await healthStore.readDataSource(readSourceRequest);
3. dataSources.forEach((dataSource) => {
4. hilog.info(0x0000, 'testTag', `Succeeded in reading dataSource, the dataSourceId is ${dataSource.dataSourceId}.`);
5. });
6. } catch (err) {
7. hilog.error(0x0000, 'testTag', `Failed to read dataSource. Code: ${err.code}, message: ${err.message}`);
8. }
```

### 更新数据源

1.导入运动健康服务功能模块及相关公共模块。

```
1. import { healthStore } from '@kit.HealthServiceKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
```

2.创建数据源。

```
1. let newDataSource: healthStore.DataSource = {
2. deviceInfo: {
3. uniqueId: 'test',
4. name: 'test',
5. category: healthStore.DeviceCategory.WEARABLE_BAND,
6. productId: '0554',
7. model: 'lotana',
8. manufacturer: 'HUAWEI',
9. mac: 'testDeviceMac',
10. sn: 'testDeviceSn',
11. hardwareVersion: '1',
12. softwareVersion: '2',
13. firmwareVersion: '3',
14. // 修改udid
15. udid: 'updateudid'
16. },
17. // 此处dataSourceId值为开发步骤插入数据源时，返回的dataSourceId
18. dataSourceId: 'xxx'
19. }
```

3.调用[updateDataSource](<../../../../../../harmonyos-references/Health Service Kit（运动健康服务）/ArkTS API/healthStore (运动健康数据服务)/health-api-healthstore.md#healthstoreupdatedatasource>)方法执行更新请求，并处理返回结果。

```
1. try {
2. await healthStore.updateDataSource(newDataSource);
3. hilog.info(0x0000, 'testTag', 'Succeeded in updating dataSource.');
4. } catch (err) {
5. hilog.error(0x0000, 'testTag', `Failed to update dataSource. Code: ${err.code}, message: ${err.message}`);
6. }
```
