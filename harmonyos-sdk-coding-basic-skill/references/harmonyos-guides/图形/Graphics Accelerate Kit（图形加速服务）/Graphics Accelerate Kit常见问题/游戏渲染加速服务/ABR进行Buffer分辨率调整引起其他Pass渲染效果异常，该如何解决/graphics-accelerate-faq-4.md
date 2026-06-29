---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/graphics-accelerate-faq-4
title: ABR进行Buffer分辨率调整引起其他Pass渲染效果异常，该如何解决
breadcrumb: 指南 > 图形 > Graphics Accelerate Kit（图形加速服务） > Graphics Accelerate Kit常见问题 > 游戏渲染加速服务 > ABR进行Buffer分辨率调整引起其他Pass渲染效果异常，该如何解决
category: harmonyos-guides
scraped_at: 2026-06-11T15:01:47+08:00
doc_updated_at: 2026-05-18
content_hash: sha256:3b5c0c266a3196a43b08fc434aaae8c16a6ab2674e53e89f4c7ece0ff0f854b9
---
**现象描述**

以团结引擎URP管线为例，ABR对DrawOpaqueObjects绑定的Buffer进行分辨率调整时会引起SSAO shadow效果异常。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6c/v3/uHAZ_AXZQMyFzkD4_SKXfw/zh-cn_image_0000002592219164.png?HW-CC-KV=V1&HW-CC-Date=20260611T070146Z&HW-CC-Expire=86400&HW-CC-Sign=85F703FBF8A0359885BD4BB6B2965F5F8EB726C4DA1DFEEA0CDBD4C7943EFEEC)

**原因分析**

通过上述URP管线可以看到，SSAO在渲染管线中是一个“前处理”，SSAO输出的图像会作为DrawOpaqueObjects的输入。当ABR对DrawOpaqueObjects绑定的Buffer进行自适应分辨率调整时，SSAO输出的图像为原始分辨率，而DrawOpaqueObjects绑定的Buffer使用低分辨率，分辨率不一致导致SSAO shadow效果异常。

**处理步骤**

* 仅支持渲染线程的游戏引擎处理步骤

  + **方案1**：调整渲染管线，将SSAO作为“后处理”，SSAO不受DrawOpaqueObjects绑定的Buffer分辨率影响。

    在URP资产中勾选“After Opaque”：

    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f1/v3/jUU5-tZmRcSg--BXSoqHCA/zh-cn_image_0000002592379098.png?HW-CC-KV=V1&HW-CC-Date=20260611T070146Z&HW-CC-Expire=86400&HW-CC-Sign=BA0D9CF2427F72F7FF31E1A9022FF9EC99BED37CB07BF7ADFE60AC192AF06B9D)
  + **方案2**：获取实时的ABR Buffer分辨率因子，并根据Buffer分辨率因子对相关渲染数据进行同步调整。

    SSAO的shader会根据scaledScreenParams参数进行计算，该变量与渲染分辨率相关，在集成ABR后，scaledScreenParams需要根据实时的ABR Buffer分辨率因子调整。

    对于团结引擎，可在ScriptableRenderer.cs的SetPerCameraShaderVariables函数中根据Buffer分辨率因子设置scaledScreenParams参数。

    ```
    1. void SetPerCameraShaderVariables(CommandBuffer cmd, ref CameraData cameraData, bool isTargetFlipped)
    2. {
    3. Camera camera = cameraData.camera;
    4. float scaledCameraWidth = (float)cameraData.cameraTargetDescriptor.width;
    5. float scaledCameraHeight = (float)cameraData.cameraTargetDescriptor.height;
    6. // scale为通过HMS_ABR_GetScale接口获取的ABR Buffer分辨率因子
    7. scaledCameraWidth *= scale;
    8. scaledCameraHeight *= scale;
    9. cmd.SetGlobalVector(ShaderPropertyId.scaledScreenParams, new Vector4(scaledCameraWidth, scaledCameraHeight, 1.0f + 1.0f / scaledCameraWidth, 1.0f + 1.0f / scaledCameraHeight));
    10. }
    ```
* 支持渲染线程、RHI线程的游戏引擎处理步骤

  对于同时支持渲染线程、RHI线程的游戏引擎，而且RHI线程延迟于渲染线程的场景，渲染线程通过[HMS\_ABR\_GetScale](<../../../../../../harmonyos-references/Graphics Accelerate Kit（图形加速服务）/C API/模块/GraphicsAccelerate/_graphics_accelerate.md#hms_abr_getscale>)接口获取的ABR Buffer分辨率因子无法解决上述问题。

  对于该场景，渲染线程在Buffer渲染后调用[HMS\_ABR\_GetNextScale](<../../../../../../harmonyos-references/Graphics Accelerate Kit（图形加速服务）/C API/模块/GraphicsAccelerate/_graphics_accelerate.md#hms_abr_getnextscale>)接口获取下一帧的ABR Buffer分辨率因子，并根据Buffer分辨率因子对相关渲染数据进行同步调整。

  ```
  1. // 在Buffer渲染后调用
  2. float scale = 1.0f;
  3. errorCode = HMS_ABR_GetNextScale(context_, &scale);
  4. if (errorCode != ABR_SUCCESS) {
  5. GOLOGE("HMS_ABR_GetNextScale execution failed, error code: %d.", errorCode);
  6. }

  8. // 根据Buffer分辨率因子对渲染数据进行同步调整
  9. void SetViewUniformParameters()
  10. {
  11. ViewUniformParameters.BufferSize.X = (int)(ViewUniformParameters.BufferSize.X * scale);
  12. ViewUniformParameters.BufferSize.Y = (int)(ViewUniformParameters.BufferSize.Y * scale);
  13. ViewUniformParameters.BufferInvSize.X /= scale;
  14. ViewUniformParameters.BufferInvSize.Y /= scale;
  15. }
  ```
