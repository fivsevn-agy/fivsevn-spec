---
id: spec-gov-terminology-001
title: Terminology Governance 术语治理规范

module: spec
submodule: gov
topic: terminology-definition

type: spec
status: active
canonical: true

summary: >
  定义 fivsevn 系统核心结构术语。
  明确 layer / axis / module / kernel / meta 等概念，
  防止术语漂移与结构混乱。

parents: []
related: []
tags: [terminology, governance, structure]

audience: collaborator
languages: zh / en
maturity: stable
confidence: 0.99
visibility: public
source_of_truth: spec

created: 2026-03-03
updated: 2026-03-03
---
# Terminology Governance

# 术语治理规范

Purpose / 目的：

Define stable structural terminology used across the fivsevn system.  
定义 fivsevn 系统的核心结构术语。

These terms are structural, not stylistic.  
这些术语属于结构定义，不属于表达风格。

---

# 1. Layer（层级）

**Definition 定义：**

A hierarchical structural level in the system.  
系统中的纵向层级结构单位。

**Characteristics 特征：**

- Layers are vertical.  
    层级是纵向关系。
    
- Layers are not parallel.  
    不同层级之间不是平行关系。
    
- Higher layers may govern or describe lower layers.  
    上层可以描述或约束下层。
    

**Current Layers 当前层级：**

- Layer 1 — Cognitive Content Layer（认知内容层）
    
- Layer 2 — Kernel / Protocol Layer（内核规则层）
    
- Layer 3 — Meta-Governance Layer（演化治理层）
    

Layer 描述的是 **垂直结构位置**。

---

# 2. Axis（轴 / 内容轴）

**Definition 定义：**

A cognitive organizing dimension inside the Content Layer.  
内容层内部的横向认知组织维度。

**Characteristics 特征：**

- Axes exist only inside Layer 1.  
    轴只存在于内容层内部。
    
- Axes are parallel to each other.  
    轴之间是平行关系。
    
- Each axis has independent structural logic.  
    每条轴有独立的组织逻辑。
    

**Current Content Axes 当前内容轴：**

- posts → temporal axis（时间轴）
    
- natsci → object axis（对象轴）
    
- netcom → system axis（系统轴）
    

Axis 描述的是 **横向认知组织方式**。

---

# 3. Module（模块）

**Definition 定义：**

A structural container at repository or directory level.  
仓库或目录级别的结构容器单位。

**Characteristics 特征：**

- A module belongs to a layer.  
    模块必须属于某一层级。
    
- A module may implement an axis.  
    模块可以承载一个轴。
    
- A module may implement kernel or meta logic.  
    模块也可以承载规则层或演化层功能。
    

**Examples 示例：**

- posts（Layer 1 模块）
    
- natsci（Layer 1 模块）
    
- netcom（Layer 1 模块）
    
- system（Layer 2 模块）
    
- blogops（Layer 3 模块）
    

Module 描述的是 **结构容器单位**。

---

# 4. Kernel Layer（内核层）

**Definition 定义：**

The structural rule-definition layer.  
定义系统结构规则的层级。

**Contains 包含：**

- boot protocol（启动协议）
    
- module map（拓扑结构）
    
- prompt routing（路由规则）
    
- metadata schema（元数据结构）
    

Kernel defines how content is interpreted.  
内核层定义内容如何被解释。

Kernel is not domain content.  
内核层不属于知识内容。

---

# 5. Meta-Governance Layer（演化治理层）

**Definition 定义：**

The system evolution and structural change layer.  
系统结构演化与变更记录层。

**Contains 包含：**

- structural adjustments（结构调整）
    
- publishing strategy changes（发布策略变化）
    
- repository transitions（仓库迁移）
    
- system milestones（系统阶段节点）
    

Meta layer documents change.  
演化层记录变化。

Meta layer does not organize knowledge objects.  
演化层不组织知识对象。

---

# 6. Domain（领域）

**Definition 定义：**

A subject-matter subdivision inside a module.  
模块内部的主题领域分区。

Examples 示例：

Inside natsci：

- taxonomy（分类）
    
- methods（方法）
    
- field-notes（观察记录）
    

Inside netcom：

- protocol（协议）
    
- architecture（架构）
    
- rf（射频）
    

Domain 是模块内部结构单位，不等同于轴。

---

# 7. Canonical（权威标识）

**Definition 定义：**

A document designated as authoritative.  
被指定为权威版本的文档。

**Characteristics 特征：**

- May serve as source_of_truth  
    可作为 source_of_truth
    
- Should not be casually modified  
    不应随意修改
    
- Represents stable structural knowledge  
    代表稳定结构知识
    

Canonical 是元数据标识，不是层级。

---

# 8. Stream（流 / 展示流）

**Definition 定义：**

A presentation interface for time-ordered publication.  
按时间顺序展示内容的界面层。

**Characteristics 特征：**

- UI-level concept  
    属于展示层概念
    
- Not equivalent to canonical archive  
    不等同于权威存档
    
- May aggregate multiple modules  
    可聚合多个模块内容
    

Stream 属于展示逻辑，不属于结构权威层。

---

# 9. Topology（拓扑）

**Definition 定义：**

The structural relationship map between layers and modules.  
层级与模块之间的结构关系图。

Defined in 定义位置：

- module-map.md
    
- boot protocol
    

Topology 描述结构关系，而非内容。

---

# 10. Stability Principle（结构稳定原则）

- Layers must not be casually redefined.  
    层级不得随意重新定义。
    
- Axes require structural justification before creation.  
    新增轴必须有结构性理由。
    
- Meta layer must not become a dumping ground.  
    演化层不得成为杂项堆积区。
    
- Kernel layer must remain content-neutral.  
    内核层必须保持内容中立。
    

---

# 最终统一定义

Layer = 垂直结构  
Axis = 内容层内部的横向组织维度  
Module = 结构容器  
Kernel = 规则定义层  
Meta = 系统演化层

