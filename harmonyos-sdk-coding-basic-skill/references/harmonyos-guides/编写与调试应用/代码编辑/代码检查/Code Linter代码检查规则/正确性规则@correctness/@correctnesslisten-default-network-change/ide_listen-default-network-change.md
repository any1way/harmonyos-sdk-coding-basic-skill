---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_listen-default-network-change
title: @correctness/listen-default-network-change
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 正确性规则@correctness > @correctness/listen-default-network-change
category: harmonyos-guides
scraped_at: 2026-06-01T15:23:40+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:925af433017dab855d117780c79e3afdc4e88d30cb2e9c6d4f7c178d4acf2a3f
---
建议应用监听默认网络的变化，关闭原有网络的数据传输，并使用新网络建立数据传输。

该规则仅在联网类应用检查整个工程时才生效。

## 规则配置

```
1. // code-linter.json5
2. {
3. "rules": {
4. "@correctness/listen-default-network-change": "suggestion"
5. }
6. }
```

## 选项

该规则无需配置额外选项。

## 正例

```
1. // With the ohos.permission.GET_NETWORK_INFO permission configured
2. import connection from '@ohos.net.connection';
3. export function test() {
4. const defaultNet = connection.getDefaultNetSync();
5. const netCapabilities = connection.getNetCapabilitiesSync(defaultNet);
6. let bearerTypes = netCapabilities.bearerTypes;
7. const netConnection = connection.createNetConnection();
8. netConnection.on('netCapabilitiesChange', (netCap: connection.NetCapabilityInfo) => {
9. const newBearTypes = netCap.netCap.bearerTypes;
10. if (newBearTypes !== bearerTypes) {
11. bearerTypes = newBearTypes;
12. }
13. });
14. }
```

## 反例

```
1. // With the ohos.permission.GET_NETWORK_INFO permission configured
2. // import connection from '@ohos.net.connection';
3. // The `on(type: 'netCapabilitiesChange', callback: Callback<connection.NetCapabilityInfo>)`, `getDefaultNet`/`getDefaultNetSync` and `getNetCapabilities`/`getNetCapabilitiesSync` functions are not called.
```

## 规则集

```
1. plugin:@correctness/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](<../../../Code Linter代码检查/ide-code-linter.md>)。
