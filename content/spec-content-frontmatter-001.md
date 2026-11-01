---
id: "spec-content-frontmatter-001"
title: "Content Frontmatter 说明"

module: "spec"
submodule: "content"
topic: "spec-content-frontmatter-001"

type: "spec"
status: "active"
canonical: true

summary: "说明Content Frontmatter 说明。"

parents: []
related: []

tags: []

audience: ["self", "internal"]
languages: ["zh"]

maturity: "evolving"
confidence: null

visibility: "public"
source_of_truth: "spec"

note: "未记录原始写作日期；created 为本路径首次 Git 记录日期，无法合理确定时留空。"

created: "2026-06-16"
updated: '2026-11-01'
metadata_updated: '2026-11-01'
---

# Frontmatter

Markdown 文件以 YAML 配置区开头。字段类型和合法取值以 [schema](content-metadata.schema.json) 为准；[字段取值表](../appendix/spec-content-frontmatter-enums-001.md) 提供速查。

```yaml
---
id: posts-example-001
title: 示例
module: posts
submodule: "2026"
topic: null
type: note
status: draft
canonical: true
summary: null
parents: []
related: []
tags: []
audience: [self]
languages: [zh]
maturity: evolving
confidence: null
visibility: private
source_of_truth: devlog
created: null
updated: null
---
```

## 核心字段

| 字段 | 用途 |
|---|---|
| `id` | 稳定身份；小写字母、数字及连字符；不随标题改变 |
| `title` | 非空标题 |
| `module`、`submodule` | 所属板块和一级目录；年份写成字符串 |
| `topic`、`tags` | 主题及检索标签 |
| `type` | 内容类型 |
| `status` | 写作或发布状态 |
| `canonical` | 是否为当前主版本；不控制是否公开 |
| `summary` | 简短摘要，未知时为 `null` |
| `parents`、`related` | 其他内容的 ID 数组；关系不确定时留空 |
| `audience`、`languages` | 预期读者及语言数组 |
| `maturity`、`confidence` | 完成程度及 0–1 的可靠度；不明时不补造高分 |
| `visibility` | `public`、`private` 或 `internal` |
| `source_of_truth` | 权威版本所在位置；不等同于原始材料来源 |
| `created`、`updated` | 内容日期，`YYYY-MM-DD` 或 `null` |

数组字段使用 `[]`，不以空字符串代替；布尔值使用 `true` / `false`。不新增 schema 之外的顶层字段。公开仓库中的源文件仍可被读取，`status` 和 `visibility` 只控制站点发布。

## 可选字段

| 字段 | 用途 |
|---|---|
| `original_title`、`original_source`、`original_publisher`、`original_url` | 原作或外部出处；译文按[翻译规则](spec-content-translation-001.md)填写 |
| `translation_note`、`rights` | 翻译说明、许可范围和核对记录；用途声明不等于授权 |
| `note`、`subtitle` | 编辑说明、副标题 |
| `references` | 引文对象数组；每项有 `text`，可有 `section` |
| `aliases` | 历史 ID 数组 |
| `legacy` | 旧字段、旧路径和无法确认的关系；只作追溯 |
| `extra` | 有明确用途的板块扩展数据 |
| `archive_url` | 曾在本站发布的位置；区别于原作的 `original_url` |
| `filename_policy` | `entrypoint` 或 `stable-link` |
| `metadata_updated` | 仅整理配置时记录的日期 |

`layout`、`lang`、`description`、`canonical_url` 和 `permalink` 按页面构建需要保留。`permalink` 可固定文章公开网址；`aliases` 和 `legacy.path` 不创建网页跳转。

普通文档用 `id.md`。README、目录及文章包的 `index.md` 保留入口名称，并使用 `filename_policy: entrypoint`。Posts 文章按 `posts/YYYY/MM/<文章编号>/index.md` 保存，AI 分析在其分区下使用相同年月结构；正文及素材属于同一个发布包。

Flux、Savour、Fieldlog、Stills、Motion、SYS、CCTV 的正式包另按 [site-post-v1](spec-content-site-post-001.md) 校验。trigger、生成文件和特别设计的叙事页面不强行套文章模板。

内容日期不因整理配置而重写。可靠日期缺失时写 `null`；从 Git 补录的日期应在 `note` 说明其依据。更改旧字段时保存在 `legacy.metadata`，不借整理工作改写正文事实或重新公开隐藏内容。
