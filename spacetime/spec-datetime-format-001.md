---
id: "spec-datetime-format-001"
title: "日期与时间书写规范"

module: "spec"
submodule: "spacetime"
topic: "spec-datetime-format-001"

type: "spec"
status: "active"
canonical: true

summary: "说明日期与时间书写规范。"

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

created: "2025-12-16"
updated: '2026-11-01'
metadata_updated: '2026-11-01'
---

# 日期与时间

| 用途 | 格式 | 示例 |
|---|---|---|
| 手写记录、正文展示 | `YYYY.MM.DD` | `2026.11.01` |
| 文件名、归档排序 | `YYYYMMDD` | `20261101` |
| Frontmatter 内容日期 | `YYYY-MM-DD` 或 `null` | `'2026-11-01'` |
| 精确发布时间、系统事件 | ISO 8601，含秒和时区 | `'2026-11-01T18:30:00+08:00'` |

本地发布、年月目录和默认标题统一使用 `Asia/Shanghai`。`extra.published_at` 保存已有的精确发布时间；内容日期 `created`、`updated` 与配置整理日期 `metadata_updated` 分开。

严格时间戳必须带时区，不用只有日期的值、文件名、文件修改时间或当前构建时间猜测。未知时间明确留空；原始来源使用其他时区时可保留，再按显示需要转换。时间证据和边界见[时间证据](spec-datetime-evidence-001.md)。
