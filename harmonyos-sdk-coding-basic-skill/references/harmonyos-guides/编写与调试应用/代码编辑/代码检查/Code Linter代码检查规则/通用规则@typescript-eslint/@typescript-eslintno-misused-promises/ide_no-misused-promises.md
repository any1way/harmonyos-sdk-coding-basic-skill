---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_no-misused-promises
title: @typescript-eslint/no-misused-promises
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > @typescript-eslint/no-misused-promises
category: harmonyos-guides
scraped_at: 2026-06-01T15:20:15+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:d7917a317c03ba247e57d0139d2e566f06c086fb367b7329f16a4b975b9596c2
---
禁止在不正确的位置使用Promise。

## 规则配置

```
1. // code-linter.json5
2. {
3. "rules": {
4. "@typescript-eslint/no-misused-promises": "error"
5. }
6. }
```

## 选项

详情请参考[@typescript-eslint/no-misused-promises选项](https://typescript-eslint.nodejs.cn/rules/no-misused-promises/#options)。

## 正例

```
1. export async function func(): Promise<void>{
2. const promise = Promise.resolve('value');

4. // Always `await` the Promise in a conditional
5. if (await promise) {
6. // Do something
7. }

9. const val = await promise ? '123' : '456';
10. console.log(`${val}`);

12. while (await promise) {
13. // Do something
14. }
15. }
```

## 反例

```
1. export async function func(): Promise<void>{
2. const promise = Promise.resolve('value');
3. // 默认条件语句中需要使用await Promise
4. if (promise) {
5. // Do something
6. }

8. // 默认条件语句中需要使用await Promise
9. const val = promise ? '123' : '456';
10. console.log(`${val}`);

12. // 默认条件语句中需要使用await Promise
13. while (promise) {
14. // Do something
15. }
16. }
```

## 规则集

```
1. plugin:@typescript-eslint/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](<../../../Code Linter代码检查/ide-code-linter.md>)。
