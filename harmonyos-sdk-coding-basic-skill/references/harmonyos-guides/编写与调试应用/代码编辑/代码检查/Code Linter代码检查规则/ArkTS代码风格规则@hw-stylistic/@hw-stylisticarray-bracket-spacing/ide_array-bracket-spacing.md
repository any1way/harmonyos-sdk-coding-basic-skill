---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_array-bracket-spacing
title: @hw-stylistic/array-bracket-spacing
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > ArkTS代码风格规则@hw-stylistic > @hw-stylistic/array-bracket-spacing
category: harmonyos-guides
scraped_at: 2026-06-01T15:23:18+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:fd2106a2d2d9c283cf40030bb030e461ed1909006c5b60d123371e8d5f74d2f4
---
强制数组“[”之后和“]”之前不加空格。该规则仅检查.ets文件类型。

## 规则配置

```
1. // code-linter.json5
2. {
3. "rules": {
4. "@hw-stylistic/array-bracket-spacing": "error"
5. }
6. }
```

## 选项

该规则无需配置额外选项。

## 正例

```
1. export const arr = ['a', 'b'];
```

## 反例

```
1. // There should be no space after '['.
2. // There should be no space before ']'.
3. export const arr = [ 'a', 'b' ];
```

## 规则集

```
1. "plugin:@hw-stylistic/recommended"
2. "plugin:@hw-stylistic/all"
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](<../../../Code Linter代码检查/ide-code-linter.md>)。
