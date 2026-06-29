---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/agc-harmonyos-clouddev-sync
title: （可选）同步云端代码至DevEco Studio工程
breadcrumb: 指南 > 开发环境搭建 > 工程创建 > 模块管理 > 端云一体化开发 > 开发端云工程 > （可选）同步云端代码至DevEco Studio工程
category: harmonyos-guides
scraped_at: 2026-06-01T15:18:32+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:270cffc89addc89d1fbd40898382e105173ba3babdecc84b4684f4d73700885a
---
DevEco Studio还支持您将AGC云端当前项目下的代码同步至本地工程，包括之前从本地部署到AGC云端的代码、以及在AGC云端编写的代码，以保证云端和本地的版本一致性，方便您的日常开发。

云端代码同步目前支持以下模式：[仅同步云函数/云对象](agc-harmonyos-clouddev-sync.md#section588213529814)、[仅同步云数据库](agc-harmonyos-clouddev-sync.md#section474014335350)、[一键同步云侧代码](agc-harmonyos-clouddev-sync.md#section1198316575339)。

## 同步云函数/云对象

说明

对于使用DevEco Studio 4.1 Canary 2之前的版本部署的函数，同步下来的是JavaScript代码。

### 同步单个云函数/云对象

云函数/云对象部署到AGC云端后，如在云端又进行了新改动，您可再将云端的云函数/云对象同步到本地工程。云函数/云对象的同步方式一致，下文以云对象为例进行说明。

1. 右击云对象目录，选择“Sync '*云对象名*'”。下文以云对象“id-generator”为例。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f/v3/o0V9j3YQTgOYslYwaPgz3g/zh-cn_image_0000002214704461.png?HW-CC-KV=V1&HW-CC-Date=20260601T071832Z&HW-CC-Expire=86400&HW-CC-Sign=56BB04986207AD4CECE48880323A4CBE503049E2EB02A0DCE16522720B2F29DE)
2. 在确认弹框中点击“Overwrite”，AGC云端的云对象“id-generator”将覆盖更新本地云对象“id-generator”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0a/v3/VGIq1dX3Sd2ku-VzX7Bh_w/zh-cn_image_0000002214704477.png?HW-CC-KV=V1&HW-CC-Date=20260601T071832Z&HW-CC-Expire=86400&HW-CC-Sign=F0A0BE09BDF937B06BCAC22E4ACF9E232A8B0E0C2979A706C4F2B400F58A9B97)
3. 等待同步完成，“cloudfunctions”目录下将生成从云端同步下来的云对象“id-generator”，同时将本地原云对象“id-generator”备份在同路径下。

   说明

   后续如执行部署或调试，DevEco Studio会自动跳过备份数据。但出于精简包的考虑，建议您在对比代码差异后，及时将无用的备份数据删除。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/73/v3/gWh5eNNgQtC3mUKERgKcew/zh-cn_image_0000002179498228.png?HW-CC-KV=V1&HW-CC-Date=20260601T071832Z&HW-CC-Expire=86400&HW-CC-Sign=7757B2C8D0C96B0EC7573A70054C9946C6BCCC2D95CA479984BEBA60E281F8F7)

### 批量同步云函数/云对象

批量同步云函数/云对象即将AGC云端当前项目下的所有云函数/云对象同步至本地工程。

1. 右击“cloudfunctions”目录，选择“Sync Cloud Functions”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8b/v3/Y7QNjDmvTNKztVZw9sj8TQ/zh-cn_image_0000002179338512.png?HW-CC-KV=V1&HW-CC-Date=20260601T071832Z&HW-CC-Expire=86400&HW-CC-Sign=3116E16E0A911FF014B6AFD5B6A3B052BD505C1773B08844813340A3956E30FE)
2. 弹窗提示您本地工程下存在同名云函数/云对象。
   * 选择“Skip”，同步时将跳过本地同名云函数/云对象。
   * 选择“Overwrite”，AGC云端的云函数/云对象将覆盖更新本地同名云函数/云对象。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b6/v3/_YVqip-ZSciaY9RGY9jxUw/zh-cn_image_0000002214704441.png?HW-CC-KV=V1&HW-CC-Date=20260601T071832Z&HW-CC-Expire=86400&HW-CC-Sign=175A2D3AEA5D70DE0C528B732F2C82C8A06B4AFDB4915FE7BBDC0C6BEFB9C8BE)
