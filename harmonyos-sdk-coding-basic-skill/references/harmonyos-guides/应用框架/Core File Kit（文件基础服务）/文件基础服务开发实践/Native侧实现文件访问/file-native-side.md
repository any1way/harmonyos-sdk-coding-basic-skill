---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/file-native-side
title: Native侧实现文件访问
breadcrumb: 指南 > 应用框架 > Core File Kit（文件基础服务） > 文件基础服务开发实践 > Native侧实现文件访问
category: harmonyos-guides
scraped_at: 2026-06-11T14:37:16+08:00
doc_updated_at: 2026-05-26
content_hash: sha256:4dd036e8f12f4437d8ac5485534432b22a0089c8d9f987a9c46a9d3240d2090b
---
## 概述

在对文件处理性能要求高的场景中，Native侧访问文件处理数据比在ArkTS侧操作文件（详见[应用文件访问(ArkTS)](../../应用文件/应用文件访问与管理/应用文件访问(ArkTS)/app-file-access.md)）有更高的效率和更快的响应，例如处理大文件、复杂的文件操作以及实时通信等低时延场景。根据文件位置的不同，应用在Native侧访问文件可以分为以下两种类型：

* 类型一：访问应用沙箱内的文件进行读写操作，主要是通过沙箱路径进行访问。
* 类型二：访问系统公共目录中的文件进行读写操作，可以使用文件picker来获取文件描述符。

本文将针对这两种场景给出具体的实现方案。

## 访问应用沙箱文件

应用沙箱（详见[应用沙箱目录](../../应用文件/应用沙箱目录/app-sandbox-directory.md)）是一种以安全防护为目的的隔离机制，避免数据受到恶意路径穿越访问。在这种沙箱的保护机制下，应用可见的目录范围即为“应用沙箱目录”，沙箱中的文件就需要通过沙箱路径去进行访问。Native侧获取沙箱路径的方案有两种：

