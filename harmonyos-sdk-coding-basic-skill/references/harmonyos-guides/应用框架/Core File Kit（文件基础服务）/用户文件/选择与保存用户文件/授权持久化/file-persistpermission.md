---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/file-persistpermission
title: 授权持久化
breadcrumb: 指南 > 应用框架 > Core File Kit（文件基础服务） > 用户文件 > 选择与保存用户文件 > 授权持久化
category: harmonyos-guides
scraped_at: 2026-06-01T11:11:06+08:00
doc_updated_at: 2026-05-26
content_hash: sha256:2b5b44220524cea9af0351192a6bd35406be122051da57967c4ec1e7bf5d772b
---
## 场景介绍

应用可以通过Picker[选择文件](../选择用户文件/select-user-file.md)或[保存文件](../保存用户文件/save-user-file.md)获取到临时授权，临时授权在应用退出后或者设备重启后会清除。如果应用重启或者设备重启后需要直接访问之前已访问过的文件，则需要对文件进行持久化授权。

## 通过Picker获取临时授权并进行授权持久化

通过Picker选择文件或文件夹进行临时授权，该方式获取到的URI只具有**临时读写权限**。应用后续可按需通过文件分享接口（[ohos.fileshare](<../../../../../../harmonyos-references/Core File Kit（文件基础服务）/ArkTS API/@ohos.fileshare (文件分享)/js-apis-fileshare.md>)）进行持久化授权。

