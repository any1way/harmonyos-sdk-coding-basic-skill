# 功能路由索引

本文件提供从"用户想要做什么"到 Kit/文档路径的路由映射。当用户不知道 Kit 名称，但知道想要实现的功能时，在此文件中查找对应路径。

路径相对于 `references/` 目录。指南路径前缀 `harmonyos-guides/`，API参考前缀 `harmonyos-references/`。

## 目录

- [应用基础](#应用基础)
- [UI开发](#ui开发)
- [数据存储](#数据存储)
- [网络通信](#网络通信)
- [媒体](#媒体)
- [图形](#图形)
- [安全](#安全)
- [位置与地图](#位置与地图)
- [设备硬件](#设备硬件)
- [应用服务](#应用服务)
- [AI能力](#ai能力)
- [多设备与协同](#多设备与协同)
- [测试与调优](#测试与调优)
- [NDK开发](#ndk开发)

---

## 应用基础

用户想做什么 → Kit → 路径

| 功能需求 | Kit | 指南 | API参考 |
|----------|-----|------|---------|
| 创建应用/页面跳转/生命周期 | Ability Kit | `harmonyos-guides/应用框架/Ability Kit（程序框架服务）/` | `harmonyos-references/Ability Kit（程序框架服务）/` |
| 后台运行/长时任务/延迟任务/提醒 | Background Tasks Kit | `harmonyos-guides/应用框架/Background Tasks Kit（后台任务开发服务）/` | `harmonyos-references/Background Tasks Kit（后台任务开发服务）/` |
| 进程间通信/RPC | IPC Kit | `harmonyos-guides/应用框架/IPC Kit（进程间通信服务）/` | `harmonyos-references/IPC Kit（进程间通信服务）/` |
| 国际化/多语言/时区 | Localization Kit | `harmonyos-guides/应用框架/Localization Kit（本地化开发服务）/` | `harmonyos-references/Localization Kit（本地化开发服务）/` |
| 公共事件/线程通信/弹窗确认 | Basic Services Kit | `harmonyos-guides/系统/基础功能/Basic Services Kit（基础服务）/` | `harmonyos-references/基础功能/Basic Services Kit（基础服务）/` |
| 应用配置/包结构/签名 | — | `harmonyos-guides/基础入门/` | — |
| ArkTS 语言基础 | ArkTS | `harmonyos-guides/基础入门/学习ArkTS语言/` | `harmonyos-references/ArkTS（方舟编程语言）/` |

## UI开发

| 功能需求 | Kit | 指南 | API参考 |
|----------|-----|------|---------|
| 写界面/用组件/布局/动画 | ArkUI | `harmonyos-guides/应用框架/ArkUI（方舟UI框架）/` | `harmonyos-references/ArkUI（方舟UI框架）/` |
| 嵌入网页/Web组件 | ArkWeb | `harmonyos-guides/应用框架/ArkWeb（方舟Web）/` | `harmonyos-references/ArkWeb（方舟Web）/` |
| 开发卡片/桌面小组件 | Form Kit | `harmonyos-guides/应用框架/Form Kit（卡片开发服务）/` | `harmonyos-references/Form Kit（卡片开发服务）/` |
| 开发输入法 | IME Kit | `harmonyos-guides/应用框架/IME Kit（输入法开发服务）/` | `harmonyos-references/IME Kit（输入法开发服务）/` |
| 无障碍/辅助功能 | Accessibility Kit | `harmonyos-guides/应用框架/Accessibility Kit（无障碍服务）/` | `harmonyos-references/Accessibility Kit（无障碍服务）/` |
| 触控/按键/鼠标/触控板 | Input Kit | `harmonyos-guides/系统/基础功能/Input Kit（多模输入服务）/` | `harmonyos-references/基础功能/Input Kit（多模输入服务）/` |
| UI设计资源/图标/规范 | UI Design Kit | `harmonyos-guides/应用框架/UI Design Kit（UI设计套件）/` | `harmonyos-references/UI Design Kit（UI设计套件）/` |
| 嵌入其他应用界面 | Content Embed Kit | `harmonyos-guides/应用框架/Content Embed Kit（内容嵌入服务）/` | `harmonyos-references/Content Embed Kit（内容嵌入服务）/` |

## 数据存储

| 功能需求 | Kit | 指南 | API参考 |
|----------|-----|------|---------|
| 数据库/关系型数据库/偏好设置/数据共享 | ArkData | `harmonyos-guides/应用框架/ArkData（方舟数据管理）/` | `harmonyos-references/ArkData（方舟数据管理）/` |
| 读写文件/应用沙箱/分布式文件 | Core File Kit | `harmonyos-guides/应用框架/Core File Kit（文件基础服务）/` | `harmonyos-references/Core File Kit（文件基础服务）/` |
| 文件管理器/用户文件访问 | File Manager Service Kit | `harmonyos-guides/应用服务/File Manager Service Kit（文件管理服务）/` | `harmonyos-references/File Manager Service Kit（文件管理服务）/` |
| 安全存储密钥/密码/Token | Asset Store Kit | `harmonyos-guides/系统/安全/Asset Store Kit（关键资产存储服务）/` | `harmonyos-references/安全/Asset Store Kit（关键资产存储服务）/` |
| RAG/知识库/数据增强 | Data Augmentation Kit | `harmonyos-guides/应用框架/Data Augmentation Kit（数据增强服务）/` | `harmonyos-references/Data Augmentation Kit（数据增强服务）/` |
| 云开发/云函数/云数据库 | Cloud Foundation Kit | `harmonyos-guides/应用服务/Cloud Foundation Kit（云开发服务）/` | `harmonyos-references/Cloud Foundation Kit（云开发服务）/` |
| 剪贴板/复制粘贴 | Basic Services Kit | `harmonyos-guides/系统/基础功能/Basic Services Kit（基础服务）/剪贴板服务/` | `harmonyos-references/基础功能/Basic Services Kit（基础服务）/` |

## 网络通信

| 功能需求 | Kit | 指南 | API参考 |
|----------|-----|------|---------|
| HTTP请求/Socket/网络连接 | Network Kit | `harmonyos-guides/系统/网络/Network Kit（网络服务）/` | `harmonyos-references/网络/Network Kit（网络服务）/` |
| 蓝牙/Wi-Fi/NFC/短距通信 | Connectivity Kit | `harmonyos-guides/系统/网络/Connectivity Kit（短距通信服务）/` | `harmonyos-references/网络/Connectivity Kit（短距通信服务）/` |
| 电话/短信/蜂窝网络 | Telephony Kit | `harmonyos-guides/系统/网络/Telephony Kit（蜂窝通信服务）/` | `harmonyos-references/网络/Telephony Kit（蜂窝通信服务）/` |
| 星闪通信 | NearLink Kit | `harmonyos-guides/系统/网络/NearLink Kit（星闪服务）/` | `harmonyos-references/网络/NearLink Kit（星闪服务）/` |
| 网络加速/多网并发 | Network Boost Kit | `harmonyos-guides/系统/网络/Network Boost Kit（网络加速服务）/` | `harmonyos-references/网络/Network Boost Kit（网络加速服务）/` |
| 远场通信/HTTP长连接 | Remote Communication Kit | `harmonyos-guides/系统/网络/Remote Communication Kit（远场通信服务）/` | `harmonyos-references/网络/Remote Communication Kit（远场通信服务）/` |
| 上传下载 | Basic Services Kit | `harmonyos-guides/系统/基础功能/Basic Services Kit（基础服务）/上传下载/` | `harmonyos-references/基础功能/Basic Services Kit（基础服务）/` |

## 媒体

| 功能需求 | Kit | 指南 | API参考 |
|----------|-----|------|---------|
| 播放音频/录制音频/音量 | Audio Kit | `harmonyos-guides/媒体/Audio Kit（音频服务）/` | `harmonyos-references/Audio Kit（音频服务）/` |
| 播放视频/录制视频 | Media Kit | `harmonyos-guides/媒体/Media Kit（媒体服务）/` | `harmonyos-references/Media Kit（媒体服务）/` |
| 拍照/录像/相机预览 | Camera Kit | `harmonyos-guides/媒体/Camera Kit（相机服务）/` | `harmonyos-references/Camera Kit（相机服务）/` |
| 图片编解码/图片处理 | Image Kit | `harmonyos-guides/媒体/Image Kit（图片处理服务）/` | `harmonyos-references/Image Kit（图片处理服务）/` |
| 音视频编解码/转码 | AVCodec Kit | `harmonyos-guides/媒体/AVCodec Kit（音视频编解码服务）/` | `harmonyos-references/AVCodec Kit（音视频编解码服务）/` |
| 音视频播控/投播/会话 | AVSession Kit | `harmonyos-guides/媒体/AVSession Kit（音视频播控服务）/` | `harmonyos-references/AVSession Kit（音视频播控服务）/` |
| 媒体库/相册/音视频文件管理 | Media Library Kit | `harmonyos-guides/媒体/Media Library Kit（媒体文件管理服务）/` | `harmonyos-references/Media Library Kit（媒体文件管理服务）/` |
| 扫码/二维码/条形码 | Scan Kit | `harmonyos-guides/媒体/Scan Kit（统一扫码服务）/` | `harmonyos-references/Scan Kit（统一扫码服务）/` |
| 数字版权/DRM | DRM Kit | `harmonyos-guides/媒体/DRM Kit（数字版权保护服务）/` | `harmonyos-references/DRM Kit（数字版权保护服务）/` |
| 铃声/系统铃声 | Ringtone Kit | `harmonyos-guides/媒体/Ringtone Kit（铃声服务）/` | `harmonyos-references/Ringtone Kit（铃声服务）/` |

## 图形

| 功能需求 | Kit | 指南 | API参考 |
|----------|-----|------|---------|
| 2D绘制/Canvas/画布 | ArkGraphics 2D | `harmonyos-guides/图形/ArkGraphics 2D（方舟2D图形服务）/` | `harmonyos-references/ArkGraphics 2D（方舟2D图形服务）/` |
| 3D渲染/3D模型 | ArkGraphics 3D | `harmonyos-guides/图形/ArkGraphics 3D（方舟3D图形）/` | `harmonyos-references/ArkGraphics 3D（方舟3D图形）/` |
| AR/增强现实 | AR Engine | `harmonyos-guides/图形/AR Engine（AR引擎服务）/` | `harmonyos-references/AR Engine（AR引擎服务）/` |
| GPU加速/图形加速 | Graphics Accelerate Kit | `harmonyos-guides/图形/Graphics Accelerate Kit（图形加速服务）/` | `harmonyos-references/Graphics Accelerate Kit（图形加速服务）/` |
| 空间建模/3D重建 | Spatial Recon Kit | `harmonyos-guides/图形/Spatial Recon Kit（空间建模服务）/` | `harmonyos-references/Spatial Recon Kit（空间建模服务）/` |
| GPU渲染引擎/XEngine | XEngine Kit | `harmonyos-guides/图形/XEngine Kit（GPU加速引擎服务）/` | `harmonyos-references/XEngine Kit（GPU加速引擎服务）/` |
| OpenGL ES/Vulkan/EGL | — | — | `harmonyos-references/OpenGL ES/` / `Vulkan/` / `EGL/` |

## 安全

| 功能需求 | Kit | 指南 | API参考 |
|----------|-----|------|---------|
| 加密/解密/哈希/签名 | Crypto Architecture Kit | `harmonyos-guides/系统/安全/Crypto Architecture Kit（加解密算法框架服务）/` | `harmonyos-references/安全/Crypto Architecture Kit（加解密算法框架服务）/` |
| 密钥管理/HUKS/密钥生成 | Universal Keystore Kit | `harmonyos-guides/系统/安全/Universal Keystore Kit（密钥管理服务）/` | `harmonyos-references/安全/Universal Keystore Kit（密钥管理服务）/` |
| 指纹/人脸/生物识别 | User Authentication Kit | `harmonyos-guides/系统/安全/User Authentication Kit（用户认证服务）/` | `harmonyos-references/安全/User Authentication Kit（用户认证服务）/` |
| 设备安全/安全检测/可信环境 | Device Security Kit | `harmonyos-guides/系统/安全/Device Security Kit（设备安全服务）/` | `harmonyos-references/安全/Device Security Kit（设备安全服务）/` |
| 设备证书/证书管理 | Device Certificate Kit | `harmonyos-guides/系统/安全/Device Certificate Kit（设备证书服务）/` | `harmonyos-references/安全/Device Certificate Kit（设备证书服务）/` |
| 数据防泄漏/数据保护 | Data Protection Kit | `harmonyos-guides/系统/安全/Data Protection Kit（数据保护服务）/` | `harmonyos-references/安全/Data Protection Kit（数据保护服务）/` |
| FIDO/通行密钥/在线认证 | Online Authentication Kit | `harmonyos-guides/系统/安全/Online Authentication Kit（在线认证服务）/` | `harmonyos-references/安全/Online Authentication Kit（在线认证服务）/` |
| 企业数据保护/沙箱隔离 | Enterprise Data Guard Kit | `harmonyos-guides/系统/安全/Enterprise Data Guard Kit（企业数据保护服务）/` | `harmonyos-references/安全/Enterprise Data Guard Kit（企业数据保护服务）/` |
| 病毒防护/威胁检测 | Enterprise Threat Protection Kit | `harmonyos-guides/系统/安全/Enterprise Threat Protection Kit（企业威胁防护服务）/` | `harmonyos-references/安全/Enterprise Threat Protection Kit（企业威胁防护服务）/` |
| 权限申请/访问控制 | — | `harmonyos-guides/系统/安全/程序访问控制/` | `harmonyos-references/安全/` |

## 位置与地图

| 功能需求 | Kit | 指南 | API参考 |
|----------|-----|------|---------|
| 定位/地理围栏/位置追踪 | Location Kit | `harmonyos-guides/应用服务/Location Kit（位置服务）/` | `harmonyos-references/Location Kit（位置服务）/` |
| 地图显示/导航/POI搜索 | Map Kit | `harmonyos-guides/应用服务/Map Kit（地图服务）/` | `harmonyos-references/Map Kit（地图服务）/` |
| 融合场景/位置+地图 | Scenario Fusion Kit | `harmonyos-guides/应用服务/Scenario Fusion Kit（融合场景服务）/` | `harmonyos-references/Scenario Fusion Kit（融合场景服务）/` |

## 设备硬件

| 功能需求 | Kit | 指南 | API参考 |
|----------|-----|------|---------|
| 传感器/加速度/陀螺仪/振动 | Sensor Service Kit | `harmonyos-guides/系统/硬件/Sensor Service Kit（传感器服务）/` | `harmonyos-references/硬件/Sensor Service Kit（传感器服务）/` |
| 车载/HiCar/车机 | Car Kit | `harmonyos-guides/系统/硬件/Car Kit（车服务）/` | `harmonyos-references/硬件/Car Kit（车服务）/` |
| 手写笔/触控笔 | Pen Kit | `harmonyos-guides/系统/硬件/Pen Kit（手写笔服务）/` | `harmonyos-references/硬件/Pen Kit（手写笔服务）/` |
| 穿戴设备/手表 | Wear Engine Kit | `harmonyos-guides/系统/硬件/Wear Engine Kit（穿戴服务）/` | `harmonyos-references/硬件/Wear Engine Kit（穿戴服务）/` |
| 驱动开发/外设/HDI | Driver Development Kit | `harmonyos-guides/系统/硬件/Driver Development Kit（驱动开发服务）/` | `harmonyos-references/硬件/Driver Development Kit（驱动开发服务）/` |
| 机械设备/工业控制 | Mechanic Kit | `harmonyos-guides/系统/硬件/Mechanic Kit（机械设备管理服务）/` | `harmonyos-references/硬件/Mechanic Kit（机械设备管理服务）/` |
| 用户状态感知/多模态 | Multimodal Awareness Kit | `harmonyos-guides/系统/硬件/Multimodal Awareness Kit（多模态融合感知服务）/` | `harmonyos-references/硬件/Multimodal Awareness Kit（多模态融合感知服务）/` |
| USB服务 | Basic Services Kit | `harmonyos-guides/系统/基础功能/Basic Services Kit（基础服务）/USB服务/` | `harmonyos-references/基础功能/Basic Services Kit（基础服务）/` |
| 电源管理/省电 | Basic Services Kit | `harmonyos-guides/系统/基础功能/Basic Services Kit（基础服务）/电源管理/` | `harmonyos-references/基础功能/Basic Services Kit（基础服务）/` |
| 企业设备管理/MDM | MDM Kit | `harmonyos-guides/系统/基础功能/MDM Kit（企业设备管理服务）/` | `harmonyos-references/基础功能/MDM Kit（企业设备管理服务）/` |

## 应用服务

| 功能需求 | Kit | 指南 | API参考 |
|----------|-----|------|---------|
| 华为账号/登录 | Account Kit | `harmonyos-guides/应用服务/Account Kit（华为账号服务）/` | `harmonyos-references/Account Kit（华为账号服务）/` |
| 推送/消息推送 | Push Kit | `harmonyos-guides/应用服务/Push Kit（推送服务）/` | `harmonyos-references/Push Kit（推送服务）/` |
| 通知/本地通知 | Notification Kit | `harmonyos-guides/应用服务/Notification Kit（用户通知服务）/` | `harmonyos-references/Notification Kit（用户通知服务）/` |
| 支付/鸿蒙支付 | Payment Kit | `harmonyos-guides/应用服务/Payment Kit（鸿蒙支付服务）/` | `harmonyos-references/Payment Kit（鸿蒙支付服务）/` |
| 应用内支付/订阅 | IAP Kit | `harmonyos-guides/应用服务/IAP Kit（应用内支付服务）/` | `harmonyos-references/IAP Kit（应用内支付服务）/` |
| 广告/激励广告 | Ads Kit | `harmonyos-guides/应用服务/Ads Kit（广告服务）/` | `harmonyos-references/Ads Kit（广告服务）/` |
| 分享/跨应用分享 | Share Kit | `harmonyos-guides/应用服务/Share Kit（分享服务）/` | `harmonyos-references/Share Kit（分享服务）/` |
| 日历/日程 | Calendar Kit | `harmonyos-guides/应用服务/Calendar Kit（日历服务）/` | `harmonyos-references/Calendar Kit（日历服务）/` |
| 联系人/通讯录 | Contacts Kit | `harmonyos-guides/应用服务/Contacts Kit（联系人服务）/` | `harmonyos-references/Contacts Kit（联系人服务）/` |
| 通话/拨号 | Call Service Kit | `harmonyos-guides/应用服务/Call Service Kit（通话服务）/` | `harmonyos-references/Call Service Kit（通话服务）/` |
| 实况窗/灵动岛 | Live View Kit | `harmonyos-guides/应用服务/Live View Kit（实况窗服务）/` | `harmonyos-references/Live View Kit（实况窗服务）/` |
| 应用链接/深度链接 | App Linking Kit | `harmonyos-guides/应用服务/App Linking Kit（应用链接服务）/` | `harmonyos-references/App Linking Kit（应用链接服务）/` |
| 应用市场/上架/更新 | AppGallery Kit | `harmonyos-guides/应用服务/AppGallery Kit（应用市场服务）/` | `harmonyos-references/AppGallery Kit（应用市场服务）/` |
| 游戏服务/成就/排行榜 | Game Service Kit | `harmonyos-guides/应用服务/Game Service Kit（游戏服务）/` | `harmonyos-references/Game Service Kit（游戏服务）/` |
| 游戏手柄/控制器 | Game Controller Kit | `harmonyos-guides/应用服务/Game Controller Kit（游戏控制器服务）/` | `harmonyos-references/Game Controller Kit（游戏控制器服务）/` |
| 运动健康/步数/心率 | Health Service Kit | `harmonyos-guides/应用服务/Health Service Kit（运动健康服务）/` | `harmonyos-references/Health Service Kit（运动健康服务）/` |
| PDF阅读/生成 | PDF Kit | `harmonyos-guides/应用服务/PDF Kit（PDF服务）/` | `harmonyos-references/PDF Kit（PDF服务）/` |
| 文件预览 | Preview Kit | `harmonyos-guides/应用服务/Preview Kit（文件预览服务）/` | `harmonyos-references/Preview Kit（文件预览服务）/` |
| 阅读/电子书 | Reader Kit | `harmonyos-guides/应用服务/Reader Kit（阅读服务）/` | `harmonyos-references/Reader Kit（阅读服务）/` |
| 钱包/卡包 | Wallet Kit | `harmonyos-guides/应用服务/Wallet Kit（钱包服务）/` | `harmonyos-references/Wallet Kit（钱包服务）/` |
| 天气 | Weather Service Kit | `harmonyos-guides/应用服务/Weather Service Kit（天气服务）/` | `harmonyos-references/Weather Service Kit（天气服务）/` |
| 屏幕时间/家长控制 | Screen Time Guard Kit | `harmonyos-guides/应用服务/Screen Time Guard Kit（屏幕时间守护服务）/` | `harmonyos-references/Screen Time Guard Kit（屏幕时间守护服务）/` |
| 企业空间/工作空间 | Enterprise Space Kit | `harmonyos-guides/应用服务/Enterprise Space Kit（企业数字空间服务）/` | `harmonyos-references/Enterprise Space Kit（企业数字空间服务）/` |
| 打印 | Basic Services Kit | `harmonyos-guides/系统/基础功能/Basic Services Kit（基础服务）/打印/` | `harmonyos-references/基础功能/Basic Services Kit（基础服务）/` |
| 压缩解压 | Basic Services Kit | `harmonyos-guides/系统/基础功能/Basic Services Kit（基础服务）/压缩与解压/` | `harmonyos-references/基础功能/Basic Services Kit（基础服务）/` |

## AI能力

| 功能需求 | Kit | 指南 | API参考 |
|----------|-----|------|---------|
| 语音识别/语音合成/TTS/ASR | Core Speech Kit / Speech Kit | `harmonyos-guides/AI/Core Speech Kit（基础语音服务）/` 或 `Speech Kit（场景化语音服务）/` | `harmonyos-references/Core Speech Kit（基础语音服务）/` / `Speech Kit（场景化语音服务）/` |
| 文字识别/OCR/图像识别 | Core Vision Kit / Vision Kit | `harmonyos-guides/AI/Core Vision Kit（基础视觉服务）/` 或 `Vision Kit（场景化视觉服务）/` | `harmonyos-references/Core Vision Kit（基础视觉服务）/` / `Vision Kit（场景化视觉服务）/` |
| 自然语言处理/分词/实体识别 | Natural Language Kit | `harmonyos-guides/AI/Natural Language Kit（自然语言理解服务）/` | `harmonyos-references/Natural Language Kit（自然语言理解服务）/` |
| 端侧推理/模型部署/MindSpore | MindSpore Lite Kit | `harmonyos-guides/AI/MindSpore Lite Kit（昇思推理框架服务）/` | `harmonyos-references/MindSpore Lite Kit（昇思推理框架服务）/` |
| 神经网络/NNRT | Neural Network Runtime Kit | `harmonyos-guides/AI/Neural Network Runtime Kit（Neural Network运行时服务）/` | `harmonyos-references/Neural Network Runtime Kit（Neural Network运行时服务）/` |
| 智能体/Agent/AI应用 | Agent Framework Kit | `harmonyos-guides/AI/Agent Framework Kit（智能体框架服务）/` | `harmonyos-references/Agent Framework Kit（智能体框架服务）/` |
| 意图框架/意图识别 | Intents Kit | `harmonyos-guides/AI/Intents Kit（意图框架服务）/` | `harmonyos-references/Intents Kit（意图框架服务）/` |
| 异构计算/CANN/NPU | CANN Kit | `harmonyos-guides/AI/CANN Kit（CANN异构计算框架服务）/` | `harmonyos-references/CANN Kit（CANN异构计算框架服务）/` |

## 多设备与协同

| 功能需求 | Kit | 指南 | API参考 |
|----------|-----|------|---------|
| 跨设备连接/设备发现/分布式 | Distributed Service Kit | `harmonyos-guides/系统/网络/Distributed Service Kit（分布式管理服务）/` | `harmonyos-references/网络/Distributed Service Kit（分布式管理服务）/` |
| 跨设备协同/流转 | Service Collaboration Kit | `harmonyos-guides/系统/网络/Service Collaboration Kit（协同服务）/` | `harmonyos-references/网络/Service Collaboration Kit（协同服务）/` |
| 分布式文件/跨设备文件 | Core File Kit | `harmonyos-guides/应用框架/Core File Kit（文件基础服务）/分布式文件系统/` | `harmonyos-references/Core File Kit（文件基础服务）/` |
| 桌面拓展/状态栏 | Desktop Extension Kit | `harmonyos-guides/系统/基础功能/Desktop Extension Kit（桌面拓展服务）/` | `harmonyos-references/基础功能/Desktop Extension Kit（桌面拓展服务）/` |
| 多端适配/一次开发多端部署 | — | `best-practices/一次开发，多端部署/` | — |
| 自由流转/跨端迁移 | — | `best-practices/自由流转/` | — |

## 测试与调优

| 功能需求 | Kit | 指南 | API参考 |
|----------|-----|------|---------|
| 性能分析/HiLog/HiTrace/调试 | Performance Analysis Kit | `harmonyos-guides/系统/调测调优/Performance Analysis Kit（性能分析服务）/` | `harmonyos-references/调测调优/Performance Analysis Kit（性能分析服务）/` |
| 单元测试/UI测试 | Test Kit | `harmonyos-guides/应用测试/` | `harmonyos-references/调测调优/Test Kit（应用测试服务）/` |
| hdc命令/调试命令 | — | `harmonyos-guides/系统/调测调优/调试命令/` | — |
| 功耗优化 | — | `best-practices/功耗/` | — |
| 算法加速 | FAST Kit | `harmonyos-guides/系统/基础功能/FAST Kit（算法加速服务）/` | `harmonyos-references/基础功能/FAST Kit（算法加速服务）/` |
| 任务并发调度/FFRT | Function Flow Runtime Kit | `harmonyos-guides/系统/基础功能/Function Flow Runtime Kit（任务并发调度服务）/` | `harmonyos-references/基础功能/Function Flow Runtime Kit（任务并发调度服务）/` |

## NDK开发

| 功能需求 | Kit | 指南 | API参考 |
|----------|-----|------|---------|
| C/C++开发/NDK工程 | — | `harmonyos-guides/NDK开发/` | — |
| Node-API/JS与C++交互 | Node-API | `harmonyos-guides/NDK开发/` | `harmonyos-references/Node-API/` |
| C API参考 | — | — | `harmonyos-references/C API/` |
| C++标准库/libc | — | `harmonyos-guides/NDK开发/C和C++标准库/` | `harmonyos-references/c++标准库/` / `libc标准库/` |
| libuv/zlib/ICU4C | — | — | `harmonyos-references/libuv/` / `zlib/` / `ICU4C/` |
| OpenSL ES音频 | — | — | `harmonyos-references/OpenSL ES/` |
