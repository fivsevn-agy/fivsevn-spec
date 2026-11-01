---
id: "spec-content-frontmatter-enums-quickref-001"
title: "Content Frontmatter 枚举速查"

module: "spec"
submodule: "appendix"
topic: "spec-content-frontmatter-enums-quickref-001"

type: "spec"
status: "active"
canonical: true

summary: "说明Content Frontmatter 枚举速查。"

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

# Frontmatter 速查

| 情形 | 配置 |
|---|---|
| 未完成笔记 | `type: note`、`status: draft`、`visibility: private` |
| 公开文章 | `status: active`、`visibility: public`、`canonical: true` |
| 中文译文 | `type: translation`、`languages: [zh]`，填写原作出处和翻译说明 |
| 固定目录或发布包入口 | `filename_policy: entrypoint` |
| 可靠度或日期不明 | `confidence: null`、日期字段 `null` |
| 暂无标签或关系 | `tags: []`、`parents: []`、`related: []` |
| 仅整理配置 | 保留内容日期，更新 `metadata_updated` |

完整取值见[枚举表](spec-content-frontmatter-enums-001.md)，字段及完整样本见 [Frontmatter](../content/spec-content-frontmatter-001.md)。此表用于查值，不省略完整文件的核心字段。
