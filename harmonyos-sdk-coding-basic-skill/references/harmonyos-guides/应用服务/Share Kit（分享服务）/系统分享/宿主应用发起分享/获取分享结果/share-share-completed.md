---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/share-share-completed
title: 获取分享结果
breadcrumb: 指南 > 应用服务 > Share Kit（分享服务） > 系统分享 > 宿主应用发起分享 > 获取分享结果
category: harmonyos-guides
scraped_at: 2026-06-01T15:11:26+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:c9c1f33c66bf4e11d2173f5c8edaff1358b6f0c66389748076929d03cf6c0032
---
## 场景介绍

从5.1.0(18)版本开始，支持宿主应用获取用户分享结果。

基于业务实现需要，开发者可统计用户使用分享功能时，将内容分享到了哪些渠道。渠道信息规则如下：

* 系统操作有固定名称。请参见：[ShareAbilityName](<../../../../../../harmonyos-references/Share Kit（分享服务）/ArkTS API/systemShare（分享）/share-system-share.md#shareabilityname>)。
* 非系统操作采用'[bundleName]#[moduleName]#[abilityName]'格式拼接。

## 开发步骤

1. 导入相关模块。

   ```
   1. import { common } from '@kit.AbilityKit';
   2. import { systemShare } from '@kit.ShareKit';
   3. import { uniformTypeDescriptor as utd } from '@kit.ArkData';
   ```
2. 构造分享数据。

   ```
   1. // 构造ShareData，需配置一条有效数据信息
   2. let data: systemShare.SharedData = new systemShare.SharedData({
   3. utd: utd.UniformDataType.PLAIN_TEXT,
   4. content: 'Hello HarmonyOS'
   5. });
   ```
3. 注册分享结果监听事件，并启动分享面板。

   ```
   1. // 构建ShareController
   2. let controller: systemShare.ShareController = new systemShare.ShareController(data);
   3. // 获取UIAbility上下文对象
   4. let uiContext: UIContext = this.getUIContext();
   5. let context: common.UIAbilityContext = uiContext.getHostContext() as common.UIAbilityContext;
   6. // 注册分享结果事件监听
   7. controller.on('shareCompleted', (result: systemShare.ShareOperationResult) => {
   8. console.info('shareCompleted name:', result.targetAbilityInfo.name);
   9. // 可根据分享渠道进行数据统计等操作
   10. });

   12. // 进行分享面板显示
   13. controller.show(context, {
   14. previewMode: systemShare.SharePreviewMode.DEFAULT,
   15. selectionMode: systemShare.SelectionMode.SINGLE
   16. });
   ```
