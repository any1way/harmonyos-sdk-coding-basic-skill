---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/image-transformation
title: 使用PixelMap完成图像变换
breadcrumb: 指南 > 媒体 > Image Kit（图片处理服务） > 图片开发指导(ArkTS) > 图片编辑和处理 > 使用PixelMap完成图像变换
category: harmonyos-guides
scraped_at: 2026-06-11T14:56:53+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:c91283cd434529fd4d2d3c8ea0bd223164e45043e93bd0a5bacc97ca2e485c0e
---
图片处理指对PixelMap进行相关的操作，如获取图片信息、裁剪、缩放、偏移、旋转、翻转、设置透明度、读写像素数据等。图片处理主要包括图像变换、[位图操作](../使用PixelMap完成位图操作/image-pixelmap-operation.md)，本文介绍图像变换。

## 开发步骤

图像变换相关API的详细介绍请参见[API参考](<../../../../../../harmonyos-references/Image Kit（图片处理服务）/ArkTS API/@ohos.multimedia.image (图片处理)/Interface (PixelMap)/arkts-apis-image-pixelmap.md>)。

1. 完成[图片解码](../../图片解码/使用ImageSource完成图片解码/image-decoding.md)，获取PixelMap对象。
2. 获取图片信息。

   ```
   1. import { BusinessError } from '@kit.BasicServicesKit';
   2. // 获取图片大小。
   3. pixelMap.getImageInfo().then( (info : image.ImageInfo) => {
   4. console.info('info.width = ' + info.size.width);
   5. console.info('info.height = ' + info.size.height);
   6. }).catch((err : BusinessError) => {
   7. console.error("Failed to obtain the image pixel map information.And the error is: " + err);
   8. });
   ```
3. 进行图像变换操作。

   原图：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3e/v3/PGNrTmohR_2zy-TQjl-JKw/zh-cn_image_0000002622858457.jpeg?HW-CC-KV=V1&HW-CC-Date=20260611T065652Z&HW-CC-Expire=86400&HW-CC-Sign=DF57CEE7E52DB60114CB56C4CCD7674B511F5C9D6BECD7E8335BD8C148A11264)

   * 裁剪

     ```
     1. // x：裁剪起始点横坐标0。
     2. // y：裁剪起始点纵坐标0。
     3. // height：裁剪高度400，方向为从上往下（裁剪后的图片高度为400）。
     4. // width：裁剪宽度400，方向为从左到右（裁剪后的图片宽度为400）。
     5. pixelMap.crop({x: 0, y: 0, size: { height: 400, width: 400 } });
     ```

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dc/v3/FjeWuYOSSQ2wM1NPEWwVcg/zh-cn_image_0000002622698579.jpeg?HW-CC-KV=V1&HW-CC-Date=20260611T065652Z&HW-CC-Expire=86400&HW-CC-Sign=1ED2BEC20EC68D1FD10B455FD8A9BAF32C9BB427C88215DB7BE16C9D8189E321)
   * 缩放

     ```
     1. // 宽为原来的0.5。
     2. // 高为原来的0.5。
     3. pixelMap.scale(0.5, 0.5);
     ```

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4f/v3/1jOpUobCTEGPLq1A-Y0HJQ/zh-cn_image_0000002592219018.jpeg?HW-CC-KV=V1&HW-CC-Date=20260611T065652Z&HW-CC-Expire=86400&HW-CC-Sign=FE33199AE6941A43B89687A334CFA356CB0FC0AF3E6D13AF1944F707CFC4A460)
   * 偏移

     ```
     1. // 向下偏移100。
     2. // 向右偏移100。
     3. pixelMap.translate(100, 100);
     ```

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/52/v3/5pGBkwdmSGum0TPUrQ3xcQ/zh-cn_image_0000002592378952.jpeg?HW-CC-KV=V1&HW-CC-Date=20260611T065652Z&HW-CC-Expire=86400&HW-CC-Sign=8F69614C06EAD45080CD4327B623D9E27C85E50571B26AE0C3D6B0F0C2E06AFC)
   * 旋转

     ```
     1. // 顺时针旋转90°。
     2. pixelMap.rotate(90);
     ```

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/30/v3/bK8ljkVERSu75ZdympFiQQ/zh-cn_image_0000002622858459.jpeg?HW-CC-KV=V1&HW-CC-Date=20260611T065652Z&HW-CC-Expire=86400&HW-CC-Sign=C0E182F711537FB91576B905DAF6B29F39B90EF9174523D668D7505946FBAF93)
   * 翻转

     ```
     1. // 垂直翻转。
     2. pixelMap.flip(false, true);
     ```

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5c/v3/hivGg62vQKe1Jf2i14Ybew/zh-cn_image_0000002622698581.jpeg?HW-CC-KV=V1&HW-CC-Date=20260611T065652Z&HW-CC-Expire=86400&HW-CC-Sign=FD16D63F1A8CC7F5D82D7B2F93BD5123FD1D2F28C236A81A8E0F5E1C11BE2774)

     ```
     1. // 水平翻转。
     2. pixelMap.flip(true, false);
     ```

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/18/v3/0GetJX7DR3a9g1rHXb_qEg/zh-cn_image_0000002592219020.jpeg?HW-CC-KV=V1&HW-CC-Date=20260611T065652Z&HW-CC-Expire=86400&HW-CC-Sign=F1CEEC5F83501282BA7E4E45824D77FDE30AC77C5600A8E15C77584D8A9B8187)
   * 透明度

     ```
     1. // 透明度0.5。
     2. pixelMap.opacity(0.5);
     ```

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/08/v3/chngZByESWarhg1sAfCWZA/zh-cn_image_0000002592378954.png?HW-CC-KV=V1&HW-CC-Date=20260611T065652Z&HW-CC-Expire=86400&HW-CC-Sign=8A16F5B7F3FEB2B8AE79CB341A62651A9E94B8C53AB55D328629C29BDF18E175)

## 示例代码

* [拼图](https://gitcode.com/HarmonyOS_Samples/game-puzzle)
