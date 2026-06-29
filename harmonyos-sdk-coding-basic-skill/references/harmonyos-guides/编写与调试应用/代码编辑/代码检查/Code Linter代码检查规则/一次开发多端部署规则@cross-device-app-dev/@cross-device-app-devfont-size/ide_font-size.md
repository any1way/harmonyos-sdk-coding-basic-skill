---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_font-size
title: @cross-device-app-dev/font-size
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 一次开发多端部署规则@cross-device-app-dev > @cross-device-app-dev/font-size
category: harmonyos-guides
scraped_at: 2026-06-01T15:23:09+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:30fbef4b11712921a0f9f4e860186bc3bf69c82d93d63c04f68ee44e92e32a9e
---
字体大小要求至少为8fp以便于阅读。

## 规则配置

```
1. // code-linter.json5
2. {
3. "rules": {
4. "@cross-device-app-dev/font-size": "warn"
5. }
6. }
```

## 选项

该规则无需配置额外选项。

## 正例

```
1. const FONT_SIZE = 12;

3. @Entry
4. @Component
5. struct Index {
6. build() {
7. RelativeContainer() {
8. Text('message').fontSize(12)
9. Text('message').fontSize('12fp')
10. }
11. }
12. }
```

## 反例

```
1. const FONT_SIZE = 7;

3. @Entry
4. @Component
5. struct Index1 {
6. build() {
7. RelativeContainer() {
8. Text('message').fontSize(FONT_SIZE)
9. Text('message').fontSize('7fp')
10. }
11. }
12. }
```

## 规则集

```
1. plugin:@cross-device-app-dev/recommended
2. plugin:@cross-device-app-dev/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](<../../../Code Linter代码检查/ide-code-linter.md>)。
