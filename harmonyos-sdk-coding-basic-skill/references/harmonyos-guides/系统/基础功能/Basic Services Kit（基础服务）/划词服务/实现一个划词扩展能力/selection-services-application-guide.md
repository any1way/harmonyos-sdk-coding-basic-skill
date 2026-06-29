---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/selection-services-application-guide
title: 实现一个划词扩展能力
breadcrumb: 指南 > 系统 > 基础功能 > Basic Services Kit（基础服务） > 划词服务 > 实现一个划词扩展能力
category: harmonyos-guides
scraped_at: 2026-06-11T14:50:01+08:00
doc_updated_at: 2026-06-03
content_hash: sha256:ea660f89cd345a7a224e3c4e9e068218a90f3875eb6d3811f1b9b1441be94029
---
## 接口说明

| 名称 | 描述 |
| --- | --- |
| [on(type: 'selectionCompleted', callback: Callback<SelectionInfo>): void](<../../../../../../harmonyos-references/基础功能/Basic Services Kit（基础服务）/ArkTS API/数据文件处理/@ohos.selectionInput.selectionManager (划词管理)/js-apis-selectioninput-selectionmanager.md#selectionmanageronselectioncompleted>) | 订阅划词完成事件，使用callback回调函数。 |
| [getSelectionContent(): Promise<string>](<../../../../../../harmonyos-references/基础功能/Basic Services Kit（基础服务）/ArkTS API/数据文件处理/@ohos.selectionInput.selectionManager (划词管理)/js-apis-selectioninput-selectionmanager.md#getselectioncontent>) | 获取选中文本的内容。 |
| [createPanel(ctx: Context, info: PanelInfo): Promise<Panel>](<../../../../../../harmonyos-references/基础功能/Basic Services Kit（基础服务）/ArkTS API/数据文件处理/@ohos.selectionInput.selectionManager (划词管理)/js-apis-selectioninput-selectionmanager.md#createpanel>) | 创建划词面板。 |
| [show(): Promise<void>](<../../../../../../harmonyos-references/基础功能/Basic Services Kit（基础服务）/ArkTS API/数据文件处理/@ohos.selectionInput.selectionManager (划词管理)/js-apis-selectioninput-selectionmanager.md#show>) | 显示面板。 |
| [hide(): Promise<void>](<../../../../../../harmonyos-references/基础功能/Basic Services Kit（基础服务）/ArkTS API/数据文件处理/@ohos.selectionInput.selectionManager (划词管理)/js-apis-selectioninput-selectionmanager.md#hide>) | 隐藏面板。 |
| [startMoving(): Promise<void>](<../../../../../../harmonyos-references/基础功能/Basic Services Kit（基础服务）/ArkTS API/数据文件处理/@ohos.selectionInput.selectionManager (划词管理)/js-apis-selectioninput-selectionmanager.md#startmoving>) | 使当前划词面板可以随鼠标拖动。 |
| [moveToGlobalDisplay(x: number, y: number): Promise<void>](<../../../../../../harmonyos-references/基础功能/Basic Services Kit（基础服务）/ArkTS API/数据文件处理/@ohos.selectionInput.selectionManager (划词管理)/js-apis-selectioninput-selectionmanager.md#movetoglobaldisplay>) | 移动划词面板至屏幕指定位置。 |

上述接口为本文档用到的核心接口，如需了解划词服务的全量接口，请参考[selectionInput.SelectionExtensionAbility](<../../../../../../harmonyos-references/基础功能/Basic Services Kit（基础服务）/ArkTS API/数据文件处理/@ohos.selectionInput.SelectionExtensionAbility (划词扩展能力)/js-apis-selectioninput-s_31342665.md>)接口文档获取接口详细描述。

## 开发步骤

完整的工程示例详见[SelectionAppSample](https://gitcode.com/openharmony/applications_app_samples/tree/master/code/DocsSample/SelectionService/SelectionAppSample)。

1. 创建划词应用工程。

   1.1 打开[DevEco Studio](https://developer.huawei.com/consumer/cn/deveco-studio/)，点击"File>New>Create Project"创建一个Empty Ability，设备类型勾选"PC/2in1"。

   1.2 在工程对应的ets目录下，右键选择"New>Directory"，新建两个目录，分别命名为selectionextability、models。

   1.3 在selectionextability目录下，新建SelectionExtAbility.ets文件；在models目录下，新建SelectionModel.ets文件；在目录pages下，新建两个page文件MainPanel.ets和MenuPanel.ets。目录如下：

   ```
   1. /src/main/
   2. ├── ets/
   3. │   ├── models
   4. │   |   └── SelectionModel.ets     # 划词模块管理类
   5. │   ├── pages
   6. │   |   ├── MainPanel.ets                    # 主面板
   7. │   |   └── MenuPanel.ets                    # 菜单面板
   8. │   └── selectionextability
   9. │       └── SelectionExtAbility.ets     # 划词扩展类
   10. ├── resources/base/profile/main_pages.json
   11. ├── module.json5                             # 配置文件
   ```

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0d/v3/k33y3fHhSOmzqr81WuSeXQ/zh-cn_image_0000002592378810.png?HW-CC-KV=V1&HW-CC-Date=20260611T064959Z&HW-CC-Expire=86400&HW-CC-Sign=244E96AE8EA8039AFFB738D507C07E4CD7A5C2918AB114F5FB76F15384EE782C)
2. 在[SelectionModel.ets](https://gitcode.com/openharmony/applications_app_samples/blob/master/code/DocsSample/SelectionService/SelectionAppSample/entry/src/main/ets/models/SelectionModel.ets)文件中，开发者可自定义划词模块管理类，用于统一管理划词内容、窗口等信息。并且实现一些get、set接口，便于信息的类间传递。

   ```
   1. import { selectionManager, SelectionExtensionContext } from '@kit.BasicServicesKit';
   2. import { hilog } from '@kit.PerformanceAnalysisKit';

   4. export class SelectionModel {
   5. private selectionInfo: selectionManager.SelectionInfo | undefined;
   6. private selectionContent: string | undefined;
   7. private selectionPanel: selectionManager.Panel | undefined;
   8. private context: SelectionExtensionContext | undefined;
   9. private listener: (selectionInfo: selectionManager.SelectionInfo) => void;

   11. private constructor() {
   12. this.selectionInfo = undefined;
   13. this.selectionContent = undefined;
   14. this.selectionPanel = undefined;
   15. this.context = undefined;
   16. this.listener = (selectionInfo: selectionManager.SelectionInfo) => {
   17. hilog.info(0x0000, 'SelectionModel', `Received selection selectionInfo: ${selectionInfo}`);
   18. }
   19. }

   21. public static getInstance(): SelectionModel {
   22. if (globalThis.instance == null) {
   23. globalThis.instance = new SelectionModel();
   24. }
   25. return globalThis.instance;
   26. }

   28. public getSelectionInfo(): selectionManager.SelectionInfo | undefined {
   29. return this.selectionInfo;
   30. }

   32. public setSelectionInfo(selectionInfo: selectionManager.SelectionInfo) {
   33. this.selectionInfo = selectionInfo;
   34. }

   36. public getSelectionContent(): string | undefined {
   37. return this.selectionContent;
   38. }

   40. public setSelectionContent(selectionContent: string) {
   41. this.selectionContent = selectionContent;
   42. }

   44. public getSelectionPanel(): selectionManager.Panel | undefined {
   45. return this.selectionPanel;
   46. }

   48. public setSelectionPanel(selectionPanel: selectionManager.Panel) {
   49. this.selectionPanel = selectionPanel;
   50. }

   52. public getContext(): SelectionExtensionContext | undefined {
   53. return this.context;
   54. }

   56. public setContext(context: SelectionExtensionContext) {
   57. this.context = context;
   58. }

   60. public registerListener(listener: (selectionInfo: selectionManager.SelectionInfo) => void) {
   61. this.listener = listener;
   62. }
   63. }
   ```

   [SelectionModel.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/SelectionService/SelectionAppSample/entry/src/main/ets/models/SelectionModel.ets#L16-L81)
3. 在[SelectionExtAbility.ets](https://gitcode.com/openharmony/applications_app_samples/blob/master/code/DocsSample/SelectionService/SelectionAppSample/entry/src/main/ets/selectionextability/SelectionExtAbility.ets)文件中，开发者可实现扩展能力类。该类需要继承[SelectionExtensionAbility](<../../../../../../harmonyos-references/基础功能/Basic Services Kit（基础服务）/ArkTS API/数据文件处理/@ohos.selectionInput.SelectionExtensionAbility (划词扩展能力)/js-apis-selectioninput-s_31342665.md>)，用于划词扩展生命周期的管理。

   ```
   1. import { selectionManager, SelectionExtensionAbility} from '@kit.BasicServicesKit';
   2. import { Want } from '@kit.AbilityKit';
   3. import { rpc } from '@kit.IPCKit';

   5. class SelectionAbilityStub extends rpc.RemoteObject {
   6. constructor(des: string) {
   7. super(des);
   8. }

   10. onRemoteMessageRequest(
   11. code: number,
   12. data: rpc.MessageSequence,
   13. reply: rpc.MessageSequence,
   14. options: rpc.MessageOption
   15. ): boolean | Promise<boolean> {
   16. return true;
   17. }
   18. }

   20. class SelectionExtAbility extends SelectionExtensionAbility {
   21. private panel_: selectionManager.Panel | undefined = undefined;

   23. onConnect(want: Want): rpc.RemoteObject {
   24. // 当SelectionExtensionAbility实例完成创建时，系统会触发该回调。开发者可在该回调中执行初始化逻辑（如定义变量、加载资源、监听划词事件等）。
   25. return new SelectionAbilityStub('remote');
   26. }

   28. onDisconnect(): void {
   29. // 当SelectionExtensionAbility实例被销毁（例如用户关闭划词开关或切换划词应用）时，系统触发该回调。开发者可以在该生命周期中执行资源清理、数据保存等相关操作。
   30. selectionManager.destroyPanel(this.panel_);
   31. }
   32. }

   34. export default SelectionExtAbility;
   ```

   上述代码中，划词扩展被拉起时会触发[onConnect](<../../../../../../harmonyos-references/基础功能/Basic Services Kit（基础服务）/ArkTS API/数据文件处理/@ohos.selectionInput.SelectionExtensionAbility (划词扩展能力)/js-apis-selectioninput-s_31342665.md#onconnect>)回调，可以在该回调中监听划词事件，完成划词窗口的创建、窗口内容的设定、窗口的移动、窗口的显示和隐藏等操作；当划词扩展退出时会触发[onDisconnect](<../../../../../../harmonyos-references/基础功能/Basic Services Kit（基础服务）/ArkTS API/数据文件处理/@ohos.selectionInput.SelectionExtensionAbility (划词扩展能力)/js-apis-selectioninput-s_31342665.md#ondisconnect>)回调，可以在该回调中完成窗口销毁的操作。详细内容可参见下面第4步。
4. 在划词扩展被拉起时，可以提前创建划词窗口（但不调用[show](<../../../../../../harmonyos-references/基础功能/Basic Services Kit（基础服务）/ArkTS API/数据文件处理/@ohos.selectionInput.selectionManager (划词管理)/js-apis-selectioninput-selectionmanager.md#show>)接口），以缩短用户在第一次划词时的响应延迟。同时，可以在[onConnect](<../../../../../../harmonyos-references/基础功能/Basic Services Kit（基础服务）/ArkTS API/数据文件处理/@ohos.selectionInput.SelectionExtensionAbility (划词扩展能力)/js-apis-selectioninput-s_31342665.md#onconnect>)中监听划词事件，执行后续的弹窗操作。通过监听[selectionCompleted](<../../../../../../harmonyos-references/基础功能/Basic Services Kit（基础服务）/ArkTS API/数据文件处理/@ohos.selectionInput.selectionManager (划词管理)/js-apis-selectioninput-selectionmanager.md#selectionmanageronselectioncompleted>)获取[SelectionInfo](<../../../../../../harmonyos-references/基础功能/Basic Services Kit（基础服务）/ArkTS API/数据文件处理/@ohos.selectionInput.selectionManager (划词管理)/js-apis-selectioninput-selectionmanager.md#selectioninfo>)其中包含了划词操作的起始和结束坐标等信息。通过调用[getSelectionContent](<../../../../../../harmonyos-references/基础功能/Basic Services Kit（基础服务）/ArkTS API/数据文件处理/@ohos.selectionInput.selectionManager (划词管理)/js-apis-selectioninput-selectionmanager.md#getselectioncontent>)接口获取划词内容。

   ```
   1. import { selectionManager, PanelInfo, PanelType, SelectionExtensionAbility, BusinessError } from '@kit.BasicServicesKit';
   2. import { SelectionModel } from '../models/SelectionModel';
   3. import { Want } from '@kit.AbilityKit';
   4. import { rpc } from '@kit.IPCKit';
   5. import { hilog } from '@kit.PerformanceAnalysisKit';

   7. class SelectionAbilityStub extends rpc.RemoteObject {
   8. constructor(des: string) {
   9. super(des);
   10. }

   12. onRemoteMessageRequest(
   13. code: number,
   14. data: rpc.MessageSequence,
   15. reply: rpc.MessageSequence,
   16. options: rpc.MessageOption
   17. ): boolean | Promise<boolean> {
   18. return true;
   19. }
   20. }

   22. class SelectionExtAbility extends SelectionExtensionAbility {
   23. private panel_: selectionManager.Panel | undefined = undefined;

   25. onConnect(want: Want): rpc.RemoteObject {
   26. SelectionModel.getInstance().setContext(this.context);
   27. selectionManager.on('selectionCompleted', async (info: selectionManager.SelectionInfo) => {
   28. if (this.panel_ == undefined) {
   29. await this.createSelectionPanel();
   30. }
   31. this.onSelected(info);
   32. });
   33. return new SelectionAbilityStub('remote');
   34. }

   36. onDisconnect(): void {
   37. selectionManager.destroyPanel(this.panel_);
   38. }

   40. async createSelectionPanel() {
   41. let panelInfo: PanelInfo = {
   42. panelType: PanelType.MENU_PANEL,
   43. x: 0,
   44. y: 0,
   45. width: 500,
   46. height: 300
   47. }
   48. try {
   49. let panel: selectionManager.Panel = await selectionManager.createPanel(this.context, panelInfo);    // 创建菜单面板
   50. this.panel_ = panel;
   51. panel.setUiContent('pages/MenuPanel')   // 设置菜单面板样式
   52. .then(() => {
   53. hilog.info(0x0000, 'SelectionExtensionAbility', 'Succeed to setUiContent [pages/MenuPanel].');
   54. })
   55. .catch((error: BusinessError) => {
   56. hilog.info(0x0000, 'SelectionExtensionAbility', `Failed to setUiContent, error: ${JSON.stringify(error)}`);
   57. return;
   58. })
   59. } catch(error) {
   60. hilog.info(0x0000, 'SelectionExtensionAbility', `Failed to createPanel, error: ${JSON.stringify(error)}`);
   61. }
   62. }

   64. async onSelected(info: selectionManager.SelectionInfo) {
   65. SelectionModel.getInstance().setSelectionInfo(info);
   66. try {
   67. let content = await selectionManager.getSelectionContent();   // 获取划词内容
   68. SelectionModel.getInstance().setSelectionContent(content);
   69. } catch (error) {
   70. hilog.info(0x0000, 'SelectionExtensionAbility', `Failed to get selection content: ${JSON.stringify(error)}`);
   71. return;
   72. }
   73. if (!this.panel_) {
   74. hilog.info(0x0000, 'SelectionExtensionAbility', 'Panel is not created yet.');
   75. return;
   76. }
   77. this.panel_.moveToGlobalDisplay(info.startDisplayX, info.startDisplayY)    // 将弹窗移动到用户鼠标划词的起始点
   78. .then(() => {
   79. hilog.info(0x0000, 'SelectionExtensionAbility', 'Move succeed.');
   80. })
   81. .catch((error: BusinessError) => {
   82. hilog.info(0x0000, 'SelectionExtensionAbility', `Failed to move, error: ${JSON.stringify(error)}`);
   83. return;
   84. });

   86. await this.panel_.show()    // 显示弹窗
   87. .then(() => {
   88. hilog.info(0x0000, 'SelectionExtensionAbility', 'Show succeed.');
   89. })
   90. .catch((error: BusinessError) => {
   91. hilog.info(0x0000, 'SelectionExtensionAbility', `Failed to show panel, error: ${JSON.stringify(error)}`);
   92. return;
   93. });

   95. this.panel_.on('hidden', () => {    // 监听弹窗隐藏（窗口失焦时会触发隐藏）
   96. hilog.info(0x0000, 'SelectionExtensionAbility', 'panel has hidden.');
   97. })
   98. }
   99. }

   101. export default SelectionExtAbility;
   ```

   [SelectionExtAbility.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/SelectionService/SelectionAppSample/entry/src/main/ets/selectionextability/SelectionExtAbility.ets#L16-L128)
5. 在[MenuPanel.ets](https://gitcode.com/openharmony/applications_app_samples/blob/master/code/DocsSample/SelectionService/SelectionAppSample/entry/src/main/ets/pages/MenuPanel.ets)文件中，开发者可根据业务内容自主实现菜单面板的显示效果，例如提供翻译、查询、扩写等按钮。并且可以通过绑定点击事件，弹出不同的主面板，以展示不同的内容。本示例仅提供了一个简单的点击按钮，用于展示如何弹出主面板。

   ```
   1. import { SelectionModel } from '../models/SelectionModel';
   2. import { selectionManager, PanelInfo, BusinessError, PanelType, SelectionExtensionContext } from '@kit.BasicServicesKit';
   3. import { hilog } from '@kit.PerformanceAnalysisKit';
   4. import { Want } from '@kit.AbilityKit';

   6. @Entry
   7. @Component
   8. struct MenuPanel {
   9. @State message: string = 'MenuPanel';
   10. selectionInfo: selectionManager.SelectionInfo | undefined = undefined;

   12. CreateMainPanel() {
   13. this.selectionInfo = SelectionModel.getInstance().getSelectionInfo();
   14. let panelInfo: PanelInfo = {
   15. panelType: PanelType.MAIN_PANEL,
   16. x: 0,
   17. y: 0,
   18. width: 1500,
   19. height: 1000
   20. }
   21. selectionManager.createPanel(SelectionModel.getInstance().getContext(), panelInfo)
   22. .then(async (panel: selectionManager.Panel) => {
   23. SelectionModel.getInstance().setSelectionPanel(panel);
   24. hilog.info(0x0000, 'SelectionExtensionAbility', 'Succeed to create main panel');
   25. if (this.selectionInfo !== undefined) {
   26. panel.moveToGlobalDisplay(this.selectionInfo.startDisplayX + 100, this.selectionInfo.startDisplayY + 100);
   27. }
   28. try {
   29. panel.on('destroyed', () => {
   30. hilog.info(0x0000, 'SelectionExtensionAbility', 'panel has destroyed');
   31. })
   32. } catch (error) {
   33. hilog.info(0x0000, 'SelectionExtensionAbility', 'Failed to listen window destroy');
   34. }
   35. panel.setUiContent('pages/MainPanel')
   36. .then(() => {
   37. hilog.info(0x0000, 'SelectionExtensionAbility', 'Succeed to setUiContent [pages/MainPanel].');
   38. })
   39. .catch((error: BusinessError) => {
   40. hilog.info(0x0000, 'SelectionExtensionAbility', `Failed to setUiContent of main panel, error: [${JSON.stringify(error)}]`);
   41. return;
   42. });

   44. await panel.show()
   45. .then(() => {
   46. hilog.info(0x0000, 'SelectionExtensionAbility', 'Succeed to show main panel.');
   47. })
   48. .catch((error: BusinessError) => {
   49. hilog.info(0x0000, 'SelectionExtensionAbility', `Failed to show main panel, error: [${JSON.stringify(error)}]`);
   50. return;
   51. });
   52. })
   53. .catch((error: BusinessError) => {
   54. hilog.info(0x0000, 'SelectionExtensionAbility', `Failed to createPanel, error: [${JSON.stringify(error)}]`);
   55. return;
   56. });
   57. }

   59. startEntryAbility() {   // 拉起应用
   60. let wantAbility: Want = {
   61. bundleName: 'com.selection.selectionapplication',   // 应用的bundleName
   62. abilityName: 'EntryAbility',    // 应用的abilityName
   63. };
   64. let context: SelectionExtensionContext | undefined = SelectionModel.getInstance().getContext();
   65. if (context !== undefined) {
   66. context.startAbility(wantAbility)
   67. .then(() => {
   68. hilog.info(0x0000, 'SelectionExtensionAbility', `startAbility success, want: ${wantAbility.abilityName}`);
   69. })
   70. .catch((error: BusinessError) => {
   71. hilog.info(0x0000, 'SelectionExtensionAbility', `startAbility failed, error: ${JSON.stringify(error)}`);
   72. })
   73. }
   74. }

   76. build() {
   77. Column() {
   78. Button('click to show MAIN_PANEL')
   79. .onClick(() => {
   80. this.CreateMainPanel();
   81. })
   82. Button('start EntryAbility')
   83. .onClick(() => {
   84. this.startEntryAbility();
   85. })
   86. }
   87. .backgroundColor('#AAFFFF')
   88. .height('100%')
   89. .width('100%')
   90. }
   91. }
   ```

   [MenuPanel.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/SelectionService/SelectionAppSample/entry/src/main/ets/pages/MenuPanel.ets#L16-L108)
6. 在[MainPanel.ets](https://gitcode.com/openharmony/applications_app_samples/blob/master/code/DocsSample/SelectionService/SelectionAppSample/entry/src/main/ets/pages/MainPanel.ets)文件中，开发者可根据业务场景，自行实现主面板的显示效果。本示例仅提供了一个简单的展示划词内容的主面板，具体的业务侧功能需要开发者自行实现。

   ```
   1. import { SelectionModel } from '../models/SelectionModel';
   2. import { selectionManager } from '@kit.BasicServicesKit';
   3. @Entry
   4. @Component
   5. struct MainPanel {
   6. @State message: string = 'MainPanel';

   8. aboutToAppear(): void {
   9. let content: string | undefined = SelectionModel.getInstance().getSelectionContent();
   10. if (content !== undefined) {
   11. this.message = content;
   12. }
   13. }

   15. build() {
   16. RelativeContainer() {
   17. Text(this.message)
   18. .id('MainPanelHelloWorld')
   19. .fontSize(8)
   20. .alignRules({
   21. center: { anchor: '__container__', align: VerticalAlign.Center },
   22. middle: { anchor: '__container__', align: HorizontalAlign.Center }
   23. })
   24. }
   25. .onTouch((event: TouchEvent) => {
   26. if (event.type === TouchType.Down) {
   27. let selectionPanel: selectionManager.Panel | undefined = SelectionModel.getInstance().getSelectionPanel();
   28. if (selectionPanel !== undefined) {
   29. selectionPanel.startMoving();   // 调用selectionManager提供的startMoving接口可实现划词面板随鼠标拖动
   30. }
   31. }
   32. })
   33. .backgroundColor('#AAA000')
   34. .height('100%')
   35. .width('100%')
   36. }
   37. }
   ```

   [MainPanel.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/SelectionService/SelectionAppSample/entry/src/main/ets/pages/MainPanel.ets#L16-L54)
7. 配置[main\_pages.json](https://gitcode.com/openharmony/applications_app_samples/blob/master/code/DocsSample/SelectionService/SelectionAppSample/entry/src/main/resources/base/profile/main_pages.json)文件。

   在..\resources\base\profile\main\_pages.json文件中的src字段中添加新增的MainPanel和MenuPanel页面。

   ```
   1. "src": [
   2. "pages/MainPanel",
   3. "pages/MenuPanel"
   4. ]
   ```
8. 配置[module.json5](https://gitcode.com/openharmony/applications_app_samples/blob/master/code/DocsSample/SelectionService/SelectionAppSample/entry/src/main/module.json5)文件。

   在extensionAbilities字段中配置划词扩展类文件路径。

   ```
   1. "extensionAbilities": [
   2. {
   3. "name": "SelectionExtAbility",
   4. "srcEntry": "./ets/selectionextability/SelectionExtAbility.ets",
   5. "type": "selection",
   6. "exported": false,
   7. }
   8. ]
   ```

   [module.json5](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/SelectionService/SelectionAppSample/entry/src/main/module.json5#L50-L59)
9. 配置签名。

   点击[DevEco Studio](https://developer.huawei.com/consumer/cn/deveco-studio/)右上角的"Project Structure"按钮，点击"Signing Configs"按钮，按操作登录华为账号后会自动生成签名。

## 调测验证

1. 连接设备后，点击[DevEco Studio](https://developer.huawei.com/consumer/cn/deveco-studio/)右上角的绿色三角形"Run entry"按钮，编译器会执行编译并自动将应用安装到设备中。
2. 设置划词服务的系统参数。

   2.1 进入设置-->系统-->智慧划词界面打开智慧划词开关。

   2.2 选择当前应用为划词应用。

   2.3 选择划词触发方式为“点击ctrl键显示”。
3. 通过日志观察划词服务拉起划词扩展能力的过程。

   使用[DevEco Studio](https://developer.huawei.com/consumer/cn/deveco-studio/)的Hilog窗口查看日志。
4. 使用鼠标左键双击、三击或拖动选中文本后，键盘点击ctrl键，观察菜单面板的弹出。点击菜单面板上的按钮，观察主面板的弹出。