3. 如选择“Skip”，等待同步完成后，“cloudfunctions”目录下将生成从云端同步下来的本项目下所有云函数/云对象，本地已存在的不同步。

   如下图，“cloudfunctions”目录下新增了云端同步下来的“test-cloud-function”，上图中本地已存在的云函数/云对象未被覆盖更新。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f6/v3/yx1CdYukTgyvpVWsd2VsZw/zh-cn_image_0000002214704485.png?HW-CC-KV=V1&HW-CC-Date=20260601T071832Z&HW-CC-Expire=86400&HW-CC-Sign=8920A3CFB2C7A8E10D2043132BED323CB85276B5CAEC1E77E089EF3B4A72A681)
4. 如选择“Overwrite”，等待同步完成后，“cloudfunctions”目录下将生成从云端同步下来的本项目下所有云函数/云对象；本地同名云函数/云对象也被覆盖更新，同时更新前的原云函数/云对象会备份在同路径下。

   如下图，“cloudfunctions”目录下新增了云端同步下来的“test-cloud-function”，本地已存在的几个云函数/云对象也被覆盖更新，并且均生成了备份文件“xxxx-*备份时间*.backup”。

   说明

   后续如执行部署或调试，DevEco Studio会自动跳过备份数据。但出于精简包的考虑，建议您在对比代码差异后，及时将无用的备份数据删除。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a3/v3/fFlIOVSDQPawkXE6Nu52JA/zh-cn_image_0000002179338508.png?HW-CC-KV=V1&HW-CC-Date=20260601T071832Z&HW-CC-Expire=86400&HW-CC-Sign=3CC3D4E50D3959F00CA44F3615A3DDE9977D77CA3800E8EEF7284194CDAFF59B)

## 同步云数据库

说明

目前仅支持同步对象类型。

### 同步单个对象类型

对象类型部署到AGC云端后，如又发生了新改动，您可再将云端的对象类型同步到本地。

1. 右击对象类型JSON文件（以“objecttype1.json”为例），选择“Sync 'objecttype1.json'”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b5/v3/YQ_wzkLjQMuhWqLo8l_acw/zh-cn_image_0000002179498216.png?HW-CC-KV=V1&HW-CC-Date=20260601T071832Z&HW-CC-Expire=86400&HW-CC-Sign=2C62EB3AD0C9BE3204ECE43D67BD9497CD0ED6C4A4CFA3AFA21F2464553E5BCE)
2. 在确认弹框中点击“Overwrite”，AGC云端的对象类型“objecttype1.json”将覆盖更新本地对象类型“objecttype1.json”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b3/v3/oa02_sr2TJKH2Q2nghLz3A/zh-cn_image_0000002214704465.png?HW-CC-KV=V1&HW-CC-Date=20260601T071832Z&HW-CC-Expire=86400&HW-CC-Sign=89A1DF282DAA5718040E0523EAD22484E29FBFA0D1840A413602FC5AFA8F86C1)
3. 等待同步完成，“objecttype”目录下将生成从云端同步下来的对象类型“objecttype1.json”。
   * 如果云端和本地的同名对象类型内容存在差异，则还会将本地原对象类型备份在同路径下。
   * 如果云端和本地的同名对象类型内容完全一致，则不生成备份。

   说明

   后续如执行部署，DevEco Studio会自动跳过备份数据。但出于精简包的考虑，建议您在对比代码差异后，及时将无用的备份数据删除。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9a/v3/qoZLvOgqS86cU6OBgd1xjg/zh-cn_image_0000002214704445.png?HW-CC-KV=V1&HW-CC-Date=20260601T071832Z&HW-CC-Expire=86400&HW-CC-Sign=EE6D40E8B3B874199BA0F37E3FEAD39407351CBC58E2E53149716F2B12FFA896)

