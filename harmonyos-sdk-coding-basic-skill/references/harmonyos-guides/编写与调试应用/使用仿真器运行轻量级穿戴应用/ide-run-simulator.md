---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-run-simulator
title: 使用仿真器运行轻量级穿戴应用
breadcrumb: 指南 > 编写与调试应用 > 使用仿真器运行轻量级穿戴应用
category: harmonyos-guides
scraped_at: 2026-06-11T15:28:32+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:5783afcc65623ba9eff71b72f9eec69a37719053ccfe6cdae807bc956b3d5a69
---
DevEco Studio提供的**Simulator**可以运行和调试Lite Wearable设备上的HarmonyOS应用，兼容签名与不签名两种类型的HAP。

## 操作步骤

1. 在DevEco Studio右上角的设备框中选择**Huawei Lite Wearable Simulator。**

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/37/v3/WGD_0nKeRZW0VirPj-p2Jg/zh-cn_image_0000002571546556.png?HW-CC-KV=V1&HW-CC-Date=20260611T072831Z&HW-CC-Expire=86400&HW-CC-Sign=9C38B8CA7BA6CD165AEA8D49A9E619DA9B7BB638CCE3B10D7AF5A7C578400960)
2. 点击**Run** ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2d/v3/lHhIFtf7QVamc7NG6ShQTA/zh-cn_image_0000002571546564.png?HW-CC-KV=V1&HW-CC-Date=20260611T072831Z&HW-CC-Expire=86400&HW-CC-Sign=A6F0F4850C813AC72343DDB11C52CCFDF95B4F2409AF0C3FA891680960A8BC5D)或**Debug** ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2f/v3/UMfBd_BLQsCuAD5pAQBdug/zh-cn_image_0000002571386924.png?HW-CC-KV=V1&HW-CC-Date=20260611T072831Z&HW-CC-Expire=86400&HW-CC-Sign=0BC7B4805859ACD697E21A7C47D322E972ED67C02A1C89681EC878A6D7BE2B3A)按钮，在弹框中选择设备形状和分辨率，点击**OK**按钮，开始运行或调试应用。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/72/v3/4aIIaEsdRbiauv3SLa3UWg/zh-cn_image_0000002602066037.png?HW-CC-KV=V1&HW-CC-Date=20260611T072831Z&HW-CC-Expire=86400&HW-CC-Sign=6D275CCD4880212116E5F14ECC20DA5557A0C3085F200F22E32914B68EE87637 "点击放大")
3. DevEco Studio会启动编译构建和安装，完成后应用即可运行在Simulator上。

## 功能介绍

在Simulator界面中，点击设备上方的**More**可展开更多功能。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9f/v3/Z7x2NvBDRC6DM_kxI8twCQ/zh-cn_image_0000002571546560.png?HW-CC-KV=V1&HW-CC-Date=20260611T072831Z&HW-CC-Expire=86400&HW-CC-Sign=E36DDEFAF585875A2F94CA367F218BBE4AAE3478EAC1ED7F3A3BE36CA19697FC)

### 屏幕

* **Turn screen on：**控制屏幕开关。
* **Keep screen on：**控制屏幕是否保持常亮状态。关闭开关时，息屏计时结束后，屏幕自动关闭，同时**Turn screen on**开关自动关闭。开启屏幕后，打开**Keep screen on**开关才能使屏幕常亮。
* **Brightness adjustment mode：**调节屏幕亮度。
  + **Manual：**手动调节，可拖动滑动条，或直接输入亮度。

    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/79/v3/lqZTCi8HR_e9BB2ulT3hnQ/zh-cn_image_0000002602186097.png?HW-CC-KV=V1&HW-CC-Date=20260611T072831Z&HW-CC-Expire=86400&HW-CC-Sign=58F5E217CCEF917DEA5DF9D57A7B77F2A328990BFF0E5C46AED4526EA844C1E0)
  + **Automatic：**自动调节。
