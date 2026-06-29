---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_operator-linebreak
title: @hw-stylistic/operator-linebreak
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > ArkTS代码风格规则@hw-stylistic > @hw-stylistic/operator-linebreak
category: harmonyos-guides
scraped_at: 2026-06-01T15:23:29+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:4a5de602931ba28b72e8ae8d69b75c0df203fccb58b6d9912a99be5d1e6984ae
---
强制运算符位于代码行末。该规则仅检查.ets文件类型。

## 规则配置

```
1. // code-linter.json5
2. {
3. "rules": {
4. "@hw-stylistic/operator-linebreak": "error"
5. }
6. }
```

## 选项

该规则无需配置额外选项。

## 正例

```
1. export function test(n1: number, n2: number): void {
2. if (n1 > n2) {
3. console.info('hello');
4. }

6. if (n1 >
7. n2) {
8. console.info('hello');
9. }
10. }
```

## 反例

```
1. export function test(n1: number, n2: number, n3: number): void {
2. if (n1 > n2
3. // '||' should be placed at the end of the line.
4. || n1 < n3) {
5. console.info('hello');
6. }
7. }
```

## 规则集

```
1. "plugin:@hw-stylistic/recommended"
2. "plugin:@hw-stylistic/all"
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](<../../../Code Linter代码检查/ide-code-linter.md>)。
