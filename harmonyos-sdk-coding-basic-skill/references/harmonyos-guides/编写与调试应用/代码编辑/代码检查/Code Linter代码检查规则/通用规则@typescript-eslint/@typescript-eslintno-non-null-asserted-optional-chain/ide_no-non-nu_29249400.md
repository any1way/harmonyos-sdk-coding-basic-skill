---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_no-non-null-asserted-optional-chain
title: @typescript-eslint/no-non-null-asserted-optional-chain
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > @typescript-eslint/no-non-null-asserted-optional-chain
category: harmonyos-guides
scraped_at: 2026-06-01T15:20:17+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:94cce2b2d761b10ccf50210a3d620180a9d42ca8392784d7f320955aa0a9aeb5
---
禁止在可选链表达式之后使用非空断言。

## 规则配置

```
1. // code-linter.json5
2. {
3. "rules": {
4. "@typescript-eslint/no-non-null-asserted-optional-chain": "error"
5. }
6. }
```

## 选项

该规则无需配置额外选项。

## 正例

```
1. class CC {
2. public bar = 'hello';

4. public foo(): void {
5. console.info('foo');
6. }
7. }
8. function getInstance(): CC | undefined {
9. return new CC();
10. }

12. const instance = getInstance();
13. console.info(`${instance?.bar}`);
14. instance?.foo();
```

## 反例

```
1. class CC {
2. public bar: string = 'hello';

4. public foo() {
5. console.info('foo');
6. }
7. }

9. function getInstance(): CC | undefined {
10. return new CC();
11. }

13. const instance = getInstance();
14. console.info(`${instance?.bar!}`);
15. instance?.foo()!;
```

## 规则集

```
1. plugin:@typescript-eslint/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](<../../../Code Linter代码检查/ide-code-linter.md>)。