### 批量同步对象类型

您可以将AGC云端当前项目下所有的对象类型一键同步至本地。

1. 右击“objecttype”目录，选择“Sync Object Type”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9c/v3/z3RRzaiqR-e2CHaAIayirQ/zh-cn_image_0000002179338532.png?HW-CC-KV=V1&HW-CC-Date=20260601T071832Z&HW-CC-Expire=86400&HW-CC-Sign=4F4438348FECCA447040F07109EC5ECE9278AEC20D1620425A4E33550265570C)

2. 弹窗提示您本地工程下已存在同名对象类型，如下图“Post.json”与“objecttype1.json”。
   * 选择“Skip”，同步时将跳过本地同名对象类型。
   * 选择“Overwrite”，AGC云端的对象类型将覆盖更新本地同名对象类型。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/48/v3/tGY3_dGpRcCtrSLqBhfQsg/zh-cn_image_0000002179498208.png?HW-CC-KV=V1&HW-CC-Date=20260601T071832Z&HW-CC-Expire=86400&HW-CC-Sign=AFBFFEA0E7E7BF6F66C63BCD6AB3A4C4DE36F1BDAC77C22C1641FFD5A65F4778)
3. 如选择“Skip”，等待同步完成后，“objecttype”目录下将生成从云端同步下来的本项目下所有对象类型，本地已存在的不同步。

   如下图，“objecttype”目录下新增了云端同步下来的“test\_object.json”，本地已存在的“Post.json”与“objecttype1.json”未被覆盖更新。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ab/v3/FULiBaYKQ3qYsTjrWY02jA/zh-cn_image_0000002179498196.png?HW-CC-KV=V1&HW-CC-Date=20260601T071832Z&HW-CC-Expire=86400&HW-CC-Sign=FC5B91FC29D959B5EBB9FEA1473DF7439FFDF328C584DF9A5210C5CAF6703C70)
4. 如选择“Overwrite”，等待同步完成后，“objecttype”目录下将生成从云端同步下来的所有对象类型，本地已存在的对象类型也被覆盖更新。
   * 如果云端和本地的同名对象类型内容存在差异，则还会将本地原对象类型备份在同路径下。
   * 如果云端和本地的同名对象类型内容完全一致，则不生成备份。

   如下图，“objecttype”目录下生成了“test\_object.json”、“Post.json”与“objecttype1.json”三个对象类型文件，其中：“test\_object.json”为从云端新同步下来的对象类型；“objecttype1.json”本地已存在且与云端内容一致，不生成备份；“Post.json”本地已存在但与云端内容存在差异，因此被覆盖更新，同时原“Post.json”备份为“Post.json-*备份时间*.backup”。

   说明

   后续如执行部署，DevEco Studio会自动跳过备份数据。但出于精简包的考虑，建议您在对比代码差异后，及时将无用的备份数据删除。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d1/v3/1d3VfnisS9yCC5L8INRrKA/zh-cn_image_0000002214704489.png?HW-CC-KV=V1&HW-CC-Date=20260601T071832Z&HW-CC-Expire=86400&HW-CC-Sign=97C5DB8073B383956634AD09DFC55551D86B5FFDB06EEDAB061965108432493B)

## 一键同步云侧代码

说明

对于使用DevEco Studio 4.1 Canary 2之前的版本部署的函数，同步下来的是JavaScript代码。

