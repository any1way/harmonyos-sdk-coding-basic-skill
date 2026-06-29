---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-debug-arkts-debugger
title: 使用调试器
breadcrumb: 指南 > 编写与调试应用 > 应用调试 > 代码调试 > 使用调试器
category: harmonyos-guides
scraped_at: 2026-06-11T15:29:16+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:83b3998d2c69a37e31a7937753919b28f4a46d8ede2071fb99e543007437fd15
---
Debug界面有三个tab页，分别是“entry”、“entry(PandaDebugger)”和“entry(Native)”。

通常第一个tab页“entry”用于展示推包安装过程。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/32/v3/02faFDdmQ--B2KpUyjP0Iw/zh-cn_image_0000002571547238.png?HW-CC-KV=V1&HW-CC-Date=20260611T072915Z&HW-CC-Expire=86400&HW-CC-Sign=BFEB5346A911C1B0717F61A7FD491820FDC6DEAF8548957E89B19176FEA6FD2F)

第二个tab页“entry(PandaDebugger)”和第三个tab页“entry(Native)”是调试器，用于调试Debugger功能，其中“entry(Native)”仅在涉及Native调试时才会拉起。调试器包含两个窗格，**[Debugger](ide-debug-arkts-debugger.md#section1437520119316)**和**[Console](ide-debug-arkts-debugger.md#section327153017314)**。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d0/v3/oGnwOuzeQvWiJvcyYoPK3g/zh-cn_image_0000002571547244.png?HW-CC-KV=V1&HW-CC-Date=20260611T072915Z&HW-CC-Expire=86400&HW-CC-Sign=47BB49E44FC2A48BD998E45589475604F36BAD1DC2A45A72E0DE65D738BFC61E)

## Debugger窗格

Debugger显示两个独立的窗格：

* 左侧区域是Frames，当应用调试到某个断点时，Frames区会显示当前代码所引用的代码位置。
* 右侧区域是Variables，用于展示当前变量。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/47/v3/o3kASllORXGrIf5dSUo6fQ/zh-cn_image_0000002571387576.png?HW-CC-KV=V1&HW-CC-Date=20260611T072915Z&HW-CC-Expire=86400&HW-CC-Sign=1509B6280283C40157224DB38BC80F32D1AB7B4CAA3AAC1DB5D9E3431F1AB4A5)

Debugger窗格有多个按钮：

**表1** 调试器按钮

| 按钮 | 名称 | 快捷键 | 功能 |
| --- | --- | --- | --- |
|  | Resume Program | **F9**（macOS为**Option+Command+R**） | 当程序执行到断点时停止执行，单击此按钮程序继续执行。 |
|  | Step Over | **F8**（macOS为**F8**） | 在单步调试时，直接前进到下一行（如果在函数中存在子函数时，不会进入子函数内单步执行，而是将整个子函数当作一步执行）。 |
|  | Step Into | **F7**（macOS为**F7**） | 在单步调试时，遇到子函数后，进入子函数并继续单步执行。 |
|  | Force Step Into | **Alt+Shift+F7**（macOS为**Option+Shift+F7**） | 在单步调试时，强制进入方法。 |
|  | Step Out | **Shift+F8**（macOS为**Shift+F8**） | 在单步调试执行到子函数内时，单击Step Out会执行完子函数剩余部分，并跳出返回到上一层函数。 |
|  | Stop | **Ctrl+F2**（macOS为**Command+F2**） | 停止调试任务。 |
|  | Run To Cursor | **Alt+F9**（macOS为**Option+F9**） | 断点执行到鼠标停留处。 |
|  | JSVM Debug Port | 无 | 转发JSVM调试的端口，转发后可以在浏览器的DevTools工具上进行[JSVM-API调试](../../../../NDK开发/代码开发/使用JSVM-API实现JS与CC++语言交互/JSVM-API典型使用场景指导/JSVM-API调试&定位/jsvm-debugger-cpuprofiler-heapsnapshot.md)。  说明  仅Native调试器中支持该按钮。 |

### Resume Program

点击Resume Program图标![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7d/v3/xr1abgqyQP6hqi3G6ZvmSA/zh-cn_image_0000002602066715.png?HW-CC-KV=V1&HW-CC-Date=20260611T072915Z&HW-CC-Expire=86400&HW-CC-Sign=61C7BEC64CC81E63CA956F6983D63C3EA55222024115893FE18794F9735A0E78)，如果存在断点时，命中下一个断点，并展示对应的Frames和Variables信息；如果不存在断点，设备上的应用正常运行，Frames和Variables信息会消失。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6a/v3/SEk_-xgAS_O6o7UOzFQiag/zh-cn_image_0000002602066691.png?HW-CC-KV=V1&HW-CC-Date=20260611T072915Z&HW-CC-Expire=86400&HW-CC-Sign=6DB65A5575423A1BEF074CFD5682D968515D6EA496195C92D7A9C52FE9F01AEF)

### Pause Program

点击Pause Program图标![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/47/v3/nYfxJ5b-Qeaxntr3gppxvg/zh-cn_image_0000002602066709.png?HW-CC-KV=V1&HW-CC-Date=20260611T072915Z&HW-CC-Expire=86400&HW-CC-Sign=3BBCF9EE0EB684B89517C019907473751FCEA8542C4C25C31BECD435314C9F38)，当有对应源代码时，应用会暂停。

### Step Over

