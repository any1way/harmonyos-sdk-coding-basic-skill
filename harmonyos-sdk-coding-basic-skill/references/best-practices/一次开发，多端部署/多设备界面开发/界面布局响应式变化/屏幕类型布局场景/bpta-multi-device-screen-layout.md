---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-multi-device-screen-layout
title: 屏幕类型布局场景
breadcrumb: 最佳实践 > 一次开发，多端部署 > 多设备界面开发 > 界面布局响应式变化 > 屏幕类型布局场景
category: best-practices
scraped_at: 2026-06-12T10:09:53+08:00
doc_updated_at: 2026-06-02
content_hash: sha256:b98406a032ada325f4629cf719178b2169902739d63cdae8b872fafc3968827a
---
## 概述

本文旨在从不同屏幕类型维度详细介绍开发多设备界面时常用的响应式布局方法，以帮助开发者更好地理解和应对跨设备界面设计的挑战。随着智能设备种类的日益丰富，市场上出现了各种尺寸和形状的屏幕，常见的设备如下：

* 手机：屏幕比例多样，存在横向和纵向两种使用场景，通常采用纵向模式。
* 平板（Pad）：提供更大的显示面积，存在横向和纵向两种使用场景。横向使用时，特别适合阅读和轻办公任务，能够支持更加复杂的用户界面。
* 折叠屏：如华为Mate X系列等，展开态可视为大方形屏，具有1:1的屏幕比例，且横向分辨率大于600vp。这类设备提供了极大的灵活性，既可以用作普通手机屏幕，也能扩展为小型平板使用。
* 三折叠：通过多个屏幕拼接实现超宽显示区域，尤其适用于需要展示大量信息的应用场景，如专业软件开发、视频编辑等。
* PC/2in1：提供更大的显示面积，一般为横向使用，为用户提供优质的视觉体验。
* 智能手表：屏幕呈现出经典的圆形外观，由于屏幕较小且形状特殊，内容布局需特别考虑信息的优先级和展示方式，以防止信息丢失，尤其是在边缘区域。

了解这些设备的特点及其屏幕尺寸差异后，可以根据不同的屏幕形态来设计适应性强、用户体验优良的响应式布局。需要考虑如何优化内容排版、图片缩放以及交互元素的放置，确保无论在哪种设备上，用户都能获得最佳的使用体验。

通过分析不同设备之间的差异，每一种屏幕形态都有其独特的应用场景和设计考量。本文从屏幕形态的角度深入探讨并围绕以下几种类别进行详细介绍：