1. 右击云开发工程（“CloudProgram”），选择“Sync Cloud Program”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/96/v3/0iHeK7BTQDWfhJk19UK8BQ/zh-cn_image_0000002214858849.png?HW-CC-KV=V1&HW-CC-Date=20260601T071832Z&HW-CC-Expire=86400&HW-CC-Sign=86A595E60E7DF2E9D9484C9619AC21C5DCADC002FE64924B2300445CDF9E1002)
2. 弹窗提示您本地工程下已存在同名对象类型/云函数/云对象。
   * 选择“Skip”，同步时将跳过本地同名对象类型/云函数/云对象。
   * 选择“Overwrite”，AGC云端的对象类型/云函数/云对象将覆盖更新本地同名对象类型/云函数/云对象。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/45/v3/hKpx9j32QMaAu0qtwbbiIg/zh-cn_image_0000002214858861.png?HW-CC-KV=V1&HW-CC-Date=20260601T071832Z&HW-CC-Expire=86400&HW-CC-Sign=378ADF0378D645769BD175A0BA8382337A13BC1114A3A659EB2047C77BEED019)
3. 如选择“Skip”，等待同步完成后，“objecttype”目录下将生成从云端同步下来的本项目下所有对象类型，“cloudfunctions”目录下将生成从云端同步下来的本项目下所有云函数/云对象，本地已存在的云函数/云对象/对象类型均不同步。

   如下图：

   * “objecttype”目录下新增了云端同步下来的“test\_object.json”，本地已存在的“Post.json”与“objecttype1.json”未被覆盖更新。
   * “cloudfunctions”目录下生成了从云端同步下来的“test-cloud-function”，本地已存在的“id-generator”、“my-cloud-function”与“my-cloud-object”未被覆盖更新。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f9/v3/L38wmwBhQ6SU1vpFjJ7IBQ/zh-cn_image_0000002179498236.png?HW-CC-KV=V1&HW-CC-Date=20260601T071832Z&HW-CC-Expire=86400&HW-CC-Sign=C05C40FD2AFADE4AE5BF7D0E0B56C6B01D1359A6DCCE27DAE3FF8EFA5BDF0DB0)
4. 如选择“Overwrite”，等待同步完成后，“objecttype”目录下将生成从云端同步下来的本项目下所有对象类型，“cloudfunctions”目录下将生成从云端同步下来的本项目下所有云函数/云对象，本地已存在的云函数/云对象/对象类型也被覆盖更新。
   * 如果云端和本地的同名对象类型内容存在差异，则还会将本地原对象类型备份在同路径下。
   * 如果云端和本地的同名对象类型内容完全一致，则不生成备份。
   * 无论云端和本地的同名云函数/云对象代码是否一致，均会将本地原云函数/云对象备份在同路径下。

   如下图：

   * “objecttype”目录下生成了“test \_object.json”、“Post.json”与“objecttype1.json”三个对象类型文件，其中：“test \_object.json”为从云端新同步下来的对象类型；“Post.json”本地已存在且与云端内容一致，不生成备份；“objecttype1.json”本地已存在但与云端内容存在差异，因此被覆盖更新，同时原“objecttype1.json”备份为“objecttype1.json-*备份时间*.backup”。
   * “cloudfunctions”目录下生成了从云端同步下来的“test-cloud-function”，本地已存在的“id-generator”、“my-cloud-function”与“my-cloud-object”也被覆盖更新，并且均生成了备份文件“xxxx-*备份时间*.backup”。

     说明

     后续如执行部署或调试，DevEco Studio会自动跳过备份数据。但出于精简包的考虑，建议您在对比代码差异后，及时将无用的备份数据删除。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4a/v3/nNv5XeAGRdOao8J2sgsudQ/zh-cn_image_0000002179338516.png?HW-CC-KV=V1&HW-CC-Date=20260601T071832Z&HW-CC-Expire=86400&HW-CC-Sign=3508F422E795B0349E4492DACA569460EB4C0E0B1AE0BB3C4AC999A7A0F411D3)
