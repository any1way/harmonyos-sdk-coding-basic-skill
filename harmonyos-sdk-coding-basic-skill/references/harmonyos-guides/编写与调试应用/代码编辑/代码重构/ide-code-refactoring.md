---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-code-refactoring
title: 代码重构
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码重构
category: harmonyos-guides
scraped_at: 2026-06-11T15:28:04+08:00
doc_updated_at: 2026-03-24
content_hash: sha256:475c100ddaeb9251a41315c82d28331dcd2362f968fd44f7f2310cdb266c12df
---

## ArkTS/TS代码重构

### Refactor-Extract代码提取

在编辑器中支持将函数内、类方法内等区域代码块或表达式，提取为新方法/函数（Method）、常量（Constant）、接口（Interface）、变量（Variable）或类型别名（Type Alias）。准确便捷的将所选区域代码从当前作用域内进行提取，提升编码效率。选中所需要提取的代码块，右键单击**Refactor**，选择需要提取的类型。

说明

Refactor-Extract代码提取为类型别名（Type Alias）能力仅TS语言支持。

方法/函数（Method）支持选中代码块或完整语句进行提取：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5/v3/uX2rTLXdQMCvQZzHbJwmWQ/zh-cn_image_0000002571547306.gif?HW-CC-KV=V1&HW-CC-Date=20260611T072745Z&HW-CC-Expire=86400&HW-CC-Sign=B7EB4ABE76E487A38EC3A9EC087D1C4AB640CA3872B50A5D1D11C29B677A055A "点击放大")

在ArkTS语言中，支持将组件调用代码块提取为@Builder装饰器装饰的方法，组件属性调用表达式可提取为@Styles或@Extend装饰器装饰的方法。

**使用方式**：选中需要提取的组件或属性，右键单击**Refactor**，选择**Extract Method...**，组件私有属性可提取为@Extend装饰的方法，通用属性可提取为@Styles或@Extend装饰的方法。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/98/v3/hyboofFURVSBAlc06SEZ0g/zh-cn_image_0000002602066795.gif?HW-CC-KV=V1&HW-CC-Date=20260611T072745Z&HW-CC-Expire=86400&HW-CC-Sign=FAA825C4EC573049E2842BC0E95821FAF20742C3BE8A3A5E62F78545E0DE60EE "点击放大")

常量（Constant）支持选中单行表达式进行提取：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e7/v3/32Wea59BRR64k0-B36ItJA/zh-cn_image_0000002602186841.gif?HW-CC-KV=V1&HW-CC-Date=20260611T072745Z&HW-CC-Expire=86400&HW-CC-Sign=D8F1312D9646865B303E5574818B1E652C8BE594AA0CD3352F580D67FA66E052 "点击放大")

接口（Interface）支持选中对象自变量进行提取：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4a/v3/oQ2MK-N7Q_WO2lo0tC8BiQ/zh-cn_image_0000002602186845.gif?HW-CC-KV=V1&HW-CC-Date=20260611T072745Z&HW-CC-Expire=86400&HW-CC-Sign=FDED8286C0270D88A1BDA5E9794FD95EDE2763D27E0F2226B7E917910AE0DCC9 "点击放大")

支持选中表达式提取为变量（Variable）：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1e/v3/JM59wHNuRlqNunM3iazF2w/zh-cn_image_0000002571547304.gif?HW-CC-KV=V1&HW-CC-Date=20260611T072745Z&HW-CC-Expire=86400&HW-CC-Sign=F7100F7D24E502F92ADBA0981DD8C21B23CF9BB22DA70BFBA99356B950D12D70 "点击放大")

### Refactor-Convert代码转换

编辑器内提供Convert重构能力，支持Convert between named imports and namespace imports等高频转换操作，辅助开发者高效重构代码，提升代码质量。

**表1** Refactor-Convert功能支持清单

