---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/multi-window-intro
title: 智慧多窗简介
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > 窗口管理 > 智慧多窗应用开发指南 > 智慧多窗简介
category: harmonyos-guides
scraped_at: 2026-06-11T14:34:42+08:00
doc_updated_at: 2026-04-29
content_hash: sha256:a0b3d30c02e27c337dab1e5b7cd47e5749e21487e8c5908d15e8d042e0543a09
---
智慧多窗是一种多任务处理解决方案，它允许用户在同一时间、同一屏幕上以悬浮窗、分屏或全景多窗的方式同时运行多个应用窗口。在智慧多窗的显示模式下，用户可以根据自己的需求，合理安排应用窗口的位置和大小。

## 悬浮窗

悬浮窗是一种在设备屏幕上悬浮的非全屏应用窗口。一般用于在已有全屏任务运行的基础上，临时处理另一个任务，或短时间多任务并行使用。如浏览网页的同时回复消息。

针对手机，一个屏幕内最多支持显示一个悬浮窗；在折叠屏手机展开态、平板类设备上，一个屏幕内最多支持显示两个悬浮窗。在超出悬浮窗显示最大个数限制时，打开新的悬浮窗会替换最近久未操作的悬浮窗。

### 悬浮窗的类型

**悬浮窗的常见类型主要分为如下两种：**

* 竖向悬浮窗：一般用于新闻资讯、社交以及购物类应用等场景。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/64/v3/m1Wp8xyuSBeJ_8jS-t7xJw/zh-cn_image_0000002622698153.png?HW-CC-KV=V1&HW-CC-Date=20260611T063440Z&HW-CC-Expire=86400&HW-CC-Sign=A9530747CD5F3D7C223C51B37180518B0EFF2C4E8F2AC262B401293D39C46CD7)
* 横向悬浮窗：主要用于横向游戏和视频全屏播放的场景。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1b/v3/9OIjsLzYQcetcAMiJPzwCQ/zh-cn_image_0000002592218592.jpg?HW-CC-KV=V1&HW-CC-Date=20260611T063440Z&HW-CC-Expire=86400&HW-CC-Sign=23E143D4250EFDE7B2C771B60B69A820F1199018410E692049553D03C104B1A9)

### 悬浮窗的触发及恢复方式

**悬浮窗的触发方式有以下几种：**

* 手势触发：应用全屏时从屏幕底部向上滑至右上方热区，松手后可开启悬浮窗模式。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8b/v3/5tc6O8MbRMCRILUNvxpwUA/zh-cn_image_0000002592378526.jpg?HW-CC-KV=V1&HW-CC-Date=20260611T063440Z&HW-CC-Expire=86400&HW-CC-Sign=37DF3C43C4527A1AB1CE8ABBCFD83D78A5E82F3D5A0355BAA115A2F7C304B5AA)
* 通知消息下拉触发：在系统接收到通知消息未收起时，可直接下拉此通知消息开启悬浮窗模式。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/92/v3/1ELnzdqvSR6vmZt31lZ0fw/zh-cn_image_0000002622858033.png?HW-CC-KV=V1&HW-CC-Date=20260611T063440Z&HW-CC-Expire=86400&HW-CC-Sign=2AA7224A31C13A0AEDF37A683860D3D46C5A449774632D44E327DF5597EC363A)
* 侧边Dock触发：侧滑调出侧边Dock栏，点击Dock上的应用，支持悬浮窗的应用以悬浮窗模式开启。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/73/v3/cpXNvUFhTde8f14Cd3ngmw/zh-cn_image_0000002622698155.png?HW-CC-KV=V1&HW-CC-Date=20260611T063440Z&HW-CC-Expire=86400&HW-CC-Sign=34959754DA0D14D9AB10C8159E85541E0704248BAAACAB32068A520E2DD524D4)
* 分屏切换悬浮窗：分屏时，按住分屏应用顶部横条，拖拽到相应的热区，应用从分屏切换到悬浮窗模式。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/48/v3/rmw8yIiLSNiYajmV37keSQ/zh-cn_image_0000002592218594.png?HW-CC-KV=V1&HW-CC-Date=20260611T063440Z&HW-CC-Expire=86400&HW-CC-Sign=F515EB981027ECB9E9C535ACB595F18D3935C2FFC0324393F29A2C633EB9D57A)

**悬浮窗的恢复方式主要有以下两种：**

