---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_prefer-for-of
title: @typescript-eslint/prefer-for-of
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > @typescript-eslint/prefer-for-of
category: harmonyos-guides
scraped_at: 2026-06-01T15:20:44+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:fa77321edc2943a78170c0253f3705e216e849f48d55820be6c9271a733a731a
---
强制使用“for-of”循环而不是标准“for”循环。

## 规则配置

```
1. // code-linter.json5
2. {
3. "rules": {
4. "@typescript-eslint/prefer-for-of": "error"
5. }
6. }
```

## 选项

该规则无需配置额外选项。

## 正例

```
1. declare const array: string[];

3. for (const x of array) {
4. console.log(x);
5. }

7. for (let i = 0; i < array.length; i++) {
8. // i is used, so for-of could not be used.
9. console.log(`${i}-${array[i]}`);
10. }
```

## 反例

```
1. declare const array: string[];

3. for (const x of array) {
4. console.log(x);
5. }

7. for (let i = 0; i < array.length; i++) {
8. console.log(array[i]);
9. }
```

## 规则集

```
1. plugin:@typescript-eslint/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](<../../../Code Linter代码检查/ide-code-linter.md>)。
