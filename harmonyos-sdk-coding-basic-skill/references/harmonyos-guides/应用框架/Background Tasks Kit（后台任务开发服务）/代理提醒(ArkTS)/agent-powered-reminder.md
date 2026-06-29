---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/agent-powered-reminder
title: 代理提醒(ArkTS)
breadcrumb: 指南 > 应用框架 > Background Tasks Kit（后台任务开发服务） > 代理提醒(ArkTS)
category: harmonyos-guides
scraped_at: 2026-06-11T14:36:24+08:00
doc_updated_at: 2026-06-05
content_hash: sha256:dae45b9745166dfedc0233b02b8f7bc8bc3240619b86c9dc3acf298b0ac87103
---
## 功能介绍

应用退到后台或进程终止后，仍然有一些提醒用户的定时类通知，为满足此类功能场景，系统提供了代理提醒的能力。当应用退至后台或进程终止后，系统会代理应用做定时提醒。当前支持的提醒类型包括：倒计时、日历和闹钟。为了防止代理提醒被滥用于广告、营销类提醒，影响用户体验，部分设备上代理提醒增加了管控机制，应用无法直接使用代理提醒，管控后的使用方法请参考[管控限制](agent-powered-reminder.md#约束与限制)。

## 约束与限制

* **设备限制**：代理提醒适用于手机、平板、PC/2in1、智慧屏、智能穿戴设备。
* **管控限制**：

1. 手机、平板、PC/2in1设备存在管控，智慧屏、智能穿戴设备无管控限制。
2. 管控后可通过日历Calendar Kit替代代理提醒，实现相应的提醒功能，具体请参考[开发指南](<../../../应用服务/Calendar Kit（日历服务）/Calendar Kit简介/calendarmanager-overview.md>)；或者参考[代理提醒开放能力申请](agent-powered-reminder.md#代理提醒开放能力申请)向华为侧申请代理提醒权限，申请通过后会开通权益，即可正常调用代理提醒接口。

* **应用限制**：

  代理提醒仅对如下类型的应用开放申请：工具类、商务类、效率类、金融理财类、教育类、生活服务类、旅游类、医疗类、运动健康类、游戏类应用。若您的应用不在上述类型中，则不符合申请条件。符合上述类型的应用，请在线上申请时一并在附件中提交应用分类截图。应用分类信息可登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)网站，在“APP”页签中选择“应用上架”->“应用信息”查询。
* **场景限制**：

  营销类场景（如电商/红包/优惠券抢购、直播预约等）不支持申请代理提醒权限，以下给出几种常见的开放代理提醒申请的场景示例：

1. 生活类提醒（闹钟提醒、记账提醒、时间/日程提醒、临期提醒、习惯打卡、计时提醒、日历/纪念日提醒、行程提醒）。
2. 运动健康类提醒（运动/训练提醒、经期提醒、喝水提醒、饮食记录提醒、测血糖/吃药提醒、睡眠提醒、疫苗/产检提醒）。
3. 学习类提醒（学习提醒、课程提醒、背单词提醒）。
4. 办公类提醒（排班、办公打卡提醒）。
5. 游戏类提醒（游戏内玩家重要任务预警提醒，包含角色/资产受到损害，游戏任务完成提醒）。

说明

代理提醒需要同时满足应用限制和场景限制。单个应用可能涉及多个场景，例如某个游戏类应用包含直播预约和游戏任务完成提醒两种场景，因为直播预约属于营销类场景，因此不支持申请代理提醒。

* **个数限制**：

1. 单个普通应用有效/未过期的提醒数量不超过30个。
2. 从API version 10开始，所有应用有效/未过期的提醒数量总和不超过12000个。API version 9及之前的版本，有效/未过期的提醒数量总和不超过2000个。

说明

当到达设置的提醒时间点时，通知中心会弹出相应提醒。若未点击提醒上的关闭/CLOSE按钮，则代理提醒是有效/未过期的；若点击了关闭/CLOSE按钮，则代理提醒过期。

当代理提醒是周期性提醒时，如设置每天提醒，无论是否点击关闭/CLOSE按钮，代理提醒都是有效的。

* **跳转限制**：点击提醒通知后跳转的应用必须是申请代理提醒的本应用。

## 与相关Kit的关系

* 当到达设置的提醒时间点后，代理提醒使用Notification Kit发布通知，通知会显示在通知中心，通知样式请参考[Notification Kit通知样式](<../../../应用服务/Notification Kit（用户通知服务）/Notification Kit简介/notification-overview.md#通知样式>)中的文本类型。

## 模拟器支持情况

从API version 20开始，本能力支持模拟器开发。

## 接口说明

以下是代理提醒的相关接口，下表均以Promise形式为例，更多接口及使用方式请见[后台代理提醒](<../../../../harmonyos-references/Background Tasks Kit（后台任务开发服务）/ArkTS API/@ohos.reminderAgentManager (后台代理提醒)/js-apis-reminderagentmanager.md>)文档。

**表1** 主要接口

| 接口名 | 描述 |
| --- | --- |
| publishReminder(reminderReq: ReminderRequest): Promise<number> | 发布后台代理提醒。 |
| cancelReminder(reminderId: number): Promise<void> | 取消指定id的代理提醒。 |
| getValidReminders(): Promise<Array<ReminderRequest>> | 获取当前应用设置的所有[有效（未过期）的代理提醒](agent-powered-reminder.md#约束与限制)。 |
| cancelAllReminders(): Promise<void> | 取消当前应用设置的所有代理提醒。 |
| addNotificationSlot(slot: NotificationSlot): Promise<void> | 添加通知渠道。 |
| removeNotificationSlot(slotType: notification.SlotType): Promise<void> | 删除指定的通知渠道类型。 |

## 开发步骤

### 代理提醒开放能力申请

1. 登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)，选择“开发与服务”。
2. 在项目列表中找到您的项目，在项目下的应用列表中选择需要申请代理提醒的应用。如果无对应应用，请先[创建HarmonyOS应用](https://developer.huawei.com/consumer/cn/doc/app/agc-help-create-app-0000002247955506)。
3. 进入“项目设置”->“开放能力管理”页面，点击“代理提醒”卡片对应的“申请”按钮。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/23/v3/WqZJZQxQSIOgDe3G-iyKiA/zh-cn_image_0000002622858103.png?HW-CC-KV=V1&HW-CC-Date=20260611T063623Z&HW-CC-Expire=86400&HW-CC-Sign=344066DD68AFAF5682F80FBCF2A9B61AFA830351AACF09B14D9A72770E0AE1CA)
4. 在“新建业务申请”窗口填写申请原因，上传代理提醒功能场景截图和应用分类信息截图，然后点击“提交”。应用分类信息可登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)网站，在“APP”页签中选择“应用上架”->“应用信息”查询。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/30/v3/aO-yt0WZQqCgkCz6yq9zqw/zh-cn_image_0000002622698225.png?HW-CC-KV=V1&HW-CC-Date=20260611T063623Z&HW-CC-Expire=86400&HW-CC-Sign=64BF46C2E82E5FD84BC1B42F7127945FA405D1E063601D9696A573A3D5E24FC5)
5. 返回“开放能力接入”页面，原“申请”按钮变为“申请中”，8个工作日反馈申请结果。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2a/v3/mGhRTfaxSyCN_GlhFdDKnQ/zh-cn_image_0000002592218664.png?HW-CC-KV=V1&HW-CC-Date=20260611T063623Z&HW-CC-Expire=86400&HW-CC-Sign=047E8443608E31F235D7E7FFB9875A19CC33AED140660B0000AD3FB05FC1E20C)
6. 申请审批通过后，互动中心会发送通知给您，同时“申请中”按钮会变为置灰显示的“申请”。
7. 能力申请通过后，勾选代理提醒的能力开关，点击右上角“保存”。至此，您的应用已成功接入开放能力。此时，调试和发布应用必须重新生成Profile文件并使用[手动签名](../../../编写与调试应用/配置调试签名/ide-signing.md)。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c3/v3/5D5BAmVyTLm-FdVeRISHjQ/zh-cn_image_0000002592378598.png?HW-CC-KV=V1&HW-CC-Date=20260611T063623Z&HW-CC-Expire=86400&HW-CC-Sign=A9F86C0F5797DE9E717A1D74DFBB9ACBA7E10869615665543D1A119EE8CBF69C)

