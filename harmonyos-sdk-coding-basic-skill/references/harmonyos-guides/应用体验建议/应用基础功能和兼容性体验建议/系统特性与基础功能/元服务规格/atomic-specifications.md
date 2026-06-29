---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/atomic-specifications
title: 元服务规格
breadcrumb: 指南 > 应用体验建议 > 应用基础功能和兼容性体验建议 > 系统特性与基础功能 > 元服务规格
category: harmonyos-guides
scraped_at: 2026-06-01T15:28:29+08:00
doc_updated_at: 2026-01-19
content_hash: sha256:fc2a73db81dcbbb754fa3ce2291acbb639696deeb83d4003f4f342950c0dc05a
---
|  |  |
| --- | --- |
| **描述** | 元服务内所有包总和大小不超过10MB。 |
| **类型** | 规则 |
| **适用设备** | 通用 |
| **应用形态适用性** | 鸿蒙元服务 |
| **说明** | [元服务程序包基础知识](https://developer.huawei.com/consumer/cn/doc/atomic-guides/atomic-service-package-basics) |

|  |  |
| --- | --- |
| **描述** | 元服务单个包文件大小不超过2MB。 |
| **类型** | 规则 |
| **适用设备** | 通用 |
| **应用形态适用性** | 鸿蒙元服务 |
| **说明** | [元服务程序包基础知识](https://developer.huawei.com/consumer/cn/doc/atomic-guides/atomic-service-package-basics) |

|  |  |
| --- | --- |
| **描述** | 元服务只能使用元服务API。 |
| **类型** | 规则 |
| **适用设备** | 通用 |
| **应用形态适用性** | 鸿蒙元服务 |
| **说明** | [元服务API说明](https://developer.huawei.com/consumer/cn/doc/atomic-references/atomic-apis-intro) |

|  |  |
| --- | --- |
| **描述** | 元服务仅支持免安装。 |
| **类型** | 规则 |
| **适用设备** | 通用 |
| **应用形态适用性** | 鸿蒙元服务 |
| **说明** | [应用配置文件（Stage模型）-module.json5配置文件](../../../../基础入门/开发基础知识/应用配置文件（Stage模型）/module.json5配置文件/module-configuration-file.md) |

|  |  |
| --- | --- |
| **描述** | 元服务预加载对应模块类型不能为entry。 |
| **类型** | 规则 |
| **适用设备** | 通用 |
| **应用形态适用性** | 鸿蒙元服务 |
| **说明** | [预加载](https://developer.huawei.com/consumer/cn/doc/atomic-guides/atomic-preparing-for-loading) |

|  |  |
| --- | --- |
| **描述** | 元服务涉及账号体系和登录能力时，需使用华为账号能力进行静默登录。 |
| **类型** | 规则 |
| **适用设备** | 通用 |
| **应用形态适用性** | 鸿蒙元服务 |
| **说明** | [元服务登录](https://developer.huawei.com/consumer/cn/doc/design-guides/accounts-0000001967444380) |

|  |  |
| --- | --- |
| **描述** | 元服务用户界面禁止出现微信、安卓相关字眼和图标。 |
| **类型** | 推荐 |
| **适用设备** | 通用 |
| **应用形态适用性** | 鸿蒙元服务 |
| **说明** | 无 |

|  |  |
| --- | --- |
| **描述** | 元服务用户界面禁止出现提示跳转或诱导至APP、微信小程序、快应用进行转化和下单行为。 |
| **类型** | 规则 |
| **适用设备** | 通用 |
| **应用形态适用性** | 鸿蒙元服务 |
| **说明** | 无 |

|  |  |
| --- | --- |
| **描述** | 元服务要求有且仅有一个UIAbility，并且该UIAbility只能在entry模块，启动模式需要设置为单例模式，mainElement指向唯一的UIAbility的Name。 |
| **类型** | 规则 |
| **适用设备** | 通用 |
| **应用形态适用性** | 鸿蒙元服务 |
| **说明** | 无 |

|  |  |
| --- | --- |
| **描述** | 元服务链接打开只支持短链形式，不支持deeplinking和开发者自认证的applinking，禁止声明隐式跳转。 |
| **类型** | 规则 |
| **适用设备** | 通用 |
| **应用形态适用性** | 鸿蒙元服务 |
| **说明** | [元服务不支持隐式跳转](https://developer.huawei.com/consumer/cn/doc/atomic-guides/start-other-atomicservices) |

|  |  |
| --- | --- |
| **描述** | 元服务禁止使用arkWeb组件，涉及网页显示需使用AtomicServiceWeb。 |
| **类型** | 规则 |
| **适用设备** | 通用 |
| **应用形态适用性** | 鸿蒙元服务 |
| **说明** | [使用元服务Web组件](https://developer.huawei.com/consumer/cn/doc/atomic-guides/atomicserviceweb-guidelines) |

|  |  |
| --- | --- |
| **描述** | 元服务需要按规范使用场景化Button组件。 |
| **类型** | 规则 |
| **适用设备** | 通用 |
| **应用形态适用性** | 鸿蒙元服务 |
| **说明** | [场景化Button](<../../../../应用服务/Scenario Fusion Kit（融合场景服务）/场景化Button/scenario-fusion-button.md>) |

|  |  |
| --- | --- |
| **描述** | 元服务需要合理设计申请手机号授权功能。 |
| **类型** | 规则 |
| **适用设备** | 通用 |
| **应用形态适用性** | 鸿蒙元服务 |
| **说明** | [快速验证手机号Button](<../../../../应用服务/Scenario Fusion Kit（融合场景服务）/场景化Button/快速验证手机号Button/scenario-fusion-button-getphonenumber.md>) |

|  |  |
| --- | --- |
| **描述** | 元服务需要规范使用华为账号头像Button。 |
| **类型** | 建议 |
| **适用设备** | 通用 |
| **应用形态适用性** | 鸿蒙元服务 |
| **说明** | [选择头像Button](<../../../../应用服务/Scenario Fusion Kit（融合场景服务）/场景化Button/选择头像Button/scenario-fusion-button-chooseavatar.md>) |
