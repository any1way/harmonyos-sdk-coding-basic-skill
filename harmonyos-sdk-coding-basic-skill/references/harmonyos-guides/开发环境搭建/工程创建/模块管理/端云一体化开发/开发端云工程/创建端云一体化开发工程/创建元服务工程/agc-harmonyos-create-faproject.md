---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/agc-harmonyos-create-faproject
title: 创建元服务工程
breadcrumb: 指南 > 开发环境搭建 > 工程创建 > 模块管理 > 端云一体化开发 > 开发端云工程 > 创建端云一体化开发工程 > 创建元服务工程
category: harmonyos-guides
scraped_at: 2026-06-01T15:18:15+08:00
doc_updated_at: 2026-01-30
content_hash: sha256:3af2a2580fcb327f833e3e57a0c9a4288e4f01e89ad03cc1fb2ab62d711d4a08
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
2. 点击“Atomic Service”页签，选择合适的云开发模板，然后点击“Next”。

   说明

   当前仅支持通用云开发模板（[CloudDev]Empty Ability）。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8c/v3/bW1b3HPZS9-Y-icDDK2rVg/zh-cn_image_0000002495751689.png?HW-CC-KV=V1&HW-CC-Date=20260601T071816Z&HW-CC-Expire=86400&HW-CC-Sign=7E4101B1CA946D135B02A17F6A8950870AB85C94698594F77561B41252B9E05C)

### 关联云开发资源

为工程关联云开发所需的资源，即将您账号团队在AGC创建的元服务关联到待创建工程。具体操作如下：

1. （可选）如您尚未登录DevEco Studio，点击“Sign In”，在弹出的账号登录页面，使用[已实名认证](../../../开发准备/注册华为开发者账号并实名认证/agc-harmonyos-clouddev-account.md)的华为开发者账号完成登录。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b7/v3/9KzC7oQ9RL2dBKeVpE4prw/zh-cn_image_0000002214858877.png?HW-CC-KV=V1&HW-CC-Date=20260601T071816Z&HW-CC-Expire=86400&HW-CC-Sign=F3E95A11A4166C0FDEB89EB163E4822CF2332F2EDD5FB047792F2779CAB52690)

   登录成功后，界面将展示账号昵称。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/08/v3/bSTLM6EAQ9-OIdkt9WcLrw/zh-cn_image_0000002179498232.png?HW-CC-KV=V1&HW-CC-Date=20260601T071816Z&HW-CC-Expire=86400&HW-CC-Sign=BA9890AED1265F1DE60D5DAADF91648B18EA9F8D69B9A8B28D461DF02D908BB2)