* [超大屏横屏](bpta-multi-device-screen-layout.md#section191032013355)
* [大屏横屏](bpta-multi-device-screen-layout.md#section6493354468)
* [大屏竖屏](bpta-multi-device-screen-layout.md#section86231545125515)
* [大方形屏](bpta-multi-device-screen-layout.md#section12921201325714)
* [直板机竖屏](bpta-multi-device-screen-layout.md#section1919517165814)
* [直板机横屏](bpta-multi-device-screen-layout.md#section8373105265815)
* [小方形屏](bpta-multi-device-screen-layout.md#section1395830175918)
* [圆形屏](bpta-multi-device-screen-layout.md#section1298815351411)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ed/v3/UR8sOKyZRvS4RQIaVTzHQA/zh-cn_image_0000002552781908.png?HW-CC-KV=V1&HW-CC-Date=20260612T020944Z&HW-CC-Expire=86400&HW-CC-Sign=7C823F5EF3F746A3FF2431FCF1FA169AE742EA2FB1F364268C2AC43F82B33507 "点击放大")

上图清晰地展示了各个设备在不同屏幕形态下的断点，这为本文后续的深入探讨提供了坚实的基础。通过此图，可以直观看到超大屏横屏、大屏横屏、大屏竖屏、大方形屏、直板机竖屏、直板机横屏、小方形屏、圆形屏等多种屏幕形态下的设备断点。

说明

* 根据屏幕形态区分不同场景下的布局，均基于断点结合响应式布局与自适应布局实现，详情可参考[断点](../响应式布局/bpta-multi-device-responsive-layout.md#section1532120147301)。
* 同一设备由于横竖屏旋转的场景，会产生横向和纵向两种屏幕形态，旋转适配案例可参考[窗口方向](https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-multi-device-window-direction)。

## 超大屏横屏

超大屏横屏设备横向分辨率通常超过1440vp，具备更强的多任务处理能力，可同时展示多个应用或复杂布局，提升工作效率。典型设备应用开发参考[电脑应用开发](../../../../多端设备体验提升/电脑/电脑应用开发/bpta-pc-guide.md)等。适用于文档处理、数据分析、编程开发、内容创作等生产力场景。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/09/v3/j_0Vv6JgTQugCX-5obhvmQ/zh-cn_image_0000002321148150.png?HW-CC-KV=V1&HW-CC-Date=20260612T020944Z&HW-CC-Expire=86400&HW-CC-Sign=63766E8252DA2F4BDA0B51F8AC8E7663E54A3E32B808F7519E3A336F72D28901 "点击放大")

### 断点判断

| 横纵断点 | 设备 |
| --- | --- |
| 横向断点xl，纵向断点sm | PC/2in1 |

### 布局设计与实现

超大屏横屏设备独具大尺寸屏幕的优势，开发应用时建议采用响应式布局，以实时适应窗口尺寸变化，确保内容展示的最佳布局。在布局设计中，建议设置导航栏以提升可用性，并结合重复布局和多栏布局，充分利用屏幕空间，提升信息密度与用户的操作效率。

本章节提供针对超大屏横屏设备典型布局场景的开发指导。更多UX设计标准与规范，请参考[电脑应用UX体验标准](https://developer.huawei.com/consumer/cn/doc/design-guides/ux-guidelines-2in1-0000001777895636)、[电脑](https://developer.huawei.com/consumer/cn/doc/design-guides/2in1-0000001777531700)。

* 导航栏

  布局建议：当应用窗口宽度达到或超过1440vp，即横向断点为xl时，建议采用挪移布局，将底部导航栏变更为侧边分级导航栏。

  实现原理：使用[SideBarContainer](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/栅格与分栏/SideBarContainer/ts-container-sidebarcontainer.md)组件实现侧边栏效果，该组件需要传入两个子组件，分别表示侧边栏区域和内容区域。

  参考设计图如下：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/db/v3/oSRL2LVQTRG7EyFhBPEFRg/zh-cn_image_0000002355266657.png?HW-CC-KV=V1&HW-CC-Date=20260612T020944Z&HW-CC-Expire=86400&HW-CC-Sign=9701E0D7908B57C190AB8E04F512EA57432918CEA68FC9D6E17FA03C3290EDF0 "点击放大")
* 网格

  布局建议：当页面中需要展示较多元素内容时，建议采用重复布局，结合网格实现结构化与多样化的排布方式。

  实现原理：网格布局通过[Grid](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/滚动与滑动/Grid/ts-container-grid.md)组件实现。在不同断点下，设置不同的列数（[columnsTemplate](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/滚动与滑动/Grid/ts-container-grid.md#columnstemplate)）和行数（[rowsTemplate](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/滚动与滑动/Grid/ts-container-grid.md#rowstemplate)），即可呈现网格的多端效果。

  参考设计图如下：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/70/v3/qfTRirIFRvyt-XwFPsVv6Q/zh-cn_image_0000002321307946.png?HW-CC-KV=V1&HW-CC-Date=20260612T020944Z&HW-CC-Expire=86400&HW-CC-Sign=62113264EDED29325218F53909E2038B181E14CA722BA3B003C22A959C5308AD "点击放大")
* 列表

  布局建议：为了提高屏幕利用率，在大屏上展示更多的内容信息，可以根据断点展示更多列数实现重复布局。

  实现原理：[List](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/滚动与滑动/List/ts-container-list.md)组件提供[lanes](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/滚动与滑动/List/ts-container-list.md#lanes9)属性，支持设置布局列数或行数。在xl断点下，需要通过该属性设置更多列数。

  参考设计图如下：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/db/v3/efHgJr0NSHGO4CRVRb0HJg/zh-cn_image_0000002355146809.png?HW-CC-KV=V1&HW-CC-Date=20260612T020944Z&HW-CC-Expire=86400&HW-CC-Sign=AAB8B6D5D8F1513BA2F66EB606FA3CCD0D1CD12A9E1479F499CB5A318805F2A1 "点击放大")
* 三分栏

  布局建议：在超大屏横屏设备上，面对具有多级属性的内容，建议采用分栏布局，以清晰展现层级结构，同时提升信息展示密度和用户操作效率。

  实现原理：组合使用[Navigation](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/导航与切换/Navigation/ts-basic-components-navigation.md)组件和[SideBarContainer](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/栅格与分栏/SideBarContainer/ts-container-sidebarcontainer.md)组件即可实现。在xl断点下，设置SideBarContainer组件的[showSideBar](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/栅格与分栏/SideBarContainer/ts-container-sidebarcontainer.md#showsidebar)为true，显示侧边栏；设置Navigation的mode为Auto。

  参考设计图如下：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/12/v3/oNn0HZZUR061KtIaWH7zaw/zh-cn_image_0000002321148158.png?HW-CC-KV=V1&HW-CC-Date=20260612T020944Z&HW-CC-Expire=86400&HW-CC-Sign=865F9819CBC5A36E0BB4FF5B79A38A8C0C75B6736CB3DFF929760C06A50F7089 "点击放大")

## 大屏横屏

大屏横屏的特点主要表现为横向分辨率超过840vp，提供更宽广的显示视野和更强的信息承载能力，支持同时展示多个应用界面或复杂内容布局，显著提升多任务处理效率。典型设备有[Pad](../../../../多端设备体验提升/平板/平板应用开发/bpta-pad-guide.md)、[三折叠](../../../../多端设备体验提升/手机/三折叠应用开发/bpta-matext-guide.md)三屏态等。

这类屏幕拥有高分辨率，还具备出色的显示细腻度和广阔的可视区域，适合展示更加丰富和多层次的内容。在学习、娱乐或办公等多种应用场景中，这些屏幕能为用户提供更清晰的文字、更完整的界面布局以及更流畅的视觉体验，从而有效提升信息获取效率和使用舒适度，增强工作与学习的专注力及完成效率。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/64/v3/kI4hzKoiSumXeaHvJEBC-A/zh-cn_image_0000002577262247.png?HW-CC-KV=V1&HW-CC-Date=20260612T020944Z&HW-CC-Expire=86400&HW-CC-Sign=5596BBD0193BE998B67621C68157244F6C571323E545C847C6F8537464BC7ABA "点击放大")

### 断点判断

| 横纵断点 | 设备 |
| --- | --- |
| 横向断点lg，纵向断点sm | Pad（横向） |
| 三折叠三屏态（横向） |
| 折叠PC（半折叠态） |
| Pura 70 Ultra/Pro 系列、Pocket 2手机（横向） |
| 智慧屏（横向） |
| Pura X Max（展开态横向） |

### 布局设计与实现

大屏横屏设备独具大尺寸屏幕的优势，开发应用时建议采用响应式布局，以实时适应窗口尺寸变化，确保内容展示的最佳布局。

在大屏横屏布局设计中，为了简化操作流程并支持多层次信息架构，通常会设置导航栏以提高应用的可用性。充分利用大屏优势展示更多信息时，常采用重复元素布局来增加内容展示量。对于插图和文字结合的场景，小屏上采用上下排列的内容，在大屏上则多使用左右布局，使页面更加美观。此外，利用大屏的优势，可以通过侧边栏显示更多资讯。鉴于大屏横向空间充裕，在进行页面分栏布局时，为了提升视觉效果和丰富内容，应考虑使用多栏布局方案。

本章节提供针对大屏横屏设备典型布局场景的开发指导。更多UX设计标准与规范，请参考[大屏应用UX体验标准](https://developer.huawei.com/consumer/cn/doc/design-guides/ux-guidelines-large-screen-0000001807707561)、[平板](https://developer.huawei.com/consumer/cn/doc/design-guides/pad-0000001823654157)。

* 导航栏

  布局建议：当应用窗口宽度达到或超过840vp，横向断点为lg时，建议采用挪移布局，将底部导航栏变更为侧边导航栏。

  实现原理：导航页签使用[Tabs](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/导航与切换/Tabs/ts-container-tabs.md)组件实现，窗口为lg断点时，页签位于页面左侧，此时vertical=true，barPosition=Start。

  参考设计图如下：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/47/v3/3oLdYSJuQ5iEPxYjerPz9w/zh-cn_image_0000002321307954.png?HW-CC-KV=V1&HW-CC-Date=20260612T020944Z&HW-CC-Expire=86400&HW-CC-Sign=2CAB1839A99D45E93C68098D2DA618FB636C704F58419AB5137BA798BAFD5302 "点击放大")

* 瀑布流

  布局建议：在宽屏设备上，为提升信息展示效率，建议采用响应式布局策略。将小尺寸屏幕上的全屏内容，在宽屏设备上自动切换为瀑布流布局，通过重复布局，实现更多内容的可视化呈现，从而提升用户浏览效率与信息获取体验。

  实现原理：[WaterFlow](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/滚动与滑动/WaterFlow/ts-container-waterflow.md)组件提供columnsTemplate属性，支持设置当前瀑布流组件布局的列数。

  参考设计图如下：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/23/v3/l83QKiwkRZuOw1WihEpo4Q/zh-cn_image_0000002355146833.png?HW-CC-KV=V1&HW-CC-Date=20260612T020944Z&HW-CC-Expire=86400&HW-CC-Sign=953980733B6460953612E7B3477E886BBE2AB3436FCD8D1A6CD34E9FAA98C0F7 "点击放大")
* 轮播图

  布局建议：多张图片展示的场景下，建议使用轮播图展示图片，采用重复布局的方式，展示重复的元素。

  实现原理：[Swiper](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/滚动与滑动/Swiper/ts-container-swiper.md)组件提供子组件滑动轮播显示的能力，可以用来实现轮播图片。通过Swiper组件的displayCount属性，可以设置视窗内图片显示的个数。

  参考设计图如下：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d1/v3/SBxp9qHIQZGkm0-G2aGw9A/zh-cn_image_0000002321148166.png?HW-CC-KV=V1&HW-CC-Date=20260612T020944Z&HW-CC-Expire=86400&HW-CC-Sign=FA6F2BFCE2D7CD28C25EC3C7CC05998D3F282B078CFEA01CBD3F3E137BA2EBAD "点击放大")
* 网格

  布局建议：页面中重复内容（如卡片、商品项、文章列表等）的展示方式应根据可用空间进行动态调整。建议采用重复布局，根据不同设备的显示特性自动调整列数、间距与排列方向。

  实现原理：网格布局通过[Grid](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/滚动与滑动/Grid/ts-container-grid.md)组件实现。在不同断点下，设置不同的列数（columnsTemplate）和行数（rowsTemplate），即可呈现网格的多端效果。

  参考设计图如下：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/93/v3/Ht6oCn2aTGmKy5DMRznoBw/zh-cn_image_0000002355266677.png?HW-CC-KV=V1&HW-CC-Date=20260612T020944Z&HW-CC-Expire=86400&HW-CC-Sign=9A2549D20F7B7C121FF18D290C3AE7A43B466729312F4F64A24F9F3F2D12E506 "点击放大")
* 列表

  布局建议：当面临大量重复内容（如商品列表、文章卡片、用户评论等）需要有序展示时，建议采用重复布局，通过统一的样式模板对内容进行结构化排列。

  实现原理：[List](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/滚动与滑动/List/ts-container-list.md)组件提供lanes属性，支持设置布局列数或行数。

  参考设计图如下：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/05/v3/BYIz9KAFQcKnuCtDwhB5rA/zh-cn_image_0000002321307966.png?HW-CC-KV=V1&HW-CC-Date=20260612T020944Z&HW-CC-Expire=86400&HW-CC-Sign=AB5EF09ADD50C2AA9ABFA02D08951966F5475165A0282600B7FC70A2A31C36AB "点击放大")
* 侧边栏

  布局建议：为充分发挥大屏设备在空间展示上的优势，提升信息密度与用户操作效率，建议采用分栏布局，合理划分主内容区与侧边栏区域。

  实现原理：使用[SideBarContainer](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/栅格与分栏/SideBarContainer/ts-container-sidebarcontainer.md)组件展示侧边栏，在lg断点下设置[showSideBar](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/栅格与分栏/SideBarContainer/ts-container-sidebarcontainer.md#showsidebar)为true，显示侧边栏。

  参考设计图如下：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7f/v3/SUGJ4MdYSnqTKAmfWE4VBQ/zh-cn_image_0000002355146849.png?HW-CC-KV=V1&HW-CC-Date=20260612T020944Z&HW-CC-Expire=86400&HW-CC-Sign=0A04CD590A937BD89B80BC2A6EB09EC7A1B7B765E9B45E19ECC274204D0393F7 "点击放大")

* 三分栏

  布局建议：当应用页面包含层级关系，如一级目录、二级目录和内容区，为了利用大屏优势达到内容清晰直观展示的目的，建议使用分栏布局，实现三分栏的效果。

  实现原理：组合使用[SideBarContainer](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/栅格与分栏/SideBarContainer/ts-container-sidebarcontainer.md)与[Navigation](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/导航与切换/Navigation/ts-basic-components-navigation.md)组件，在lg断点下设置SideBarContainer组件的showSideBar为true，显示侧边栏；设置Navigation组件的mode为Auto。

  参考设计图如下：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0/v3/_CufQkJnRWCEEe2ZBVdTgA/zh-cn_image_0000002321148182.png?HW-CC-KV=V1&HW-CC-Date=20260612T020944Z&HW-CC-Expire=86400&HW-CC-Sign=CC7CE3C7079383BE90DA1C953A53AB01EE8CF75A652C2ACFF5136D256D685B30 "点击放大")
* 插图和文字组合布局

  布局建议：在需要图文并茂展示的场景下，推荐采用挪移布局，将图片与文字设置为左右分布的形式，使信息传递更加高效直观。

  实现原理：借助栅格组件[GridRow](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/栅格与分栏/GridRow/ts-container-gridrow.md)和[GridCol](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/栅格与分栏/GridCol/ts-container-gridcol.md)，可以设置在不同断点下栅格子元素所占据的列数。当一行中的列数超过了该断点下栅格组件的总列数时，栅格子元素会自动换行，从而实现灵活的布局效果。

  参考设计图如下：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/62/v3/X-aYoywaQgOcUJyM24Jizg/zh-cn_image_0000002355266693.png?HW-CC-KV=V1&HW-CC-Date=20260612T020944Z&HW-CC-Expire=86400&HW-CC-Sign=8C3D0DE9469D8C3A7DC153518A8CFE7B9BBA2F9AF2B66351D9B24076624E319C "点击放大")

## 大屏竖屏

大屏竖屏是指原本设计为横屏使用的大屏幕设备在垂直方向上的展示形态，即这些设备从默认的横向模式旋转90度后的状态。大屏竖屏为大屏设备的竖向态，典型设备有Pad（竖屏）、三折叠三屏态（竖屏）。

竖屏模式便于用户聚焦内容流并进行滚动、点击等基础操作。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/df/v3/_wb_25SgQkmeb2ZJ-nr4sQ/zh-cn_image_0000002546822098.png?HW-CC-KV=V1&HW-CC-Date=20260612T020944Z&HW-CC-Expire=86400&HW-CC-Sign=8CF558A134C2154A096DEB9BF58F1D71A9B21DB9F7F4171B6CBCDEF8977E02B3 "点击放大")

