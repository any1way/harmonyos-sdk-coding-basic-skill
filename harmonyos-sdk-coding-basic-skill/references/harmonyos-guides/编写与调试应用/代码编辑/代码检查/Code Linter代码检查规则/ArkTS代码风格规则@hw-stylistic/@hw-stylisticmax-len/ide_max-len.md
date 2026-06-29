---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_max-len
title: @hw-stylistic/max-len
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > ArkTS代码风格规则@hw-stylistic > @hw-stylistic/max-len
category: harmonyos-guides
scraped_at: 2026-06-01T15:23:24+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:bb94a89815f4c1c0d017a6799ce1850936473a52c8a71cf88d28ea42e683581d
---
强制代码行最大长度为120个字符。该规则仅检查.ets文件类型。

## 规则配置

```
1. // code-linter.json5
2. {
3. "rules": {
4. "@hw-stylistic/max-len": "error"
5. }
6. }
```

## 选项

该规则无需配置额外选项。

## 正例

```
1. @Entry
2. @Component
3. struct Index {
4. message: string = 'hello';

6. build() {
7. Text(this.message)
8. }
9. }
```

## 反例

```
1. // This line has a length of 135. Maximum allowed is 120.
2. export const longLongLongLongLongLongLongLongLongLongLongLongLongLongLongLongLongLongLongLongLongLongLongLongLongLongLongLongName = 10;
```

## 规则集

```
1. "plugin:@hw-stylistic/recommended"
2. "plugin:@hw-stylistic/all"
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](<../../../Code Linter代码检查/ide-code-linter.md>)。
