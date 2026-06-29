---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_no-page-method-on-preview-component
title: @previewer/no-page-method-on-preview-component
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 预览规则@previewer > @previewer/no-page-method-on-preview-component
category: harmonyos-guides
scraped_at: 2026-06-01T15:23:04+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:6518228b5ee31fc88a0334a982254d3dbf1a6a96d7eb61467147be742c12a829
---
禁止在非路由组件上实例化onPageShow、onPageHide、onBackPress等页面级方法。

## 规则配置

```
1. // code-linter.json5
2. {
3. "rules": {
4. "@previewer/no-page-method-on-preview-component": "warn"
5. }
6. }
```

## 选项

该规则无需配置额外选项。

## 正例

```
1. @Entry
2. @Component
3. struct Index {
4. @State message: string = 'Hello World';
5. onPageShow(): void {}
6. onPageHide(): void {}
7. onBackPress(): void {}
8. build() {
9. Row() {
10. Column() {
11. Text(this.message)
12. }
13. }
14. }
15. }
```

## 反例

```
1. @Preview
2. @Component
3. struct Index {
4. @State message: string = 'Hello World';
5. onPageShow(): void {}
6. onPageHide(): void {}
7. onBackPress(): void {}
8. build() {
9. Column() {
10. Text(this.message)
11. }
12. }
13. }
```

## 规则集

```
1. plugin:@previewer/recommended
2. plugin:@previewer/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](<../../../Code Linter代码检查/ide-code-linter.md>)。