2. 选择已登录账号下的APP ID，以关联AGC上的元服务。
   * 从APP ID下拉列表中选中所需的APP ID后，界面会展示该元服务在AGC控制台的名称、所属项目、包名与数据处理位置。确认无误后，点击“Next”。

     说明

     元服务包名为自动生成，格式为固定前缀与appid的组合（com.atomicservice.[appid]）。不符合命名规范的包名无法在APP ID下拉列表中展示。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1a/v3/GsIX-zrAS2Sk-9-ZQSgFEw/zh-cn_image_0000002496005713.png?HW-CC-KV=V1&HW-CC-Date=20260601T071816Z&HW-CC-Expire=86400&HW-CC-Sign=12978C82FFE57416FCFC915F019EC40314F58906A6CE432FD925EFC5E297536F)
   * 当出现以下场景时，您可点击“Register App ID”，[前往AGC控制台补充创建元服务](agc-harmonyos-create-faproject.md#section397317130308)。创建成功后返回DevEco Studio界面，即可看到新建的元服务信息。
     + APP ID框为空，即当前账号尚未在AGC控制台创建任何元服务。
     + 您需为待创建工程关联一个新的元服务。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d1/v3/u5o46CQCQLu4ts871zlqzA/zh-cn_image_0000002214858837.png?HW-CC-KV=V1&HW-CC-Date=20260601T071816Z&HW-CC-Expire=86400&HW-CC-Sign=31B27B5D103E3E52F23DA70771323D934FF8F3FECA08E761D164DFF6E459B5B0)
   * 如查询到的元服务尚未关联任何项目，则无法选中。请先[将游离元服务添加到AGC项目下](agc-harmonyos-create-faproject.md#section152521927193013)，再返回DevEco Studio界面操作。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/47/v3/Ukc-A8mUSz26JA4EEMVdhg/zh-cn_image_0000002462648052.png?HW-CC-KV=V1&HW-CC-Date=20260601T071816Z&HW-CC-Expire=86400&HW-CC-Sign=B40DF6C43E20BE5D9233042EF452D71E1EC3869B6BCE3CECD0886BAD22E61A12)
   * 如果查询到的元服务所属项目尚未启用数据处理位置，请点击界面提示内的“AppGallery Connect”[设置数据处理位置](https://developer.huawei.com/consumer/cn/doc/app/agc-help-datalocation-0000001160439813)。设置完成后返回DevEco Studio界面，点击“Refresh”刷新当前APP ID列表，即可看到设置的数据处理位置。

     注意

     + 由于云开发目前仅支持中国境内（香港特别行政区、澳门特别行政区、中国台湾除外），请确保项目启用的数据处理位置包含“中国”。
     + 无论项目启用的默认数据处理位置为哪个站点，后续开发的云服务资源都将部署在“中国”站点。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/73/v3/IE0w7Xu4SfmwQ3CAj-hnmw/zh-cn_image_0000002462747966.png?HW-CC-KV=V1&HW-CC-Date=20260601T071816Z&HW-CC-Expire=86400&HW-CC-Sign=61DCE3322EC137BC2F51389B7A0E9B2D5EAEE617B1ADA6EB560E872AC6C7F93D)

### 配置工程信息

1. 进入工程配置界面，配置工程的基本信息。

   其中，Device type和Enable CloudDev参数不可更改，其他参数请参考[创建元服务工程](https://developer.huawei.com/consumer/cn/doc/atomic-guides/atomic-service-create-project)内对应的指导进行配置。

   | 参数 | 说明 |
   | --- | --- |
   | Device type | 该工程模板支持的设备类型，目前仅支持手机设备。 |
   | Enable CloudDev | 是否启用云开发。云开发模板默认启用且无法更改。 |

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d2/v3/8_Gy_XTETFaoyt_rcou_fQ/zh-cn_image_0000002547471367.png?HW-CC-KV=V1&HW-CC-Date=20260601T071816Z&HW-CC-Expire=86400&HW-CC-Sign=EEE2AC6433B49CD12746322EC9962B3A7EC686FFE4410822B59E10B216887B9E)

2. 点击“Finish”，进入主开发界面，DevEco Studio执行工程同步操作，端侧工程会自动执行“ohpm install”，云侧工程会自动执行“npm install”，以分别下载端侧和云侧依赖。

   说明

   若云侧执行“npm install”失败，请排查是否尚未[配置NPM代理](../../../../../../../编写与调试应用/附录/配置代理/ide-environment-config.md#section197296441787)。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b6/v3/wE_ZTu2MSMO9pJsaGlJJ7w/zh-cn_image_0000002214858865.png?HW-CC-KV=V1&HW-CC-Date=20260601T071816Z&HW-CC-Expire=86400&HW-CC-Sign=6EBC24215F023DE187525C1FA83348E59E3BA27234FE51D5D9B88D3A34D6DFE1)
3. 在主开发界面，可查看刚刚新建的工程。关于工程的详细目录结构介绍，请参见[端云一体化开发工程目录结构](agc-harmonyos-create-faproject.md#section20250910164411)。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/94/v3/Q-ckpvQfS82JEN6Rlfh0fw/zh-cn_image_0000002214704493.png?HW-CC-KV=V1&HW-CC-Date=20260601T071816Z&HW-CC-Expire=86400&HW-CC-Sign=1FB0189621DCECD0DED2ACE78E8FB7923DD9CDAAE6837DE17A8F0F79B0A1C4A2)

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

端开发工程主要用于开发应用端侧的业务代码，使用通用云开发模板创建的端开发工程目录结构如下图所示。“Application/cloud\_objects”模块用于存放云对象的调用接口类，“src/main/ets/pages”目录下包含了云存储、云数据库和云函数页面，其他目录文件介绍请参见[工程目录结构](../../../../../工程目录结构介绍/ide-project-structure.md)。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/68/v3/rmsV-0DWQfGohGw0ZkFFYg/zh-cn_image_0000002179498204.png?HW-CC-KV=V1&HW-CC-Date=20260601T071816Z&HW-CC-Expire=86400&HW-CC-Sign=01FDC4C3C590EB79A8DE346E1CA1EA13B27959F2F132D8CE352D86C8009B6B0F)

### 云开发工程（CloudProgram）

在云开发工程中，您可为您的元服务开发云端代码，包括云函数和云数据库服务代码。使用通用云开发模板创建的云开发工程目录结构如下图所示。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ae/v3/nW0_UIGURw-ausjYbGQXoQ/zh-cn_image_0000002279948894.png?HW-CC-KV=V1&HW-CC-Date=20260601T071816Z&HW-CC-Expire=86400&HW-CC-Sign=7C0F65036286E48E6AF0F10FF948E03A2EF831C37DE3B19D5EA98F269835C83B)

* clouddb：云数据库目录，包含数据条目目录（dataentry）和对象类型目录（objecttype）。
  + dataentry：用于存放数据条目文件。

    该目录下一般会根据您选择的云开发模板预置数据条目示例文件。在通用云开发模板工程中，该目录下会预置名为“d\_Post.json”的数据条目示例文件，内含两条示例数据。您可按需使用、修改或删除。

    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e0/v3/A229tO-UQHO76k-Msnq--g/zh-cn_image_0000002314788585.png?HW-CC-KV=V1&HW-CC-Date=20260601T071816Z&HW-CC-Expire=86400&HW-CC-Sign=3F22FF8DF2E9CB25D156E6E0FA5600C2FEF8570BEFC01C8A5782C9DA3EC496B6)
  + objecttype：用于存放对象类型文件。

    该目录下一般会根据您选择的云开发模板预置对象类型示例文件。在通用云开发模板工程中，该目录下会预置名为“Post.json”的对象类型示例文件，内含对象类型“Post”的权限、索引、字段名称和字段值等。您可按需使用、修改或删除。

    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9b/v3/PHqc6ov-TJGRTtV6cYuBDA/zh-cn_image_0000002179498164.png?HW-CC-KV=V1&HW-CC-Date=20260601T071816Z&HW-CC-Expire=86400&HW-CC-Sign=F683FACF4F51B9184B5C24DD6F384E6C72BD1BC243B13E92BF90ED54BAAAAE6D)
  + db-config.json：模块配置文件，主要包含云数据库工程的配置信息，如默认存储区名称、默认数据处理位置。
