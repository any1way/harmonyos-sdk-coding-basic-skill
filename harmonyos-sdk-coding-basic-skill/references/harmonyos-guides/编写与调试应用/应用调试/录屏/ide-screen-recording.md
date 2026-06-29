---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-screen-recording
title: 录屏
breadcrumb: 指南 > 编写与调试应用 > 应用调试 > 录屏
category: harmonyos-guides
scraped_at: 2026-06-11T15:29:28+08:00
doc_updated_at: 2026-06-10
content_hash: sha256:84ddb91f36e1f5dc251b7e09a9014aeebdf6c4ccf311f66c056925d14064f66e
---
在应用开发过程中，可以使用录屏功能录制应用的运行状态，并通过录屏文件向他人展示正在开发的应用的各种功能效果。

## 使用约束

* 如果设置了锁屏密码，录屏开始前请解锁设备屏幕，锁屏状态下录屏应用无法正常拉起。
* 如果设置了锁屏密码，录屏时请保持设备的屏幕解锁状态，若录屏过程中锁屏将导致录屏应用退出。
* 模拟器不支持录屏。

## 通过DevEco Studio录屏

1. 连接真机设备，并在其中运行应用。
2. 在DevEco Studio底部切换到**Log**页签。
3. 点击左侧工具栏中![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5e/v3/pbQXhGHcTZKv-o6UVBnb8Q/zh-cn_image_0000002602186729.png?HW-CC-KV=V1&HW-CC-Date=20260611T072927Z&HW-CC-Expire=86400&HW-CC-Sign=CE614C5E1CD346562597A1BD3914CB628C1B83023887397EFAEC4FA2F14CF0C4)，即可开始录屏。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/31/v3/aBYPFk2xRpe7AOVOMgit_Q/zh-cn_image_0000002571547198.png?HW-CC-KV=V1&HW-CC-Date=20260611T072927Z&HW-CC-Expire=86400&HW-CC-Sign=0F8944A2F1712950B0C4E0B34819B92D1582D4040D1DC47109DB48F1E21A4105)
4. 录屏时，需要先选择录屏文件的保存路径，开发者可使用默认路径或[设置自定义路径](ide-screen-recording.md#section89111791511)。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c4/v3/bbQfBgOURGCWTD5UWn-xxA/zh-cn_image_0000002571387560.png?HW-CC-KV=V1&HW-CC-Date=20260611T072927Z&HW-CC-Expire=86400&HW-CC-Sign=1FD1C1ED324495277DF05BE83A2B2983DC667B231054F7A8ACD89867B96F9A8F)
5. 路径选择完毕后，点击**Start Recording**开始录屏。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e1/v3/u_B1_URHRhWI1KBYKAh1Sw/zh-cn_image_0000002602066679.png?HW-CC-KV=V1&HW-CC-Date=20260611T072927Z&HW-CC-Expire=86400&HW-CC-Sign=E40275B093B04B661B18D8F9177D38EE153D460661A1ECC66301B6B1284B2231 "点击放大")
6. 录制完操作流程之后，点击**Stop Recording**结束录屏。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/30/v3/UI3X-hGlTNyzh7Z9bKLppQ/zh-cn_image_0000002571387564.png?HW-CC-KV=V1&HW-CC-Date=20260611T072927Z&HW-CC-Expire=86400&HW-CC-Sign=4127C6B940A00AB86977612B9C34493C08473DCC96F929C7DBB958B1495C53EF "点击放大")
7. 结束录屏后，录屏文件将会保存到之前选择的路径下，可以选择调用系统播放器播放视频文件或打开文件所在的文件夹。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/04/v3/RLzCDNGwQoqdGKx9_pX43w/zh-cn_image_0000002571387558.png?HW-CC-KV=V1&HW-CC-Date=20260611T072927Z&HW-CC-Expire=86400&HW-CC-Sign=AAAD8D0BB587483B7DFF9726EEC999A156A6134959CF2BC5D05E9514FA15F934 "点击放大")

