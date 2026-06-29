---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/graphics-accelerate-assetdownload-release
title: 发布资源包下载任务
breadcrumb: 指南 > 图形 > Graphics Accelerate Kit（图形加速服务） > 游戏资源加速服务 > 资源包后台下载 > 发布资源包下载任务
category: harmonyos-guides
scraped_at: 2026-06-01T14:58:03+08:00
doc_updated_at: 2026-05-08
content_hash: sha256:b7458db2c25be1d939891258ec6395cf4fe6b8d0d75ae9042dce584e823315d3
---
在AppGallery Connect支持创建“使用华为CDN”或“使用三方CDN”的游戏资源包下载任务。

## 前提条件

* 已准备好游戏资源包并加密，且自行保证游戏资源包的可用性。资源包支持的格式请参见[上传至华为CDN的资源包文件支持哪些格式类型](<../../../Graphics Accelerate Kit常见问题/游戏资源加速服务/上传至华为CDN的资源包文件支持哪些格式类型/graphics-accelerate-assetdownload-faq-1.md>)。
* 游戏资源包支持使用三方CDN或托管至华为CDN。若使用三方CDN，请提前将资源包上传至三方CDN服务器。若托管至华为CDN，将在AppGallery Connect上传资源包，一个下载任务中的每个资源包大小不超过2GB，所有任务的资源包总大小不超过150GB。

## 进入申请页面

登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)，点击“APP与元服务 ”，在游戏列表中选择游戏后，选择“分发 > 服务 > 资源包后台下载申请”，在页面右侧点击“申请”。

说明

* 若列表中有“审核中”、“预上线”、“已发布”、“任务暂停”中的任一状态任务，将无法点击“申请”，需要终止该任务后才能申请。
* 资源包下载任务的状态说明请参见[下载任务状态说明](graphics-accelerate-assetdownload-release.md#下载任务状态说明)。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/37/v3/crDcE4XLR6-WCoJ5ktLPMA/zh-cn_image_0000002613519207.png?HW-CC-KV=V1&HW-CC-Date=20260601T065803Z&HW-CC-Expire=86400&HW-CC-Sign=1F4DB569E959DE5BB62655FC4271D1BDE418374F0D3EA19AF46EEF8F21ED2DC0)

## 创建下载任务

### 资源包下载方式一：使用三方CDN

说明

已提前将资源包上传至三方CDN服务器。

在“资源包后台下载申请”页面填写资源包信息后，点击“提交申请”，提交资源包下载任务。若暂不提交该任务，点击“保存草稿”，允许继续编辑后再提交申请。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/79/v3/kvvD7e3TSN-Kaopyg3mYNw/zh-cn_image_0000002582959410.png?HW-CC-KV=V1&HW-CC-Date=20260601T065803Z&HW-CC-Expire=86400&HW-CC-Sign=D113DEF3BBC2FAD2474EE249AB94872F89E760AC3D116DE4745F47FF11DD7B7A)

