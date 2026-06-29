---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hp-arkui-sg-anonymousid-async
title: @performance/hp-arkui-suggest-use-get-anonymousid-async
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 性能规则@performance > @performance/hp-arkui-suggest-use-get-anonymousid-async
category: harmonyos-guides
scraped_at: 2026-06-01T15:22:16+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:3b73bd5e66227bd22d095128877c028543cfbe7fa8f35527d2d77940270c6704
---
建议在主线程中通过异步获取IFAA免密认证的匿名化ID。

高耗时函数处理场景下，建议优先修改。

## 规则配置

```
1. // code-linter.json5
2. {
3. "rules": {
4. "@performance/hp-arkui-suggest-use-get-anonymousid-async": "suggestion",
5. }
6. }
```

## 选项

该规则无需配置额外选项。

## 正例

```
1. import { ifaa } from '@kit.OnlineAuthenticationKit'
2. import { BusinessError } from '@kit.BasicServicesKit';

4. // 开发者需要按照IIFAA的TLV格式构造入参，并转换为Uint8Array参数；此处arg需要开发者替换为真实入参。
5. let arg = new Uint8Array([0]);
6. let getAnonIdPromise: Promise<Uint8Array> = ifaa.getAnonymousId(arg);
7. getAnonIdPromise.then(result => {
8. console.info("Succeeded in doing getAnonymousId.");
9. // 开发者处理result
10. }).catch((err: BusinessError) => {
11. console.error(`Failed to call getAnonymousId. Code: ${err.code}, message: ${err.message}`);
12. });
```

## 反例

```
1. import { ifaa } from '@kit.OnlineAuthenticationKit'

3. // 开发者需要按照IIFAA的TLV格式构造入参，并转换为Uint8Array参数；此处arg需要开发者替换为真实入参。
4. let arg = new Uint8Array([0]);
5. let getAnonIdResult: Uint8Array = ifaa.getAnonymousIdSync(arg);
```

## 规则集

```
1. plugin:@performance/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](<../../../Code Linter代码检查/ide-code-linter.md>)。
