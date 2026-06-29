---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-running-40
title: 设备管理获取模板数据提示网络异常，下载模拟器镜像提示网络异常
breadcrumb: FAQ > DevEco Studio > 应用运行 > 设备管理获取模板数据提示网络异常，下载模拟器镜像提示网络异常
category: harmonyos-faqs
scraped_at: 2026-06-12T10:44:33+08:00
doc_updated_at: 2026-06-05
content_hash: sha256:a5163bf62030bd48ddb6a0990a3f52250a1692af031a8c44a95d163f298feada
---
**问题现象**

* **场景一**：设备管理获取模板数据失败，错误提示：“Network request failed. Verify your network connection and Emulator is available in your country/region.”

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d2/v3/38gPOnKdSmydDkZSs23vbg/zh-cn_image_0000002194318324.png?HW-CC-KV=V1&HW-CC-Date=20260612T024432Z&HW-CC-Expire=86400&HW-CC-Sign=709563C852861ACDAB2DE5DED3C0BD1516BB249F1746C57F98E79374554B99F0)
* **场景二**：模拟器镜像下载失败，提示“The network or server is abnormal.”。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/59/v3/QrpIcz5eTg2t5oGhPMGBgw/zh-cn_image_0000002229758585.png?HW-CC-KV=V1&HW-CC-Date=20260612T024432Z&HW-CC-Expire=86400&HW-CC-Sign=B2236E2D42EE19003C922778D39C30E2E5ADC6E42FB90DCFF4A25C9066AE7E2D)
* **场景三**：打开设备管理，界面显示为空，错误提示：“Network request failed. Verify your network connection and Emulator is available in your country/region.”

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/84/v3/q6g7JPs5REahHCeL-7ieBg/zh-cn_image_0000002313594524.png?HW-CC-KV=V1&HW-CC-Date=20260612T024432Z&HW-CC-Expire=86400&HW-CC-Sign=29B133ECA80AAEADDB309E95751563EBD86C225461B9E882D2F7942D4931752D)

**解决措施**

1. 尝试清除本机DevEco Studio缓存文件后重启，缓存目录：

   Windows:C:\Users\xxx\AppData\Local\Huawei\DevEcoStudioX.X\caches

   Mac：~/Library/Caches/Huawei/DevEcoStudioX.X/caches
2. 尝试修改本机网络环境后进行重试，例如：[配置Proxy代理](../../../../harmonyos-guides/编写与调试应用/附录/配置代理/ide-environment-config.md#section10369436568)、连接手机热点、关闭VPN。
3. 请检测您的网络并确认您当前电脑环境或华为账号是否在[模拟器支持的国家/地区](../../../../harmonyos-guides/编写与调试应用/使用模拟器运行应用/概述/设备支持类型/ide-emulator-devicetype.md)内。
