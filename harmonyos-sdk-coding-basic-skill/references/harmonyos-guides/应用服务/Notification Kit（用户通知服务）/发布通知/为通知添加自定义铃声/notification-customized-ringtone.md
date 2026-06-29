---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/notification-customized-ringtone
title: 为通知添加自定义铃声
breadcrumb: 指南 > 应用服务 > Notification Kit（用户通知服务） > 发布通知 > 为通知添加自定义铃声
category: harmonyos-guides
scraped_at: 2026-06-01T15:07:42+08:00
doc_updated_at: 2026-05-26
content_hash: sha256:229d3b57e081589876acd8677bca2775c4478c22d1d00c9a58cd0d4d1d020ed8
---
从API version 12开始，应用发布通知时，可以使用自定义的通知铃声，该铃声的音频资源需要预置在应用中。从API version 24开始，系统增强了该字段的能力，应用可以使用非预置的音频资源作为通知铃声，比如从网络下载或者用户生成的音频资源。

## 接口说明

自定义铃声可通过[NotificationRequest](<../../../../../harmonyos-references/Notification Kit（用户通知服务）/ArkTS API/notification/NotificationRequest/js-apis-inner-notification-notificationrequest.md#notificationrequest-1>)携带sound字段来指定，不指定该字段默认为系统铃声。

* 资源文件：应用预置的音频文件，资源文件必须放在放在resources/rawfile目录下，使用时直接传入文件名。
* 沙箱文件：网络下载或者用户生成的音频文件，必须放在[沙箱文件目录](<../../../../应用框架/Core File Kit（文件基础服务）/应用文件/应用沙箱目录/app-sandbox-directory.md#应用文件目录与应用文件路径>)EL1区域的files目录或者其子目录下，传入格式为uri::{fileUri}，其中fileUri是通过[getUriFromPath](<../../../../../harmonyos-references/Core File Kit（文件基础服务）/ArkTS API/@ohos.file.fileuri (文件URI)/js-apis-file-fileuri.md#fileurigeturifrompath>)获取的路径。

支持m4a、aac、mp3、ogg、wav、flac、amr等格式。

**表1** 通知发布接口功能介绍

| 接口名 | 描述 |
| --- | --- |
| [publish(request: NotificationRequest): Promise<void>](<../../../../../harmonyos-references/Notification Kit（用户通知服务）/ArkTS API/@ohos.notificationManager (NotificationManager模块)/js-apis-notificationmanager.md#notificationmanagerpublish-1>) | 发布通知。 |

## 开发步骤

1. 导入模块。

   ```
   1. import { notificationManager } from '@kit.NotificationKit';
   2. import { BusinessError } from '@kit.BasicServicesKit';
   3. import { hilog } from '@kit.PerformanceAnalysisKit';
   4. import { contextConstant, common } from '@kit.AbilityKit';
   5. import { fileIo as fs, fileUri } from '@kit.CoreFileKit';

   7. const TAG: string = '[SpecifiedCustomizedRingtone]';
   8. const DOMAIN_NUMBER: number = 0xFF00;
   9. const SOUND_FILE_NAME: string = 'ringtone_demo.mp3'; // 实际项目中请替换为自己的音频文件
   ```
2. 准备音频资源。

   场景一：使用应用预置的音频资源作为通知铃声。

   (1) 将音频资源放入项目的resources/rawfile目录下。

   (2) 创建发布通知的sound信息。

   ```
   1. let soundFile: string = SOUND_FILE_NAME; // 需要替换为resources/rawfile目录下对应的音频文件
   ```

   场景二：使用沙箱内音频资源作为通知铃声。

   (1) 生成沙箱内音频资源路径。

   ```
   1. // 生成沙箱内音频资源路径
   2. const uiContext: UIContext = this.getUIContext();
   3. let context: Context | undefined = uiContext.getHostContext() as common.UIAbilityContext;
   4. if (!context) {
   5. hilog.error(DOMAIN_NUMBER, TAG, 'Context is not initialized.');
   6. return;
   7. }
   8. const applicationContext: common.ApplicationContext = context.getApplicationContext();
   9. applicationContext.area = contextConstant.AreaMode.EL1; // 必须在EL1沙箱下
   10. const sandboxDir: string = applicationContext.filesDir;
   11. let sandboxFilePath: string = sandboxDir + '/' + SOUND_FILE_NAME;
   ```

   (2) 将网络下载或者用户生成的音频资源放在[沙箱文件目录](<../../../../应用框架/Core File Kit（文件基础服务）/应用文件/应用沙箱目录/app-sandbox-directory.md#应用文件目录与应用文件路径>)EL1区域的files目录下或者其子目录下，下面示例展示了如何将resources/rawfile目录下的音频资源拷贝到指定沙箱目录。

   ```
   1. // 拷贝resources/rawfile/目录下的音频文件到应用沙箱EL1的files目录下
   2. try {
   3. let rawFileData: Uint8Array = context.resourceManager.getRawFileContentSync(SOUND_FILE_NAME);
   4. if (!fs.accessSync(sandboxDir)) {
   5. fs.mkdirSync(sandboxDir, true);
   6. }
   7. const file = fs.openSync(sandboxFilePath, fs.OpenMode.CREATE | fs.OpenMode.WRITE_ONLY);
   8. fs.writeSync(file.fd, rawFileData.buffer);
   9. fs.closeSync(file);
   10. hilog.info(DOMAIN_NUMBER, TAG, 'copy file to sandbox success.');
   11. } catch (error) {
   12. hilog.error(DOMAIN_NUMBER, TAG, `copy file to sandbox error: ${JSON.stringify(error)}`);
   13. return;
   14. }
   ```

   (3) 创建发布通知的sound信息。

   ```
   1. // 获取沙箱文件uri
   2. let sandboxFileUri: string = fileUri.getUriFromPath(sandboxFilePath)
   3. let soundFile: string = 'uri::' + sandboxFileUri; // 必须以uri::开头，且路径中不能包含'../'和'/..'
   ```
3. 发布携带自定义铃声的通知。

   ```
   1. let notificationRequest: notificationManager.NotificationRequest = {
   2. id: 0,
   3. notificationSlotType: notificationManager.SlotType.SOCIAL_COMMUNICATION,
   4. content: {
   5. notificationContentType: notificationManager.ContentType.NOTIFICATION_CONTENT_BASIC_TEXT,
   6. normal: {
   7. title: 'title',
   8. text: 'text',
   9. additionalText: 'test_additionalText'
   10. }
   11. },
   12. sound: soundFile
   13. }

   15. notificationManager.publish(notificationRequest).then(() => {
   16. hilog.info(DOMAIN_NUMBER, TAG, 'Succeeded in publishing notification.');
   17. }).catch((err: BusinessError) => {
   18. hilog.error(DOMAIN_NUMBER, TAG, `Failed to publish notification. Code is ${err.code}, message is ${err.message}`);
   19. });
   ```

## 约束限制

* 应用使用非预置的音频资源作为通知铃声，发布通知时，[NotificationRequest](<../../../../../harmonyos-references/Notification Kit（用户通知服务）/ArkTS API/notification/NotificationRequest/js-apis-inner-notification-notificationrequest.md#notificationrequest-1>)携带sound字段指定的uri资源路径中不能包含"../"或者"/.."，并且必须以"uri::"开始。
* 应用使用非预置的音频资源作为通知铃声，音频资源必须放在应用沙箱EL1区域files目录下。
