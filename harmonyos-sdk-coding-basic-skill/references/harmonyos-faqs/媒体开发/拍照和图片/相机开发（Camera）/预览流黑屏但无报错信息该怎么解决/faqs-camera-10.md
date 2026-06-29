---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-camera-10
title: 预览流黑屏但无报错信息该怎么解决
breadcrumb: FAQ > 媒体开发 > 拍照和图片 > 相机开发（Camera） > 预览流黑屏但无报错信息该怎么解决
category: harmonyos-faqs
scraped_at: 2026-06-12T10:38:38+08:00
doc_updated_at: 2026-05-15
content_hash: sha256:34db0c297a5e99954a95e7a8c677a66d0b2d6f452e66052e3f8e236271781bc9
---
**可能原因**

* 未正确获取相机权限的情况下，进行相机初始化和相机输入流获取等操作。
* 应用切换到后台再返回时，相机资源被回收，未重新获取权限并开启预览导致。
* 配置的预览流尺寸不被支持。

**解决措施**

* 确保在初始化相机和获取相机输入流之前，先正确获取相机权限。
  1. 首先在module.json5文件中申请需要的权限（地理位置权限可以根据需要申请，非必选）；

     ```
     1. "requestPermissions": [
     2. {
     3. "name": "ohos.permission.CAMERA",
     4. "usedScene": {
     5. "abilities": [
     6. "FormAbility"
     7. ],
     8. "when": "always"
     9. },
     10. "reason": "$string:Camera_Permission_Request"
     11. },
     12. {
     13. "name": "ohos.permission.MICROPHONE",
     14. "usedScene": {
     15. "abilities": [
     16. "FormAbility"
     17. ],
     18. "when": "always"
     19. },
     20. "reason": "$string:Camera_Permission_Request"
     21. },
     22. // The geographical location permission can be applied for as required. This parameter is optional.
     23. {
     24. "name": "ohos.permission.MEDIA_LOCATION",
     25. "usedScene": {
     26. "abilities": [
     27. "FormAbility"
     28. ],
     29. "when": "always"
     30. },
     31. "reason": "$string:Camera_Permission_Request"
     32. }
     33. ],
     ```

     [module.json5](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/CameraKit/entry/src/main/module.json5#L56-L88)
  2. 接着在EntryAbility.ets中onWindowStageCreate中使用[requestPermissionsFromUser](<../../../../../harmonyos-references/Ability Kit（程序框架服务）/ArkTS API/通用能力的接口(推荐)/@ohos.abilityAccessCtrl (程序访问控制管理)/js-apis-abilityaccessctrl.md#requestpermissionsfromuser9>)方法获取权限。

     ```
     1. onWindowStageCreate(windowStage: window.WindowStage): void {
     2. let atManager = abilityAccessCtrl.createAtManager();
     3. atManager.requestPermissionsFromUser(this.context,
     4. [
     5. 'ohos.permission.CAMERA',
     6. 'ohos.permission.MICROPHONE',
     7. 'ohos.permission.MEDIA_LOCATION'
     8. ]
     9. ).then((data) => {
     10. console.info('data:' + JSON.stringify(data));
     11. console.info('data permissions:' + data.permissions);
     12. console.info('data authResults:' + data.authResults);
     13. // Main window is created, set main page for this ability
     14. hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onWindowStageCreate');

     16. windowStage.loadContent('pages/CameraPreviewFlow', (err, data) => {
     17. if (err.code) {
     18. hilog.error(0x0000, 'testTag', 'Failed to load the content. Cause: %{public}s', JSON.stringify(err) ?? '');
     19. return;
     20. }
     21. hilog.info(0x0000, 'testTag', 'Succeeded in loading the content. Data: %{public}s', JSON.stringify(data) ?? '');
     22. });
     23. }).catch((err: BusinessError) => {
     24. console.info('data:' + JSON.stringify(err));
     25. });
     26. }
     ```

     [EntryAbility.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/CameraKit/entry/src/main/ets/entryability/EntryAbility.ets#L27-L52)
* 当应用被切换到后台后，相机资源会被全部回收，所以为了避免出现前后台切换时预览流黑屏的问题，需在onPageShow中进行重新创建会话、配置会话、启动等操作，并在onPageHide中对相机资源进行释放。

  ```
  1. async onPageShow() {
  2. let baseContext = this.getUIContext().getHostContext()! as common.BaseContext;
  3. await this.initCamera(baseContext, this.surfaceId);
  4. }

  6. async onPageHide() {
  7. await this.releaseCamera();
  8. }
  ```

  [ResolvePreviewStreamBlackScreenIssuePage.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/CameraKit/entry/src/main/ets/pages/ResolvePreviewStreamBlackScreenIssuePage.ets#L28-L35)
* 获取相机设备支持的输出流能力，确定支持的预览尺寸。

  ```
  1. // Obtain the output stream capability supported by the camera device
  2. let cameraOutputCap: camera.CameraOutputCapability =
  3. cameraManager.getSupportedOutputCapability(cameraArray[0], camera.SceneMode.NORMAL_PHOTO);
  4. if (!cameraOutputCap) {
  5. console.error(TAG, "cameraManager.getSupportedOutputCapability error");
  6. return;
  7. }
  8. console.info(TAG, "outputCapability: " +
  9. JSON.stringify(cameraOutputCap));  //The aspect ratio of the preview stream and the video output stream resolution should be consistent
  10. let previewProfilesArray: Array<camera.Profile> = cameraOutputCap.previewProfiles;
  11. let position: number = 0;
  12. if (previewProfilesArray != null) {
  13. previewProfilesArray.forEach((value: camera.Profile,
  14. index: number) => { // View supported preview sizes
  15. console.info(TAG,
  16. `Supported preview sizes: [${value.size.width},${value.size.height},${value.size.width / value.size.height}]`);
  17. if (value.size.width === 2592 && value.size.height === 1200) {
  18. position = index;
  19. }
  20. })
  21. } else {
  22. console.error(TAG, "createOutput photoProfilesArray == null || undefined");
  23. }
  ```

  [ResolvePreviewStreamBlackScreenIssue.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/CameraKit/entry/src/main/ets/pages/ResolvePreviewStreamBlackScreenIssue.ets#L29-L51)
