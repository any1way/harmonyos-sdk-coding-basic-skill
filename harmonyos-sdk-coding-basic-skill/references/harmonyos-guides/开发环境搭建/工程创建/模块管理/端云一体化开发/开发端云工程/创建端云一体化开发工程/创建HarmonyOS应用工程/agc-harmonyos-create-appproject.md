---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/agc-harmonyos-create-appproject
title: 创建HarmonyOS应用工程
breadcrumb: 指南 > 开发环境搭建 > 工程创建 > 模块管理 > 端云一体化开发 > 开发端云工程 > 创建端云一体化开发工程 > 创建HarmonyOS应用工程
category: harmonyos-guides
scraped_at: 2026-06-01T15:18:14+08:00
doc_updated_at: 2026-05-12
content_hash: sha256:582ae6afa3c1ef15d1d556f74f403d4390f5c61ef9b95b944402aab0d518f8f7
---
## 新建工程

### 前提条件

* 您已完成[开发准备工作](../../../开发准备/agc-harmonyos-clouddev-prerequisite.md)。
* 您已使用[已实名认证](../../../开发准备/注册华为开发者账号并实名认证/agc-harmonyos-clouddev-account.md)、且注册地为中国境内（香港特别行政区、澳门特别行政区、中国台湾除外）的华为开发者账号登录DevEco Studio。
* 请确保您的华为开发者账号无欠款，账户欠费将导致云存储服务开通失败。

### 选择模板

1. 选择以下任一种方式，打开工程创建向导界面。
   * 如果当前未打开任何工程，可以在DevEco Studio的欢迎页点击“Create Project”开始创建一个新工程。
   * 如果已经打开了工程，可以在菜单栏选择“File > New > Create Project”来创建一个新工程。
2. 在“Application”页签，选择合适的云开发模板，然后点击“Next”。

   说明

   当前仅支持通用云开发模板（[CloudDev]Empty Ability）。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bf/v3/YiA8UUL2SvarxJ-B-5epsw/zh-cn_image_0000002462973802.png?HW-CC-KV=V1&HW-CC-Date=20260601T071815Z&HW-CC-Expire=86400&HW-CC-Sign=7C3D98B8A3692E360CEC2D7EC1371EA7A18A66E7A417C870678A49D5C56870DC)

### 配置工程信息

1. 在工程配置界面，配置工程的基本信息。

   其中，Device type和Enable CloudDev参数不可更改，其他参数请参考[创建一个新的工程](../../../../../创建一个新的工程/ide-create-new-project.md#section181328285169)内对应的指导进行配置。

   | 参数 | 说明 |
   | --- | --- |
   | Device type | 该工程模板支持的设备类型，目前仅支持手机设备。 |
   | Enable CloudDev | 是否启用云开发。云开发模板默认启用且无法更改。 |

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fb/v3/7PbD9uwESWm__snvfFUQow/zh-cn_image_0000002547465643.png?HW-CC-KV=V1&HW-CC-Date=20260601T071815Z&HW-CC-Expire=86400&HW-CC-Sign=624104AA852C8A857DDEA4620A9F5F6E9CE2B36C2BD020E8A70B47D95C237B1B)

2. 点击“Next”，开始关联云开发资源。

### 关联云开发资源

为工程关联云开发所需的资源，即将您账号团队在AGC创建的同包名应用关联到当前工程。具体操作如下：

1. （可选）如您尚未登录DevEco Studio，点击“Sign In”，在弹出的账号登录页面，使用[已实名认证](../../../开发准备/注册华为开发者账号并实名认证/agc-harmonyos-clouddev-account.md)的华为开发者账号完成登录。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/36/v3/FT53l2T-TDeQGsUO2GLA8w/zh-cn_image_0000002214858793.png?HW-CC-KV=V1&HW-CC-Date=20260601T071815Z&HW-CC-Expire=86400&HW-CC-Sign=FA425F527E9C53F65D05FDA03EAC818C930AEE50722986075F4CBE35207D3FF3)

   登录成功后，界面将展示账号昵称。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/59/v3/F_ulY8b1SlSYQ6OODeN1nA/zh-cn_image_0000002179338404.png?HW-CC-KV=V1&HW-CC-Date=20260601T071815Z&HW-CC-Expire=86400&HW-CC-Sign=9D0A68D879BFE257BD700A0D2FB186C71191FF5D942F48F26E1ACC93DBF4321D)
