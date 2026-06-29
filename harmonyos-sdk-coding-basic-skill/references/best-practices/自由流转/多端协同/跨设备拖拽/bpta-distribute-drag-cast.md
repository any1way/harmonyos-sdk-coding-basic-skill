---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-distribute-drag-cast
title: 跨设备拖拽
breadcrumb: 最佳实践 > 自由流转 > 多端协同 > 跨设备拖拽
category: best-practices
scraped_at: 2026-06-12T10:12:32+08:00
doc_updated_at: 2026-05-18
content_hash: sha256:6302744903fbc3c59e6fa297955db8ef96deb3ceda79a6c9af0335309d8478e7
---
跨端拖拽提供跨设备的键鼠共享能力，支持在平板或2in1类型的任意两台设备之间拖拽文本、图片、视频、PDF文档等文件。

例如，当用户拥有两台平板设备时，可以共享一套键鼠，通过跨设备拖拽，一步将设备A的素材拖拽到设备B快速创作，实现跨设备的协同工作体验。

当前系统应用中，文件管理器、浏览器支持拖出；备忘录支持拖入。用户可以体验以下场景：

* 将A设备文件管理器中的图片拖拽至B设备的备忘录应用。
* 将A设备备忘录中的文本拖拽至B设备的备忘录应用，并在B设备中使用A设备连接的键盘输入，协同操作。

开发者可以根据实际需求，实现组件的拖入或拖出，即可接入跨设备拖拽。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b0/v3/3DwWM7kxQ8SDCZnkaCaHtg/zh-cn_image_0000002593676861.gif?HW-CC-KV=V1&HW-CC-Date=20260612T021231Z&HW-CC-Expire=86400&HW-CC-Sign=4DB835AD71634743DFD1DB3B562809091A245864FC206D5D8547ADC6357E7A11 "点击放大")

## 运作机制

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cb/v3/NfcL9dEzRbyso1gaXPkCcw/zh-cn_image_0000002563037188.png?HW-CC-KV=V1&HW-CC-Date=20260612T021231Z&HW-CC-Expire=86400&HW-CC-Sign=38D06F3AA258474BCC75FC4626E49DD08585B647ECA5C650645990216334439E "点击放大")

1. 用户使用鼠标点击组件，触发拖拽事件。
2. 应用设置拖拽数据。
3. 系统完成跨设备数据处理，此过程应用不感知。
4. 用户松手触发拖拽松手事件。
5. 目的端应用获取并处理拖拽数据。

## 约束与限制

需同时满足以下条件，才能使用该功能：

* **设备限制**

  HarmonyOS NEXT Developer Preview0及以上版本的平板或2in1设备。
* **使用限制**
  + 双端设备需要登录同一华为账号。
  + 双端设备需要打开Wi-Fi和蓝牙开关，并接入同一个局域网。
  + 打开键鼠穿越开关。
  + 应用本身预置的资源文件（即应用在安装前的HAP包中已经存在的资源文件）不支持跨设备拖拽。

## 接口说明

在开发具体功能前，请先查阅参考文档，获取详细的接口说明。

* [拖拽控制](../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/通用属性/交互属性/拖拽控制/ts-universal-attributes-drag-drop.md)：设置组件是否可以响应拖拽事件的属性。组件均需要设置draggable属性才能响应拖拽事件。

  当前部分组件默认支持拖拽控制。应用使用这些组件时，只需要将draggable设置为true，系统将根据组件的支持情况，自动实现onDragStart的写信息或onDrop的读信息。
* [拖拽事件](../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/通用事件/交互响应事件/拖拽事件/ts-universal-events-drag-drop.md)：组件被鼠标选中后拖拽时触发的事件。

  应用应根据实际需求，实现组件拖入或拖出。

## 开发示例

拖拽事件通过鼠标左键来操作和响应，开发示例请参考：[拖拽事件](../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/通用事件/交互响应事件/拖拽事件/ts-universal-events-drag-drop.md)。
