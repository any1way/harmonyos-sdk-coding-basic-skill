---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hp-arkts-no-use-any-export-current
title: @performance/hp-arkts-no-use-any-export-current
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 性能规则@performance > @performance/hp-arkts-no-use-any-export-current
category: harmonyos-guides
scraped_at: 2026-06-01T15:22:04+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:dc04014e81d84f3854a87709993243c143a6c7bb520d5ff0dd551be6bf4cbbbd
---
避免使用export \* 导出当前module中定义的类型和数据。

冷启动完成时延场景下，建议优先修改。

## 规则配置

```
1. // code-linter.json5
2. {
3. "rules": {
4. "@performance/hp-arkts-no-use-any-export-current": "warn",
5. }
6. }
```

## 选项

该规则无需配置额外选项。

## 正例

```
1. export class User {
2. id?: number;
3. name?: string;
4. }
```

## 反例

```
1. class User {
2. id?: number;
3. name?: string;
4. }
5. // 当前文件 User.ets
6. export * from './User';
7. // 当前文件 User.ets
8. export * as XX from './User';
```

## 规则集

```
1. plugin:@performance/recommended
2. plugin:@performance/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](<../../../Code Linter代码检查/ide-code-linter.md>)。
