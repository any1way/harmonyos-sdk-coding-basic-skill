---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_space-infix-ops
title: @typescript-eslint/space-infix-ops
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > @typescript-eslint/space-infix-ops
category: harmonyos-guides
scraped_at: 2026-06-01T15:21:09+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:9764e58a089f124766c3570dcf437213b2edb0660e557808e8335aec3dcd7709
---
运算符前后要求有空格。

## 规则配置

```
1. // code-linter.json5
2. {
3. "rules": {
4. "@typescript-eslint/space-infix-ops": "error"
5. }
6. }
```

## 选项

详情请参考[@typescript-eslint/space-infix-ops选项](https://eslint.nodejs.cn/docs/rules/space-infix-ops#选项)。

## 正例

```
1. declare const a: number;
2. declare const b: number;
3. export const c = a + b;
```

## 反例

```
1. declare const a: number;
2. declare const b: number;
3. export const c = a+b;
```

## 规则集

```
1. plugin:@typescript-eslint/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](<../../../Code Linter代码检查/ide-code-linter.md>)。
