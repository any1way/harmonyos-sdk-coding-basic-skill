---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/share-sec-panel-back
title: 分享详情页关闭分享面板
breadcrumb: 指南 > 应用服务 > Share Kit（分享服务） > 系统分享 > 目标应用处理分享内容 > 分享详情页关闭分享面板
category: harmonyos-guides
scraped_at: 2026-06-01T15:11:30+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:bda6f9c7358c1d4dc783b7ae28a4d9c6560661a697f2cde678fc99af18e2f622
---
从分享详情页返回分享面板时，可通过设置resultCode值为特定的[ShareAbilityResultCode](<../../../../../../harmonyos-references/Share Kit（分享服务）/ArkTS API/systemShare（分享）/share-system-share.md#shareabilityresultcode>)，以告知分享面板做出不同的处理，具体处理方式如下：

* ERROR：返回分享面板，并提示用户发生错误。
* BACK：正常返回分享面板。
* CLOSE：关闭分享面板。

## 开发步骤

1. 导入相关模块。

   ```
   1. import { ShareExtensionAbility, UIExtensionContentSession, Want } from '@kit.AbilityKit';
   2. import { systemShare } from '@kit.ShareKit';
   ```
2. 目标应用可以通过terminateSelfWithResult接口，设置resultCode值为systemShare.ShareAbilityResultCode.CLOSE，以关闭分享面板。

   ```
   1. export default class TestShareAbility extends ShareExtensionAbility {
   2. async onSessionCreate(want: Want, session: UIExtensionContentSession) {
   3. session.terminateSelfWithResult({
   4. resultCode: systemShare.ShareAbilityResultCode.CLOSE
   5. });
   6. }
   7. }
   ```