## 设置录屏自定义路径

1. 点击DevEco Studio底部**Log**页签，选择**HiLog >** **Settings** **>** **Record Screen**选项。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fe/v3/yvQmsyCAT5eKzeKAsw9IRw/zh-cn_image_0000002571387568.png?HW-CC-KV=V1&HW-CC-Date=20260611T072927Z&HW-CC-Expire=86400&HW-CC-Sign=8659421235F71B6EEF2E44D2950AA55214858CB724FFFC8E9FC0DC204532CC7E)
2. 在弹出的界面选择自定义路径，当设置好路径并勾选“Use the selected path and auto-generated file name as defaults and don't ask again”选项后，录屏时将自动使用此时设置的路径以及以录屏时的时间戳构造的文件名作为录屏文件的保存地址及文件名。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1c/v3/LJi1vS0gTWyvnnc_fdGuWQ/zh-cn_image_0000002602066683.png?HW-CC-KV=V1&HW-CC-Date=20260611T072927Z&HW-CC-Expire=86400&HW-CC-Sign=8F37EA902533F6E1909181A9B190A505103E9F518FA498778C3D51D39D01860B)

## 通过命令行方式录屏

hdc是可以用于调试的命令行工具，通过该工具可以实现录屏功能。更多关于命令行工具hdc的说明请参见[hdc工具使用指导](../../../系统/调测调优/调试命令/hdc/hdc.md)。

1. 启动录屏。

   ```
   1. hdc shell aa start -b com.huawei.hmos.screenrecorder -a com.huawei.hmos.screenrecorder.ServiceExtAbility --ps "CustomizedFileName" "test.mp4"   // 指定录屏文件名称为test.mp4
   ```
2. 停止录屏。

   ```
   1. hdc shell aa start -b com.huawei.hmos.screenrecorder -a com.huawei.hmos.screenrecorder.ServiceExtAbility
   ```
3. 获取录屏文件位置，记录为{RecordFile}。

   ```
   1. hdc shell mediatool query test.mp4 -u
   ```

   * 如果查询的结果中包含uri字段，则返回值第三行对应的录屏文件路径不允许直接下载。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/59/v3/eihTWmvpTe2FO2TNKPhkBQ/zh-cn_image_0000002602066685.png?HW-CC-KV=V1&HW-CC-Date=20260611T072927Z&HW-CC-Expire=86400&HW-CC-Sign=A13438D12B10B884A5B00B1EFEE81BB38B70C23DC9A2DBC3F2BE179DC6AA9772)

     需要再执行如下命令，指定该uri，将录屏文件复制到有下载权限的路径中（如/data/local/tmp）。

     ```
     1. hdc shell mediatool recv "file://media/Photo/2/VID_1736853237_001/test.mp4" /data/local/tmp
     ```

     命令返回值第二行即为录屏文件路径{RecordFile}。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c7/v3/1cDJa7JwQmOztJ3odXmLQQ/zh-cn_image_0000002571547202.png?HW-CC-KV=V1&HW-CC-Date=20260611T072927Z&HW-CC-Expire=86400&HW-CC-Sign=F634822C26092FD9CC07548AC4C15F6A1C4ED40F27798DF94A83F92A40AF61B8)
   * 如果查询结果不包含uri字段，则返回值第二行即为录屏文件路径{RecordFile}。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c6/v3/z1Oj_GX8RQao4i3lXmlE4w/zh-cn_image_0000002571387566.png?HW-CC-KV=V1&HW-CC-Date=20260611T072927Z&HW-CC-Expire=86400&HW-CC-Sign=BD0C5F54CA0622E12CD6748CDB03B47A4F143B4996FECFADB4C2E9C0CBF86115)
4. 指定上一个步骤中获取到的录屏文件路径{RecordFile}，下载录屏文件到本地。

   ```
   1. hdc file recv {RecordFile} d:\test.mp4
   ```
