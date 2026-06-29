---
name: harmonyos-sdk-coding-basic-skill
description: HarmonyOS SDK 开发指南文档检索与路由技能。当用户询问任何与 HarmonyOS/鸿蒙/方舟开发相关的问题时，使用此技能定位和检索官方文档。触发场景包括但不限于：HarmonyOS API 用法查询、ArkTS/ArkUI开发指导、Kit 功能说明、鸿蒙开发 FAQ 排查、最佳实践参考、版本变更与兼容性查询。即使用户只是提到"鸿蒙"、"HarmonyOS"、"ArkUI"、"ArkTS"、"方舟"、"DevEco Studio"、"OHOS"、"OpenHarmony"、"HarmonyOS NEXT"等关键词，也应触发此技能。当用户需要编写、调试、优化鸿蒙应用代码，或查找任何 HarmonyOS 平台能力说明时，此技能提供精确的文档路径路由，避免盲目搜索。
---

# HarmonyOS SDK 文档技能

本技能管理 HarmonyOS 全量开发文档的检索与路由。文档按官网层级结构存储在本地，每个 `.md` 文件对应一篇官方文档，包含 YAML frontmatter 元数据（url、title、breadcrumb、category）。

为什么需要这个技能：HarmonyOS 文档量巨大（11000+ 篇），分布在五大分类、数十个 Kit 目录中。直接搜索效率极低，需要根据用户需求类型快速定位到正确的分类和 Kit 目录。

## 文档仓库结构

所有文档位于 `references/` 目录下，共 11033 篇，分为五大类：

| 分类 | 目录 | 文档数 | 解决什么问题 |
|------|------|--------|-------------|
| 开发指南 | `references/harmonyos-guides/` | ~4000 | "怎么做" — 按领域/Kit组织的开发指导 |
| API参考 | `references/harmonyos-references/` | ~4500 | "接口是什么" — ArkTS/C/JS API 详细参考 |
| FAQ | `references/harmonyos-faqs/` | ~400 | "遇到问题怎么办" — 常见问题与解答 |
| 最佳实践 | `references/best-practices/` | ~500 | "怎么做得更好" — 场景化最佳实践案例 |
| 版本说明 | `references/harmonyos-releases/` | ~1600 | 版本变更、兼容性、升级指导 |


## 检索流程

根据用户需求，按以下优先级检索：

### 第一步：判断需求类型

| 用户意图 | 优先检索分类 |
|----------|-------------|
| "怎么做XXX"、"如何实现XXX"、"开发XXX" | 开发指南 → 最佳实践 |
| "XXX API"、"XXX 接口"、"XXX 方法" | API参考 |
| "XXX 报错"、"XXX 不工作"、"XXX 问题" | FAQ → 开发指南 |
| "XXX 最佳实践"、"XXX 优化" | 最佳实践 → 开发指南 |
| "版本变更"、"API 变更"、"升级适配" | 版本说明 |
| 不确定 | 直接用 `python scripts/search_hybrid.py "<关键词>"` 做全量 Hybrid 检索（见第三步） |

### 第二步：定位 Kit 目录

有两种定位方式，根据用户描述选择：

**方式 A：用户提到 Kit 名称** — 查阅 `references/kit-routing.md`，该文件包含 103 个 Kit 的完整路由映射。

常用 Kit 快速路由（无需查阅参考文件）：

| Kit | 指南 | API参考 |
|-----|------|---------|
| ArkUI | `harmonyos-guides/应用框架/ArkUI（方舟UI框架）/` | `harmonyos-references/ArkUI（方舟UI框架）/` |
| ArkTS | `harmonyos-guides/基础入门/学习ArkTS语言/` | `harmonyos-references/ArkTS（方舟编程语言）/` |
| ArkWeb | `harmonyos-guides/应用框架/ArkWeb（方舟Web）/` | `harmonyos-references/ArkWeb（方舟Web）/` |
| Audio Kit | `harmonyos-guides/媒体/Audio Kit（音频服务）/` | `harmonyos-references/Audio Kit（音频服务）/` |
| Camera Kit | `harmonyos-guides/媒体/Camera Kit（相机服务）/` | `harmonyos-references/Camera Kit（相机服务）/` |
| Network Kit | `harmonyos-guides/系统/网络/` | `harmonyos-references/网络/Network Kit（网络服务）/` |
| Form Kit | `harmonyos-guides/应用框架/Form Kit（卡片开发服务）/` | `harmonyos-references/Form Kit（卡片开发服务）/` |

