---
id: 
title: 

module: system / natsci / netcom / posts / blogops / narrative
submodule: 
topic: 

type: note / article / index / log / spec / release
status: draft / active / archived
canonical: true / false

summary: >

parents: []
related: []
tags: []

audience: self / public / tutorial / collaborator
languages: zh / en / jp
maturity: draft / evolving / stable / deprecated
confidence: 0.0
visibility: public / private
source_of_truth: devlog / site / spec / internal

created: 
updated: 
---
# Commit Message Specification
# Git提交规范

---
## 1. 规范目的

- 1.1 本规范用于说明：每一次Git提交，应该如何用一句话清楚地说明“这次改动在做什么”。

- 1.2 目标并非追求形式感，而是保证：
  - 追溯时一眼就能够知道当时做了什么
  - 不同类型的改动不会混在一起
  - 提交记录本身能够当作一条可靠的修改历史


---
## 2. 基本原则

- 2.1 `原则a`：一次提交，只做一类事情
  - 保证一次commit只修改同一类型的内容。
  - 目的是为了让历史记录可回溯、可理解、可撤销。
  - 程序员通常称为：atomic commit

```
e.g.
写正文内容→单独一次提交
调整结构或重排顺序→单独一次提交
改格式、修错别字→单独一次提交
```

- 2.2 `原则b`：提交信息只回答一件事
  - 提交信息的那一行是为了说明“这次提交，最核心的改动是什么？”，而非日志或说明书。


---
## 3. 提交信息的基本格式

-  `前缀（全部小写）:空格+简要说明（第一个单词首字母大写）`

  - 使用英文冒号`:`，后面加一个空格
  - 简要说明使用一句完整可读的话
  - 使用祈使语气（Add/Fix/Update）
  - 简要说明句的第一个单词首字母大写

```
e.g.
feat: Add initial content structure
```

### 3.1 提交前缀的含义说明（按“在改什么”来分）

- 下面这些前缀，是为了让人一眼分清：这次是在改内容，还是改结构，还是只是维护。


#### 3.1.1 🤌`feat`：新增内容或新能力

> programmer habit: feature

- 新写了一篇内容
- 新增了一个章节、一个功能性部分
- 第一次把某个东西正式加进来

```
e.g.
feat: Add initial content structure
feat: Add image upload section
```


#### 3.1.2 🤌`fix`：修正错误

> programmer habit: bug fix

- 改错别字
- 修正字段值写错
- 修复链接、路径、拼写问题

```
e.g.
fix: Correct typo in note
fix: Fix broken internal link
```


#### 3.1.3 🤌`docs`：说明性文档的新增或调整

> programmer habit: documentation

- 写README
- 写规范说明
- 写模板、注释、操作说明
- 不用于正文内容本身

```
e.g.
docs: Update README
docs: Add git commit guide
```


#### 3.1.4 🤌`style`：只改外观，不改意思

> programmer habit: formatting

- 调整空格、缩进、换行
- 统一标题或列表格式
- 不改变任何实际含义

```
e.g.
style: Reformat headings
style: Standardize bullet lists
```


#### 3.1.5 🤌`refactor`：调整结构，但不改变内容含义

> programmer habit: refactor

- 重排段落顺序
- 拆分或合并章节
- 重命名文件以便理解

```
e.g.
refactor: Split note into sections
refactor: Rename files for clarity
```


#### 3.1.6 🤌`chore`：维护性杂项

> programmer habit: chore/maintenance

- 删除不用的文件
- 调整配置
- 改`.gitignore`之类的维护工作

```
e.g.
chore: Remove unused images
chore: Update ignore rules
```


#### 3.1.7 🤌`test`：测试和试验

> programmer habit: test

- 添加示例内容用于测试
- 试验结构、展示效果
- 临时验证某种写法

```
e.g.
test: Add sample note for testing
test: Try image insertion
```


#### 3.1.8 🤌`revert`：撤销之前的提交

- 通常由git自动生成

```
e.g.
revert: fix: Correct boolean value for pin field
```


---
## 4. 细节提示

- 使用英文冒号加空格 `: `
- 不使用中文冒号 `：`
- 简要说明控制在50个字符以内
- 一次提交一个核心事件
- 如果中文更便于回忆，也可以在英文后加中文注释

> **清楚、单一、可回看，即可。**