### 断点判断

| 横纵断点 | 设备 |
| --- | --- |
| 横向断点md，纵向断点lg | Pad（竖屏） |
| 三折叠三屏态（竖屏） |
| Pura X Max（展开态竖向） |

### 布局设计与实现

在大屏竖屏布局设计中，由于屏幕高度显著增加，用户在浏览内容时，对操作效率和视觉节奏的要求也相应提高。因此，在导航栏与重复布局设计上，需结合竖屏的展示特性进行有针对性的优化。在大屏竖屏设备中，导航栏通常位于顶部或底部，便于用户快速识别和操作。大屏竖屏提供了充足的高度空间，可以利用重复布局来展示结构相似但内容不同的信息模块。大屏竖屏的布局设计可参考[大屏应用 UX 体验标准](https://developer.huawei.com/consumer/cn/doc/design-guides/ux-guidelines-large-screen-0000001807707561)。

* 导航栏

  布局建议：大屏竖屏设备推荐将页签栏布局在底部，提升核心功能的可访问性与操作效率。

  实现原理：结合响应式布局能力，设置[Tabs组件](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/导航与切换/Tabs/ts-container-tabs.md)的barPosition为End、vertical为false属性实现目标效果。

  参考设计图如下：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1b/v3/9dnN2xLHQOCGlaFjWBK1_A/zh-cn_image_0000002355146861.png?HW-CC-KV=V1&HW-CC-Date=20260612T020944Z&HW-CC-Expire=86400&HW-CC-Sign=5202BA70FD1ADEF735FF1B5114E9292CAAA0E28AF9E91B9CF125BF0A1B190EF0 "点击放大")
* 轮播图

  布局建议：在大屏竖屏场景下，由于屏幕宽度较大，推荐采用重复布局，多张图片轮播，提升内容密度与用户的浏览效率。

  实现原理：[Swiper](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/滚动与滑动/Swiper/ts-container-swiper.md)组件支持图片的滑动轮播展示能力，可通过设置displayCount属性，实现多个轮播项的同时展示。

  参考设计图如下：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3e/v3/c0g67B1MR0WK_Bx2x86SHw/zh-cn_image_0000002321148194.png?HW-CC-KV=V1&HW-CC-Date=20260612T020944Z&HW-CC-Expire=86400&HW-CC-Sign=6D4E5CF51CE8AC48013EAD0AB7500D7409AD600E465A410DB6592CD8F46727FD "点击放大")
* 列表

  布局建议：大屏竖屏相较于直板机竖屏具有更大的展示内容区，建议采用重复布局，设置为一行多列或一列多行展示。

  实现原理：[List](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/滚动与滑动/List/ts-container-list.md)组件提供lanes属性，支持设置布局列数或行数。

  参考设计图如下：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d5/v3/qkVq4WmLSlywRLm1dWXw0g/zh-cn_image_0000002355266713.png?HW-CC-KV=V1&HW-CC-Date=20260612T020944Z&HW-CC-Expire=86400&HW-CC-Sign=B023446217EE4DA6F04314C40554EEB6D53236F5BFAFDCC0D9455F42C7D6F2C9 "点击放大")
* 网格

  布局建议：大屏竖屏相较于直板机竖屏具有更大的展示内容区，支持设置布局为多行多列展示。

  实现原理：通过[Grid](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/滚动与滑动/Grid/ts-container-grid.md)组件实现。在不同断点下，设置不同的列数（columnsTemplate）和行数（rowsTemplate），即可呈现网格的多端效果。

  参考设计图如下：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9e/v3/NNG8uKPnTA-3p-Sg5BQU3w/zh-cn_image_0000002321307994.png?HW-CC-KV=V1&HW-CC-Date=20260612T020944Z&HW-CC-Expire=86400&HW-CC-Sign=C510DF9D5EE80AB6D3BC77C9D77669260B3CD3ED799581C3BE4E458369C98160 "点击放大")

## 大方形屏

大方形屏幕的特点包括：屏幕比例为 1:1，呈现出对称且均衡的视觉效果，横向分辨率超过 600vp，具备较高的信息承载能力和良好的阅读舒适度。典型设备如华为 Mate X 系列在展开状态下的屏幕形态，可为用户提供更宽广的操作空间和更丰富的界面布局可能性。

此类屏幕非常适合多任务处理、内容分屏展示以及创作类应用，能够显著提升用户的操作效率与交互体验。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/da/v3/wAtMJghsTFifrXw09mx5wg/zh-cn_image_0000002355146881.png?HW-CC-KV=V1&HW-CC-Date=20260612T020944Z&HW-CC-Expire=86400&HW-CC-Sign=DDD4023D5D980CCADB45B160CC547D31140B9E6099B7C751057542C20432A131 "点击放大")

### 断点判断

| 横纵断点 | 设备 |
| --- | --- |
| 横向断点md，纵向断点md | [双折叠](../../../../多端设备体验提升/手机/双折叠应用开发/bpta-foldable-guide.md)：Mate X系列（展开态） |
| [三折叠](../../../../多端设备体验提升/手机/三折叠应用开发/bpta-matext-guide.md)：Mate XT系列（双屏M态） |