* 方案一：ArkTS侧获取沙箱路径（详见[获取应用文件路径](<../../../Ability Kit（程序框架服务）/Stage模型开发指导/Stage模型应用组件/应用上下文Context/application-context-stage.md#获取应用文件路径>)）传递给Native侧访问文件。
* 方案二：Native侧直接拼接沙箱路径（详见[应用沙箱路径和真实物理路径的对应关系](../../应用文件/应用沙箱目录/app-sandbox-directory.md#应用沙箱路径和真实物理路径的对应关系)）访问文件。

### 方案一：ArkTS侧获取沙箱路径传递给Native侧访问文件

**图 1** ArkTS侧获取沙箱路径传递给Native侧访问文件示意图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c6/v3/HLn469eiRmqaabdm27sDWA/zh-cn_image_0000002592218688.png?HW-CC-KV=V1&HW-CC-Date=20260611T063712Z&HW-CC-Expire=86400&HW-CC-Sign=BEFAA2B5715C7ADE67B37F52532565E5620BA56426729994EB3C227F3AFECF67)

**实现方案**

这里以访问沙箱文件并写入文本的场景为例，实现方案分为Native侧定义操作文件的方法和ArkTS侧调用该方法两部分。

第一部分：在Native侧定义一个方法，用于接收沙箱路径并将文本写入到文件中。

1. 通过Node-API接口将沙箱路径和要写入文本的内容传递到Native侧。

   ```
   1. napi_get_value_string_utf8(env, argv[0], pathBuf, sizeof(pathBuf), &pathSize);
   2. napi_get_value_string_utf8(env, argv[1], contentsBuf, sizeof(contentsBuf), &contentsSize);
   ```
2. 通过指定的路径打开文件。

   ```
   1. FILE *fp;
   2. fp = fopen(pathBuf, "w");
   ```
3. 使用C标准库的文件操作函数写入文件。

   ```
   1. // Write a file using the file operation function of the C standard library.
   2. fprintf(fp, "%s", contentsBuf);
   ```
4. 完整代码如下所示：

   ```
   1. // entry/src/main/cpp/FileAccessMethods.cpp
   2. static napi_value TransferSandboxPath(napi_env env, napi_callback_info info) {
   3. size_t argc = 2;
   4. napi_value argv[2] = {nullptr};
   5. napi_get_cb_info(env, info, &argc, argv, nullptr, nullptr);
   6. // Convert the sandbox path and the contents of the text to be written into C-side variables through the Node-API interface.
   7. size_t pathSize, contentsSize;
   8. char pathBuf[BUFFER_SIZE], contentsBuf[BUFFER_SIZE];
   9. napi_get_value_string_utf8(env, argv[0], pathBuf, sizeof(pathBuf), &pathSize);
   10. napi_get_value_string_utf8(env, argv[1], contentsBuf, sizeof(contentsBuf), &contentsSize);
   11. // Open the file through the specified path.
   12. snprintf(pathBuf, sizeof(pathBuf), "%s/TransferSandboxPath.txt", pathBuf);
   13. FILE *fp;
   14. fp = fopen(pathBuf, "w");
   15. if (fp == nullptr) {
   16. OH_LOG_Print(LOG_APP, LOG_ERROR, DOMAIN, TAG, "Open file error!");
   17. return nullptr;
   18. }
   19. OH_LOG_Print(LOG_APP, LOG_INFO, DOMAIN, TAG, "Open file successfully!");
   20. // Write a file using the file operation function of the C standard library.
   21. fprintf(fp, "%s", contentsBuf);
   22. fclose(fp);
   23. return nullptr;
   24. }
   ```
5. 将该C++接口与ArkTS接口进行绑定和映射（详见[Native侧方法的实现](../../../../NDK开发/代码开发/使用Node-API实现ArkTSJS与CC++语言交互/使用Node-API实现跨语言交互开发流程/use-napi-process.md#native侧方法的实现)），同时在index.d.ts文件中，提供该接口方法以便于ArkTS侧调用。

   ```
   1. export const transferSandboxPath: (path: string, contents: string) => void;
   ```

第二部分：在Native侧访问沙箱文件写数据的功能实现后，在ArkTS侧调用该方法。

1. 引用Native侧相应的so库。

   ```
   1. import FileAccess from 'libfile_access.so';
   ```
2. 在ArkTS侧获取沙箱路径。

   ```
   1. private sandboxFilesDir: string = this.getUIContext().getHostContext()!.filesDir;
   ```
3. 获取到沙箱路径后，将该路径传递给Native侧，同时传递需要写入的内容。

   ```
   1. FileAccess.transferSandboxPath(this.sandboxFilesDir, content);
   ```

通过上述步骤，实现了在Native侧通过ArkTS侧传递的沙箱路径访问与操作应用沙箱文件的方案。

**效果展示**

**图 2** ArkTS侧传递沙箱路径到Native侧方案效果展示

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fe/v3/nTu4CEgcTtG6832YHB5-YQ/zh-cn_image_0000002592378622.png?HW-CC-KV=V1&HW-CC-Date=20260611T063712Z&HW-CC-Expire=86400&HW-CC-Sign=666E7E0CB99C472EC23BC3DE6B6F0A02A9322B015BC4E153594980F56A2D13E4)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d3/v3/NPXlxd9oSnyCitkHyZXDfg/zh-cn_image_0000002622858129.png?HW-CC-KV=V1&HW-CC-Date=20260611T063712Z&HW-CC-Expire=86400&HW-CC-Sign=CF6DFF5FB18E89BB25648C8895B7B37AE9CBBF87765047B0A1E7337EDE9FC5EB)

### 方案二：Native侧直接拼接沙箱路径访问文件

**图 3** Native侧直接拼接沙箱路径访问文件示意图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3d/v3/_1wO6egwS4iT4UGcbCvf7Q/zh-cn_image_0000002622698251.png?HW-CC-KV=V1&HW-CC-Date=20260611T063712Z&HW-CC-Expire=86400&HW-CC-Sign=0C87D55FE9D4D5F9DE0280415EEF43A5D5F1C144D7F3FD180CA4F6649B897568)

**实现方案**

这里同样以访问沙箱文件并写入文本的场景为例，实现方案分为Native侧定义操作文件的方法和ArkTS侧调用该方法两部分。

第一部分：在Native侧定义一个方法，用于拼接沙箱路径并将文本写入到文件中。