2. 点击“Team”下拉框，选择开发团队。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/46/v3/_m7Bpo2rTNOHxzlI_Wq2dg/zh-cn_image_0000002500639597.png?HW-CC-KV=V1&HW-CC-Date=20260601T071815Z&HW-CC-Expire=86400&HW-CC-Sign=4F93AD5798670576E93C2B146558B043395BFF4AEA69126973DC46A4C315D612)
3. 关联应用。

   选中团队后，系统根据工程Bundle name在该团队中自动查询AGC上的同包名应用。

   * 如查询到应用，选中该应用，点击“Finish”即可。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7/v3/MotRIVt_TfKvrAyWEvg3IQ/zh-cn_image_0000002214704349.png?HW-CC-KV=V1&HW-CC-Date=20260601T071815Z&HW-CC-Expire=86400&HW-CC-Sign=83B7FD391AECEC361D42505B4ED491FC49EDA03AE2F56E39FD8792D6EEBD8B3B)
   * 如查询到的应用尚未关联任何项目（即为游离应用），则无法选中。请先[将游离应用添加到AGC项目下](agc-harmonyos-create-appproject.md#section152521927193013)。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ae/v3/9BKCVwE1QeWfoSjiI4UNkA/zh-cn_image_0000002179498144.png?HW-CC-KV=V1&HW-CC-Date=20260601T071815Z&HW-CC-Expire=86400&HW-CC-Sign=3C71AB892FE88511CED297CDE5FD7127BE705297854C82FA2E1B330F4685D8B3)
   * 如果查询到的应用所属项目尚未启用数据处理位置，请点击界面提示内的“AppGallery Connect”[设置数据处理位置](https://developer.huawei.com/consumer/cn/doc/app/agc-help-datalocation-0000001160439813)。设置完成后返回DevEco Studio界面，点击Bundle name后的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/53/v3/Yz1QpC67S5St6S_Mje3Hww/zh-cn_image_0000002495893905.png?HW-CC-KV=V1&HW-CC-Date=20260601T071815Z&HW-CC-Expire=86400&HW-CC-Sign=40480C3B610C6C386FAF713021EA6DE7367607CEC5FA08DE28D9D05056ABCA6E)刷新当前APP ID列表，即可看到设置的数据处理位置。

     注意

     + 由于云开发目前仅支持中国境内（香港特别行政区、澳门特别行政区、中国台湾除外），请确保项目启用的数据处理位置包含“中国”。
     + 无论项目启用的默认数据处理位置为哪个站点，后续开发的云服务资源都将部署在“中国”站点。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a7/v3/LjLH8RnERhmRwGrAnoJp6Q/zh-cn_image_0000002495893753.png?HW-CC-KV=V1&HW-CC-Date=20260601T071815Z&HW-CC-Expire=86400&HW-CC-Sign=E8C070E56E5AAA0C47ED3430144D499D2E86FA8BA5FFDAEC6B0AC0A2BDD05C79)
   * 如查询到应用但出现如下提示，表明查询到的应用类型为元服务，与当前工程类型不一致。请修改以确保当前工程与AGC上同包名应用均为HarmonyOS应用类型。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8a/v3/OnJWJKTwRBic3PQ5_HHnAA/zh-cn_image_0000002462815550.png?HW-CC-KV=V1&HW-CC-Date=20260601T071815Z&HW-CC-Expire=86400&HW-CC-Sign=C2E3A8138D8FD7DB676276D5929D5A2D97B16799DB1A24C2DCE0CAA726B1B720)
   * 如在当前团队中未查询到同包名应用，请先确认填写的包名是否有误。
     + 如包名有误，点击界面提示中的“go back”返回工程信息配置界面进行修改。
     + 如包名无误，则表明当前团队尚未在AGC控制台创建与当前工程包名相同的应用。您可点击界面提示中的“AppGallery Connect”，[前往AGC控制台进行补充创建](agc-harmonyos-create-appproject.md#section397317130308)。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/68/v3/75-n5_RzSo-vtVRbHZ27xA/zh-cn_image_0000002214858765.png?HW-CC-KV=V1&HW-CC-Date=20260601T071815Z&HW-CC-Expire=86400&HW-CC-Sign=A1CDCE7CA5433AA174411AF1CA800B93EEA33A979F3615091AF1F28C1B447827)

     完成以上操作后，DevEco Studio即可获取到同包名应用信息。选中应用后，点击“Finish”。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ca/v3/x2MgueDNTJ2WKnly72a2bg/zh-cn_image_0000002214858801.png?HW-CC-KV=V1&HW-CC-Date=20260601T071815Z&HW-CC-Expire=86400&HW-CC-Sign=4738523D5034B44F34AA74633444B656E76A6AEF99CD9E4D44192B00F075A278)
