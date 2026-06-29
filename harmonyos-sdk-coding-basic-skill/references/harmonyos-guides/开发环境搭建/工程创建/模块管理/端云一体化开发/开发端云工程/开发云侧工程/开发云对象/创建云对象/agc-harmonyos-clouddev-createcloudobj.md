---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/agc-harmonyos-clouddev-createcloudobj
title: 创建云对象
breadcrumb: 指南 > 开发环境搭建 > 工程创建 > 模块管理 > 端云一体化开发 > 开发端云工程 > 开发云侧工程 > 开发云对象 > 创建云对象
category: harmonyos-guides
scraped_at: 2026-06-01T15:18:26+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:ab2cecd8662b23325903e6c34edf7b0e16dee1e6fd50585e565aefa27c1b0665
---

首先您需要在云侧工程下创建云对象。

1. 右击“cloudfunctions”目录，选择“New > Cloud Function”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1b/v3/nQIRTz-nRzyEOpamV-w7QA/zh-cn_image_0000002383015456.png?HW-CC-KV=V1&HW-CC-Date=20260601T071827Z&HW-CC-Expire=86400&HW-CC-Sign=180C9D367C75080AC288A1FDF978D860289FCD673B57286667D1EEAADE89A664)
2. 在“Select the Cloud Function Type”栏选择“Cloud Object”，输入云对象名称（如“my-cloud-object”），点击“OK”。

   与云函数名一样，云对象名称长度2-63个字符，仅支持小写英文字母、数字、中划线（-），首字符必须为小写字母，结尾不能为中划线（-）。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5c/v3/7hV5JLr3Scyg9F1Kz-2mAw/zh-cn_image_0000002179498304.png?HW-CC-KV=V1&HW-CC-Date=20260601T071827Z&HW-CC-Expire=86400&HW-CC-Sign=68DC3060727A0144BAEA4C945111E4FB67CCB607E40F874470A0AE63AEFE828F)

   “cloudfunctions”目录下生成新建的云对象目录，目录下主要包含如下文件：
   * 云对象配置文件“function-config.json”：包含handler、触发器等信息。
     + handler: 云对象的入口模块及云对象导出的类，通过“.”连接。
     + functionType：表示函数类型，“0”表示云函数，“1”表示云对象。
     + triggers：定义了云对象使用的触发器类型，当前云对象仅支持HTTP触发器。

     说明

     云对象的配置文件“function-config.json”不建议手动修改，否则将导致云对象部署失败或其它错误。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d4/v3/f7DL1LkUTuiErZrtfrTBLA/zh-cn_image_0000002214858949.png?HW-CC-KV=V1&HW-CC-Date=20260601T071827Z&HW-CC-Expire=86400&HW-CC-Sign=8595743C4692D2C288F220A70FAAFD1D95B51D333CB8BA5D7FF0A20A0ED8C61C)
   * 云对象入口文件“*xxx*.ts”（如“myCloudObject.ts”）：在此文件中编写云对象代码。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/38/v3/9zoEPWKXRwqXUZF2RNH_dA/zh-cn_image_0000002214704565.png?HW-CC-KV=V1&HW-CC-Date=20260601T071827Z&HW-CC-Expire=86400&HW-CC-Sign=49DAA5AB5EE4ED51B44CFD263079EDD00C4A5270A1E6274A78536F2A0CD8A355)
   * 云对象依赖配置文件“package.json”：在此文件中添加依赖。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/25/v3/5JuBqFI7R-qa1klRdEQtPA/zh-cn_image_0000002179338620.png?HW-CC-KV=V1&HW-CC-Date=20260601T071827Z&HW-CC-Expire=86400&HW-CC-Sign=BD8AB6D535DA3B01AD17C49746B5C54B8470FD9D417C79177EB8DE3082FE0A0C)