1. 根据实际文件位置拼接沙箱路径（详见[应用沙箱路径和真实物理路径的对应关系](../../应用文件/应用沙箱目录/app-sandbox-directory.md#应用沙箱路径和真实物理路径的对应关系)）。

   ```
   1. char pathBuf[READ_SIZE] = {0};
   2. strncpy(pathBuf,FILE_PATH,READ_SIZE);
   ```
2. 将要写入文本的内容通过Node-API接口传递到Native侧。

   ```
   1. napi_get_value_string_utf8(env, argv[0], contentsBuf, sizeof(contentsBuf), &contentsSize);
   ```
3. 通过指定的路径打开文件。

   ```
   1. // Open the file through the specified path.
   2. FILE *fp;
   3. fp = fopen(pathBuf, "w");
   ```
4. 使用C标准库的文件操作函数写入文件。

   ```
   1. // Write a file using the file operation function of the C standard library.
   2. fprintf(fp, "%s", contentsBuf);
   ```
5. 完整代码如下所示：

   ```
   1. static napi_value SplicePath(napi_env env, napi_callback_info info) {
   2. size_t argc = 1;
   3. napi_value argv[1] = {nullptr};
   4. napi_get_cb_info(env, info, &argc, argv, nullptr, nullptr);
   5. // Splice the sandbox path according to the actual file location.
   6. size_t contentsSize;
   7. char pathBuf[READ_SIZE] = {0};
   8. strncpy(pathBuf,FILE_PATH,READ_SIZE);
   9. // Convert the contents of the text to be written into C-side variables through the Node-API interface.
   10. char contentsBuf[BUFFER_SIZE];
   11. napi_get_value_string_utf8(env, argv[0], contentsBuf, sizeof(contentsBuf), &contentsSize);
   12. // Open the file through the specified path.
   13. FILE *fp;
   14. fp = fopen(pathBuf, "w");
   15. if (fp == nullptr) {
   16. OH_LOG_Print(LOG_APP, LOG_ERROR, DOMAIN, TAG, "Open file error!");
   17. return nullptr;
   18. }
   19. OH_LOG_Print(LOG_APP, LOG_INFO, DOMAIN, TAG, "Open file successfully!");
   20. // Write a file using the file operation function of the C standard library.
   21. fprintf(fp, "%s", contentsBuf);
   22. fclose(fp);
   23. return nullptr;
   24. }
   ```
6. 将该C++接口与ArkTS接口进行绑定和映射（详见[Native侧方法的实现](../../../../NDK开发/代码开发/使用Node-API实现ArkTSJS与CC++语言交互/使用Node-API实现跨语言交互开发流程/use-napi-process.md#native侧方法的实现)），同时在index.d.ts文件中，提供该接口方法。

   ```
   1. export const splicePath: (contents: string) => void;
   ```

第二部分：Native侧访问沙箱文件写数据的功能实现后，在ArkTS侧调用该方法。

1. 引用Native侧相应的so库。

   ```
   1. import FileAccess from 'libfile_access.so';
   ```
2. 在ArkTS侧调用该接口实现文件写入的操作。

   ```
   1. FileAccess.splicePath(content);
   ```

通过上述步骤，实现了在Native侧通过拼接沙箱路径访问与操作应用沙箱文件的方案。

**效果展示**

**图 4** Native侧拼接沙箱路径方案效果展示

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/48/v3/lf7AzbbJR3qM1R38sgLZbQ/zh-cn_image_0000002592218690.png?HW-CC-KV=V1&HW-CC-Date=20260611T063712Z&HW-CC-Expire=86400&HW-CC-Sign=95E4DA64D6007C4B952A04563682D2B0393FDF0C57D4DD47A79251CB96960CCD)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f9/v3/aT4OGVWYQeeWLxKomTOdOw/zh-cn_image_0000002592378624.png?HW-CC-KV=V1&HW-CC-Date=20260611T063712Z&HW-CC-Expire=86400&HW-CC-Sign=282072209ADF544103A77C63D2722D9E25968148E71D2724F6D90FBC66E937AD)

## 访问公共目录文件

