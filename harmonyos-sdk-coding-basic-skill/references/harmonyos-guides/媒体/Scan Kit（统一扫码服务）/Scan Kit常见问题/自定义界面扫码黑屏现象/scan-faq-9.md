---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/scan-faq-9
title: 自定义界面扫码黑屏现象
breadcrumb: 指南 > 媒体 > Scan Kit（统一扫码服务） > Scan Kit常见问题 > 自定义界面扫码黑屏现象
category: harmonyos-guides
scraped_at: 2026-06-01T14:55:14+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:d9c143831912a791449038cfaa05a7bd913e266796aa1a0c9c3ee357ee791e24
---
**问题现象**

自定义启动相机却显示黑屏现象。

**解决措施**

* 权限校验错误码：201，没有申请相机权限，[向用户申请授权](../../../../系统/安全/程序访问控制/应用权限管控/申请应用权限/向用户申请授权/request-user-authorization.md)。
* 参考ArkTS API错误码[1000500001](<../../../../../harmonyos-references/Scan Kit（统一扫码服务）/ArkTS API/ArkTS API错误码/scan-error-code.md#section1000500001-内部错误>)：如首次未调用customScan.[init](<../../../../../harmonyos-references/Scan Kit（统一扫码服务）/ArkTS API/customScan (自定义界面扫码)/scan-customscan-api.md#customscaninit>)初始化，直接调用customScan.[start](<../../../../../harmonyos-references/Scan Kit（统一扫码服务）/ArkTS API/customScan (自定义界面扫码)/scan-customscan-api.md#customscanstart-1>)启动扫码相机流，请参考自定义界面扫码的[业务流程](../../自定义界面扫码/scan-customscan.md#业务流程)。
