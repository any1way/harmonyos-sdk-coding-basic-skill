---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview
title: 模块描述
breadcrumb: API参考 > 应用框架 > ArkWeb（方舟Web） > ArkTS API > @ohos.web.webview (Webview) > 模块描述
category: harmonyos-references
scraped_at: 2026-06-11T16:00:15+08:00
doc_updated_at: 2026-06-03
content_hash: sha256:d1b36cec2cc89dcd098b4063b1d2fc8e5bc915212cb46d3b1e871ca4568ced51
---
本模块提供Web控制能力，网页显示的能力请参考[组件描述](<../../../ArkTS 组件/Web/组件描述/arkts-basic-components-web.md>)。

元服务中使用ArkWeb的说明，请参考[Web组件概述](https://developer.huawei.com/consumer/cn/doc/atomic-guides/atomicserviceweb-guidelines)。

说明

* 本模块首批接口从API version 9开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。
* 示例效果请以真机运行为准。
* 静态方法必须在用户界面（UI）线程上使用。

该模块提供以下Web控制相关的常用功能：

* [AdsBlockManager](<../Class (AdsBlockManager)/arkts-apis-webview-adsblockmanager.md>)：广告过滤配置。
* [BackForwardCacheOptions](<../Class (BackForwardCacheOptions)/arkts-apis-webview-backforwardcacheoptions.md>)：前进后退缓存配置。
* [BackForwardCacheSupportedFeatures](<../Class (BackForwardCacheSupportedFeatures)/arkts-apis-webview-backforwa_37427919.md>)：设置前进后退缓存配置所支持的特性。
* [GeolocationPermissions](<../Class (GeolocationPermissions)/arkts-apis-webview-geolocationpermissions.md>)：地理位置权限配置。
* [JsMessageExt](<../Class (JsMessageExt)/arkts-apis-webview-jsmessageext.md>)：执行JavaScript脚本的结果。
* [MediaSourceInfo](<../Class (MediaSourceInfo)/arkts-apis-webview-mediasourceinfo.md>)：媒体源信息。
* [NativeMediaPlayerSurfaceInfo](<../Class (NativeMediaPlayerSurfaceInfo)/arkts-apis-webview-nativemediaplayersurfaceinfo.md>)：应用接管媒体播放时渲染信息。
* [PdfData](<../Class (PdfData)/arkts-apis-webview-pdfdata.md>)：生成的PDF输出数据。
* [ProxyConfig](<../Class (ProxyConfig)/arkts-apis-webview-proxyconfig.md>)：网络代理配置。
* [ProxyController](<../Class (ProxyController)/arkts-apis-webview-proxycontroller.md>)：网络代理控制器。
* [WebviewController](<../Class (WebviewController)/arkts-apis-webview-webviewcontroller.md>)：Web组件控制器。
* [WebCookieManager](<../Class (WebCookieManager)/arkts-apis-webview-webcookiemanager.md>)：Cookie管理。
* [WebDataBase](<../Class (WebDataBase)/arkts-apis-webview-webdatabase.md>)：数据库管理。
* [WebDownloadDelegate](<../Class (WebDownloadDelegate)/arkts-apis-webview-webdownloaddelegate.md>)：下载任务状态事件。
* [WebDownloadItem](<../Class (WebDownloadItem)/arkts-apis-webview-webdownloaditem.md>)：下载任务。
* [WebDownloadManager](<../Class (WebDownloadManager)/arkts-apis-webview-webdownloadmanager.md>)：下载任务管理。
* [WebHttpBodyStream](<../Class (WebHttpBodyStream)/arkts-apis-webview-webhttpbodystream.md>)：HTTP请求体。
* [WebMessageExt](<../Class (WebMessageExt)/arkts-apis-webview-webmessageext.md>)：前端与应用通信数据对象。
* [WebResourceHandler](<../Class (WebResourceHandler)/arkts-apis-webview-webresourcehandler.md>)：资源加载控制。
* [WebSchemeHandler](<../Class (WebSchemeHandler)/arkts-apis-webview-webschemehandler.md>)：指定Scheme的请求拦截器。
* [WebSchemeHandlerRequest](<../Class (WebSchemeHandlerRequest)/arkts-apis-webview-webschemehandlerrequest.md>)：通过拦截器拦截到的请求。
* [WebSchemeHandlerResponse](<../Class (WebSchemeHandlerResponse)/arkts-apis-webview-webschemehandlerresponse.md>)：为拦截到的请求创建自定义响应。
* [WebStorage](<../Class (WebStorage)/arkts-apis-webview-webstorage.md>)：Web组件存储操作接口。
* [BackForwardList](<../Interface (BackForwardList)/arkts-apis-webview-backforwardlist.md>)：历史信息列表。
* [NativeMediaPlayerBridge](<../Interface (NativeMediaPlayerBridge)/arkts-apis-webview-nativemediaplayerbridge.md>)：托管网页媒体播放器桥接接口。
* [NativeMediaPlayerHandler](<../Interface (NativeMediaPlayerHandler)/arkts-apis-webview-nativemediaplayerhandler.md>)：托管网页媒体播放器的事件接口。
* [WebMessagePort](<../Interface (WebMessagePort)/arkts-apis-webview-webmessageport.md>)：网页前端与应用的消息端口。

## 需要权限

PhonePC/2in1TabletTVWearable

访问在线网页时需添加网络权限：ohos.permission.INTERNET，具体申请方式请参考[声明权限](../../../../../harmonyos-guides/系统/安全/程序访问控制/应用权限管控/申请应用权限/声明权限/declare-permissions.md)。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { webview } from '@kit.ArkWeb';
```

**系统能力：** SystemCapability.Web.Webview.Core