| 配置项 | 是否可选 | 填写说明 |
| --- | --- | --- |
| 下载类型 | 必选 | 请选择下载器，建议根据应用自身是否有下载器进行选择：  - 应用未内置下载器，建议选择“extension系统托管下载”，表示将由华为提供的系统下载器下载游戏资源包。  - 应用已内置下载器，建议选择“extension协同下载”，表示将由应用自身下载器下载游戏资源包。 |
| CDN | 必选 | 选择“使用三方CDN”。 |
| 指定下载时间段 | 可选 | 用户向三方CDN服务器请求下载游戏资源包的时间段。步骤如下：  1. 打开“指定下载时间段”开关。  2. 点击“添加时间段”，指定开始时间和结束时间，最多可支持添加20个时间段，且多个时间段不能重叠。 |
| 包体大小 | 必选 | 填写已上传至三方CDN服务器的资源包大小。 |
| CDN域名白名单 | 必选 | 英文逗号隔开，最多添加20个。 |
| 可下载的端侧最小版本号 | 可选 | 为了提升CDN资源利用率，开发者可以限制下载游戏资源包的游戏版本。  请填写app.json5配置文件中的versionCode字段值。app.json5配置文件介绍请参见[配置文件标签](../../../../../基础入门/开发基础知识/应用配置文件（Stage模型）/app.json5配置文件/app-configuration-file.md#配置文件标签)。  若设备上已安装的游戏版本低于指定的端侧最小版本号，则无法下载游戏资源包。  若未填写端侧最小版本号，所有游戏版本均可下载游戏资源包。 |

### 资源包下载方式二：使用华为CDN

说明

除了支持在AppGallery Connect“页面”方式创建“华为CDN”的资源包下载任务，还支持开发者使用“API”方式创建“华为CDN”的资源包下载任务，详情请参见[API接口](https://developer.huawei.com/consumer/cn/doc/AppGallery-connect-Guides/agcapi-res-pkg-preload-0000002362269981)。

在“资源包后台下载申请”页面填写资源包信息，具体步骤如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ae/v3/14jfdSx4SVeODFII9eliUA/zh-cn_image_0000002583119336.png?HW-CC-KV=V1&HW-CC-Date=20260601T065803Z&HW-CC-Expire=86400&HW-CC-Sign=443960D10609C9F797FE719DD1083EB06BECA4A2666E9D5D913D0DE838D67996)

1. “下载类型”请选择“extension系统托管下载”。
2. “CDN”选择“使用华为CDN”。
3. 设置资源包下载的开始时间和结束时间。要求如下：

   | 要求 | 举例 |
   | --- | --- |
   | 开始时间和结束时间的生效时间均为用户设备的本地时间。 | - |
   | 开始时间和结束时间只能选择到天。 | - 开始时间选择2024年4月2日，则默认开始时间为2024年4月2日0点。  - 结束时间选择2024年4月10日，则默认结束时间为2024年4月10日23点59分。 |
   | 开始时间和结束时间最长间隔为14天。 | - |
   | 资源包下载申请只有华为运营审批通过后，才能正式对外发布，因此请提前1~3天申请资源包下载任务，给华为运营预留时间进行审批。 | 申请资源包下载任务时，开始时间选择2024年4月2日，结束时间选择2024年4月10日。  若华为运营审核通过，正式对外发布的时间为2024年4月5日，则当前资源包下载任务只能从2024年4月5日开始执行。 |
   | 游戏资源包在用户客户端最长保留时间为14天，开始时间需要根据游戏首发或游戏发布更新版本的时间合理安排。 | 申请资源包下载任务时，开始时间选择2024年4月2日，结束时间选择2024年4月10日。  下载任务在2024年4月2日审核通过并对外正式发布，此后符合条件的用户设备就会将资源包下载到设备本地，直到2024年4月10日任务结束。  但您在4月25日才在华为应用市场上架游戏的最新版本，而此时用户设备的游戏资源包已经过了14天的最大保留时间，系统会自动删除设备本地的游戏资源包，从而导致用户下载游戏后无法加载下载的游戏资源包。 |
   | 开始时间设置后如果更改，则结束时间自动清除，需要重新选择。 | - |
   | 如果审核通过的时间已经晚于下载结束时间，则审核通过后任务会直接变为“任务结束”状态。 | - |
4. （可选）填写客户端的最小版本号。

   为了提升CDN资源利用率，开发者可以限制下载游戏资源包的游戏版本。请填写app.json5配置文件中的versionCode字段值。app.json5配置文件介绍请参见[配置文件标签](../../../../../基础入门/开发基础知识/应用配置文件（Stage模型）/app.json5配置文件/app-configuration-file.md#配置文件标签)。

   若设备上已安装的游戏版本低于versionCode，则无法下载游戏资源包。

   若未填写端侧最小版本号，所有游戏版本均可下载游戏资源包。
5. 填写资源包版本号。

   版本号用于跟踪不同资源包的下载任务，版本号要求不超过9位的整数，且必须高于已创建任务的版本号。重新编辑“草稿”、“预上线”、“任务结束”状态的资源包下载任务时，资源包版本号也不能低于已有的版本号。
6. 上传资源包。

   在“上传资源包”栏点击“选择文件”，上传提前准备好的游戏资源包。

   说明

   * 同一个开发者支持上传至华为CDN的资源包总大小不超过150GB，且历史任务的资源包文件最多保留半年。
   * 上传资源包文件的过程中，若提示华为CDN空间已满，开发者应删除历史无用的资源包文件或下载任务。

   资源包上传过程及最终状态分为如下几种：

   | 游戏资源包的文件状态 | 处理说明 |
   | --- | --- |
   | 上传中...进度x% | 等待资源包上传完成，如需停止上传，可以点击“取消上传”。 |
   | 上传失败 | 检查网络是否正常、资源包大小是否超过上限，如无异常，可点击“删除”将游戏资源包删除，并重新上传资源包。 |
   | 扫描中 | 等待游戏资源包扫描完成。 |
   | 扫描不通过，可能存在病毒 | 点击“删除”将游戏资源包删除，并检查包体中是否存在病毒，修复资源包后重新上传。 |
   | 扫描通过 | 表示游戏资源包上传成功。 |
7. （可选）填写hotversion。

   开发者可以通过hotversion版本号指定下一级文件的存储路径。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ec/v3/1oMHzt55SpCcHjxJK6bMUg/zh-cn_image_0000002613639103.png?HW-CC-KV=V1&HW-CC-Date=20260601T065803Z&HW-CC-Expire=86400&HW-CC-Sign=F060DBAFAF42273B102943DBF4E5DBED5CCF086F9A952FFED1EA75B7716F6066)

   例如，资源包版本号为2.1，hotversion为2.1.0，资源包文件的存储路径如下：

   ```
   1. └──appid  10035 // 游戏APP ID
   2. ├──v2.1/ // 资源包版本号
   3. │  ├──v2.1.0/ // hotversion
   4. │  │  ├──button.png?v=20240223 // 资源包文件
   5. │  │  ├──font.ttf?v=20240210 // 资源包文件
   6. │  │  └──font.ttf?v=20240213 // 资源包文件
   7. │  └──v2.1.1/ // hotversion
   8. │     └──font.ttf?v=20240214 // 资源包文件
   9. └──v2.0/
   ```
8. 提交资源包下载任务。

   点击“提交申请”提交资源包下载任务。若暂不提交该任务，点击“保存草稿”，允许继续编辑后再提交申请。

## 提交下载任务

在[创建下载任务](graphics-accelerate-assetdownload-release.md#创建下载任务)时已提交申请，可跳过当前步骤。

在[创建下载任务](graphics-accelerate-assetdownload-release.md#创建下载任务)时保存为草稿，请继续编辑后再提交申请。具体步骤如下：

1. 在任务列表中找到“草稿”状态的任务，点击“操作”列中的“编辑”进入申请详情页。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a5/v3/ER1Shy7MR56QfGqu-AHHyQ/zh-cn_image_0000002613519209.png?HW-CC-KV=V1&HW-CC-Date=20260601T065803Z&HW-CC-Expire=86400&HW-CC-Sign=DF42C8C6177016E5A56915C8BEB89FE568AFA1039F897948541D84D04A7E9EA6)
2. 在申请页填写资源包信息，填写要求请参见[创建下载任务](graphics-accelerate-assetdownload-release.md#创建下载任务)。完成后，点击“提交申请”提交资源包下载任务，当前任务状态变更为“预上线”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/de/v3/PB2wVWdoSfeFjNlcZvbUzw/zh-cn_image_0000002582959412.png?HW-CC-KV=V1&HW-CC-Date=20260601T065803Z&HW-CC-Expire=86400&HW-CC-Sign=2A256AB584E75DC6B5F4AFF844F186779A774114E35D6E5792CAF6E5B7C85660)

## 测试下载功能

正式发布下载任务前， 请在本地测试“预上线”状态的任务是否可以成功下载资源包。

### 打开资源包自动更新开关

请在HarmonyOS 5.1.0及以上版本测试设备的“游戏中心”客户端打开“我的 > 设置 > 服务管理 > 游戏服务”，打开“允许资源包自动更新”开关。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/87/v3/KO1ZvYz_SoCTQtUjqVhQhg/zh-cn_image_0000002583119338.png?HW-CC-KV=V1&HW-CC-Date=20260601T065803Z&HW-CC-Expire=86400&HW-CC-Sign=368F555DAD50AF0C1D0581DFF7BE8B9DC807C13B78463CE25C0419D12BAF22AC "点击放大")

### 配置设备号

1. 输入如下命令行，获取测试设备的设备号。

   ```
   1. hdc shell bm get --udid
   ```

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f3/v3/-Peb-M7mT4O54U-Z8m4Tsg/zh-cn_image_0000002613639105.png?HW-CC-KV=V1&HW-CC-Date=20260601T065803Z&HW-CC-Expire=86400&HW-CC-Sign=51EE09B1A68873AF31707E6527E01BB8E34ED437204BC93EA7719FE61740BCF5)
2. 在AppGallery Connect页面点击“测试设备”后的“编辑”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5b/v3/7VTyr8bIRv6jIVNadWnXRg/zh-cn_image_0000002613519211.png?HW-CC-KV=V1&HW-CC-Date=20260601T065803Z&HW-CC-Expire=86400&HW-CC-Sign=42C87ABEB6CCDE5ABD54ECCF9EC81D9FA535C66F4A1D0DD77C29DD334753A90B)
3. 在输入框中最多添加10台测试设备的设备号，且使用英文逗号（,）间隔开，完成后点击“保存”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ae/v3/Efm7kc10SvGxWSQOQjzSuA/zh-cn_image_0000002582959414.png?HW-CC-KV=V1&HW-CC-Date=20260601T065803Z&HW-CC-Expire=86400&HW-CC-Sign=4E74750A4A63D8B6C15D744B9EA7EEBB3AD2FF59B091BF66BDFD3B876989D2DA)

