---
id: "spec-system-map-001"
title: "仓库结构说明"

module: "spec"
submodule: "system"
topic: "spec-system-map-001"

type: "spec"
status: "active"
canonical: true

summary: "说明仓库结构说明。"

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

# 仓库目录

| 目录 | 内容 |
|---|---|
| `content/` | 字段、发布包、媒体和译文规则及 schema |
| `tools/`、`tests/` | 共享工具和回归测试 |
| `appendix/` | 枚举和速查 |
| `source/` | 来源登记和引用格式 |
| `spacetime/` | 日期、时间和证据 |
| `gov/` | 提交信息 |
| `archive/` | 旧文件清理规则 |

README 只链接当前规则；过时文本和中间文件删除，历史版本从 Git 查询。
