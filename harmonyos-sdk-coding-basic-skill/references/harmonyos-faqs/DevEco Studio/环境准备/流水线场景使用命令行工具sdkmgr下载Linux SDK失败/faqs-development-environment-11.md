---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-development-environment-11
title: 流水线场景使用命令行工具sdkmgr下载Linux SDK失败
breadcrumb: FAQ > DevEco Studio > 环境准备 > 流水线场景使用命令行工具sdkmgr下载Linux SDK失败
category: harmonyos-faqs
scraped_at: 2026-06-12T10:40:13+08:00
doc_updated_at: 2026-06-05
content_hash: sha256:c71a09569ed0b2a8662902cea3d9e3a545c7bb0975aa822c4130e870b3330f38
---

**问题现象**

在Linux上使用命令行工具sdkmgr时，如果提示“Failed to request URL https://devecostudio-dre.op.hicloud.com/sdkmanager/v5/hos/getSdkList”。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1c/v3/bwsvfm0VSVKIgp1Hhx33qw/zh-cn_image_0000002194158336.png?HW-CC-KV=V1&HW-CC-Date=20260612T024011Z&HW-CC-Expire=86400&HW-CC-Sign=21961EB35B68146DBA88C1EE31C48C28735BBB72CBDC27F195904F5AC019F215)

**解决措施**

该问题通常是因为Linux的国家码未设置为中国区。

1. 进入sdkmgr所在的目录。

   ```
   1. cd ${命令行工具根目录}/sdkmanager/bin
   ```

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a4/v3/41MTVJRdQdaElfHTsWxbBQ/zh-cn_image_0000002229603729.png?HW-CC-KV=V1&HW-CC-Date=20260612T024011Z&HW-CC-Expire=86400&HW-CC-Sign=16FA8E466FB44B3B6D026B4C7E5CBD79452E4CBC151CA517CFE54EBB73736E1B)
2. 打开sdkmgr文件。

   ```
   1. vim sdkmgr
   ```

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/20/v3/iDj09btTSQK9mOae3YhidA/zh-cn_image_0000002229758205.png?HW-CC-KV=V1&HW-CC-Date=20260612T024011Z&HW-CC-Expire=86400&HW-CC-Sign=D6431F0E8BEBCBBDCBD1A63FA4EFA8D9172FBFC91800A594267F8396781CEADD)
3. 在sdkmgr文件的最后一行“-Dfile.encoding=UTF-8”后添加国家码“-Duser.country=CN”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/44/v3/yt-eGWVhROCioCvP4T009w/zh-cn_image_0000002194317952.png?HW-CC-KV=V1&HW-CC-Date=20260612T024011Z&HW-CC-Expire=86400&HW-CC-Sign=7B34744A94CBE861A0395518F26F1BC026AC17DCE69F38E6393C75437D765ED0)
4. ​保存修改后，再次执行sdkmgr相关命令即可正常下载Linux SDK。