| 功能 | 说明 | 使用方法 | 支持转换的源码类型 |
| --- | --- | --- | --- |
| Convert to class | 将JS源码中的function转换为符合ES6标准的类 | 点击或选中function名，右键单击**Refactor** > **Convert**，或使用快捷键**Ctrl+Alt+Shift+R**（macOS为**Option+Shift+Command+R**），在弹窗中选择转换的方式。  说明  若当前工程中已引用该方法，执行Convert to class后，在Find Usages中可查看引用的具体位置，点击**Do Refactor**可忽略冲突并执行转换；也可以逐条修改引用位置的代码后，重新执行上述操作。 | JS |
| Convert to anonymous function | 将箭头函数转换为匿名函数 | 选中箭头函数赋值变量，右键单击**Refactor** > **Convert**，或使用快捷键**Ctrl+Alt+Shift+R**（macOS为**Option+Shift+Command+R**），在弹窗中选择转换的方式。 | JS/TS |
| Convert to named function | 将箭头函数转换为普通函数 | 选中箭头函数赋值变量，右键单击**Refactor** > **Convert**，或使用快捷键**Ctrl+Alt+Shift+R**（macOS为**Option+Shift+Command+R**），在弹窗中选择转换的方式。 | JS/TS/ArkTS |
| Convert to arrow function | 将匿名函数转换为箭头函数 | 选中匿名函数赋值变量，右键单击**Refactor** > **Convert**，或使用快捷键**Ctrl+Alt+Shift+R**（macOS为**Option+Shift+Command+R**），在弹窗中选择转换的方式。 | JS/TS/ArkTS |
| Convert default export to named export | 支持named export和default export相互转换 | 完整选中export default语句，右键单击**Refactor** > **Convert**，或使用快捷键**Ctrl+Alt+Shift+R**（macOS为**Option+Shift+Command+R**），在弹窗中选择转换的方式。 | JS/TS/ArkTS |
| Convert named export to default export | 完整选中export语句，右键单击**Refactor** > **Convert**，或使用快捷键**Ctrl+Alt+Shift+R**（macOS为**Option+Shift+Command+R**），在弹窗中选择转换的方式。 |
| Convert named imports to namespace import | 支持在命名import和命名空间import形态间转换 | 完整选中import语句，右键单击**Refactor** > **Convert**，或使用快捷键**Ctrl+Alt+Shift+R**（macOS为**Option+Shift+Command+R**），在弹窗中选择转换的方式。 | JS/TS/ArkTS |
| Convert namespace import to named imports | 完整选中命名空间import语句，右键单击**Refactor** > **Convert**，或使用快捷键**Ctrl+Alt+Shift+R**（macOS为**Option+Shift+Command+R**），在弹窗中选择转换的方式。 |
| Convert to template string | 将字符串转换为模板字面量 | 选中字符串或完整表达式，右键单击**Refactor** > **Convert**，或使用快捷键**Ctrl+Alt+Shift+R**（macOS为**Option+Shift+Command+R**），在弹窗中选择转换的方式。 | JS/TS/ArkTS |
| Convert to optional chain expression | 将判空逻辑转换为可选链式调用 | 选中连续判空表达式，右键单击**Refactor** > **Convert**，或使用快捷键**Ctrl+Alt+Shift+R**（macOS为**Option+Shift+Command+R**），在弹窗中选择转换的方式。 | JS/TS/ArkTS |

### Refactor-Rename代码重命名

代码编辑支持Rename功能，可以快速更改变量、方法、对象属性等相关标识符及文件、模块的名称，并同步到整个工程中对其进行引用的位置。

**使用方式**：选中需要重新命名的标识符（变量、类、接口、自定义组件等），右键单击**Refactor**，选择**Rename...**（或使用**快捷键Shift+F6**），在弹框中输入新的标识符名称，并在**Scope**中选择替换的范围，点击**Refactor**完成重新命名。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/93/v3/Jhc0PkRUTUSqDESxHZBCOA/zh-cn_image_0000002602186837.png?HW-CC-KV=V1&HW-CC-Date=20260611T072745Z&HW-CC-Expire=86400&HW-CC-Sign=608E6C00C42C80F7F0831B0583E39226DDBE4DB7091413DE43A73ED2E660AD5A)

代码编辑支持筛选并过滤不需要rename的引用位置。在**Rename...**弹窗中点击**Preview**，在弹出预览窗口中，用户选中无需Rename的选项，单击右键菜单**Exclude****/Remove**进行过滤/删除，完成筛选后点击左下角**Do Refactor**，重新执行Rename操作。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8d/v3/dcVRzBS_TayGro0d7P6ltw/zh-cn_image_0000002571547314.png?HW-CC-KV=V1&HW-CC-Date=20260611T072745Z&HW-CC-Expire=86400&HW-CC-Sign=D207D21BB31DAE1DBF760382586728351B2D79804DD5830102562DE1FC08D859)

说明

