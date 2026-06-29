---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-previewer-operating-3
title: 预览告警“@Consume/@Link decorated property <propertyName> not initialized”
breadcrumb: FAQ > DevEco Studio > 界面预览 > 预览告警“@Consume/@Link decorated property <propertyName> not initialized”
category: harmonyos-faqs
scraped_at: 2026-06-12T10:40:53+08:00
doc_updated_at: 2026-03-17
content_hash: sha256:4417508fdf718f906fcac08630dbdf84a4aa7c625f1dcce347904f7766e429d8
---

**问题现象**

启动预览后，预览窗口显示白屏，上方出现错误信息：“Preview failed. View details in the PreviewerLog window.”

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6c/v3/FkCy2mMcRECAH1sGVQPwgw/zh-cn_image_0000002194317968.png?HW-CC-KV=V1&HW-CC-Date=20260612T024052Z&HW-CC-Expire=86400&HW-CC-Sign=A5F48A704C53E0F97EFF1AC7019EFF24A8190200CDC2578FFD415856FA05E6E5 "点击放大")

此时，PreviewerLog 窗口显示如下告警信息：“@Consume/@Link 装饰的属性 \_<propertyName>\_未初始化。”

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/61/v3/HSoRdUlGQ7CAmQNGbVNdkg/zh-cn_image_0000002194158348.png?HW-CC-KV=V1&HW-CC-Date=20260612T024052Z&HW-CC-Expire=86400&HW-CC-Sign=8F5550F808EFE08209D2CD2DF2C450703B3FBCDB4E6DE4939F2EA76230F45E9E)

**解决措施**

由于@Consume/@Link装饰的成员需要与父组件建立绑定关系，单独预览时无法完成初始化，因此如果预览包含@Consume（或@Link）装饰的成员的页面或组件，就可能会出现空白屏幕。

建议不要直接预览含有@Consume或@Link装饰的子组件，而应通过预览父组件来查看子组件的预览效果。

示例代码：

```
1. // Suggest adding @ Preview on ParentComp to preview the preview effect of ChildComp
2. @Preview
3. @Component
4. struct ParentComp {
5. // @Provide decoration is provided by the entrance component ParentComp as its descendant component
6. @Provide reviewVotes: number = 10;

8. build() {
9. Column() {
10. Button(`reviewVotes(${this.reviewVotes}), give +1`)
11. .onClick(() => this.reviewVotes += 1)
12. ChildComp()
13. }
14. }
15. }

17. // @Preview is not recommended to directly preview ChildComp
18. @Component
19. struct ChildComp {
20. // The variable decorated with '@Consume' is bound to the variable decorated with '@Provide' in its ancestor component ParentComp using the same attribute name
21. @Consume reviewVotes: number;
22. build() {
23. Column() {
24. Text(`reviewVotes(${this.reviewVotes})`)
25. Button(`reviewVotes(${this.reviewVotes}), give +1`)
26. .onClick(() => this.reviewVotes += 1)
27. }
28. .width('50%')
29. }
30. }
```

[PreviewFailed.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/PreviewerOperating/entry/src/main/ets/pages/PreviewFailed.ets#L3-L32)
