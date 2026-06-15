# Content Frontmatter 枚举速查

本文件按标准 frontmatter 的字段顺序排列。  
每个枚举字段直接列出可选值，方便查阅、复制和改写。

---

## 1. 普通内容速查模板

```yaml
---
id: module-submodule-topic-001
title: 标题

module:
  - posts      # 个人笔记、文章、时间线内容
  - natsci     # 自然科学笔记
  - netcom     # 通讯技术、工程、数学与系统笔记
  - blogops    # 博客后台、结构调整、发布与维护日志
  - spec       # 规范仓库内容；主要用于 fivsevn-spec
  - system     # 系统说明、全局索引或跨模块结构

submodule:
  posts:
    - index                  # posts 模块入口
    - drafts                 # posts 草稿区
    - 2025                   # 2025 年内容
    - 2026                   # 2026 年内容
    - ai-discourse-analysis  # AI 话语分析专题

  natsci:
    - index          # natsci 模块入口
    - drafts         # natsci 草稿区
    - ethnobiology   # 民族生物学、人与生物关系材料
    - paleontology   # 古生物学
    - reading        # 阅读材料、文献摘记、外部文章整理
    - taxonomy       # 分类学、物种分类、类群索引

  netcom:
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

  blogops:
    - index    # blogops 模块入口
    - content  # 后台日志、说明、维护记录
    - docs     # 文档、说明材料、辅助资料

  spec:
    - content  # 内容规范
    - gov      # 治理规范、元信息规范
    - archive  # 归档规范
    - refs     # 引用规范
    - time     # 时间语义规范

topic: specific-topic

type:
  - index        # 模块入口、目录页、索引页
  - note         # 普通笔记；当前默认内容类型
  - article      # 较完整的文章或长文
  - translation  # 翻译内容；需要添加翻译扩展字段
  - log          # 日志、变更记录、维护记录
  - spec         # 规范说明文件
  - release      # 版本发布说明或阶段性发布记录
  - traslation   # translation 的历史误拼写；只作兼容，不建议新增使用

status:
  - hidden     # 不进入模块 index；草稿默认状态
  - private    # 不进入模块 index；私人或非公开内容
  - draft      # 进入模块 index，但显示为“更新中”，不生成正式链接
  - active     # 进入模块 index，并生成链接
  - publish    # 进入模块 index，并生成链接；兼容旧写法
  - published  # 进入模块 index，并生成链接；兼容旧写法
  - archive    # 不进入模块 index；归档内容
  - archived   # 不进入模块 index；归档内容

canonical:
  - true   # 当前文件是该内容单元的主版本
  - false  # 当前文件不是主版本

summary: >
  摘要

parents: []
related: []

tags: []

audience:
  - self      # 主要供自己使用
  - public    # 面向公开读者
  - internal  # 内部使用或系统维护语境

languages:
  - zh  # 中文
  - en  # 英文
  - ja  # 日文

maturity:
  - draft       # 初稿、暂存、尚未充分整理
  - evolving    # 持续扩展或仍在调整
  - stable      # 基本稳定，可长期引用
  - deprecated  # 已过时，不建议继续作为当前版本使用

confidence:
  - 0.0  # 未确认、暂存、初步判断
  - 0.1
  - 0.2
  - 0.3
  - 0.4
  - 0.5  # 有一定依据，但仍需复核
  - 0.6
  - 0.7
  - 0.8
  - 0.9
  - 1.0  # 高度确认，已充分核对

visibility:
  - private   # 私人或非公开
  - public    # 公开展示
  - internal  # 内部、维护、系统语境

source_of_truth:
  - devlog       # 以 fivsevn-devlog 内容仓库为准
  - spec         # 以 fivsevn-spec 规范仓库为准
  - site         # 以站点展示版本为准
  - translation  # 以翻译关系及原文材料为依据
  - external     # 以外部来源为准

created: YYYY-MM-DD
updated: YYYY-MM-DD
---
```

---

## 2. 翻译内容速查模板

