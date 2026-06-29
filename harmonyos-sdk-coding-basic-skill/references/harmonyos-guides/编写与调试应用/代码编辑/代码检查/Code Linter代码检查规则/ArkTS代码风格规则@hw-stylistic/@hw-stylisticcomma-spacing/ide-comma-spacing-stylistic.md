---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-comma-spacing-stylistic
title: @hw-stylistic/comma-spacing
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > ArkTS代码风格规则@hw-stylistic > @hw-stylistic/comma-spacing
category: harmonyos-guides
scraped_at: 2026-06-01T15:23:20+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:4305d85f5876213cf9d68889639ee809101c46f7d298a4b7f99ceeea8dbba4a6
---
强制数组元素和函数中多个参数之间的逗号后面加空格，逗号前不加空格。该规则仅检查.ets文件类型。

## 规则配置

```
1. // code-linter.json5
2. {
3. "rules": {
4. "@hw-stylistic/comma-spacing": "error"
5. }
6. }
```

## 选项

该规则无需配置额外选项。

## 正例

```
1. export {bar, arr};

3. function bar(param1: string, param2: string) {
4. return [param1, param2];
5. }
6. const arr = ['s1', 's2', 's3', 's4'];
```

## 反例

```
1. export {arr};
2. // A space is required after ','.
3. // There should be no space before ','.
4. const arr = ['s1' ,'s2' ,'s3'];
```

## 规则集

```
1. "plugin:@hw-stylistic/recommended"
2. "plugin:@hw-stylistic/all"
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](<../../../Code Linter代码检查/ide-code-linter.md>)。
