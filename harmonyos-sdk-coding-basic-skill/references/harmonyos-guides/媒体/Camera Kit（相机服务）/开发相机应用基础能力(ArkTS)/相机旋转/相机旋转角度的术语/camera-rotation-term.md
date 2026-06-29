---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/camera-rotation-term
title: 相机旋转角度的术语
breadcrumb: 指南 > 媒体 > Camera Kit（相机服务） > 开发相机应用基础能力(ArkTS) > 相机旋转 > 相机旋转角度的术语
category: harmonyos-guides
scraped_at: 2026-06-11T14:56:03+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:c9140687fbad4591b9f2cf29142338491753cb5acc6e738f30de80f2863dbf44
---
在适配相机旋转角度中涉及设备方向、镜头角度、屏幕显示角度等多个术语，开发者可以了解相关概念，帮助理解框架的运作机制。

## 设备自然方向

**设备自然方向**指设备默认的使用方向，以手机为例，如图所示，手机的自然方向为竖屏且充电口向下。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6a/v3/zf_OqcdUSf-NBwVEZ8QU0A/zh-cn_image_0000002592378938.png?HW-CC-KV=V1&HW-CC-Date=20260611T065602Z&HW-CC-Expire=86400&HW-CC-Sign=6E5DF391665D4251FBC5A0257DA9835D380CD553C320CD61F5085D2CD282EF69)

## 屏幕显示方向

**屏幕显示方向**指当前用户视角下，设备正确的显示方向。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e2/v3/NGQqvwbiTjSOkJOj05UYeQ/zh-cn_image_0000002622858445.png?HW-CC-KV=V1&HW-CC-Date=20260611T065602Z&HW-CC-Expire=86400&HW-CC-Sign=62A9834B52EB801690273A07BCB84A87C773560B22329971EEBDF56AA962E7C8)

## 屏幕旋转角度

显示设备的屏幕顺时针旋转角度，简称为**屏幕旋转角度**，即设备从自然方向到当前方向的顺时针夹角。

如图所示，图示夹角即为屏幕旋转角度，可通过[Display.rotation](<../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS API/屏幕管理/@ohos.display (屏幕属性)/js-apis-display.md#属性>)获取。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/65/v3/ZJ4322VbRiiLYU6LBRxU6g/zh-cn_image_0000002622698567.png?HW-CC-KV=V1&HW-CC-Date=20260611T065602Z&HW-CC-Expire=86400&HW-CC-Sign=E57857D587AFB35533AC5D2E9817D28A0BE2AC2C6209D9209F72B07CC8FB2C97)

## 相机镜头安装角度

**相机镜头安装角度**指相机采集图像方向到设备自然方向在顺时针方向的夹角。

以手机为例，手机后置相机传感器是横屏安装的，当手机在竖屏方向使用后置相机镜头拍摄时，相机采集到的原始图像方向如图所示。

此时图像需要顺时针旋转90度，才能与设备自然方向保持一致，所以**后置相机的镜头角度为90度**。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/51/v3/xe7bFdrUTkucUQla4_I23A/zh-cn_image_0000002592219006.png?HW-CC-KV=V1&HW-CC-Date=20260611T065602Z&HW-CC-Expire=86400&HW-CC-Sign=6E34B242BA3A60518B9E07A9FE61942D5A8FD6BB20C896E37434E190B0D69662)

而手机前置镜头，是朝向使用者的，当手机在竖屏方向使用前置相机镜头拍摄时，出图方向与后置出图方向互为镜像，如下图所示，**前置相机的镜头角度为270度**。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d1/v3/T67wJzePSUqFsNLV96Tk-Q/zh-cn_image_0000002592378940.png?HW-CC-KV=V1&HW-CC-Date=20260611T065602Z&HW-CC-Expire=86400&HW-CC-Sign=89EBA60F918CBE378823BDF23544B72635DCA45D11E8A9C0A063AA56FEE86004)

## 预览旋转角度

说明