### 布局设计与实现

大方形屏幕提供了广阔的显示区域，使得导航栏能够包含更多功能入口而不会显得拥挤。大方形屏幕也适合采用重复布局，展示结构相似但内容不同的信息单元。对于小屏幕上下排列的内容，大方形屏幕多采用左右布局，以使页面更加美观。鉴于大方形屏幕宽广的横向和纵向空间，分栏布局是一种非常有效的信息组织方法。

* 导航栏

  布局建议：对于md断点的大方形屏幕，推荐页签栏位于底部，图标与文字水平排列，页签宽度平均分配，页签高度固定为56vp。

  实现原理：结合响应式布局能力，设置[Tabs组件](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/导航与切换/Tabs/ts-container-tabs.md)的barPosition为End、vertical为false，实现目标效果。

  参考设计图如下：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/da/v3/cQNwJg9XT5mHb6x5gct0Eg/zh-cn_image_0000002321148206.png?HW-CC-KV=V1&HW-CC-Date=20260612T020944Z&HW-CC-Expire=86400&HW-CC-Sign=927E306235578CF4AEEE4C49031247E121F8B25F2797D8083042485FC1743D56 "点击放大")
* 瀑布流

  布局建议：小尺寸屏幕上的单列瀑布流，在大方形屏上采用重复布局，变为多列瀑布流布局，可以提升宽屏设备上的阅读体验。

  实现原理：[WaterFlow](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/滚动与滑动/WaterFlow/ts-container-waterflow.md)组件提供columnsTemplate属性，支持设置当前瀑布流组件布局的列的数量。

  参考设计图如下：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8c/v3/JV4ey29-SPyzDirAnj44cw/zh-cn_image_0000002355266729.png?HW-CC-KV=V1&HW-CC-Date=20260612T020944Z&HW-CC-Expire=86400&HW-CC-Sign=7EC155B132AE42CE0F6A67EBDB8C00EA48AF7FA758B1427812C14C5C4D3D3A27 "点击放大")
* 网格

  布局建议：大方形屏推荐使用重复布局，以多行多列的形式展示重复性信息元素，充分发挥大屏空间优势，提升信息密度与展示效率。

  实现原理：使用[Grid](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/滚动与滑动/Grid/ts-container-grid.md)组件实现多行多列布局效果，定义行列结构和单元格分布，灵活展示信息内容。

  参考设计图如下：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a8/v3/JfPegj22RWSVU9YH0nWHMw/zh-cn_image_0000002321308006.png?HW-CC-KV=V1&HW-CC-Date=20260612T020944Z&HW-CC-Expire=86400&HW-CC-Sign=526DB16A3250C4EB5444D9915ED447BDA06DC49E88A8CF8B75E33C290423090A "点击放大")
* 列表

  布局建议：在大方形屏上，建议使用重复布局，通过“一行多列”或“一列多行”的排布方式展示更多内容，提升信息密度和界面利用率。

  实现原理：[List](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/滚动与滑动/List/ts-container-list.md)组件提供lanes属性，支持设置布局列数或行数。

  参考设计图如下：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d2/v3/ZqBKcJ68RxCMLVDDxRtAIQ/zh-cn_image_0000002355146889.png?HW-CC-KV=V1&HW-CC-Date=20260612T020944Z&HW-CC-Expire=86400&HW-CC-Sign=57D8F5E22842C4AFCFBE155F94E6FCF7ED7C48F5085FB0F74EF2443D996D53B8 "点击放大")
* 双栏

  布局建议：大方形屏建议采用分栏布局，利用横向空间优势，清晰展示具有层级关系的内容，提升界面组织性和用户操作效率。

  实现原理：将[Navigation](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/导航与切换/Navigation/ts-basic-components-navigation.md)的mode属性设置为Auto，可以自动实现单/双栏的切换。

  参考设计图如下：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2d/v3/FK5Hd93_St-58TmPkFquzg/zh-cn_image_0000002321148226.png?HW-CC-KV=V1&HW-CC-Date=20260612T020944Z&HW-CC-Expire=86400&HW-CC-Sign=CB376BEC247D4759168A9229D619D4B10BADFF063B2068211E3D11665FF4AADC "点击放大")
* 侧边栏

  布局建议：由于大方形屏横向空间充裕，在需要展示更多信息时，建议采用分栏布局，添加侧边栏，以提升界面组织性与信息展示效率。

  实现原理：在需要展示侧边栏的事件触发时，使用[SideBarContainer](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/栅格与分栏/SideBarContainer/ts-container-sidebarcontainer.md)组件，动态设置[showSideBar](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/栅格与分栏/SideBarContainer/ts-container-sidebarcontainer.md#showsidebar)为true，显示侧边栏。

  参考设计图如下：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c1/v3/YkuhSDwyQtK7lGoE96UPPA/zh-cn_image_0000002355266749.png?HW-CC-KV=V1&HW-CC-Date=20260612T020944Z&HW-CC-Expire=86400&HW-CC-Sign=32F8B193517B78DF8386746306BB4180ED44AEAF3A4579D39E6FEE450A51FA1B "点击放大")
* 插图和文字组合布局

  布局建议：在部分小屏上下显示的场景，大方形屏时推荐采用挪移布局，左右分布。

  实现原理：通过响应式布局能力结合[Grid组件](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/滚动与滑动/Grid/ts-container-grid.md)实现，栅格子元素占据的列数会随着开发者的配置发生改变。当一行中的列数超过栅格组件在该断点的总列数时，可以自动换行。

  参考设计图如下：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e5/v3/ZEDKdETUS2OapwKODI4u8g/zh-cn_image_0000002321308038.png?HW-CC-KV=V1&HW-CC-Date=20260612T020944Z&HW-CC-Expire=86400&HW-CC-Sign=FFC166495FAE46EA8EE8B35CA8503ECDF37F4B7BF262EEF6A317C8B41D7A6EF5 "点击放大")

## 直板机竖屏

直板机竖屏是手机的主流屏幕类型，展示区域适中，适合单手操作和日常信息浏览。典型设备有华为全系列的直板机（如Mate 60）、小折叠（展开态）、阔折叠（如Pura X系列展开态和Pura X Max系列折叠态）、双折叠（折叠态）。

这种屏幕形态特别适合社交应用、新闻阅读、即时通讯、短视频播放等高频交互场景。由于高度适应移动设备的使用习惯，开发者在设计界面时能够更容易地实现内容的垂直排列和层次展示。此外，直板机竖屏在响应式布局中表现出良好的兼容性，能够灵活适应不同分辨率和设备尺寸，在多设备协同开发中发挥着承上启下的重要作用。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/08/v3/4v0vfwo4SjuATjCHp9Sf1A/zh-cn_image_0000002552782174.png?HW-CC-KV=V1&HW-CC-Date=20260612T020944Z&HW-CC-Expire=86400&HW-CC-Sign=406FA15F6A4207D8A0583C5F608EED8D3D2B55B0275D075190DFF9CCBB47367F)

### 断点判断

| 横纵断点 | 设备 |
| --- | --- |
| 横向断点sm，纵向断点lg | 直板机 |
| 小折叠（展开态） |
| Pura X（展开态） |
| 双折叠（折叠态） |
| 三折叠（折叠态） |
| Pura X Max（折叠态） |

### 布局设计与实现

直板机竖屏由于屏幕宽度有限而高度相对充裕，设计布局时应以简洁直观、操作高效为核心目标。在竖屏界面中，导航栏通常置于屏幕顶部或底部，作为用户进行功能切换和页面跳转的主要入口。竖屏设计时，建议合理运用挪移布局，以减轻空间受限导致的视觉拥挤。鉴于直板机竖屏横向宽度较短，推荐采用单栏布局。

* 导航栏

  布局建议：在直板机竖屏设备上，建议使用底部页签栏布局，方便用户快速切换功能模块，提升操作便捷性与界面友好度。

  实现原理：结合响应式布局能力，设置[Tabs组件](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/导航与切换/Tabs/ts-container-tabs.md)的barPosition为End、vertical为false属性实现目标效果。

  参考设计图如下：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/20/v3/2BW5BisTTD-yzYZVuz9wqA/zh-cn_image_0000002321148234.jpg?HW-CC-KV=V1&HW-CC-Date=20260612T020944Z&HW-CC-Expire=86400&HW-CC-Sign=87B411815C0557450F4CEF08DE77C11C3135F9AA183EB6E6DA531A9734331CA7 "点击放大")
