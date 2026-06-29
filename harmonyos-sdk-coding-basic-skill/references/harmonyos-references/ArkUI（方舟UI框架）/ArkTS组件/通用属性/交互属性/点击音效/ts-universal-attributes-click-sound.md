---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-click-sound
title: 点击音效
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 通用属性 > 交互属性 > 点击音效
category: harmonyos-references
scraped_at: 2026-06-01T15:40:02+08:00
doc_updated_at: 2026-04-30
content_hash: sha256:3599df4eab16da6379d012874e5eb65dbbe32223ac2ca317b6192ecd0b92a4b1
---
设置组件是否启用默认点击音效。

说明

从API version 24开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

## enableClickSoundEffect

PhonePC/2in1TabletTVWearable

enableClickSoundEffect(enabled: boolean | undefined): T

设置组件是否启用默认点击音效。是否能够发音依赖设备声音相关的设置，如静音模式下不会播放音效。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从API version 24开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异**：该接口在TV中可正常调用，在其他设备中无效果。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enabled | boolean | undefined | 是 | 设置此组件是否启用默认点击音效。  true表示启用默认点击音效；false表示禁用默认点击音效。  值为undefined时，启用默认点击音效。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

## 示例

PhonePC/2in1TabletTVWearable

### 示例1（启用默认点击音效）

该示例通过配置enableClickSoundEffect属性，实现组件禁用默认点击音效，开发者可以在onClick回调中调用音频相关接口自定义发音。自定义发音可参考[SoundPool播放短音频指南](<../../../../../../harmonyos-guides/媒体/Media Kit（媒体服务）/媒体开发指导(ArkTS)/播放/使用SoundPool播放短音频(ArkTS)/using-soundpool-for-playback.md>)。

从API version 24开始，新增[enableClickSoundEffect](ts-universal-attributes-click-sound.md#enableclicksoundeffect)属性。

```
1. @Entry
2. @Component
3. struct Index {
4. build() {
5. Column() {
6. Button('点击')
7. .fontSize('20dp')
8. .height('60')
9. .width('200')
10. .enableClickSoundEffect(false)
11. .onClick(() => {
12. // 此处自定义发音，参考SoundPool播放短音频指南
13. })
14. }
15. .width('100%')
16. .height('100%')
17. .justifyContent(FlexAlign.Center)
18. .alignItems(HorizontalAlign.Center)
19. }
20. }
```