系统公共目录下储存的是用户文件（详见[用户文件概述](../../用户文件/用户文件概述/user-file-overview.md)），应用对用户文件的操作需要提前获取用户授权，或由用户操作完成。可以通过系统预置的文件选择器（FilePicker）（详见[选择文档类文件](../../用户文件/选择与保存用户文件/选择用户文件/select-user-file.md#选择文档类文件)）实现该能力，目前主要有创建文件、写入和读取三类操作，创建文件（详见[save](<../../../../../harmonyos-references/Core File Kit（文件基础服务）/ArkTS API/@ohos.file.picker (选择器)/js-apis-file-picker.md#save>))可以直接使用picker，针对Native侧，有如下两种场景：

* 场景一：写数据到公共目录文件。
* 场景二：从公共目录文件中读取数据。

### 场景一：写数据到公共目录文件

**场景描述**

ArkTS侧通过文件picker在公共目录下创建文件，并传递文件描述符到Native侧，Native侧通过文件描述符打开文件并将数据写入到文件中。

**图 7** Native侧写入公共目录文件场景示意图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/30/v3/FNVBei9gQbKaBR531Csrcg/zh-cn_image_0000002622858131.png?HW-CC-KV=V1&HW-CC-Date=20260611T063712Z&HW-CC-Expire=86400&HW-CC-Sign=369EC7616BAC9D1D292FAAE9ABF24117A9642AD99BB0152E00F9AAD4B1DB11A7)

**实现方案**

实现方案分为Native侧定义操作文件的方法和ArkTS侧调用该方法两部分。

第一部分：在Native侧定义一个方法，用于接收文件描述符并将数据写入到文件中，注意使用文件描述符操作文件需要引用头文件unistd.h。

1. 将传入的文件描述符和要写入文件的内容通过Node-API接口传递到Native侧。

   ```
   1. // Convert the incoming file descriptor and the contents to be written into the file into C-side variables.
   2. napi_get_value_uint32(env, argv[0], &fd);
   3. napi_get_value_string_utf8(env, argv[1], contentsBuf, sizeof(contentsBuf), &contentsSize);
   ```
2. 使用C标准库的文件操作函数写入文件。

   ```
   1. // Write a file using the file operation function of the C standard library.
   2. size_t buffSize = write(fd, contentsBuf, contentsSize);
   ```
3. 根据write函数的返回值判断操作是否成功。

   ```
   1. std::string res;
   2. // According to the return value of the write function, judge whether the operation returns the result successfully.
   3. napi_value contents;
   4. if (buffSize == -1) {
   5. res = "Write File Failed!";
   6. OH_LOG_Print(LOG_APP, LOG_ERROR, DOMAIN, TAG, "%s", res.c_str());
   7. } else {
   8. res = "Write File Successfully!!!";
   9. OH_LOG_Print(LOG_APP, LOG_INFO, DOMAIN, TAG, "%s", res.c_str());
   10. }
   11. napi_create_string_utf8(env, res.c_str(), sizeof(res), &contents);
   12. return contents;
   ```
4. 完整代码如下所示：

   ```
   1. static napi_value WriteFileUsingPickerFd(napi_env env, napi_callback_info info) {
   2. size_t argc = 2;
   3. napi_value argv[2] = {nullptr};
   4. napi_get_cb_info(env, info, &argc, argv, nullptr, nullptr);

   6. unsigned int fd = -1;
   7. size_t contentsSize;
   8. char contentsBuf[BUFFER_SIZE];
   9. // Convert the incoming file descriptor and the contents to be written into the file into C-side variables.
   10. napi_get_value_uint32(env, argv[0], &fd);
   11. napi_get_value_string_utf8(env, argv[1], contentsBuf, sizeof(contentsBuf), &contentsSize);
   12. ftruncate(fd, 0);
   13. // Write a file using the file operation function of the C standard library.
   14. size_t buffSize = write(fd, contentsBuf, contentsSize);
   15. std::string res;
   16. // According to the return value of the write function, judge whether the operation returns the result successfully.
   17. napi_value contents;
   18. if (buffSize == -1) {
   19. res = "Write File Failed!";
   20. OH_LOG_Print(LOG_APP, LOG_ERROR, DOMAIN, TAG, "%s", res.c_str());
   21. } else {
   22. res = "Write File Successfully!!!";
   23. OH_LOG_Print(LOG_APP, LOG_INFO, DOMAIN, TAG, "%s", res.c_str());
   24. }
   25. napi_create_string_utf8(env, res.c_str(), sizeof(res), &contents);
   26. return contents;
   27. }
   ```