### 申请权限

申请ohos.permission.PUBLISH\_AGENT\_REMINDER权限，配置方式请参阅[声明权限](../../../系统/安全/程序访问控制/应用权限管控/申请应用权限/声明权限/declare-permissions.md)。

### 请求通知授权

[请求通知授权](<../../../应用服务/Notification Kit（用户通知服务）/请求通知授权/notification-enable.md>)。获得用户授权后，才能使用代理提醒功能。

### 功能开发

1. 导入模块。

   ```
   1. import { notificationManager } from '@kit.NotificationKit';
   2. import { reminderAgentManager } from '@kit.BackgroundTasksKit';
   3. import { BusinessError } from '@kit.BasicServicesKit';
   ```

   [Timer.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/BackGroundTasksKit/ReminderAgentManager/entry/src/main/ets/pages/timer/Timer.ets#L16-L20)
2. 定义目标提醒代理。开发者根据实际需要，选择定义如下类型的提醒。

   * 定义倒计时实例。

     ```
     1. let timer: reminderAgentManager.ReminderRequestTimer = {
     2. reminderType: reminderAgentManager.ReminderType.REMINDER_TYPE_TIMER, // 提醒类型为倒计时类型
     3. ringDuration: Constant.REMINDER_DURATION, // 指明响铃时长和振动时长（单位：秒）
     4. title: context.resourceManager.getStringSync($r('app.string.timer')
     5. .id), // 指明提醒标题, "app.string.timer"资源文件中的value值为"计时器"
     6. content: context.resourceManager.getStringSync($r('app.string.countdown_close')
     7. .id), // 指明提醒内容, "app.string.countdown_close"资源文件中的value值为"计时器已结束"
     8. wantAgent: {
     9. // 点击提醒通知后跳转的目标UIAbility信息
     10. pkgName: 'com.example.reminderagentmanager',
     11. abilityName: 'EntryAbility'
     12. },
     13. notificationId: 100, // 指明提醒使用的通知的ID号，相同ID号的提醒会覆盖
     14. slotType: notificationManager.SlotType.CONTENT_INFORMATION, // 指明提醒的Slot类型
     15. triggerTimeInSeconds: this.countdownTime
     16. };
     ```

     [Timer.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/BackGroundTasksKit/ReminderAgentManager/entry/src/main/ets/pages/timer/Timer.ets#L247-L264)
   * 定义日历实例。

     ```
     1. let calendar: reminderAgentManager.ReminderRequestCalendar = {
     2. reminderType: reminderAgentManager.ReminderType.REMINDER_TYPE_CALENDAR, // 提醒类型为日历类型
     3. dateTime: {
     4. // 指明提醒的目标时间
     5. year: date.getFullYear(),
     6. month: date.getUTCMonth() + 1,
     7. day: date.getDate(),
     8. hour: date.getHours(),
     9. minute: date.getMinutes(),
     10. },
     11. actionButton: // 设置弹出的提醒通知信息上显示的按钮类型和标题
     12. [{
     13. title: context.resourceManager.getStringSync($r('app.string.calendar_close')
     14. .id), // "app.string.calendar_close"资源文件中的value值为"关闭日历提醒"
     15. type: reminderAgentManager.ActionButtonType.ACTION_BUTTON_TYPE_CLOSE
     16. }],
     17. // 点击提醒通知后跳转的目标UIAbility信息
     18. wantAgent: { pkgName: 'com.example.reminderagentmanager', abilityName: 'EntryAbility' },
     19. ringDuration: Constant.REMINDER_DURATION, // 指明响铃时长和振动时长（单位：秒）
     20. title: context.resourceManager.getStringSync($r('app.string.calendar')
     21. .id), // 指明提醒标题, "app.string.calendar"资源文件中的value值为"日历"
     22. content: context.resourceManager.getStringSync($r('app.string.calendar_reach')
     23. .id), // 指明提醒内容, "app.string.calendar_reach"资源文件中的value值为"日历提醒时间到了"
     24. slotType: notificationManager.SlotType.CONTENT_INFORMATION  // 指明提醒的Slot类型
     25. }
     ```

     [CalendarReminder.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/BackGroundTasksKit/ReminderAgentManager/entry/src/main/ets/util/CalendarReminder.ets#L59-L85)
   * 定义闹钟实例。

     ```
     1. let alarm: reminderAgentManager.ReminderRequestAlarm = {
     2. reminderType: reminderAgentManager.ReminderType.REMINDER_TYPE_ALARM, // 提醒类型为闹钟类型
     3. hour: time.hour, // 指明提醒的目标时刻
     4. minute: time.minute, // 指明提醒的目标分钟
     5. actionButton: // 设置弹出的提醒通知信息上显示的按钮类型和标题
     6. [
     7. {
     8. title: context.resourceManager.getStringSync($r('app.string.alarm_clock_close')
     9. .id), // "app.string.alarm_clock_close"资源文件中的value值为"关闭闹钟"
     10. type: reminderAgentManager.ActionButtonType.ACTION_BUTTON_TYPE_CLOSE
     11. },
     12. {
     13. title: context.resourceManager.getStringSync($r('app.string.alarm_clock_postpone')
     14. .id), // "app.string.alarm_clock_postpone"资源文件中的value值为"推迟闹钟"
     15. type: reminderAgentManager.ActionButtonType.ACTION_BUTTON_TYPE_SNOOZE
     16. }
     17. ],
     18. slotType: notificationManager.SlotType.CONTENT_INFORMATION, // 指明提醒的Slot类型
     19. ringDuration: Constant.REMINDER_DURATION, // 指明响铃时长和振动时长（单位：秒）
     20. wantAgent: {
     21. // 点击提醒通知后跳转的目标UIAbility信息
     22. pkgName: 'com.example.reminderagentmanager',
     23. abilityName: 'EntryAbility'
     24. },
     25. title: context.resourceManager.getStringSync($r('app.string.alarm_clock')
     26. .id), // 指明提醒标题, "app.string.alarm_clock"资源文件中的value值为"闹钟"
     27. content: context.resourceManager.getStringSync($r('app.string.alarm_clock_reach')
     28. .id), // 指明提醒内容, "app.string.alarm_clock_reach"资源文件中的value值为"闹钟时间已到"
     29. snoozeTimes: 0, // 指明延迟提醒次数
     30. timeInterval: 0, // 执行延迟提醒间隔（单位：秒）
     31. daysOfWeek: []  // 指明每周哪几天需要重复提醒
     32. }
     ```

     [AlarmClockReminder.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/BackGroundTasksKit/ReminderAgentManager/entry/src/main/ets/util/AlarmClockReminder.ets#L59-L92)
3. 发布相应的提醒代理。代理发布后，应用即可使用后台代理提醒功能。

   ```
   1. let reminderId: number = await reminderAgentManager.publishReminder(
   2. this.calendarReminders[index].reminderRequestCalendar!);
   3. Logger.info(TAG, `publish reminder result: id is ${reminderId}`);
   4. this.calendarReminders[index].reminderId = reminderId;  // 保存发布的提醒ID
   ```

   [CalendarReminder.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/BackGroundTasksKit/ReminderAgentManager/entry/src/main/ets/util/CalendarReminder.ets#L109-L114)
4. 根据需要删除提醒任务。

   ```
   1. Logger.info(TAG, `cancel reminder id is ${this.calendarReminders[index].reminderId}`)
   2. await reminderAgentManager.cancelReminder(this.calendarReminders[index].reminderId);
   ```

   [CalendarReminder.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/BackGroundTasksKit/ReminderAgentManager/entry/src/main/ets/util/CalendarReminder.ets#L162-L165)
