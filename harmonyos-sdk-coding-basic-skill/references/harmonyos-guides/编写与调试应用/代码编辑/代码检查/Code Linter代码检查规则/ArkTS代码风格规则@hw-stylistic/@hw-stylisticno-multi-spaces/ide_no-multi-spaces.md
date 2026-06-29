---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_no-multi-spaces
title: @hw-stylistic/no-multi-spaces
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > ArkTS代码风格规则@hw-stylistic > @hw-stylistic/no-multi-spaces
category: harmonyos-guides
scraped_at: 2026-06-01T15:23:25+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:15aaecc98b14c7a3d78c05346765904968a57d62760afe944dd28c0bb0b8bce3
---
不允许出现连续多个空格，除非是换行。该规则仅检查.ets文件类型。

## 规则配置

```
1. // code-linter.json5
2. {
3. "rules": {
4. "@hw-stylistic/no-multi-spaces": "error"
5. }
6. }
```

## 选项

该规则无需配置额外选项。

## 正例

```
1. export const message: string = 'Hello World';
```

## 反例

```
1. // Multiple spaces found before 'message'.
2. // Multiple spaces found before 'string'.
3. // Multiple spaces found before '='.
4. // Multiple spaces found before 'Hello World'.
5. export const   message:  string  =  'Hello World';
```

## 规则集

```
1. "plugin:@hw-stylistic/recommended"
2. "plugin:@hw-stylistic/all"
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](<../../../Code Linter代码检查/ide-code-linter.md>)。
