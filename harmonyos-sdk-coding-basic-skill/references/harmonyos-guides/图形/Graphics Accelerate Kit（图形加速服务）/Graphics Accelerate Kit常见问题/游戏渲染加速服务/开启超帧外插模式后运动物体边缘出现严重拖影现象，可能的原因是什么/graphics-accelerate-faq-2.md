---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/graphics-accelerate-faq-2
title: 开启超帧外插模式后运动物体边缘出现严重拖影现象，可能的原因是什么
breadcrumb: 指南 > 图形 > Graphics Accelerate Kit（图形加速服务） > Graphics Accelerate Kit常见问题 > 游戏渲染加速服务 > 开启超帧外插模式后运动物体边缘出现严重拖影现象，可能的原因是什么
category: harmonyos-guides
scraped_at: 2026-06-11T15:01:45+08:00
doc_updated_at: 2026-05-18
content_hash: sha256:c988ed7b4d8656e09416708d146dc1fa11a8ffa068a37769c70be57ff530913f
---

由于外插模式需要标记模板缓冲（Stencil Buffer）的第8位用于区分静态物体和动态物体，即静态物体模板值第8位标记成0，动态物体模板值第8位标记成1，模板缓冲的低7位模板值开发者可自行设置。如果标记错误或漏标记，可能会在动态物体边缘产生严重的拖影现象。

**现象描述**

Demo中运动角色出现头身分离等严重拖影现象，角色头部向右偏。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c9/v3/NhiEItiVRU2R5JlJ8B64Jg/zh-cn_image_0000002592379096.png?HW-CC-KV=V1&HW-CC-Date=20260611T070144Z&HW-CC-Expire=86400&HW-CC-Sign=95D11B52036B31CF8F29CD51E5A1320F2609FC1D843F3D4979477EE95E8BA4C0)

**原因分析**

通过抓帧查看模板缓冲中的模板值，发现头发区域模板值为0，身体区域模板值为0x80。由于角色头、身均属于运动目标区域，应该将所有运动物体区域的模板值第8位标记为1。错误的头部区域模板值导致超帧效果出现头身分离的严重拖影现象。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f1/v3/n9eaA_IoS8qZFfD05RCxWQ/zh-cn_image_0000002622858603.png?HW-CC-KV=V1&HW-CC-Date=20260611T070144Z&HW-CC-Expire=86400&HW-CC-Sign=1CFDFAD1FE7AA621E0C4F7CE61C078CDACDD52AFD00267C7B62F138B19C8D308)

**处理步骤**

基于分析结论，造成头身分离拖影现象的主要原因是运动区域模板值未统一标记为1xxx xxxx。因此将运动角色头发和面部区域的模板值统一改为0x80，保持和身体模板值一致，头身分离的拖影现象消失，效果如下图所示。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/38/v3/g30cvxfeQbiHhr48qoKisQ/zh-cn_image_0000002622698725.png?HW-CC-KV=V1&HW-CC-Date=20260611T070144Z&HW-CC-Expire=86400&HW-CC-Sign=1826B57546547A3E6A5975AB2B158A97ADF1379F5AE51046E296ECB54BEAFA41)

**代码示例**

检查动态物体材质Shader中的模板值是否设置正确，即静态物体模板值标记为0xxx xxxx，动态物体模板值标记为1xxx xxxx。

```
1. Shader "Standard_with_stencil"
2. {
3. Properties
4. {
5. /* ... */
6. _LightingStencilRef("Lighting Stencil Reference", Float) = 128 // 将动态物体材质模板值改为1xxx xxxx，消除头身分离现象
7. [Enum(UnityEngine.Rendering.CompareFunction)] _LightingStencilComp("Lighting Stencil Comparison", Float) = 8
8. _StencilReadMask("Stencil Read Mask", Float) = 255
9. _StencilWriteMask("Stencil Write Mask", Float) = 255
10. }
11. SubShader
12. {
13. /* ... */
14. Pass
15. {
16. /* ... */
17. Stencil
18. {
19. Ref[_LightingStencilRef]
20. Comp[_LightingStencilComp]
21. ReadMask[_StencilReadMask]
22. WriteMask[_StencilWriteMask]
23. Pass Replace
24. }
25. }
26. }
27. }
```

说明

不同管线的Shader中需要配置模板值的Pass不同，如下：

* 团结引擎URP管线

  在每个有DepthOnly或DepthNormals的Pass中，即出现Tags {"LightMode" = "DepthOnly" }或Tags {"LightMode" = "DepthNormals" }的Pass，配置模板值。
* 团结引擎Build-in管线

  在每个有ForwardBase或ForwardAdd的Pass中，即出现Tags {"LightMode" = "ForwardBase" }或Tags {"LightMode" = "ForwardAdd" }的Pass，配置模板值。