### 验证方式

1. 如果游戏未安装，则安装游戏。

   ```
   1. // 输入命令行，安装游戏。
   2. // "entry-default-signed.hap"为示例包名，请根据您项目的实际包名替换使用。
   3. hdc install .\entry-default-signed.hap
   ```
2. 如果游戏已安装，则执行模拟设备闲时命令。

   ```
   1. // 输入命令行，模拟设备满足闲时条件。
   2. hdc shell hidumper -s 1904 -a "-s 66272 7800"
   ```
3. 验证以上两个场景是否触发系统后台下载资源包：查看测试设备的通知栏出现下载任务，则系统后台下载资源包功能验证通过。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/38/v3/WdUm9YGAS2evnssC6c5x-Q/zh-cn_image_0000002583119340.png?HW-CC-KV=V1&HW-CC-Date=20260601T065803Z&HW-CC-Expire=86400&HW-CC-Sign=16B225FE6C564DD4ABD8A28135E302D8DA852DBCE7B305FE78126B2F076B8CCB "点击放大")

## 发布下载任务

1. 在任务列表找到“预上线”状态的任务，点击“操作”列中的“发布”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ec/v3/FH_ph0kOQYyuGA3yJHUhOg/zh-cn_image_0000002613639107.png?HW-CC-KV=V1&HW-CC-Date=20260601T065803Z&HW-CC-Expire=86400&HW-CC-Sign=84BCFEE79182C9E92EAE7D7E63660CD0DB80261A7B7356D9C2848FFB16134485)

   在弹出的提示窗中点击“确认”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ad/v3/ItBotlSMTNCJyiNXZgr04Q/zh-cn_image_0000002613519213.png?HW-CC-KV=V1&HW-CC-Date=20260601T065803Z&HW-CC-Expire=86400&HW-CC-Sign=D430ECA274AC17F2F8CF96789860594B07D3660755B959819D012A873F10223F)

   发布该任务后，华为运营人员将在1~3个工作日内完成审批，请耐心等待。

   任务通过审批后，游戏资源包将在指定时间内向满足条件的用户设备进行推送。
