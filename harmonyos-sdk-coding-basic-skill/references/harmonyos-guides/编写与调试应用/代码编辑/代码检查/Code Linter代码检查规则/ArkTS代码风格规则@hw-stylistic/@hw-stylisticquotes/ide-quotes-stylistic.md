---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-quotes-stylistic
title: @hw-stylistic/quotes
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > ArkTS代码风格规则@hw-stylistic > @hw-stylistic/quotes
category: harmonyos-guides
scraped_at: 2026-06-01T15:23:30+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:b1ab319ce411ac0b31f84fd7aad77d8238330ca4819d97b536832267ae3dc787
---
强制字符串使用单引号。该规则仅检查.ets文件类型。

## 规则配置

```
1. // code-linter.json5
2. {
3. "rules": {
4. "@hw-stylistic/quotes": "error"
5. }
6. }
```

## 选项

该规则无需配置额外选项。

## 正例

```
1. export {a, b};

3. const a = 'hello';
4. const b = `hello`;
```

## 反例

```
1. // Strings must use single quotes.
2. export const a = "hello";
```

## 规则集

```
1. "plugin:@hw-stylistic/recommended"
2. "plugin:@hw-stylistic/all"
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](<../../../Code Linter代码检查/ide-code-linter.md>)。
