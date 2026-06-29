---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/agc-harmonyos-clouddev-faq
title: FAQ
breadcrumb: 指南 > 开发环境搭建 > 工程创建 > 模块管理 > 端云一体化开发 > FAQ
category: harmonyos-guides
scraped_at: 2026-06-01T15:18:36+08:00
doc_updated_at: 2026-04-22
content_hash: sha256:9c91860ada437ee7debcfd16be96cc3e2a1e03fe910e3f0dc3fd29a777731be6
---
## 使用DevEco Studio打开端云一体化项目文件夹，左侧的项目列表不显示云侧工程

**问题现象**

开发者使用DevEco Studio打开端云一体化项目文件夹，左侧的项目列表不显示云侧工程“CloudProgram”。

**解决措施**

端云一体化工程根目录下只允许有“Application”与“CloudProgram”文件夹，不能有其他文件。否则，DevEco Studio会把该工程当成纯端侧工程，不显示云侧工程“CloudProgram”。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/53/v3/iH9qQk_MSWy518sEgePU9Q/zh-cn_image_0000002313987669.png?HW-CC-KV=V1&HW-CC-Date=20260601T071837Z&HW-CC-Expire=86400&HW-CC-Sign=66AB591C87B26B21BB39316CCD3E2F2A8AFB29AB52CEF775E358589D48B14C06)

## 部署云数据库时，提示“clouddb deploy failed. Reason is the number of CloudDBZone exceeds the limit.”

**问题现象**

部署云数据库失败，提示“clouddb deploy failed. Reason is the number of CloudDBZone exceeds the limit.”

**解决措施**

出现此错误，表示AGC云端的存储区数量超过最大限制。

部署到AGC云端的存储区数量不得超过4个，否则会导致部署失败。如AGC云端当前已存在4个存储区，请将数据部署到已有的存储区，或者删除已有存储区后再部署新的存储区。

**需要注意的是，删除存储区，该存储区内的数据也将一并删除，且不可恢复。**

## 部署云数据库时，提示“clouddb deploy failed. Reason is existing fields cannot be modified.”

**问题现象**

部署云数据库失败，提示“clouddb deploy failed. Reason is existing fields cannot be modified.”

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d0/v3/Fc1glYb1TH-ttb3gN3apAQ/zh-cn_image_0000002179338656.png?HW-CC-KV=V1&HW-CC-Date=20260601T071837Z&HW-CC-Expire=86400&HW-CC-Sign=7622033BC78DD4973B19352627C89EE29EBE54637453988704CFFB8F2B30BAFB)

**解决措施**

出现此错误，可能是您在本地对象类型内做了与云端不兼容的修改。

对象类型中的fieldType等字段信息，部署到AGC云端后，请勿在本地再做修改。例如，fieldType设置为String，对象类型部署成功后，又在本地修改fieldType为Integer，再次部署将失败，提示“clouddb deploy failed. Reason is existing fields cannot be modified.”错误。如需更改fieldType等字段信息，请先删除云端部署的对象类型。

**需要注意的是，删除云端对象类型，对象类型内添加的数据也将一并删除，且不可恢复。**

## 体验端云一体化模板APP功能时，云存储上传图片失败，Hilog中打印“on response {"version":"HTTP/1.1","statusCode":403,"reason":"Forbidden","headers":{}}”

**问题现象**

体验端云一体化模板APP功能时，云存储上传图片失败，Hilog中打印“on response {"version":"HTTP/1.1","statusCode":403,"reason":"Forbidden","headers":{}}”。

**解决措施**

出现此错误，原因是访问权限不足，可采用以下任一方法解决：

