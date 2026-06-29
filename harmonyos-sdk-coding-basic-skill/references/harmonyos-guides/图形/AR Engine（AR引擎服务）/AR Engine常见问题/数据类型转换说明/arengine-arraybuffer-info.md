---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arengine-arraybuffer-info
title: 数据类型转换说明
breadcrumb: 指南 > 图形 > AR Engine（AR引擎服务） > AR Engine常见问题 > 数据类型转换说明
category: harmonyos-guides
scraped_at: 2026-06-01T14:56:17+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:de8f7d02fd9a8667416cecd08f5771665f9b891ef0e01aab39af42f47c32968b
---
在开发AR应用时，部分数据类型需要转换才能使用，以下进行汇总及示例。

## ArrayBuffer

在一些不支持接收ArrayBuffer数据类型的方法中，需要将其反序列化为int32或者float32类型，涉及转换的接口列表如下：

| 接口名 | 描述 |
| --- | --- |
| [ImageComponent](<../../../../../harmonyos-references/AR Engine（AR引擎服务）/ArkTS API/arEngine（AR增强现实能力）/arengine-api-arengine.md#imagecomponent>) | 参数buffer为ArrayBuffer类型，可转换为int32。 |
| [ARPlane.getPolygonXZ](<../../../../../harmonyos-references/AR Engine（AR引擎服务）/ArkTS API/arEngine（AR增强现实能力）/arengine-api-arengine.md#arplanegetpolygonxz>) | 返回值为ArrayBuffer类型，可转换为float32。 |
| [ARSceneMesh.getVertices](<../../../../../harmonyos-references/AR Engine（AR引擎服务）/ArkTS API/arEngine（AR增强现实能力）/arengine-api-arengine.md#arscenemeshgetvertices>) | 返回值为ArrayBuffer类型，可转换为float32。 |
| [ARSceneMesh.getVertexNormals](<../../../../../harmonyos-references/AR Engine（AR引擎服务）/ArkTS API/arEngine（AR增强现实能力）/arengine-api-arengine.md#arscenemeshgetvertexnormals>) | 返回值为ArrayBuffer类型，可转换为float32。 |
| [ARSceneMesh.getTriangleIndices](<../../../../../harmonyos-references/AR Engine（AR引擎服务）/ArkTS API/arEngine（AR增强现实能力）/arengine-api-arengine.md#arscenemeshgettriangleindices>) | 返回值为ArrayBuffer类型，可转换为int32。 |
| [ARSemanticDensePointData](<../../../../../harmonyos-references/AR Engine（AR引擎服务）/ArkTS API/arEngine（AR增强现实能力）/arengine-api-arengine.md#arsemanticdensepointdata>) | 参数id为ArrayBuffer类型，可转换为int32。 |
| [ARSemanticDensePointData](<../../../../../harmonyos-references/AR Engine（AR引擎服务）/ArkTS API/arEngine（AR增强现实能力）/arengine-api-arengine.md#arsemanticdensepointdata>) | 参数position为ArrayBuffer类型，可转换为float32。 |
| [ARSemanticDensePointData](<../../../../../harmonyos-references/AR Engine（AR引擎服务）/ArkTS API/arEngine（AR增强现实能力）/arengine-api-arengine.md#arsemanticdensepointdata>) | 参数color为ArrayBuffer类型，可转换为int32。 |

转换的示例如下：

```
1. // ArrayBuffer转float32
2. function arrayBufferFloat32ToNumber(buffer: ArrayBuffer): number[] {
3. let view: Float32Array = new Float32Array(buffer);
4. let numberArray: number[] = Array.from(view);
5. return numberArray;
6. }

8. // ArrayBuffer转int32
9. function arrayBufferInt32ToNumber(buffer: ArrayBuffer): number[] {
10. let view: Int32Array = new Int32Array(buffer);
11. let numberArray: number[] = Array.from(view);
12. return numberArray;
13. }
```
