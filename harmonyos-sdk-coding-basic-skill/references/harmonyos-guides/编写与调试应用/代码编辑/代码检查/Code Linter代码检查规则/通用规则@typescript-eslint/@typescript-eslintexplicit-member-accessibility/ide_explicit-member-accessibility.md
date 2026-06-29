---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_explicit-member-accessibility
title: @typescript-eslint/explicit-member-accessibility
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > @typescript-eslint/explicit-member-accessibility
category: harmonyos-guides
scraped_at: 2026-06-01T15:19:36+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:11b0cbb766e63eba3b08dc1af407774dc13315c243d78c7a474f1972406c83bc
---
在类属性和方法上需要显式定义访问修饰符。

## 规则配置

```
1. // code-linter.json5
2. {
3. "rules": {
4. "@typescript-eslint/explicit-member-accessibility": "error"
5. }
6. }
```

## 选项

详情请参考[@typescript-eslint/explicit-member-accessibility选项](https://typescript-eslint.nodejs.cn/rules/explicit-member-accessibility)。

## 正例

```
1. export class Animal {
2. private animalName: string; // Property

4. public constructor(name: string) {
5. // Parameter property and constructor
6. this.animalName = name;
7. }

9. public get name(): string {
10. // get accessor
11. return this.animalName;
12. }

14. public set name(value: string) {
15. // set accessor
16. this.animalName = value;
17. }

19. public walk() {
20. // method
21. }
22. }
```

## 反例

```
1. export class Animal {
2. private animalName: string; // Property

4. constructor(name: string) {
5. // Parameter property and constructor
6. this.animalName = name;
7. }

9. get name(): string {
10. // get accessor
11. return this.animalName;
12. }

14. set name(value: string) {
15. // set accessor
16. this.animalName = value;
17. }

19. walk() {
20. // method
21. }
22. }
```

## 规则集

```
1. plugin:@typescript-eslint/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](<../../../Code Linter代码检查/ide-code-linter.md>)。
