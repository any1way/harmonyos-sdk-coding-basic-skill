---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/c-api-compatibility-warning-elim
title: C API兼容性保护
breadcrumb: 版本说明 > 应用兼容性说明 > 应用开发中的兼容性场景开发指导 > API兼容性保护和告警屏蔽 > C API兼容性保护
category: harmonyos-releases
scraped_at: 2026-06-01T10:55:49+08:00
doc_updated_at: 2026-04-30
content_hash: sha256:cee9e62e36382db8a20697d5290ec00bcc09cf645acd2fa6fc35239d8b5ab5ef
---

## 通过dlopen加载动态库，调用dlsym接口查询的方式，判断API兼容性

示例如下：

```
1. void *handle = NULL; // 库的句柄
2. Location_ResultCode (*OH_Location_StartLocating_Test)(const Location_RequestConfig *); // 函数指针
3. OH_Location_StartLocating_Test = NULL;
4. handle = dlopen("liblocation_ndk.so", RTLD_LAZY);
5. if (handle != NULL) {
6. OH_Location_StartLocating_Test =
7. (Location_ResultCode(*)(const Location_RequestConfig *))dlsym(handle, "OH_Location_StartLocating");
8. if (OH_Location_StartLocating_Test != NULL) {
9. OH_LOG_INFO(LOG_APP, "OH_Location_StartLocating != NULL");
10. } else {
11. OH_LOG_INFO(LOG_APP, "OH_Location_StartLocating = NULL");
12. }
13. } else {
14. OH_LOG_INFO(LOG_APP, "handle = NULL");
15. }
```
