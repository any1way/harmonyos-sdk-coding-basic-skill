---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-emulator-customize-screen-configuration
title: 自定义屏幕配置
breadcrumb: 指南 > 编写与调试应用 > 使用模拟器运行应用 > 修改模拟器 > 自定义屏幕配置
category: harmonyos-guides
scraped_at: 2026-06-11T15:28:48+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:c30b845cc08300aab102823db54de1eb64f71d4d0bac9cedfbc91070668e60e6
---
从DevEco Studio 6.0.0 Beta1版本开始，模拟器支持自定义屏幕配置，支持在创建新的模拟器时自定义，具体请参考[创建模拟器](../../管理模拟器/创建模拟器/ide-emulator-create.md)，或者对已创建的模拟器进行修改，具体参考以下步骤。

## 使用约束

* phone类型的模拟器支持自定义屏幕配置。
* 从DevEco Studio 6.0.1 Beta1版本开始，新增foldable、tablet和2in1类型的模拟器支持自定义屏幕配置。

## 操作步骤

1. 在模拟器关闭状态下，点击模拟器的修改按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c0/v3/gxkGG2_aQNyCz4WgaSBjlg/zh-cn_image_0000002571385674.png?HW-CC-KV=V1&HW-CC-Date=20260611T072847Z&HW-CC-Expire=86400&HW-CC-Sign=B9CE79772F4FB8EB54D549FB28F944EC23930BE3FCF620EA0239EBB84CAD22E4)，进入Virtual Device Configure界面。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/df/v3/cEJuYY7URN6oSyMLx9k2Ew/zh-cn_image_0000002602184839.png?HW-CC-KV=V1&HW-CC-Date=20260611T072847Z&HW-CC-Expire=86400&HW-CC-Sign=25DF751B663E972C92C934F9730C6ADCDCCC2D15B80A36B8EBFBED9801A224D1 "点击放大")
2. 点击**Customize**按钮，可以自定义设备的屏幕尺寸、分辨率和DPI配置，取值范围参考界面提示。
   * **Screen size：**屏幕的对角线长度，单位为inch。
   * **Resolution**：分辨率，宽度和高度，单位为px。
   * **DPI**：像素密度，DPI 越高，UI组件占用的像素点越多，从而提供更精细的显示效果。

   确认所有参数后，点击**Finish**完成修改，并保存为新的预置配置。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/22/v3/FQw-LhlhQ0Cyjmy786HQEQ/zh-cn_image_0000002602064789.png?HW-CC-KV=V1&HW-CC-Date=20260611T072847Z&HW-CC-Expire=86400&HW-CC-Sign=669AEDEE0E86A347EA35AFE35C979003193D869ADBCFEA70189D6D0597942141 "点击放大")
