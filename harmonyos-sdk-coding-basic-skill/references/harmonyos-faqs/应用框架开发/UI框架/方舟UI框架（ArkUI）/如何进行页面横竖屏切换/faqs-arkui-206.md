---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-206
title: 如何进行页面横竖屏切换
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > 如何进行页面横竖屏切换
category: harmonyos-faqs
scraped_at: 2026-06-12T10:29:08+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:fa757ae5149cd1a4531212dd5c0992c6461731835596a03e2cf3e2634626ebf0
---
设置方法：setPreferredOrientation(orientation: Orientation, callback: AsyncCallback<void>): void。Orientation取值为AUTO\_ROTATION，表示传感器自动旋转模式。参考代码如下：

```
1. let orientation = window.Orientation.AUTO_ROTATION;
2. try{
3. windowClass.setPreferredOrientation(orientation, (err) => {
4. if(err.code){
5. console.error('Failed to set window orientation. Cause: ' + JSON.stringify(err));
6. return;
7. }
8. console.info('Succeeded in setting window orientation.');
9. });
10. }catch (exception) {
11. console.error('Failed to set window orientation. Cause: ' + JSON.stringify(exception));
12. }
```

[EntryAbilityHorizontalAndVertical.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/entryability/EntryAbilityHorizontalAndVertical.ets#L40-L51)

**参考链接**

[setPreferredOrientation](<../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS API/窗口管理/@ohos.window (窗口)/Interface (Window)/arkts-apis-window-window.md#setpreferredorientation9>)
