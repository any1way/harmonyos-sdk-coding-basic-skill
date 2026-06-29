---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/map-faq-1
title: 地图不显示
breadcrumb: 指南 > 应用服务 > Map Kit（地图服务） > Map Kit常见问题 > 地图不显示
category: harmonyos-guides
scraped_at: 2026-06-11T15:10:46+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:82c3aa31ab2867e7edbd2a2e4575c735cbea7aa729cca11d08a349ffe53e04ce
---
**现象描述**

无法加载地图。

**可能原因**

1. 无网络。
2. 应用身份校验失败或地图权限未开通。
3. 未完成基本准备工作。

**处理步骤**

1. 检查是否存在日志：get network status error, code: 201, message:Permission denied。日志存在，说明应用缺少获取网络状态的权限。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/31/v3/wUeYQ2GlRBm1mneYzTdMDQ/zh-cn_image_0000002622699051.png?HW-CC-KV=V1&HW-CC-Date=20260611T071046Z&HW-CC-Expire=86400&HW-CC-Sign=9C7ED5274A2E8869386577D915333473C2C222466517840D26A1542152B23AF7)

   请在应用的module.json5文件中配置获取网络状态的权限。

   ```
   1. {
   2. "module" : {
   3. // ...
   4. "requestPermissions": [
   5. {
   6. "name": "ohos.permission.INTERNET",
   7. "usedScene": {
   8. "when": "always"
   9. }
   10. },
   11. {
   12. "name": "ohos.permission.GET_NETWORK_INFO",
   13. "usedScene": {
   14. "when": "always"
   15. }
   16. }
   17. ]
   18. }
   19. }
   ```

   请检查应用日志中是否存在日志：The network is unavailable。日志存在，说明设备网络存在问题，请检查网络状态。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8f/v3/4_cC1uWkScWBHh5SipgXVQ/zh-cn_image_0000002592219490.png?HW-CC-KV=V1&HW-CC-Date=20260611T071046Z&HW-CC-Expire=86400&HW-CC-Sign=0FC6E51D31F84E077C74A37A3417C9431AC9C321095B6B5AADFCB0194FF57580)
2. 请检查应用日志中是否存在日志：The app does not have map permission。日志存在，说明应用身份校验失败。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fb/v3/PBePhkooRv6Al8AcDHPRog/zh-cn_image_0000002592379424.png?HW-CC-KV=V1&HW-CC-Date=20260611T071046Z&HW-CC-Expire=86400&HW-CC-Sign=13B6D393A4F03E06C9FD7BE515566B2B0BF881FD7EBC112A0AA0E49EE2F1E827)

   查看com.huawei.hms.mapservice进程日志，检查是否存在该日志：App authentication failed. code: 1002600003。参考[1002600003](<../../../../../harmonyos-references/Map Kit（地图服务）/ArkTS API/ArkTS API错误码/errorcode-map.md#section1002600003-应用身份校验失败>)完成应用身份校验。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ed/v3/sq_mMfOCTmSZRxiHV5aMSw/zh-cn_image_0000002622858933.png?HW-CC-KV=V1&HW-CC-Date=20260611T071046Z&HW-CC-Expire=86400&HW-CC-Sign=CDEC180ABAC300284C26DAC392A08F5181428441A95C10B530E0AD29E6B80FA9)
3. 请参考“[应用开发准备](../../../../应用开发准备/应用开发准备/application-dev-overview.md)”检查是否完成基本准备工作。
