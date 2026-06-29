---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/push-delivery-report
title: （可选）推送报告
breadcrumb: 指南 > 应用服务 > Push Kit（推送服务） > 端云调试 > （可选）推送报告
category: harmonyos-guides
scraped_at: 2026-06-11T15:13:19+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:2466d6de48845c4e6f720a194afd63da174cff7b5c74a8169d7000f2dc6993dc
---

登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)网站，点击“开发与服务”，在项目列表中找到您的项目，通过“增长 > 推送服务 > 推送报告”，您可以在“推送报告”中查看推送消息详情和推送用户详情。

说明

推送报告数据不是实时数据，当天生成的数据在控制台次日才能查看到。

## 推送消息详情

您可以查看推送消息的详情，场景化消息的统计图和对应表格，同时可以按照通道维度进行查看，有“通过AGC控制台”、“通过API方式”和“全部通道”；也可以按照消息类型维度进行查看。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c4/v3/ZPG4l-OlSPuXzJ3nDnjgVg/zh-cn_image_0000002592379506.png?HW-CC-KV=V1&HW-CC-Date=20260611T071318Z&HW-CC-Expire=86400&HW-CC-Sign=690C16B7973593830F1D96CD3678434FBCAF576D111B34F431254DD93D05E7E0)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5a/v3/QTreGqtJTqqQtzLcQLY3lA/zh-cn_image_0000002622859015.png?HW-CC-KV=V1&HW-CC-Date=20260611T071318Z&HW-CC-Expire=86400&HW-CC-Sign=8510FC3E90AA809A53F8C2816A5293EFD622D6E43C89571F1107AF7E6D8845D4)

点击自定义后的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/46/v3/NyqOsLDySUSQffU4p4KIIw/zh-cn_image_0000002622699135.png?HW-CC-KV=V1&HW-CC-Date=20260611T071318Z&HW-CC-Expire=86400&HW-CC-Sign=74BF1F3AB7687A23A502E3F4FCBBAF672CB7F4F85E9CED7898CF3F8896B9E15A)，可自定义推送消息报表展示的表格列，默认展示的表格列有：日期、消息类型、请求量、发送量、到达量、显示量、点击量、到达率（%）、点击率（%）、沉默设备丢弃、应用被卸载、无效TOKEN、通知关闭。全选可展示全部表格列，重置则恢复默认表格列。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ea/v3/YecAUJpdRWGouP65Ai_S3g/zh-cn_image_0000002592219574.png?HW-CC-KV=V1&HW-CC-Date=20260611T071318Z&HW-CC-Expire=86400&HW-CC-Sign=0448255109F08C03D93F20D5F9797B8C9A374F0F63ED1CC273409B95CDEA1B6A)

报表数据条目说明：

* 请求量：该推送任务预计覆盖的设备数量。
* 发送量：在请求量的基础上剔除不符合下发条件的消息数量，实际下发的消息数量。
* 到达量：扣除未触达量后实际到达的数量。
* 显示量：消息展示在通知栏的数量。
* 点击量：用户点击推送消息的数量。
* 到达率（%）：到达量/发送量。
* 点击率（%）：点击量/显示量。
* 沉默设备丢弃：终端设备超过30天没有联网的数量。
* 频控丢弃量：向单个设备发送消息超出上限，超出部分被丢弃的数量。
* 应用被卸载：用户已经卸载该应用并且没有重新安装的数量。
* 无效TOKEN：消息从云端发送到终端设备过程中，由于Token无效不展示的数量。
* 通知关闭：用户关闭了应用的消息通知权限的数量。
* 消息覆盖：待发送消息被覆盖的数量。针对待发送消息，只保留最新一条，其余待发送消息会被覆盖不下发。
* 其他原因：其他不满足触达条件的情况，如推送链接无法正常访问等。
* 过期量：目标设备离线，在消息有效期内设备未上线导致消息过期的数量。
* 缓存量：目标设备离线，消息仍在有效期内的数量。
* 未触达量：消息未到达终端设备的数量。

说明

不符合下发条件的消息数量包括：沉默设备丢弃、频控丢弃量、应用被卸载、无效TOKEN、通知关闭、消息覆盖、其他原因、过期量、缓存量。

## 推送用户详情

您可以查看推送用户的详情，根据时间维度查看活跃用户、新增用户和总用户的统计数据。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d3/v3/M_6pw5D_TEqcXbJeqVTKMw/zh-cn_image_0000002592379508.png?HW-CC-KV=V1&HW-CC-Date=20260611T071318Z&HW-CC-Expire=86400&HW-CC-Sign=A66D746BAD08E80192393211D7B3C3DD6296D246884DF3417177236BC744530E)

报表数据条目说明：

* 当天活跃用户数：当天设备与Push服务端建立连接的用户数量。
* 当天新增用户数：当天新安装的用户数量。不统计重复卸载安装应用场景。
* 30日活跃用户数：查询日往前30日内设备与Push服务端建立连接的用户数量。
* 总用户数：已安装的总用户数量。
