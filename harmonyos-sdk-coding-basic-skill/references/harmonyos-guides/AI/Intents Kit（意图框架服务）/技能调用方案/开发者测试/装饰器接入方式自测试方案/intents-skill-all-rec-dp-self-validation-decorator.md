---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/intents-skill-all-rec-dp-self-validation-decorator
title: 装饰器接入方式自测试方案
breadcrumb: 指南 > AI > Intents Kit（意图框架服务） > 技能调用方案 > 开发者测试 > 装饰器接入方式自测试方案
category: harmonyos-guides
scraped_at: 2026-06-11T15:18:56+08:00
doc_updated_at: 2026-04-29
content_hash: sha256:67f55060109d4817a7335374af418d5f4ceae10c7bc79e27218c04d58285fe0c
---

从6.0.0(20)开始，Intents Kit向开发者提供意图调用调试能力。开发者完成代码开发之后，功能正式上架应用市场前，可以在HarmonyOS 5及以上的设备上面进行自验证，调试分为两个步骤：环境准备和联调验证。

## 环境准备

1. 登录[华为开发者联盟](https://developer.huawei.com/consumer/cn/) ，通过“管理中心 > 生态服务 > 智慧服务 > 小艺开放平台（原HarmonyOS服务开放平台） > 意图框架”，点击“立即体验”进入意图注册入口，需使用与应用上架相同的账号登录。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d3/v3/HYMr9uRtS5uvPjTBZcZGyw/zh-cn_image_0000002622859211.png?HW-CC-KV=V1&HW-CC-Date=20260611T071853Z&HW-CC-Expire=86400&HW-CC-Sign=5B620010F4C22A8E94BA0AC350503039A354C41494C81746CEC11B2764B7ADE7)

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8/v3/t8PgBFhxRxK1h2PUeO7A7A/zh-cn_image_0000002622699331.png?HW-CC-KV=V1&HW-CC-Date=20260611T071853Z&HW-CC-Expire=86400&HW-CC-Sign=F71774903B8065BAAE75CA13D162A3490069DACDFAA44ED6CCAD12C034B2EE40)
2. 点击注册意图新增意图集。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3c/v3/UUywqjapRX67-3prpMrLGw/zh-cn_image_0000002592219770.png?HW-CC-KV=V1&HW-CC-Date=20260611T071853Z&HW-CC-Expire=86400&HW-CC-Sign=62911503BD876A5C30B6B471A5142C217E994D4249AF7DBF989EEC11B72BCA20)

   1. 点击新增注册意图，填写注册信息进行创建。

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/65/v3/OeI9R8NrRl6IsCzvxLJQ0Q/zh-cn_image_0000002592379704.png?HW-CC-KV=V1&HW-CC-Date=20260611T071853Z&HW-CC-Expire=86400&HW-CC-Sign=0A042333667B436186AC8BFB0586EF95E6754EEDE179B0FCF835831E87982C7B)

      | 名称 | 描述 |
      | --- | --- |
      | 意图注册协议类型 | 选择意图标准协议。 |
      | 意图集（插件）名称 | 需唯一标识。 |
      | 分类 | 开发者根据自定义意图选择对应垂域。 |
   2. 编辑意图集基本信息。

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f5/v3/vz7PbYPwQGGipQIW8zsebA/zh-cn_image_0000002622859213.png?HW-CC-KV=V1&HW-CC-Date=20260611T071853Z&HW-CC-Expire=86400&HW-CC-Sign=ADEF2855B25EDCFBE6944DF4FB78987E6B2C4C38FD1F6B3424AF891EA8D9739D)

      | 名称 | 描述 |
      | --- | --- |
      | 意图注册名称 | 填写应用名称。 |
      | APP名称 | 填写应用名称。 |
      | 关联APP | 选择需要进行测试的应用。 |
      | 支持的设备类型 | 选择手机、平板、PC。 |
      | 版本号 | 开发者自定义，仅支持正整数。 |
      | 版本描述 | 开发者自定义，该内容不对外展示。 |
      | 图标 | 尺寸：72\*72（1:1）  格式：png、jpg、jpeg  样式要求：方角、不透明背景 |
