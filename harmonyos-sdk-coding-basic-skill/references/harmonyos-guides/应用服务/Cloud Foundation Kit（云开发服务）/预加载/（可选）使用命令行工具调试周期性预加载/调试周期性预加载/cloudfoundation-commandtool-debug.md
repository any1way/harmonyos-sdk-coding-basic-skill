---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cloudfoundation-commandtool-debug
title: 调试周期性预加载
breadcrumb: 指南 > 应用服务 > Cloud Foundation Kit（云开发服务） > 预加载 > （可选）使用命令行工具调试周期性预加载 > 调试周期性预加载
category: harmonyos-guides
scraped_at: 2026-06-11T15:06:13+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:d21779cd62a88891b49355b68753b920ed5009f76beb99a5649b0cc663f81bcf
---
prefetch\_test\_tool是为周期性预加载功能提供的一种命令行工具，开发者集成预加载服务后，使用该工具可以更方便、更高效地进行周期性预加载功能测试和调试，提高开发效率，同时确保预加载服务的平稳运行。

当前命令行工具支持的命令集如下：

| 命令名 | 描述 |
| --- | --- |
| [getcache](cloudfoundation-commandtool-debug.md#调试命令) | 提供获取周期性预加载数据的能力。 |

## 调试准备

使用命令行工具调试周期性预加载之前，需要完成以下准备工作：

* 您已在开发者联盟官网注册账号并通过实名认证，详情请参见[账号注册认证](https://developer.huawei.com/consumer/cn/doc/start/registration-and-verification-0000001053628148)。
* 您已在本地安装DevEco Studio 5.0.3 Release及以上版本。
* 手机/平板终端设备的ROM版本已升级至HarmonyOS 6.0.0 Beta5及以上版本。
* 设置HAP包的“Build Mode”为“debug”，且已[申请调试证书](https://developer.huawei.com/consumer/cn/doc/app/agc-help-debug-cert-0000002283256797)。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f2/v3/QSGxA9TlRS-el9g1MxQyEQ/zh-cn_image_0000002622698869.png?HW-CC-KV=V1&HW-CC-Date=20260611T070612Z&HW-CC-Expire=86400&HW-CC-Sign=3C2CE4E2C25F8B6E346D16AE80C85F1CBC5B6BEDA4E78235D0D18B32F77ACBE8)

## 切换shell环境

prefetch\_test\_tool命令行工具基于hdc shell调试，需要切换到hdc shell命令环境。

1. PC连接调试设备。连接方式请根据实际情况选择，详情请参见[设备连接管理](../../../../../系统/调测调优/调试命令/hdc/hdc.md#设备连接管理)。
2. 打开DevEco Studio，菜单栏选择“View > Tool Windows > Terminal”进入Terminal窗口。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bb/v3/YU_jXkMnRwqNZR6d53eJrg/zh-cn_image_0000002592219308.png?HW-CC-KV=V1&HW-CC-Date=20260611T070612Z&HW-CC-Expire=86400&HW-CC-Sign=DDBD45BB02108C7E490D23F0790FC99CAC98A94C5DC92CD0B737639E8E0430DE)
3. 输入hdc shell，切换到hdc shell命令环境。切换过程中如果出现报错，请参见[常见问题](../../../../../系统/调测调优/调试命令/hdc/hdc.md#常见问题)排查解决。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f6/v3/XtAWf_FRTtuAOmZS-1AG_Q/zh-cn_image_0000002592379242.png?HW-CC-KV=V1&HW-CC-Date=20260611T070612Z&HW-CC-Expire=86400&HW-CC-Sign=BB75946C5EAC76ACC6E98D9CEFCB1FD4CE5C58C64783A0921EB8C9CDFF245813)

## 调试命令

命令名“getcache”，提供获取周期性预加载数据的能力。

### 命令格式

```
1. cf_prefetch getcache -m <bundlename>
```

### 命令选项

| 命令选项 | 必填(M)/选填(O) | 描述 | 示例 |
| --- | --- | --- | --- |
| -m | M | 应用包名。此处的包名需要与您在AppGallery Connect中创建应用时配置的包名保持一致。 | cf\_prefetch getcache -m com.huawei.hms.xs.test |

## 调用示例

### 正常场景

* 输入cf\_prefetch help，获取命令行工具的使用说明。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cd/v3/08l8TkDnSTaEza9VbKG3Mg/zh-cn_image_0000002622858751.png?HW-CC-KV=V1&HW-CC-Date=20260611T070612Z&HW-CC-Expire=86400&HW-CC-Sign=BE3E672742932CC2CA74AD01B354D84061F49CFF6E42D66C55BD6980FA96E1DD)
* 输入cf\_prefetch getcache -h，获取getcache命令支持的参数信息。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/21/v3/nH0BcpsRQXSNzZ04DGgLfA/zh-cn_image_0000002622698871.png?HW-CC-KV=V1&HW-CC-Date=20260611T070612Z&HW-CC-Expire=86400&HW-CC-Sign=D31B09093443C01D3AE092EE7FBE4AF1A653CE1AEA9F417860FECCA8EF469EE6)
* 输入cf\_prefetch getcache -m <bundlename>，立即向云侧请求获取一次周期性预加载数据。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/56/v3/Ej_OXDtcSFqI8dK-uwG5TQ/zh-cn_image_0000002592219310.png?HW-CC-KV=V1&HW-CC-Date=20260611T070612Z&HW-CC-Expire=86400&HW-CC-Sign=581693B0ABD0065969BF2FFE05276C9971934C4C17D4E5C273DDDF74B419D357)

  说明

  如果返回结果中的“fetch data timestamp”不是当前时间，则表示仍为上一次成功拉取数据的时间戳，此次数据拉取失败，请参见[异常场景](cloudfoundation-commandtool-debug.md#异常场景)排查。

### 异常场景

* 链路不通，例如无网络情况；或周期性预加载配置不正确。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/62/v3/ZylrPW9ERLyzEc7lX0J6YQ/zh-cn_image_0000002592379244.png?HW-CC-KV=V1&HW-CC-Date=20260611T070612Z&HW-CC-Expire=86400&HW-CC-Sign=B6507207697B79978491EC22C9A4EC1D5AB37A5C3EEBA00F3A8982D7D5FC5F5A)
* 命令行工具内部错误。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e5/v3/vMdAPaFHQua2qHqrrXSUHQ/zh-cn_image_0000002622858753.png?HW-CC-KV=V1&HW-CC-Date=20260611T070612Z&HW-CC-Expire=86400&HW-CC-Sign=A7CCB3D76F9F9963E6178E83C179A272901CF06BA96382F9293798FD0B9BFF6C)
* HAP包非debug调试模式。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c6/v3/0wa4DPPsSXm2iTE06tZMeQ/zh-cn_image_0000002622698873.png?HW-CC-KV=V1&HW-CC-Date=20260611T070612Z&HW-CC-Expire=86400&HW-CC-Sign=0F5965E92AEB8B2239E5E42F95E491104571ACE2D2036530855BD6C1E6712583)
* 应用包名输入错误。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/47/v3/LoDKe4plQgWtNXKUVOmO7g/zh-cn_image_0000002592219312.png?HW-CC-KV=V1&HW-CC-Date=20260611T070612Z&HW-CC-Expire=86400&HW-CC-Sign=8FC75150E20D270501CD72A74DBCF68EE9893111EF2912E34B685F20790CCB50)
