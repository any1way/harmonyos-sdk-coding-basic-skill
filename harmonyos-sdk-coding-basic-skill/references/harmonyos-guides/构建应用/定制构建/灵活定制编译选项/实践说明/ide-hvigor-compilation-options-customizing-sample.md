---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hvigor-compilation-options-customizing-sample
title: 实践说明
breadcrumb: 指南 > 构建应用 > 定制构建 > 灵活定制编译选项 > 实践说明
category: harmonyos-guides
scraped_at: 2026-06-11T15:30:40+08:00
doc_updated_at: 2026-04-30
content_hash: sha256:9325bf62c7727b473693dcb5fe4d87ba2493e6e2063c0742e89f82ae94b5777a
---

应用正式对外发布版本前，需要对应用进行代码调试。调试和正式发布版本，两者编译行为可能不同。此时，可以利用buildMode能力，来定制两个版本的编译差异性。

假设其中构建产物均为default，但编译行为不同：release模式下使能混淆，debug模式下使能debug调试。

示例工程中包含一个模块entry，将entry模块交付到构建产物default中，模块定制两种不同的编译模式debug、release，将两种构建模式均绑定到构建产物default中。工程示例图如下（模块）：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c5/v3/uZ3bvkhCR_iauCMH5TJtgQ/zh-cn_image_0000002571546442.png?HW-CC-KV=V1&HW-CC-Date=20260611T073039Z&HW-CC-Expire=86400&HW-CC-Sign=D0EAD9DA21940DCF5344C5A264A2E7F0206B18521B92B6394B20FF3BF2304781)

## 工程级build-profile.json5示例

```
1. {
2. "app": {
3. "signingConfigs": [],
4. "products": [
5. {
6. "name": "default",
7. "signingConfig": "default",
8. "compatibleSdkVersion": "6.1.1(24)",
9. "runtimeOS": "HarmonyOS",
10. "buildOption": {
11. "strictMode": {
12. "caseSensitiveCheck": true,
13. "useNormalizedOHMUrl": true
14. }
15. }
16. }
17. ],
18. "buildModeSet": [
19. {
20. "name": "debug"
21. },
22. {
23. "name": "release"
24. }
25. ]
26. },
27. "modules": [
28. {
29. "name": "entry",
30. "srcPath": "./entry",
31. "targets": [
32. {
33. "name": "default",
34. "applyToProducts": [
35. "default"
36. ]
37. }
38. ]
39. }
40. ]
41. }
```

## 模块级build-profile.json5示例

### entry模块

```
1. {
2. "apiType": "stageMode",
3. "buildOption": {
4. },
5. "buildOptionSet": [
6. {
7. "name": "release",
8. "arkOptions": {
9. "obfuscation": {
10. "ruleOptions": {
11. "enable": true,
12. "files": [
13. "./obfuscation-rules.txt"
14. ]
15. }
16. }
17. }
18. },
19. {
20. "name": "debug",
21. "debuggable": true,
22. "arkOptions": {
23. "obfuscation": {
24. "ruleOptions": {
25. "enable": false
26. }
27. }
28. }
29. }
30. ],
31. "buildModeBinder": [
32. {
33. "buildModeName": "release",
34. "mappings": [
35. {
36. "buildOptionName": "release",
37. "targetName": "default"
38. }
39. ]
40. },
41. {
42. "buildModeName": "debug",
43. "mappings": [
44. {
45. "buildOptionName": "debug",
46. "targetName": "default"
47. }
48. ]
49. }
50. ],
51. "targets": [
52. {
53. "name": "default",
54. },
55. {
56. "name": "ohosTest",
57. }
58. ]
59. }
```

## 指定构建模式

### 命令行

示例1：构建APP时，构建产物为default，指定构建模式为debug，可执行如下命令：

```
1. hvigorw --mode project -p product=default -p buildMode=debug assembleApp
```

编译产物示例如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e0/v3/tbC3yz-YR-aKPEB8wOs2Iw/zh-cn_image_0000002602185973.png?HW-CC-KV=V1&HW-CC-Date=20260611T073039Z&HW-CC-Expire=86400&HW-CC-Sign=C3161FA30B7C7F5A98D801AF3C4E9EBFB346979784FD66DE37717597BBF228AD)

示例2：构建APP时，构建产物为default，指定构建模式为release，可执行如下命令：

```
1. hvigorw --mode project -p product=default -p buildMode=release assembleApp
```

编译产物示例如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/83/v3/NtkvpUqgQMOknQ3ITNwxLw/zh-cn_image_0000002571546444.png?HW-CC-KV=V1&HW-CC-Date=20260611T073039Z&HW-CC-Expire=86400&HW-CC-Sign=63C4B4091EA1C97E73DE55E718F6E073E9C883F82390BDF47B38D1D0AA5E609E)

### DevEco Studio界面

在DevEco Studio界面进行可视化配置，Build Mode下拉选择对应配置选项debug后，点击Build -> Build Hap(s)/APP(s) -> Build APP(s) ，构建编译模式为debug，构建产物为default的APP包。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/59/v3/43hd7jGYSiymXWrgil47Bw/zh-cn_image_0000002602065923.png?HW-CC-KV=V1&HW-CC-Date=20260611T073039Z&HW-CC-Expire=86400&HW-CC-Sign=73AB3C93E7F3B331FA4689F9F30C4B9064C3B174FE6C7273EE9E79F7A4A89AE0)