* cloudfunctions：云函数目录，包含各个云函数/云对象子目录。每个子目录下包含了云函数/云对象的配置文件、入口文件、依赖文件等。

  该目录下一般会根据您选择的云开发模板预置示例函数。通用云开发模板工程下预置了一个用于生成UUID的示例云对象“id-generator”，您可按需使用、修改或删除。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8b/v3/yQm0eJnvS9G7pzG4JR-Jvg/zh-cn_image_0000002179498100.png?HW-CC-KV=V1&HW-CC-Date=20260601T071816Z&HW-CC-Expire=86400&HW-CC-Sign=41765495E538FA37E7365C82A4B1C9A6BD1B3587BEBB7293DECD46393B699218)
* node\_modules：工程同步时执行“npm install”生成，包含“typescript”和“@types/node”公共依赖。
* cloud-config.json：云开发工程配置文件，包含应用名称与ID、项目名称与ID、启用的数据处理位置、支持的设备类型等。
* package.json：定义了“typescript”和“@types/node”公共依赖。
* package-lock.json：工程同步时执行“npm install”生成，记录当前状态下实际安装的各个npm package的具体来源和版本号。

## （可选）AGC元服务管理

### 从DevEco Studio补充创建元服务

如创建元服务工程时，发现尚未在AGC控制台创建对应的元服务，可直接从DevEco Studio进行补充创建。

1. 点击“Register App ID”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7b/v3/wdJ5T-YmS_2giKBMSKMrLw/zh-cn_image_0000002214704425.png?HW-CC-KV=V1&HW-CC-Date=20260601T071816Z&HW-CC-Expire=86400&HW-CC-Sign=6C86271105A2790AADF04CF0701649046745D09FD317981915E7C5D81A2F1FF3)
2. 在弹窗中填写待创建的元服务信息后，点击“OK”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9d/v3/upmzt34nSSip2Vz7pvxhIg/zh-cn_image_0000002496008473.png?HW-CC-KV=V1&HW-CC-Date=20260601T071816Z&HW-CC-Expire=86400&HW-CC-Sign=BACD10F75D3FF6F42593DCE453A280501A59355FAAE6425B16C81132ACA7B9D6)

   | 参数 | 说明 |
   | --- | --- |
   | Project | 为当前元服务选择所属的项目。可以输入一个新项目名称，或在下拉框中选择已有项目。 |
   | App type | 应用形态。默认为“AtomicService”，不支持修改。 |
   | App name | 元服务在华为应用市场详情页展示的名称。 |
   | App category | 应用分类。元服务暂不支持游戏类别，请选择“App”。  说明  应用分类设置后不支持修改，请谨慎选择。 |
