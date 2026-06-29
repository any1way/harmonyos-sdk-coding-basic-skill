---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/self-verification
title: 开发者自验证
breadcrumb: 指南 > 应用框架 > Core File Kit（文件基础服务） > 应用文件 > 应用数据备份恢复 > 设备升级应用数据迁移适配指导 > 验证应用数据迁移 > 开发者自验证
category: harmonyos-guides
scraped_at: 2026-06-11T14:36:52+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:f0a633644041652267bcf01e22dbe024e8f56d4d040c5ccf8fc375a325665c61
---
## 简介

在开发的过程中，当开发者完成所需[适配流程](../../适配流程/adaptation-process.md)后，可导入提前准备好的APK应用沙箱数据，自验证HarmonyOS应用数据迁移适配结果。

在HarmonyOS应用适配完成并上架到华为应用市场之后，开发者仍需要将终端设备从HarmonyOS升级到HarmonyOS NEXT，[端到端验证](../端到端验证/e2e-verification.md)应用数据迁移结果。

## 开发者自验证流程

### 应用沙箱数据准备

请自行构造APK应用沙箱数据，并将构造好的APK应用沙箱数据按指定格式打包成“{APK包名}.zip”。

说明

在打包‘{APK包名}.zip’文件时，必须使用UTF-8编码格式进行压缩，否则压缩中文命名的文件时，文件名会出现乱码。

| **APK应用沙箱目录** | {APK包名}.zip目录 |
| --- | --- |
| /data/user\_de/{userId}/{APK包名}/ | {APK包名}/de |
| /data/user/{userId}/{APK包名}/ | {APK包名}/ce |
| /data/media/{userId}/Android/data/{APK包名}/ | {APK包名}/A/data |
| /data/media/{userId}/Android/obb/{APK包名}/ | {APK包名}/A/obb |

打包好的“{APK包名}.zip”解压后，要满足包含一个“APK包名”根目录，根目录下包含对应沙箱目录文件夹，文件结构如下。

```
1. ─com.demo.demo
2. ├─A
3. │  ├─data
4. │  └─obb
5. ├─ce
6. └─de
```

1. 将打包好的“{APK包名}.zip”推送到外部存储设备（U盘或者移动硬盘），连接终端设备和外部存储设备。

   说明

   当前终端设备支持识别NTFS格式的外部存储设备，请使用NTFS格式的外部存储设备连接终端设备。
2. 在终端设备中，打开“文件管理”应用，长按选中外部存储设备中的“{APK包名}.zip”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2d/v3/HeBa8vFASd69t4NwQWQj5Q/zh-cn_image_0000002622858115.png?HW-CC-KV=V1&HW-CC-Date=20260611T063651Z&HW-CC-Expire=86400&HW-CC-Sign=3FBDDC7C21E01D90C7A245DD56A5E114540063100161E1D1BA02610563470EAE)

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ee/v3/TywQjrPVR_GFUlJ98DGSJA/zh-cn_image_0000002622698237.png?HW-CC-KV=V1&HW-CC-Date=20260611T063651Z&HW-CC-Expire=86400&HW-CC-Sign=202C30B6CEF6C952F37F3D2DFD22F7DD5F723BB1FD671029A740F723330B6B42)
3. 单击“复制”按钮，将数据复制到文件管理器的“下载”目录下，作为后续自验证的测试数据源。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/27/v3/ia7oKdJIQTqeCkVmKAVi1Q/zh-cn_image_0000002592218676.png?HW-CC-KV=V1&HW-CC-Date=20260611T063651Z&HW-CC-Expire=86400&HW-CC-Sign=272F2D691751C73AB369C9782F901C3299DB06F662F6637F6381C5ECC2EBF617) ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/29/v3/Q-8Ja0NyR4excEbWZ3gesQ/zh-cn_image_0000002592378610.png?HW-CC-KV=V1&HW-CC-Date=20260611T063651Z&HW-CC-Expire=86400&HW-CC-Sign=82C057E3BE3683678F95ECE41E6F0B00A67A32A6DD8E74975E137A81B579B650)