4. 如您所属的团队尚未签署云开发相关协议，点击协议链接仔细阅读协议内容后，勾选同意协议，点击“Finish”。

   说明

   只有账号持有者和法务角色才有权限签署协议。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/47/v3/1LvbKWobRO--sMcp73iAxA/zh-cn_image_0000002179498108.png?HW-CC-KV=V1&HW-CC-Date=20260601T071815Z&HW-CC-Expire=86400&HW-CC-Sign=BF81225BADB830EF48A3508C23938215DB81E011BE08B85AED0A0CBFF61B128B)
5. 进入主开发界面，DevEco Studio执行工程同步操作，端侧工程会自动执行“ohpm install”，云侧工程会自动执行“npm install”，以分别下载端侧和云侧依赖。

   说明

   若云侧执行“npm install”失败，请排查是否尚未[配置NPM代理](../../../../../../../编写与调试应用/附录/配置代理/ide-environment-config.md#section197296441787)。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3b/v3/7MpuZVt6Tn6c1xNPDhROPA/zh-cn_image_0000002179498148.png?HW-CC-KV=V1&HW-CC-Date=20260601T071815Z&HW-CC-Expire=86400&HW-CC-Sign=8FA589A594C1D69B8AC99F822860787BC5C7293628E20C581813CB58CDAF8C4E)
6. 在主开发界面，可查看刚刚新建的工程。关于工程的详细目录结构介绍，请参见[端云一体化开发工程目录结构](agc-harmonyos-create-appproject.md#section20250910164411)。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c8/v3/rMgoI5lbRJSCI6jQzv5CZw/zh-cn_image_0000002214704397.png?HW-CC-KV=V1&HW-CC-Date=20260601T071815Z&HW-CC-Expire=86400&HW-CC-Sign=EA70690F26DE0BF796C80E6C0EE8C21128BBF078698DBC0DEA2BF59675666845)

## 工程初始化配置

当您成功创建工程并关联云开发资源后，DevEco Studio会为您的工程自动执行一些初始化配置。

### 自动开通云开发服务

DevEco Studio为工程关联的项目自动开通云函数、云数据库、云存储等云开发服务，您可在“Notifications”窗口查看服务开通状态。

说明

* 如服务开通失败，您可通过[CloudDev云开发管理面板](../../../（可选）通过CloudDev面板获取云开发资源支持/agc-harmonyos-clouddev-console.md)快捷进入AGC控制台进行手动开通。
* 如云存储服务自动开通与手动开通均失败，可能是账户欠费导致。请您[检查账户是否余额不足](https://developer.huawei.com/consumer/cn/doc/AppGallery-connect-Guides/agc-account-bill-0000001200817917#section813072912208)，[补齐欠款](https://developer.huawei.com/consumer/cn/doc/AppGallery-connect-Guides/agc-account-recharge-0000001126625360)后再前往AGC控制台进行手动开通。

## 端云一体化开发工程目录结构

端云一体化开发工程主要包含端开发工程（Application）与云开发工程（CloudProgram）。

### 端开发工程（Application）

端开发工程主要用于开发应用端侧的业务代码，使用通用云开发模板创建的端开发工程目录结构如下图所示。“Application/cloud\_objects”模块用于存放云对象的端侧调用接口类，“src/main/ets/pages”目录下包含了云存储、云数据库和云函数页面，其他目录文件介绍请参见[工程目录结构](../../../../../工程目录结构介绍/ide-project-structure.md)。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/77/v3/PWodrGjbTIW5vxuNKIjBGQ/zh-cn_image_0000002214858825.png?HW-CC-KV=V1&HW-CC-Date=20260601T071815Z&HW-CC-Expire=86400&HW-CC-Sign=963EAA2A8EEC72E0054D925F4388753F53D31E8F5339E35BEA648EA3ACE89E7A)

### 云开发工程（CloudProgram）

在云开发工程中，您可为您的应用开发云端代码，包括云函数和云数据库服务代码。使用通用云开发模板创建的云开发工程目录结构如下图所示。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e5/v3/ktH1I7rISriBc2QuSjeRhg/zh-cn_image_0000002279845320.png?HW-CC-KV=V1&HW-CC-Date=20260601T071815Z&HW-CC-Expire=86400&HW-CC-Sign=7CF649D8651D489A938D2B16D75F5FD47A99D4E6D68F164897752BA72577E3D4)

* clouddb：云数据库目录，包含数据条目目录（dataentry）和对象类型目录（objecttype）。
  + dataentry：用于存放数据条目文件。

    该目录下一般会根据您选择的云开发模板预置数据条目示例文件。在通用云开发模板工程中，该目录下会预置名为“d\_Post.json”的数据条目示例文件，内含两条示例数据。您可按需使用、修改或删除。

    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/47/v3/P89GCSjwTrW1l45Wfj0WPw/zh-cn_image_0000002314788585.png?HW-CC-KV=V1&HW-CC-Date=20260601T071815Z&HW-CC-Expire=86400&HW-CC-Sign=728B8A662539FDEA8B09097A96742DD94DDF130F51B9F6E19AE1991CDD1467ED)
  + objecttype：用于存放对象类型文件。

    该目录下一般会根据您选择的云开发模板预置对象类型示例文件。在通用云开发模板工程中，该目录下会预置名为“Post.json”的对象类型示例文件，内含对象类型“Post”的权限、索引、字段名称和字段值等。您可按需使用、修改或删除。

    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/eb/v3/WxT3KigWScynF4ptu-reFA/zh-cn_image_0000002179498164.png?HW-CC-KV=V1&HW-CC-Date=20260601T071815Z&HW-CC-Expire=86400&HW-CC-Sign=0E25095ADB37BDDE704D80839F7E9D4606675585404EB7719F3B8A127E140AA1)
  + db-config.json：模块配置文件，主要包含云数据库工程的配置信息，如默认存储区名称、默认数据处理位置。