3. 返回DevEco Studio界面，可查看到刚刚创建的元服务的名称及APP ID、所属项目及项目ID、包名、数据处理位置。

   说明

   若元服务关联的是一个新建项目或者尚未启用数据处理位置的已有项目，则还会提示尚未启用数据处理位置，参考[上文](agc-harmonyos-create-faproject.md#li58931263712)处理即可。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/50/v3/0fhTTLvXQeOG47ry-g4crg/zh-cn_image_0000002463542130.png?HW-CC-KV=V1&HW-CC-Date=20260601T071816Z&HW-CC-Expire=86400&HW-CC-Sign=BB23552CD397419B093DA819463CD19306D815B94DB849E4AA6D1240A7E93DD5)

### 将游离元服务添加到AGC项目下

游离元服务指未关联任何AGC项目的元服务。创建工程时，如需要关联的AGC元服务为游离状态，则您需要将该元服务添加到您的AGC项目下。

注意

元服务与项目的关联关系一旦创建则无法再修改，请谨慎操作。

1. 点击“Not associated yet”，或点击界面下方提示内的“AppGallery Connect”，可打开AGC控制台“开发与服务”页面。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ae/v3/-Qm_pqF-S7Wc1cW42NUI6w/zh-cn_image_0000002495887153.png?HW-CC-KV=V1&HW-CC-Date=20260601T071816Z&HW-CC-Expire=86400&HW-CC-Sign=43D30DF3B0340B5B1C0AA62E1AF910B81337EB38D92E4EDCC4F641061C79D38E)
2. 点击选择希望为元服务关联的项目，或者点击“添加项目”新建一个项目。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/97/v3/HA9h1KZySb2OKvWWAW7rsA/zh-cn_image_0000002463616410.png?HW-CC-KV=V1&HW-CC-Date=20260601T071816Z&HW-CC-Expire=86400&HW-CC-Sign=E9052D8976AAECBF98DF9D4714C6D1CBD2DC148C9A518EE4E69B11EEE33A4229)
3. 如选择了新建一个项目，设置项目名称，点击“确认”。

   如选择了已有项目，则忽略此步骤。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f2/v3/oYE40LOKRhaTzZHYxwfNAA/zh-cn_image_0000002179498244.png?HW-CC-KV=V1&HW-CC-Date=20260601T071816Z&HW-CC-Expire=86400&HW-CC-Sign=4960F83723C6D235C8BF490139A5F7A8669364F3B078416C65E6829C0E62F68F)
4. 设置或管理项目的数据处理位置。
   * 如项目尚未设置数据处理位置：
     1. 点击“启用”。

        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3b/v3/oCjs2OjvRe6q32FbCcrFyQ/zh-cn_image_0000002179338536.png?HW-CC-KV=V1&HW-CC-Date=20260601T071816Z&HW-CC-Expire=86400&HW-CC-Sign=81552BFA0C425FD5601F624F5FBF28E0E52CFD0FB035FED6F7BDCE24BC96EB89)
     2. 仔细阅读提示框的文字说明后，在“启用”栏为您的项目勾选一个或多个数据处理位置，并在“设为默认”栏将其中一个设置为默认数据处理位置。

        注意

        启用的数据处理位置必须包含中国站点。

        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/77/v3/9I8YY1NVRKWLBx3IDAL0lw/zh-cn_image_0000002179498220.png?HW-CC-KV=V1&HW-CC-Date=20260601T071816Z&HW-CC-Expire=86400&HW-CC-Sign=DD7535641A36131CBD95BCE7A0188039C1093217DFFDF5CFBF7D2C5A7B7FA16D)
   * 如项目已设置过数据处理位置，可点击“管理”启用新的数据处理位置、取消已启用的数据处理位置，或修改默认数据处理位置。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d2/v3/wV59husxSuW4YI-V2QBudw/zh-cn_image_0000002179338548.png?HW-CC-KV=V1&HW-CC-Date=20260601T071816Z&HW-CC-Expire=86400&HW-CC-Sign=C52AC69AF8B5816164BD0279E83CA2359CA0DD7BBB2F65914D593BEF749E6ACD)
5. 点击“确认”，元服务成功关联项目。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6b/v3/GeLQif2uRdeIAeRkQLKYKw/zh-cn_image_0000002214858853.png?HW-CC-KV=V1&HW-CC-Date=20260601T071816Z&HW-CC-Expire=86400&HW-CC-Sign=E0C9099F78A5B3E7278548D56B89FB4DDB2DBCD5DFDA8926CEBA3CAE312E9571)
6. 返回DevEco Studio，点击“Refresh”刷新，可看到元服务已关联上了项目。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/13/v3/jY-OC6owQC65WiPbC3R1Tw/zh-cn_image_0000002509136865.png?HW-CC-KV=V1&HW-CC-Date=20260601T071816Z&HW-CC-Expire=86400&HW-CC-Sign=0CA264B83DFB2ABF96790F0D91FBECFAE6E66F90775EC6F8F50D45E10EF48ADB)
