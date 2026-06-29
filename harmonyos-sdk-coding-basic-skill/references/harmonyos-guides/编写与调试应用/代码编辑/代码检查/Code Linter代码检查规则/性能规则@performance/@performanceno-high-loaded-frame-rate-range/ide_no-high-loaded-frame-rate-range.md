---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_no-high-loaded-frame-rate-range
title: @performance/no-high-loaded-frame-rate-range
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 性能规则@performance > @performance/no-high-loaded-frame-rate-range
category: harmonyos-guides
scraped_at: 2026-06-01T15:22:43+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:ecc23b7df06fddab90a1b1f0fd7b7b73885614f9b0193fc0317c3ad86a728018
---
不允许锁定最高帧率运行。

## 规则配置

```
1. // code-linter.json5
2. {
3. "rules": {
4. "@performance/no-high-loaded-frame-rate-range": "warn",
5. }
6. }
```

## 选项

该规则无需配置额外选项。

## 正例

```
1. import { displaySync } from '@kit.ArkGraphics2D';
2. let sync = displaySync.create();
3. sync.setExpectedFrameRateRange({
4. expected: 60,
5. min: 45,
6. max: 60,
7. });
```

## 反例

```
1. import { displaySync } from '@kit.ArkGraphics2D';
2. let sync = displaySync.create();
3. sync.setExpectedFrameRateRange({
4. expected: 120,
5. min: 120,
6. max: 120,
7. });
```

## 规则集

```
1. plugin:@performance/all
2. plugin:@performance/recommended
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](<../../../Code Linter代码检查/ide-code-linter.md>)。
