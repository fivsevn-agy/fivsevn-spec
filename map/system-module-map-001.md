---
id: system-module-map-001
title: Module Topology Map

module: system
submodule: map
topic: structural-axes

type: specification
status: active
canonical: true

summary: >
  定义 fivsevn 内容系统的模块拓扑结构。
  明确各模块职责边界与语义轴线，
  作为结构解析与未来扩展的基础。

parents: [spec-index]
related: []
tags: [structure, topology, modules]

audience: self
languages: zh
maturity: evolving
confidence: 0.95
visibility: public
source_of_truth: spec

created: 2026-03-01
updated: 2026-03-01
---

# Module Topology Map

fivsevn-spec 由以下语义轴线构成：

---

## 1. Governance Axis（行为规则）

目录：`/gov`

功能：
- 行为一致性
- 提交规范
- 元数据约束

关键词：流程、约束、复现性

---

## 2. Version Axis（变化语义）

目录：`/ver`

功能：
- 区分更新 vs 修订 vs 重写
- 定义版本层级

关键词：演化、语义变化

---

## 3. Content Axis（内容结构）

目录：`/content`

功能：
- frontmatter
- body
- backmatter
- 结构可解析性

关键词：结构、可迁移性

---

## 4. Source Axis（来源与证据）

目录：`/source`

功能：
- 信息可信度分层
- 引用标准

关键词：证据、来源、引用

---

## 5. Spacetime Axis（时空语义）

目录：`/spacetime`

功能：
- 时间戳规范
- 语境保真

关键词：时间、语境、语义冻结

---

## 6. Archive Axis（长期保存）

目录：`/archive`

功能：
- 长期可访问
- 版本可追溯

关键词：存档、可持续性

---

## System Logic

- 所有内容必须同时落在多个轴线的交叉点上。
- 任何新模块都必须明确其所属语义轴线。
- 禁止语义混合。