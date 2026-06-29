---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/system-share-overview
title: 概述
breadcrumb: 指南 > 应用服务 > Share Kit（分享服务） > 系统分享 > 概述
category: harmonyos-guides
scraped_at: 2026-06-11T15:15:07+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:852ccb539d765d70db0d2971356f8a9a5c97ee67ea71987aacb0290fbcb8d39d
---

## 场景介绍

在手机设备中，分享框通过模态弹窗方式被拉起，效果如下图所示。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/59/v3/ysfNk_1ASQe1OpKBFxNL6w/zh-cn_image_0000002592379546.png?HW-CC-KV=V1&HW-CC-Date=20260611T071506Z&HW-CC-Expire=86400&HW-CC-Sign=D6D6849C63CF8C97D5B9FA88156AC637206610ED0BE6F911D6911925D760C328)

在2in1设备上分享框通过Popup形式展示，效果如图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7a/v3/k8crjZ-ATwyTkxCSIZizZw/zh-cn_image_0000002622859055.png?HW-CC-KV=V1&HW-CC-Date=20260611T071506Z&HW-CC-Expire=86400&HW-CC-Sign=035DF442562195965F0323A3BE15B6C400B160BF0EC320757717B865B9EBCD43)

1. 宿主应用可以分享一段文本、一个文件或一条备忘录到其他应用。
2. 宿主应用可以分享多个内容，如文本、图片等到其他应用。

## 业务流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5d/v3/CVhoOUt8QqG0ji5cRDxsQg/zh-cn_image_0000002622699175.png?HW-CC-KV=V1&HW-CC-Date=20260611T071506Z&HW-CC-Expire=86400&HW-CC-Sign=68ED69E83517C6E8B80989DCCEBE6E75334E556E5608A9419B45E9B2B0881630)

流程说明：

1、宿主应用构造分享数据、构造ShareController以及注册分享面板状态监听（可选）。

2、宿主应用拉起系统分享面板。

3、用户可选择目标设备或者应用。

4、目标应用处理分享数据，并关闭系统分享面板。

## 设计规范

宿主应用接入系统分享时，根据不同的内容类型，应选择恰当的分享方式。详细参见：[系统分享设计指南](https://developer.huawei.com/consumer/cn/doc/design-guides/share-0000001957076313)。