* 多任务中心中恢复：对于已开启悬浮窗模式的应用，在进入多任务中心时，悬浮窗应用同全屏应用一起显示在多任务中心，用户选择点击悬浮窗应用卡片时可恢复悬浮窗模式。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b4/v3/ylzrW39cQbuzhKF0Bl8LoQ/zh-cn_image_0000002592378528.png?HW-CC-KV=V1&HW-CC-Date=20260611T063440Z&HW-CC-Expire=86400&HW-CC-Sign=4AE53910FBF69B14AC4DB04B57FA90406C17A1C56FE8A84F1FFC1940D29A7F39)
* 侧边条恢复：对于已开启悬浮窗模式的应用，其最小化后会暂存在屏幕上的侧边条中，点击或者长按侧边条可展开任务选择界面，选择点击侧边条中悬浮窗应用卡片时可恢复悬浮窗模式。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/22/v3/49Ac0nmgSuWLLjd-NttA5g/zh-cn_image_0000002622858035.png?HW-CC-KV=V1&HW-CC-Date=20260611T063440Z&HW-CC-Expire=86400&HW-CC-Sign=DA0278C93ABA5C441D7CD4BA9C895D6C9D59AF002B2E09D1365E21690259FF31)

### 适配注意事项

* 针对在Tablet设备上运行的PC应用，不支持悬浮窗。

  当应用module.json5配置文件中的设备类型[deviceTypes标签](../../../../../基础入门/开发基础知识/应用配置文件（Stage模型）/module.json5配置文件/module-configuration-file.md#devicetypes标签)包含"2in1"且不包含"phone"时，系统判定其为PC应用。
* 在智慧多窗的显示模式下，窗口尺寸由系统决定，不受[WindowLimits](<../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS API/窗口管理/@ohos.window (窗口)/Interfaces (其他)/arkts-apis-window-i.md#windowlimits11>)约束。

## 分屏

分屏一般用于两个应用长时间并行使用的场景。例如：边看购物攻略边浏览商品；边看视频边玩游戏；看学习类视频的同时做笔记等。

### 分屏的触发方式

* 分屏通过手势触发：应用全屏时，从屏幕底部向上滑至左上方热区，进入待分屏状态，点击桌面另一个支持分屏的应用图标或卡片，可形成分屏。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5e/v3/w-0k1P3bRuej1eRF7PsT2g/zh-cn_image_0000002622698157.png?HW-CC-KV=V1&HW-CC-Date=20260611T063440Z&HW-CC-Expire=86400&HW-CC-Sign=E011149DF1BAF63EEDBDEAACF320715ED0A339C94C3C1B9F8C3C12B23AA4D0E2)
* 应用自主启动分屏：除了通过手势触发分屏之外，应用可以自主选择启动分屏，具体步骤可见[应用内分屏](../应用适配智慧多窗/应用声明支持智慧多窗/multi-window-support.md#应用内分屏)。
* 侧边Dock栏触发：长按Dock栏中的应用图标并拖出，和前台支持分屏的全屏应用形成分屏。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6a/v3/suGKrH6lRhq3FvQVu-pcWw/zh-cn_image_0000002592218596.png?HW-CC-KV=V1&HW-CC-Date=20260611T063440Z&HW-CC-Expire=86400&HW-CC-Sign=59AE6E6FDFAF32B36EE411140EF68C26B0DB76AD26EE836E934E3ADE345C5234)
* 悬浮窗切分屏：按住悬浮窗顶部横条，拖到相应热区，悬浮窗和前台全屏应用形成分屏。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b1/v3/_IbwgUe7QAa5AyQYamKrfA/zh-cn_image_0000002592378530.png?HW-CC-KV=V1&HW-CC-Date=20260611T063440Z&HW-CC-Expire=86400&HW-CC-Sign=305B5E815FE0EFE03949461EBB333361AC2BBE6CF7975997BCD5CA3471BDFFFB)

### 适配注意事项

* 在智慧多窗的显示模式下，窗口尺寸由系统决定，不受[WindowLimits](<../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS API/窗口管理/@ohos.window (窗口)/Interfaces (其他)/arkts-apis-window-i.md#windowlimits11>)约束。

## 全景多窗

从HarmonyOS 5.0.1开始，折叠机、部分Tablet设备支持全景多窗。

全景多窗旨在帮助用户在折叠机设备展开态时高效处理多个任务。通过全景多窗，用户可以突破物理屏幕的围墙，实现在同一屏幕上同时运行多个应用，并在这些应用之间快速切换。

全景多窗在折叠机设备上最多可支持三个窗口同时运行（部分Tablet设备最多可支持四个窗口）。

### 全景多窗的样式

目前全景多窗在双折叠设备上支持小窗口与大窗口两个档位显示，在三折叠与Tablet设备上支持小窗口、中窗口、大窗口三个档位显示，且窗口的档位与位置支持调节。

* 双折叠设备全景多窗窗口档位及窗口宽高比：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a1/v3/yQxtfdbcRsK0BeNVCjCg5g/zh-cn_image_0000002622858037.jpg?HW-CC-KV=V1&HW-CC-Date=20260611T063440Z&HW-CC-Expire=86400&HW-CC-Sign=886A710A1DC08652B5744A43B93ACEA2617933E853BA3C0BE988394152D03ABE)
* 三折叠与Tablet设备全景多窗窗口档位及窗口宽高比：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d5/v3/I6G8XedgQQmCGZ1vMImn5Q/zh-cn_image_0000002622698159.jpg?HW-CC-KV=V1&HW-CC-Date=20260611T063440Z&HW-CC-Expire=86400&HW-CC-Sign=2A637E2329D3D0369DD67D94CED0A6E15A93D970DBC46B3F69ABFB57EC895068)
* 窗口状态分为平铺和侧身两种状态：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f3/v3/yDZ8PpUFQkyUhaC6Faiu1A/zh-cn_image_0000002592218598.png?HW-CC-KV=V1&HW-CC-Date=20260611T063440Z&HW-CC-Expire=86400&HW-CC-Sign=6294C1F419836A85EA3DC3185C50175C955E2D22D970430D5B6116293CBF34AA)