5. 将该C++接口与ArkTS接口进行绑定和映射（详见[Native侧方法的实现](../../../../NDK开发/代码开发/使用Node-API实现ArkTSJS与CC++语言交互/使用Node-API实现跨语言交互开发流程/use-napi-process.md#native侧方法的实现)），同时在index.d.ts文件中，提供该接口方法。

   ```
   1. export const writeFileUsingPickerFd: (fd: number, contents: string) => string;
   ```

第二部分：Native侧访问公共目录文件写数据的功能实现后，在ArkTS侧调用该方法。

1. 引用Native侧相应的so库。

   ```
   1. import FileAccess from 'libfile_access.so';
   ```
2. 在ArkTS侧拉起picker选择文件并将文件描述符传入Native接口中。

   ```
   1. async function WriteFileByPicker(contents: string): Promise<string> {
   2. // Configure picker Selection Information
   3. const documentSelectOptions = new picker.DocumentSelectOptions();
   4. documentSelectOptions.maxSelectNumber = 1;
   5. documentSelectOptions.fileSuffixFilters = ['.txt'];

   7. let uris: Array<string> = [];
   8. const documentViewPicker = new picker.DocumentViewPicker();
   9. // Pull up the picker selection file
   10. return await documentViewPicker.select(documentSelectOptions).then((documentSelectResult: Array<string>) => {
   11. uris = documentSelectResult;
   12. let uri: string = uris[0];
   13. let path: string = new fileUri.FileUri(uri).path;
   14. Logger.info(`Open The File path is [${uri}]`);
   15. let file = fs.openSync(path, fs.OpenMode.WRITE_ONLY);
   16. // Call the native method to write a file
   17. let res = FileAccess.writeFileUsingPickerFd(file.fd, contents);
   18. fs.closeSync(file.fd);
   19. return res;
   20. }).catch((error: BusinessError) => {
   21. Logger.error(`Open The file failed, error code is [${error.code}], error message is [${error.message}]`);
   22. return 'Write Failed by Picker';
   23. })
   24. }
   ```

通过上述步骤，实现了在Native侧通过ArkTS侧picker传递的文件资源描述符访问公共目录文件并写入内容的方案。

**效果展示**

**图 8** Native侧写公共目录文件场景方案效果展示

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/99/v3/QqxWa8fnQAepkym9dIqYng/zh-cn_image_0000002622698253.png?HW-CC-KV=V1&HW-CC-Date=20260611T063712Z&HW-CC-Expire=86400&HW-CC-Sign=8D2DB33F2EBC670400D63811D5F8BD93253538B86A49C74931F2012920585485)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ea/v3/Put3nlpvQS2i4HraOw9CSg/zh-cn_image_0000002592218692.png?HW-CC-KV=V1&HW-CC-Date=20260611T063712Z&HW-CC-Expire=86400&HW-CC-Sign=B869EBCFFE87890CB3883E36B93FF4BB8F0BE8E830FE9E9C8AA4D2E5B71CA180)

### 场景二：从公共目录文件中读取数据

**场景描述**

ArkTS侧通过文件picker选择文件，并传递文件描述符到Native侧，Native侧通过文件描述符打开文件并读取文件数据。

**图 9** Native侧读取公共目录文件场景示意图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1e/v3/DH-r46YCTHm_Ek9LhXJvIw/zh-cn_image_0000002592378626.png?HW-CC-KV=V1&HW-CC-Date=20260611T063712Z&HW-CC-Expire=86400&HW-CC-Sign=612E0A314B623E525EC0178D5E8054524D81EA5960E87D5C4E764E35C2F4D085)

**实现方案**

实现方案分为Native侧定义操作文件的方法和ArkTS侧调用该方法两部分。

第一部分：在Native侧定义一个方法，用于接收文件描述符并从文件中读取数据，注意使用文件描述符操作文件需要引用头文件unistd.h。

1. 将传入的文件描述符通过Node-API接口传递到Native侧。

   ```
   1. // Convert the incoming file descriptor into a C-side variable.
   2. napi_get_value_uint32(env, argv[0], &fd);
   ```
2. 使用C标准库的文件操作函数读取文件。

   ```
   1. // Use the file operation function of the C standard library to read the file.
   2. char buff[READ_SIZE];
   3. size_t buffSize = read(fd, buff, sizeof(buff));
   ```
3. 判断读取是否成功并返回文件内容。

   ```
   1. // Judge whether the reading is successful or not and return the file content.
   2. napi_value contents;
   3. if (buffSize == -1) {
   4. OH_LOG_Print(LOG_APP, LOG_ERROR, DOMAIN, TAG, "Read File Failed!!!");
   5. } else {
   6. OH_LOG_Print(LOG_APP, LOG_INFO, DOMAIN, TAG, "Read File Successfully!!!");
   7. napi_create_string_utf8(env, buff, buffSize, &contents);
   8. }
   9. return contents;
   ```
