---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-screenshot
title: 截屏
breadcrumb: 指南 > 编写与调试应用 > 应用调试 > 截屏
category: harmonyos-guides
scraped_at: 2026-06-11T15:29:27+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:65222ab8ebd7cf9fac67387df44d30aabd4b2c04e3b8db4cd0a62beb0a2aedf3
---
在调试过程中，可以通过多种方式截取屏幕截图。

## 通过DevEco Studio截屏

1. 连接真机设备或模拟器，并在其中运行应用。
2. 在DevEco Studio底部切换到**Log**页签。
3. 点击左侧工具栏中![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3b/v3/5hgYe-kORNKw0b2pMNGonw/zh-cn_image_0000002602186613.png?HW-CC-KV=V1&HW-CC-Date=20260611T072926Z&HW-CC-Expire=86400&HW-CC-Sign=14AA841EA8EB832E90A7553FB041E2569004B965F513B81A285E14A045CDB9C8)，即可截取屏幕截图。

   截图的图片将直接显示在DevEco Studio中。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dc/v3/Ek0tw6xURDuc36hh9ovE9g/zh-cn_image_0000002602186593.png?HW-CC-KV=V1&HW-CC-Date=20260611T072926Z&HW-CC-Expire=86400&HW-CC-Sign=B00C2A5EE4C6B27BE78D3D95CB27B63D3AAE94302D8EE55947739BB88358ABB8)
4. （可选）在图片显示区域右击，选择**Copy Path/Reference...**可以查看截屏的本地存储路径或者在菜单栏下方查看本地存储路径。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/95/v3/q4m1JDfLQbOZamCK8fno2A/zh-cn_image_0000002571387424.png?HW-CC-KV=V1&HW-CC-Date=20260611T072926Z&HW-CC-Expire=86400&HW-CC-Sign=F762B7357494E88BADDA7ADF9A71D82D75E4C5976EE373524D084044211B84EE)

## 通过命令行方式截屏

hdc是可以用于调试的命令行工具，通过该工具可以实现截屏功能。更多关于命令行工具hdc的说明请参见[hdc工具使用指导](../../../系统/调测调优/调试命令/hdc/hdc.md)。

### 方式一：hdc shell snapshot\_display

```
1. hdc shell snapshot_display -f /data/local/tmp/0.jpeg  // -f参数指定图片在设备上的存储路径，如不指定，会在命令执行完成后显示图片默认存储路径。
2. hdc file recv /data/local/tmp/0.jpeg  // 将图片从设备发送到本地目录，本示例将图片发送到当前执行hdc命令的目录。
```

### 方式二：hdc shell wukong special -p

wukong是系统稳定性测试工具，通过指定参数-p可以实现截图功能。更多关于稳定性测试工具wukong的说明请参见[wukong工具使用指导](../../../应用测试/专项测试/命令行工具/wukong稳定性工具使用指导/wukong-guidelines.md)。

```
1. hdc shell wukong special -p
```

命令执行效果如下图所示，其中Report currentTestDir为结果存储路径，包含截屏图片。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e9/v3/AE6W_frKTbyD6UvUKUooTw/zh-cn_image_0000002602186597.png?HW-CC-KV=V1&HW-CC-Date=20260611T072926Z&HW-CC-Expire=86400&HW-CC-Sign=CC853CE7B1327DE52DD19043E1681F49C5406DFDC245BC2989B52897BB548ED5)

通过hdc命令可以将该路径文件发送到本地，例如发送到当前执行hdc命令的目录。

```
1. hdc file recv /data/local/tmp/wukong/report/20231010_141610/
```
