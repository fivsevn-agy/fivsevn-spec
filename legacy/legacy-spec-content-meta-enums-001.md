---
module: system
type: note
status: archived
canonical: false
summary: >
  archived
tags: [archive]
visibility: public
source_of_truth: devlog
updated: 2026-06-15
---
# Metadata Enumerations
# 元数据枚举规范

This file defines all allowed enumerated values for YAML metadata.

Do not introduce new values without updating this file.

---

1. module

一级模块（知识域）

Top-level knowledge domains.
一级知识领域分类。

Allowed values / 允许值：
	•	natsci — Natural Science / 自然科学模块
	•	netcom — Network & Communication / 通讯与网络技术模块
	•	posts — Essays & Time Stream / 随笔与时间流模块
	•	ops — Public Operations Log / 运维与仪式日志模块
	•	system — Core System Definitions / 系统核心结构模块
	•	narrative — Narrative Interface Layer / 叙事接口模块

⸻

2️⃣ type

内容类型

Content classification.
内容分类方式。

Allowed values / 允许值：
	•	note — Study note / 学习笔记
	•	article — Formal article / 成文文章
	•	index — Directory page / 目录页
	•	log — Timeline or update log / 时间流或更新记录
	•	spec — Specification document / 规范文件
	•	release — Version release note / 版本发布说明
	•	dataset — Structured data list / 数据清单
	•	howto — Procedural guide / 操作指南
	•	interface — System or AI interface file / 系统或 AI 接口文件

⸻

3️⃣ status

当前状态

Current working state.
当前工作状态。

Allowed values / 允许值：
	•	draft — In progress / 草稿阶段
	•	active — Current valid content / 当前有效内容
	•	archived — Historical archive / 历史归档内容

⸻

4️⃣ maturity

认知成熟度

Epistemic stage of the content.
内容在知识层面的成熟阶段。

Allowed values / 允许值：
	•	draft — Concept not yet formed / 概念尚未成型
	•	evolving — Structured but subject to change / 结构稳定但仍在演化
	•	stable — Long-term valid / 长期有效
	•	deprecated — Replaced or outdated / 已被替代或过时

⸻

5️⃣ audience

目标读者

Target reader category.
目标读者类型。

Allowed values / 允许值：
	•	self — Personal reference / 个人自用
	•	public — Public-facing content / 面向公众
	•	tutorial — Educational / 教程型内容
	•	collaborator — Intended for collaborators / 协作者使用

⸻

6️⃣ visibility

可见性

Access scope.
访问范围。

Allowed values / 允许值：
	•	public — Publicly accessible / 公开
	•	private — Restricted access / 私有

⸻

7️⃣ languages

内容语言

Content language codes.
内容语言代码。

Common values / 常用值：
	•	zh — Chinese / 中文
	•	en — English / 英文
	•	jp — Japanese / 日文

Additional languages allowed if needed.
如需新增语言，可扩展。

⸻

8️⃣ source_of_truth

权威来源

Authoritative source location.
权威版本来源位置。

Allowed values / 允许值：
	•	devlog — Git repository canonical source / 仓库为权威版本
	•	site — Website canonical source / 网站为权威版本
	•	external — External source / 外部来源
	•	mixed — Multiple sources / 多来源混合

⸻

Governance Rules

维护规则
	1.	Enumerations are versioned.
枚举值受版本控制。
	2.	Adding new values requires explicit update to this file.
新增枚举必须更新本文件。
	3.	Avoid semantic overlap between values.
避免语义重叠。
	4.	Do not create synonyms.
不允许同义词并存。
	5.	Keep vocabulary minimal and stable.
词汇保持最小化与稳定。

⸻

