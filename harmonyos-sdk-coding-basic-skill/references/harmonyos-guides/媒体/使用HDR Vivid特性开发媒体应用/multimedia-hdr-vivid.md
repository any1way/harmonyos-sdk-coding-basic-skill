---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/multimedia-hdr-vivid
title: 使用HDR Vivid特性开发媒体应用
breadcrumb: 指南 > 媒体 > 使用HDR Vivid特性开发媒体应用
category: harmonyos-guides
scraped_at: 2026-06-01T11:26:33+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:39341275cf281399b2c96b450104cec8540cf1e7b8b474bb632e67c357782a71
---
[HDR Vivid](https://www.theuwa.com/standard?cate=3)是UWA认证的动态HDR视频标准，在HarmonyOS平台上，开发者能够利用HDR Vivid的特性，开发媒体类应用，为用户呈现高动态范围和广色域的视觉体验。作为新一代高动态范围图像标准，HDR Vivid贯穿内容创作、平台支持和设备显示，为用户带来更宽广的色彩范围、更细腻的层次表现、更显著的明暗对比，以及更智能的动态元数据处理，助力用户领略世界的真实色彩。

## HDR Vivid视频

应用只需调用媒体领域提供的API，即可接入HarmonyOS的HDR Vivid视频采集、转码和解码显示功能，基于HDR Vivid标准，制作出高质量的视频。

| 类别 | 开发指导 | 提供能力的Kit |
| --- | --- | --- |
| 采集 | [HDR Vivid相机录像](<../Camera Kit（相机服务）/开发相机应用基础能力(ArkTS)/HDR Vivid相机录像(ArkTS)/camera-hdr-recording.md>) | Camera Kit |
| 编码 | [HDR Vivid视频录制](<../AVCodec Kit（音视频编解码服务）/音视频编解码/HDR Vivid能力/HDR Vivid视频录制/hdr-vivid-video-recorder.md>) | AVCodec Kit |
| 解码 | [HDR Vivid视频播放](<../AVCodec Kit（音视频编解码服务）/音视频编解码/HDR Vivid能力/HDR Vivid视频播放/hdr-vivid-video-player.md>) | AVCodec Kit |
| 转换 | [视频解码支持HDRVivid2SDR](<../AVCodec Kit（音视频编解码服务）/音视频编解码/HDR Vivid能力/视频解码支持HDRVivid2SDR/hdrvivid2sdr.md>) | AVCodec Kit |
| 转换 | [HDR Vivid视频动态元数据生成](<../Media Kit（媒体服务）/媒体开发指导(CC++)/视频处理/视频动态元数据生成/generate-video-dynamic-metadata.md>) | Media Kit |
| 转换 | [HDR视频色彩空间转换](<../Media Kit（媒体服务）/媒体开发指导(CC++)/视频处理/视频色彩空间转换/video-csc.md>) | Media Kit |

## HDR Vivid图片

应用只需调用媒体领域提供的API，即可接入HarmonyOS的HDR Vivid图片采集、转码和解码显示功能，基于HDR Vivid标准，制作出高质量的图片。

| 类别 | 开发指导 | 提供能力的Kit |
| --- | --- | --- |
| 采集 | [HDR Vivid相机拍照](<../Camera Kit（相机服务）/开发相机应用基础能力(ArkTS)/HDR Vivid相机拍照(ArkTS)/camera-hdr-shooting.md>) | Camera Kit |
| 编码 | [HDR Vivid图片编码](<../Image Kit（图片处理服务）/图片开发指导(CC++)/图片编码/使用Image_NativeModule完成图片编码/image-packer-c.md>) | Image Kit |
| 解码 | [HDR Vivid图片解码](<../Image Kit（图片处理服务）/图片开发指导(CC++)/图片解码/使用Image_NativeModule完成图片解码/image-source-c.md>) | Image Kit |
| 转换 | [HDR图片动态元数据生成](<../Image Kit（图片处理服务）/图片开发指导(CC++)/图片编辑和处理/使用ImageProcessing处理图片/图片动态元数据生成/image-dynamic-metadata-generation.md>) | Image Kit |
| 转换 | [HDR图片色彩空间转换](<../Image Kit（图片处理服务）/图片开发指导(CC++)/图片编辑和处理/使用ImageProcessing处理图片/图片色彩空间转换/image-csc.md>) | Image Kit |
| 转换 | [单层HDR图片转换双层](<../Image Kit（图片处理服务）/图片开发指导(CC++)/图片编辑和处理/使用ImageProcessing处理图片/单层HDR图片转换双层/hdr-single-to-dual.md>) | Image Kit |
| 转换 | [双层HDR图片转换单层](<../Image Kit（图片处理服务）/图片开发指导(CC++)/图片编辑和处理/使用ImageProcessing处理图片/双层HDR图片转换单层/hdr-dual-to-single.md>) | Image Kit |
