---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/speech-textreader-guide
title: 朗读控件
breadcrumb: 指南 > AI > Speech Kit（场景化语音服务） > 朗读控件
category: harmonyos-guides
scraped_at: 2026-06-11T15:19:33+08:00
doc_updated_at: 2026-05-26
content_hash: sha256:fe9f7c9336da3d0189d86bca0109bf8ad01155255c3c9520e0059030576eeec7
---
## 适用场景

朗读控件应用广泛，例如在用户不方便或者无法查看屏幕文字的时候，为用户朗读新闻，提供资讯。

本章节将向您介绍如何使用朗读组件，效果如下图所示。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5f/v3/qZLy4D5PT5iE_LZL9_9IKw/zh-cn_image_0000002622859237.png?HW-CC-KV=V1&HW-CC-Date=20260611T071931Z&HW-CC-Expire=86400&HW-CC-Sign=E90B595645271494082026FAB55DC3169E211542742A20D7A58162D856724998)

## 接口说明

以下仅列出demo中调用的部分主要接口，具体API说明详见[API参考](<../../../../harmonyos-references/Speech Kit（场景化语音服务）/ArkTS API/TextReader（朗读控件）/speech-textreader-api.md>)。

| 接口名 | 描述 |
| --- | --- |
| [init](<../../../../harmonyos-references/Speech Kit（场景化语音服务）/ArkTS API/TextReader（朗读控件）/speech-textreader-api.md#init>)(context: [common.BaseContext](<../../../../harmonyos-references/Ability Kit（程序框架服务）/ArkTS API/接口依赖的元素及定义/application/BaseContext/js-apis-inner-application-basecontext.md>), readParams: [ReaderParam](<../../../../harmonyos-references/Speech Kit（场景化语音服务）/ArkTS API/TextReader（朗读控件）/speech-textreader-api.md#readerparam>)): Promise<void> | 初始化TextReader。 |
| [start](<../../../../harmonyos-references/Speech Kit（场景化语音服务）/ArkTS API/TextReader（朗读控件）/speech-textreader-api.md#start>)(readInfoList: [ReadInfo](<../../../../harmonyos-references/Speech Kit（场景化语音服务）/ArkTS API/TextReader（朗读控件）/speech-textreader-api.md#readinfo>)[], articleId?: string): Promise<void> | 启动TextReader。 |
| on(type: string, callback: function): void | 注册所有事件回调，具体事件类型详见[API参考](<../../../../harmonyos-references/Speech Kit（场景化语音服务）/ArkTS API/TextReader（朗读控件）/speech-textreader-api.md>)。 |

## 开发步骤

1. 首先从项目根目录进入/src/main/ets/entryability/EntryAbility.ets文件，将WindowManager添加至工程。

   ```
   1. import { WindowManager } from '@kit.SpeechKit';
   2. import { ConfigurationConstant } from '@kit.AbilityKit';
   ```
2. （可选）在onWindowStageCreate(windowStage: window.WindowStage)生命周期方法中，添加setWindowStage方法设置窗口管理器。

   ```
   1. onWindowStageCreate(windowStage: window.WindowStage): void {
   2. console.info('Ability onWindowStageCreate');
   3. WindowManager.setWindowStage(windowStage);

   5. windowStage.loadContent('pages/Index', (err, data) => {
   6. if (err) {
   7. console.error(`Failed to load the content. Code: ${err.code}, message: ${err.message}`);
   8. return;
   9. }
   10. console.info(`Succeeded in loading the content. Data: ${JSON.stringify(data)}.` );
   11. });
   12. }
   ```
3. 在onCreate()生命周期方法中，设置应用的颜色模式，使控件颜色模式跟应用的颜色模式保持一致。

   * 如果应用想要跟随系统切换深浅色模式，请将颜色模式设置为COLOR\_MODE\_NOT\_SET。
   * 如果应用想要主动配置颜色模式，请将颜色模式设置为COLOR\_MODE\_LIGHT（浅色）或者COLOR\_MODE\_DARK（深色）。

   下面以自动跟随系统切换为例。

   ```
   1. onCreate(): void {
   2. this.context.getApplicationContext().setColorMode(ConfigurationConstant.ColorMode.COLOR_MODE_NOT_SET);
   3. }
   ```
4. 从项目根目录进入/src/main/ets/pages/Index.ets文件，在使用朗读控件前，将实现朗读控件和其他相关的类添加至工程。

   ```
   1. import { TextReader, TextReaderIcon, ReadStateCode } from '@kit.SpeechKit';
   ```
5. 简单配置页面的布局，加入听筒图标，并且设置onClick点击事件。

   ```
   1. /**
   2. * 播放状态
   3. */
   4. @State readState: ReadStateCode = ReadStateCode.WAITING;

   6. build() {
   7. Column() {
   8. TextReaderIcon({ readState: this.readState })
   9. .margin({ right: 20 })
   10. .width(32)
   11. .height(32)
   12. .onClick(() => {
   13. // 设置点击事件
   14. // ...
   15. })
   16. }
   17. }
   ```
6. 初始化朗读控件。

   ```
   1. // 用于显示当前页的按钮状态
   2. @State isInit: boolean = false;
   3. /**
   4. * 待加载的文章
   5. */
   6. @State readInfoList: TextReader.ReadInfo[] = [];
   7. @State selectedReadInfo: TextReader.ReadInfo = this.readInfoList[0];

   9. async aboutToAppear() {
   10. // ...
   11. void this.init();
   12. /**
   13. * 加载数据
   14. */
   15. let readInfoList: TextReader.ReadInfo[] = [{
   16. id: '001',
   17. title: {
   18. text:'水调歌头.明月几时有',
   19. isClickable:true
   20. },
   21. author:{
   22. text:'宋.苏轼',
   23. isClickable:true
   24. },
   25. date: {
   26. text:'2024/01/01',
   27. isClickable:false
   28. },
   29. bodyInfo: '明月几时有？把酒问青天。'
   30. }];
   31. this.readInfoList = readInfoList;
   32. this.selectedReadInfo = this.readInfoList[0];
   33. // ...
   34. }

   36. /**
   37. * 初始化
   38. */
   39. async init() {
   40. const readerParam: TextReader.ReaderParam = {
   41. isVoiceBrandVisible: true,
   42. businessBrandInfo: {
   43. panelName: '小艺朗读',
   44. panelIcon: $r('app.media.startIcon')
   45. }
   46. }
   47. try {
   48. let context: Context | undefined = this.getUIContext().getHostContext()
   49. if (context) {
   50. await TextReader.init(context, readerParam);
   51. this.isInit = true;
   52. this.setActionListener();
   53. }
   54. } catch (err) {
   55. console.error(`TextReader failed to init. Code: ${err.code}, message: ${err.message}`);
   56. }
   57. }

   59. onStateChanged = (state: TextReader.ReadState) => {
   60. if (this.selectedReadInfo?.id === state.id) {
   61. this.readState = state.state;
   62. } else {
   63. this.readState = ReadStateCode.WAITING;
   64. }
   65. }

   67. // 设置操作监听
   68. setActionListener() {
   69. TextReader.on('stateChange', (state: TextReader.ReadState) => {
   70. this.onStateChanged(state);
   71. });
   72. // 在列表页无更多内容时，会显示加载失败，需要设置requestMore监听，调用loadMore函数以获得正确的显示信息。
   73. TextReader.on('requestMore', () => {
   74. TextReader.loadMore([], true);
   75. })
   76. }

   78. // 注销监听，根据业务情况在合适的时机调用
   79. releaseActionListener() {
   80. TextReader.off('stateChange');
   81. TextReader.off('requestMore');
   82. }
   ```
7. （可选）在setActionListener方法中设置更多监听，在用户与控件进行交互时触发回调通知开发者。注销监听，监听结束后进行释放。

   ```
   1. // 设置监听
   2. setActionListener() {
   3. TextReader.on('setArticle', async (id: string) => { console.info(`setArticle ${id}`) });
   4. TextReader.on('clickArticle', (id: string) => {console.info(`onClickArticle ${id}`) });
   5. TextReader.on('clickAuthor', (id: string) => { console.info(`onClickAuthor ${id}`) });
   6. TextReader.on('clickNotification',  (id: string) => { console.info(`onClickNotification ${id}`) });
   7. TextReader.on('showPanel', () => { console.info(`onShowPanel`) });
   8. TextReader.on('hidePanel', () => { console.info(`onHidePanel`) });
   9. // ...
   10. }
   11. // 注销监听
   12. releaseActionListener() {
   13. TextReader.off('setArticle');
   14. TextReader.off('clickArticle');
   15. TextReader.off('clickAuthor');
   16. TextReader.off('clickNotification');
   17. TextReader.off('showPanel');
   18. TextReader.off('hidePanel');
   19. // ...
   20. }
   ```
8. 启动朗读控件。

   ```
   1. build() {
   2. Column() {
   3. TextReaderIcon({ readState: this.readState })
   4. // ...
   5. .onClick(() => {
   6. try {
   7. void TextReader.start(this.readInfoList, this.selectedReadInfo?.id);
   8. } catch (err) {
   9. console.error(`TextReader failed to start. Code: ${err.code}, message: ${err.message}`);
   10. }
   11. })
   12. }
   13. }
   ```
9. （可选）若要配置长时任务，需要在[module.json5配置文件](../../../基础入门/开发基础知识/应用配置文件（Stage模型）/module.json5配置文件/module-configuration-file.md)中添加ohos.permission.KEEP\_BACKGROUND\_RUNNING权限，并且加入backgroundModes选项，然后在readerParam中将keepBackgroundRunning配置为true，确保朗读控件后台播报正常。

   ```
   1. // module.json5
   2. {
   3. "module": {
   4. // ...
   5. "requestPermissions": [
   6. {
   7. "name": "ohos.permission.KEEP_BACKGROUND_RUNNING",
   8. "usedScene": {
   9. "abilities": [
   10. "FormAbility"
   11. ],
   12. "when": "inuse"
   13. }
   14. },
   15. ],
   16. "abilities": [
   17. {
   18. // ...
   19. "backgroundModes": [
   20. "audioPlayback"
   21. ],
   22. // ...
   23. }
   24. ]
   25. }
   26. }

   28. // Index.ets
   29. async init() {
   30. const readerParam: TextReader.ReaderParam = {
   31. // ...
   32. keepBackgroundRunning: true
   33. }
   34. }
   ```
10. （可选）若要在控件使用功能时切换音色，需要在[module.json5配置文件](../../../基础入门/开发基础知识/应用配置文件（Stage模型）/module.json5配置文件/module-configuration-file.md)中添加ohos.permission.INTERNET和ohos.permission.GET\_NETWORK\_INFO权限，确保朗读控件可以正常切换音色。

```
1. {
2. "module": {
3. // ...
4. "requestPermissions": [
5. {
6. "name": "ohos.permission.INTERNET",
7. "reason": "$string:reason",
8. "usedScene": {"abilities": []}
9. },
10. {
11. "name": "ohos.permission.GET_NETWORK_INFO",
12. "reason": "$string:reason",
13. "usedScene": {"abilities": []}
14. },
15. ],
16. }
17. }
```

## 开发实例

### EntryAbility.ets

```
1. import { AbilityConstant, ConfigurationConstant, UIAbility, Want } from '@kit.AbilityKit';
2. import { window } from '@kit.ArkUI';
3. import { WindowManager } from '@kit.SpeechKit';
4. import { common } from '@kit.AbilityKit';
5. import { BusinessError } from '@kit.BasicServicesKit';

7. export default class EntryAbility extends UIAbility {
8. onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
9. try {
10. this.context.getApplicationContext().setColorMode(ConfigurationConstant.ColorMode.COLOR_MODE_NOT_SET);
11. let eventHub = this.context.eventHub;
12. eventHub.on('onShowPanel', this.onShowPanel);
13. } catch (err) {
14. console.error(`error code: ${err.code}, message: ${err.message}.`);
15. }
16. console.info('Ability onCreate');
17. }

19. onDestroy(): void {
20. console.info('Ability onDestroy');
21. }

23. onWindowStageCreate(windowStage: window.WindowStage): void {
24. console.info('Ability onWindowStageCreate');
25. WindowManager.setWindowStage(windowStage);

27. windowStage.loadContent('pages/Index', (err, data) => {
28. if (err.code) {
29. console.error(`Failed to load the content. Code: ${err.code}, message: ${err.message}`);
30. return;
31. }
32. console.info(`Succeeded in loading the content. Data: ${JSON.stringify(data)}.`);
33. });
34. }

36. onWindowStageDestroy(): void {
37. console.info('Ability onWindowStageDestroy');
38. }

40. onForeground(): void {
41. console.info('Ability onForeground');
42. }

44. onBackground(): void {
45. console.info('Ability onBackground');
46. }

48. onShowPanel = () => {
49. let context: common.UIAbilityContext = this.context;
50. let want: Want = {
51. deviceId: '',
52. bundleName: 'com.example.speechkit', // 需替换成实际应用包名
53. abilityName: 'SubAbility',
54. parameters: {
55. info: 'From EntryAbility onShowPanel'
56. }
57. };
58. context?.startAbility(want).then(() => {
59. console.info('Succeeded in starting ability');
60. }).catch((e: BusinessError) => {
61. console.error(`Failed to start ability. Code is ${e.code}, message is ${e.message}`);
62. })
63. };
64. }
```

### Index.ets

```
1. import { TextReader, TextReaderIcon, ReadStateCode } from '@kit.SpeechKit';
2. import { deviceInfo } from '@kit.BasicServicesKit';

4. @Entry
5. @Component
6. struct Index {

8. /**
9. * 待加载的文章
10. */
11. @State readInfoList: TextReader.ReadInfo[] = [];
12. @State selectedReadInfo: TextReader.ReadInfo = this.readInfoList[0];

14. /**
15. * 播放状态
16. */
17. @State readState: ReadStateCode = ReadStateCode.WAITING;

19. /**
20. * 用于显示当前页的按钮状态
21. */
22. @State isInit: boolean = false;

24. async aboutToAppear() {
25. /**
26. * 加载数据
27. */
28. let readInfoList: TextReader.ReadInfo[] = [{
29. id: '001',
30. title: {
31. text: '水调歌头.明月几时有',
32. isClickable: true
33. },
34. author: {
35. text: '宋.苏轼',
36. isClickable: true
37. },
38. date: {
39. text: '2024/01/01',
40. isClickable: false
41. },
42. bodyInfo: '明月几时有？把酒问青天。'
43. }];
44. this.readInfoList = readInfoList;
45. this.selectedReadInfo = this.readInfoList[0];
46. void await this.init();
47. AppStorage.setOrCreate('isReadyToStart', false);
48. }

50. /**
51. * 初始化
52. */
53. async init() {
54. const readerParam: TextReader.ReaderParam = {
55. isVoiceBrandVisible: true,
56. businessBrandInfo: {
57. panelName: '小艺朗读',
58. panelIcon: $r('app.media.startIcon')
59. }
60. };
61. try {
62. let context: Context | undefined = this.getUIContext().getHostContext();
63. if (context) {
64. await TextReader.init(context, readerParam);
65. this.isInit = true;
66. this.setActionListener();
67. }
68. } catch (err) {
69. console.error(`TextReader failed to init. Code: ${err.code}, message: ${err.message}`);
70. }
71. }

73. // 设置操作监听
74. setActionListener() {
75. TextReader.on('stateChange', (state: TextReader.ReadState) => {
76. this.onStateChanged(state);
77. });

79. TextReader.on('requestMore', () => {
80. TextReader.loadMore([], true);
81. });
82. }

84. onStateChanged = (state: TextReader.ReadState) => {
85. if (this.selectedReadInfo?.id === state.id) {
86. this.readState = state.state;
87. } else {
88. this.readState = ReadStateCode.WAITING;
89. }
90. };

92. build() {
93. Column() {
94. TextReaderIcon({ readState: this.readState })
95. .margin({ right: 20 })
96. .width(32)
97. .height(32)
98. .onClick(() => {
99. try {
100. if (deviceInfo.deviceType === '2in1') {
101. let context = this.getUIContext().getHostContext();
102. context?.eventHub.emit('onShowPanel');
103. }
104. void TextReader.start(this.readInfoList, this.selectedReadInfo?.id);
105. TextReader.showPanel();
106. } catch (err) {
107. console.error(`TextReader failed to start. Code: ${err.code}, message: ${err.message}`);
108. }
109. })
110. }
111. .height('100%')
112. }
113. }
```

### SubAbility.ets

```
1. import { TextReader, WindowManager } from '@kit.SpeechKit';
2. import { emitter } from '@kit.BasicServicesKit';
3. import { window } from '@kit.ArkUI';
4. import { AbilityConstant, UIAbility,Want } from '@kit.AbilityKit';

7. export default class SubAbility extends UIAbility {
8. private link: SubscribedAbstractProperty<boolean> = AppStorage.link('isReadyToStart');

10. onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
11. let info = want?.parameters?.info;
12. }

14. onDestroy(): void {
15. console.info('Ability onDestroy');
16. }

18. onWindowStageCreate(windowStage: window.WindowStage): void {
19. // 主窗口正在被创建，为此窗口设置主页面
20. console.info('SubAbility onWindowStageCreate');

22. WindowManager.setWindowStage(windowStage);
23. let eventData: emitter.EventData = {
24. data: {
25. 'state': 'publish'
26. }
27. };
28. emitter.emit("onLoadSubAbility", eventData);
29. this.link.set(true);
30. console.debug(`onWindowStageCreate::isReadyToStart: ${AppStorage.get<boolean>('isReadyToStart')}`)
31. }

33. async onWindowStageDestroy(): Promise<void> {
34. // 主窗口正在被销毁，隐藏面板并停止播放
35. console.info('Ability onWindowStageDestroy');
36. TextReader.hidePanel();
37. await TextReader.stop();
38. this.link.set(false);
39. console.debug(`onWindowStageDestroy::isReadyToStart: ${AppStorage.get<boolean>('isReadyToStart')}`)
40. }

42. onForeground(): void {

44. }

46. onBackground(): void {

48. }
49. }
```

### module.json5

```
1. {
2. "module": {
3. "name": "entry",
4. "type": "entry",
5. "description": "$string:module_desc",
6. "mainElement": "EntryAbility",
7. "deviceTypes": [
8. "phone",
9. "tablet",
10. "2in1"
11. ],
12. "deliveryWithInstall": true,
13. "installationFree": false,
14. "pages": "$profile:main_pages",
15. "abilities": [
16. {
17. "name": "EntryAbility",
18. "srcEntry": "./ets/entryability/EntryAbility.ets",
19. "description": "$string:EntryAbility_desc",
20. "icon": "$media:layered_image",
21. "label": "$string:EntryAbility_label",
22. "startWindowIcon": "$media:startIcon",
23. "startWindowBackground": "$color:start_window_background",
24. "exported": true,
25. "skills": [
26. {
27. "entities": [
28. "entity.system.home"
29. ],
30. "actions": [
31. "ohos.want.action.home"
32. ]
33. }
34. ]
35. },
36. {
37. "name": "SubAbility", // UIAbility组件的名称
38. "srcEntry": "./ets/entryability/SubAbility.ets", // UIAbility组件的代码路径
39. "description": "$string:EntryAbility_desc", // UIAbility组件的描述信息
40. "icon": "$media:layered_image", // UIAbility组件的图标
41. "label": "$string:EntryAbility_label", // UIAbility组件的标签
42. "startWindowIcon": "$media:startIcon", // UIAbility组件启动页面图标资源文件的索引
43. "startWindowBackground": "$color:start_window_background", // UIAbility组件启动页面背景颜色资源文件的索引
44. "supportWindowMode": ['floating'],
45. "maxWindowWidth": 1158,
46. "minWindowWidth": 750,
47. "maxWindowHeight": 772,
48. "minWindowHeight": 500,
49. }
50. ],
51. "requestPermissions": [
52. {
53. "name": "ohos.permission.KEEP_BACKGROUND_RUNNING",
54. "usedScene": {
55. "abilities": []}
56. },
57. {
58. "name": "ohos.permission.INTERNET",
59. "reason": "$string:reason",
60. "usedScene": {"abilities": []}
61. },
62. {
63. "name": "ohos.permission.GET_NETWORK_INFO",
64. "reason": "$string:reason",
65. "usedScene": {"abilities": []}
66. },
67. ]
68. }
69. }
```

## 2in1适配步骤

2in1设备除了适配[开发步骤](speech-textreader-guide.md#开发步骤)，还需执行以下步骤。如果开发者按照上述开发步骤来适配2in1，将会出现无法拉起播放面板的情况。

1. 在/src/main/ets/entryability下新建一个ability，用来承载2in1主窗，导入相关依赖。

   ```
   1. import { TextReader, WindowManager } from '@kit.SpeechKit';
   2. import { commonEventManager } from '@kit.BasicServicesKit';
   ```
2. 在新ability中声明一个应用全局的状态变量isReadyToStart，并且通过AppStorage管理此状态变量。

   ```
   1. private link: SubscribedAbstractProperty<boolean>= AppStorage.link('isReadyToStart');
   ```
3. 在Index.ets的aboutToAppear生命周期方法中，创建全局的状态变量isReadyToStart。

   ```
   1. aboutToAppear() {
   2. AppStorage.setOrCreate('isReadyToStart', false);
   3. // ...其他配置
   4. }
   ```
4. 配置WindowStage。对于5.1.1(19)及之前版本，使用getContext(this)接口实现。对于6.0.0(20)及以后版本，开始使用以下逻辑实现。

   * 在新ability的onWindowStageCreate生命周期方法中，发送onLoadSubAbility事件。
   * 通过WindowManager.setWindowStage(windowStage)来设置新ability的windowStage。
   * 在onWindowStageCreate中将isReadyToStart设为true。

   ```
   1. onWindowStageCreate(windowStage: window.WindowStage): void {
   2. // 主窗口正在被创建，为此窗口设置主页面
   3. WindowManager.setWindowStage(windowStage)
   4. let eventData: emitter.EventData = {
   5. data: {
   6. 'state': 'publish'
   7. }
   8. }
   9. emitter.emit("onLoadSubAbility", eventData);
   10. this.link.set(true);
   11. };
   ```
5. 在新ability的onWindowStageDestroy生命周期方法中，将isReadyToStart设为false，同时隐藏面板并停止播放。

   ```
   1. async onWindowStageDestroy(): Promise<void> {
   2. try {
   3. TextReader.hidePanel();
   4. await TextReader.stop();
   5. this.link.set(false);
   6. }catch (e) {
   7. console.error(`onWindowStageDestroy fail , msg: ${e}`)
   8. }
   9. }
   ```
6. 在entryability中，onCreate方法需要用eventHub设置'onShowPanel'回调，用来创造新的ability；onShowPanel回调中，首先构造want，然后通过context.startAbility接口创建新的ability。

   ```
   1. import { AbilityConstant, Want } from '@kit.AbilityKit';
   2. import { common } from "@kit.AbilityKit";
   3. import { BusinessError } from "@kit.BasicServicesKit";

   6. onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
   7. // ...其他配置
   8. let eventHub = this.context.eventHub;
   9. eventHub.on('onShowPanel', this.onShowPanel);
   10. }

   12. onShowPanel = () => {
   13. let context: common.UIAbilityContext = this.context;
   14. let want: Want = {
   15. deviceId: '',
   16. bundleName: 'com.example.speechkit', // 需替换成实际应用包名
   17. abilityName: 'SubAbility',
   18. parameters: {
   19. info: 'From EntryAbility onShowPanel'
   20. }
   21. };
   22. context?.startAbility(want).then(() => {
   23. console.info('Succeeded in starting ability');
   24. }).catch((e: BusinessError) => {
   25. console.error(`Failed to start ability. Code is ${e.code}, message is ${e.message}`);
   26. })
   27. };
   ```
7. 在调用start之前根据设备类型进行判断，如果是2in1需要首先发送'onShowPanel'事件构造ability。

   ```
   1. import { deviceInfo } from '@kit.BasicServicesKit';

   3. if (deviceInfo.deviceType === '2in1') {
   4. let context = this.getUIContext().getHostContext();
   5. context?.eventHub.emit('onShowPanel');
   6. }
   7. try {
   8. TextReader.showPanel();
   9. } catch (err) {
   10. console.error(`error code: ${err.code}, message: ${err.message}.`)
   11. }
   ```
8. 在module.json5中添加ability配置项，max和min的值需要保持一致，固定窗口的大小。

   ```
   1. {
   2. "name": "SubAbility", // UIAbility组件的名称
   3. "srcEntry": "./ets/entryability/SubAbility.ets", // UIAbility组件的代码路径
   4. "description": "$string:SubAbility_desc", // UIAbility组件的描述信息
   5. "icon": "$media:icon", // UIAbility组件的图标
   6. "label": "$string:EntryAbility_label", // UIAbility组件的标签
   7. "startWindowIcon": "$media:icon", // UIAbility组件启动页面图标资源文件的索引
   8. "startWindowBackground": "$color:start_window_background", // UIAbility组件启动页面背景颜色资源文件的索引
   9. "supportWindowMode": ['floating'], // 窗口支持悬浮窗显示
   10. "maxWindowWidth": 1158, // 最大窗口宽度
   11. "minWindowWidth": 1158, // 最小窗口宽度
   12. "maxWindowHeight": 772, // 最大窗口高度
   13. "minWindowHeight": 772, // 最小窗口高度
   14. }
   ```
