---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-11
title: 编译报错“Property xxx does not exist on type 'typeof BuildProfile'.”
breadcrumb: FAQ > DevEco Studio > 编译构建 > 编译报错“Property xxx does not exist on type 'typeof BuildProfile'.”
category: harmonyos-faqs
scraped_at: 2026-06-12T10:41:07+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:ef118e4161e21b01dceb909e1e78b1aeee94d40c73645de4ccb9172d9050cdae
---

**问题现象****1**

使用自定义参数BuildProfile时，编译过程中未出现异常，但编译构建失败，提示“Property xxx does not exist on type 'typeof BuildProfile'”。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bd/v3/YJRwFhyFTAG9RKTSDfjomg/zh-cn_image_0000002229604165.png?HW-CC-KV=V1&HW-CC-Date=20260612T024105Z&HW-CC-Expire=86400&HW-CC-Sign=23FE1D42AF5EEACA16889DA9E6A73EED2527EBBB2DC5F08B647DEF5143822EB8)

**解决措施**

检查当前模块下build-profile.json5文件中targets>buildProfileFields配置的自定义参数的key值是否一致。如果不一致，请将targets内所有buildProfileFields的key值统一。

以下为导致编译报错的配置示例：

```
1. "targets": [
2. {
3. "name": "default",
4. "config": {
5. "buildOption": {
6. "arkOptions": {
7. "buildProfileFields": {
8. "targetName": "default"
9. }
10. }
11. }
12. }
13. },
14. {
15. "name": "default1",
16. "config": {
17. "buildOption": {
18. "arkOptions": {
19. "buildProfileFields": {
20. "targetName1": "default1"
21. }
22. }
23. }
24. }
25. }
26. ]
```

将targets内所有buildProfileFields的key值修改为一致，例如都修改为targetName。

**问题现象2**

使用了自定义参数BuildProfile并且编译器标红且构建失败，提示“Property xxx does not exist on type 'typeof BuildProfile'.”。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/95/v3/ZH3FHkyOSNWT3f0POKmn4g/zh-cn_image_0000002194318396.png?HW-CC-KV=V1&HW-CC-Date=20260612T024105Z&HW-CC-Expire=86400&HW-CC-Sign=9DED3E11E705131682066C77B2901250737C00F7A23A7BB2840F0BDB4E880809)

**解决措施**

检查当前模块下的 build-profile.json5文件，确保buildProfileFields中已添加所使用的自定义参数。
