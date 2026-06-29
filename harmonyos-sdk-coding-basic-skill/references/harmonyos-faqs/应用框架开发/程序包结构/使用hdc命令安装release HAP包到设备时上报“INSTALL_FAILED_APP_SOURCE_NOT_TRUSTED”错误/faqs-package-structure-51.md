---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-package-structure-51
title: 使用hdc命令安装release HAP包到设备时上报“INSTALL_FAILED_APP_SOURCE_NOT_TRUSTED”错误
breadcrumb: FAQ > 应用框架开发 > 程序包结构 > 使用hdc命令安装release HAP包到设备时上报“INSTALL_FAILED_APP_SOURCE_NOT_TRUSTED”错误
category: harmonyos-faqs
scraped_at: 2026-06-01T17:03:56+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:09c7ce5d024435fb20f1fd9ff56cfe7001be40e4e81081beb750087154fd561d
---
**问题现象**

release HAP包用hdc命令安装到手机上时报错："INSTALL\_FAILED\_APP\_SOURCE\_NOT\_TRUSTED"。

**解决措施**

AGC发布的证书仅支持上架使用，不支持本地安装。签名中心只为预置应用申请Profile，不支持本地调试。

**参考链接**

[调试概述](../../../../harmonyos-guides/编写与调试应用/应用调试/调试概述/ide-debug-device.md)
