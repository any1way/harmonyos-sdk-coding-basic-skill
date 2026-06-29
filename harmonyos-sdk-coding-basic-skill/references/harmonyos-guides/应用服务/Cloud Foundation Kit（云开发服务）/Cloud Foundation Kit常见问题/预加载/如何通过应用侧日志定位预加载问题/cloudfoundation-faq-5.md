---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cloudfoundation-faq-5
title: 如何通过应用侧日志定位预加载问题
breadcrumb: 指南 > 应用服务 > Cloud Foundation Kit（云开发服务） > Cloud Foundation Kit常见问题 > 预加载 > 如何通过应用侧日志定位预加载问题
category: harmonyos-guides
scraped_at: 2026-06-11T15:06:20+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:eb4e35873f3179659331e4ba7e2a3b0e46734c21a26c22fbbda32e408bc12c96
---
预加载的日志进程为“clouddevelopproxy”，日志过滤选择“No filters”。

下文列举几种场景下的日志提示信息：

* 场景一：系统服务在应用安装期间预加载数据成功

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ba/v3/NuzaqydhSpW5OqLzCwjYOA/zh-cn_image_0000002622698877.png?HW-CC-KV=V1&HW-CC-Date=20260611T070619Z&HW-CC-Expire=86400&HW-CC-Sign=9CC2865BFC0F2F9CF547B2769C0832845A11BD39FCD0808A1E123AC40D39D596)

  预加载数据成功时日志会提示：http onSuccess code: 200，并且提示预加载的数据大小：get rsp data, len 47（单位为字节）。
* 场景二：应用调用getPrefetchResult接口获取预加载数据成功

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0a/v3/z10DIV7rT0OfnuWc6I4EDQ/zh-cn_image_0000002592219316.png?HW-CC-KV=V1&HW-CC-Date=20260611T070619Z&HW-CC-Expire=86400&HW-CC-Sign=EA5DEA4ED1FCC81BD3E282C8D9E20B827D6B4F6E24418B8041238E6BEB0E7A3A)

  数据获取成功时，无Error级别日志，会提示OnGetPreloadCache: end status:0。
* 场景三：应用调用getPrefetchResult接口获取预加载数据失败

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/da/v3/17A1LxjERkCoQVkvSTQHAQ/zh-cn_image_0000002592379250.png?HW-CC-KV=V1&HW-CC-Date=20260611T070619Z&HW-CC-Expire=86400&HW-CC-Sign=F4FA9E9AECD97369FD6D6C3933C1C2008708AB5F4333C6042370C939BE31615D)

  **问题现象**

  数据获取失败时，存在Error级别日志，会提示GetPreloadData get cache fail。

  **解决措施**

  出现此问题，可按照如下步骤排查和解决：

  1. 检查系统服务在应用安装期间预加载数据的日志。如果打印日志与上文场景一提示的日志信息不一致，则继续执行后续步骤。
  2. 确认是否存在多次调用安装预加载接口问题。安装预加载接口不支持多次调用。
  3. 排除以上原因后，检查日志中是否出现“appid \*\*\*\* is not in white list, to skip”或者“XXX Read timed out”。如果出现，请参考[运行应用时提示“appid \*\*\*\* is not in white list, to skip”](<../运行应用时提示“appid is not in white list, to skip”/cloudfoundation-faq-3.md>)或者[运行应用时报“XXX Read timed out”异常](<../运行应用时报“XXX Read timed out”异常/cloudfoundation-faq-4.md>)解决。
