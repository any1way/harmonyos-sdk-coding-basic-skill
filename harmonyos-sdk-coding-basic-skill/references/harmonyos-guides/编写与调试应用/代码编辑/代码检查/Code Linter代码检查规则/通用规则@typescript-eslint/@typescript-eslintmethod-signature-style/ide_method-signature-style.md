---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_method-signature-style
title: @typescript-eslint/method-signature-style
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > @typescript-eslint/method-signature-style
category: harmonyos-guides
scraped_at: 2026-06-01T15:19:45+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:b8ea716592f965a85c2d5ea507767962a34e0bf4d574d29313f572acb0c20fff
---
定义函数类型的属性时，强制使用特定的风格。

有两种方式定义对象/接口中函数类型的属性，一种是定义为属性，属性签名是函数，另一种是直接定义为方法。

该规则仅支持对.js/.ts文件进行检查。

## 规则配置

```
1. // code-linter.json5
2. {
3. "rules": {
4. "@typescript-eslint/method-signature-style": "error"
5. }
6. }
```

## 选项

详情请参考[@typescript-eslint/method-signature-style选项](https://typescript-eslint.nodejs.cn/rules/method-signature-style/#options)。

## 正例

```
1. // 默认要求定义为属性
2. export interface T1 {
3. func: (arg: string) => number;
4. }
```

## 反例

```
1. // 默认要求定义为属性
2. export interface T1 {
3. func(arg: string): number;
4. }
```

## 规则集

```
1. plugin:@typescript-eslint/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](<../../../Code Linter代码检查/ide-code-linter.md>)。
