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
updated: "2026-06-16"
metadata_updated: "2026-10-13"
---
# System Map
# 仓库结构说明

本文说明 fivsevn-spec 仓库中各主要目录的基本职责。  
本文件只作为结构说明，不替代各目录中的正式规范文档。

---

## 1. 目的

fivsevn-spec 会持续调整和扩展。  
为了避免目录含义混乱，本文件用于说明每个目录主要放什么、不主要放什么。

---

## 2. 目录职责

```text
appendix/
  辅助材料、枚举表、速查表、示例集合。

archive/
  历史文档处理规则、归档策略和旧文件处理说明。

content/
  内容文件本身的规范，例如 frontmatter、正文结构、内容组织方式。

gov/
  行为规则和流程规范，例如 commit message、维护流程、协作规则。

source/
  来源、引用、资料类型和证据来源相关规范。

spacetime/
  日期、时间、时间戳和严格时间语义相关规范。

system/
  仓库自身结构、目录职责和系统性说明。

tools/
  共用字段校验、发布包校验和媒体命名工具。

tests/
  schema、字段工具和媒体命名的回归测试。
```

---

## 3. 使用原则

- 当前有效规范应放在对应主题目录中；
- 枚举、示例、速查材料优先放入 `appendix/`；
- 已被替代的旧规则和无用中间文件在核对引用后删除，历史版本由 Git 保存；
- README 应只链接当前有效规范；
- 已退役文件不作为当前规范入口；
- 目录含义发生变化时，应同步更新本文。

---

## 4. 当前状态

当前阶段，仓库主要维护以下几类规范：

```text
content      frontmatter 与内容组织规则
gov          commit message 等行为规范
spacetime    日期、时间与严格时间戳规则
source       来源与引用规范
archive      旧文件与归档处理规则
appendix     枚举与速查材料
```

`system/` 记录仓库结构，`tools/` 和 `tests/` 维护共用工具及其校验。

---
