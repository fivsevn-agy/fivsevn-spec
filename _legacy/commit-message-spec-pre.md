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
> Status: legacy  
> Validity: expired  
> Replaced by: [gov-commit-message.md](../gov/gov-commit-message.md)
> Note: retained for historical reference only

---

# Git 提交规范  

请保持每次 commit **只修改一类内容**，单独 commit，避免混合推送。

---

## 额外建议

- 使用英文撰写 commit message。
- 如果中文更便于回忆，可在英文后加注释。

---

# Git 提交前缀备忘录（Conventional Commits）

> 提交信息格式：
>
> `前缀: 空格 + 摘要内容`
>
> ✅ 正确示例：`feat: Add initial note structure`

---

## 常用前缀说明与示例

| 层级 | 改动例子| commit 类型 |
|-----|--------|------------|
| 内容层 | 改正文、补段落、加脚注、翻译 | feat / fix |
| 结构层 | 调整小节顺序、插入新部分、加图片 | refactor / feat |
| 元信息层 | 改 lang、category、pin 等字段 | chore / style |
| 注释/模板 | 增加注释说明、模板文档、写提交规范等 | docs |
  
--- 

### 1. feat（新增内容 / 功能）
用于添加新文件、新笔记、新结构等。

- `feat: Add initial notes`  
  添加了初始的笔记内容。
- `feat: Add image upload section`  
  增加了图片上传的说明或功能。
- `feat: Create new documentation folder`  
  新建了一个文档文件夹。

---

### 2. fix（修复问题）
用于修复错误、字段拼写、类型不正确、路径错误等。

- `fix: Correct typo in note`  
  修复了笔记中的拼写错误。
- `fix: Fix broken internal link`  
  修复了笔记内部的无效链接。
- `fix: correct boolean value for pin field`  
  修正了布尔值写法。

---

### 3. docs（文档修改）
用于添加或改进注释、模板、说明文档，不涉及正文内容变动。

- `docs: Update README`  
  更新了 README 文档。
- `docs: Revise formatting in notes`  
  调整了笔记中的排版格式。
- `docs: Add usage instructions`  
  补充了使用说明或操作指南。
- `docs: write git commit guide`  
  写了一份 Git 提交规范文档。

---

### 4. style（格式调整）
仅修改格式，不改变实际内容，如空格、缩进、标点等。

- `style: Reformat headings`  
  重新整理了标题的格式。
- `style: Standardize bullet lists`  
  统一了项目符号列表的格式。

---

### 5. refactor（结构重组）
用于调整字段顺序、重命名字段等非功能性重构。

- `refactor: Split note into sections`  
  将一份笔记拆分为多个部分。
- `refactor: Rename files for clarity`  
  重命名文件以提升可读性。

---

### 6. chore（杂项维护）
用于非内容性的修改，如文件重命名、项目配置、删除临时文件等。

- `chore: Remove unused images`  
  删除了未使用的图片文件。
- `chore: Rename old files`  
  重命名了一些旧文件。
- `chore: Update ignore rules`  
  更新了 `.gitignore` 忽略规则。

---

### 7. test（测试相关）
用于测试功能、文件结构、内容展示效果等。

- `test: Add sample note for testing`  
  添加了用于测试的示例笔记。
- `test: Try image insertion`  
  测试插入图片的显示效果。

---

### 8. revert（撤销提交）
用于撤销先前的变更（由 `git revert` 自动生成）。

- `revert: fix: correct boolean value for pin field`

---

## 使用规范小结

- 使用英文冒号 `:`（后跟一个空格）
- 不使用中文冒号 `：`
- 摘要尽量控制在 50 字符以内
- 用**祈使句**（如“Add”“Fix”“Update”），不要写成“Added”“I fixed”等

---