# Commit Message 说明

本文定义 fivsevn 相关仓库中 Git commit message 的写法。  
目标是让提交历史保持清楚、单一、可追溯，便于以后回看、比较、撤销和整理。

本文说明写作原则与基本格式。可用前缀、前缀含义与示例，另见 `commit-message-enums.md`。

---

## 目录

- [1. 规范目的](#1-规范目的)
- [2. 基本原则](#2-基本原则)
- [3. 基本格式](#3-基本格式)
- [4. 前缀的作用](#4-前缀的作用)
- [5. 简要说明的写法](#5-简要说明的写法)
- [6. 常见判断方式](#6-常见判断方式)
- [7. 不推荐写法](#7-不推荐写法)
- [8. 与枚举文件的关系](#8-与枚举文件的关系)

---

## 1. 规范目的

commit message 是一次提交的标题。它应当用一句话说明：这次提交主要改变了什么。

本规范的目的不是增加形式负担，而是让提交历史具有稳定的阅读价值。良好的提交记录应当让人能够快速判断：

- 这次提交属于新增、修正、整理、维护还是撤销；
- 改动是否影响正文内容；
- 改动是否只涉及格式、结构或说明；
- 日后如果需要回退，应当回退哪一次提交。

提交记录本身应当成为一条可靠的修改历史，而不是一串难以辨认的临时备注。

---

## 2. 基本原则

### 2.1 一次提交只做一类事情

一次 commit 应尽量只处理同一类改动。

例如：

```text
写一篇新内容          → 单独提交
修正文中的错误        → 单独提交
调整文件结构          → 单独提交
统一标题和列表格式    → 单独提交
删除不用的草稿或资源  → 单独提交
```

这样做的好处是：

- 历史记录更容易阅读；
- 后续比较差异更清楚；
- 需要撤销时不会牵连无关改动；
- 不同性质的工作不会混在一起。

如果一次改动同时包含“新增内容”和“格式整理”，通常应拆成两次提交。

---

### 2.2 提交信息只回答一个问题

commit message 的第一行只回答一个问题：

```text
这次提交最核心的改动是什么？
```

它不是日记，也不是详细说明书。  
细节可以留在正文、Pull Request、issue、工作日志或后续说明文档里。

---

### 2.3 先判断改动性质，再选择前缀

提交前缀不是装饰，而是分类。

写 commit message 时，应先判断这次提交主要是在做什么：

- 新增内容；
- 修正错误；
- 更新说明；
- 调整结构；
- 统一格式；
- 清理维护；
- 测试试验；
- 撤销旧提交。

确认性质之后，再选择合适的前缀。

---

## 3. 基本格式

标准格式如下：

```text
prefix: Summary
```

例如：

```text
feat: Add initial content structure
```

格式要求：

- 前缀使用小写英文；
- 前缀后使用英文冒号；
- 英文冒号后加一个空格；
- 简要说明使用一句可读的话；
- 简要说明第一个单词首字母大写；
- 简要说明不以句号结尾；
- 一行内说清楚核心改动。

推荐：

```text
docs: Update README structure overview
fix: Correct broken internal link
refactor: Split frontmatter rules into separate files
```

不推荐：

```text
docs：Update README
fix:correct link
update
修改一下
feat: add thing.
```

---

## 4. 前缀的作用

前缀用于说明“这次提交属于哪一类改动”。

常用前缀包括：

```text
init
feat
docs
fix
refactor
style
chore
test
revert
```

不同前缀之间的边界，应按照“主要改动对象”判断。

例如：

- 写一篇新的内容，用 `feat`；
- 修改规范说明文字，用 `docs`；
- 修正文中错误，用 `fix`；
- 拆分文件、调整目录，用 `refactor`；
- 只改缩进、空行、标题格式，用 `style`；
- 删除不用文件、整理配置，用 `chore`。

具体前缀含义、可用范围和示例，见 `commit-message-enums.md`。

---

## 5. 简要说明的写法

简要说明应当具体、准确、可回看。

### 5.1 使用动词开头

推荐使用动词开头：

```text
Add
Update
Clarify
Correct
Fix
Split
Rename
Remove
Reorganize
Normalize
```

示例：

```text
docs: Clarify frontmatter status behavior
fix: Correct source_of_truth example
refactor: Rename commit message files
```

### 5.2 避免空泛词

不推荐只写：

```text
update
change
misc
fix
work
test
```

这些词无法说明实际改动。

如果确实是更新，应写清楚更新了什么：

```text
docs: Update commit message examples
```

如果确实是修正，应写清楚修正了什么：

```text
fix: Correct typo in commit message guide
```

---

### 5.3 控制长度

简要说明宜控制在一行内。  
一般不超过 50 个英文字符；必要时可以略长，但不应变成完整段落。

推荐：

```text
docs: Add commit message quick reference
```

不推荐：

```text
docs: Add a very long and detailed explanation about how commit messages should be written in every possible repository situation
```

---

## 6. 常见判断方式

### 6.1 新增内容还是说明文档

如果新增的是正文内容、主题内容、笔记或文章，通常使用：

```text
feat
```

如果新增的是说明、规范、指南、README、模板解释，通常使用：

```text
docs
```

示例：

```text
feat: Add paleontology whale necropolis note
docs: Add commit message specification
```

---

### 6.2 修正错误还是调整表述

如果原文存在明确错误，应使用：

```text
fix
```

如果只是让表达更清楚、结构更合理，但原意未错，通常使用：

```text
docs
```

或在结构调整明显时使用：

```text
refactor
```

示例：

```text
fix: Correct incorrect status example
docs: Clarify status and visibility distinction
refactor: Reorganize frontmatter explanation sections
```

---

### 6.3 结构调整还是格式调整

如果移动、拆分、合并、重命名内容，属于结构调整：

```text
refactor
```

如果只调整空行、缩进、标题层级、列表格式，属于格式调整：

```text
style
```

示例：

```text
refactor: Split commit rules into spec and enums
style: Normalize heading levels
```

---

### 6.4 删除文件用什么前缀

如果删除的是过时内容、无用资源、临时文件，通常使用：

```text
chore
```

如果删除本身是一次结构重整的一部分，也可以使用：

```text
refactor
```

示例：

```text
chore: Remove obsolete draft notes
refactor: Remove duplicated commit examples section
```

---

### 6.5 撤销提交

撤销旧提交时使用：

```text
revert
```

示例：

```text
revert: docs: Update README structure overview
```

如果由 Git 自动生成 revert 信息，通常可以保留自动生成的格式。

---

## 7. 不推荐写法

以下写法不推荐使用。

### 7.1 没有前缀

```text
Update README
Fix link
Add files
```

应改为：

```text
docs: Update README
fix: Fix broken link
feat: Add initial files
```

---

### 7.2 使用中文冒号

```text
docs：Update README
```

应改为：

```text
docs: Update README
```

---

### 7.3 前缀与内容不匹配

```text
feat: Fix broken link
fix: Add new content section
style: Rename content files
```

应改为：

```text
fix: Fix broken link
feat: Add new content section
refactor: Rename content files
```

---

### 7.4 一次提交包含多类事情

不推荐：

```text
feat: Add new note and fix README typo
```

更好的做法是拆成两次提交：

```text
feat: Add new note
fix: Correct README typo
```

---

## 8. 与枚举文件的关系

本文说明 commit message 的写作原则和基本判断方式。  
具体前缀、适用场景、推荐动词和示例，见：

```text
commit-message-enums.md
```

两份文件的职责如下：

| 文件 | 职责 |
|---|---|
| `spec-commit-message-spec-001.md` | 说明 commit message 的格式、原则和判断方式 |
| `spec-commit-message-enums-001.md` | 列出前缀枚举、适用场景、常用动词和示例 |

---