开发者可参考以下章节，了解框架实现的机制，在实际开发过程中，推荐通过接口[获取预览旋转角度](../适配相机旋转角度(ArkTS)/camera-rotation-angle-adaptation.md#预览)。

在预览时，图像旋转角度与屏幕显示旋转角度相关。系统将以原始图像方向为基线，根据相机镜头角度和屏幕显示补偿角度，旋转图像。

计算公式：图像旋转角度=镜头安装角度+屏幕显示补偿角度，屏幕显示补偿角度的值与屏幕旋转角度相等。

以手机设备为例展示相机在预览下如何处理图像，计算的角度设置给系统侧，作用于直接送显场景，应用自绘制参考[应用自绘制预览角度处理](camera-rotation-term.md#应用自绘制预览角度处理)。

| 设备和镜头方向 | 处理过程示意图 |
| --- | --- |
| **设备条件：**  手机竖屏、充电口向下。  使用后置相机拍摄。  **可得：**  - 后置相机镜头角度 = 90°  - 屏幕旋转角度= 0°，[Display.rotation](<../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS API/屏幕管理/@ohos.display (屏幕属性)/js-apis-display.md#属性>) = 0  - **图像预览旋转角度 = 90°+0° = 90°** |  |
| **设备条件：**  手机横屏、充电口向左。  使用后置相机拍摄。  **可得：**  - 后置相机镜头角度 = 90°  - 屏幕旋转角度 = 90°，[Display.rotation](<../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS API/屏幕管理/@ohos.display (屏幕属性)/js-apis-display.md#属性>) = 1  - **图像预览旋转角度 = 90°+90° = 180°** |  |
| **设备条件：**  手机竖屏、充电口向上。  使用后置相机拍摄。  **可得：**  - 后置相机镜头角度 = 90°  - 屏幕旋转角度 = 180°，[Display.rotation](<../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS API/屏幕管理/@ohos.display (屏幕属性)/js-apis-display.md#属性>) = 2  - **图像预览旋转角度 = 90°+180° = 270°** |  |
| **设备条件：**  手机横屏、充电口向右。  使用后置相机拍摄。  **可得：**  - 后置相机镜头角度 = 90°  - 屏幕旋转角度 = 270°，[Display.rotation](<../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS API/屏幕管理/@ohos.display (屏幕属性)/js-apis-display.md#属性>) = 3  - **图像预览旋转角度 = 90°+270° = 0°** |  |
| **设备条件：**  手机竖屏、充电口向下。  使用前置相机拍摄。  **可得：**  - 前置相机镜头角度 = 270°  - 前置相机镜像出图  - 屏幕旋转角度= 0°，[Display.rotation](<../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS API/屏幕管理/@ohos.display (屏幕属性)/js-apis-display.md#属性>) = 0  - **图像预览旋转角度 = 270°+0° = 270°** |  |
| **设备条件：**  手机横屏、充电口向左。  使用前置相机拍摄。  **可得：**  - 前置相机镜头角度 = 270°  - 前置相机镜像出图  - 屏幕旋转角度 = 90°，[Display.rotation](<../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS API/屏幕管理/@ohos.display (屏幕属性)/js-apis-display.md#属性>) = 1  - **图像预览旋转角度 = 270°+90° =0°** |  |
| **设备条件：**  手机竖屏、充电口向上。  使用前置相机拍摄。  **可得：**  - 前置相机镜头角度 = 270°  - 前置相机镜像出图  - 屏幕旋转角度 = 180°，[Display.rotation](<../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS API/屏幕管理/@ohos.display (屏幕属性)/js-apis-display.md#属性>) = 2  - **图像预览旋转角度 = 270°+180° = 90°** |  |
| **设备条件：**  手机横屏、充电口向右。  使用前置相机拍摄。  **可得：**  - 前置相机镜头角度 = 270°  - 前置相机镜像出图  - 屏幕旋转角度 = 270°，[Display.rotation](<../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS API/屏幕管理/@ohos.display (屏幕属性)/js-apis-display.md#属性>) = 3  - **图像预览旋转角度 = 270°+270° = 180°** |  |

## 应用自绘制预览角度处理

应用自绘制场景是指应用获取图片后，通过libyuv、GL等图形处理库进行二次处理，生成新的图像数据并送到显示设备进行渲染绘制。

常见的实现方式是通过使用imageReceiver创建的回调流，应用层作为消费端，自行处理图片旋转等操作，以适应自绘制场景的预览角度需求。自绘制场景预览角度与[预览旋转角度](camera-rotation-term.md#预览旋转角度)中描述的场景存在细微差异。

主要差异体现在使用前置镜头拍摄预览的场景：

* 自绘制场景可以按照[预览旋转角度](camera-rotation-term.md#预览旋转角度)中的图示方式，先根据镜头的安装角度进行旋转，随后进行镜像处理，最后再次旋转以适应屏幕角度。然而，这种方式包含多个步骤，较为繁琐，不被推荐。
* 自绘制场景也可以采取先旋转再镜像的方式，这种方式需要考虑水平镜像和垂直镜像，具体的处理步骤如下图所示，代码实现可参考[自绘制场景预览角度的归一化处理](../适配相机旋转角度(ArkTS)/camera-rotation-angle-adaptation.md#自绘制场景预览角度的归一化处理)。

| 设备和镜头方向 | 处理过程示意图 |
| --- | --- |
| **设备条件：**  手机竖屏、充电口向下。  使用前置相机拍摄。  **可得：**  - 前置相机镜头角度 = 270°  - 前置相机镜像出图  - 屏幕旋转角度= 0°，[Display.rotation](<../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS API/屏幕管理/@ohos.display (屏幕属性)/js-apis-display.md#属性>) = 0  - **图像预览旋转角度 = 270°+0° = 270°** |  |
| **设备条件：**  手机横屏、充电口向左。  使用前置相机拍摄。  **可得：**  - 前置相机镜头角度 = 270°  - 前置相机镜像出图  - 屏幕旋转角度 = 90°，[Display.rotation](<../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS API/屏幕管理/@ohos.display (屏幕属性)/js-apis-display.md#属性>) = 1  - **图像预览旋转角度 = 270°+90° = 0°** |  |

## 拍照/录像角度

在拍照、录像时，图像旋转角度与设备重力方向（即设备旋转角度）相关。

* 使用后置相机拍摄时，图像旋转角度=[镜头安装角度](camera-rotation-term.md#相机镜头安装角度)+重力方向。
* 使用前置相机拍摄时，图像旋转角度=[镜头安装角度](camera-rotation-term.md#相机镜头安装角度)-重力方向。

| 设备和镜头方向 | 处理过程示意图 |
| --- | --- |
| **设备条件：**  手机横屏、充电口向左。  使用后置相机拍摄。  **可得：**  - 后置相机镜头角度 = 90°  - 设备旋转角度 = 90°  - **图像预览旋转角度 = 90°+90° = 180°** |  |

应用需要监听[SensorId.GRAVITY](<../../../../../../harmonyos-references/Sensor Service Kit（传感器服务）/ArkTS API/@ohos.sensor (传感器)/js-apis-sensor.md#gravity9-1>)事件，获取重力传感器在x、y、z三个方向上的数据，计算得出设备旋转角度，请参考[计算设备旋转角度](../适配相机旋转角度(ArkTS)/camera-rotation-angle-adaptation.md#计算设备旋转角度)。
