# Content Frontmatter 说明

本文定义 fivsevn 内容文件所使用的 YAML frontmatter 结构。frontmatter 用于描述一篇内容的基本身份、所属位置、展示状态、内容关系、语言属性、成熟程度、来源信息与更新时间。

本文侧重说明每个字段的意义与使用方式。各字段可填写的具体取值，另见 `content-frontmatter-enums.md`。

## 目录

- [1. 基本原则](#1-基本原则)
- [2. 标准样本](#2-标准样本)
- [3. 翻译内容样本](#3-翻译内容样本)
- [4. 字段分组说明](#4-字段分组说明)
- [5. 内容身份字段](#5-内容身份字段)
  - [`id`](#id)
  - [`title`](#title)
- [6. 内容位置字段](#6-内容位置字段)
  - [`module`](#module)
  - [`submodule`](#submodule)
  - [`topic`](#topic)
- [7. 内容类型与展示状态字段](#7-内容类型与展示状态字段)
  - [`type`](#type)
  - [`status`](#status)
  - [`canonical`](#canonical)
- [8. 内容摘要字段](#8-内容摘要字段)
  - [`summary`](#summary)
- [9. 内容关系字段](#9-内容关系字段)
  - [`parents`](#parents)
  - [`related`](#related)
- [10. 标签、受众与语言字段](#10-标签受众与语言字段)
  - [`tags`](#tags)
  - [`audience`](#audience)
  - [`languages`](#languages)
- [11. 内容质量字段](#11-内容质量字段)
  - [`maturity`](#maturity)
  - [`confidence`](#confidence)
- [12. 可见性与来源字段](#12-可见性与来源字段)
  - [`visibility`](#visibility)
  - [`source_of_truth`](#source_of_truth)
- [13. 翻译扩展字段](#13-翻译扩展字段)
  - [`original_title`](#original_title)
  - [`original_source`](#original_source)
  - [`original_publisher`](#original_publisher)
  - [`original_url`](#original_url)
  - [`translation_note`](#translation_note)
- [14. 时间字段](#14-时间字段)
  - [`created`](#created)
  - [`updated`](#updated)
- [15. 字段使用规则](#15-字段使用规则)
  - [15.1 核心字段应保持完整](#151-核心字段应保持完整)
  - [15.2 字段组之间保留空行](#152-字段组之间保留空行)
  - [15.3 数组字段统一使用数组写法](#153-数组字段统一使用数组写法)
  - [15.4 空数组与空字段的区别](#154-空数组与空字段的区别)
  - [15.5 `status` 与 `visibility` 不应混淆](#155-status-与-visibility-不应混淆)
  - [15.6 `type: translation` 的额外要求](#156-type-translation-的额外要求)
  - [15.7 日期字段只使用 `created` 和 `updated`](#157-日期字段只使用-created-和-updated)
- [16. 与枚举文件的关系](#16-与枚举文件的关系)
- [17. 推荐维护方式](#17-推荐维护方式)

---

## 1. 基本原则

每一篇内容文件应在正文之前放置一段 YAML frontmatter，并使用三条短横线包围：

```yaml
---
id: module-submodule-topic-001
title: 标题
---
```

frontmatter 的作用不是替代正文，而是为内容提供稳定的结构信息。它应保持清晰、克制、可维护，不应堆放正文中已经能够自然表达的信息。

frontmatter 应满足以下原则：

1. **稳定性**  
   字段名称应保持稳定，不因单篇内容的特殊情况随意增删核心字段。

2. **可读性**  
   字段值应便于人工阅读和判断，不应使用过度缩写或含义不明的代号。

3. **可索引性**  
   字段应能支持内容目录、模块索引、归档、检索和后续迁移。

4. **职责分明**  
   本文件说明字段意义；字段可选值由 `content-frontmatter-enums.md` 统一列出。

5. **分组清楚**  
   frontmatter 应按字段含义分组书写，并在不同字段组之间保留空行，方便人工阅读和维护。

---

## 2. 标准样本

以下为普通内容文件的标准 frontmatter 样本。

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

该样本使用的是假设值。实际填写时，应根据内容所属模块、具体主题、展示状态和来源情况替换为真实值。

---

## 3. 翻译内容样本

当内容类型为翻译时，应使用 `type: translation`，并增加原文信息字段。

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

翻译扩展字段只在 `type: translation` 时使用。普通原创内容、笔记、索引页或说明页不应添加这些字段。

---

## 4. 字段分组说明

frontmatter 字段按功能可分为以下几组：

| 分组 | 字段 |
|---|---|
| 内容身份 | `id`, `title` |
| 内容位置 | `module`, `submodule`, `topic` |
| 内容类型与展示状态 | `type`, `status`, `canonical` |
| 内容摘要 | `summary` |
| 内容关系 | `parents`, `related` |
| 标签与语言 | `tags`, `audience`, `languages` |
| 内容质量 | `maturity`, `confidence` |
| 可见性与来源 | `visibility`, `source_of_truth` |
| 翻译扩展 | `original_title`, `original_source`, `original_publisher`, `original_url`, `translation_note` |
| 时间信息 | `created`, `updated` |

---

## 5. 内容身份字段

### `id`

`id` 是内容的稳定标识符。

```yaml
id: module-submodule-topic-001
```

`id` 应当全局唯一。它用于内容引用、索引生成、关系标注和长期归档。

建议格式为：

```text
module-submodule-topic-001
```

其中：

- `module` 表示所属主模块；
- `submodule` 表示所属子模块；
- `topic` 表示具体主题；
- `001` 表示同一主题下的编号。

`id` 推荐与文件名保持一致，但二者不是同一个概念。文件名可以改变；`id` 一旦确定，应尽量保持稳定。

填写要求：

- 使用小写英文字母、数字和连字符；
- 不使用空格；
- 不使用中文标点；
- 不使用容易变动的日期作为唯一识别依据；
- 同一内容迁移位置时，原则上不更改 `id`。

---

### `title`

`title` 是内容标题。

```yaml
title: 标题
```

`title` 应为人类可读的自然语言标题，用于索引、目录、页面标题和内容识别。

填写要求：

- 应简明、准确；
- 不宜过长；
- 不应包含路径信息；
- 不应为了排序而添加编号前缀；
- 如为翻译内容，应填写中文标题或当前内容标题，原文标题填写在 `original_title` 中。

---

## 6. 内容位置字段

### `module`

`module` 表示内容所属的主模块。

```yaml
module: natsci
```

它用于确定内容的大类归属，也是生成模块索引和组织内容结构的重要依据。

示例：

```yaml
module: natsci
```

可用取值见 `content-frontmatter-enums.md`。

---

### `submodule`

`submodule` 表示内容所属的子模块。

```yaml
submodule: paleontology
```

它用于在主模块之下进一步划分内容位置。

示例：

```yaml
submodule: paleontology
```

当某篇内容是模块首页、总索引或暂不归入具体子模块时，可使用约定的子模块名称，例如 `index`。具体可用取值见 `content-frontmatter-enums.md`。

---

### `topic`

`topic` 表示内容所讨论的具体主题。

```yaml
topic: whale-evolution
```

它比 `module` 和 `submodule` 更细，用于标识单篇内容的主题焦点。

对于索引页、模块说明页或无法明确归入单一主题的内容，`topic` 可以留空，但建议保留字段：

```yaml
topic:
```

填写要求：

- 使用小写英文、数字和连字符；
- 应体现主题，而不是标题的机械缩写；
- 不应包含过长说明；
- 不应与 `tags` 混用。

---

## 7. 内容类型与展示状态字段

### `type`

`type` 表示内容类型。

```yaml
type: note
```

它用于区分笔记、文章、索引页、翻译、日志等不同内容形态。

常见类型包括：

```yaml
type: note
type: article
type: index
type: translation
```

具体可用取值见 `content-frontmatter-enums.md`。

当 `type: translation` 时，必须使用翻译扩展字段：

```yaml
original_title:
original_source:
original_publisher:
original_url:
translation_note:
```

---

### `status`

`status` 表示内容在当前系统中的展示与索引状态。

```yaml
status: hidden
```

在 fivsevn-devlog 的自动化流程中，`status` 会影响模块 index 的生成方式。它不仅是一般意义上的“写作状态”，也是内容是否进入索引、以何种形式进入索引的控制字段。

当前规则如下：

| `status` | 索引行为 |
|---|---|
| `hidden` / `private` | 不进入模块 index |
| `draft` | 进入模块 index，但显示为“更新中”，不生成正式链接 |
| `active` / `publish` / `published` | 进入模块 index，并生成链接 |
| `archive` / `archived` | 不进入模块 index，表示已归档或不再展示 |

因此，`status: hidden` 与 `visibility: private` 并不重复。前者主要影响自动化索引行为，后者表示内容预期可见范围。

填写建议：

- 尚不希望出现在 index 中的草稿，使用 `status: hidden`；
- 希望在 index 中显示为“更新中”的内容，使用 `status: draft`；
- 已准备公开展示并进入索引的内容，使用 `status: active`；
- 不再展示或已归档的内容，使用 `status: archived`。

具体可用取值见 `content-frontmatter-enums.md`。

---

### `canonical`

`canonical` 表示该文件是否为当前内容单元的主版本。

```yaml
canonical: true
```

推荐使用布尔值：

```yaml
canonical: true
canonical: false
```

一般情况下，原创内容、正式内容和主要维护版本应设为：

```yaml
canonical: true
```

当某个文件只是副本、迁移页、临时页或非主版本时，可设为：

```yaml
canonical: false
```

`canonical` 不直接表示是否公开，也不直接控制 index 是否展示。展示行为主要由 `status` 决定。

---

## 8. 内容摘要字段

### `summary`

`summary` 是内容摘要。

```yaml
summary: >
  摘要
```

摘要用于帮助读者和系统快速理解内容主题。它可以出现在索引、列表、搜索结果或内容概览中。

推荐使用 YAML 折叠文本写法：

```yaml
summary: >
  这是一段简短摘要，用于说明本文讨论的主要内容。
```

填写要求：

- 应为一段自然语言说明；
- 不写 Markdown 标题；
- 不放列表；
- 不写过多背景材料；
- 不应完全重复标题；
- 长度宜适中，以说明内容核心为准。

---

## 9. 内容关系字段

### `parents`

`parents` 表示当前内容的上级内容节点。

```yaml
parents: []
```

它用于建立纵向关系，例如某篇内容属于某个模块索引、专题入口或上级说明页。

示例：

```yaml
parents: [natsci-paleontology-index-001]
```

填写要求：

- 使用数组；
- 数组元素应填写其他内容的 `id`；
- 不填写标题；
- 不填写文件路径；
- 不填写外部 URL。

当没有明确上级内容时，使用空数组：

```yaml
parents: []
```

---

### `related`

`related` 表示横向相关内容。

```yaml
related: []
```

它用于标记与当前内容相关、但不构成上下级关系的其他内容。

示例：

```yaml
related: [natsci-evolution-whale-001]
```

填写要求：

- 使用数组；
- 数组元素应填写其他内容的 `id`；
- 不填写标题；
- 不填写文件路径；
- 不填写外部 URL；
- 不宜堆放过多弱相关内容。

当没有明确相关内容时，使用空数组：

```yaml
related: []
```

---

## 10. 标签、受众与语言字段

### `tags`

`tags` 是自由标签。

```yaml
tags: []
```

它用于补充描述内容主题、材料类型、知识领域或组织线索。

示例：

```yaml
tags: [natsci, paleontology, whale-evolution]
```

填写要求：

- 使用数组；
- 标签使用小写英文、数字和连字符；
- 不使用空格；
- 不使用过长词组；
- 不应与 `module`、`submodule`、`topic` 机械重复，但可以在必要时保留关键分类词；
- `tags` 原则上不作为固定枚举字段管理。

---

### `audience`

`audience` 表示内容的预期读者范围。

```yaml
audience: [self]
```

它说明这篇内容主要面向谁，而不直接等同于可见性控制。

示例：

```yaml
audience: [self]
audience: [public]
audience: [internal]
```

填写要求：

- 必须使用数组；
- 即使只有一个值，也应写作 `[self]`，而不是 `self`；
- 具体可用取值见 `content-frontmatter-enums.md`。

---

### `languages`

`languages` 表示内容所使用的语言。

```yaml
languages: [zh]
```

它用于说明当前文件正文的语言，而不是原始材料的语言。

示例：

```yaml
languages: [zh]
languages: [en]
languages: [zh, en]
```

填写要求：

- 必须使用数组；
- 即使只有一种语言，也应写作 `[zh]`；
- 使用短语言代码；
- 具体可用取值见 `content-frontmatter-enums.md`。

对于翻译内容，`languages` 表示译文使用的语言；原文语言如有必要，可在正文或 `translation_note` 中说明。

---

## 11. 内容质量字段

### `maturity`

`maturity` 表示内容成熟度。

```yaml
maturity: draft
```

它描述内容本身的完成程度和稳定程度，不直接控制内容是否进入索引。

常见含义包括：

- 初稿；
- 持续扩展中；
- 已基本稳定；
- 已过时或不再维护。

具体可用取值见 `content-frontmatter-enums.md`。

注意：`maturity` 与 `status` 不同。

```yaml
status: hidden
maturity: draft
```

表示该内容尚不进入 index，且内容本身仍处于草稿阶段。

```yaml
status: active
maturity: draft
```

表示该内容已经可以进入 index，但内容本身仍可能继续修订。

---

### `confidence`

`confidence` 表示内容可靠度或确认程度。

```yaml
confidence: 0.0
```

推荐使用 `0.0` 到 `1.0` 之间的数值。

示例：

```yaml
confidence: 0.0
confidence: 0.5
confidence: 1.0
```

建议含义：

| 数值 | 含义 |
|---|---|
| `0.0` | 尚未确认，可能只是暂存、摘录或初步判断 |
| `0.5` | 有一定依据，但仍需复核 |
| `1.0` | 高度确认，内容已充分核对 |

填写要求：

- 使用数字；
- 范围为 `0.0` 至 `1.0`；
- 建议保留一位小数；
- 不应用作情绪化评价；
- 不替代正文中的来源说明。

---

## 12. 可见性与来源字段

### `visibility`

`visibility` 表示内容预期可见范围。

```yaml
visibility: private
```

它说明内容面向公开、私人、内部或其他范围。

示例：

```yaml
visibility: private
visibility: public
```

需要注意的是，在当前 devlog 自动化中，模块 index 的生成主要由 `status` 控制，而不是由 `visibility` 控制。

因此：

```yaml
status: hidden
visibility: private
```

表示内容不进入 index，且预期为私人内容。

而：

```yaml
status: draft
visibility: private
```

则可能表示内容会进入 index 并显示为“更新中”，但其预期可见范围仍是私人或非公开。

具体可用取值见 `content-frontmatter-enums.md`。

---

### `source_of_truth`

`source_of_truth` 表示当前内容的权威来源。

```yaml
source_of_truth: devlog
```

它用于说明当多个仓库、页面或版本之间出现差异时，应以哪一处为准。

示例：

```yaml
source_of_truth: devlog
source_of_truth: spec
source_of_truth: site
source_of_truth: translation
```

对于普通 devlog 内容，一般使用：

```yaml
source_of_truth: devlog
```

对于翻译内容，建议使用：

```yaml
source_of_truth: translation
```

这里的 `translation` 表示该内容的权威依据来自翻译关系及其原文材料，而不是表示当前文件本身比原文更权威。

具体可用取值见 `content-frontmatter-enums.md`。

---

## 13. 翻译扩展字段

以下字段只在 `type: translation` 时使用。

普通内容不应添加这些字段。

---

### `original_title`

`original_title` 表示原文标题。

```yaml
original_title: 原文标题
```

填写要求：

- 应尽量保留原文正式标题；
- 不应填写译文标题；
- 如原文没有明确标题，可留空，或在 `translation_note` 中说明。

---

### `original_source`

`original_source` 表示原文来源名称。

```yaml
original_source: 来源名称
```

它可以是原文所在栏目、机构、项目、数据库、发布平台或来源页面名称。

示例：

```yaml
original_source: Example Journal
```

---

### `original_publisher`

`original_publisher` 表示原文发布方。

```yaml
original_publisher: 发布方名称
```

它通常是机构、媒体、出版社、研究组织、网站或作者所属发布主体。

当 `original_source` 与 `original_publisher` 相同或难以区分时，可以二者填写相同值，也可以保留其中一项为空，并在 `translation_note` 中说明。

---

### `original_url`

`original_url` 表示原文链接。

```yaml
original_url: https://example.com/original-page
```

它用于记录原始材料位置。在部分自动索引场景中，如果内容进入正式链接状态，`original_url` 可能被用作 index 中的链接目标。

填写要求：

- 使用完整 URL；
- 不使用短链接；
- 优先填写原始发布页面，而不是转载页面；
- 如果原文无稳定 URL，可留空，并在 `translation_note` 中说明。

---

### `translation_note`

`translation_note` 表示翻译说明。

```yaml
translation_note: 译文说明
```

它用于记录翻译范围、删改情况、术语处理、原文状态或其他需要说明的信息。

示例：

```yaml
translation_note: 本文为节选翻译，保留原文主要结构，个别术语按本站习惯译法处理。
```

填写要求：

- 简明说明翻译情况；
- 不写成长篇译者序；
- 不替代正文中的详细说明；
- 如无特别说明，可留空。

---

## 14. 时间字段

### `created`

`created` 表示内容首次创建日期。

```yaml
created: YYYY-MM-DD
```

它记录当前内容单元首次形成的日期，而不是某次小修订的日期。

填写要求：

- 使用 `YYYY-MM-DD` 格式；
- 不使用中文日期；
- 不使用斜线格式；
- 不附加具体时间。

示例：

```yaml
created: 2026-06-15
```

---

### `updated`

`updated` 表示内容最近一次实质更新日期。

```yaml
updated: YYYY-MM-DD
```

实质更新包括内容结构调整、观点修订、重要补充、来源更新或状态改变。单纯修正错别字、格式空格或无关紧要的标点，不一定需要更新该字段。

填写要求：

- 使用 `YYYY-MM-DD` 格式；
- 不使用中文日期；
- 不使用斜线格式；
- 不附加具体时间；
- 不应早于 `created`。

示例：

```yaml
updated: 2026-06-15
```

---

## 15. 字段使用规则

### 15.1 核心字段应保持完整

普通内容建议保留以下字段：

```yaml
id:
title:

module:
submodule:
topic:

type:
status:
canonical:

summary:

parents:
related:

tags:

audience:
languages:

maturity:
confidence:

visibility:
source_of_truth:

created:
updated:
```

即使某些字段暂时没有内容，也建议保留字段并使用空值或空数组，而不是删除字段。

---

### 15.2 字段组之间保留空行

frontmatter 在书写时，应按字段含义分组，并在字段组之间保留一个空行。

推荐分组如下：

```yaml
id:
title:

module:
submodule:
topic:

type:
status:
canonical:

summary:

parents:
related:

tags:

audience:
languages:

maturity:
confidence:

visibility:
source_of_truth:

created:
updated:
```

翻译内容在 `source_of_truth` 之后、时间字段之前增加翻译扩展字段：

```yaml
visibility:
source_of_truth:

original_title:
original_source:
original_publisher:
original_url:
translation_note:

created:
updated:
```

保留空行的目的，是让 frontmatter 在人工编辑时更容易辨认。  
这些空行不改变 YAML 含义，但属于本规范推荐的书写格式。

---

### 15.3 数组字段统一使用数组写法

以下字段应统一使用数组：

```yaml
parents: []
related: []
tags: []
audience: [self]
languages: [zh]
```

即使只有一个值，也应使用数组写法。

推荐：

```yaml
audience: [self]
languages: [zh]
```

不推荐：

```yaml
audience: self
languages: zh
```

统一数组写法可以减少后续解析、检查和迁移时的歧义。

---

### 15.4 空数组与空字段的区别

空数组表示“当前没有此类项目”：

```yaml
parents: []
related: []
tags: []
```

空字段表示“该字段保留，但暂时没有具体值”：

```yaml
topic:
original_url:
```

对于关系类和列表类字段，优先使用空数组。  
对于单值字段，在确实没有值时可以留空。

---

### 15.5 `status` 与 `visibility` 不应混淆

`status` 主要影响自动化索引行为。  
`visibility` 表示内容预期可见范围。

示例：

```yaml
status: hidden
visibility: private
```

表示内容不进入模块 index，且预期为私人内容。

```yaml
status: active
visibility: public
```

表示内容进入模块 index，并可公开展示。

```yaml
status: draft
visibility: private
```

表示内容可能进入模块 index 并显示为“更新中”，但预期可见范围仍为私人或非公开。

---

### 15.6 `type: translation` 的额外要求

当使用：

```yaml
type: translation
```

时，必须添加：

```yaml
original_title:
original_source:
original_publisher:
original_url:
translation_note:
```

并建议使用：

```yaml
source_of_truth: translation
```

翻译字段只描述原文和翻译关系，不应承担正文摘要、标签分类或内容评价的功能。

---

### 15.7 日期字段只使用 `created` 和 `updated`

新版 frontmatter 使用：

```yaml
created:
updated:
```

不再使用旧式字段：

```yaml
date:
```

如旧内容中仍存在 `date`，后续迁移时应改为 `created` 或根据实际情况拆分为 `created` 与 `updated`。

---

## 16. 与枚举文件的关系

本文只说明字段意义与使用方式。字段可填写的具体取值应以：

```text
content-frontmatter-enums.md
```

为准。

两份文件的职责如下：

| 文件 | 职责 |
|---|---|
| `spec-content-frontmatter-001.md` | 说明 frontmatter 的结构、字段意义和使用规则 |
| `spec-content-frontmatter-enums-001.md` | 列出枚举字段的合法取值 |

当本文中的示例值与枚举文件不一致时，应优先检查并更新两者，使说明与枚举保持一致。

---

## 17. 推荐维护方式

维护 frontmatter 时，建议遵循以下顺序：

1. 先确认内容属于哪个 `module` 与 `submodule`；
2. 再确认内容的 `type`；
3. 根据是否希望进入 index，设置 `status`；
4. 根据预期读者和公开范围，设置 `audience` 与 `visibility`；
5. 根据内容完成程度，设置 `maturity` 与 `confidence`；
6. 如为翻译内容，补充原文信息字段；
7. 最后检查 `created` 与 `updated`。

frontmatter 应服务于内容组织，而不是制造额外负担。若某个字段一时无法准确填写，应优先使用保守值，并在后续修订中更新。

---
