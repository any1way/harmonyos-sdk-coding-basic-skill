---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_listen-multi-network-concurrent
title: @correctness/listen-multi-network-concurrent
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 正确性规则@correctness > @correctness/listen-multi-network-concurrent
category: harmonyos-guides
scraped_at: 2026-06-01T15:23:41+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:1bc6ed34a18ff3b736adc34bd972e92da8c3314996f1d7fbf6dec1817be236c8
---
建议应用订阅连接迁移通知，可在WiFi/蜂窝连接切换前后获取切换状态通知。

该规则仅在联网类应用检查整个工程时才生效。

## 规则配置

```
1. // code-linter.json5
2. {
3. "rules": {
4. "@correctness/listen-multi-network-concurrent": "suggestion"
5. }
6. }
```

## 选项

该规则无需配置额外选项。

## 正例

```
1. // With the ohos.permission.GET_NETWORK_INFO permission configured
2. import { netHandover } from '@kit.NetworkBoostKit';
3. import { BusinessError } from '@kit.BasicServicesKit';
4. try {
5. netHandover.on('handoverChange', (info: netHandover.HandoverInfo) => {
6. if (info.handoverStart) {
7. console.info('handover start');
8. } else if (info.handoverComplete) {
9. console.info('handover complete');
10. }
11. });
12. } catch (err) {
13. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
14. }
15. try {
16. netHandover.off('handoverChange');
17. } catch (err) {
18. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
19. }
```

## 反例

```
1. // With the ohos.permission.GET_NETWORK_INFO permission configured
2. // The `on(type: 'handoverChange', callback: Callback<HandoverInfo>)` function is not called.
```

## 规则集

```
1. plugin:@correctness/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](<../../../Code Linter代码检查/ide-code-linter.md>)。
