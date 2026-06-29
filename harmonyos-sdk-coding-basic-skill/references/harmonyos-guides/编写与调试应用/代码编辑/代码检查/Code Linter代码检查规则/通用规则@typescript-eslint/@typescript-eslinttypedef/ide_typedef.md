---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_typedef
title: @typescript-eslint/typedef
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > @typescript-eslint/typedef
category: harmonyos-guides
scraped_at: 2026-06-01T15:21:15+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:1f1bdedfa265b9c2609b7de6663ff6f2abd729d1f1b11ac713a662aae2fb7613
---
在某些位置需要类型注释。

支持检查的范围从选项中查看。

## 规则配置

```
1. // code-linter.json5
2. {
3. "rules": {
4. "@typescript-eslint/typedef": "error"
5. }
6. }
```

## 选项

详情请参考[@typescript-eslint/typedef选项](https://typescript-eslint.nodejs.cn/rules/typedef#options)。

## 正例

```
1. export const text = 'text';
```

## 反例

```
1. // 默认配置下，规则不会告警
```

## 规则集

```
1. plugin:@typescript-eslint/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](<../../../Code Linter代码检查/ide-code-linter.md>)。