点击Step Over![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ed/v3/A2kBC3ckTBymoUBqv7p3oA/zh-cn_image_0000002571387594.png?HW-CC-KV=V1&HW-CC-Date=20260611T072915Z&HW-CC-Expire=86400&HW-CC-Sign=5A9A98116641C7B7873710DADB32244C4D864869CD81D80FABC1493E84B8AB1F)，当前代码执行到下一行代码。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c4/v3/6sy0kGY-SlCRXdpEa4nAFw/zh-cn_image_0000002571547234.png?HW-CC-KV=V1&HW-CC-Date=20260611T072915Z&HW-CC-Expire=86400&HW-CC-Sign=612C14A34FD6CE83B326093D2A34CEA38358A6077C1B81AC63F6C7F8A90E181D)

### Step Into

点击Step Into![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0e/v3/-X9a0BbLR-WmJ4fR7xWnGg/zh-cn_image_0000002571387610.png?HW-CC-KV=V1&HW-CC-Date=20260611T072915Z&HW-CC-Expire=86400&HW-CC-Sign=F911486D5900CD1DC5D6937ADECFA837BEE33AE402AED18E05537B2C54E64C52)，当前代码进入到方法内部。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f9/v3/jMB5J6L6Sy2Li6dP2nRX5g/zh-cn_image_0000002571387578.png?HW-CC-KV=V1&HW-CC-Date=20260611T072915Z&HW-CC-Expire=86400&HW-CC-Sign=70E0834BD5E94C9D97EB66413CDA52EFED8C1223677DA25B01DC7FC609AC366C)

例如代码进入add方法的定义处。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/22/v3/Rxxg3t5pSJOEhJ5ye_7E1g/zh-cn_image_0000002602066705.png?HW-CC-KV=V1&HW-CC-Date=20260611T072915Z&HW-CC-Expire=86400&HW-CC-Sign=2FEBDD161350F4CC90A1273CE6B4FB1B647D3F0810D6606DE5AF8EED16D2F5F0)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f5/v3/glUC71H1SOmDYxuc45fvIw/zh-cn_image_0000002571547214.png?HW-CC-KV=V1&HW-CC-Date=20260611T072915Z&HW-CC-Expire=86400&HW-CC-Sign=D33FEA726B941DA18954EF17502ACE9579CFEBF11CC87A21BD39C0BEF7EC3660)

### Step Out

点击Step Out![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/62/v3/i307cQLhTIS6U1QJbJuA1w/zh-cn_image_0000002602186749.png?HW-CC-KV=V1&HW-CC-Date=20260611T072915Z&HW-CC-Expire=86400&HW-CC-Sign=AE36B1718678FA532AD718FB35C66044DE96438F6911F6D7C20EA6EB2FF31080)，代码会从方法内部回到调用处。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/17/v3/0ZF_tFDrTrS__h0-Ll3cmA/zh-cn_image_0000002602066707.png?HW-CC-KV=V1&HW-CC-Date=20260611T072915Z&HW-CC-Expire=86400&HW-CC-Sign=CFC8AE6ACCD02F2AD4C66CCF549F741342B4784318563F773AC6B9EC16615755)

### Run to Cursor

点击Run to Cursor![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/55/v3/QUSeWwooRS-yHVWBoepjnw/zh-cn_image_0000002571547218.png?HW-CC-KV=V1&HW-CC-Date=20260611T072915Z&HW-CC-Expire=86400&HW-CC-Sign=0801D97F0FC22E45C16D5A80470CFA4440B43E289BD9D89CEA2BD3635C0F3135)，代码停留在鼠标停留处。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/33/v3/wcNZIHRaRdG5FicN2HVpRA/zh-cn_image_0000002602066695.png?HW-CC-KV=V1&HW-CC-Date=20260611T072915Z&HW-CC-Expire=86400&HW-CC-Sign=5E7660372D18D5F84CFE7F4ADE2747E5738B23AB70B0542565F15E1FDF2F3AA7)

### JSVM Debug Port

点击JSVM Debug Port![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fa/v3/ht0UszePTdOmu5Z4-GG3xA/zh-cn_image_0000002602066725.png?HW-CC-KV=V1&HW-CC-Date=20260611T072915Z&HW-CC-Expire=86400&HW-CC-Sign=AFFFD242159C1D9D253D99304B8AE4CA7C2FE0335EFDF2D3E42FFCEE998B63DF)，弹出输入转发端口的面板，输入端口并点击**OK**后会开始转发，转发成功后会有弹窗提示，打开对应的URL即可对JS代码进行调试。关于如何调试C++拉起的JS代码，请查阅[JSVM-API调试&定位](../../../../NDK开发/代码开发/使用JSVM-API实现JS与CC++语言交互/JSVM-API典型使用场景指导/JSVM-API调试&定位/jsvm-debugger-cpuprofiler-heapsnapshot.md)。

该功能从DevEco Studio 5.1.0 Release版本开始支持。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d3/v3/g-6TIrjqS2yNBtb8npXmkw/zh-cn_image_0000002602066721.png?HW-CC-KV=V1&HW-CC-Date=20260611T072915Z&HW-CC-Expire=86400&HW-CC-Sign=0290EDE6604F2801B4B1BB1BF10BC642084F6E0EFF7AB534A99842FEBACD924D) ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/96/v3/z6JwHTcHQZWBw5RkDQPuxw/zh-cn_image_0000002571547212.png?HW-CC-KV=V1&HW-CC-Date=20260611T072915Z&HW-CC-Expire=86400&HW-CC-Sign=CA601170F8E7DDB723B6FD0AAA1C32BD392341AD9165E243E5A3B71A2E9E0B88)

## Console窗格

Console窗格用于展示已加载的ets/js。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cf/v3/xvnQNcD3QK6M6ay4FWZLAQ/zh-cn_image_0000002602186751.png?HW-CC-KV=V1&HW-CC-Date=20260611T072915Z&HW-CC-Expire=86400&HW-CC-Sign=F0DEE37065D40AE817CCA716E8F8040F391FDF55EA2B0161BD7A4F46092D457D)
