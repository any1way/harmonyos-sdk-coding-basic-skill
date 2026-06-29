---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_one-var-declaration-per-line
title: @hw-stylistic/one-var-declaration-per-line
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > ArkTS代码风格规则@hw-stylistic > @hw-stylistic/one-var-declaration-per-line
category: harmonyos-guides
scraped_at: 2026-06-01T15:23:27+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:56972ec43802c71377cb22e4e2ae612caba4f57a063255e3740212fb6611074a
---
变量声明时，要求一次仅声明一个变量。该规则仅检查.ets文件类型。

## 规则配置

```
1. // code-linter.json5
2. {
3. "rules": {
4. "@hw-stylistic/one-var-declaration-per-line": "error"
5. }
6. }
```

## 选项

该规则无需配置额外选项。

## 正例

```
1. let a: string = 'hello';
2. let b: string = 'world';
3. a += 'my';
4. b += 'my';

6. const c: string = 'hello';
7. const d: string = 'world';

9. console.info(`a: ${a}, b: ${b}, c: ${c}, d: ${d}`);
```

## 反例

```
1. // Split 'const' declarations into multiple statements.
2. const a: string = 'hello', b: string = 'world';
```

## 规则集

```
1. "plugin:@hw-stylistic/recommended"
2. "plugin:@hw-stylistic/all"
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](<../../../Code Linter代码检查/ide-code-linter.md>)。
