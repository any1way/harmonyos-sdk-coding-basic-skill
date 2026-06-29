---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/iap-faq-14
title: 如何解决证书链不完整？
breadcrumb: 指南 > 应用服务 > IAP Kit（应用内支付服务） > IAP Kit常见问题 > 如何解决证书链不完整？
category: harmonyos-guides
scraped_at: 2026-06-11T15:08:45+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:8932e8bada4bef541ae539bae233ffa1737828fdf48249b11c4e2afa86534d9a
---

如果开发者提供的证书在IAP服务内置信任库中查询不到，则该证书不被IAP信任，需要构造完整的信任链以被IAP信任。

此处以Chrome浏览器最新版本（一般是支持自动验证证书链）为工具，以华为的证书为例，手工构造完整的证书链步骤如下：

说明

开发者也可以选择其他证书链工具构造完整的证书链。

1. 查看服务器证书。

   访问[华为开发者网站](https://developer.huawei.com/consumer/cn/)，依次点击“查看网站信息 > 显示连接详情 > 显示证书 > 详细信息”，可查看证书状况，如下图所示：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a0/v3/R0pf4Sf9SC27lkyXqSV9uw/zh-cn_image_0000002592219382.png?HW-CC-KV=V1&HW-CC-Date=20260611T070844Z&HW-CC-Expire=86400&HW-CC-Sign=3347647D30EF8C5EF3539DE0DCE61CE94793A3FF97FCA1FFF4B1B8E4C918E36E)
2. 导出服务器证书链至文件中。

   依次点击“服务器证书 > 导出 > Base64 编码 ASCII，证书链（\*.pem;\*.crt） > 保存”，如下图所示：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/53/v3/aIGNiNNESh6OZrGeydpqiA/zh-cn_image_0000002592379316.png?HW-CC-KV=V1&HW-CC-Date=20260611T070844Z&HW-CC-Expire=86400&HW-CC-Sign=8F69BAE225BB60EB61A881DC6641683EF6B97706FED395F9AD7647D1109E731F)
3. 导出的证书链文件，使用文本编辑器打开.crt文件，可以看到与下图格式相似的PEM格式的证书内容，从上到下依次为“服务器证书 > 中间证书 > 根证书”，将已经拼接好的证书链返回给IAP服务器。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1e/v3/5fLpg9DWQraVMi-X98unBQ/zh-cn_image_0000002622858825.png?HW-CC-KV=V1&HW-CC-Date=20260611T070844Z&HW-CC-Expire=86400&HW-CC-Sign=A2AB7382C551FF46BBFE403EF02F139610B4B1E9F9A73211DC6A9609F2296F94)