更多 Kit（Account Kit、Ads Kit、DRM Kit、IME Kit、Location Kit、Push Kit 等 30+ 个）见 `references/kit-routing.md`。

**方式 B：用户只描述功能需求，不知道 Kit 名称** — 查阅 `references/feature-routing.md`，该文件按 14 个功能领域组织，从"用户想做什么"路由到对应的 Kit 和文档路径。例如用户说"我想播放音频"，在 feature-routing.md 的"媒体"分类下找到 Audio Kit 的路径。

功能领域概览：应用基础、UI开发、数据存储、网络通信、媒体、图形、安全、位置与地图、设备硬件、应用服务、AI能力、多设备与协同、测试与调优、NDK开发。

### 第三步：检索与读取

使用本技能内置的 **Hybrid 检索工具**（BM25 + Dense + RRF 融合）在全量文档（12000+ 篇）中精准定位 Top N 最相关文档，再读取正文综合回答。

#### 工具位置

**推荐：Hybrid 检索（语义 + 关键词）**
- Dense 索引构建：[scripts/build_dense_index.py](scripts/build_dense_index.py)
- Hybrid 检索入口：[scripts/search_hybrid.py](scripts/search_hybrid.py)
- 索引产物：`scripts/index/`（含 BM25 与 Dense 两套索引）

**快速回退：纯 BM25 检索（无依赖）**
- BM25 索引构建：[scripts/build_index.py](scripts/build_index.py)
- BM25 检索入口：[scripts/search.py](scripts/search.py)

#### 检索命令

```bash
# 推荐：Hybrid 检索（BM25 + Dense 融合，支持语义泛化）
python scripts/search_hybrid.py "怎么让应用启动更快" --top 8 --snippet

# 纯关键词精确匹配（API 名、类名等）
python scripts/search.py "AVPlayer setURL" --top 5 --snippet

# 限定分类（guides / api / faq / best / release）
python scripts/search_hybrid.py "状态管理" --category api --top 8

# 调整融合权重（BM25 更重 0.7 : Dense 0.3）
python scripts/search_hybrid.py "AVPlayer" --weights 0.7 0.3 --top 5

# 机器可读 JSON 输出
python scripts/search_hybrid.py "音频播放" --top 5 --json
```

> **首次运行 Hybrid 检索**：若 Dense 索引缺失会自动触发构建（约 10 分钟，含模型加载与 12000 篇文档编码），之后查询通常在 200–500ms 内返回（含 query 编码）。纯 BM25 检索在 20ms 内返回，无依赖。

#### 标准检索流程

1. **构造查询** — 从用户问题中提取核心意图。可直接用自然语言描述（如"怎么让应用启动更快"），Hybrid 的 Dense 通道会做语义匹配；也可提取关键词（如"AVPlayer 播放音频"），BM25 通道做精确匹配。两路融合后兼顾语义泛化与精确召回。
2. **执行检索** — 运行 `python scripts/search_hybrid.py "<查询>" --top 8 --snippet`，获取按 RRF 融合分数排序的候选文档列表（含路径、标题、面包屑、BM25 rank/score、Dense rank/score、上下文片段）。
3. **读取 Top 文档** — 根据融合得分与摘要，用 Read 工具读取排名靠前的 1–3 篇 `.md` 文档完整正文（路径相对 `references/` 目录，需要拼接为绝对路径）。
4. **跨分类综合** — 同一主题跨分类时，可分别检索 guides/api/faq/best 多个分类（用 `--category` 过滤），综合"指南怎么做 + API 是什么 + FAQ 排错 + 最佳实践"给出完整回答。
5. **回退策略** — 若 Top N 命中不佳：纯关键词查询改用 `search.py`；语义查询调整 `--weights` 提高 Dense 权重；或查阅 `references/feature-routing.md` 按功能领域路由。

#### 输出示例