* **Resolution：**运行/调试模式下暂不支持调整分辨率，如需调整，请停止运行后，按照[操作步骤](ide-run-simulator.md#section1332819367496)选择分辨率。

### 传感器

仿真器提供了虚拟传感器来模拟硬件传感器的能力。在该界面，您可以调节不同的传感器来测试您的应用，使用[@system.sensor](<../../../harmonyos-references/Sensor Service Kit（传感器服务）/ArkTS API/@system.sensor (传感器)/js-apis-system-sensor.md>)模块监听传感器值的变化，使用[@system.geolocation](<../../../harmonyos-references/Location Kit（位置服务）/ArkTS API/已停止维护的接口/@system.geolocation (地理位置)/js-apis-system-location.md>)模块监听地理位置的变化。仿真器提供以下虚拟传感器：

* **On-body status**：传感器所在设备穿戴状态，包括已穿戴和未穿戴。
* **Barometer：**气压传感器用于测量环境气压，单位为Pa。
* **Heart rate：**心率传感器用于测量心率数值，拖动滑动条，或直接输入心率大小。
* **Step count：**计步传感器用于统计行走步数，拖动滑动条，或直接输入步数。
* **Geographic location：**输入经度、纬度，模拟设备所处的地理位置。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/94/v3/OUCn_9jrSIuF21cPvHunDg/zh-cn_image_0000002602066041.png?HW-CC-KV=V1&HW-CC-Date=20260611T072831Z&HW-CC-Expire=86400&HW-CC-Sign=CB42D5C77C8852B0B2003C5A7B20DF12F1A2DDC838B4B9EF6625F9962541EF64)

### 电池

您可以通过仿真器模拟不同的电池状态，包括以下三种充电状态，也可以手动输入或拖动滑动条来改变电量大小。在应用中，您可以通过[@system.battery](<../../../harmonyos-references/基础功能/Basic Services Kit（基础服务）/ArkTS API/已停止维护的接口/@system.battery (电量信息)/js-apis-system-battery.md>)模块查询仿真器的剩余电量以及充电状态。

* Not charging：未充电。
* Charging：正在充电。
* Wireless charging：无线充电。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c3/v3/aVUhI_XTS2K7R4nsHntieA/zh-cn_image_0000002571386922.png?HW-CC-KV=V1&HW-CC-Date=20260611T072831Z&HW-CC-Expire=86400&HW-CC-Sign=017BAB6C18C0896E0DDB262CFAA791380CC48705ED67ABD321538A09E63D0718)

### 设备设置

您可以更改设备的语言和地区，当前仅运行模式可以更改，调试模式暂不支持。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/32/v3/m7nf4Wv-S3mhxNKouLnmFQ/zh-cn_image_0000002602066039.png?HW-CC-KV=V1&HW-CC-Date=20260611T072831Z&HW-CC-Expire=86400&HW-CC-Sign=2E73F571904E3B142FB8DFBA075BFC8EF4F2D2244C0AE013A7E39CCFB3A3CAB3)

### 调试

* **Screen coordinate system****：**开启屏幕坐标系后，将光标移动到表盘上时，会显示屏幕坐标。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/81/v3/qn8VAx7lTWeuIhcx1uBi_g/zh-cn_image_0000002571546562.gif?HW-CC-KV=V1&HW-CC-Date=20260611T072831Z&HW-CC-Expire=86400&HW-CC-Sign=C258C16964D57F2DF524EDD09CFF594D144651F888A52E7CF867A30819D92053 "点击放大")
* **Show device mask****：**关闭开关后，表盘周围的表冠颜色淡化。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/37/v3/FEDSvuE4QD-veDRyhJcuBg/zh-cn_image_0000002602186095.gif?HW-CC-KV=V1&HW-CC-Date=20260611T072831Z&HW-CC-Expire=86400&HW-CC-Sign=50D6F910AA055A2861C3BB4305866B0728481069805FBF91338FF87EF6C24ABB "点击放大")