1.应用仅临时需要访问公共目录的数据，例如：通讯类应用需要发送用户的文件或者图片。应用调用Picker的([select](<../../../../../../harmonyos-references/Core File Kit（文件基础服务）/ArkTS API/@ohos.file.picker (选择器)/js-apis-file-picker.md#select-3>))接口选择需要发送的文件或者图片，此时应用获取到是该文件的临时访问权限，应用重启或者设备重启后，再次访问该文件则仍需使用Picker进行文件选择。

2.应用如果需要长期访问某个文件或目录时，可以通过Picker选择文件或文件夹进行临时授权，然后利用persistPermission接口（[ohos.fileshare.persistPermission](<../../../../../../harmonyos-references/Core File Kit（文件基础服务）/ArkTS API/@ohos.fileshare (文件分享)/js-apis-fileshare.md#filesharepersistpermission11>)）对授权进行持久化（在授权方同意被持久化的情况下，例如使用Picker选择文件场景，Picker会将权限授予当前应用，即可进行授权持久化），例如：文档编辑类应用本次编辑完一个用户文件，期望在历史记录中可以直接选中打开，无需再拉起Picker进行选择授权。

可使用canIUse接口，确认设备是否具有以下系统能力：SystemCapability.FileManagement.AppFileService.FolderAuthorization。

```
1. if (!canIUse('SystemCapability.FileManagement.AppFileService.FolderAuthorization')) {
2. console.error('this api is not supported on this device');
3. return;
4. }
```

**需要权限**

ohos.permission.FILE\_ACCESS\_PERSIST，具体参考[访问控制-申请应用权限](../../../../../系统/安全/程序访问控制/应用权限管控/申请应用权限/选择申请权限的方式/determine-application-mode.md)。

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { picker } from '@kit.CoreFileKit';
3. import { fileShare } from '@kit.CoreFileKit';

5. export async function persistPermissionExample() {
6. try {
7. // ...
8. let documentSelectOptions = new picker.DocumentSelectOptions();
9. let documentPicker = new picker.DocumentViewPicker();
10. let uris = await documentPicker.select(documentSelectOptions);
11. // 可以组合授予多个权限，例如读写权限可使用 fileShare.OperationMode.READ_MODE | fileShare.OperationMode.WRITE_MODE。
12. // 注意：只能对已获取到的临时权限进行持久化授权操作，否则会报错。
13. let policyInfo: fileShare.PolicyInfo = {
14. uri: uris[0],
15. operationMode: fileShare.OperationMode.READ_MODE,
16. };
17. let policies: fileShare.PolicyInfo[] = [policyInfo];
18. fileShare.persistPermission(policies).then(() => {
19. console.info('persistPermission successfully');
20. }).catch((err: BusinessError<Array<fileShare.PolicyErrorResult>>) => {
21. console.error('persistPermission failed with error message: ' + err.message + ', error code: ' + err.code);
22. if (err.code == 13900001 && err.data) {
23. for (let i = 0; i < err.data.length; i++) {
24. console.error('error code : ' + JSON.stringify(err.data[i].code));
25. console.error('error uri : ' + JSON.stringify(err.data[i].uri));
26. console.error('error reason : ' + JSON.stringify(err.data[i].message));
27. }
28. }
29. });
30. } catch (error) {
31. let err: BusinessError = error as BusinessError;
32. console.error(`persistPermission failed with err, Error code: ${err.code}, message: ${err.message}`);
33. }
34. }
```

[PersistPermission.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/CoreFile/PersistPermission/entry/src/main/ets/persistpermission/PersistPermission.ets#L17-L59)

注意

1. 持久化授权文件信息建议应用在本地存储数据，供后续按需激活持久化文件。
2. 持久化授权的数据存储在系统的数据库中，应用或者设备重启后需要激活已持久化的授权才可以正常使用[激活持久化授权](file-persistpermission.md#激活已经持久化的权限访问文件或目录)。
3. 持久化权限接口(可以使用canIUse接口进行校验能力是否可用)，且需要申请对应的权限。
4. 应用在卸载时会将之前的授权数据全部清除，重新安装后需要重新授权。
5. 只能对已获取到的临时权限进行持久化授权操作，否则会报错。

**备注**：C/C++持久化授权接口说明及开发指南具体参考：[OH\_FileShare\_PersistPermission持久化授权接口](../授权持久化(CC++)/native-fileshare-guidelines.md)。

3.可以通过revokePermission接口（[ohos.fileshare.revokePermission](<../../../../../../harmonyos-references/Core File Kit（文件基础服务）/ArkTS API/@ohos.fileshare (文件分享)/js-apis-fileshare.md#filesharerevokepermission11>)）对已持久化的文件取消授权，同时更新应用存储的数据以删除最近访问数据。

**需要权限**

ohos.permission.FILE\_ACCESS\_PERSIST，具体参考[访问控制-申请应用权限](../../../../../系统/安全/程序访问控制/应用权限管控/申请应用权限/选择申请权限的方式/determine-application-mode.md)。

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { picker } from '@kit.CoreFileKit';
3. import { fileShare } from '@kit.CoreFileKit';

5. // ...
6. export async function revokePermissionExample() {
7. try {
8. let uri = 'file://docs/storage/Users/username/tmp.txt';
9. // 可以组合取消多个权限，例如读写权限可使用 fileShare.OperationMode.READ_MODE | fileShare.OperationMode.WRITE_MODE。
10. // 注意：只能对已获取到的持久化权限进行取消持久化授权操作，否则会报错。
11. let policyInfo: fileShare.PolicyInfo = {
12. uri: uri,
13. operationMode: fileShare.OperationMode.READ_MODE,
14. };
15. let policies: fileShare.PolicyInfo[] = [policyInfo];
16. fileShare.revokePermission(policies).then(() => {
17. console.info('revokePermission successfully');
18. }).catch((err: BusinessError<Array<fileShare.PolicyErrorResult>>) => {
19. console.error('revokePermission failed with error message: ' + err.message + ', error code: ' + err.code);
20. if (err.code == 13900001 && err.data) {
21. for (let i = 0; i < err.data.length; i++) {
22. console.error('error code : ' + JSON.stringify(err.data[i].code));
23. console.error('error uri : ' + JSON.stringify(err.data[i].uri));
24. console.error('error reason : ' + JSON.stringify(err.data[i].message));
25. }
26. }
27. });
28. } catch (error) {
29. let err: BusinessError = error as BusinessError;
30. console.error(`revokePermission failed with err, Error code: ${err.code}, message: ${err.message}`);
31. }
32. }
```

[PersistPermission.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/CoreFile/PersistPermission/entry/src/main/ets/persistpermission/PersistPermission.ets#L16-L86)

注意

1. 示例中的URI来源自应用存储的持久化数据中。
2. 只能对已获取到的持久化权限进行取消持久化授权操作，建议按照使用需求去取消对应的持久化权限。
3. 持久化权限接口(可以使用canIUse接口进行校验能力是否可用)，且需要申请对应的权限。

**备注**：C/C++去持久化授权接口说明及开发指南具体参考：[OH\_FileShare\_RevokePermission去持久化授权接口](../授权持久化(CC++)/native-fileshare-guidelines.md)。

## 激活已经持久化的权限访问文件或目录

对于应用已经持久化的授权，应用每次启动时实际未加载到内存中，需要应用按需进行手动激活已持久化授权的权限，通过activatePermission接口（[ohos.fileshare.activatePermission](<../../../../../../harmonyos-references/Core File Kit（文件基础服务）/ArkTS API/@ohos.fileshare (文件分享)/js-apis-fileshare.md#fileshareactivatepermission11>)）对已经持久化授权的权限进行使能操作，否则已经持久化授权的权限仍存在不能使用的情况。

**需要权限**

ohos.permission.FILE\_ACCESS\_PERSIST，具体参考[访问控制-申请应用权限](../../../../../系统/安全/程序访问控制/应用权限管控/申请应用权限/选择申请权限的方式/determine-application-mode.md)。

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { picker } from '@kit.CoreFileKit';
3. import { fileShare } from '@kit.CoreFileKit';

5. // ...
6. export async function activatePermissionExample() {
7. try {
8. let uri = 'file://docs/storage/Users/username/tmp.txt';
9. // 可以组合激活多个权限，例如读写权限可使用 fileShare.OperationMode.READ_MODE | fileShare.OperationMode.WRITE_MODE。
10. // 注意：只能对已获取到的持久化权限进行激活持久化授权操作，否则会报错。
11. let policyInfo: fileShare.PolicyInfo = {
12. uri: uri,
13. operationMode: fileShare.OperationMode.READ_MODE,
14. };
15. let policies: fileShare.PolicyInfo[] = [policyInfo];
16. fileShare.activatePermission(policies).then(() => {
17. console.info('activatePermission successfully');
18. }).catch((err: BusinessError<Array<fileShare.PolicyErrorResult>>) => {
19. console.error('activatePermission failed with error message: ' + err.message + ', error code: ' + err.code);
20. if (err.code == 13900001 && err.data) {
21. for (let i = 0; i < err.data.length; i++) {
22. console.error('error code : ' + JSON.stringify(err.data[i].code));
23. console.error('error uri : ' + JSON.stringify(err.data[i].uri));
24. console.error('error reason : ' + JSON.stringify(err.data[i].message));
25. if (err.data[i].code == fileShare.PolicyErrorCode.PERMISSION_NOT_PERSISTED) {
26. // 可以选择进行持久化后再激活。
27. }
28. }
29. }
30. });
31. } catch (error) {
32. let err: BusinessError = error as BusinessError;
33. console.error(`activatePermission failed with err, Error code: ${err.code}, message: ${err.message}`);
34. }
35. }
```

[PersistPermission.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/CoreFile/PersistPermission/entry/src/main/ets/persistpermission/PersistPermission.ets#L15-L116)

注意

1. 示例中的URI来源自应用存储的持久化数据中。
2. 建议按照使用需求去激活对应的持久化权限，不要盲目的全量激活。
3. 如果激活失败显示未持久化的权限可以按照示例进行持久化。
4. 持久化权限接口可以使用canIUse接口进行校验能力是否可用，且需要申请对应的权限。

**备注**：C/C++持久化授权激活接口说明及开发指南具体参考：[OH\_FileShare\_ActivatePermission持久化授权激活接口](../授权持久化(CC++)/native-fileshare-guidelines.md)。

## 持久化权限保留配置

从API version 24开始，系统新增支持持久化权限保留能力。应用卸载时根据ohos.fileshare.supportPreservePersistentPermission标签保留持久化。再次安装时恢复上次已保留的持久化权限。

### 配置方式

开发者可在应用模块级配置文件[src/main/module.json5](../../../../../基础入门/开发基础知识/应用配置文件（Stage模型）/module.json5配置文件/module-configuration-file.md)的module标签中metadata里配置ohos.fileshare.supportPreservePersistentPermission标签，以启用持久化权限保留能力。

**metadata标签配置示例**

```
1. {
2. "module": {
3. // ...
4. "metadata": [
5. {
6. "name": "ohos.fileshare.supportPreservePersistentPermission"
7. }
8. ],
9. // ...
10. }
11. }
```

**ohos.fileshare.supportPreservePersistentPermission标签说明**

| 属性名称 | 含义 | 数据类型 | 是否可缺省 |
| --- | --- | --- | --- |
| name | 标识元信息名称，固定值为ohos.fileshare.supportPreservePersistentPermission。 | 字符串 | 该标签不可缺省。 |