```
Hybrid Top 5 results for "怎么让应用启动更快" (searched 12232 docs in 0.4s)

[1] rrf=0.0082  best  best-practices/性能/性能场景优化案例/应用启动与响应优化/应用冷启动时延优化/bpta-application-cold-start-optimization.md
    BM25 rank=None score=None | Dense rank=1 score=0.6688
    Title: 应用冷启动时延优化
    Breadcrumb: 最佳实践 > 性能 > 性能场景优化案例 > 应用启动与响应优化 > 应用冷启动时延优化
    Snippet: 概述 应用启动时延是影响用户体验的关键要素...
[2] rrf=0.0082  faq  harmonyos-faqs/应用框架开发/程序框架/程序框架（Ability）/faqs-ability-kit.md
    BM25 rank=1 score=42.2075 | Dense rank=None score=None
    ...
```

> Dense rank=1 命中"应用冷启动时延优化"，这是纯 BM25 无法召回的语义匹配（查询词"启动更快"与文档标题"冷启动时延优化"字面不同但语义相同）。

#### 为什么用 Hybrid（BM25 + Dense + RRF）

- **语义泛化**：BM25 仅靠词项统计，遇同义词、改写、跨语言即失效；Dense（BGE 向量）能理解"启动更快≈冷启动时延优化"的语义相似。
- **精确匹配**：Dense 对 API 名、类名等精确字符串不如 BM25 敏感（如 "AVPlayer setURL" 这种字面查询）。
- **融合互补**：RRF（Reciprocal Rank Fusion）取两路 Top 30，按 `1/(k+rank)` 融合，兼顾语义召回与精确命中，业界主流方案。
- **效率**：BM25 查询 20ms，Dense 查询（含 query 编码）200–500ms，整体可在 1s 内完成。

#### 模型与依赖

- **Dense 模型**：`BAAI/bge-small-zh-v1.5`（24M 参数，512 维，Apache-2.0），CPU 友好。
  - 选 small 而非 m3（568M）：CPU 推理速度差 ~20x（10 分钟 vs 3+ 小时），Top-N 召回场景精度差距可接受。
  - 通过 ModelScope 下载，约 100MB。
- **依赖**：torch（CPU 版）+ transformers + faiss-cpu + numpy，约 2GB。
- **纯 BM25 回退**：若未安装上述依赖，`search.py` 仍可独立使用（纯 Python 标准库）。

#### 索引维护

- **BM25 索引**：`search.py` 启动时自动检测 `references/` 最新 mtime，过期则自动重建；强制重建用 `python scripts/build_index.py --force`（约 1 分钟）。
- **Dense 索引**：`search_hybrid.py` 启动时检测 Dense 索引是否存在，缺失则自动构建；强制重建用 `python scripts/build_dense_index.py --force`（约 10 分钟）。
- **索引规模**：BM25 约 110MB（docs.pkl + inverted.pkl），Dense 约 24MB（vectors.npy + faiss.index），合计 ~134MB。
- **文档对齐**：两套索引通过文档 `path` 字段对齐 doc_id，RRF 融合时按 path 匹配。

## 开发指南目录索引

开发指南按领域组织，每个领域下包含相关 Kit 和功能模块：

- **基础入门** — 快速入门、学习ArkTS语言、HarmonyOS术语
- **开发环境搭建** — DevEco Studio、工程创建、离线配置
- **应用框架** — ArkTS、ArkUI、ArkData、ArkWeb、Form Kit、IME Kit、IPC Kit
- **媒体** — Audio Kit、Camera Kit、Media Kit、Image Kit、DRM Kit
- **系统** — 安全、网络、硬件、基础功能、调测调优
- **编写与调试应用** — 代码编辑、应用调试、界面预览、签名配置
- **构建应用** — 混淆加固、构建报错排查、构建效率
- **NDK开发** — 创建/构建NDK工程、代码开发、编译工具链
- **应用测试** — 单元测试、UI测试、专项测试
- **发布应用** — 签名与发布流程
- **优化应用性能** — 性能分析与优化
- **使用AI智能辅助编程** — AI辅助开发

## API参考目录索引

API参考按 Kit 组织，包含 ArkTS API、C API、ArkTS组件等类型：

