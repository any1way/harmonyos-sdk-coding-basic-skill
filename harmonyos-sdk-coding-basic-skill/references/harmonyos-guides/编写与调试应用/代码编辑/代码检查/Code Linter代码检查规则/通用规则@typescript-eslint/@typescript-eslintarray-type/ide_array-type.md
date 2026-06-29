---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_array-type
title: @typescript-eslint/array-type
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > @typescript-eslint/array-type
category: harmonyos-guides
scraped_at: 2026-06-01T15:19:20+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:ed1acb520e700d2b3ce0506df1bf2021dee0cfc848f31d3674417110cc5979d1
---
定义数组类型时，建议使用相同的样式。比如都使用T[]或者都使用Array<T>。

## 规则配置

```
1. // code-linter.json5
2. {
3. "rules": {
4. "@typescript-eslint/array-type": "error"
5. }
6. }
```

## 选项

详情请参考[typescript/array-type 选项](https://typescript-eslint.nodejs.cn/rules/array-type#options)。

## 正例

```
1. const x: string[] = ['a', 'b'];
2. const y: readonly string[] = ['a', 'b'];

4. export { x, y };
```

## 反例

```
1. const x: Array<string> = ['a', 'b'];
2. const y: ReadonlyArray<string> = ['a', 'b'];

4. export { x, y };
```

## 规则集

```
1. plugin:@typescript-eslint/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](<../../../Code Linter代码检查/ide-code-linter.md>)。