### 全景多窗的进入方式

* 全景多窗通过手势触发：

  应用全屏时，从屏幕底部向上滑至上方中间热区，点击桌面另一个支持全景多窗的应用图标或卡片，可形成全景多窗。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fe/v3/dKZnJaaNRHK3vWQM0c918Q/zh-cn_image_0000002592378532.png?HW-CC-KV=V1&HW-CC-Date=20260611T063440Z&HW-CC-Expire=86400&HW-CC-Sign=F7122A4039A00E2F8E084457808EF4187686B0911CA722D29CA317B4D1341B20)

  应用分屏时，从屏幕底部向上滑至上方中间热区，点击桌面另一个支持全景多窗的应用图标或卡片，可形成全景多窗。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0f/v3/1yO62ZAaTT-rCCpT4YhlKQ/zh-cn_image_0000002622858039.png?HW-CC-KV=V1&HW-CC-Date=20260611T063440Z&HW-CC-Expire=86400&HW-CC-Sign=D8515DA3E162AEE36BABECDB0EE5FC27EC4B24ECAF4CC58FA939814C5A061090)

  应用分屏时，从屏幕底部向上滑至左上方热区，点击桌面另一个支持全景多窗的应用图标或卡片，可形成三小窗全景多窗。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a2/v3/lMANzvOiQFqgOxTLJ9qaNA/zh-cn_image_0000002622698161.png?HW-CC-KV=V1&HW-CC-Date=20260611T063440Z&HW-CC-Expire=86400&HW-CC-Sign=5B673BFCD3CAF2081AF539A247BBFAC57B809CB02C6C727889AB9AE4687C000A)
* 全景多窗通过顶部横条触发：

  应用全屏时，点击全屏应用顶部横条，选择“全景多窗”，点击桌面另一个支持全景多窗的应用图标或卡片，可形成全景多窗。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a6/v3/YyXq9C5nRc2LrL8d-k2-aA/zh-cn_image_0000002592218600.png?HW-CC-KV=V1&HW-CC-Date=20260611T063440Z&HW-CC-Expire=86400&HW-CC-Sign=94EB74C3106DE547FA1588BEE78B173DE6E8EBE6B79F4DEF8F7280AF3062877A)

  应用分屏时，点击分屏应用顶部横条，选择“增加窗口”，点击桌面另一个支持全景多窗的应用图标或卡片，可形成全景多窗。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/40/v3/evTt9nNVRV61WAHWE9ENDA/zh-cn_image_0000002592378534.png?HW-CC-KV=V1&HW-CC-Date=20260611T063440Z&HW-CC-Expire=86400&HW-CC-Sign=D1D62095D33C7808A52376DF501143E942BD7B64364A7A0FEDD81A6CDEA51366)
* 全景多窗通过分屏拖拽触发：应用分屏时，调节分屏比例到相应热区，进入全景多窗。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d1/v3/_HrE0yD0T3CLjWE1nLJRNg/zh-cn_image_0000002622858041.png?HW-CC-KV=V1&HW-CC-Date=20260611T063440Z&HW-CC-Expire=86400&HW-CC-Sign=B01D576F4F7910FF59F781FA20EF2F1FF32EC765FC5F37EB9F0E26C596CE9178)

### 适配注意事项

* 全景多窗侧身窗口为不可见窗口，可以通过监听[on('windowVisibilityChange')](<../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS API/窗口管理/@ohos.window (窗口)/Interface (Window)/arkts-apis-window-window.md#onwindowvisibilitychange11>)感知应用是否处于侧身。
* 在智慧多窗的显示模式下，窗口尺寸由系统决定，不受[WindowLimits](<../../../../../../harmonyos-references/ArkUI（方舟UI框架）/ArkTS API/窗口管理/@ohos.window (窗口)/Interfaces (其他)/arkts-apis-window-i.md#windowlimits11>)约束。
