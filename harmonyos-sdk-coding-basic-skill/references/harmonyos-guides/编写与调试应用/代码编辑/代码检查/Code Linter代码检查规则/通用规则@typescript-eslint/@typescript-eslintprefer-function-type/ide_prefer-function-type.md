---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_prefer-function-type
title: @typescript-eslint/prefer-function-type
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > @typescript-eslint/prefer-function-type
category: harmonyos-guides
scraped_at: 2026-06-01T15:20:46+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:196c301c86aa94b0a56e1aa327da83f73f10e45acb383bcfe742625dfd764b6c
---
强制使用函数类型而不是带有签名的对象类型。

## 规则配置

```
1. // code-linter.json5
2. {
3. "rules": {
4. "@typescript-eslint/prefer-function-type": "error"
5. }
6. }
```

## 选项

该规则无需配置额外选项。

## 正例

```
1. export function foo(example: () => number): number {
2. return example();
3. }

5. // returns the function itself, not the `this` argument.
6. export type ReturnsSelf = (arg: string) => ReturnsSelf;

8. export interface Foo {
9. bar: string;
10. }
```

## 反例

```
1. interface GeneratedTypeLiteralInterface {
2. (): number;
3. }

5. export function foo(example: GeneratedTypeLiteralInterface): number {
6. return example();
7. }

9. export interface Foo {
10. (bar: string): this;
11. }
```

## 规则集

```
1. plugin:@typescript-eslint/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](<../../../Code Linter代码检查/ide-code-linter.md>)。
