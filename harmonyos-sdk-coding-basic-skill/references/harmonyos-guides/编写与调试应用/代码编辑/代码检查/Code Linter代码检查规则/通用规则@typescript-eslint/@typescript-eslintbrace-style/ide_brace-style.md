---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_brace-style
title: @typescript-eslint/brace-style
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > @typescript-eslint/brace-style
category: harmonyos-guides
scraped_at: 2026-06-01T15:19:25+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:0ceda4d55ac67bc0cfb8f1ce67387675d6ec554a0af05b82cca7384fbbb0ccb1
---
对代码块强制执行一致的括号样式。

## 规则配置

```
1. // code-linter.json5
2. {
3. "rules": {
4. "@typescript-eslint/brace-style": "error"
5. }
6. }
```

## 选项

详情请参考[@typescript-eslint/brace-style选项](https://eslint.nodejs.cn/docs/rules/brace-style#选项)。

## 正例

```
1. function foo(): boolean {
2. return true;
3. }

5. class C {
6. static {
7. foo();
8. }

10. public meth() {
11. foo();
12. }
13. }

15. export { C };
```

## 反例

```
1. function foo(): boolean
2. {
3. return true;
4. }

6. class C {
7. static
8. {
9. foo();
10. }

12. public meth()
13. {
14. foo();
15. }
16. }

18. export { C };
```

## 规则集

```
1. plugin:@typescript-eslint/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](<../../../Code Linter代码检查/ide-code-linter.md>)。
