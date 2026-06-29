---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/share-utd-text
title: 分享文本
breadcrumb: 指南 > 应用服务 > Share Kit（分享服务） > 系统分享 > 常见分享场景 > 分享文本
category: harmonyos-guides
scraped_at: 2026-06-11T15:15:18+08:00
doc_updated_at: 2026-05-26
content_hash: sha256:91c7d841020d2cbb1db08019c4480a7a6d183e209e60d24a41fd2e532ad008e7
---

纯文本类型分享支持将一段文字分享到目标设备/目标应用。

* 目标设备接收时，文本会转化为.txt文件保存在文件管理中。
* 目标应用接收时，可便捷地处理文本内容。例如：将文字分享给备忘录，可新增一条备忘录内容。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1b/v3/qh5ADsaURIWLvnffOoFaQg/zh-cn_image_0000002592379550.png?HW-CC-KV=V1&HW-CC-Date=20260611T071517Z&HW-CC-Expire=86400&HW-CC-Sign=5DE9C1CB5671E593E1813E1E535C096F992E0E0BB0CDD2BBBC0AE9EAA269314B)

## 开发步骤

1. 导入相关模块。

   ```
   1. import { systemShare } from '@kit.ShareKit';
   2. import { uniformTypeDescriptor as utd } from '@kit.ArkData';
   3. import { common } from '@kit.AbilityKit';
   4. import { BusinessError } from '@kit.BasicServicesKit';
   ```
2. 构造分享数据。

   ```
   1. // 构造ShareData，需配置一条有效数据信息
   2. let shareData: systemShare.SharedData = new systemShare.SharedData({
   3. utd: utd.UniformDataType.TEXT,
   4. content: '这是一段文本内容',
   5. title: '文本内容', // 不传title字段时,显示content
   6. description: '文本描述',
   7. // thumbnail: new Uint8Array() // 推荐传入适合的缩略图 不传则显示默认text图标
   8. });
   ```
3. 额外增加一条数据。

   ```
   1. shareData.addRecord({
   2. utd: utd.UniformDataType.TEXT,
   3. content: '这是一段文本内容',
   4. title: '文本内容', // 不传title字段时,显示content
   5. description: '文本描述'
   6. });
   ```
4. 启动分享面板。

   ```
   1. // 进行分享面板显示
   2. let controller: systemShare.ShareController = new systemShare.ShareController(shareData);
   3. let uiContext: UIContext = this.getUIContext();
   4. let context: common.UIAbilityContext = uiContext.getHostContext() as common.UIAbilityContext;
   5. controller.show(context, {
   6. selectionMode: systemShare.SelectionMode.SINGLE,
   7. previewMode: systemShare.SharePreviewMode.DETAIL
   8. }).then(() => {
   9. console.info('ShareController show success.');
   10. }).catch((error: BusinessError) => {
   11. console.error(`ShareController show error. code: ${error.code}, message: ${error.message}`);
   12. });
   ```

   完整示例代码请参见：[samplecode-分享文本](https://gitcode.com/harmonyos_samples/share-kit_-sample-code_-clientdemo_-arkts/blob/master/entry/src/main/ets/scenario/TextScenario.ets)。
