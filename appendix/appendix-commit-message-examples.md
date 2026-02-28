---
id: module-submodule-topic-001   # 全仓唯一主键，不随文件名变化

title: 标题                         # 给人读的标题

module: module-name               # 一级模块（natsci / netcom / posts / blogops / system / narrative）
submodule: submodule-name         # 二级分类（如 rf / lora / taxonomy）
topic: specific-topic             # 具体对象或主题（如 meshtastic / coleoptera）

type: note                        # 内容类型（note / article / index / log / spec / release 等）
status: active                    # 当前状态（draft / active / archived）
canonical: true                   # 是否权威版本

summary: >                        # 1–2 句摘要，供 AI 快速扫描
  简要说明这篇内容解决什么问题。

parents: []                       # 上级节点（通常只 1 个 index）
related: []                       # 相关内容 id 列表

tags: []                          # 关键词标签（3–8 个为宜）

audience: [self]                  # 目标读者（self / public / tutorial / collaborator）
languages: [zh]                   # 内容语言（zh / en / jp 等）

maturity: evolving                # 认知成熟度（draft / evolving / stable / deprecated）
confidence: 0.70                  # 主观确定度（0–1）

visibility: public                # 可见性（public / private）
source_of_truth: devlog           # 权威来源（devlog / site / other）

created: 2026-01-01               # 创建日期（YYYY-MM-DD）
updated: 2026-01-01               # 最近修改日期
---
# Commit Message Examples

- This document provides practical commit message examples for reference only.

---
## init

> Initialize a repository or establish the initial structure.

```
init: Establish fivsevn-spec repository structure
```
```
init: Initialize specification repository
```

---
## feat

> Add new content, rules, or capabilities for the first time.

```
feat: Add spacetime datetime format specification
```
```
feat: Add source classification rules
```
```
feat: Add initial content structure
```

---
## docs

> Add or update documentation and explanatory text.

```
docs: Add initial README
```
```
docs: Update structure overview
```
```
docs: Clarify archive status definition
```

---
## fix

> Correct errors without changing the intended meaning.

```
fix: Correct typo in spacetime specification
```
```
fix: Fix broken internal link
```
```
fix: Correct incorrect field name example
```

---
## refactor

> Reorganize or restructure content without changing its meaning.

```
refactor: Reorganize spacetime specifications
```
```
refactor: Split content rules into separate files
```
```
refactor: Rename files for clarity
```

---
## style

> Change formatting only, without affecting meaning.

```
style: Reformat headings and lists
```
```
style: Normalize spacing
```

---
## test

> Add temporary or experimental content for testing purposes.

```
test: Try alternative frontmatter layout
```
```
test: Add temporary sample for structure testing
```

---
## chore

> Perform maintenance or cleanup tasks.

```
chore: Remove unused appendix draft
```
```
chore: Clean up obsolete notes
```

---
## revert

> Revert a previous commit.

```
revert: docs: Update README structure overview
```