若ArkTS文件中存在C++接口调用，使用Rename进行重命名时，C++文件中涉及的函数名也会被重命名。

### Move File

在文件中单击右键，选择**Refactor > Move File...**，在弹窗中输入或点击**...**选择指定的目录，点击**Refactor**，可将当前文件移动至该目录下。勾选**Search for references**，可查找并更新工程中对该文件的引用；勾选**Open in editor**，可在编辑器中查看移动的文件。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/71/v3/qtNaCWvkQLuo_bR4SsdtOw/zh-cn_image_0000002571547312.png?HW-CC-KV=V1&HW-CC-Date=20260611T072745Z&HW-CC-Expire=86400&HW-CC-Sign=4D7DCC67E263D3BF37C41E7E14473389F83108FB726A60DFAA706035A2949423)

### Safe Delete

编辑器支持Safe Delete功能，帮助您安全地删除代码中的标识符对象（变量、函数或类等）或删除指定文件。在删除前，编辑器将先在代码中搜索对该对象的引用，如果存在引用，编辑器将提示您进行必要的检查和调整。

**使用方式**：在编辑器内选中需要删除的标识符对象或在工程目录选择待删除的文件，右键单击**Refactor**，选择**Safe Delete**，单击**OK**将自动检查当前对象在代码中被引用的情况，点击**View Usages**可查看具体使用的代码内容，点击**Delete Anyway**将直接删除该对象的定义。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/72/v3/08RfpGRxSMirPMaHSa6IpA/zh-cn_image_0000002571547308.png?HW-CC-KV=V1&HW-CC-Date=20260611T072745Z&HW-CC-Expire=86400&HW-CC-Sign=2160667DE30E0C8732AB8D937B6F7D2B84C30E8921B714BAA1C47EF7BE820110)

## C++代码重构

编辑器提供C++代码重构能力，当前支持展开宏、交换if分支、移动函数体到声明处等使用场景下的重构能力，提升开发效率。

### 展开宏

支持在当前宏引用处展开宏。将光标移动至需要展开的宏，右键单击**Refactor**，选择**Inline**，展开此处引用的宏。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b0/v3/ZWDxv8hHT_mrWA6HGyyqZA/zh-cn_image_0000002571547302.gif?HW-CC-KV=V1&HW-CC-Date=20260611T072745Z&HW-CC-Expire=86400&HW-CC-Sign=85EC9BF8DF7FB063A4BD99D0523B44B48226BD6171BFCDB12A3A0C49B85614BB)

### 交换if分支

编辑器支持在选中if-else完整代码块的情况下，实现对if-else代码块的位置交换，并对条件取反。

**使用约束**

* 需要重构的代码块必须为完整的if-else代码结构，{}不能省略；
* if-else中的statement包含嵌套if-else语句时，只反转最外层的if-else语句。对于if() -else if()-else() 结构，仅支持对最后一层if-else结构进行交换；
* 不支持赋值语句的判断条件取反。

**使用方式**

编辑器内选择需要转换的代码区域，右键单击**Refactor**，选择**Swap If Branches**，对原有if条件取反，并交换if-else原代码块顺序。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/19/v3/B9HPnOmqQkiq1T-iRXaIQw/zh-cn_image_0000002602186843.gif?HW-CC-KV=V1&HW-CC-Date=20260611T072745Z&HW-CC-Expire=86400&HW-CC-Sign=358FCD92897527FEE1C9D1653CCFBA3E7747E3AD6A79DA8D5BE6D4031E685018 "点击放大")

### 移动函数体到声明处

编辑器支持将函数体从源文件移动到头文件中，提高代码可读性。编辑器内选中函数名，右键单击**Refactor**，选择**Move to Declaration**，源文件中的函数实现将移动至头文件中。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4f/v3/fGg73OVeT2CLEEnOdrPTxQ/zh-cn_image_0000002602066783.gif?HW-CC-KV=V1&HW-CC-Date=20260611T072745Z&HW-CC-Expire=86400&HW-CC-Sign=AF303AEB20EC55630FF9FA34B8B6FA33A56F4454036455469B32DDF7A02E885A)

### 移动函数体到实现处

在编辑器内将光标放在或选中函数名，右键单击**Refactor**，选择**Move to Implementation**，选择移动到的文件，将函数定义移动到该文件。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/df/v3/MEzmS2eKQIa1j1yRCrWDfQ/zh-cn_image_0000002602186849.gif?HW-CC-KV=V1&HW-CC-Date=20260611T072745Z&HW-CC-Expire=86400&HW-CC-Sign=161251E725A1FBA0EF57BF4A44A4D5EF034B660412D8DCE838DD8518C96EC897)

