---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/image-overview
title: Image Kit简介
breadcrumb: 指南 > 媒体 > Image Kit（图片处理服务） > Image Kit简介
category: harmonyos-guides
scraped_at: 2026-06-11T14:56:43+08:00
doc_updated_at: 2026-03-20
content_hash: sha256:65cb871e28ea75c0d7b99c301a17bd40197e1b4e19ae6f26fc15464fd268f9ed
---
开发者通过调用Image Kit（图片处理服务）提供的接口，可以实现图片的解码、编码、编辑、元数据处理和图片接收等功能。

## 亮点/特征

* 编解码支持HEIF、JPEG、PNG、WebP等主流图片格式。
* 支持HDR图片编解码，给用户带来更高质量的色彩体验，还可以使用AI能力将SDR图片转换成HDR图片。
* 提供丰富的图片编辑和处理的能力，包括：图像变换、位图操作、滤镜效果等。
* 采用了高效的算法和优化策略，提高了图片处理的速度和效率。

## 基础概念

在开发前，需要了解以下基础概念：

* [PixelMap](<../../../../harmonyos-references/Image Kit（图片处理服务）/ArkTS API/@ohos.multimedia.image (图片处理)/Interface (PixelMap)/arkts-apis-image-pixelmap.md>)

  位图对象。可用于读取或写入像素数据，可以进行裁剪、缩放、平移、旋转、镜像等操作，并可直接传给[Image组件](<../../../应用框架/ArkUI（方舟UI框架）/UI开发 (ArkTS声明式开发范式)/媒体展示/显示图片 (Image)/arkts-graphics-display.md>)用于显示。还提供了获取图片信息、获取和设置图片色域、HDR元数据的方法。
* [Picture](<../../../../harmonyos-references/Image Kit（图片处理服务）/ArkTS API/@ohos.multimedia.image (图片处理)/Interface (Picture)/arkts-apis-image-picture.md>)

  多图对象。包含主图、辅助图和元数据。其中，主图包含了主要图像信息；辅助图用于存储与主图相关的附加信息；元数据用于存储与图片相关的其他信息。Picture提供获取主图、合成HDR图、获取辅助图、设置辅助图、获取元数据、设置元数据等方法。
* 图片解码

  将所支持格式的图片文件解码成PixelMap或Picture，以便在应用或系统中进行图片显示或图片处理。
* 图片编辑和处理

  对PixelMap进行相关的操作，如旋转、缩放、设置透明度、获取图片信息、读写像素数据等，操作时坐标系原点为左上角。
* 图片编码

  将PixelMap（或Picture）编码成不同格式的图片文件，用于后续处理，如保存、传输等。

## 使用方式

Image Kit提供了丰富的图片处理能力，开发者可按需灵活使用。既可以完整调用图片解码、编辑处理、编码的全流程；也可以图片解码后不做处理，直接将解码得到的PixelMap传给[Image组件](<../../../应用框架/ArkUI（方舟UI框架）/UI开发 (ArkTS声明式开发范式)/媒体展示/显示图片 (Image)/arkts-graphics-display.md>)显示。解码、编码过程中均提供了丰富的选项参数，可以满足各种实际开发场景的需求。

Image Kit支持对解码得到的PixelMap进行[位图操作](../图片开发指导(ArkTS)/图片编辑和处理/使用PixelMap完成位图操作/image-pixelmap-operation.md)，对目标图片中的部分区域进行处理；实现[图像变换](../图片开发指导(ArkTS)/图片编辑和处理/使用PixelMap完成图像变换/image-transformation.md)，可以对图片做裁剪、缩放、偏移、旋转、翻转、设置透明度等变换。

Image Kit支持通过[ImageEffect](../图片开发指导(CC++)/图片编辑和处理/使用ImageEffect编辑图片/image-effect-guidelines.md)为图片添加滤镜效果。

Image Kit还提供了读取和[编辑图片EXIF信息](../图片开发指导(ArkTS)/图片编辑和处理/编辑图片Exif信息/image-tool.md)的能力，可以获取和配置图片文件中的附加属性，如：宽、高、旋转方向等图片基本信息，光圈、焦距等图片拍照参数，经度、纬度等图片GPS信息等。

