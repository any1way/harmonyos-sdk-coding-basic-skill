---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-development-environment-3
title: 导入Sample时，提示SSL证书校验错误
breadcrumb: FAQ > DevEco Studio > 环境准备 > 导入Sample时，提示SSL证书校验错误
category: harmonyos-faqs
scraped_at: 2026-06-12T10:40:07+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:2147bd1bfd2a73a323e8a141d1f66adf5b22082a3ee15ebb44c759940fe9f677
---

**问题现象**

导入Sample时，导入失败，提示“SSL certificate problem: unable to get local issuer certificate”证书校验错误。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4e/v3/Md82m9xbTzi_pp_-pwNhKg/zh-cn_image_0000002194318052.png?HW-CC-KV=V1&HW-CC-Date=20260612T024006Z&HW-CC-Expire=86400&HW-CC-Sign=48DF5924BEB1FFD92A4BC5FFEB169071F6F8B74D1F9EB92F8FFED7E38946B867)

**解决措施**

出现这个错误可能是网络遭受了攻击，或者你的网络提供方网络策略阻止了相关操作，如果你确认所处的网络环境安全，可以临时关闭证书校验以获取Sample。

1. 进入Git安装目录（默认为C:\Program Files\Git），双击运行“git-cmd.exe”文件。
2. 在打开的命令行窗口中，执行如下命令关闭SSL证书校验功能。

   说明

   关闭SSL证书校验，可能会带来安全风险，建议导入完Sample后，及时开启。开启方法：将该命令中的false修改为true即可。

   ```
   1. git config --global http.sslVerify false
   ```
3. 执行完成后，请重新尝试导入Sample。