### 将语句转为原始字符串

编辑器提供重构能力，支持将带有 \n, \t, \", \\, \'五类转义字符的字符串转换为原始字符串。当前仅支持标准字符串，不支持 u8""等其他字符串。

在编辑器内选择字符串代码区域，右键单击**Refactor**，选择**Convert To Raw String**，将语句转换为原始字符串。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/47/v3/xd-zAXaJRyCy0qjNdCuutA/zh-cn_image_0000002602186847.gif?HW-CC-KV=V1&HW-CC-Date=20260611T072745Z&HW-CC-Expire=86400&HW-CC-Sign=9DF2FEADF6B324DA9B3B5CD21A69DFF53E6771900784F9CF9E47194688B59A6A "点击放大")

### 定义构造函数

编辑器提供重构能力，支持为类的成员变量生成默认的构造函数。

**规格限制**

1. 不支持未初始化成员变量的类
2. 不支持在（class标识符，类名，大括号）以外的位置触发
3. 不支持类已存在有入参的构造函数

**使用方法：**在类的定义的类名处，右键单击**Generate****...**，选择**Constructor**，在弹框中点击**Define**，为成员变量定义一个构造函数。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e3/v3/nSQlH8fETey5hTQiSwF8zg/zh-cn_image_0000002571387666.gif?HW-CC-KV=V1&HW-CC-Date=20260611T072745Z&HW-CC-Expire=86400&HW-CC-Sign=CDBF5286B3B28F4B6F2B9A4555FB0A0E8C4F90802A9B47E946C52E956F9FA23F)

### 提取表达式到变量

在编辑器内，选中需要提取的表达式范围，右键单击**Refactor**，选择**Extract Variable**，支持提取表达式到变量。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/eb/v3/neF3sa8dQIyYBoYm8EQwvw/zh-cn_image_0000002602186835.gif?HW-CC-KV=V1&HW-CC-Date=20260611T072745Z&HW-CC-Expire=86400&HW-CC-Sign=AE487C7B01A8B56789D2E1A7F9F53E35F182B18585DD9FE2D0CDCD58E00093E2 "点击放大")

### 移除namespace

光标停留在需要移除的namespace处，右键单击**Refactor**，选择**Remove Using Namespace**进行移除，可以避免命名冲突，提高代码可读性。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/53/v3/2W99YoP5QKqUIgbvUPy6lw/zh-cn_image_0000002602186839.gif?HW-CC-KV=V1&HW-CC-Date=20260611T072745Z&HW-CC-Expire=86400&HW-CC-Sign=81462F06EA3F8B780FD81F38B2BE5867B8045F3B3BB98AC625E09FC5A8B97A39)

### 添加using声明

编辑器内，光标停留在需要添加using声明处，右键单击**Refactor**，选择**Add Using**完成使用using定义类型别名。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5b/v3/eBhGfD2pQaeE2rdmugQ7ug/zh-cn_image_0000002571547310.gif?HW-CC-KV=V1&HW-CC-Date=20260611T072745Z&HW-CC-Expire=86400&HW-CC-Sign=DDFF702DA5A737D42F2699111EC6A66D5A2FE44213C4CC6B45A568AC7ACC17A1)

### auto自动展开

在auto关键字处右键单击**Refactor**，选择**Expand Auto Type**，可以使用推断类型替换auto类型。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a6/v3/31P-7E14TL6T9TEoZtvTzA/zh-cn_image_0000002602066781.gif?HW-CC-KV=V1&HW-CC-Date=20260611T072745Z&HW-CC-Expire=86400&HW-CC-Sign=FDBDD2620B70910D795248C643F81224F545AC0422DAB08FFFF1503BE6CD55B2)

### 声明隐式成员

编辑器支持在类中声明隐式复制/移动成员。光标停留在需要生成的类处，右键单击**Generate**..., 选择**Copy/Move Members**。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/af/v3/r9lr1eQyROiyh-YAadmh9g/zh-cn_image_0000002571547316.gif?HW-CC-KV=V1&HW-CC-Date=20260611T072745Z&HW-CC-Expire=86400&HW-CC-Sign=6EEF3F702A0057136F2E93F8ED4804611F046159AED6611A771277A18AD161B0)
