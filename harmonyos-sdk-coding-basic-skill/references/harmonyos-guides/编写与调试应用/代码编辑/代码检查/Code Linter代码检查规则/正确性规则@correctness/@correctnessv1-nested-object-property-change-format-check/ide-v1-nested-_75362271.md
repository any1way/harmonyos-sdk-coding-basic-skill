---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-v1-nested-object-property-change-format-check
title: @correctness/v1-nested-object-property-change-format-check
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 正确性规则@correctness > @correctness/v1-nested-object-property-change-format-check
category: harmonyos-guides
scraped_at: 2026-06-01T15:23:44+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:4b9eeb6f59be518f80424f0f31f1fbc0c1563af3069323a6114b6e3851e886b3
---
建议不要直接修改普通V1状态变量中嵌套对象的属性，应使用@Observed/@ObjectLink来观察嵌套对象的属性更改。

## 规则配置

```
1. // code-linter.json5
2. {
3. "rules": {
4. "@correctness/v1-nested-object-property-change-format-check": "warn"
5. }
6. }
```

## 选项

该规则无需配置额外选项。

## 正例

```
1. class Parent {
2. parentId: number;
3. constructor(parentId: number) {
4. this.parentId = parentId;
5. }
6. getParentId(): number {
7. return this.parentId;
8. }
9. setParentId(parentId: number): void {
10. this.parentId = parentId;
11. }
12. }
13. @Observed
14. class Child {
15. childId: number;
16. constructor(childId: number) {
17. this.childId = childId;
18. }
19. getChildId(): number {
20. return this.childId;
21. }
22. setChildId(childId: number): void {
23. this.childId = childId;
24. }
25. }
26. class Cousin extends Parent {
27. cousinId: number = 47;
28. child: Child;
29. constructor(parentId: number, cousinId: number, childId: number) {
30. super(parentId);
31. this.cousinId = cousinId;
32. this.child = new Child(childId);
33. }
34. getCousinId(): number {
35. return this.cousinId;
36. }
37. setCousinId(cousinId: number): void {
38. this.cousinId = cousinId;
39. }
40. getChild(): number {
41. return this.child.getChildId();
42. }
43. setChild(childId: number): void {
44. return this.child.setChildId(childId);
45. }
46. }
47. @Component
48. struct ViewChild {
49. @ObjectLink child: Child;
50. build() {
51. Column({ space: 10 }) {
52. Text(`childId: ${this.child.getChildId()}`)
53. Button('Change childId')
54. .onClick(() => {
55. this.child.setChildId(this.child.getChildId() + 1);
56. })
57. }
58. }
59. }
60. @Entry
61. @Component
62. struct MyView {
63. @State cousin: Cousin = new Cousin(10, 20, 30);
64. build() {
65. Column({ space: 10 }) {
66. Text(`parentId: ${this.cousin.parentId}`)
67. Button('Change Parent.parentId')
68. .onClick(() => {
69. this.cousin.parentId += 1;
70. })
71. Text(`cousinId: ${this.cousin.cousinId}`)
72. Button('Change Cousin.cousinId')
73. .onClick(() => {
74. this.cousin.cousinId += 1;
75. })
76. ViewChild({ child: this.cousin.child }) // Text(`childId: ${this.cousin.child.childId}`)的替代写法
77. Button('Change Cousin.Child.childId')
78. .onClick(() => {
79. this.cousin.child.childId += 1;
80. })
81. }
82. }
83. }
```

## 反例

```
1. class Parent {
2. parentId: number;
3. constructor(parentId: number) {
4. this.parentId = parentId;
5. }
6. getParentId(): number {
7. return this.parentId;
8. }
9. setParentId(parentId: number): void {
10. this.parentId = parentId;
11. }
12. }
13. class Child {
14. childId: number;
15. constructor(childId: number) {
16. this.childId = childId;
17. }
18. getChildId(): number {
19. return this.childId;
20. }
21. setChildId(childId: number): void {
22. this.childId = childId;
23. }
24. }
25. class Cousin extends Parent {
26. cousinId: number = 47;
27. child: Child;
28. constructor(parentId: number, cousinId: number, childId: number) {
29. super(parentId);
30. this.cousinId = cousinId;
31. this.child = new Child(childId);
32. }
33. getCousinId(): number {
34. return this.cousinId;
35. }
36. setCousinId(cousinId: number): void {
37. this.cousinId = cousinId;
38. }
39. getChild(): number {
40. return this.child.getChildId();
41. }
42. setChild(childId: number): void {
43. return this.child.setChildId(childId);
44. }
45. }
46. @Entry
47. @Component
48. struct MyView {
49. @State cousin: Cousin = new Cousin(10, 20, 30);
50. build() {
51. Column({ space: 10 }) {
52. Text(`parentId: ${this.cousin.parentId}`)
53. Button('Change Parent.parent')
54. .onClick(() => {
55. this.cousin.parentId += 1;
56. })
57. Text(`cousinId: ${this.cousin.cousinId}`)
58. Button('Change Cousin.cousinId')
59. .onClick(() => {
60. this.cousin.cousinId += 1;
61. })
62. Text(`childId: ${this.cousin.child.childId}`)
63. Button('Change Cousin.Child.childId')
64. .onClick(() => {
65. // 点击时上面的Text组件不会刷新
66. this.cousin.child.childId += 1;
67. })
68. }
69. }
70. }
```

## 规则集

```
1. plugin:@correctness/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](<../../../Code Linter代码检查/ide-code-linter.md>)。
