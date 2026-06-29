---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/rcp_8h
title: rcp.h
breadcrumb: API参考 > 系统 > 网络 > Remote Communication Kit（远场通信服务） > C API > 头文件 > rcp.h
category: harmonyos-references
scraped_at: 2026-06-01T16:08:24+08:00
doc_updated_at: 2026-05-26
content_hash: sha256:96a6c8b4c1d44df086946cd51b17bc12e5f93b42b9da3b5e755aca5eba1ccfb1
---
## 概述

PhonePC/2in1TabletTVWearable

声明用于访问远程通信的API。提供基本的函数，结构体和const定义。

**引用文件：** <RemoteCommunicationKit/rcp.h>

**库：** librcp\_c.so

**系统能力：** SystemCapability.Collaboration.RemoteCommunication

**起始版本：** 5.0.0(12)

**相关模块：** [RemoteCommunication](../../模块/RemoteCommunication/remote-communication-overview.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 结构体

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| struct [Rcp\_Buffer](../../结构体/Rcp_Buffer/_rcp___buffer.md) | 文本存储结构。 |
| struct [Rcp\_ContentOrPathOrCallback](../../结构体/Rcp_ContentOrPathOrCallback/_rcp___content_or_path_or_callback.md) | [Rcp\_FormFieldFileValue](../../结构体/Rcp_FormFieldFileValue/_rcp___form_field_file_value.md)中使用的简单表单数据字段值。 |
| struct [Rcp\_FormFieldFileValue](../../结构体/Rcp_FormFieldFileValue/_rcp___form_field_file_value.md) | 表单字段文件值。 |
| struct [Rcp\_FormFieldValue](../../结构体/Rcp_FormFieldValue/_rcp___form_field_value.md) | 简单表单数据字段值，参见[Rcp\_Form](../../模块/RemoteCommunication/remote-communication-overview.md#rcp_form)和[Rcp\_MultipartFormFieldValue](../../结构体/Rcp_MultipartFormFieldValue/_rcp___multipart_form_field_value.md)。 |
| struct [Rcp\_MultipartFormFieldValue](../../结构体/Rcp_MultipartFormFieldValue/_rcp___multipart_form_field_value.md) | 多部分表单域值，在[Rcp\_MultipartForm](../../模块/RemoteCommunication/remote-communication-overview.md#rcp_multipartform)中使用。 |
| struct [Rcp\_RequestContent](../../结构体/Rcp_RequestContent/_rcp___request_content.md) | 请求的内容。 |
| struct [Rcp\_HeaderValue](../../结构体/Rcp_HeaderValue/_rcp___header_value.md) | 请求或响应的标头映射的值类型。 |
| struct [Rcp\_HeaderEntry](../../结构体/Rcp_HeaderEntry/_rcp___header_entry.md) | 请求或响应的标头的所有键值对。 |
| struct [Rcp\_Credential](../../结构体/Rcp_Credential/_rcp___credential.md) | 服务器身份验证中使用的身份验证凭据，包括用户名和密码。 |
| struct [Rcp\_ServerAuthentication](../../结构体/Rcp_ServerAuthentication/_rcp___server_authentication.md) | 服务器身份验证。 |
| struct [Rcp\_Urls](../../结构体/Rcp_Urls/_rcp___urls.md) | url，用于确定主机是否正在使用代理。 |
| struct [Rcp\_Exclusions](../../结构体/Rcp_Exclusions/_rcp___exclusions.md) | 代理配置中用于过滤不使用代理的urls。 |
| struct [Rcp\_CertificateAuthority](../../结构体/Rcp_CertificateAuthority/_rcp___certificate_authority.md) | 用于验证远程服务器标识的证书颁发机构（CA）。 |
| struct [Rcp\_ClientCertificate](../../结构体/Rcp_ClientCertificate/_rcp___client_certificate.md) | 发送到远程服务器的客户端证书，远程服务器将使用它来验证客户端的标识。 |
| struct [Rcp\_SecurityConfiguration](../../结构体/Rcp_SecurityConfiguration/_rcp___security_configuration.md) | 请求的安全配置。 |
| struct [Rcp\_WebProxy](../../结构体/Rcp_WebProxy/_rcp___web_proxy.md) | 自定义代理配置。 |
| struct [Rcp\_IpAndPort](../../结构体/Rcp_IpAndPort/_rcp___ip_and_port.md) | 该接口用在[Rcp\_DnsServers](../../结构体/Rcp_DnsServers/_rcp___dns_servers.md)中，表示一个DNS服务器的地址和端口。 |
| struct [Rcp\_DnsServers](../../结构体/Rcp_DnsServers/_rcp___dns_servers.md) | DNS服务器。[Rcp\_DnsConfiguration.dnsRules](../../结构体/Rcp_DnsConfiguration/_rcp___dns_configuration.md#dnsrules)中的类型之一。 |
| struct [Rcp\_IpAddress](../../结构体/Rcp_IpAddress/_rcp___ip_address.md) | 指定静态DNS规则使用的IP地址组。用于[Rcp\_StaticDnsRuleItem](../../结构体/Rcp_StaticDnsRuleItem/_rcp___static_dns_rule_item.md)。 |
| struct [Rcp\_StaticDnsRuleItem](../../结构体/Rcp_StaticDnsRuleItem/_rcp___static_dns_rule_item.md) | 描述单个静态DNS规则。 |
| struct [Rcp\_StaticDnsRule](../../结构体/Rcp_StaticDnsRule/_rcp___static_dns_rule.md) | 静态DNS规则。 |
| struct [Rcp\_DnsRule](../../结构体/Rcp_DnsRule/_rcp___dns_rule.md) | DNS规则配置。 |
| struct [Rcp\_OnDataReceiveCallback](../../结构体/Rcp_OnDataReceiveCallback/_rcp___on_data_receive_callback.md) | 接收到数据时回调。[Rcp\_EventsHandler](../../结构体/Rcp_EventsHandler/_rcp___events_handler.md)中的配置。 |
| struct [Rcp\_OnProgressCallback](../../结构体/Rcp_OnProgressCallback/_rcp___on_progress_callback.md) | 收发时回调配置，在[Rcp\_EventsHandler](../../结构体/Rcp_EventsHandler/_rcp___events_handler.md)中配置。 |
| struct [Rcp\_OnHeaderReceiveCallback](../../结构体/Rcp_OnHeaderReceiveCallback/_rcp___on_header_receive_callback.md) | [Rcp\_EventsHandler](../../结构体/Rcp_EventsHandler/_rcp___events_handler.md)中配置的接收到的header的回调配置。 |
| struct [Rcp\_OnVoidCallback](../../结构体/Rcp_OnVoidCallback/_rcp___on_void_callback.md) | 在[Rcp\_EventsHandler](../../结构体/Rcp_EventsHandler/_rcp___events_handler.md)中配置的数据结束或已取消事件的回调配置。 |
| struct [Rcp\_EventsHandler](../../结构体/Rcp_EventsHandler/_rcp___events_handler.md) | 监听不同HTTP事件的回调函数。 |
| struct [Rcp\_Timeout](../../结构体/Rcp_Timeout/_rcp___timeout.md) | 请求的超时配置 |
| struct [Rcp\_DnsOverHttps](../../结构体/Rcp_DnsOverHttps/_rcp___dns_over_https.md) | HTTPS上的DNS配置如果设置，则首选由DOH dns服务器解析的地址。 |
| struct [Rcp\_TransferConfiguration](../../结构体/Rcp_TransferConfiguration/_rcp___transfer_configuration.md) | 传输配置。 |
| struct [Rcp\_InfoToCollect](../../结构体/Rcp_InfoToCollect/_rcp___info_to_collect.md) | 指定要收集的请求处理事件。可以通过响应对象检查收集的事件。 |
| struct [Rcp\_TracingConfiguration](../../结构体/Rcp_TracingConfiguration/_rcp___tracing_configuration.md) | 请求追踪配置。 |
| struct [Rcp\_ProxyConfiguration](../../结构体/Rcp_ProxyConfiguration/_rcp___proxy_configuration.md) | 代理配置。 |
| struct [Rcp\_DnsConfiguration](../../结构体/Rcp_DnsConfiguration/_rcp___dns_configuration.md) | DNS解析配置。 |
| struct [Rcp\_Configuration](../../结构体/Rcp_Configuration/_rcp___configuration.md) | 请求配置。 |
| struct [Rcp\_TransferRange](../../结构体/Rcp_TransferRange/_rcp___transfer_range.md) | HTTP传输范围。该设置将转换为HTTP Range标头。具有范围标头的HTTP请求要求服务器仅发送回HTTP响应的一部分。 |
| struct [Rcp\_Request](../../结构体/Rcp_Request/_rcp___request.md) | 网络请求。 |
| struct [Rcp\_RequestCookieEntry](../../结构体/Rcp_RequestCookieEntry/_rcp___request_cookie_entry.md) | 描述请求的所有Cookie键值对。 |
| struct [Rcp\_DebugInfo](../../结构体/Rcp_DebugInfo/_rcp___debug_info.md) | 描述存储在[Rcp\_Response](../../结构体/Rcp_Response/_rcp___response.md)中的调试信息的结构。 |
| struct [Rcp\_CookieAttributeEntry](../../结构体/Rcp_CookieAttributeEntry/_rcp___cookie_attribute_entry.md) | 响应Cookie属性条目。 |
| struct [Rcp\_ResponseCookies](../../结构体/Rcp_ResponseCookies/_rcp___response_cookies.md) | 响应Cookie。 |
| struct [Rcp\_TimeInfo](../../结构体/Rcp_TimeInfo/_rcp___time_info.md) | 响应计时信息。 |
| struct [Rcp\_ResponseCallbackObject](../../结构体/Rcp_ResponseCallbackObject/_rcp___response_callback_object.md) | 响应回调结构体。 |
| struct [Rcp\_Response](../../结构体/Rcp_Response/_rcp___response.md) | 网络请求的响应。 |
| struct [Rcp\_Interceptor](../../结构体/Rcp_Interceptor/_rcp___interceptor.md) | 异步拦截器。 |
| struct [Rcp\_SyncInterceptor](../../结构体/Rcp_SyncInterceptor/_rcp___sync_interceptor.md) | 同步拦截器 |
| struct [Rcp\_InterceptorArray](../../结构体/Rcp_InterceptorArray/_rcp___interceptor_array.md) | 异步拦截器数组。 |
| struct [Rcp\_SyncInterceptorArray](../../结构体/Rcp_SyncInterceptorArray/_rcp___sync_interceptor_array.md) | 同步拦截器数组。 |
| struct [Rcp\_SessionListener](../../结构体/Rcp_SessionListener/_rcp___session_listener.md) | 关闭或取消会话事件的回调函数。 |
| struct [Rcp\_ConnectionConfiguration](../../结构体/Rcp_ConnectionConfiguration/_rcp___connection_configuration.md) | 连接配置。 |
| struct [Rcp\_SessionConfiguration](../../结构体/Rcp_SessionConfiguration/_rcp___session_configuration.md) | 会话配置。 |
| struct [Rcp\_OnBinaryReceiveCallback](../../结构体/Rcp_OnBinaryReceiveCallback/_rcp___on_binary_receive_callback.md) | 接收到响应数据时的回调。支持二进制数据的接收。使用[HMS\_Rcp\_SetRequestOnBinaryDataRecvCallback](../../模块/RemoteCommunication/remote-communication-overview.md#hms_rcp_setrequestonbinarydatarecvcallback)给请求设置。 |
| struct [Rcp\_OnStatusCodeReceiveCallback](../../结构体/Rcp_OnStatusCodeReceiveCallback/_rcp___on_status_code_callback.md) | 接收到响应状态码时的回调。使用[HMS\_Rcp\_SetRequestOnStatusCodeReceiveCallback](../../模块/RemoteCommunication/remote-communication-overview.md#hms_rcp_setrequestonstatuscodereceivecallback)给请求设置。 |

### 宏定义

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| [RCP\_MAX\_REQUEST\_ID\_LEN](../../模块/RemoteCommunication/remote-communication-overview.md#rcp_max_request_id_len) 32 | 请求ID的最大长度。 |
| [RCP\_MAX\_CONTENT\_TYPE\_LEN](../../模块/RemoteCommunication/remote-communication-overview.md#rcp_max_content_type_len) 64 | 内容类型最大长度。 |
| [RCP\_MAX\_FILENAME\_LEN](../../模块/RemoteCommunication/remote-communication-overview.md#rcp_max_filename_len) 128 | 文件名最大长度。 |
| [RCP\_MAX\_PATH\_LEN](../../模块/RemoteCommunication/remote-communication-overview.md#rcp_max_path_len) 128 | 路径的最大长度。 |
| [RCP\_METHOD\_GET](../../模块/RemoteCommunication/remote-communication-overview.md#rcp_method_get) "GET" | HTTP get方法。 |
| [RCP\_METHOD\_HEAD](../../模块/RemoteCommunication/remote-communication-overview.md#rcp_method_head) "HEAD" | HTTP head方法。 |
| [RCP\_METHOD\_OPTIONS](../../模块/RemoteCommunication/remote-communication-overview.md#rcp_method_options) "OPTIONS" | HTTP options方法。 |
| [RCP\_METHOD\_TRACE](../../模块/RemoteCommunication/remote-communication-overview.md#rcp_method_trace) "TRACE" | HTTP trace方法。 |
| [RCP\_METHOD\_DELETE](../../模块/RemoteCommunication/remote-communication-overview.md#rcp_method_delete) "DELETE" | HTTP delete方法。 |
| [RCP\_METHOD\_POST](../../模块/RemoteCommunication/remote-communication-overview.md#rcp_method_post) "POST" | HTTP post方法。 |
| [RCP\_METHOD\_PUT](../../模块/RemoteCommunication/remote-communication-overview.md#rcp_method_put) "PUT" | HTTP put方法。 |
| [RCP\_METHOD\_PATCH](../../模块/RemoteCommunication/remote-communication-overview.md#rcp_method_patch) "PATCH" | HTTP patch方法。 |
| [RCP\_IP\_MAX\_LEN](../../模块/RemoteCommunication/remote-communication-overview.md#rcp_ip_max_len) 40 | IP地址的最大长度。 |
| [RCP\_HOST\_MAX\_LEN](../../模块/RemoteCommunication/remote-communication-overview.md#rcp_host_max_len) 256 | 主机名的最大长度。 |

### 类型定义

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| typedef enum [Rcp\_FormValueType](../../模块/RemoteCommunication/remote-communication-overview.md#rcp_formvaluetype) [Rcp\_FormValueType](../../模块/RemoteCommunication/remote-communication-overview.md#rcp_formvaluetype) | 表单值类型。 |
| typedef int(\* [Rcp\_GetDataCallback](../../模块/RemoteCommunication/remote-communication-overview.md#rcp_getdatacallback)) (char \*out, uint32\_t size) | 通过回调函数获取数据。当API需要将数据的下一部分发送到服务器时，将调用此回调。 |
| typedef enum [Rcp\_ContentOrPathOrCallbackType](../../模块/RemoteCommunication/remote-communication-overview.md#rcp_contentorpathorcallbacktype) [Rcp\_ContentOrPathOrCallbackType](../../模块/RemoteCommunication/remote-communication-overview.md#rcp_contentorpathorcallbacktype) | 回调的内容、路径或类型。用于区分[Rcp\_ContentOrPathOrCallback](../../结构体/Rcp_ContentOrPathOrCallback/_rcp___content_or_path_or_callback.md)中使用的数据。 |
| typedef struct [Rcp\_Buffer](../../结构体/Rcp_Buffer/_rcp___buffer.md) [Rcp\_Buffer](../../模块/RemoteCommunication/remote-communication-overview.md#rcp_buffer) | 文本存储结构。 |
| typedef struct [Rcp\_ContentOrPathOrCallback](../../结构体/Rcp_ContentOrPathOrCallback/_rcp___content_or_path_or_callback.md) [Rcp\_ContentOrPathOrCallback](../../模块/RemoteCommunication/remote-communication-overview.md#rcp_contentorpathorcallback) | [Rcp\_FormFieldFileValue](../../结构体/Rcp_FormFieldFileValue/_rcp___form_field_file_value.md)中使用的简单表单数据字段值。 |
| typedef enum [Rcp\_MultipartValueType](../../模块/RemoteCommunication/remote-communication-overview.md#rcp_multipartvaluetype) [Rcp\_MultipartValueType](../../模块/RemoteCommunication/remote-communication-overview.md#rcp_multipartvaluetype) | 多部分值类型。用于区分[Rcp\_MultipartFormFieldValue](../../结构体/Rcp_MultipartFormFieldValue/_rcp___multipart_form_field_value.md)中使用的数据。 |
| typedef struct [Rcp\_FormFieldFileValue](../../结构体/Rcp_FormFieldFileValue/_rcp___form_field_file_value.md) [Rcp\_FormFieldFileValue](../../模块/RemoteCommunication/remote-communication-overview.md#rcp_formfieldfilevalue) | 表单字段文件值。 |
| typedef struct [Rcp\_FormFieldValue](../../结构体/Rcp_FormFieldValue/_rcp___form_field_value.md) [Rcp\_FormFieldValue](../../模块/RemoteCommunication/remote-communication-overview.md#rcp_formfieldvalue) | 简单表单数据字段值，参见[Rcp\_Form](../../模块/RemoteCommunication/remote-communication-overview.md#rcp_form)和[Rcp\_MultipartFormFieldValue](../../结构体/Rcp_MultipartFormFieldValue/_rcp___multipart_form_field_value.md)。 |
| typedef struct [Rcp\_MultipartFormFieldValue](../../结构体/Rcp_MultipartFormFieldValue/_rcp___multipart_form_field_value.md) [Rcp\_MultipartFormFieldValue](../../模块/RemoteCommunication/remote-communication-overview.md#rcp_multipartformfieldvalue) | 多部分表单域值，在[Rcp\_MultipartForm](../../模块/RemoteCommunication/remote-communication-overview.md#rcp_multipartform)中使用。 |
| typedef enum [Rcp\_ContentType](../../模块/RemoteCommunication/remote-communication-overview.md#rcp_contenttype) [Rcp\_ContentType](../../模块/RemoteCommunication/remote-communication-overview.md#rcp_contenttype) | 内容类型。用于区分[Rcp\_RequestContent](../../结构体/Rcp_RequestContent/_rcp___request_content.md)中使用的数据。 |
| typedef struct [Rcp\_Form](../../模块/RemoteCommunication/remote-communication-overview.md#rcp_form) [Rcp\_Form](../../模块/RemoteCommunication/remote-communication-overview.md#rcp_form) | 简单表单。 |
| typedef struct [Rcp\_MultipartForm](../../模块/RemoteCommunication/remote-communication-overview.md#rcp_multipartform) [Rcp\_MultipartForm](../../模块/RemoteCommunication/remote-communication-overview.md#rcp_multipartform) | 多部分表单。 |
| typedef struct [Rcp\_RequestContent](../../结构体/Rcp_RequestContent/_rcp___request_content.md) [Rcp\_RequestContent](../../模块/RemoteCommunication/remote-communication-overview.md#rcp_requestcontent) | 请求的内容。 |
| typedef struct [Rcp\_Headers](../../模块/RemoteCommunication/remote-communication-overview.md#rcp_headers) [Rcp\_Headers](../../模块/RemoteCommunication/remote-communication-overview.md#rcp_headers) | 请求或响应的标头。 |
| typedef struct [Rcp\_HeaderValue](../../结构体/Rcp_HeaderValue/_rcp___header_value.md) [Rcp\_HeaderValue](../../模块/RemoteCommunication/remote-communication-overview.md#rcp_headervalue) | 请求或响应的标头映射的值类型。 |
| typedef struct [Rcp\_HeaderEntry](../../结构体/Rcp_HeaderEntry/_rcp___header_entry.md) [Rcp\_HeaderEntry](../../模块/RemoteCommunication/remote-communication-overview.md#rcp_headerentry) | 请求或响应的标头的所有键值对。 |
| typedef enum [Rcp\_AuthenticationType](../../模块/RemoteCommunication/remote-communication-overview.md#rcp_authenticationtype) [Rcp\_AuthenticationType](../../模块/RemoteCommunication/remote-communication-overview.md#rcp_authenticationtype) | 枚举类型。服务器的身份验证类型。如果未设置，请与服务器协商。 |
| typedef struct [Rcp\_Credential](../../结构体/Rcp_Credential/_rcp___credential.md) [Rcp\_Credential](../../模块/RemoteCommunication/remote-communication-overview.md#rcp_credential) | 服务器身份验证中使用的身份验证凭据，包括用户名和密码。 |
| typedef struct [Rcp\_ServerAuthentication](../../结构体/Rcp_ServerAuthentication/_rcp___server_authentication.md) [Rcp\_ServerAuthentication](../../模块/RemoteCommunication/remote-communication-overview.md#rcp_serverauthentication) | 服务器身份验证。 |
| typedef bool(\* [Rcp\_ExclusionFunction](../../模块/RemoteCommunication/remote-communication-overview.md#rcp_exclusionfunction)) (const char \*url) | 判断host是否使用代理的函数指针。 |
| typedef struct [Rcp\_Urls](../../结构体/Rcp_Urls/_rcp___urls.md) [Rcp\_Urls](../../模块/RemoteCommunication/remote-communication-overview.md#rcp_urls) | url，用于确定主机是否正在使用代理。 |
| typedef enum [Rcp\_ExclusionsValueType](../../模块/RemoteCommunication/remote-communication-overview.md#rcp_exclusionsvaluetype) [Rcp\_ExclusionsValueType](../../模块/RemoteCommunication/remote-communication-overview.md#rcp_exclusionsvaluetype) | 代理排除中使用的数据类型. 用于区分[Rcp\_Exclusions](../../结构体/Rcp_Exclusions/_rcp___exclusions.md)中使用的数据。 |
| typedef struct [Rcp\_Exclusions](../../结构体/Rcp_Exclusions/_rcp___exclusions.md) [Rcp\_Exclusions](../../模块/RemoteCommunication/remote-communication-overview.md#rcp_exclusions) | 代理配置中用于过滤不使用代理的URLs。 |
| typedef enum [Rcp\_CertType](../../模块/RemoteCommunication/remote-communication-overview.md#rcp_certtype) [Rcp\_CertType](../../模块/RemoteCommunication/remote-communication-overview.md#rcp_certtype) | 客户端证书类型。 |
| typedef struct [Rcp\_CertificateAuthority](../../结构体/Rcp_CertificateAuthority/_rcp___certificate_authority.md) [Rcp\_CertificateAuthority](../../模块/RemoteCommunication/remote-communication-overview.md#rcp_certificateauthority) | 用于验证远程服务器标识的证书颁发机构（CA）。 |
| typedef struct [Rcp\_ClientCertificate](../../结构体/Rcp_ClientCertificate/_rcp___client_certificate.md) [Rcp\_ClientCertificate](../../模块/RemoteCommunication/remote-communication-overview.md#rcp_clientcertificate) | 发送到远程服务器的客户端证书，远程服务器将使用它来验证客户端的标识。 |
| typedef enum [Rcp\_RemoteValidationType](../../模块/RemoteCommunication/remote-communication-overview.md#rcp_remotevalidationtype) [Rcp\_RemoteValidationType](../../模块/RemoteCommunication/remote-communication-overview.md#rcp_remotevalidationtype) | 远程验证类型。 |
| typedef struct [Rcp\_SecurityConfiguration](../../结构体/Rcp_SecurityConfiguration/_rcp___security_configuration.md) [Rcp\_SecurityConfiguration](../../模块/RemoteCommunication/remote-communication-overview.md#rcp_securityconfiguration) | 请求的安全配置。 |
| typedef enum [Rcp\_ProxyTunnelMode](../../模块/RemoteCommunication/remote-communication-overview.md#rcp_proxytunnelmode) [Rcp\_ProxyTunnelMode](../../模块/RemoteCommunication/remote-communication-overview.md#rcp_proxytunnelmode) | 用于控制何时创建代理隧道。 隧道或隧道传输意味着向代理发送HTTP CONNECT请求，要求它连接到特定端口号上的远程主机，然后流量只是通过代理。“auto”表示为HTTPS创建隧道。“always”表示始终创建隧道。 |
| typedef struct [Rcp\_WebProxy](../../结构体/Rcp_WebProxy/_rcp___web_proxy.md) [Rcp\_WebProxy](../../模块/RemoteCommunication/remote-communication-overview.md#rcp_webproxy) | 自定义代理配置。 |
| typedef struct [Rcp\_IpAndPort](../../结构体/Rcp_IpAndPort/_rcp___ip_and_port.md) [Rcp\_IpAndPort](../../模块/RemoteCommunication/remote-communication-overview.md#rcp_ipandport) | 该接口用在[Rcp\_DnsServers](../../结构体/Rcp_DnsServers/_rcp___dns_servers.md)中，表示一个DNS服务器的地址和端口。 |
| typedef struct [Rcp\_DnsServers](../../结构体/Rcp_DnsServers/_rcp___dns_servers.md) [Rcp\_DnsServers](../../模块/RemoteCommunication/remote-communication-overview.md#rcp_dnsservers) | DNS服务器。[Rcp\_DnsConfiguration.dnsRules](../../结构体/Rcp_DnsConfiguration/_rcp___dns_configuration.md#dnsrules)中的类型之一。 |
| typedef struct [Rcp\_IpAddress](../../结构体/Rcp_IpAddress/_rcp___ip_address.md) [Rcp\_IpAddress](../../模块/RemoteCommunication/remote-communication-overview.md#rcp_ipaddress) | 指定静态DNS规则使用的IP地址组。用于[Rcp\_StaticDnsRuleItem](../../结构体/Rcp_StaticDnsRuleItem/_rcp___static_dns_rule_item.md)。 |
| typedef struct [Rcp\_StaticDnsRuleItem](../../结构体/Rcp_StaticDnsRuleItem/_rcp___static_dns_rule_item.md) [Rcp\_StaticDnsRuleItem](../../模块/RemoteCommunication/remote-communication-overview.md#rcp_staticdnsruleitem) | 描述单个静态DNS规则。 |
| typedef struct [Rcp\_StaticDnsRule](../../结构体/Rcp_StaticDnsRule/_rcp___static_dns_rule.md) [Rcp\_StaticDnsRule](../../模块/RemoteCommunication/remote-communication-overview.md#rcp_staticdnsrule) | 静态DNS规则。 |
| typedef [Rcp\_IpAddress](../../结构体/Rcp_IpAddress/_rcp___ip_address.md) \*(\* [Rcp\_DynamicDnsRuleFunction](../../模块/RemoteCommunication/remote-communication-overview.md#rcp_dynamicdnsrulefunction)) (const char \*host, uint16\_t port) | 一个可以根据主机名和端口直接返回IP地址的函数。用于动态DNS解析。 |
| typedef enum [Rcp\_DnsRuleType](../../模块/RemoteCommunication/remote-communication-overview.md#rcp_dnsruletype) [Rcp\_DnsRuleType](../../模块/RemoteCommunication/remote-communication-overview.md#rcp_dnsruletype) | DNS规则类型。用于区分[Rcp\_DnsRule](../../结构体/Rcp_DnsRule/_rcp___dns_rule.md)中使用的dns规则类型。 |
| typedef struct [Rcp\_DnsRule](../../结构体/Rcp_DnsRule/_rcp___dns_rule.md) [Rcp\_DnsRule](../../模块/RemoteCommunication/remote-communication-overview.md#rcp_dnsrule) | DNS规则配置。 |
| typedef size\_t(\* [Rcp\_OnDataReceiveCallbackFunc](../../模块/RemoteCommunication/remote-communication-overview.md#rcp_ondatareceivecallbackfunc)) (void \*usrObject, const char \*data) | 接收到响应正文时调用的回调函数。 |
| typedef size\_t(\* [Rcp\_OnBinaryReceiveCallbackFunc](../../模块/RemoteCommunication/remote-communication-overview.md#rcp_onbinaryreceivecallbackfunc)) (void \*usrObject, [Rcp\_Buffer](../../结构体/Rcp_Buffer/_rcp___buffer.md) \*buffer) | 接收到响应正文时调用的回调函数（二进制数据）。 |
| typedef void (\* [Rcp\_OnStatusCodeReceiveCallbackFunc](../../模块/RemoteCommunication/remote-communication-overview.md#rcp_onstatuscodereceivecallbackfunc))(void \*usrObject, uint32\_t statusCode) | 接收到响应状态码时调用的回调函数。 |
| typedef void(\* [Rcp\_OnProgressCallbackFunc](../../模块/RemoteCommunication/remote-communication-overview.md#rcp_onprogresscallbackfunc)) (void \*usrObject, uint64\_t totalSize, uint64\_t transferredSize) | 请求/响应数据传输过程中调用的回调函数。 |
| typedef void(\* [Rcp\_OnHeaderReceiveCallbackFunc](../../模块/RemoteCommunication/remote-communication-overview.md#rcp_onheaderreceivecallbackfunc)) (void \*usrObject, [Rcp\_Headers](../../模块/RemoteCommunication/remote-communication-overview.md#rcp_headers) \*headers) | 收到所有请求时调用的回调。 |
| typedef void(\* [Rcp\_OnVoidCallbackFunc](../../模块/RemoteCommunication/remote-communication-overview.md#rcp_onvoidcallbackfunc)) (void \*usrObject) | 请求的DataEnd或Canceled事件回调的回调函数。 |
| typedef struct [Rcp\_OnDataReceiveCallback](../../结构体/Rcp_OnDataReceiveCallback/_rcp___on_data_receive_callback.md) [Rcp\_OnDataReceiveCallback](../../模块/RemoteCommunication/remote-communication-overview.md#rcp_ondatareceivecallback) | 接收到数据时回调。[Rcp\_EventsHandler](../../结构体/Rcp_EventsHandler/_rcp___events_handler.md)中的配置。 |
| typedef struct [Rcp\_OnProgressCallback](../../结构体/Rcp_OnProgressCallback/_rcp___on_progress_callback.md) [Rcp\_OnProgressCallback](../../模块/RemoteCommunication/remote-communication-overview.md#rcp_onprogresscallback) | 收发时回调配置，在[Rcp\_EventsHandler](../../结构体/Rcp_EventsHandler/_rcp___events_handler.md)中配置。 |
| typedef struct [Rcp\_OnHeaderReceiveCallback](../../结构体/Rcp_OnHeaderReceiveCallback/_rcp___on_header_receive_callback.md) [Rcp\_OnHeaderReceiveCallback](../../模块/RemoteCommunication/remote-communication-overview.md#rcp_onheaderreceivecallback) | [Rcp\_EventsHandler](../../结构体/Rcp_EventsHandler/_rcp___events_handler.md)中配置的接收到的header的回调配置。 |
| typedef struct [Rcp\_OnVoidCallback](../../结构体/Rcp_OnVoidCallback/_rcp___on_void_callback.md) [Rcp\_OnVoidCallback](../../模块/RemoteCommunication/remote-communication-overview.md#rcp_onvoidcallback) | 在[Rcp\_EventsHandler](../../结构体/Rcp_EventsHandler/_rcp___events_handler.md)中配置的数据结束或已取消事件的回调配置。 |
| typedef struct [Rcp\_EventsHandler](../../结构体/Rcp_EventsHandler/_rcp___events_handler.md) [Rcp\_EventsHandler](../../模块/RemoteCommunication/remote-communication-overview.md#rcp_eventshandler) | 监听不同HTTP事件的回调函数。 |
| typedef struct [Rcp\_Timeout](../../结构体/Rcp_Timeout/_rcp___timeout.md) [Rcp\_Timeout](../../模块/RemoteCommunication/remote-communication-overview.md#rcp_timeout) | 请求的超时配置。 |
| typedef struct [Rcp\_DnsOverHttps](../../结构体/Rcp_DnsOverHttps/_rcp___dns_over_https.md) [Rcp\_DnsOverHttps](../../模块/RemoteCommunication/remote-communication-overview.md#rcp_dnsoverhttps) | HTTPS上的DNS配置如果设置，则首选由DOH dns服务器解析的地址。 |
| typedef enum [Rcp\_PathPreference](../../模块/RemoteCommunication/remote-communication-overview.md#rcp_pathpreference) [Rcp\_PathPreference](../../模块/RemoteCommunication/remote-communication-overview.md#rcp_pathpreference) | 请求路径首选项。 |
| typedef struct [Rcp\_TransferConfiguration](../../结构体/Rcp_TransferConfiguration/_rcp___transfer_configuration.md) [Rcp\_TransferConfiguration](../../模块/RemoteCommunication/remote-communication-overview.md#rcp_transferconfiguration) | 传输配置。 |
| typedef struct [Rcp\_InfoToCollect](../../结构体/Rcp_InfoToCollect/_rcp___info_to_collect.md) [Rcp\_InfoToCollect](../../模块/RemoteCommunication/remote-communication-overview.md#rcp_infotocollect) | 指定要收集的请求处理事件。可以通过响应对象检查收集的事件。 |
| typedef struct [Rcp\_TracingConfiguration](../../结构体/Rcp_TracingConfiguration/_rcp___tracing_configuration.md) [Rcp\_TracingConfiguration](../../模块/RemoteCommunication/remote-communication-overview.md#rcp_tracingconfiguration) | 请求追踪配置。 |
| typedef enum [Rcp\_ProxyType](../../模块/RemoteCommunication/remote-communication-overview.md#rcp_proxytype) [Rcp\_ProxyType](../../模块/RemoteCommunication/remote-communication-overview.md#rcp_proxytype) | 代理类型。用于区分不同的代理配置。 |
| typedef struct [Rcp\_ProxyConfiguration](../../结构体/Rcp_ProxyConfiguration/_rcp___proxy_configuration.md) [Rcp\_ProxyConfiguration](../../模块/RemoteCommunication/remote-communication-overview.md#rcp_proxyconfiguration) | 代理配置。 |
| typedef struct [Rcp\_DnsConfiguration](../../结构体/Rcp_DnsConfiguration/_rcp___dns_configuration.md) [Rcp\_DnsConfiguration](../../模块/RemoteCommunication/remote-communication-overview.md#rcp_dnsconfiguration) | DNS解析配置。 |
| typedef struct [Rcp\_Configuration](../../结构体/Rcp_Configuration/_rcp___configuration.md) [Rcp\_Configuration](../../模块/RemoteCommunication/remote-communication-overview.md#rcp_configuration) | 请求配置。 |
| typedef struct [Rcp\_TransferRange](../../结构体/Rcp_TransferRange/_rcp___transfer_range.md) [Rcp\_TransferRange](../../模块/RemoteCommunication/remote-communication-overview.md#rcp_transferrange) | HTTP传输范围。该设置将转换为HTTP Range标头。具有范围标头的HTTP请求要求服务器仅发送回HTTP响应的一部分。 |
| typedef struct [Rcp\_RequestCookies](../../模块/RemoteCommunication/remote-communication-overview.md#rcp_requestcookies) [Rcp\_RequestCookies](../../模块/RemoteCommunication/remote-communication-overview.md#rcp_requestcookies) | 请求Cookie。 |
| typedef struct [Rcp\_Request](../../结构体/Rcp_Request/_rcp___request.md) [Rcp\_Request](../../模块/RemoteCommunication/remote-communication-overview.md#rcp_request) | 网络请求。 |
| typedef struct [Rcp\_RequestCookieEntry](../../结构体/Rcp_RequestCookieEntry/_rcp___request_cookie_entry.md) [Rcp\_RequestCookieEntry](../../模块/RemoteCommunication/remote-communication-overview.md#rcp_requestcookieentry) | 描述请求的所有Cookie键值对。 |
| typedef enum [Rcp\_StatusCode](../../模块/RemoteCommunication/remote-communication-overview.md#rcp_statuscode) [Rcp\_StatusCode](../../模块/RemoteCommunication/remote-communication-overview.md#rcp_statuscode) | 请求响应的状态码。 |
| typedef enum [Rcp\_DebugEvent](../../模块/RemoteCommunication/remote-communication-overview.md#rcp_debugevent) [Rcp\_DebugEvent](../../模块/RemoteCommunication/remote-communication-overview.md#rcp_debugevent) | 描述调试信息的事件类型。 |
| typedef struct [Rcp\_DebugInfo](../../结构体/Rcp_DebugInfo/_rcp___debug_info.md) [Rcp\_DebugInfo](../../模块/RemoteCommunication/remote-communication-overview.md#rcp_debuginfo) | 描述存储在[Rcp\_Response](../../结构体/Rcp_Response/_rcp___response.md)中的调试信息的结构。 |
| typedef struct [Rcp\_CookieAttributes](../../模块/RemoteCommunication/remote-communication-overview.md#rcp_cookieattributes) [Rcp\_CookieAttributes](../../模块/RemoteCommunication/remote-communication-overview.md#rcp_cookieattributes) | 描述[Rcp\_Response](../../结构体/Rcp_Response/_rcp___response.md)中Cookie属性的类型。 |
| typedef struct [Rcp\_CookieAttributeEntry](../../结构体/Rcp_CookieAttributeEntry/_rcp___cookie_attribute_entry.md) [Rcp\_CookieAttributeEntry](../../模块/RemoteCommunication/remote-communication-overview.md#rcp_cookieattributeentry) | 响应Cookie属性条目。 |
| typedef struct [Rcp\_ResponseCookies](../../结构体/Rcp_ResponseCookies/_rcp___response_cookies.md) [Rcp\_ResponseCookies](../../模块/RemoteCommunication/remote-communication-overview.md#rcp_responsecookies) | 响应Cookie。 |
| typedef struct [Rcp\_TimeInfo](../../结构体/Rcp_TimeInfo/_rcp___time_info.md) [Rcp\_TimeInfo](../../模块/RemoteCommunication/remote-communication-overview.md#rcp_timeinfo) | 响应计时信息。 |
| typedef struct [Rcp\_Response](../../结构体/Rcp_Response/_rcp___response.md) [Rcp\_Response](../../模块/RemoteCommunication/remote-communication-overview.md#rcp_response) | 网络请求的响应。 |
| typedef void(\* [Rcp\_ResponseCallback](../../模块/RemoteCommunication/remote-communication-overview.md#rcp_responsecallback)) (void \*usrCtx, [Rcp\_Response](../../结构体/Rcp_Response/_rcp___response.md) \*response, uint32\_t errCode) | 响应回调函数指针。 |
| typedef struct [Rcp\_ResponseCallbackObject](../../结构体/Rcp_ResponseCallbackObject/_rcp___response_callback_object.md) [Rcp\_ResponseCallbackObject](../../模块/RemoteCommunication/remote-communication-overview.md#rcp_responsecallbackobject) | 响应回调结构体。 |
| typedef struct [Rcp\_RequestHandler](../../模块/RemoteCommunication/remote-communication-overview.md#rcp_requesthandler) [Rcp\_RequestHandler](../../模块/RemoteCommunication/remote-communication-overview.md#rcp_requesthandler) | 与[Rcp\_Interceptor](../../结构体/Rcp_Interceptor/_rcp___interceptor.md)关联的异步处理器。 |
| typedef struct [Rcp\_SyncRequestHandler](../../模块/RemoteCommunication/remote-communication-overview.md#rcp_syncrequesthandler) [Rcp\_SyncRequestHandler](../../模块/RemoteCommunication/remote-communication-overview.md#rcp_syncrequesthandler) | 与[Rcp\_SyncInterceptor](../../结构体/Rcp_SyncInterceptor/_rcp___sync_interceptor.md)关联的同步处理器。 |
| typedef struct [Rcp\_Interceptor](../../结构体/Rcp_Interceptor/_rcp___interceptor.md) [Rcp\_Interceptor](../../模块/RemoteCommunication/remote-communication-overview.md#rcp_interceptor) | 异步拦截器。 |
| typedef struct [Rcp\_SyncInterceptor](../../结构体/Rcp_SyncInterceptor/_rcp___sync_interceptor.md) [Rcp\_SyncInterceptor](../../模块/RemoteCommunication/remote-communication-overview.md#rcp_syncinterceptor) | 同步拦截器。 |
| typedef struct [Rcp\_InterceptorArray](../../结构体/Rcp_InterceptorArray/_rcp___interceptor_array.md) [Rcp\_InterceptorArray](../../模块/RemoteCommunication/remote-communication-overview.md#rcp_interceptorarray) | 异步拦截器数组。 |
| typedef struct [Rcp\_SyncInterceptorArray](../../结构体/Rcp_SyncInterceptorArray/_rcp___sync_interceptor_array.md) [Rcp\_SyncInterceptorArray](../../模块/RemoteCommunication/remote-communication-overview.md#rcp_syncinterceptorarray) | 同步拦截器数组。 |
| typedef enum [Rcp\_SessionType](../../模块/RemoteCommunication/remote-communication-overview.md#rcp_sessiontype) [Rcp\_SessionType](../../模块/RemoteCommunication/remote-communication-overview.md#rcp_sessiontype) | 会话类型。 |
| typedef struct [Rcp\_Session](../../模块/RemoteCommunication/remote-communication-overview.md#rcp_session) [Rcp\_Session](../../模块/RemoteCommunication/remote-communication-overview.md#rcp_session) | 会话。 |
| typedef struct [Rcp\_SessionListener](../../结构体/Rcp_SessionListener/_rcp___session_listener.md) [Rcp\_SessionListener](../../模块/RemoteCommunication/remote-communication-overview.md#rcp_sessionlistener) | 关闭或取消会话事件的回调函数。 |
| typedef struct [Rcp\_ConnectionConfiguration](../../结构体/Rcp_ConnectionConfiguration/_rcp___connection_configuration.md) [Rcp\_ConnectionConfiguration](../../模块/RemoteCommunication/remote-communication-overview.md#rcp_connectionconfiguration) | 连接配置。 |
| typedef struct [Rcp\_SessionConfiguration](../../结构体/Rcp_SessionConfiguration/_rcp___session_configuration.md) [Rcp\_SessionConfiguration](../../模块/RemoteCommunication/remote-communication-overview.md#rcp_sessionconfiguration) | 会话配置。 |
| typedef struct [Rcp\_OnBinaryReceiveCallback](../../结构体/Rcp_OnBinaryReceiveCallback/_rcp___on_binary_receive_callback.md) [Rcp\_OnBinaryReceiveCallback](../../结构体/Rcp_OnBinaryReceiveCallback/_rcp___on_binary_receive_callback.md) | 响应的二进制数据接收回调函数。 |
| typedef size\_t(\* [Rcp\_OnBinaryReceiveCallbackFunc](../../模块/RemoteCommunication/remote-communication-overview.md#rcp_onbinaryreceivecallbackfunc)) (void \*usrObject, [Rcp\_Buffer](../../结构体/Rcp_Buffer/_rcp___buffer.md) \*buffer) | 二进制数据接收回调函数指针。 |
| typedef struct [Rcp\_OnStatusCodeReceiveCallback](../../结构体/Rcp_OnStatusCodeReceiveCallback/_rcp___on_status_code_callback.md) [Rcp\_OnStatusCodeReceiveCallback](../../模块/RemoteCommunication/remote-communication-overview.md#rcp_onstatuscodereceivecallback) | 用于接收响应状态码的回调函数。 |

### 枚举

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| [Rcp\_FormValueType](../../模块/RemoteCommunication/remote-communication-overview.md#rcp_formvaluetype) {  RCP\_FORM\_VALUE\_TYPE\_INT32, RCP\_FORM\_VALUE\_TYPE\_INT64, RCP\_FORM\_VALUE\_TYPE\_BOOL, RCP\_FORM\_VALUE\_TYPE\_STRING,  RCP\_FORM\_VALUE\_TYPE\_DOUBLE  } | 表单值类型。 |
| [Rcp\_ContentOrPathOrCallbackType](../../模块/RemoteCommunication/remote-communication-overview.md#rcp_contentorpathorcallbacktype) { RCP\_FILE\_VALUE\_TYPE\_CONTENT, RCP\_FILE\_VALUE\_TYPE\_PATH, RCP\_FILE\_VALUE\_TYPE\_CALLBACK} | 回调的内容、路径或类型。用于区分[Rcp\_ContentOrPathOrCallback](../../结构体/Rcp_ContentOrPathOrCallback/_rcp___content_or_path_or_callback.md)中使用的数据。 |
| [Rcp\_MultipartValueType](../../模块/RemoteCommunication/remote-communication-overview.md#rcp_multipartvaluetype) { RCP\_TYPE\_FORM\_FIELD\_VALUE, RCP\_TYPE\_FORM\_FIELD\_FILE\_VALUE } | 多部分值类型。用于区分[Rcp\_MultipartFormFieldValue](../../结构体/Rcp_MultipartFormFieldValue/_rcp___multipart_form_field_value.md)中使用的数据。 |
| [Rcp\_ContentType](../../模块/RemoteCommunication/remote-communication-overview.md#rcp_contenttype) { RCP\_CONTENT\_TYPE\_STRING, RCP\_CONTENT\_TYPE\_FORM, RCP\_CONTENT\_TYPE\_MULTIPARTFORM, RCP\_CONTENT\_TYPE\_GETCALLBACK } | 内容类型。用于区分[Rcp\_RequestContent](../../结构体/Rcp_RequestContent/_rcp___request_content.md)中使用的数据。 |
| [Rcp\_AuthenticationType](../../模块/RemoteCommunication/remote-communication-overview.md#rcp_authenticationtype) { RCP\_AUTHENTICATION\_AUTO, RCP\_AUTHENTICATION\_BASIC, RCP\_AUTHENTICATION\_NTLM, RCP\_AUTHENTICATION\_DIGEST } | 枚举类型。服务器的身份验证类型。如果未设置，请与服务器协商。 |
| [Rcp\_ExclusionsValueType](../../模块/RemoteCommunication/remote-communication-overview.md#rcp_exclusionsvaluetype) { RCP\_EXCLUSION\_USE\_URL\_ARRAY, RCP\_EXCLUSION\_USE\_CALLBACK } | 代理排除中使用的数据类型. 用于区分[Rcp\_Exclusions](../../结构体/Rcp_Exclusions/_rcp___exclusions.md)中使用的数据。 |
| [Rcp\_CertType](../../模块/RemoteCommunication/remote-communication-overview.md#rcp_certtype) { RCP\_CERT\_PEM, RCP\_CERT\_DER, RCP\_CERT\_P12 } | 客户端证书类型。 |
| [Rcp\_RemoteValidationType](../../模块/RemoteCommunication/remote-communication-overview.md#rcp_remotevalidationtype) { RCP\_REMOTE\_VALIDATION\_SYSTEM, RCP\_REMOTE\_VALIDATION\_SKIP, RCP\_REMOTE\_VALIDATION\_CERTIFICATE\_AUTHORITY } | 远程验证类型。 |
| [Rcp\_ProxyTunnelMode](../../模块/RemoteCommunication/remote-communication-overview.md#rcp_proxytunnelmode) { RCP\_PROXY\_TUNNEL\_AUTO, RCP\_PROXY\_TUNNEL\_ALWAYS } | 用于控制何时创建代理隧道。 隧道或隧道传输意味着向代理发送HTTP CONNECT请求，要求它连接到特定端口号上的远程主机，然后流量只是通过代理。“auto”表示为HTTPS创建隧道。“always”表示始终创建隧道。 |
| [Rcp\_DnsRuleType](../../模块/RemoteCommunication/remote-communication-overview.md#rcp_dnsruletype) { RCP\_DNS\_RULE\_DNS\_SERVERS, RCP\_DNS\_RULE\_STATIC, RCP\_DNS\_RULE\_DYNAMIC } | DNS规则类型。用于区分[Rcp\_DnsRule](../../结构体/Rcp_DnsRule/_rcp___dns_rule.md)中使用的dns规则类型。 |
| [Rcp\_PathPreference](../../模块/RemoteCommunication/remote-communication-overview.md#rcp_pathpreference) { RCP\_PATH\_PREFERENCE\_AUTO, RCP\_PATH\_PREFERENCE\_WIFI, RCP\_PATH\_PREFERENCE\_CELLULAR } | 请求路径首选项。 |
| [Rcp\_ProxyType](../../模块/RemoteCommunication/remote-communication-overview.md#rcp_proxytype) { RCP\_PROXY\_SYSTEM, RCP\_PROXY\_CUSTOM, RCP\_PROXY\_NO\_PROXY } | 代理类型。用于区分不同的代理配置。 |
| [Rcp\_StatusCode](../../模块/RemoteCommunication/remote-communication-overview.md#rcp_statuscode) {  RCP\_NONE = 0, RCP\_OK = 200, RCP\_CREATED, RCP\_ACCEPTED,  RCP\_NOT\_AUTHORITATIVE, RCP\_NO\_CONTENT, RCP\_RESET, RCP\_PARTIAL,  RCP\_MULTI\_CHOICE = 300, RCP\_MOVED\_PERMANENTLY, RCP\_MOVED\_TEMPORARILY, RCP\_SEE\_OTHER,  RCP\_NOT\_MODIFIED, RCP\_USE\_PROXY, RCP\_BAD\_REQUEST = 400, RCP\_UNAUTHORIZED,  RCP\_PAYMENT\_REQUIRED, RCP\_FORBIDDEN, RCP\_NOT\_FOUND, RCP\_BAD\_METHOD,  RCP\_NOT\_ACCEPTABLE, RCP\_PROXY\_AUTH, RCP\_CLIENT\_TIMEOUT, RCP\_CONFLICT,  RCP\_GONE, RCP\_LENGTH\_REQUIRED, RCP\_PRECON\_FAILED, RCP\_ENTITY\_TOO\_LARGE,  RCP\_REQ\_TOO\_LONG, RCP\_UNSUPPORTED\_TYPE, RCP\_INTERNAL\_ERROR = 500, RCP\_NOT\_IMPLEMENTED,  RCP\_BAD\_GATEWAY, RCP\_UNAVAILABLE, RCP\_GATEWAY\_TIMEOUT, RCP\_VERSION  } | 请求响应的状态码。 |
| [Rcp\_DebugEvent](../../模块/RemoteCommunication/remote-communication-overview.md#rcp_debugevent) {  RCP\_DEBUG\_EVENT\_TEXT, RCP\_DEBUG\_EVENT\_HEADER\_IN, RCP\_DEBUG\_EVENT\_HEADER\_OUT, RCP\_DEBUG\_EVENT\_DATA\_IN,  RCP\_DEBUG\_EVENT\_DATA\_OUT, RCP\_DEBUG\_EVENT\_SSL\_DATA\_IN, RCP\_DEBUG\_EVENT\_SSL\_DATA\_OUT  } | 描述调试信息的事件类型。 |
| [Rcp\_SessionType](../../模块/RemoteCommunication/remote-communication-overview.md#rcp_sessiontype) { RCP\_SESSION\_TYPE\_HTTP = 0, RCP\_SESSION\_TYPE\_MAX = 100} | 会话类型。 |

### 函数

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| [Rcp\_Form](../../模块/RemoteCommunication/remote-communication-overview.md#rcp_form) \* [HMS\_Rcp\_CreateForm](../../模块/RemoteCommunication/remote-communication-overview.md#hms_rcp_createform) (void) | 创建一个简单表单。 |
| void [HMS\_Rcp\_DestroyForm](../../模块/RemoteCommunication/remote-communication-overview.md#hms_rcp_destroyform) ([Rcp\_Form](../../模块/RemoteCommunication/remote-communication-overview.md#rcp_form) \*form) | 销毁一个简单表单。 |
| uint32\_t [HMS\_Rcp\_SetFormValue](../../模块/RemoteCommunication/remote-communication-overview.md#hms_rcp_setformvalue) ([Rcp\_Form](../../模块/RemoteCommunication/remote-communication-overview.md#rcp_form) \*form, const char \*key, const [Rcp\_FormFieldValue](../../结构体/Rcp_FormFieldValue/_rcp___form_field_value.md) \*value) | 设置简单表单的键值对。 |
| [Rcp\_FormFieldValue](../../结构体/Rcp_FormFieldValue/_rcp___form_field_value.md) \* [HMS\_Rcp\_GetFormValue](../../模块/RemoteCommunication/remote-communication-overview.md#hms_rcp_getformvalue) ([Rcp\_Form](../../模块/RemoteCommunication/remote-communication-overview.md#rcp_form) \*form, const char \*key) | 通过键获取一个简单表单的对应值。 |
| [Rcp\_MultipartForm](../../模块/RemoteCommunication/remote-communication-overview.md#rcp_multipartform) \* [HMS\_Rcp\_CreateMultipartForm](../../模块/RemoteCommunication/remote-communication-overview.md#hms_rcp_createmultipartform) (void) | 创建一个多部分表单。 |
| void [HMS\_Rcp\_DestroyMultipartForm](../../模块/RemoteCommunication/remote-communication-overview.md#hms_rcp_destroymultipartform) ([Rcp\_MultipartForm](../../模块/RemoteCommunication/remote-communication-overview.md#rcp_multipartform) \*multipartForm) | 销毁一个多部分表单。 |
| uint32\_t [HMS\_Rcp\_SetMultipartFormValue](../../模块/RemoteCommunication/remote-communication-overview.md#hms_rcp_setmultipartformvalue) ([Rcp\_MultipartForm](../../模块/RemoteCommunication/remote-communication-overview.md#rcp_multipartform) \*multipartForm, const char \*key, const [Rcp\_MultipartFormFieldValue](../../结构体/Rcp_MultipartFormFieldValue/_rcp___multipart_form_field_value.md) \*value) | 设置多部分表单的键值对。 |
| [Rcp\_MultipartFormFieldValue](../../结构体/Rcp_MultipartFormFieldValue/_rcp___multipart_form_field_value.md) \* [HMS\_Rcp\_GetMultipartFormValue](../../模块/RemoteCommunication/remote-communication-overview.md#hms_rcp_getmultipartformvalue) ([Rcp\_MultipartForm](../../模块/RemoteCommunication/remote-communication-overview.md#rcp_multipartform) \*multipartForm, const char \*key) | 通过键获取多部分表单的值。 |
| [Rcp\_Headers](../../模块/RemoteCommunication/remote-communication-overview.md#rcp_headers) \* [HMS\_Rcp\_CreateHeaders](../../模块/RemoteCommunication/remote-communication-overview.md#hms_rcp_createheaders) (void) | 为请求或响应创建标头。 |
| void [HMS\_Rcp\_DestroyHeaders](../../模块/RemoteCommunication/remote-communication-overview.md#hms_rcp_destroyheaders) ([Rcp\_Headers](../../模块/RemoteCommunication/remote-communication-overview.md#rcp_headers) \*headers) | 销毁请求或响应的标头。 |
| uint32\_t [HMS\_Rcp\_SetHeaderValue](../../模块/RemoteCommunication/remote-communication-overview.md#hms_rcp_setheadervalue) ([Rcp\_Headers](../../模块/RemoteCommunication/remote-communication-overview.md#rcp_headers) \*headers, const char \*name, const char \*value) | 设置请求或响应头的键值对。 |
| [Rcp\_HeaderValue](../../结构体/Rcp_HeaderValue/_rcp___header_value.md) \* [HMS\_Rcp\_GetHeaderValue](../../模块/RemoteCommunication/remote-communication-overview.md#hms_rcp_getheadervalue) ([Rcp\_Headers](../../模块/RemoteCommunication/remote-communication-overview.md#rcp_headers) \*headers, const char \*name) | 通过键获取请求或响应头的值。 |
| [Rcp\_HeaderEntry](../../结构体/Rcp_HeaderEntry/_rcp___header_entry.md) \* [HMS\_Rcp\_GetHeaderEntries](../../模块/RemoteCommunication/remote-communication-overview.md#hms_rcp_getheaderentries) ([Rcp\_Headers](../../模块/RemoteCommunication/remote-communication-overview.md#rcp_headers) \*headers) | 获取请求或响应头的所有键值对。 |
| void [HMS\_Rcp\_DestroyHeaderEntries](../../模块/RemoteCommunication/remote-communication-overview.md#hms_rcp_destroyheaderentries) ([Rcp\_HeaderEntry](../../结构体/Rcp_HeaderEntry/_rcp___header_entry.md) \*headerEntry) | 销毁[HMS\_Rcp\_GetHeaderEntries](../../模块/RemoteCommunication/remote-communication-overview.md#hms_rcp_getheaderentries)中获取的所有键值对。 |
| [Rcp\_Request](../../结构体/Rcp_Request/_rcp___request.md) \* [HMS\_Rcp\_CreateRequest](../../模块/RemoteCommunication/remote-communication-overview.md#hms_rcp_createrequest) (const char \*url) | 创建请求。 |
| void [HMS\_Rcp\_DestroyRequest](../../模块/RemoteCommunication/remote-communication-overview.md#hms_rcp_destroyrequest) ([Rcp\_Request](../../结构体/Rcp_Request/_rcp___request.md) \*request) | 销毁请求。 |
| [Rcp\_RequestCookies](../../模块/RemoteCommunication/remote-communication-overview.md#rcp_requestcookies) \* [HMS\_Rcp\_CreateRequestCookies](../../模块/RemoteCommunication/remote-communication-overview.md#hms_rcp_createrequestcookies) (void) | 创建空的请求Cookie。 |
| void [HMS\_Rcp\_DestroyRequestCookies](../../模块/RemoteCommunication/remote-communication-overview.md#hms_rcp_destroyrequestcookies) ([Rcp\_RequestCookies](../../模块/RemoteCommunication/remote-communication-overview.md#rcp_requestcookies) \*cookies) | 销毁请求Cookie。 |
| uint32\_t [HMS\_Rcp\_SetRequestCookieValue](../../模块/RemoteCommunication/remote-communication-overview.md#hms_rcp_setrequestcookievalue) ([Rcp\_RequestCookies](../../模块/RemoteCommunication/remote-communication-overview.md#rcp_requestcookies) \*cookies, const char \*name, const char \*value) | 设置请求Cookie。 |
| char \* [HMS\_Rcp\_GetRequestCookieValue](../../模块/RemoteCommunication/remote-communication-overview.md#hms_rcp_getrequestcookievalue) ([Rcp\_RequestCookies](../../模块/RemoteCommunication/remote-communication-overview.md#rcp_requestcookies) \*cookies, const char \*name) | 通过名称获取请求Cookie的值。 |
| [Rcp\_RequestCookieEntry](../../结构体/Rcp_RequestCookieEntry/_rcp___request_cookie_entry.md) \* [HMS\_Rcp\_GetRequestCookieEntries](../../模块/RemoteCommunication/remote-communication-overview.md#hms_rcp_getrequestcookieentries) ([Rcp\_RequestCookies](../../模块/RemoteCommunication/remote-communication-overview.md#rcp_requestcookies) \*cookies) | 获取请求Cookie中的所有键值对。 |
| void [HMS\_Rcp\_DestroyRequestCookieEntries](../../模块/RemoteCommunication/remote-communication-overview.md#hms_rcp_destroyrequestcookieentries) ([Rcp\_RequestCookieEntry](../../结构体/Rcp_RequestCookieEntry/_rcp___request_cookie_entry.md) \*cookieEntry) | 销毁从[HMS\_Rcp\_GetRequestCookieValue](../../模块/RemoteCommunication/remote-communication-overview.md#hms_rcp_getrequestcookievalue)获取的所有与请求Cookie相关的键值对。 |
| const char \* [HMS\_Rcp\_GetResponseCookieAttrValue](../../模块/RemoteCommunication/remote-communication-overview.md#hms_rcp_getresponsecookieattrvalue) ([Rcp\_CookieAttributes](../../模块/RemoteCommunication/remote-communication-overview.md#rcp_cookieattributes) \*cookieAttributes, const char \*name) | 通过名称获取Cookie属性的值。 |
| [Rcp\_CookieAttributeEntry](../../结构体/Rcp_CookieAttributeEntry/_rcp___cookie_attribute_entry.md) \* [HMS\_Rcp\_GetResponseCookieAttrEntries](../../模块/RemoteCommunication/remote-communication-overview.md#hms_rcp_getresponsecookieattrentries) ([Rcp\_CookieAttributes](../../模块/RemoteCommunication/remote-communication-overview.md#rcp_cookieattributes) \*cookieAttributes) | 在[Rcp\_CookieAttributes](../../模块/RemoteCommunication/remote-communication-overview.md#rcp_cookieattributes)中获取所有响应Cookie属性。 |
| void [HMS\_Rcp\_DestroyResponseCookieAttrEntries](../../模块/RemoteCommunication/remote-communication-overview.md#hms_rcp_destroyresponsecookieattrentries) ([Rcp\_CookieAttributeEntry](../../结构体/Rcp_CookieAttributeEntry/_rcp___cookie_attribute_entry.md) \*entries) | 销毁响应Cookie属性。 |
| uint32\_t [HMS\_Rcp\_CallNextRequestHandler](../../模块/RemoteCommunication/remote-communication-overview.md#hms_rcp_callnextrequesthandler) ([Rcp\_Request](../../结构体/Rcp_Request/_rcp___request.md) \*request, const [Rcp\_RequestHandler](../../模块/RemoteCommunication/remote-communication-overview.md#rcp_requesthandler) \*next, const [Rcp\_ResponseCallbackObject](../../结构体/Rcp_ResponseCallbackObject/_rcp___response_callback_object.md) \*responseCallback) | 在拦截器[Rcp\_Interceptor](../../结构体/Rcp_Interceptor/_rcp___interceptor.md)的函数中可以调用下一个拦截器或defaultHandler。 |
| [Rcp\_Response](../../结构体/Rcp_Response/_rcp___response.md) \* [HMS\_Rcp\_CallNextSyncRequestHandler](../../模块/RemoteCommunication/remote-communication-overview.md#hms_rcp_callnextsyncrequesthandler) ([Rcp\_Request](../../结构体/Rcp_Request/_rcp___request.md) \*request, const [Rcp\_SyncRequestHandler](../../模块/RemoteCommunication/remote-communication-overview.md#rcp_syncrequesthandler) \*next, uint32\_t \*errCode) | 在拦截器[Rcp\_SyncInterceptor](../../结构体/Rcp_SyncInterceptor/_rcp___sync_interceptor.md)的函数中可以调用下一个拦截器或默认处理器。 |
| [Rcp\_Session](../../模块/RemoteCommunication/remote-communication-overview.md#rcp_session) \* [HMS\_Rcp\_CreateSession](../../模块/RemoteCommunication/remote-communication-overview.md#hms_rcp_createsession) (const [Rcp\_SessionConfiguration](../../结构体/Rcp_SessionConfiguration/_rcp___session_configuration.md) \*configuration, uint32\_t \*errCode) | 创建会话。 |
| const char \* [HMS\_Rcp\_GetSessionId](../../模块/RemoteCommunication/remote-communication-overview.md#hms_rcp_getsessionid) ([Rcp\_Session](../../模块/RemoteCommunication/remote-communication-overview.md#rcp_session) \*session) | 获取会话ID。 |
| const [Rcp\_SessionConfiguration](../../结构体/Rcp_SessionConfiguration/_rcp___session_configuration.md) \* [HMS\_Rcp\_GetSessionConfiguration](../../模块/RemoteCommunication/remote-communication-overview.md#hms_rcp_getsessionconfiguration) ([Rcp\_Session](../../模块/RemoteCommunication/remote-communication-overview.md#rcp_session) \*session) | 获取会话配置。 |
| [Rcp\_Response](../../结构体/Rcp_Response/_rcp___response.md) \* [HMS\_Rcp\_FetchSync](../../模块/RemoteCommunication/remote-communication-overview.md#hms_rcp_fetchsync) ([Rcp\_Session](../../模块/RemoteCommunication/remote-communication-overview.md#rcp_session) \*session, [Rcp\_Request](../../结构体/Rcp_Request/_rcp___request.md) \*request, uint32\_t \*errCode) | 发送同步请求并获取响应。 |
| uint32\_t [HMS\_Rcp\_Fetch](../../模块/RemoteCommunication/remote-communication-overview.md#hms_rcp_fetch) ([Rcp\_Session](../../模块/RemoteCommunication/remote-communication-overview.md#rcp_session) \*session, [Rcp\_Request](../../结构体/Rcp_Request/_rcp___request.md) \*request, const [Rcp\_ResponseCallbackObject](../../结构体/Rcp_ResponseCallbackObject/_rcp___response_callback_object.md) \*responseCallback) | 发送异步请求并获取响应。 |
| uint32\_t [HMS\_Rcp\_CancelRequest](../../模块/RemoteCommunication/remote-communication-overview.md#hms_rcp_cancelrequest) ([Rcp\_Session](../../模块/RemoteCommunication/remote-communication-overview.md#rcp_session) \*session, const [Rcp\_Request](../../结构体/Rcp_Request/_rcp___request.md) \*request) | 取消一个请求。 |
| uint32\_t [HMS\_Rcp\_CancelSession](../../模块/RemoteCommunication/remote-communication-overview.md#hms_rcp_cancelsession) ([Rcp\_Session](../../模块/RemoteCommunication/remote-communication-overview.md#rcp_session) \*session) | 取消会话。 |
| uint32\_t [HMS\_Rcp\_CloseSession](../../模块/RemoteCommunication/remote-communication-overview.md#hms_rcp_closesession) ([Rcp\_Session](../../模块/RemoteCommunication/remote-communication-overview.md#rcp_session) \*\*session) | 关闭会话。 |
| uint32\_t [HMS\_Rcp\_SetRequestOnBinaryDataRecvCallback](../../模块/RemoteCommunication/remote-communication-overview.md#hms_rcp_setrequestonbinarydatarecvcallback) ([Rcp\_Request](../../结构体/Rcp_Request/_rcp___request.md) \*request, [Rcp\_OnBinaryReceiveCallback](../../结构体/Rcp_OnBinaryReceiveCallback/_rcp___on_binary_receive_callback.md) onBinaryReceiveCallback) | 为请求设置流式接收二进制数据的回调函数。该回调函数与[Rcp\_OnDataReceiveCallback](../../结构体/Rcp_OnDataReceiveCallback/_rcp___on_data_receive_callback.md)功能一致，功能上可以包含字符数据和二进制数据。 |
| uint32\_t [HMS\_Rcp\_GetDefaultSession](../../模块/RemoteCommunication/remote-communication-overview.md#hms_rcp_getdefaultsession) ([Rcp\_Session](../../模块/RemoteCommunication/remote-communication-overview.md#rcp_session) \*\*session) | 获取默认会话。 |
| uint32\_t [HMS\_Rcp\_SetRequestConnectOnly](../../模块/RemoteCommunication/remote-communication-overview.md#hms_rcp_setrequestconnectonly) ([Rcp\_Request](../../结构体/Rcp_Request/_rcp___request.md) \*request, bool connectOnly) | 设置请求仅用于建立连接，而不进行数据传输。 |
