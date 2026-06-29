---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_return-await
title: @typescript-eslint/return-await
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > @typescript-eslint/return-await
category: harmonyos-guides
scraped_at: 2026-06-01T15:21:06+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:f9f9ad04169b2b99c0cae1299cbb7e2a756a96ca3488aa99b7102611906532a2
---
要求异步函数返回“await”。

## 规则配置

```
1. // code-linter.json5
2. {
3. "rules": {
4. "@typescript-eslint/return-await": "error"
5. }
6. }
```

## 选项

详情请参考[@typescript-eslint/return-await选项](https://typescript-eslint.nodejs.cn/rules/return-await/#options)。

## 正例

```
1. export async function validInTryCatch1() {
2. try {
3. return await Promise.resolve('try');
4. } catch (e) {
5. return await Promise.resolve('catch');
6. }
7. }
```

## 反例

```
1. export async function validInTryCatch1() {
2. try {
3. return Promise.resolve('try');
4. } catch (e) {
5. return Promise.resolve('catch');
6. }
7. }
```

## 规则集

```
1. plugin:@typescript-eslint/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](<../../../Code Linter代码检查/ide-code-linter.md>)。