2. 若需要终止已发布的任务，可以在任务列表中主动点击“终止”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4/v3/nantWgKyQ9ayfZArfgJxxQ/zh-cn_image_0000002582959416.png?HW-CC-KV=V1&HW-CC-Date=20260601T065803Z&HW-CC-Expire=86400&HW-CC-Sign=58A419CEF87C124A7820B2A54AC08A323BB1F31F8B638BBCF1423EF2EA7F86C7)

   此时，系统将不再对该资源包进行自动下载。对于用户设备上已开始下载的游戏资源包不会立刻删除，而是在下一次启动自动更新时，删除下载时间大于7\*24小时的游戏资源包。

## 下载任务状态说明

| 序号 | 状态 | 说明 |
| --- | --- | --- |
| 1 | 草稿 | 填写信息后保存为草稿后的状态，草稿状态的任务支持“编辑”和“删除”。 |
| 2 | 预上线 | 提交申请后的状态，任务可以在这个状态下进行资源包下载测试。预上线状态的任务支持“发布”和“终止”。 |
| 3 | 审核中 | “预上线”状态的任务点击“发布”后的状态。审核中的任务不支持执行任何操作。 |
| 4 | 审核不通过 | 任务点击“发布”后提交到华为运营人员审核，审核不通过的状态。审核不通过的任务支持重新“编辑”。 |
| 5 | 已发布 | 任务审核通过后任务正式发布的状态，发布中的任务仅支持“终止”。 |
| 6 | 任务结束 | 本次下载任务执行结束或者被华为运营人员终止了任务。 |
| 7 | 任务暂停 | 被华为运营人员暂停了任务。 |
