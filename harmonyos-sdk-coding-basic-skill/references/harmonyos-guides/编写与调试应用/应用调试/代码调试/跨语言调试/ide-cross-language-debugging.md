---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-cross-language-debugging
title: 跨语言调试
breadcrumb: 指南 > 编写与调试应用 > 应用调试 > 代码调试 > 跨语言调试
category: harmonyos-guides
scraped_at: 2026-06-11T15:29:16+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:2fe4d07ecbba88e18b2fad4d4ce59a6d4194d5c9eb8c71099c3f024c2e9f6d26
---
DevEco Studio支持C++和ArkTS的跨语言调试，可以同时调试这两种语言。整体操作体验与单一语言调试一致，无需额外在对应语言去手动添加断点，提升了使用两种语言混合开发的调试效率。

1. 将DevEco Studio与设备进行连接。如果使用真机设备，请先对应用/元服务进行签名，具体请参考[为应用/元服务进行签名](../../../配置调试签名/ide-signing.md)。
2. 在菜单栏单击**Run > Edit Configurations**，选择**Application**下的模块名（如entry），然后在右侧窗口中选择**Debugger**，将**Debug type**设置为“Dual(ArkTS/JS + Native)”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cd/v3/LOJAfnM0QqCyyA0E0ByrMw/zh-cn_image_0000002602066569.png?HW-CC-KV=V1&HW-CC-Date=20260611T072916Z&HW-CC-Expire=86400&HW-CC-Sign=876BD31F02FF7744F8A1198D7E7420509A5FDC7C17498E5C589371D9C6C8C6B4)
3. 代码调试执行到ArkTS调用C++方法处，点击Step Into可以进入到对应的C++方法的第一行代码处。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dc/v3/qLp6tfa9SYacngwR4TFqwA/zh-cn_image_0000002571387454.png?HW-CC-KV=V1&HW-CC-Date=20260611T072916Z&HW-CC-Expire=86400&HW-CC-Sign=88109A4D4F5EEFCEB01F4ACF65C54A0BD493BC9B67DEA3780DE97A5F721D9EBA)

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/18/v3/8hCs-GsHSZSmAfrhh9KSCw/zh-cn_image_0000002571387450.png?HW-CC-KV=V1&HW-CC-Date=20260611T072916Z&HW-CC-Expire=86400&HW-CC-Sign=0EED6231F8EFF7E69476AB9AD01313EC26BA46952D6CD716EEDA334F2C35F4B6)
4. 进入到C++代码后，可以从左下角Frames区域查看C++的调用栈，如需查看对应的ArkTS调用栈，在Frames区域中单击鼠标右键，勾选**Show ArkTs Stack Frame。**点击调用栈可以跳转到对应的代码行。

   说明

   从DevEco Studio 6.0.0 Beta3版本开始，支持查看ArkTS变量，其他变量相关的操作暂不支持。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/86/v3/wNYvP_yDSuiudaGOtLt99A/zh-cn_image_0000002602186623.png?HW-CC-KV=V1&HW-CC-Date=20260611T072916Z&HW-CC-Expire=86400&HW-CC-Sign=F2260E0E28DAA79752515012C0E31E6E1FA214CDE5FFF8ED9E88DA5F9F7DF96B)
5. ArkTS调用C++方法之后的代码存在断点时，点击Resume可以回到下一个ArkTS断点处，继续进行ArkTS代码调试。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/20/v3/50_w5x0WTqiEBuPMsQghfA/zh-cn_image_0000002602066567.png?HW-CC-KV=V1&HW-CC-Date=20260611T072916Z&HW-CC-Expire=86400&HW-CC-Sign=000363FA7806249575EA5CBEFE62740123253F5795B0D4F28F55642ED26C964D)
