# Archive and Legacy Policy
# 历史文档与旧文件处理规则

本文说明 fivsevn-spec 中旧文档、历史规范和退役文件的处理方式。

本规则保持简单，主要用于降低迭代压力：  
当仓库发生较大调整时，不要求立即彻底判断每个旧文件的最终去向，而是先将旧文件从当前规范入口中移出，保留可追溯性，再逐步清理。

---

## 1. 基本思路

fivsevn-spec 会持续迭代。  
在结构调整、规范重写、文件合并或文件拆分时，旧文件不一定需要立刻删除。

推荐做法是：

```text
当前有效文档保持清楚；
旧文档先移入 legacy；
确实无价值时再删除。
```

这样可以避免两种问题：

- 当前目录被旧文件干扰；
- 旧内容过早删除，导致以后无法回看、比较或恢复。

---

## 2. 目录分工

### 2.1 `legacy/`

`legacy/` 用于保存旧文件本体。

适用情况：

- 文件来自旧结构；
- 文件已经不再作为当前规范使用；
- 文件仍有参考、迁移、比对或追溯价值；
- 暂时不想立即删除。

简单理解：

```text
legacy = 旧文件存放区
```

---

### 2.2 `archive/`

`archive/` 用于保存归档规则和历史处理说明。

适用情况：

- 说明历史文件如何处理；
- 说明旧文件何时进入 `legacy/`；
- 说明退役文档如何标记；
- 保存归档政策类文档。

简单理解：

```text
archive = 归档规则说明区
```

当前约定下，历史文件本体主要放入 `legacy/`，而不是堆入 `archive/`。

---

## 3. Legacy 文件命名方式

旧文档迁入 `legacy/` 时，采用最小改名规则：

```text
legacy-原文件名
```

示例：

```text
spec-gov-commit-message-001.md
→ legacy/legacy-spec-gov-commit-message-001.md
```

```text
content-frontmatter.md
→ legacy/legacy-content-frontmatter.md
```

```text
spec-datetime-format-001.md
→ legacy/legacy-spec-datetime-format-001.md
```

该规则的目的：

- 保留原文件名主体，方便追溯；
- 一眼识别该文件已经是历史文件；
- 不需要为旧文件重新设计命名；
- 降低大规模调整时的操作成本。

迁入 `legacy/` 的文件不需要重新套用当前命名规范。

---

## 4. 旧文档处理流程

当一次改动会替换、重写或废弃旧文档时，按以下流程处理：

```text
1. 新文档放入当前有效目录；
2. 旧文档文件名前加 legacy-；
3. 旧文档移动到 legacy/；
4. README 只链接当前有效文档；
5. 如有必要，在旧文档中使用归档 frontmatter；
6. 确认完全无价值后，再考虑删除旧文档。
```

推荐优先保留旧文件，不急于删除。

---

## 5. 归档 frontmatter

历史文档退役时，可以使用以下简化 frontmatter：

```yaml
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
updated: 2026-03-01
---
```

该 frontmatter 用于标记文件已经退役，不再是当前主版本。

字段含义：

- `status: archived` 表示文档已归档；
- `canonical: false` 表示它不再是当前规范主版本；
- `summary: archived` 表示只保留历史用途；
- `tags: [archive]` 便于识别归档文件；
- `visibility: public` 表示文件可以公开保留；
- `updated` 记录归档或最后处理日期。

---

## 6. 当前规范入口

`legacy/` 中的文件不作为当前规范入口。

当前有效文档应通过以下位置进入：

- 仓库 README；
- 当前目录下的正式规范文件；
- 当前索引或模块映射文件。

README 不应把 `legacy/` 文件列为正式规范链接。  
如果 README 仍链接到旧文件，应在整理时更新为新文件路径。

---

## 7. 什么时候可以删除旧文件

旧文件满足以下条件时，可以考虑删除：

- 已经被新版文档完全取代；
- README 和其他文档不再引用它；
- 不需要再用于比较旧规则；
- 不含仍有价值的示例、命名、字段或历史说明；
- 删除不会影响理解当前规范。

如果不确定，应先保留在 `legacy/` 中。

---

## 8. 最小维护原则

旧文件进入 `legacy/` 后，一般不再继续维护。

除非出现以下情况，否则不需要修改旧文件：

- 修正明显错误链接；
- 添加或替换归档 frontmatter；
- 说明它被哪个新文件取代；
- 调整文件名以符合 `legacy-原文件名` 规则。

legacy 文件的目标是保留历史，而不是继续参与当前规范迭代。

---

## 9. 推荐提交方式

处理旧文件时，建议单独提交。

示例：

```text
chore: Move legacy commit message files
```

```text
chore: Archive outdated frontmatter specifications
```

```text
refactor: Replace legacy spacetime documents
```

如果同时新增新版文档和移动旧文档，建议拆成两次提交：

```text
docs: Add updated frontmatter specification
chore: Move old frontmatter documents to legacy
```

这样可以保持提交历史清楚，也方便以后回看。

---
