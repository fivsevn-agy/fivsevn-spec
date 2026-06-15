# Content Frontmatter 枚举表

本文列出 fivsevn 内容 frontmatter 中建议统一管理的枚举值。

本文件只负责列出可选值及简短注释；字段意义与使用规则见 `content-frontmatter-001.md`。

---

## 目录

- [1. 使用原则](#1-使用原则)
- [2. `module`](#2-module)
- [3. `submodule`](#3-submodule)
- [4. `type`](#4-type)
- [5. `status`](#5-status)
- [6. `canonical`](#6-canonical)
- [7. `audience`](#7-audience)
- [8. `languages`](#8-languages)
- [9. `maturity`](#9-maturity)
- [10. `confidence`](#10-confidence)
- [11. `visibility`](#11-visibility)
- [12. `source_of_truth`](#12-source_of_truth)
- [13. 翻译扩展字段](#13-翻译扩展字段)
- [14. 非枚举字段](#14-非枚举字段)

---

## 1. 使用原则

- 本文件以 devlog 当前结构为主要依据。
- 枚举项采用竖排列，便于查阅和后续修改。
- `#` 后为简短注释，不属于字段值本身。
- 未列入本文件的自由值字段，不应强行枚举。
- 如需新增模块、子模块或内容类型，应同步更新本文件。

---

## 2. `module`

主模块枚举。

```yaml
module:
  - posts      # 个人笔记、文章、时间线内容
  - natsci     # 自然科学笔记
  - netcom     # 通讯技术、工程、数学与系统笔记
  - blogops    # 博客后台、结构调整、发布与维护日志
```

预留或跨仓库场景：

```yaml
module:
  - spec       # 规范仓库内容；主要用于 fivsevn-spec
  - system     # 系统说明、全局索引或跨模块结构
```

---

## 3. `submodule`

子模块枚举按 `module` 分组维护。

### 3.1 `posts`

```yaml
submodule:
  - index                  # posts 模块入口
  - drafts                 # posts 草稿区
  - 2025                   # 2025 年内容
  - 2026                   # 2026 年内容
  - ai-discourse-analysis  # AI 话语分析专题
```

### 3.2 `natsci`

```yaml
submodule:
  - index          # natsci 模块入口
  - drafts         # natsci 草稿区
  - ethnobiology   # 民族生物学、人与生物关系材料
  - paleontology   # 古生物学
  - reading        # 阅读材料、文献摘记、外部文章整理
  - taxonomy       # 分类学、物种分类、类群索引
```

### 3.3 `netcom`

```yaml
submodule:
  - index         # netcom 模块入口
  - drafts        # netcom 草稿区
  - ai            # AI、模型、评估与相关技术材料
  - architecture  # 系统架构、网络结构、分层模型
  - cs            # 计算机科学基础概念
  - digital       # 数字通信、数字电台等内容
  - lora          # LoRa、Meshtastic、Mesh 通信
  - math          # 数学基础、公式、模型与推导
  - mcu           # 微控制器、硬件平台
  - methods       # 方法论、学习路径、工程理解方式
  - protocol      # 协议、通信规则与结构
  - rf            # 射频、电磁波、天线与频谱
```

### 3.4 `blogops`

```yaml
submodule:
  - index    # blogops 模块入口
  - content  # 后台日志、说明、维护记录
  - docs     # 文档、说明材料、辅助资料
```

### 3.5 `spec`

```yaml
submodule:
  - content  # 内容规范
  - gov      # 治理规范、元信息规范
  - archive  # 归档规范
  - refs     # 引用规范
  - time     # 时间语义规范
```

---

## 4. `type`

内容类型枚举。

```yaml
type:
  - index        # 模块入口、目录页、索引页
  - note         # 普通笔记；当前默认内容类型
  - article      # 较完整的文章或长文
  - translation  # 翻译内容；需要添加翻译扩展字段
  - log          # 日志、变更记录、维护记录
  - spec         # 规范说明文件
  - release      # 版本发布说明或阶段性发布记录
```

历史兼容或错误拼写：

```yaml
type:
  - traslation   # translation 的历史误拼写；只作兼容，不建议新增使用
```

建议：

```yaml
type:
  - translation  # 新增翻译内容统一使用此值
```

---

## 5. `status`

内容展示与索引状态枚举。

```yaml
status:
  - hidden     # 不进入模块 index；草稿默认状态
  - private    # 不进入模块 index；私人或非公开内容
  - draft      # 进入模块 index，但显示为“更新中”，不生成正式链接
  - active     # 进入模块 index，并生成链接
  - publish    # 进入模块 index，并生成链接；兼容旧写法
  - published  # 进入模块 index，并生成链接；兼容旧写法
  - archive    # 不进入模块 index；归档内容
  - archived   # 不进入模块 index；归档内容
```

推荐新内容优先使用：

```yaml
status:
  - hidden
  - draft
  - active
  - archived
```

---

## 6. `canonical`

主版本标记。

```yaml
canonical:
  - true   # 当前文件是该内容单元的主版本
  - false  # 当前文件不是主版本
```

---

## 7. `audience`

预期读者范围枚举。

```yaml
audience:
  - self      # 主要供自己使用
  - public    # 面向公开读者
  - internal  # 内部使用或系统维护语境
```

写法要求：

```yaml
audience: [self]
audience: [public]
audience: [internal]
```

---

## 8. `languages`

内容语言枚举。

```yaml
languages:
  - zh  # 中文
  - en  # 英文
  - ja  # 日文
```

写法要求：

```yaml
languages: [zh]
languages: [en]
languages: [zh, en]
```

---

## 9. `maturity`

内容成熟度枚举。

```yaml
maturity:
  - draft       # 初稿、暂存、尚未充分整理
  - evolving    # 持续扩展或仍在调整
  - stable      # 基本稳定，可长期引用
  - deprecated  # 已过时，不建议继续作为当前版本使用
```

---

## 10. `confidence`

`confidence` 不使用离散枚举，采用数值范围。

```yaml
confidence:
  - 0.0  # 未确认、暂存、初步判断
  - 0.5  # 有一定依据，但仍需复核
  - 1.0  # 高度确认，已充分核对
```

规则：

```yaml
confidence: 0.0  # 最低值
confidence: 1.0  # 最高值
```

建议：

```yaml
confidence:
  - 0.0
  - 0.1
  - 0.2
  - 0.3
  - 0.4
  - 0.5
  - 0.6
  - 0.7
  - 0.8
  - 0.9
  - 1.0
```

---

## 11. `visibility`

预期可见范围枚举。

```yaml
visibility:
  - private   # 私人或非公开
  - public    # 公开展示
  - internal  # 内部、维护、系统语境
```

注意：

```yaml
visibility:
  - private  # 不等同于 status: hidden
```

`visibility` 表示预期可见范围；是否进入模块 index 主要由 `status` 控制。

---

## 12. `source_of_truth`

权威来源枚举。

```yaml
source_of_truth:
  - devlog       # 以 fivsevn-devlog 内容仓库为准
  - spec         # 以 fivsevn-spec 规范仓库为准
  - site         # 以站点展示版本为准
  - translation  # 以翻译关系及原文材料为依据
  - external     # 以外部来源为准；也可用于自己发布在 WordPress、个人博客等外部平台的原创内容
```

常用写法：

```yaml
source_of_truth: devlog       # 普通 devlog 内容
source_of_truth: translation  # 翻译内容
source_of_truth: spec         # 规范内容
```

---

## 13. 翻译扩展字段

以下字段主要在翻译内容中使用。

当使用：

```yaml
type: translation
```

时，应使用以下字段。对于外链原创内容，也可单独使用 `original_source` 与 `original_url` 记录外部原始发布位置。

```yaml
translation_fields:
  - original_title      # 原文标题
  - original_source     # 原文来源名称
  - original_publisher  # 原文发布方
  - original_url        # 原文 URL
  - translation_note    # 翻译说明
```

推荐组合：

```yaml
type: translation
source_of_truth: translation
```

外链原创内容推荐组合：

```yaml
type: article
source_of_truth: external
original_source: WordPress
original_url: https://fivsevn.home.blog/example-post/
```

---

## 14. 非枚举字段

以下字段不在本文件中枚举。

```yaml
non_enum_fields:
  - id                 # 全局唯一标识符
  - title              # 内容标题
  - topic              # 具体主题；自由值
  - summary            # 摘要
  - parents            # 上级内容 id 数组
  - related            # 相关内容 id 数组
  - tags               # 自由标签数组
  - original_title     # 原文标题
  - original_source    # 原文来源
  - original_publisher # 原文发布方
  - original_url       # 原文链接
  - translation_note   # 翻译说明
  - created            # 创建日期
  - updated            # 更新日期
```

---
