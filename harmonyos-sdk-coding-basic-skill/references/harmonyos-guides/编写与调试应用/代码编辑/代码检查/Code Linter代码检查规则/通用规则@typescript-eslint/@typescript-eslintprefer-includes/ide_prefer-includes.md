---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_prefer-includes
title: @typescript-eslint/prefer-includes
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > @typescript-eslint/prefer-includes
category: harmonyos-guides
scraped_at: 2026-06-01T15:20:46+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:f64fca154472448fdc9efe66177aff9720f71513caa6883e0660cc8078cef53f
---
强制使用“includes”方法而不是“indexOf”方法。

## 规则配置

```
1. // code-linter.json5
2. {
3. "rules": {
4. "@typescript-eslint/prefer-includes": "error"
5. }
6. }
```

## 选项

该规则无需配置额外选项。

## 正例

```
1. const str: string = 'hello';
2. const array: string[] = ['hello'];
3. const readonlyArray: readonly string[] = ['hello'];

5. str.includes('h');
6. array.includes('h');
7. readonlyArray.includes('h');
```

## 反例

```
1. const str: string = 'hello';
2. const array: string[] = ['hello'];
3. const readonlyArray: readonly string[] = ['hello'];

5. const num = -1;
6. let vv = str.indexOf('h') !== num;
7. vv = vv && array.indexOf('h') !== num;
8. vv = vv && readonlyArray.indexOf('h') !== num;
9. export { vv };
```

## 规则集

```
1. plugin:@typescript-eslint/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](<../../../Code Linter代码检查/ide-code-linter.md>)。
