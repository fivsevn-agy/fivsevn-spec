---
id: "spec-content-frontmatter-enums-001"
title: "Content Frontmatter 枚举表"

module: "spec"
submodule: "appendix"
topic: "spec-content-frontmatter-enums-001"

type: "spec"
status: "active"
canonical: true

summary: "说明Content Frontmatter 枚举表。"

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

# Frontmatter 取值

合法取值以 [schema](../content/content-metadata.schema.json) 为准；字段含义见 [Frontmatter](../content/spec-content-frontmatter-001.md)。

| 字段 | 取值 |
|---|---|
| `module` | `posts`、`natsci`、`netcom`、`blogops`、`savour`、`stills`、`motion`、`57store`、`now`、`intake`、`system`、`spec`、`assets` |
| `type` | `note`、`article`、`translation`、`index`、`log`、`spec`、`release` |
| `status` | `hidden`、`private`、`draft`、`active`、`publish`、`published`、`archive`、`archived` |
| `maturity` | `draft`、`evolving`、`stable`、`deprecated` |
| `visibility` | `public`、`private`、`internal` |
| `source_of_truth` | `devlog`、`spec`、`assets`、`site`、`translation`、`external` |
| `filename_policy` | `entrypoint`、`stable-link` |

`submodule` 使用实际一级目录。Posts 按年份或 `ai-discourse-analysis`，Flux 用 `flux`；Fieldlog 用 `fieldlog`；Savour 按年份；Stills/Motion 用 `roll`；SYS/CCTV 分别用 `sys`、`cctv`。Spec 当前目录见[目录表](../system/spec-system-map-001.md)。新目录不沿用已废弃的 `refs`、`time` 等旧分类。

| 字段 | 规则 |
|---|---|
| `canonical` | `true` / `false` |
| `audience` | 字符串数组，如 `[self]`、`[public]`、`[self, internal]` |
| `languages` | 字符串数组，如 `[zh]`、`[en]`、`[zh, en]` |
| `confidence` | 0–1 的数字或 `null` |
| `parents`、`related` | 内容 ID 数组 |
| `tags`、`aliases` | 字符串数组 |
| `created`、`updated`、`metadata_updated` | `YYYY-MM-DD` 或 `null` |

`topic`、摘要、出处和编辑说明是自由文本。不要把示例标签或语言当成封闭枚举。发布包的板块映射、日期和公开条件见 [site-post-v1](../content/spec-content-site-post-001.md)。
