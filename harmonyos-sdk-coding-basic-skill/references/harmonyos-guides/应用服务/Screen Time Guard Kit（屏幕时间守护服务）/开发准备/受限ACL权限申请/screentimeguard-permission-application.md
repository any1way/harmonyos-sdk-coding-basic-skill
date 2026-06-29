---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/screentimeguard-permission-application
title: 受限ACL权限申请
breadcrumb: 指南 > 应用服务 > Screen Time Guard Kit（屏幕时间守护服务） > 开发准备 > 受限ACL权限申请
category: harmonyos-guides
scraped_at: 2026-06-11T15:14:37+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:bbb28ff17228191bbd3b399cb5d2ae6f3ebb5d0f3bb5d5860bb5ba92d82b25a0
---
1. 在 [申请调试Profile](https://developer.huawei.com/consumer/cn/doc/app/agc-help-debug-profile-0000002248181278)和[发布Profile文件](https://developer.huawei.com/consumer/cn/doc/app/agc-help-release-profile-0000002248341090)之前，需要[申请相应的ACL权限](https://developer.huawei.com/consumer/cn/doc/app/agc-help-apply-acl-0000002394212138)。
2. 登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html#/)，点击“开发与服务”，在项目列表中找到对应的项目，并点击选择您需要申请ACL权限的应用。在“项目设置”页面，选择“ACL权限”页签，开始为应用申请ACL权限。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0a/v3/J6ZJKNaOTAmcfcnsGe47ZQ/zh-cn_image_0000002592379530.png?HW-CC-KV=V1&HW-CC-Date=20260611T071436Z&HW-CC-Expire=86400&HW-CC-Sign=D1D46CE840E955581081AA8046CF2E16B76FBD9B935664BCDBC4EAA04BCECE3A)
3. 在核对注意事项后，在“未获取权限”区域中勾选“我已知晓”。在权限搜索框中输入"ohos.permission.MANAGE\_SCREEN\_TIME\_GUARD"，查找并勾选权限，提交申请。
4. 根据实际业务需求填写申请原因并提交，提交后将在1个工作日回复。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3b/v3/Rm7L09xORtSKXUgzFXKsJQ/zh-cn_image_0000002622859039.png?HW-CC-KV=V1&HW-CC-Date=20260611T071436Z&HW-CC-Expire=86400&HW-CC-Sign=C365CEFEF378A3FDA7B42609CBB506E0F0114A093DF04FD2B34D98D054A3CA93)
5. 权限申请通过后，在申请profile文件时，在“申请权限”栏选中“受限ACL权限（HarmonyOS API9及以上）”选项，点击“选择”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5f/v3/KQdOACusTduYgyQikSOrbg/zh-cn_image_0000002622699159.png?HW-CC-KV=V1&HW-CC-Date=20260611T071436Z&HW-CC-Expire=86400&HW-CC-Sign=4AC77F31433D1B4D0632EFE3088D3A43CAC1C3136CE79A8B28FB3C4A1EC9F6EA)
6. 在弹出的“选择受限ACL权限”窗口可以看到已申请的权限，勾选后点击确定。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2e/v3/3Co2GXvsSYmJW0fRuE6TzQ/zh-cn_image_0000002592219598.png?HW-CC-KV=V1&HW-CC-Date=20260611T071436Z&HW-CC-Expire=86400&HW-CC-Sign=5335BF8CDF0C7B8BD68EBD618C30CDC607E926964BA12374BA00A26CC87378B2)
7. 选择权限后点击“添加”生成新的Profile文件，下载后按[手动配置签名信息](../../../../编写与调试应用/配置调试签名/ide-signing.md#section297715173233)替换profile文件。
8. 在工程中entry模块的module.json5文件中添加"ohos.permission.MANAGE\_SCREEN\_TIME\_GUARD"权限，如下所示：

   ```
   1. "requestPermissions": [{
   2. "name": "ohos.permission.MANAGE_SCREEN_TIME_GUARD"
   3. }]
   ```