* 瀑布流

  布局建议：直板机竖屏设备推荐使用重复布局，提升内容展示密度与滚动浏览体验，适用于图集、商品列表、动态卡片等内容密集型场景。

  实现原理：[WaterFlow](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/滚动与滑动/WaterFlow/ts-container-waterflow.md)组件提供columnsTemplate属性，支持设置当前瀑布流组件布局的列的数量。

  参考设计图如下：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d5/v3/dN6Py77CTqSk8Ai1O4gfdA/zh-cn_image_0000002355266757.jpg?HW-CC-KV=V1&HW-CC-Date=20260612T020944Z&HW-CC-Expire=86400&HW-CC-Sign=23970EC64D97997C19975CF2933427B8282B022997CCC9640D97604C360C1A35 "点击放大")
* 插图和文字组合布局

  布局建议：插图和文字组合场景在直板机竖屏设备上推荐使用上下布局，按内容优先级从上至下排列，适配小屏显示需求，提升可读性与操作便利性。

  实现原理：主要是借助栅格组件[GridRow](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/栅格与分栏/GridRow/ts-container-gridrow.md)和[GridCol](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/栅格与分栏/GridCol/ts-container-gridcol.md)，配置在不同断点下栅格子元素占据的列数实现。

  参考设计图如下：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/87/v3/yFO2Ui8IRhCk4f7xo0WMmw/zh-cn_image_0000002321308050.png?HW-CC-KV=V1&HW-CC-Date=20260612T020944Z&HW-CC-Expire=86400&HW-CC-Sign=53BE54C789124B2ED6ED631EE94A1713E7F18D1796549E5CC68722A2BA163C0B "点击放大")
* 单栏

  布局建议：直板机竖屏设备推荐使用单栏布局，按内容顺序垂直排列，提升界面简洁性与用户操作效率。

  实现原理：通过设置[Navigation](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/导航与切换/Navigation/ts-basic-components-navigation.md)组件的mode属性为Stack实现。

  参考设计图如下：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d1/v3/df7TlvIDTuSPwJu1S69efw/zh-cn_image_0000002355146929.png?HW-CC-KV=V1&HW-CC-Date=20260612T020944Z&HW-CC-Expire=86400&HW-CC-Sign=9F043C641BBD7A33B2837923364513EFD163CAFA0207B73F977AE87C382A3B16 "点击放大")

## 直板机横屏

直板机横屏的主要使用场景通常是竖屏设备旋转至横屏后的情况。当需要更宽广的横向显示区域来增强视觉体验或提升特定任务的操作效率时，这种屏幕展示方式特别适合观看视频、浏览网页、编辑文档及游戏等需要较大横向空间的应用。典型设备有华为全系列的直板机（如Mate 60）、小折叠（展开态）、阔折叠（如Pura X系列展开态和Pura X Max系列折叠态）、双折叠（折叠态）。

在这些设备上，当用户从竖屏切换到横屏模式时，界面布局会自动调整以适应新的屏幕方向，提供更加沉浸的观看体验或更适合阅读和编辑的工作环境。例如，观看电影或电视剧时，横屏模式可以最大化屏幕宽度的使用，减少黑边，增加画面比例；而在编辑文档或电子表格时，横向布局允许同时查看更多的列数据或文本内容，从而提高工作效率。通过这种方式，直板机横屏不仅增加了设备的实用性，也为用户提供了更加灵活多样的使用体验。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/db/v3/zCqXaf7fS9ud3Kp23fml1g/zh-cn_image_0000002583421893.png?HW-CC-KV=V1&HW-CC-Date=20260612T020944Z&HW-CC-Expire=86400&HW-CC-Sign=7441224697414FA4EC0DB5288F53176352552991623F77493C8674B97537AC5B)

### 断点判断

| 横纵断点 | 设备 |
| --- | --- |
| 横向断点md，纵向断点sm | 直板机（横屏） |
| 小折叠（展开态横屏） |
| Pura X（展开态横屏） |
| 双折叠（折叠态横屏） |
| 三折叠（折叠态横屏） |
| Pura X Max（折叠态横屏） |

### 布局设计与实现

直板机横屏由于屏幕宽度的增加，使用户拥有更广阔的视野和更大的操作空间，因此界面布局可以充分利用横向空间，采用重复布局，提升信息密度和交互效率。对于横向内容的展示，可以采用左右结构来呈现信息。考虑到直板机横屏的横向长度较长，建议使用分栏布局，提升用户操作效率。

* 网格

  布局建议：直板机横屏设备推荐使用重复布局，利用较宽的显示区域横向展示更多内容，提升信息密度与用户浏览效率。

  实现原理：使用[Grid](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/滚动与滑动/Grid/ts-container-grid.md)组件实现多行多列布局效果，定义行列结构和单元格分布，灵活展示信息内容，特别适合卡片式内容、商品列表等场景。

  参考设计图如下：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8e/v3/Us4Uv6D8RmeTVTxcLAitiQ/zh-cn_image_0000002355266777.png?HW-CC-KV=V1&HW-CC-Date=20260612T020944Z&HW-CC-Expire=86400&HW-CC-Sign=2ADEFAD53AF9BC64992A68EA0D608159445ACB18191FE84D98BF62877E82F299 "点击放大")
* 插图与文字组合布局

  布局建议：直板机横屏推荐采用挪移布局，将图片与文字左右排列，合理利用横向空间，提升信息展示效率与界面美观性。

  实现原理：使用[GridRow](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/栅格与分栏/GridRow/ts-container-gridrow.md)/[GridCol](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/栅格与分栏/GridCol/ts-container-gridcol.md)实现，栅格子元素占据的列数会随着开发者的配置发生改变。当一行中的列数超过栅格组件在该断点的总列数时，可以自动换行。

  参考设计图如下：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/88/v3/WzNpiOqVS5aiRR1lM9ZuuA/zh-cn_image_0000002321308074.png?HW-CC-KV=V1&HW-CC-Date=20260612T020944Z&HW-CC-Expire=86400&HW-CC-Sign=0BC64C4290404719BA1A4C0A4D3EF5D433F723054D66FCC3BD2E5C081F7B88F8 "点击放大")
* 双栏

  布局建议：直板机横屏设备推荐使用分栏布局，将界面划分为左右两部分，充分利用横向空间展示更多信息，提升用户操作效率。

  实现原理：使用[Navigation](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/导航与切换/Navigation/ts-basic-components-navigation.md)组件，设置mode为Auto；或者使用[SideBarContainer](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/栅格与分栏/SideBarContainer/ts-container-sidebarcontainer.md)组件，设置showSideBar为true，显示侧边栏。两种方式均能实现目标效果。

  参考设计图如下：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cc/v3/UgC2eoyOTJ6miAjyxol3ng/zh-cn_image_0000002355146953.png?HW-CC-KV=V1&HW-CC-Date=20260612T020944Z&HW-CC-Expire=86400&HW-CC-Sign=60B8C2D6A1F2909C62B1343B2B6610B101B1A2BB8A8CBFB614107A86F36D20F3 "点击放大")

说明

直板机横屏的页面设计实现可参考[多设备长视频界面](../../多设备界面开发案例/多设备长视频界面/multi-video-app.md)。

## 小方形屏

小方形屏的特点包括：屏幕比例为1:1，横向分辨率低于600vp，典型设备如华为推出的Pura X系列产品的外屏。

此类屏幕主要应用于即时信息处理、便捷出行导航、快速移动支付、沉浸影音播放、轻量游戏畅玩等场景，能够充分发挥小方屏高效便捷的优势，无需使用内屏操作。

由于1:1的屏幕比例和小尺寸屏幕，带来了一定的基础功能适配工作。在实际适配时，主要考虑如何充分利用屏幕空间，提供最佳的用户体验。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d3/v3/cKDe0xyLSBCCOBNRGPn2eA/zh-cn_image_0000002552883100.png?HW-CC-KV=V1&HW-CC-Date=20260612T020944Z&HW-CC-Expire=86400&HW-CC-Sign=4BEF21C1FBD0E427942CE6F186B3BDEDFF8E0F235C2727BE4C47035E75B6FAAC "点击放大")

### 断点判断

