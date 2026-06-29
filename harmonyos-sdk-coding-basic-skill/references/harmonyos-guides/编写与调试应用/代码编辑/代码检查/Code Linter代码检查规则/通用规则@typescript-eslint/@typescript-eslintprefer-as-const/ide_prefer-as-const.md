---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_prefer-as-const
title: @typescript-eslint/prefer-as-const
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > @typescript-eslint/prefer-as-const
category: harmonyos-guides
scraped_at: 2026-06-01T15:20:42+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:64e2a1e7452d4599abf1d99fd5d35a04f7469f63356fb5e6e96d449809727a7f
---
对于字面量类型，强制使用“as const”。

将字面量类型的值转换为对应的字面量类型，有两种方式，一种是“as const”，另一种是“as 字面量类型”，推荐使用“as const”。

该规则仅支持对.js/.ts文件进行检查。

## 规则配置

```
1. // code-linter.json5
2. {
3. "rules": {
4. "@typescript-eslint/prefer-as-const": "error"
5. }
6. }
```

## 选项

该规则无需配置额外选项。

## 正例

```
1. export const foo1 = 'bar';
2. export const foo2 = 'bar' as const;
3. export const foo3: 'bar' = 'bar' as const;
4. export const bar4 = 'bar' as string;
5. export const foo6 = { bar: 'baz' };
```

## 反例

```
1. export const bar: 1 = 1;
2. export const foo1 = <'bar'>'bar';
3. export const foo2 = { bar: 'baz' as 'baz' };
```

## 规则集

```
1. plugin:@typescript-eslint/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](<../../../Code Linter代码检查/ide-code-linter.md>)。
