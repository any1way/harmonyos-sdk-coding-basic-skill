---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_no-empty-interface
title: @typescript-eslint/no-empty-interface
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > @typescript-eslint/no-empty-interface
category: harmonyos-guides
scraped_at: 2026-06-01T15:19:56+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:dbb1e4b7f72d0c3205ae7953504f3f6c1bbdaa1bedf134ecbe1fceb5f618a0bf
---
不允许声明空接口。

## 规则配置

```
1. // code-linter.json5
2. {
3. "rules": {
4. "@typescript-eslint/no-empty-interface": "error"
5. }
6. }
```

## 选项

详情请参考[@typescript-eslint/no-empty-interface选项](https://typescript-eslint.nodejs.cn/rules/no-empty-interface/#options)。

## 正例

```
1. // an interface with any number of members
2. interface Foo {
3. name: string;
4. }

6. interface Bar {
7. age: number;
8. }

10. // an interface with more than one supertype
11. // in this case the interface can be used as a replacement of an intersection type.
12. export interface Baz extends Foo, Bar {}
```

## 反例

```
1. // an empty interface
2. interface Foo {}

4. // an interface with only one supertype (Bar === Foo)
5. export interface Bar extends Foo {}

7. // an interface with an empty list of supertypes
8. export interface Baz {}
```

## 规则集

```
1. plugin:@typescript-eslint/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](<../../../Code Linter代码检查/ide-code-linter.md>)。