## HarmonyOS NEXT上模拟验证应用数据迁移

在应用沙箱数据准备好之后，开发者需要先完成所需[适配流程](../../适配流程/adaptation-process.md)，再模拟验证应用数据迁移。

1. 安装目标HarmonyOS应用到终端设备。

   注意

   “迁移调试”工具“205.0.0.110”之前的版本，仅支持调试release签名的应用。

   从“205.0.0.110”版本开始，“迁移调试”工具仅支持调试debug签名的应用。请开发者升级到最新版本，并使用debug签名的包验证。

   “迁移调试”工具版本查看方式：**设置**>**应用和元服务**>**MigrateTool**>**版本**
2. 打开迁移调试工具。迁移调试工具图标如下图所示：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ce/v3/IxNXrVdvRViBg6wHl1-ERw/zh-cn_image_0000002622858117.png?HW-CC-KV=V1&HW-CC-Date=20260611T063651Z&HW-CC-Expire=86400&HW-CC-Sign=B1F150304F05CF8BFB7A537B2A14C82F983E45907EE572376910A20666226288)
3. 在“迁移工具”应用的首页，开发者通过单击“选择”按钮进入设备文件管理界面。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a2/v3/TgTCkr-MTcCZhDlbdZ7pOA/zh-cn_image_0000002622698239.png?HW-CC-KV=V1&HW-CC-Date=20260611T063651Z&HW-CC-Expire=86400&HW-CC-Sign=DFB48A7A4BABB306385E4D7DCE00CBD69BD423791D2BCF5AAE41A6C53067FAFB)
4. 在设备文件管理界面，单击“浏览”按钮，进入浏览手机内部存储界面。单击“我的手机”，根据之前导入数据的路径，进入手机存储的相应路径，选择需要导入的APK应用数据zip包。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/70/v3/WSOq0vawS862X-ytufodRQ/zh-cn_image_0000002592218678.png?HW-CC-KV=V1&HW-CC-Date=20260611T063651Z&HW-CC-Expire=86400&HW-CC-Sign=3D93A4E0A613E5595DA196FA91E3318AD8D7333D537E62B1A157E8C5040DB580) ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2d/v3/k49HgOKHQ2udd79YjxBt4A/zh-cn_image_0000002592378612.png?HW-CC-KV=V1&HW-CC-Date=20260611T063651Z&HW-CC-Expire=86400&HW-CC-Sign=A0CF47B68292E158171E54E33ADFF976A2E7C5A2CB828D6B3DE408701942EEB9)
5. 单击需要导入的APK应用数据zip包后，会返回“迁移调试”工具首页，已选择的需要导入的APK应用数据会显示在第一栏中。选择好需要导入的APK应用数据后，单击“请输入应用包名”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/51/v3/RadV4kfMQbGu0T8TNuWW5A/zh-cn_image_0000002622858119.png?HW-CC-KV=V1&HW-CC-Date=20260611T063651Z&HW-CC-Expire=86400&HW-CC-Sign=0EC97430CCBB91EA0F3E92179032AACEFF5A112CEA48410A4C424091A1F153A0)
6. 输入需要验证的目标HarmonyOS应用包名，目标HarmonyOS应用会显示在“迁移调试”工具首页的第二栏中。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/81/v3/jz_5nImwQTKrDgZ0r6o9lQ/zh-cn_image_0000002622698241.png?HW-CC-KV=V1&HW-CC-Date=20260611T063651Z&HW-CC-Expire=86400&HW-CC-Sign=0087D96DCA15FDDB0A027E6DC706F7D4D77B5C70DBBB45F0B93ABB5E88402243)

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e7/v3/j5j0X8a3QeuGmnp-OGhpgg/zh-cn_image_0000002592218680.png?HW-CC-KV=V1&HW-CC-Date=20260611T063651Z&HW-CC-Expire=86400&HW-CC-Sign=3528EC807DE0842098875AFF747002C48D493620E40EA2108AE8BE41966D812F)
7. 选择需要导入的APK数据和目标HarmonyOS应用后，单击“启动迁移”按钮，开始模拟数据迁移，页面切换为数据优化界面，应用数据迁移的进度在数据迁移进度条中显示。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ae/v3/9RaJSPdIRvGz9WgSReXnGg/zh-cn_image_0000002622698241.png?HW-CC-KV=V1&HW-CC-Date=20260611T063651Z&HW-CC-Expire=86400&HW-CC-Sign=6D071CA425AFB22602422F7E39CB8EFB1F696392B8672FC34AF8BBCB96BC3CEC) ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f8/v3/gWTVYYzsTGu1oQthlycRuA/zh-cn_image_0000002592378614.png?HW-CC-KV=V1&HW-CC-Date=20260611T063651Z&HW-CC-Expire=86400&HW-CC-Sign=0988F69086D6F10F668F4CCA052DF7A4F98750D3C6025A71EBA055AE98FE14CC)
8. 应用数据迁移完成之后，数据迁移进度条上方显示“已优化完成”，进度更新为100%。数据迁移成功的情况下，界面中无异常提示。单击“完成”按钮，切换回“迁移调试”工具首页，在下方的“迁移日志”版块中显示详细迁移信息。result字段表示数据迁移结果，costTime字段表示数据迁移时长（单位ms）。

   注意

   **1、此处的数据迁移成功，仅表示“备份恢复框架”接入成功，APK应用的数据成功迁移到“备份恢复框架”需要的指定目录。开发者需要通过从应用的沙箱中获取数据并解析，判断应用适配“备份恢复框架”的结果**。

   **2、单个应用数据迁移执行超过十五分钟，超过设定的单个应用最长数据迁移时间，会导致任务执行失败。开发者需要优化应用BackupExtensionAbility的代码实现，在十五分钟内完成应用数据迁移。**

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/71/v3/xs2VUaavTS2QGwboTH4iZg/zh-cn_image_0000002622858121.png?HW-CC-KV=V1&HW-CC-Date=20260611T063651Z&HW-CC-Expire=86400&HW-CC-Sign=AE84364B6D8A623442CA288146635AA476AD5F0602A98B169A07A9708B9E6793) ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/81/v3/9_wIp_ThQgiXFLiMuvXJMQ/zh-cn_image_0000002622698243.png?HW-CC-KV=V1&HW-CC-Date=20260611T063651Z&HW-CC-Expire=86400&HW-CC-Sign=04182F66A3F576F2F3F5277E359E7B9500070AB05C7625064E6C13F193065995)
9. 数据迁移失败的情况下，应用图标上方的状态显示“优化失败”。单击“完成”按钮，切换回“迁移工具”应用首页，在下方的“迁移日志”版块中显示详细迁移信息。result字段表示数据迁移结果，costTime字段表示数据迁移时长（单位ms）。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8f/v3/2J_LOIMtTwGvW_-yytT3nw/zh-cn_image_0000002592218682.png?HW-CC-KV=V1&HW-CC-Date=20260611T063651Z&HW-CC-Expire=86400&HW-CC-Sign=9AD482091CBD090D32B3928FFA93B51B5555393A61E24C4536D1155AACC4B6D4) ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4e/v3/IjSeYtRETXG6Q6zkumlw6w/zh-cn_image_0000002592378616.png?HW-CC-KV=V1&HW-CC-Date=20260611T063651Z&HW-CC-Expire=86400&HW-CC-Sign=6D18D581CDB195B7E15D57F1B8BE86D2E085F4494D31C2EC91B577B6F8736C5F)
