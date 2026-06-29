---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_prefer-namespace-keyword
title: @typescript-eslint/prefer-namespace-keyword
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > @typescript-eslint/prefer-namespace-keyword
category: harmonyos-guides
scraped_at: 2026-06-01T15:20:49+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:a7f1104ee5e609d128243fc6f4128834c96b64b05c6775fd5bdcccc192f66959
---
推荐使用“namespace”关键字而不是“module”关键字来声明一个自定义的 TypeScript 模块。

该规则仅支持对.js/.ts文件进行检查。

## 规则配置

```
1. // code-linter.json5
2. {
3. "rules": {
4. "@typescript-eslint/prefer-namespace-keyword": "error"
5. }
6. }
```

## 选项

该规则无需配置额外选项。

## 正例

```
1. export namespace Example {}
```

## 反例

```
1. export module Example {}
```

## 规则集

```
1. plugin:@typescript-eslint/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](<../../../Code Linter代码检查/ide-code-linter.md>)。
