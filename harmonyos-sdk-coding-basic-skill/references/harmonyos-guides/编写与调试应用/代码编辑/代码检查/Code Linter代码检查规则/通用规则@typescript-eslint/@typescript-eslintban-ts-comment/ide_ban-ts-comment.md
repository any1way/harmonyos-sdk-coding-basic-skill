---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_ban-ts-comment
title: @typescript-eslint/ban-ts-comment
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > @typescript-eslint/ban-ts-comment
category: harmonyos-guides
scraped_at: 2026-06-01T15:19:22+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:950c194ce76078fe90794b6091d8ea72672c103463d7c4f03212ef2dfd62b16c
---
不允许使用`@ts-<directional>`格式的注释，或要求在注释后进行补充说明。

## 规则配置

```
1. // code-linter.json5
2. {
3. "rules": {
4. "@typescript-eslint/ban-ts-comment": "error"
5. }
6. }
```

## 选项

详情请参考[@typescript-eslint/ban-ts-comment选项](https://typescript-eslint.nodejs.cn/rules/ban-ts-comment/#options)。

## 正例

```
1. console.log('hello');
```

## 反例

```
1. // @ts-expect-error
2. console.log('hello');

4. /* @ts-expect-error */
5. console.log('hello');
```

## 规则集

```
1. plugin:@typescript-eslint/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](<../../../Code Linter代码检查/ide-code-linter.md>)。