* [将云存储的安全策略配置为始终可读写](附录：云开发工程模板/通用云开发模板/agc-harmonyos-clouddev-emptyability.md#li1693311281068)
* 参考[AuthProvider](<../../../../../harmonyos-references/Cloud Foundation Kit（云开发服务）/ArkTS API/cloudCommon (公共模块)/cloudfoundation-cloudcommon.md#authprovider>)获取用户凭据

## 体验端云一体化模板APP功能时，云数据库界面不展示数据，Hilog中打印“schemaJson\_ is empty”

**问题现象**

体验端云一体化模板APP功能时，云数据库界面不展示数据，Hilog中打印“schemaJson\_ is empty”。

**解决措施**

请检查resources/rawfile目录下是否存在schema文件。schema文件是云数据库功能依赖的必要文件，部署云数据库成功时会自动产生。如schema文件不存在，请重新部署云数据库，或[从AGC控制台导出](https://developer.huawei.com/consumer/cn/doc/AppGallery-connect-Guides/agc-clouddb-agcconsole-objecttypes-0000001127675459#section1558018208151)。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2c/v3/EKfGNAg0QEiyCpkKksj1nw/zh-cn_image_0000002179338664.png?HW-CC-KV=V1&HW-CC-Date=20260601T071837Z&HW-CC-Expire=86400&HW-CC-Sign=C14067C565A41981B173A02AC58E8303BFB3BFF1C776DF641C9A49CDFE3B2498)

## 云数据库无法新建数据条目，Hilog中打印“2001015:permission denied”

**问题现象**

云数据库无法新建数据条目，Hilog中打印“2001015:permission denied”。

**解决措施**

出现此错误，是因为APP操作者的角色权限不足，请检查[操作的对象类型的权限配置](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/agc-harmonyos-clouddev-objecttype#li01856582915)。

## 云函数调用失败，error message包含“404:160404:Trigger not exist”

**问题现象**

云函数调用失败，error message包含“404:160404:Trigger not exist”。

**解决措施**

出现此错误，是因为云函数未部署。error message中的404是服务端返回的HTTP状态码，表示找不到对应的函数。

## 云函数调用失败，error message包含“hmos auth app doesn't have permission”

**问题现象**

云函数调用失败，error message包含“hmos auth app doesn't have permission”。

**解决措施**

出现此错误，是因为选择的签名方式有误。推荐您使用[关联注册应用进行签名](../../../../编写与调试应用/配置调试签名/ide-signing.md#section20943184413328)方式，或者使用[手动签名](../../../../编写与调试应用/配置调试签名/ide-signing.md#section297715173233)。

## 云函数部署失败，提示“The function type cannot be changed”

**问题现象**

云函数部署失败，错误信息中提示“The function type cannot be changed”。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/33/v3/lJANVizOQ_OrXEZBsX7Vaw/zh-cn_image_0000002214858977.png?HW-CC-KV=V1&HW-CC-Date=20260601T071837Z&HW-CC-Expire=86400&HW-CC-Sign=7D3EA8CE0F2A628DA947EAF3AC620C52F386CB483AE618693F0801144C17E8EA)

**解决措施**

出现此错误，是因为云函数分为传统云函数类型和云对象类型。一种类型的云函数在部署到AGC云端后，不允许再变更成另一种类型。您可以前往AGC控制台的云函数服务页面，手动删除之前已部署的同名云函数/云对象，然后重新在DevEco Studio执行部署操作。

## 部署云工程失败，提示“Remote host terminated the handshake”

**问题现象**

部署云工程失败，错误信息中提示“Remote host terminated the handshake”。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/96/v3/JYAyLwQcRpeNAdg1V3Ijww/zh-cn_image_0000002279650126.png?HW-CC-KV=V1&HW-CC-Date=20260601T071837Z&HW-CC-Expire=86400&HW-CC-Sign=29D7D45ABAC0FAE2F55039EAFE13DD7E0B4438DF29D7B2CA4487328EE1D9B6D9)

**解决措施**

出现此错误，是因为网络连接SSL/TLS握手失败。建议检查[DevEco Studio Proxy代理配置](../../../../编写与调试应用/附录/配置代理/ide-environment-config.md#section10369436568)或本地网络防火墙/安全配置。

## 在云函数中调用云函数失败，提示“mismatched authType”

**问题现象**

在云函数中调用云函数失败，错误信息中提示“mismatched authType”。

**解决措施**

出现此错误，是因为被调用的云函数的HTTP触发器的认证类型须配置为云侧网关认证，即“authType”字段须配置为“cloudgw-client”。修改被调用云函数的“function-config.json”文件中的“authType”字段值，然后重新部署被调用的云函数即可。

## 端云一体化开发工程同步失败，失败步骤为npm install failed

**问题现象**

端云一体化开发工程同步失败，失败步骤是npm install failed。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/df/v3/4sGq1FbYR-K3gl8bU1F0_Q/zh-cn_image_0000002279546734.png?HW-CC-KV=V1&HW-CC-Date=20260601T071837Z&HW-CC-Expire=86400&HW-CC-Sign=680DCD9F446B31EE36B22335693295A5B47FBA5273194F87D19DF3B2AC7E2263)

**解决措施**

出现此错误，是因为端云一体化开发的云侧工程是通过npm管理依赖，同步时需要通过npm去下载对应依赖。请参考[配置NPM代理](../../../../编写与调试应用/附录/配置代理/ide-environment-config.md#section197296441787)检查npm代理和网络情况。

## 使用云存储上传文件失败，提示“404:Product does not exist”

**问题现象**

使用云存储上传文件失败，HiLog提示“404:Product does not exist”。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/42/v3/lqNO8p4IQI-u5AW6LRjUdw/zh-cn_image_0000002214704601.png?HW-CC-KV=V1&HW-CC-Date=20260601T071837Z&HW-CC-Expire=86400&HW-CC-Sign=26F1C5957C085E608ABD0AE9C4C0BA5A0A8D1A72A68F64D84C3A3D869834351F)

**解决措施**

云存储服务端返回的错误，出现此错误是因为云存储服务未开通。请在顶部菜单栏选择“Tools > CloudDev”，进入CloudDev云开发管理面板，点击“Cloud Storage”服务下的“Go to console”快捷进入AGC服务菜单进行手动开通。

## 使用云存储上传文件失败，app日志提示“"state":65”，upload进程日志提示“403 Forbidden”

**问题现象**

使用云存储上传文件失败，出现如下错误提示：

* app日志提示“"state":65”

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dc/v3/gWbv5e-dS3WS8IzuKydyQw/zh-cn_image_0000002179498352.png?HW-CC-KV=V1&HW-CC-Date=20260601T071837Z&HW-CC-Expire=86400&HW-CC-Sign=4ECBD3438BE8107CEF1C60B092EDCF66F9DA0534B71DB249522D88DB2F1F86AE)
* upload进程的日志提示“403 Forbidden”（通过设置“No filters”模式、过滤“C01C50”关键字查找）

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f1/v3/tNCPkh-_R2adPTDCw3ZyMg/zh-cn_image_0000002214858989.png?HW-CC-KV=V1&HW-CC-Date=20260601T071837Z&HW-CC-Expire=86400&HW-CC-Sign=A84E211C53E66FD8B0EF4725E6EF5FD9D3E743D75A2569213A79A1B15A1EE245)

**解决措施**

出现此问题，可按照如下步骤排查和解决：

* 请确认应用的签名方式正确。当前支持[关联注册应用进行自动签名](../../../../编写与调试应用/配置调试签名/ide-signing.md#section20943184413328)和[手动签名](../../../../编写与调试应用/配置调试签名/ide-signing.md#section297715173233)两种方式。
* [将云存储的安全策略配置为始终可读写](附录：云开发工程模板/通用云开发模板/agc-harmonyos-clouddev-emptyability.md#li1693311281068)
* 参考[AuthProvider](<../../../../../harmonyos-references/Cloud Foundation Kit（云开发服务）/ArkTS API/cloudCommon (公共模块)/cloudfoundation-cloudcommon.md#authprovider>)获取用户凭据
