---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hp-arkui-no-high-freq-log
title: @performance/hp-arkui-no-high-freq-log（已下线）
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 性能规则@performance > @performance/hp-arkui-no-high-freq-log（已下线）
category: harmonyos-guides
scraped_at: 2026-06-01T15:22:00+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:81f4e13faffa36037955421b016ec6ad5502a298e3925fdfc4d517ebed25f0a9
---
建议在正式发布的版本中，注释掉或删除日志打印代码。该规则已于5.0.3.403版本下线。

## 正例

```
1. import hilog from '@ohos.hilog';
2. @Entry
3. @Component
4. struct MyComponent{
5. build() {
6. Column() {
7. Scroll()
8. .onScroll(() => {
9. //正例
10. //hilog.info(1001, 'Index', 'onScroll')
11. // do something
12. })
13. }
14. }
15. }
```

## 反例

```
1. import hilog from '@ohos.hilog';
2. @Entry
3. @Component
4. struct MyComponent{
5. build() {
6. Column() {
7. Scroll()
8. .onScroll(() => {
9. // 高频操作中不建议写日志
10. hilog.info(1001, 'Index', 'onScroll')
11. // do something
12. })
13. }
14. }
15. }
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](<../../../Code Linter代码检查/ide-code-linter.md>)。
