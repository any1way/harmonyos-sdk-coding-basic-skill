---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-76
title: 如何解决搭建流水线时commandline-tools-linux中sdkmgr下载开发包报错
breadcrumb: FAQ > DevEco Studio > 编译构建 > 如何解决搭建流水线时commandline-tools-linux中sdkmgr下载开发包报错
category: harmonyos-faqs
scraped_at: 2026-06-12T10:42:05+08:00
doc_updated_at: 2026-06-05
content_hash: sha256:b7bb31298f5ffba8bf7e19f57f3a89e7bd98bd8cfaa1a1df5e6fb570e22d1e68
---

**问**

使用 commandline-tools 工具在 Linux 上时，如果提示“Failed to request URL https://devecostudio-dre.op.hicloud.com/sdkmanager/v5/hos/getSdkList”，请检查网络连接是否正常，确保可以访问该 URL。如果网络无问题，尝试更新 commandline-tools到最新版本。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4f/v3/JtaldNpjTT2Sk9BSGuRdKA/zh-cn_image_0000002229603881.png?HW-CC-KV=V1&HW-CC-Date=20260612T024203Z&HW-CC-Expire=86400&HW-CC-Sign=C05942C36DDD41C22D18930C5D7365245298EFD42E93D7461595D3405A520479 "点击放大")

**解决措施**

该问题通常是因为Linux的国家码未设置为中国区所致。

请参考以下方法解决：

1. 进入sdkmgr脚本所在的文件夹：${命令行工具根目录}/sdkmanager/bin。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/52/v3/6wzrZAKKTfWd18OaGIguGQ/zh-cn_image_0000002194158460.png?HW-CC-KV=V1&HW-CC-Date=20260612T024203Z&HW-CC-Expire=86400&HW-CC-Sign=5C138E04EB9021F12FDF643514954F6A7A163D1A9077D99F138247E04113DF2E "点击放大")
2. 打开sdkmgr文件。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3f/v3/pNJVG0kZRxiXKazsfO7Bbg/zh-cn_image_0000002229603849.png?HW-CC-KV=V1&HW-CC-Date=20260612T024203Z&HW-CC-Expire=86400&HW-CC-Sign=A461E65818C07DD5E62CDEE6A9A099882E9B1AF3A6BD2F2DD9A0C0094000D323 "点击放大")
3. 在文件的最后一行，-Dfile.encoding=UTF-8 后面添加 -Duser.country=CN。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b5/v3/1XD8T4TzTtOp85jg3vlrqA/zh-cn_image_0000002194318088.png?HW-CC-KV=V1&HW-CC-Date=20260612T024203Z&HW-CC-Expire=86400&HW-CC-Sign=FE3E89F8029BB086076A093906A2FE1BF74EB6774E96132DB37F4C73AC3936B0 "点击放大")
4. 保存修改，再次执行sdkmgr相关命令即可。
