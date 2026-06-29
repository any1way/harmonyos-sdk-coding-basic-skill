---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_triple-slash-reference
title: @typescript-eslint/triple-slash-reference
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > @typescript-eslint/triple-slash-reference
category: harmonyos-guides
scraped_at: 2026-06-01T15:21:13+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:1e20ebfe41e601fed55c59d94f48cea4afb6ff91ccffb18003be66b9bace7938
---
不允许某些三斜杠引用，推荐使用ES6风格的导入声明。

支持以下三种三斜杠引用方式的检查

```
1. /// <reference lib="..." />
2. /// <reference path="..." />
3. /// <reference types="..." />
```

## 规则配置

```
1. // code-linter.json5
2. {
3. "rules": {
4. "@typescript-eslint/triple-slash-reference": "error"
5. }
6. }
```

## 选项

详情请参考[@typescript-eslint/triple-slash-reference选项](https://typescript-eslint.nodejs.cn/rules/triple-slash-reference/#options)。

## 正例

```
1. import { value } from 'code';
2. export { value };
```

## 反例

```
1. /// <reference path="code" />

3. globalThis.value;
```

## 规则集

```
1. plugin:@typescript-eslint/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](<../../../Code Linter代码检查/ide-code-linter.md>)。
