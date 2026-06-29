---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-space-before-function-paren-stylistic
title: @hw-stylistic/space-before-function-paren
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > ArkTS代码风格规则@hw-stylistic > @hw-stylistic/space-before-function-paren
category: harmonyos-guides
scraped_at: 2026-06-01T15:23:33+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:c6900a6cc6685f1b4590c979eb69fa0d248fd74c39a2c3c524cc8f663b05ab38
---
在函数名和“(”之间强制不加空格。该规则仅检查.ets文件类型。

## 规则配置

```
1. // code-linter.json5
2. {
3. "rules": {
4. "@hw-stylistic/space-before-function-paren": "error"
5. }
6. }
```

## 选项

该规则无需配置额外选项。

## 正例

```
1. function bar() {
2. // doSomething
3. }
4. bar();
```

## 反例

```
1. // Unexpected space before function parentheses.
2. function bar () {
3. // doSomething
4. }
5. // Unexpected space before function parentheses.
6. bar  ();
```

## 规则集

```
1. "plugin:@hw-stylistic/recommended"
2. "plugin:@hw-stylistic/all"
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](<../../../Code Linter代码检查/ide-code-linter.md>)。
