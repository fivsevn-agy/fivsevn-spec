---
id: system-gov-meta-frontmatter-001
title: Frontmatter Metadata Template

module: system
submodule: governance
topic: metadata-template

type: spec
status: active
canonical: true

summary: >
  定义所有文档 YAML 头部字段结构与使用说明，
  作为仓库统一的元数据模板。

parents: []
related: [
  system-gov-meta-enums-001,
  system-gov-commit-message-001
]
tags: [system, governance, metadata, template]

audience: collaborator
languages: zh
maturity: stable
confidence: 1.00
visibility: public
source_of_truth: spec

created: 2026-03-01
updated: 2026-03-01
---
## Frontmatter Template

```yaml
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
```