4. 完整代码如下所示：

   ```
   1. // entry/src/main/cpp/FileAccessMethods.cpp
   2. static napi_value ReadFileUsingPickerFd(napi_env env, napi_callback_info info) {
   3. size_t argc = 1;
   4. napi_value argv[1] = {nullptr};
   5. napi_get_cb_info(env, info, &argc, argv, nullptr, nullptr);

   7. unsigned int fd = -1;
   8. // Convert the incoming file descriptor into a C-side variable.
   9. napi_get_value_uint32(env, argv[0], &fd);
   10. // Use the file operation function of the C standard library to read the file.
   11. char buff[READ_SIZE];
   12. size_t buffSize = read(fd, buff, sizeof(buff));
   13. // Judge whether the reading is successful or not and return the file content.
   14. napi_value contents;
   15. if (buffSize == -1) {
   16. OH_LOG_Print(LOG_APP, LOG_ERROR, DOMAIN, TAG, "Read File Failed!!!");
   17. } else {
   18. OH_LOG_Print(LOG_APP, LOG_INFO, DOMAIN, TAG, "Read File Successfully!!!");
   19. napi_create_string_utf8(env, buff, buffSize, &contents);
   20. }
   21. return contents;
   22. }
   ```
5. 将该C++接口与ArkTS接口进行绑定和映射（详见[Native侧方法的实现](../../../../NDK开发/代码开发/使用Node-API实现ArkTSJS与CC++语言交互/使用Node-API实现跨语言交互开发流程/use-napi-process.md#native侧方法的实现)），同时在index.d.ts文件中，提供该接口方法。

   ```
   1. export const readFileUsingPickerFd: (fd: number) => string;
   ```

第二部分：Native侧访问公共目录文件读数据的功能实现后，在ArkTS侧调用该方法。

1. 引用Native侧相应的so库。

   ```
   1. import FileAccess from 'libfile_access.so';
   ```
2. 在ArkTS侧拉起picker选择文件并将文件描述符传入Native接口中。

   ```
   1. async function ReadFileByPicker(): Promise<string> {
   2. // Configure picker Selection Information
   3. const documentSelectOptions = new picker.DocumentSelectOptions();
   4. documentSelectOptions.maxSelectNumber = 1;
   5. documentSelectOptions.fileSuffixFilters = ['.txt'];
   6. // Pull up the picker selection file
   7. let uris: Array<string> = [];
   8. const documentViewPicker = new picker.DocumentViewPicker();
   9. return await documentViewPicker.select(documentSelectOptions).then((documentSelectResult: Array<string>) => {
   10. uris = documentSelectResult;
   11. let uri: string = uris[0];
   12. let path: string = new fileUri.FileUri(uri).path;
   13. Logger.info(`The Opened File path is [${uri}]`);
   14. let file = fs.openSync(path, fs.OpenMode.READ_ONLY);
   15. // Call the native method to read the file.
   16. let res = FileAccess.readFileUsingPickerFd(file.fd);
   17. fs.closeSync(file.fd);
   18. return res;
   19. }).catch((error: BusinessError) => {
   20. Logger.error(`Open The file failed, error code is [${error.code}], error message is [${error.message}]`);
   21. return 'Read Failed by Picker!';
   22. })
   23. }
   ```

通过上述步骤，实现了在Native侧通过ArkTS侧picker传递的文件资源描述符访问公共目录文件并读取内容的方案。

**效果展示**

**图 10** Native侧读公共目录文件场景方案效果展示

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cd/v3/wejbnzHxTw64SvVNH2l6lg/zh-cn_image_0000002622858133.png?HW-CC-KV=V1&HW-CC-Date=20260611T063712Z&HW-CC-Expire=86400&HW-CC-Sign=734FFC6EB0F3818F50EE17E530B4F837AD07D3EA349E22654F264D1B7AB65794)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/66/v3/5NUddY0BRyKw1D-Ek9kniQ/zh-cn_image_0000002622698255.png?HW-CC-KV=V1&HW-CC-Date=20260611T063712Z&HW-CC-Expire=86400&HW-CC-Sign=4E51480573E6F427AF0ABB951900E291E82784BF8FE8726AADA11AED90683F34)

## 示例代码

[实现Native侧文件访问](https://gitcode.com/harmonyos_samples/NativeFileAccess)
