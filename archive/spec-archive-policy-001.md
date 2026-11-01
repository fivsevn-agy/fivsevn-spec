---
id: "spec-archive-policy-001"
title: "历史文档与旧文件处理规则"

module: "spec"
submodule: "archive"
topic: "spec-archive-policy-001"

type: "spec"
status: "active"
canonical: true

summary: "说明历史文档与旧文件处理规则。"

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

# 旧文件清理

- 当前目录只保留有效规则、源文件和必要的发布状态。
- 已被替代的规范、一次性导入报告和不再使用的临时文件，在核对引用后删除。
- 删除或移动文件时，同步修正当前链接和脚本入口。
- 正式内容、草稿、原始素材和恢复发布所需的状态文件分别核实，不按文件年龄删除。
- 旧版本由 Git 历史保留，不额外建立 `legacy/` 或备份副本。