3. 添加意图。

   1. 切换至意图页签并添加意图。

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/eb/v3/r3G6eZt1Ql-qZNSGXnhSpQ/zh-cn_image_0000002622699333.png?HW-CC-KV=V1&HW-CC-Date=20260611T071853Z&HW-CC-Expire=86400&HW-CC-Sign=014A011BA54D8F411D1176B2FCBFC8CAAE4A67074A1DFE399CF8390E62642578)
   2. 选择自定义意图并填入意图信息（根据接入方案进行填入）并确定。

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c1/v3/xklSrW9ZTNaLqbQACfId4Q/zh-cn_image_0000002592219772.png?HW-CC-KV=V1&HW-CC-Date=20260611T071853Z&HW-CC-Expire=86400&HW-CC-Sign=5137995E59C5BBBB79856BDAED162E5519231E7F33D5D4FC1D73FF433A113CB6)
   3. 展开已创建的意图，并填入自定义输入、输出参数，点击保存。

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/62/v3/4oWskiMfRt6Ot0vJL0ryig/zh-cn_image_0000002592379706.png?HW-CC-KV=V1&HW-CC-Date=20260611T071853Z&HW-CC-Expire=86400&HW-CC-Sign=EB4A89D00613892E8C5E35AA26E792A70EFAB2FA2643C9AA1BF095BD85268D65)
4. 添加意图使用样本（意图样本用于提升模型对意图识别的准确率）。

   1. 意图使用样本可通过新增/批量导入进行上传。
   2. 若无需添加意图使用样本，打开是否已提供线下样本开关即可。

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fb/v3/3MGxj_IrQSeuzNiUSx-PiA/zh-cn_image_0000002622859215.png?HW-CC-KV=V1&HW-CC-Date=20260611T071853Z&HW-CC-Expire=86400&HW-CC-Sign=710E42E371190ACA55851E71D469CF6DA27EFFBB2022B5AFC69CF02E3AEF7C09)
5. 添加账号至真机测试用户组。

   1. 切换至测试页签，点击编辑用户组。

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8f/v3/NW0gWbytRb6XjtCd-RfDXA/zh-cn_image_0000002622699335.png?HW-CC-KV=V1&HW-CC-Date=20260611T071853Z&HW-CC-Expire=86400&HW-CC-Sign=95927FC147DF8C8D53BA207BACDCED6EC906E08507AC0AE456F9A890C8F4970F)
   2. 点击新增组，输入新用户组名称（名称自定义）。

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dd/v3/xEhFq6uXRK-dMGkSUgri8g/zh-cn_image_0000002592219774.png?HW-CC-KV=V1&HW-CC-Date=20260611T071853Z&HW-CC-Expire=86400&HW-CC-Sign=B5172CB0FF2C7E6D1248A5C1B6000D4865F922F5A7F7A63D13C982ECB70722FB)
   3. 选择已新增用户组，点击查看进入。

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/13/v3/MCC3Eh9HStSHacNIJJX3Jw/zh-cn_image_0000002592379708.png?HW-CC-KV=V1&HW-CC-Date=20260611T071853Z&HW-CC-Expire=86400&HW-CC-Sign=555E685F1F517DABD0E247CDB45C2ED6566326F5F3D36FC3A0D41E30D24667BD)
   4. 点击添加用户，选择账号类型为邮箱/手机号码，填入后点击确定（测试用户须为该项目团队下的成员）。

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a4/v3/MxPtOxFXSJmlnlM9PiE6Wg/zh-cn_image_0000002622859217.png?HW-CC-KV=V1&HW-CC-Date=20260611T071853Z&HW-CC-Expire=86400&HW-CC-Sign=01D8CA2B19B8DEF962B08A514475FDC5BE2E42C003F44509EC82B583833C06EB)
   5. 返回测试页签，选择所创建的真机测试用户组进行保存，点击开始测试准备，开发者即可通过HarmonyOS 6.0.0(20)版本及以上的设备在小艺进行端到端测试。

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6d/v3/6UPlK0JfQheDPL8K8bC4fw/zh-cn_image_0000002622699337.png?HW-CC-KV=V1&HW-CC-Date=20260611T071853Z&HW-CC-Expire=86400&HW-CC-Sign=9EF4F24009B21EC1D81A82B8CE689191A74061834546D66E3323D7B54E21B5E2)

## 联调验证

1. 开发者需确认调试设备系统版本为HarmonyOS 6.0.0(20)及以上。
2. 在调试设备上登录已添加真机测试用户组的华为账号。
3. 检查小艺App是否为应用市场最新版本（需升级至最新版）。
4. 长按电源键/语音唤起小艺，通过小艺进行自验证。

   1. 开发者预期：用户可通过小艺打开应用内页面并传递参数。
   2. 开发者验证：正常跳转目标落地页并收到对应参数。