图片解码和图片编码的流程如图1和图2所示。图片解码得到的PixelMap可以直接用于图片显示、图片编辑和处理。

**图1** 图片解码流程示意图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fa/v3/tcFyuSoqRK-V_tm51Okc4w/zh-cn_image_0000002592219016.png?HW-CC-KV=V1&HW-CC-Date=20260611T065642Z&HW-CC-Expire=86400&HW-CC-Sign=5CED7FF8BC873F17AADA22D1CC2FC38EE48E999F0E2710EA5A113613B8BAFA5E)

**图2** 图片编码流程示意图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/79/v3/d69wtbbeQ5azDlTUaijorw/zh-cn_image_0000002592378950.png?HW-CC-KV=V1&HW-CC-Date=20260611T065642Z&HW-CC-Expire=86400&HW-CC-Sign=802B7AF9DE63122F2777D61DB8F81A277FA4DA033954319348929531E8A14FA9)

## 约束与限制

* **读写权限限制：**

  在图片处理中，可能需要使用用户图片，应用需要向用户申请对应的读写操作权限才能保证功能的正常运行，申请方式请参考[向用户申请授权](../../../系统/安全/程序访问控制/应用权限管控/申请应用权限/向用户申请授权/request-user-authorization.md)。
* **选择合适的C API接口：**

  Image Kit当前提供了两套C API接口，分别为依赖于JS对象的C API（[Image](<../../../../harmonyos-references/Image Kit（图片处理服务）/C API/模块/Image/capi-image.md>)）和不依赖于JS对象的C API（[Image\_NativeModule](<../../../../harmonyos-references/Image Kit（图片处理服务）/C API/模块/Image_NativeModule/capi-image-nativemodule.md>)）。

  + 依赖于JS对象的C接口

    这类接口可以完成图片编解码，图片接收器，处理图像数据等功能，相关示例代码可以参考[图片开发指导(依赖JS对象)(C/C++)](../图片开发指导(依赖JS对象)(不再推荐)/图片解码/image-decoding-native.md)节点下的内容。开发者可查看[Image](<../../../../harmonyos-references/Image Kit（图片处理服务）/C API/模块/Image/capi-image.md>)模块下的C API，确认API范围。这部分API在API version 11之前发布，在后续的版本不再增加新功能，**不再推荐使用**。
  + 不依赖于JS对象的C接口

    这类接口除了提供上述图片框架基础功能，还可以完成多图编解码等新特性，相关开发指导请参考[图片开发指导(C/C++)](../图片开发指导(CC++)/图片解码/使用Image_NativeModule完成图片解码/image-source-c.md)节点下的内容。开发者可查看[Image\_NativeModule](<../../../../harmonyos-references/Image Kit（图片处理服务）/C API/模块/Image_NativeModule/capi-image-nativemodule.md>)模块下的C API，确认API范围。这部分API从API version 12开始支持，并将持续演进，**推荐开发者使用**。

  注意

  两套C API不建议同时使用，在部分场景下存在不兼容的问题。

## 模拟器支持情况

本Kit暂不支持模拟器。

## 与相关Kit的关系

Image Kit提供图片编解码、图片接收、图片编辑和处理等能力，为Image组件、图库以及其他有图片相关需求的应用提供支撑。图片解码得到的PixelMap可以传给[Image组件](<../../../应用框架/ArkUI（方舟UI框架）/UI开发 (ArkTS声明式开发范式)/媒体展示/显示图片 (Image)/arkts-graphics-display.md>)显示。通过[ImageReceiver](<../../../../harmonyos-references/Image Kit（图片处理服务）/ArkTS API/@ohos.multimedia.image (图片处理)/Interface (ImageReceiver)/arkts-apis-image-imagereceiver.md>)（图片接收）可以实现[相机预览流二次处理](<../../Camera Kit（相机服务）/开发相机应用基础能力(CC++)/预览流二次处理(CC++)/native-camera-preview-imagereceiver.md>)。