* cloudfunctions：云函数目录，包含各个云函数/云对象子目录。每个子目录下包含了云函数/云对象的配置文件、入口文件、依赖文件等。

  该目录下一般会根据您选择的云开发模板预置示例函数。通用云开发模板工程下预置了一个用于生成UUID的示例云对象“id-generator”，您可按需使用、修改或删除。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2c/v3/ZsxzsYu4Q3erqKcaOsQHWA/zh-cn_image_0000002179498100.png?HW-CC-KV=V1&HW-CC-Date=20260601T071815Z&HW-CC-Expire=86400&HW-CC-Sign=6DBD26C87E7D7DF11B0766E9BCC77035149EC8715513599D41A0C8EDE73820DA)
* node\_modules：工程同步时执行“npm install”生成，包含“typescript”和“@types/node”公共依赖。
* cloud-config.json：云开发工程配置文件，包含应用名称与ID、项目名称与ID、启用的数据处理位置、支持的设备类型等。
* package.json：定义了“typescript”和“@types/node”公共依赖。
* package-lock.json：工程同步时执行“npm install”生成，记录当前状态下实际安装的各个npm package的具体来源和版本号。

## （可选）AGC应用管理

### 从DevEco Studio补充创建同包名应用

如创建工程时，发现尚未在AGC控制台创建与工程包名相同的应用，可进行补充创建。

