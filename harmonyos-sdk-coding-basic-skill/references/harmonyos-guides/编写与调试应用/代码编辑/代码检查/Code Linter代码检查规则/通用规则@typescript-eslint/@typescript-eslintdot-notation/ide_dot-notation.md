---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_dot-notation
title: @typescript-eslint/dot-notation
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > @typescript-eslint/dot-notation
category: harmonyos-guides
scraped_at: 2026-06-01T15:19:34+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:269db05db4e7e3170d1fb57153d3b2cc82d2e73a2e24a4792cc072d732041e7d
---
强制使用点表示法。

访问属性有两种方式，一种是点表示法（foo.bar），另一种是括号表示法（foo["bar"]），点表示法更易于阅读，这里推荐使用点表示法。

该规则仅支持对.js/.ts文件进行检查。

## 规则配置

```
1. // code-linter.json5
2. {
3. "rules": {
4. "@typescript-eslint/dot-notation": "error"
5. }
6. }
```

## 选项

详情请参考[@typescript-eslint/dot-notation选项](https://eslint.nodejs.cn/docs/rules/dot-notation#选项)。

## 正例

```
1. const foo = {
2. bar: 'hello'
3. };

5. export const x = foo.bar;
```

## 反例

```
1. const foo = {
2. bar: 'hello'
3. };

5. export const x = foo['bar'];
```

## 规则集

```
1. plugin:@typescript-eslint/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](<../../../Code Linter代码检查/ide-code-linter.md>)。
