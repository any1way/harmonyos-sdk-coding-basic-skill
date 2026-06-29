---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_object-property-newline
title: @hw-stylistic/object-property-newline
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > ArkTS代码风格规则@hw-stylistic > @hw-stylistic/object-property-newline
category: harmonyos-guides
scraped_at: 2026-06-01T15:23:27+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:9ed96e5c7f61a9103ab12dcb71cde3187e0fa2afde0662fb1c039c1749299f79
---
强制对象属性换行。该规则仅检查.ets文件类型。

对象属性不超过4个时，允许在同一行，也可以每个属性都换行。对象属性超过4个时，每个属性必须都换行。

## 规则配置

```
1. // code-linter.json5
2. {
3. "rules": {
4. "@hw-stylistic/object-property-newline": "error"
5. }
6. }
```

## 选项

该规则无需配置额外选项。

## 正例

```
1. export {a, b};

3. interface II {
4. p1: string;
5. p2: string;
6. p3: string;
7. p4: string;
8. p5?: string;
9. }

11. const a: II = {
12. p1: 'p1',
13. p2: 'p2',
14. p3: 'p3',
15. p4: 'p4',
16. p5: 'p5'
17. };

19. const b: II = { p1: 'p1', p2: 'p2', p3: 'p3', p4: 'p4' };
```

## 反例

```
1. export {a, b};

3. interface II {
4. p1: string;
5. p2: string;
6. p3: string;
7. p4: string;
8. p5?: string;
9. }

11. // Object properties must go on a new line.
12. const a: II = { p1: 'p1', p2: 'p2',
13. p3: 'p3', p4: 'p4' };

15. // Object properties must go on a new line.
16. const b: II = { p1: 'p1', p2: 'p2', p3: 'p3', p4: 'p4', p5: 'p5' };
```

## 规则集

```
1. "plugin:@hw-stylistic/recommended"
2. "plugin:@hw-stylistic/all"
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](<../../../Code Linter代码检查/ide-code-linter.md>)。