1. 点击界面提示内的“AppGallery Connect”，浏览器打开AGC控制台页面。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/41/v3/NQom8UiATzGG6APrmEjrog/zh-cn_image_0000002214858733.png?HW-CC-KV=V1&HW-CC-Date=20260601T071815Z&HW-CC-Expire=86400&HW-CC-Sign=E129B1B7C20FF2F3DF2C555CBCE51F419A86376994B6073D4E78E994902F1204)
2. 在“应用开发基础信息”页面，填写待创建的应用信息，完成后点击“下一步”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/33/v3/TMg6ajZTQZ6Ugh_KBjLs3w/zh-cn_image_0000002312627449.png?HW-CC-KV=V1&HW-CC-Date=20260601T071815Z&HW-CC-Expire=86400&HW-CC-Sign=F3E63C190434ED50ECA661427FDB958C65455E18C377269A5839ED19F4147AC8)

   | 参数 | 说明 |
   | --- | --- |
   | 应用类型 | 创建的HarmonyOS应用形态，默认与您本地工程类型保持一致，不可更改。 |
   | 应用名称 | 应用在华为应用市场详情页展示的名称。 |
   | 应用包名 | 从DevEco Studio中带入自动填充，且不可更改。 |
   | 应用分类 | 请选择普通应用或游戏类应用。  说明  应用分类设置后不支持修改，请谨慎选择。 |
3. 进入“所属项目信息”页面，为应用选择所属的项目后点击“下一步”。
   * 如需将应用添加到已有项目，点击下拉框进行选择。
   * 如需将应用添加到新项目，直接在框中填写新项目名称。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/29/v3/s2Rhbk3oTdWJXyn3sY1Zpg/zh-cn_image_0000002312628981.png?HW-CC-KV=V1&HW-CC-Date=20260601T071815Z&HW-CC-Expire=86400&HW-CC-Sign=4C2C634D802F65A93B85EB8BAEB232533BCA53B6856F7B675E47210670F83E8B)
4. 进入“云开发数据处理位置”页面，设置或管理项目的数据处理位置。
   * 如项目尚未设置数据处理位置：
     1. 点击“启用”。

        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b5/v3/qnbB4XL6RSmRD5GAftEjQw/zh-cn_image_0000002312516673.png?HW-CC-KV=V1&HW-CC-Date=20260601T071815Z&HW-CC-Expire=86400&HW-CC-Sign=FA8127A4171473FA60234BBDACB0713F66A33CE7213DFEE53E8069723863CE50)
     2. 仔细阅读提示框的文字说明后，在“启用”栏为您的项目勾选一个或多个数据处理位置，并在“设为默认”栏将其中一个设置为默认数据处理位置。

        注意

        启用的数据处理位置必须包含中国站点。

        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8c/v3/Xj-2ElWqQNOfGGFN6yhCgA/zh-cn_image_0000002214858805.png?HW-CC-KV=V1&HW-CC-Date=20260601T071815Z&HW-CC-Expire=86400&HW-CC-Sign=2C13F723D2BC1619B27AD2ECE0C94A3B77402FFB501A6F4A8C40FB5673C2225C)
   * 如项目已设置过数据处理位置，可点击“管理”启用新的数据处理位置、取消已启用的数据处理位置，或修改默认数据处理位置。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/90/v3/LXm2BEfbRHCNGPo7f-cKrQ/zh-cn_image_0000002312630869.png?HW-CC-KV=V1&HW-CC-Date=20260601T071815Z&HW-CC-Expire=86400&HW-CC-Sign=32A54468F8D1167E6FDFB9F924D9AFBB84127BBD809A050FB12C9E3150EC6FAF)
5. 点击“确认”，应用创建完成。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1e/v3/wFAJGsIsScGuD797VaGZnQ/zh-cn_image_0000002214858821.png?HW-CC-KV=V1&HW-CC-Date=20260601T071815Z&HW-CC-Expire=86400&HW-CC-Sign=05680F71754B56B4E003013169FB7F499E79579AF385DAB104ED46FFC8A07679)
6. 返回DevEco Studio，可看到界面已获取并展示了刚刚创建的应用信息。若不展示，可点击Bundle name后的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ac/v3/9YtidGAQSTW1A0rUKjeDNg/zh-cn_image_0000002500745449.png?HW-CC-KV=V1&HW-CC-Date=20260601T071815Z&HW-CC-Expire=86400&HW-CC-Sign=F5D850DEC74B85ED1C7535E4AC791A6187B80671772A12F1DC83C419A9A045C5)刷新。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/56/v3/iUr1gGr9TLaWSJpb8EBKPg/zh-cn_image_0000002179338492.png?HW-CC-KV=V1&HW-CC-Date=20260601T071815Z&HW-CC-Expire=86400&HW-CC-Sign=E0E2EAAB7CA1A4A643F1E724BF3E44FEA676B5030B64A7FAC12B82E618923B18)