| 横纵断点 | 设备 |
| --- | --- |
| 横向断点sm，纵向断点md | Pura X（折叠态） |

### 布局设计与实现

本章节以Pura X系列产品外屏为例，提供小方形屏上的设计方案，确保布局完整显示，避免内容截断、挤压或堆叠，充分利用屏幕空间，以提供最佳用户体验。

* 页面支持滑动、完整显示

  布局建议：小方形屏展示内容建议要考虑完整性展示，推荐使用[Scroll](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/滚动与滑动/Scroll/ts-container-scroll.md)组件实现页面支持滑动。

  效果图如下：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/47/v3/G6is_ayJSqOVGMjN038I9Q/zh-cn_image_0000002355266801.gif?HW-CC-KV=V1&HW-CC-Date=20260612T020944Z&HW-CC-Expire=86400&HW-CC-Sign=8D2C079CF4CACE3E12205EF991E431C1B941A330F2F188B2FF61BF12BB98A179 "点击放大")
* **短视频播放页面完整显示，侧边控件支持滑动显示，侧边控件支持滑动**

  布局建议：小方形屏展示短视频播放页面，背景图片（视频）需等比例缩放并上下沉浸，上方沉浸至顶部标题栏，下方沉浸至底部页签栏。侧边控件支持滑动，确保页面内容完整显示。

  效果图如下：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ad/v3/MDVsQX5LQtWD5unCNNzX_w/zh-cn_image_0000002445121925.gif?HW-CC-KV=V1&HW-CC-Date=20260612T020944Z&HW-CC-Expire=86400&HW-CC-Sign=AE2B0D5A74F07046C4D79BEE19ECD83E41E847E4DD494D8CF5EFFE4A8B1DDC62 "点击放大")

  实现原理：使用Stack组件控制页面内容显示层级，背景图片上下沉浸，且互相不影响交互事件。[Z序控制](<../../../../../harmonyos-guides/应用框架/ArkUI（方舟UI框架）/UI开发 (ArkTS声明式开发范式)/组件布局/构建布局/层叠布局 (Stack)/arkts-layout-development-stack-layout.md#z序控制>)从下到上分别是背景图片（视频）区、底部页签区、短视频描述区、侧边控件区、顶部页签区。顶部和底部页签设置内边距padding为topAvoidHeight或bottomAvoidHeight，避让系统规避区。侧边控件区使用Scroll组件自动控制滑动，使用[Blank组件](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/空白与分隔/Blank/ts-basic-components-blank.md)和[displayPriority属性](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/通用属性/布局与边框/布局约束/ts-universal-attributes-layout-constraints.md#displaypriority)控制侧边控件区上下两侧的留白，容器高度足够时上下留白，容器高度不足时自动隐藏。

  ```
  1. Stack({ alignContent: Alignment.BottomEnd }) {
  2. // Background image.
  3. Row() {
  4. Image($r('app.media.background_image'))
  5. .height('100%')
  6. .objectFit(ImageFit.Cover)
  7. .aspectRatio(0.6)
  8. }
  9. .height('100%')
  10. .width('100%')
  11. .justifyContent(FlexAlign.Center)

  13. // Bottom tabs.
  14. List() {
  15. // ...
  16. }
  17. .backgroundColor($r('sys.color.mask_secondary'))
  18. .listDirection(Axis.Horizontal)
  19. .height(this.bottomBarHeight)
  20. .padding({ bottom: this.bottomAvoidHeight })
  21. // ...

  23. // Video description.
  24. Column() {
  25. // ...
  26. }
  27. .alignItems(HorizontalAlign.Start)
  28. .padding({
  29. left: $r('app.float.margin_md'),
  30. right: $r('app.float.margin_md')
  31. })
  32. // ...

  34. // Sidebar buttons.
  35. Scroll() {
  36. Column() {
  37. Blank()
  38. .layoutWeight(3)
  39. .displayPriority(1)
  40. // ...
  41. Blank()
  42. .layoutWeight(1)
  43. .displayPriority(1)
  44. }
  45. // ...
  46. }
  47. .scrollBar(BarState.Off)
  48. .layoutWeight(1)
  49. .width('56vp')
  50. .edgeEffect(EdgeEffect.None)
  51. .align(Alignment.Bottom)
  52. .margin({
  53. top: this.topAvoidHeight + 24,
  54. bottom: this.bottomBarHeight,
  55. right: '8vp'
  56. })

  58. // Top tabs.
  59. Row() {
  60. // ...
  61. }
  62. .height('100%')
  63. .width('100%')
  64. .backgroundColor(Color.Black)
  ```

  [ShortVideoView.ets](https://gitcode.com/HarmonyOS_Samples/SmallWindowScene/blob/master/entry/src/main/ets/views/ShortVideoView.ets#L41-L239)
* **自定义弹窗适配小方形屏**

  布局建议：在小方形屏上，当窗口高度无法完整显示自定义弹窗时，可能出现弹窗内容截断，需要进行自定义弹窗适配小方形屏。

  效果图如下：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8f/v3/w_CzgrypQ-yIYDdQtbRxQg/zh-cn_image_0000002321308094.gif?HW-CC-KV=V1&HW-CC-Date=20260612T020944Z&HW-CC-Expire=86400&HW-CC-Sign=80FD812F0E2BBE82DFE94E1A1A4D5C8B8596A5311F14CCA4EA774B1C9E6B63EF "点击放大")

  实现原理：弹框内容区使用scroll组件包裹，且使用[constraintSize](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/通用属性/布局与边框/尺寸设置/ts-universal-attributes-size.md#constraintsize)约束其高度最大不超过父组件的90%，避免弹框内容截断。

  ```
  1. Scroll() {
  2. Column() {
  3. // ...
  4. }
  5. }
  6. .scrollBar(BarState.Off)
  7. .constraintSize({
  8. minHeight: 0,
  9. maxHeight: '90%'
  10. })
  ```

  [ShareDialog.ets](https://gitcode.com/harmonyos_samples/SmallWindowScene/blob/master/entry/src/main/ets/views/ShareDialog.ets#L24-L43)
* 沉浸式浏览

  布局建议：在小方形屏通用场景中，考虑到屏幕空间有限，为了提供更佳的内容体验，建议使用上滑隐藏、下滑恢复显示的功能。上滑可以临时隐藏标题栏、页签栏等界面元素，实现全屏内容浏览。下滑时，标题栏和页签栏将通过动画逐渐恢复显示。

  效果图如下：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/04/v3/nKb9C4rFRHa_v1mAHFDl_A/zh-cn_image_0000002445161793.gif?HW-CC-KV=V1&HW-CC-Date=20260612T020944Z&HW-CC-Expire=86400&HW-CC-Sign=23F4019DEEBA33CD58A140E527F13FD982E8D22697BC409FF4A75C4A37EC738D "点击放大")

  实现原理：监听滚动行为，滚动时动态调整页面组件的高度和透明度，达到视觉上逐渐显示和隐藏的效果。具体为以下步骤：

  1. 使用状态变量控制顶部标题栏和底部页签栏的高度及透明度。标题栏高度为topBarHeight，页签栏高度为bottomBarHeight，标题栏和页签栏的透明度为barOpacity。

     ```
     1. @StorageLink('topBarHeight') topBarHeight: number = CommonConstants.UTIL_HEIGHTS[1] + this.topAvoidHeight;
     2. @State bottomBarHeight: number = CommonConstants.UTIL_HEIGHTS[0] + this.bottomAvoidHeight;
     3. @State barOpacity: number = 1;
     ```

     [Index.ets](https://gitcode.com/HarmonyOS_Samples/SmallWindowScene/blob/master/entry/src/main/ets/pages/Index.ets#L36-L38)
  2. 在沉浸式布局下，标题栏高度为78vp加顶部系统规避区高度topAvoidHeight；页签栏高度为56vp加底部系统规避区高度bottomAvoidHeight，页签栏底部内边距为bottomAvoidHeight，以避让底部系统导航条。

     ```
     1. @StorageLink('topAvoidHeight') @Watch('topBarHeightChange') topAvoidHeight: number = 0;
     2. @StorageLink('bottomAvoidHeight') @Watch('bottomBarHeightChange') bottomAvoidHeight: number = 0;
     3. // ...
     4. topBarHeightChange(): void {
     5. if (this.currentWidthBreakpoint === WidthBreakpoint.WIDTH_SM &&
     6. (this.currentHeightBreakpoint === HeightBreakpoint.HEIGHT_MD ||
     7. this.currentHeightBreakpoint === HeightBreakpoint.HEIGHT_SM)) {
     8. this.topBarHeight = 78 + this.topAvoidHeight;
     9. }
     10. // ...
     11. };

     13. bottomBarHeightChange(): void {
     14. this.bottomBarHeight = 56 + this.bottomAvoidHeight;
     15. };
     ```

     [Index.ets](https://gitcode.com/HarmonyOS_Samples/SmallWindowScene/blob/master/entry/src/main/ets/pages/Index.ets#L30-L89)
  3. 顶部和底部系统避让区高度会随应用窗口变化而变化。窗口生命周期创建时，调用[window.getWindowAvoidArea](<../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS API/窗口管理/@ohos.window (窗口)/Interface (Window)/arkts-apis-window-window.md#getwindowavoidarea9>)()获取初始的系统避让区高度，并使用window.on('avoidAreaChange')监听系统避让区的变化。常见触发系统避让区回调的场景可参考[on('avoidAreaChange')](<../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS API/窗口管理/@ohos.window (窗口)/Interface (Window)/arkts-apis-window-window.md#onavoidareachange9>)。

     ```
     1. export default class EntryAbility extends UIAbility {
     2. private uiContext ?: UIContext;
     3. private windowUtil?: WindowUtil = WindowUtil.getInstance();
     4. private windowObj?: window.Window;
     5. private onAvoidAreaChange: (avoidArea: window.AvoidAreaOptions) => void = (avoidArea: window.AvoidAreaOptions) => {
     6. if (avoidArea.type === window.AvoidAreaType.TYPE_SYSTEM) {
     7. AppStorage.setOrCreate('topAvoidHeight', this.windowObj!.getUIContext().px2vp(avoidArea.area.topRect.height));
     8. } else if (avoidArea.type === window.AvoidAreaType.TYPE_NAVIGATION_INDICATOR) {
     9. AppStorage.setOrCreate('bottomAvoidHeight', this.windowObj!.getUIContext().px2vp(avoidArea.area.bottomRect.height));
     10. }
     11. };
     12. // ...
     13. onWindowStageCreate(windowStage: window.WindowStage): void {
     14. // Main window is created, set main page for this ability
     15. hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onWindowStageCreate');
     16. this.windowUtil?.setWindowStage(windowStage);

     18. windowStage.loadContent('pages/Index', (err) => {
     19. if (err.code) {
     20. hilog.error(0x0000, 'testTag', 'Failed to load the content. Cause: %{public}s', JSON.stringify(err) ?? '');
     21. return;
     22. }
     23. windowStage.getMainWindow((err: BusinessError, data: window.Window) => {
     24. if (err.code) {
     25. hilog.error(0x0000, 'testTag', 'Failed to get the main window. Cause: %{public}s', JSON.stringify(err) ?? '');
     26. return;
     27. }
     28. this.windowObj = data;
     29. this.uiContext = data.getUIContext();
     30. this.windowUtil!.setFullScreen();
     31. // ...
     32. let topAvoidHeight: window.AvoidArea = data.getWindowAvoidArea(window.AvoidAreaType.TYPE_SYSTEM);
     33. AppStorage.setOrCreate('topAvoidHeight', this.uiContext.px2vp(topAvoidHeight.topRect.height));
     34. let bottomAvoidHeight: window.AvoidArea =
     35. data.getWindowAvoidArea(window.AvoidAreaType.TYPE_NAVIGATION_INDICATOR);
     36. AppStorage.setOrCreate('bottomAvoidHeight', this.uiContext.px2vp(bottomAvoidHeight.bottomRect.height));
     37. data.on('avoidAreaChange', this.onAvoidAreaChange);
     38. if (AppStorage.get('currentWidthBreakpoint') === WidthBreakpoint.WIDTH_SM &&
     39. (AppStorage.get('currentHeightBreakpoint') === HeightBreakpoint.HEIGHT_MD ||
     40. AppStorage.get('currentHeightBreakpoint') === HeightBreakpoint.HEIGHT_SM)) {
     41. // Set top bar height when the application is in small screen.
     42. AppStorage.setOrCreate('topBarHeight',
     43. CommonConstants.UTIL_HEIGHTS[1] + this.uiContext!.px2vp(topAvoidHeight.topRect.height));
     44. } else {
     45. // Set top bar height when the application is in full screen.
     46. AppStorage.setOrCreate('topBarHeight',
     47. CommonConstants.UTIL_HEIGHTS[2] + this.uiContext!.px2vp(topAvoidHeight.topRect.height));
     48. }
     49. })
     50. // ...
     51. }
     52. // ...
     53. }
     ```

     [EntryAbility.ets](https://gitcode.com/HarmonyOS_Samples/SmallWindowScene/blob/master/entry/src/main/ets/entryability/EntryAbility.ets#L24-L123)
  4. 设置顶部标题栏的高度为topBarHeight，透明度为barOpacity；底部页签栏的高度为bottomBarHeight，透明度为barOpacity，确保滑动时标题栏和页签栏能够逐渐显隐。在Stack组件内，将列表内容的顶部外边距设置为topBarHeight，确保滑动时列表占满剩余高度。

     ```
     1. Tabs() {
     2. TabContent() {
     3. Stack({ alignContent: Alignment.Top }) {
     4. Row() {
     5. Text($r('app.string.app_title'))
     6. .fontSize($r('app.float.font_size_xl'))
     7. .fontWeight(CommonConstants.FONT_WEIGHTS[1])
     8. .height(this.topBarHeight)
     9. .align(Alignment.Bottom)
     10. .padding({ bottom: 12 })
     11. }
     12. .height(this.topBarHeight)
     13. .opacity(this.barOpacity)
     14. // ...
     15. List({
     16. space: CommonConstants.LIST_SPACE[0],
     17. scroller: this.listScroller,
     18. }) {
     19. // ...
     20. }
     21. .onScrollIndex((start: number) => {
     22. this.currentIndex = start;
     23. })
     24. .margin({ top: this.topBarHeight })
     25. // ...
     26. }
     27. .height('100%')
     28. .width('100%')
     29. }
     30. .tabBar(this.bottomTabBuilder(0))

     32. // ...
     33. }
     34. // ...
     35. .barHeight(this.bottomBarHeight)
     36. // ...
     ```

     [Index.ets](https://gitcode.com/HarmonyOS_Samples/SmallWindowScene/blob/master/entry/src/main/ets/pages/Index.ets#L129-L275)
  5. 当横向断点为sm，纵向断点为sm或md，应用窗口属于小方形屏（例如Pura X外屏和手机上下分屏）时，在滑动过程中，如果当前Y轴滑动的偏移量>0（上滑时）且固定区（顶部标题栏和底部页签栏）未完全隐藏，逐渐减少固定区的高度和透明度，实现滑动过程隐藏的效果；当 Y 轴滑动偏移量＜ 0（下滑时），且未处于恢复动画状态、固定区域已隐藏的情况下，通过动画逐步恢复固定区域的高度与透明度。

     ```
     1. .onScrollFrameBegin((offset: number) => {
     2. if (this.currentWidthBreakpoint !== WidthBreakpoint.WIDTH_SM ||
     3. (this.currentHeightBreakpoint !== HeightBreakpoint.HEIGHT_MD &&
     4. this.currentHeightBreakpoint !== HeightBreakpoint.HEIGHT_SM)) {
     5. return { offsetRemain: offset };
     6. }
     7. if (offset > 0) {
     8. this.currentYOffset += offset;
     9. }
     10. if (offset < 0) {
     11. this.currentYOffset -= offset;
     12. }
     13. this.getUIContext().animateTo({
     14. duration: 300
     15. }, () => {
     16. this.topBarHeight = 0;
     17. this.bottomBarHeight = 0;
     18. this.barOpacity = 0;
     19. });
     20. return { offsetRemain: offset };
     21. })
     22. .onScrollStop(() => {
     23. setTimeout(() => {
     24. this.getUIContext().animateTo({
     25. duration: 300
     26. }, () => {
     27. this.bottomBarHeight = 56 + this.bottomAvoidHeight;
     28. this.topBarHeight = 78 + this.topAvoidHeight;
     29. this.barOpacity = 1;
     30. this.currentYOffset = 0;
     31. this.isHiding = false;
     32. });
     33. }, 500);
     34. });
     ```

     [Index.ets](https://gitcode.com/HarmonyOS_Samples/SmallWindowScene/blob/master/entry/src/main/ets/pages/Index.ets#L207-L240)

## 圆形屏

典型配备圆形屏幕的设备包括手表等可穿戴装置，其主要特点为即时通知和轻量级交互。

即时通知：几乎不受时间和空间限制，便于及时提醒用户相关消息。同时，需注意在特定场景中减少重复或无关通知对用户的干扰，依据用户实际使用情况调整通知策略。

轻量级交互：在同一应用程序中，智能穿戴设备应利用其便携性，作为大型屏幕设备的补充和扩展，而不是替代。具体设计时，应考虑智能手表的屏幕尺寸和使用环境，进行简洁界面的定制，确保使用过程顺畅和操作便捷。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/58/v3/aT_nmO7PTEKmWL_9mnK7kw/zh-cn_image_0000002321148278.png?HW-CC-KV=V1&HW-CC-Date=20260612T020944Z&HW-CC-Expire=86400&HW-CC-Sign=DBD38D86696AC5E32C09308ECC3493279A886151E4962A112392846D35D7FC8E "点击放大")

### 断点判断

| 横纵断点 | 设备 |
| --- | --- |
| 横向断点xs，纵向断点sm | 智能手表（圆形屏） |

说明

由于手表等圆形屏幕设备在屏幕形态和使用场景上的独特性，其交互方式和界面设计与普通设备有显著区别。为了确保用户体验的连贯性和功能的全面适配，建议在开发过程中专门为圆形屏幕设备进行界面和逻辑设计，并独立创建一个 HAP（HarmonyOS Ability Package）包进行发布和安装。

在开发穿戴应用时，需要将工程中module.json5的deviceTypes改为wearable，以确保应用能够在穿戴设备上正确部署和运行。可参考[穿戴服务](<../../../../../harmonyos-guides/系统/硬件/Wear Engine Kit（穿戴服务）/wear-engine-kit-guide.md>)了解能力介绍。

### 布局设计与实现

本节以手表的布局设计为例，提供了一份圆形屏的设计方案，确保内容布局完整、可实现简单交互，拓展并补充其他大型设备的功能。针对手表常见的开发场景，我们提出了推荐的设计方案和开发指导。

当显示的内容量超过单屏范围时，为确保用户能够方便、完整地查看所有信息，建议采用横向切屏和垂直切屏的布局策略。通过横向切屏，内容可沿水平方向分布，用户可通过左右滑动浏览额外信息，特别适用于内容宽度较大的情况。此外，垂直切屏允许信息在垂直方向扩展，用户可通过上下滚动访问更多信息，非常适合展示长列表或详细说明。综合应用这两种切屏方法，不仅可有效避免因内容拥挤而引起的视觉混乱，还可提升界面的美观度和用户交互体验，确保每部分内容都能清晰、有序地展示。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a9/v3/iaOGnlxbQu6_zMcAC9ES2A/zh-cn_image_0000002355266833.png?HW-CC-KV=V1&HW-CC-Date=20260612T020944Z&HW-CC-Expire=86400&HW-CC-Sign=64286C9DE030FEA413147AA7779A90E1F738501B1CAEFBBB637A75E53B7A40D1 "点击放大")

横向切屏，把更多内容切换至下一屏进行独立布置，以防止内容平铺导致的圆形屏幕边缘的信息丢失。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/96/v3/LCZz7zSDQeiKhq-1_fFO9Q/zh-cn_image_0000002321308130.png?HW-CC-KV=V1&HW-CC-Date=20260612T020944Z&HW-CC-Expire=86400&HW-CC-Sign=F975B3B445B797CA1B9E6A49D2A71B820D1BC11293BEFFCCA942876EA392DED1 "点击放大")

垂直切屏，拓展了手表上下信息承载的空间，增强了信息展示的连贯性。

ArkUI为圆形屏幕提供了部分弧形组件，建议开发者优先使用这些适配组件进行智能手表界面的开发。关于智能手表设备的开发指南，可以参考[智能穿戴应用开发](../../../../多端设备体验提升/穿戴/智能穿戴应用开发/bpta-smartwatch.md)。

| 组件名 | 备注 |
| --- | --- |
| [ArcList](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/滚动与滑动/ArcList/ts-container-arclist.md) | 弧形列表组件包含一系列列表项。适合连续、多行呈现同类数据，例如图片和文本。 |
| [ArcButton](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/按钮与选择/ArcButton/ohos-arkui-advanced-arcbutton.md) | 弧形按钮组件用于圆形屏幕使用。为手表用户提供强调、普通、警告等样式按钮。 |
| [ArcSlider](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/按钮与选择/ArcSlider/ohos-arkui-advanced-arcslider.md) | 弧形滑动组件，通常用于在圆形屏幕中快速调节设置值，如音量调节、亮度调节等应用场景。 |
| [ArcScrollBar](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/滚动与滑动/ArcScrollBar/ts-basic-components-arcscrollbar.md) | 弧形滚动条组件，用于配合可滚动组件使用，如[ArcList](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/滚动与滑动/ArcList/ts-container-arclist.md)、[List](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/滚动与滑动/List/ts-container-list.md)、[Grid](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/滚动与滑动/Grid/ts-container-grid.md)、[Scroll](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/滚动与滑动/Scroll/ts-container-scroll.md)、[WaterFlow](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/滚动与滑动/WaterFlow/ts-container-waterflow.md)。 |
| [ArcAlphabetIndexer](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/信息展示/ArcAlphabetIndexer/ts-container-arc-alphabet-indexer.md) | 弧形索引条是一种弧形的、可按字母顺序排序进行快速定位的组件，可以与容器组件联动，按逻辑结构快速定位至容器显示区域。 |
| [ArcSwiper](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/滚动与滑动/ArcSwiper/ts-container-arcswiper.md) | 弧形滑块视图容器，提供子组件滑动轮播显示的能力。 |
| [ArcListItem](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/滚动与滑动/ArcListItem/ts-container-arclistitem.md) | 用来展示列表具体子组件，必须配合[ArcList](../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS组件/滚动与滑动/ArcList/ts-container-arclist.md)来使用。 |

说明

弧形组件从API version 18开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

智能手表特殊的圆形表盘，需要在设计手表页面时进行考虑。圆形表盘的设计决定了需要给表页面最外层容器添加borderRadius属性，并为其设置一个50%大小的圆角。

```
1. build() {
2. Navigation(this.pathStack) {
3. // ...
4. }
5. .backgroundColor(Color.Black)
6. .hideTitleBar(true)
7. .hideToolBar(true)
8. .height('100%')
9. .width('100%')
10. .borderRadius('50%')
11. }
```

[Index.ets](https://gitcode.com/HarmonyOS_Samples/SmartWatchCarControl/blob/master/entry/src/main/ets/pages/Index.ets#L25-L42)

内容通常需要居中，保证在圆表屏幕下能够正常显示，示意图如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1/v3/zVMKRCS9SxOqHOJKjprTxQ/zh-cn_image_0000002494502253.png?HW-CC-KV=V1&HW-CC-Date=20260612T020944Z&HW-CC-Expire=86400&HW-CC-Sign=7B5F8226C86FB74376482E470964015BBEF100EE765F9699E0C5B2E6783DD977 "点击放大")

智能手表页面设计通常包含上下滑动或左右滑动实现页面切换的场景，建议使用手表特有组件ArcSwiper组件，实现手表上页面滑动切换的效果，效果示意图如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9d/v3/ggL2hEwRQ_eB8Juhm7qKFQ/zh-cn_image_0000002461462726.gif?HW-CC-KV=V1&HW-CC-Date=20260612T020944Z&HW-CC-Expire=86400&HW-CC-Sign=F9DDE7C0F9286C55323222A283492BBD6188A36B124523E04898891514AE712C "点击放大")

```
1. ArcSwiper() {
2. CarInformationView()
3. CarControlView({ pathStack: this.pathStack })
4. }
```

[Index.ets](https://gitcode.com/HarmonyOS_Samples/SmartWatchCarControl/blob/master/entry/src/main/ets/pages/Index.ets#L29-L32)
