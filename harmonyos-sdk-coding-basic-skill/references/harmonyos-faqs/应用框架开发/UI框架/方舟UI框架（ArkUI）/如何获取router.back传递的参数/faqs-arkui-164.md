---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-164
title: 如何获取router.back传递的参数
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > 如何获取router.back传递的参数
category: harmonyos-faqs
scraped_at: 2026-06-12T10:28:25+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:d54612d8432c4a5ec667667d144021330815edea48ee428951f6f94c6b3a6b36
---
在 onPageShow 回调方法中使用 Router模块的getParams方法来获取传递过来的参数。参考代码如下：

```
1. class InfoTmp {
2. age: number = 0
3. }

5. class RouTmp {
6. id: object = () => {
7. }
8. info: InfoTmp = new InfoTmp()
9. }

11. const context = AppStorage.get("context") as UIContext;
12. const params: RouTmp = context.getRouter().getParams() as RouTmp; // Get the parameter object passed
13. const id: object = params.id // Get the value of the id property
14. const age: number = params.info.age // Get the value of the age property
```

[GetRouterBackParam.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/GetRouterBackParam.ets#L21-L34)

**参考链接**

[页面跳转](<../../../../../harmonyos-guides/应用框架/ArkUI（方舟UI框架）/UI开发 (ArkTS声明式开发范式)/设置组件导航和页面路由/页面路由 (@ohos.router)(不推荐)/arkts-routing.md#页面跳转>)