### 将游离应用添加到AGC项目下

游离应用指未关联任何AGC项目的应用。创建工程时，如需要关联的AGC应用为游离应用，则您需要将该应用添加到您的AGC项目下。

注意

应用与项目的关联关系一旦创建则无法再修改，请谨慎操作。

1. 点击“Not associated yet”，或点击界面下方提示内的“AppGallery Connect”，可打开AGC控制台“开发与服务”页面。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e5/v3/nSYaKP3LRBG-nPIPCtDn1Q/zh-cn_image_0000002214704437.png?HW-CC-KV=V1&HW-CC-Date=20260601T071815Z&HW-CC-Expire=86400&HW-CC-Sign=329A476D575ACF8575012221EFAFD7C37961DF82560CF8D23805B474F0A1A43F)
2. 点击选择希望为应用关联的项目，或者点击“添加项目”新建一个项目。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c8/v3/iHXzvsvXReOi7VSFjVhYeQ/zh-cn_image_0000002496495517.png?HW-CC-KV=V1&HW-CC-Date=20260601T071815Z&HW-CC-Expire=86400&HW-CC-Sign=358A9745B78D6F294280DC7F378319302031788FEC7B32A3725D3DEBDBF0E6BD)
3. 如选择了新建一个项目，设置项目名称，点击“确认”。

   如选择了已有项目，则忽略此步骤。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e4/v3/Ra4HnLvzSj6KaP0bzL6-nw/zh-cn_image_0000002214704389.png?HW-CC-KV=V1&HW-CC-Date=20260601T071815Z&HW-CC-Expire=86400&HW-CC-Sign=07617A0F0A70A305F585105B24B9D92A2D4F7D90CBF1E597A40628204C690489)
4. 设置或管理项目的数据处理位置。
   * 如项目尚未设置数据处理位置：
     1. 点击“启用”。

        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/19/v3/3-3E8b0nSZe6tibLpyb60A/zh-cn_image_0000002214704417.png?HW-CC-KV=V1&HW-CC-Date=20260601T071815Z&HW-CC-Expire=86400&HW-CC-Sign=20B551D568CAB5BDEACB976A0DB987D87CD85E08A8BDB73EDF1D4E8D0600E9D9)
     2. 仔细阅读提示框的文字说明后，在“启用”栏为您的项目勾选一个或多个数据处理位置，并在“设为默认”栏将其中一个设置为默认数据处理位置。

        注意

        启用的数据处理位置必须包含中国站点。

        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bf/v3/aoEWskyTRIic4MbILVWO8Q/zh-cn_image_0000002179338436.png?HW-CC-KV=V1&HW-CC-Date=20260601T071815Z&HW-CC-Expire=86400&HW-CC-Sign=97B4E23ACEB857DD7E8A13AB5BAF163FF18157E8CCEF2A570719BFEAE91D7D4A)
   * 如项目已设置过数据处理位置，可点击“管理”启用新的数据处理位置、取消已启用的数据处理位置，或修改默认数据处理位置。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ed/v3/_RbQLygwSveqN9PAo6-YaQ/zh-cn_image_0000002179338464.png?HW-CC-KV=V1&HW-CC-Date=20260601T071815Z&HW-CC-Expire=86400&HW-CC-Sign=930E1F1F9DA5B88A63CF394EDEA5B12611A91D1B54AACCAE12BF1C5EC4E4F977)
5. 点击“确认”，应用成功关联项目。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ed/v3/0A_S4zBkR4aYXlxmSi52NQ/zh-cn_image_0000002179498200.png?HW-CC-KV=V1&HW-CC-Date=20260601T071815Z&HW-CC-Expire=86400&HW-CC-Sign=41762402EBDCD28DF52B5325BE6F2BEFB78DEED53770A34717F29F4A190F8DDA)
6. 返回DevEco Studio，可看到应用已关联上了项目。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1f/v3/xNEaF8_YR7-hjxMbOaWoCw/zh-cn_image_0000002214858777.png?HW-CC-KV=V1&HW-CC-Date=20260601T071815Z&HW-CC-Expire=86400&HW-CC-Sign=7D9BD6FDE1AE252578D33028A36FD92059BFD68B7A39D99DB5C0807F5285C9B1)
