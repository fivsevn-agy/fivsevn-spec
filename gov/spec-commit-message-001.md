---
id: "spec-commit-message-001"
title: "Commit Message 说明"

module: "spec"
submodule: "gov"
topic: "spec-commit-message-001"

type: "spec"
status: "active"
canonical: true

summary: "说明Commit Message 说明。"

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

# 提交信息

```text
prefix: Summary
```

前缀小写，冒号后一个空格；摘要直接说明改动，用一句话，不加句号。英文摘要首词首字母大写。一次提交尽量处理同一类改动；原因和必要细节放在提交正文。

```text
feat: Add field observation
fix: Correct pagination links
docs: Update publishing instructions
chore: Remove unused import files
```

前缀及用途见[取值表](../appendix/spec-commit-message-enums-001.md)。不使用 `update`、`test123`、`final` 等无法辨认改动的摘要。
