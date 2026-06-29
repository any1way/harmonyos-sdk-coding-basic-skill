---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-network-23
title: Socket接口库是否支持绑定域名
breadcrumb: FAQ > 系统开发 > 网络 > 网络（Network） > Socket接口库是否支持绑定域名
category: harmonyos-faqs
scraped_at: 2026-06-12T10:37:31+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:a2d398a99093d61b22143e8213e9cd923bc488a67c9e90e2f0c1ac4353899509
---
Socket不支持域名访问，只能使用IP地址。域名需要通过DNS解析为对应的IP地址。

参考代码如下：

```
1. import { connection } from '@kit.NetworkKit'
2. import { BusinessError } from "@kit.BasicServicesKit"

4. connection.getAddressesByName("xxxx", (error: BusinessError, data: connection.NetAddress[]) => {
5. console.log(JSON.stringify(error));
6. console.log(JSON.stringify(data));
7. })
```

[AddressesByName.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/NetworkKit/entry/src/main/ets/pages/AddressesByName.ets#L21-L27)

**参考链接**

[connection.getAddressesByName](<../../../../../harmonyos-references/网络/Network Kit（网络服务）/ArkTS API/@ohos.net.connection (网络连接管理)/js-apis-net-connection.md#connectiongetaddressesbyname>)