- **应用框架类** — Ability Kit、ArkData、ArkTS、ArkUI、ArkWeb、Form Kit、IME Kit、IPC Kit
- **媒体类** — Audio Kit、AVCodec Kit、Camera Kit、DRM Kit、Image Kit、Media Kit、Media Library Kit
- **图形类** — ArkGraphics 2D/3D、EGL、OpenGL/ES、Vulkan、XEngine Kit
- **安全类** — Asset Store Kit、Crypto Architecture Kit、Device Certificate/Security Kit、Online Authentication Kit
- **网络/通信类** — Network Kit、NearLink Kit
- **系统基础类** — Basic Services Kit、FAST Kit、Input Kit、MDM Kit、Test Kit
- **硬件类** — Car Kit、Pen Kit
- **应用服务类** — Account/Ads/AppGallery/Calendar/IAP/Intents/Live View/Location/Map/Payment/Push/Scan/Share Kit
- **AI类** — CANN/MindSpore Lite/Neural Network Runtime/Natural Language/Core Speech/Vision/Speech/Data Augmentation Kit
- **NDK/C/C++基础库** — Node-API、C API、c++/libc标准库、libuv、zlib、ICU4C、OpenSL ES

详细的 Kit 与 API 类型对应关系见 `references/kit-routing.md`。

## FAQ 目录索引

- **DevEco Studio** — 代码编辑、工程管理、编译构建、应用调试/运行/测试、性能分析、签名服务
- **应用框架开发** — ArkTS语言、UI框架（ArkUI）、Web框架、本地数据和文件、程序框架/包结构、NDK开发
- **媒体开发** — 拍照和图片、音频和视频
- **系统开发** — 基础功能、安全、网络、硬件

## 最佳实践目录索引

- **应用架构** — 分层架构设计、模块化设计
- **应用框架** — ArkTS语言、ArkWeb、数据和文件、服务卡片
- **声明式语法** — 状态管理、组件冗余刷新
- **布局与弹窗** — 长列表、瀑布流、网格、轮播图、Tabs、弹窗、富文本编辑器
- **动画与转场** — 动画使用、页面间转场、一镜到底动效
- **图形** — GPU加速、图像处理、图形绘制
- **媒体** — 图片、相机、音频和视频
- **应用安全** — 安全编码、代码混淆、数据安全、权限申请、隐私保护
- **功耗** — 功耗优化、分析、检测
- **NDK开发** — 子线程通信、三方库集成、跨语言调用
- **一次开发，多端部署** — 多设备界面/功能开发、工程部署

## 版本说明

当前版本：HarmonyOS 6.0.0(20) ~ 6.1.1(24) Beta，历史版本回溯至 5.0.0(12)。

每个版本目录包含：版本概览、DevEco Studio 变更、DevEco Testing 变更、OS平台能力 API 变更清单。

兼容性与升级：`harmonyos-releases/应用兼容性说明/`、`harmonyos-releases/应用升级适配指导/`

## 新建工程

本技能提供了一个 HarmonyOS 工程模板（`assets/template/`）及配套新建工程指南，详见 [new-project.md](references/new-project.md)。

## 构建工程

Hvigor 命令行构建 HarmonyOS 工程的详细说明，包括命令参数、环境变量、常见错误处理，详见 [build-project.md](references/build-project.md)。

## 运行工程

安装和启动 HarmonyOS 应用的命令说明，包括设备连接、HAP 安装、应用启动和日志查看，详见 [run-project.md](references/run-project.md)。

## 文档路径格式

所有文档路径相对于 `references/` 目录：

```
references/
├── harmonyos-guides/          # 开发指南
│   └── {领域}/{Kit名（中英文）}/{功能}/{文档名}.md
├── harmonyos-references/      # API参考
│   └── {Kit名（中英文）}/{API类型}/{模块}/{文档名}.md
├── harmonyos-faqs/            # FAQ
│   └── {开发领域}/{子领域}/{faq-xxx-N}.md
├── best-practices/            # 最佳实践
│   └── {主题}/{场景}/{bpta-xxx}.md
├── harmonyos-releases/        # 版本说明
│   └── HarmonyOS {版本}/{子目录}/{文档名}.md
└── INDEX.md                   # 全量索引
```
