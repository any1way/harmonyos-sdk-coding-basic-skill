---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_hp-arkui-use-row-column-to-replace-flex
title: @performance/hp-arkui-use-row-column-to-replace-flex
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 性能规则@performance > @performance/hp-arkui-use-row-column-to-replace-flex
category: harmonyos-guides
scraped_at: 2026-06-01T15:22:23+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:919f237c327e20f303d4d1da3c6fbb594ef729f927f267cbc8ec99eefdbddffd
---
建议使用Column/Row替代Flex。

通用丢帧场景下，建议优先修改。

## 规则配置

```
1. // code-linter.json5
2. {
3. "rules": {
4. "@performance/hp-arkui-use-row-column-to-replace-flex": "suggestion",
5. }
6. }
```

## 选项

该规则无需配置额外选项。

## 正例

```
1. @Entry
2. @Component
3. struct MyComponent {
4. build() {
5. // Replace Flex with Column/Row
6. Column() {
7. Text('Replace Flex with Column/Row')
8. .fontSize(12)
9. .height('16')
10. .margin({
11. top: 5,
12. bottom: 10
13. })
14. Flex().width(300).height(200).backgroundColor(Color.Pink)
15. Flex().width(300).height(200).backgroundColor(Color.Yellow)
16. Flex().width(300).height(200).backgroundColor(Color.Grey)
17. Flex().width(300).height(200).backgroundColor(Color.Pink)
18. Flex().width(300).height(200).backgroundColor(Color.Yellow)
19. Flex().width(300).height(200).backgroundColor(Color.Grey)
20. }.height(200)
21. }
22. }
```

## 反例

```
1. @Entry
2. @Component
3. struct MyComponent {
4. build() {
5. // Flex Nesting
6. Flex({ direction: FlexDirection.Column }) {
7. Text('Replace Flex with Column/Row')
8. .fontSize(12)
9. .height('16')
10. .margin({
11. top: 5,
12. bottom: 10
13. })
14. Flex().width(300).height(200).backgroundColor(Color.Pink)
15. Flex().width(300).height(200).backgroundColor(Color.Yellow)
16. Flex().width(300).height(200).backgroundColor(Color.Grey)
17. Flex().width(300).height(200).backgroundColor(Color.Pink)
18. Flex().width(300).height(200).backgroundColor(Color.Yellow)
19. Flex().width(300).height(200).backgroundColor(Color.Grey)
20. }.height(200)
21. }
22. }
```

## 规则集

```
1. plugin:@performance/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](<../../../Code Linter代码检查/ide-code-linter.md>)。
