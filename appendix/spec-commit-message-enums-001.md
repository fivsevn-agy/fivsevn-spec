---
id: "spec-commit-message-enums-001"
title: "Commit Message 枚举表"

module: "spec"
submodule: "appendix"
topic: "spec-commit-message-enums-001"

type: "spec"
status: "active"
canonical: true

summary: "说明Commit Message 枚举表。"

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

# 提交前缀

| 前缀 | 用途 |
|---|---|
| `init` | 初始化仓库或初始结构 |
| `feat` | 新内容、规则或功能 |
| `docs` | 说明文档 |
| `fix` | 修正错误 |
| `refactor` | 调整结构，保持内容含义 |
| `style` | 仅格式变化 |
| `chore` | 清理、配置及维护 |
| `test` | 测试和验证 |
| `revert` | 撤销已有提交 |

格式为 `prefix: Summary`。摘要写具体对象和结果；常用动词有 Add、Update、Correct、Remove、Move、Rename、Split、Merge。完整规则见[提交信息](../gov/spec-commit-message-001.md)。
