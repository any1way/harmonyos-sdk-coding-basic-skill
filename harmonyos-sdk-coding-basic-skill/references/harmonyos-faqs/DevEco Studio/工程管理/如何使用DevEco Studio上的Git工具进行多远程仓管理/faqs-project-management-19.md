---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-project-management-19
title: 如何使用DevEco Studio上的Git工具进行多远程仓管理
breadcrumb: FAQ > DevEco Studio > 工程管理 > 如何使用DevEco Studio上的Git工具进行多远程仓管理
category: harmonyos-faqs
scraped_at: 2026-06-12T10:40:31+08:00
doc_updated_at: 2026-06-05
content_hash: sha256:56e02c52227977b8c192575859417a3a65d42b6227170e54298c1c368eae3d38
---

添加新的远程仓库：

1. 右击Remote以调出菜单。
2. 点击Manage Remotes，打开Git Remotes窗口。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/21/v3/dafIcUXkShOZNiCrM_3O3w/zh-cn_image_0000002194318352.png?HW-CC-KV=V1&HW-CC-Date=20260612T024030Z&HW-CC-Expire=86400&HW-CC-Sign=7A42EB5478349158122A28BE94013D234A4C1EA2EC2EFA91DF549BDB9CB8D398)
3. 点击添加按钮。
4. 输入远程仓名称和URL，远程仓名称可自由命名。
5. 点击Define Remote窗口的OK按钮，在新弹出的窗口中输入域账号和密码。
6. 点击Git Remotes窗口的确定按钮。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1d/v3/-yPVQOCWQheIpZ8GnFe0OQ/zh-cn_image_0000002229604125.png?HW-CC-KV=V1&HW-CC-Date=20260612T024030Z&HW-CC-Expire=86400&HW-CC-Sign=55AF23AEB45E0E60E88A990E9EF99CDB122EC755079DFAF14D7E39BF8F5E495F "点击放大")
7. 点击拉取远程记录，新添加的远程仓库将在Remote子菜单中显示。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/de/v3/sNZe2sbJQwyT9AWevBHsFg/zh-cn_image_0000002229758613.png?HW-CC-KV=V1&HW-CC-Date=20260612T024030Z&HW-CC-Expire=86400&HW-CC-Sign=D568A3BE59E41E58198B2CAFB3E3ED0471158F6565D8795A8C20BBBE6010625D)

Push提交：

Push提交和Push提交到远程仓库的过程相似。如需切换远程仓库，可单击下图中标记1的分支名；标记3表示以PR方式提交。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/93/v3/CyNCknWSRGezJc-2YlVDGg/zh-cn_image_0000002194158744.png?HW-CC-KV=V1&HW-CC-Date=20260612T024030Z&HW-CC-Expire=86400&HW-CC-Sign=E1AA92DB57222BBC663A588299177DE4FE127A4919E5BE77EDD30B34BA8AB5CF "点击放大")

切换默认关联的远程仓库：

可以使用以下命令进行切换。

```
1. git branch hmos_dev_20230907 --set-upstream-to=codehub_origin/hmos_dev_20230907
```
