---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/medialibrary-asset-judgment-faq
title: 如何正确判断媒体资源类型
breadcrumb: 指南 > 媒体 > Media Library Kit（媒体文件管理服务） > Media Library Kit常见问题 > 如何正确判断媒体资源类型
category: harmonyos-guides
scraped_at: 2026-06-01T11:31:17+08:00
doc_updated_at: 2026-05-26
content_hash: sha256:bfd548926d4895faff7bcda5e4fde88317c279173647bdd98e2495889e256431
---
[Media Library Kit](<../../Media Library Kit 简介/photoaccesshelper-overview.md>)（媒体文件管理服务）提供了媒体资源的管理能力，开发者可以访问和管理相册中的媒体信息。针对不同的媒体资源类型，系统会提供相应的判断方式，本文档提供了相关示例方法以便开发者使用。

## 使用mimeType字段来判断资源类型

开发者可以通过判断mimeType的字符串前缀来区分媒体类型，具体判断方式如下：

* 当mimeType以'image/'开头时，表示该媒体文件为图片。
* 当mimeType以'video/'开头时，表示该媒体文件为视频。

**示例：**

```
1. function getMediaTypeByMimeType(mimeType: string): string {
2. if (mimeType.startsWith('video/')) {
3. return 'video';
4. } else if (mimeType.startsWith('image/')) {
5. return 'image';
6. }
7. return 'unknown';
8. }
```

[MediaLibraryPickerUtils.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/Media/Picker/PickerMediaLibrarySample/entry/src/main/ets/common/utils/MediaLibraryPickerUtils.ets#L234-L243)

## 通过URI判断连拍图资源

未重命名连拍照片的URI中包含特定标识，开发者可以通过检查URI中的关键字来判断是否为连拍图资源。

* 当URI同时包含burst和cover时，表示该资源为连拍封面。
* 当URI仅包含burst时，表示该资源为连拍照片（非封面）。
* 当URI中不包含burst关键字时，表示该资源为非连拍图。

**示例：**

```
1. function getBurstTypeByUri(uri: string): string {
2. const hasBurst = uri.includes('burst');
3. const hasCover = uri.includes('cover');

5. if (hasBurst && hasCover) {
6. return '连拍封面';
7. } else if (hasBurst) {
8. return '连拍照片';
9. }
10. return '非连拍图';
11. }
```

[MediaLibraryPickerUtils.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/Media/Picker/PickerMediaLibrarySample/entry/src/main/ets/common/utils/MediaLibraryPickerUtils.ets#L249-L261)