```yaml
---
id: module-submodule-topic-001
title: 标题

module:
  - posts      # 个人笔记、文章、时间线内容
  - natsci     # 自然科学笔记
  - netcom     # 通讯技术、工程、数学与系统笔记
  - blogops    # 博客后台、结构调整、发布与维护日志
  - spec       # 规范仓库内容；主要用于 fivsevn-spec
  - system     # 系统说明、全局索引或跨模块结构

submodule:
  posts:
    - index                  # posts 模块入口
    - drafts                 # posts 草稿区
    - 2025                   # 2025 年内容
    - 2026                   # 2026 年内容
    - ai-discourse-analysis  # AI 话语分析专题

  natsci:
    - index          # natsci 模块入口
    - drafts         # natsci 草稿区
    - ethnobiology   # 民族生物学、人与生物关系材料
    - paleontology   # 古生物学
    - reading        # 阅读材料、文献摘记、外部文章整理
    - taxonomy       # 分类学、物种分类、类群索引

  netcom:
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

  blogops:
    - index    # blogops 模块入口
    - content  # 后台日志、说明、维护记录
    - docs     # 文档、说明材料、辅助资料

  spec:
    - content  # 内容规范
    - gov      # 治理规范、元信息规范
    - archive  # 归档规范
    - refs     # 引用规范
    - time     # 时间语义规范

topic: specific-topic

type:
  - translation  # 翻译内容；需要添加翻译扩展字段

status:
  - hidden     # 不进入模块 index；草稿默认状态
  - private    # 不进入模块 index；私人或非公开内容
  - draft      # 进入模块 index，但显示为“更新中”，不生成正式链接
  - active     # 进入模块 index，并生成链接
  - publish    # 进入模块 index，并生成链接；兼容旧写法
  - published  # 进入模块 index，并生成链接；兼容旧写法
  - archive    # 不进入模块 index；归档内容
  - archived   # 不进入模块 index；归档内容

canonical:
  - true   # 当前文件是该内容单元的主版本
  - false  # 当前文件不是主版本

summary: >
  摘要

parents: []
related: []

tags: []

audience:
  - self      # 主要供自己使用
  - public    # 面向公开读者
  - internal  # 内部使用或系统维护语境

languages:
  - zh  # 中文
  - en  # 英文
  - ja  # 日文

maturity:
  - draft       # 初稿、暂存、尚未充分整理
  - evolving    # 持续扩展或仍在调整
  - stable      # 基本稳定，可长期引用
  - deprecated  # 已过时，不建议继续作为当前版本使用

confidence:
  - 0.0  # 未确认、暂存、初步判断
  - 0.1
  - 0.2
  - 0.3
  - 0.4
  - 0.5  # 有一定依据，但仍需复核
  - 0.6
  - 0.7
  - 0.8
  - 0.9
  - 1.0  # 高度确认，已充分核对

visibility:
  - private   # 私人或非公开
  - public    # 公开展示
  - internal  # 内部、维护、系统语境

source_of_truth:
  - translation  # 翻译内容推荐值
  - devlog       # 以 fivsevn-devlog 内容仓库为准
  - spec         # 以 fivsevn-spec 规范仓库为准
  - site         # 以站点展示版本为准
  - external     # 以外部来源为准

original_title:      # 原文标题
original_source:     # 原文来源名称
original_publisher:  # 原文发布方
original_url:        # 原文 URL
translation_note:    # 翻译说明

created: YYYY-MM-DD
updated: YYYY-MM-DD
---
```

---

## 3. 最常用默认值

```yaml
---
id: module-submodule-topic-001
title: 标题

module: module-name
submodule: submodule-name
topic: specific-topic

type: note
status: hidden
canonical: true

summary: >
  摘要

parents: []
related: []

tags: []

audience: [self]
languages: [zh]

maturity: draft
confidence: 0.0

visibility: private
source_of_truth: devlog

created: YYYY-MM-DD
updated: YYYY-MM-DD
---
```

---

## 4. 翻译内容常用默认值

```yaml
---
id: module-submodule-topic-001
title: 标题

module: module-name
submodule: submodule-name
topic: specific-topic

type: translation
status: hidden
canonical: true

summary: >
  摘要

parents: []
related: []

tags: []

audience: [self]
languages: [zh]

maturity: draft
confidence: 0.0

visibility: private
source_of_truth: translation

original_title:
original_source:
original_publisher:
original_url:
translation_note:

created: YYYY-MM-DD
updated: YYYY-MM-DD
---
```
