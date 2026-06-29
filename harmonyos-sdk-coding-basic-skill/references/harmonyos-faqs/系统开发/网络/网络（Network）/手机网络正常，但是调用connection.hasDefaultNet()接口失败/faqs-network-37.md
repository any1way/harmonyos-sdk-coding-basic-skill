---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-network-37
title: 手机网络正常，但是调用connection.hasDefaultNet()接口失败
breadcrumb: FAQ > 系统开发 > 网络 > 网络（Network） > 手机网络正常，但是调用connection.hasDefaultNet()接口失败
category: harmonyos-faqs
scraped_at: 2026-06-12T10:37:39+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:cae473bff87308b26af76b59252c4e4a43740daabf52f1b35f1f5f0a5781e97a
---
**问题现象**

手机已连接互联网，浏览器可以正常访问网页，但调用hasDefaultNet方法时失败，回调函数进入了错误处理流程。

**原因**

未申请ohos.permission.GET\_NETWORK\_INFO权限。

**解决措施**

connection.hasDefaultNet接口需要申请ohos.permission.GET\_NETWORK\_INFO权限。在Stage模型中，开发者需在module.json5配置文件中声明该权限。参考代码如下：

```
1. {
2. "module": {
3. // ...
4. "requestPermissions": [
5. {
6. "name": "ohos.permission.GET_NETWORK_INFO",
7. "reason": "$string:reason",
8. "usedScene": {
9. "abilities": [
10. "FormAbility"
11. ],
12. "when": "inuse"
13. }
14. }
15. ]
16. }
17. }
```

[NetModule.json5](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/NetworkKit/entry/src/main/ets/pages/NetModule.json5#L6-L22)

**参考链接**

[访问控制概述](../../../../../harmonyos-guides/系统/安全/程序访问控制/访问控制概述/access-token-overview.md)
