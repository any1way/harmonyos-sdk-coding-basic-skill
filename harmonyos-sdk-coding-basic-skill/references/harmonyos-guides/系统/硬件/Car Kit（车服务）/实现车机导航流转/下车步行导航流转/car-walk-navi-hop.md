---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/car-walk-navi-hop
title: 下车步行导航流转
breadcrumb: 指南 > 系统 > 硬件 > Car Kit（车服务） > 实现车机导航流转 > 下车步行导航流转
category: harmonyos-guides
scraped_at: 2026-06-11T14:50:58+08:00
doc_updated_at: 2026-04-30
content_hash: sha256:e2306820cd2b7ede13b81cf3a780b840a53483356614e31c3403c6d842066aa8
---
支持将车机指定的地图应用的步行导航数据流转至手机。

## 场景介绍

下车步行导航流转：用户下车前，车机地图应用导航还未结束，下车后可将车机上的导航数据流转至手机，发起步行导航。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/45/v3/UgCChyj4QZSUdKm5KeLEvA/zh-cn_image_0000002592378832.png?HW-CC-KV=V1&HW-CC-Date=20260611T065057Z&HW-CC-Expire=86400&HW-CC-Sign=B0193163F5F78EB3AF2F7CB5C155BB5E5AE192CDFF6991779D1AE5B7AF980B12)

## 接口说明

| 接口名 | 描述 |
| --- | --- |
| [registerSystemNavigationListener](<../../../../../../harmonyos-references/Car Kit（车服务）/ArkTS API/navigationInfoMgr（导航信息管理）/car-navigationinfomgr.md#registersystemnavigationlistener>) | 注册监听系统导航信息和指令。 |
| [unregisterSystemNavigationListener](<../../../../../../harmonyos-references/Car Kit（车服务）/ArkTS API/navigationInfoMgr（导航信息管理）/car-navigationinfomgr.md#unregistersystemnavigationlistener>) | 取消注册监听系统导航信息和指令。 |

## 开发流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e3/v3/tB9QfyWITjiT438bIVImjg/zh-cn_image_0000002622858339.png?HW-CC-KV=V1&HW-CC-Date=20260611T065057Z&HW-CC-Expire=86400&HW-CC-Sign=7ED357FC856E114F8D96D98475E53446E7D91255BC094A953451AADB3022069F)

## 开发步骤

1. 能力配置。

   请参考[配置能力](../../开发准备/car-preparations.md#配置能力)进行配置。下车步行导航流转场景下，metadata的name取值为carHopCapability，value取值应为**getOffCarNavi**。示例代码如下所示：

   ```
   1. "metadata": [
   2. {
   3. "name": "carHopCapability",
   4. "value": "getOffCarNavi"
   5. }
   6. ]
   ```
2. 导入相关模块。

   ```
   1. import { navigationInfoMgr } from '@kit.CarKit';
   2. import { hilog } from '@kit.PerformanceAnalysisKit';
   ```
3. 监听系统导航信息和指令。

   地图应用需要注册监听系统导航信息和指令，方便地图应用接收系统指令。用户下车后，系统会给地图应用发送START\_NAVIGATION指令，地图应用在收到指令后即可开启步行导航任务。

   ```
   1. // 实现SystemNavigationListener接口
   2. class Listener implements navigationInfoMgr.SystemNavigationListener {
   3. // 实现onQueryNavigationInfo方法
   4. onQueryNavigationInfo(query: navigationInfoMgr.QueryType,
   5. args: Record<string, Object>): Promise<navigationInfoMgr.ResultData> {
   6. // 返回导航信息给系统
   7. return new Promise(resolve => {
   8. let ret: navigationInfoMgr.ResultData = {
   9. code: 1001,
   10. message: 'message test1',
   11. data: args
   12. };
   13. resolve(ret);
   14. });
   15. }

   17. // 实现onReceiveNavigationCmd方法
   18. onReceiveNavigationCmd(command: navigationInfoMgr.CommandType,
   19. args: Record<string, Object>): Promise<navigationInfoMgr.ResultData> {
   20. if (command == navigationInfoMgr.CommandType.START_NAVIGATION) {
   21. // 地图应用处理下车后自动开启步行导航的逻辑
   22. if (args !== undefined && args !== null) {
   23. // 获取导航类型
   24. let naviType: navigationInfoMgr.NaviType = args['naviType'] as navigationInfoMgr.NaviType;
   25. // 如果是步行导航
   26. if (naviType === navigationInfoMgr.NaviType.WALKING) {
   27. let destPoi: string = args['destPoi'] as string;
   28. // 获取目的地名
   29. let destLocationName: string = args['destName'] as string;
   30. // 获取目的地纬度
   31. let destLatitude: string = destPoi?.split(',')[0].toString();
   32. // 获取目的地经度
   33. let destLongitude: string = destPoi?.split(',')[1].toString();
   34. // 开发者根据destLocationName、destLatitude、destLongitude发起步行导航
   35. // ...
   36. }
   37. }
   38. }
   39. return new Promise(resolve => {
   40. let ret: navigationInfoMgr.ResultData = {
   41. code: 1002,
   42. message: 'message test2',
   43. data: args
   44. };
   45. resolve(ret);
   46. });
   47. }
   48. }

   50. try {
   51. // 获取NavigationController实例
   52. let navInfoController: navigationInfoMgr.NavigationController = navigationInfoMgr.getNavigationController();
   53. // 注册监听系统导航信息和指令
   54. navInfoController.registerSystemNavigationListener(new Listener());
   55. } catch (e) {
   56. // 捕获接口调用异常时的错误码并做相应处理
   57. hilog.error(0x0000, 'testTag', `register system navigation listener, error code: ${e?.code}`);
   58. }
   ```
4. 取消监听。

   在地图应用退出时，需要取消之前注册的监听，减少手机系统不必要的资源消耗。

   ```
   1. try {
   2. // 获取NavigationController实例
   3. let navInfoController: navigationInfoMgr.NavigationController = navigationInfoMgr.getNavigationController();
   4. // 取消注册监听系统导航信息和指令
   5. navInfoController.unregisterSystemNavigationListener();
   6. } catch (e) {
   7. // 捕获接口调用异常时的错误码并做相应处理
   8. hilog.error(0x0000, 'testTag', `unregister system navigation listener error, error code: ${e?.code}`);
   9. }
   ```
