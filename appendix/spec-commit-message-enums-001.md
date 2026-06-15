# Commit Message 枚举表

本文列出 fivsevn 相关仓库中 commit message 可使用的前缀、适用范围、常用动词和示例。

本文件偏查阅用途。写作原则与格式说明见 `commit-message-spec.md`。

---

## 目录

- [1. 前缀总览](#1-前缀总览)
- [2. `init`](#2-init)
- [3. `feat`](#3-feat)
- [4. `docs`](#4-docs)
- [5. `fix`](#5-fix)
- [6. `refactor`](#6-refactor)
- [7. `style`](#7-style)
- [8. `chore`](#8-chore)
- [9. `test`](#9-test)
- [10. `revert`](#10-revert)
- [11. 常用动词](#11-常用动词)
- [12. 判断速查](#12-判断速查)
- [13. 完整示例集](#13-完整示例集)

---

## 1. 前缀总览

```yaml
commit_prefix:
  - init      # 初始化仓库、建立初始结构
  - feat      # 新增内容、规则、章节或能力
  - docs      # 新增或修改说明性文档
  - fix       # 修正错误
  - refactor  # 调整结构，但不改变内容含义
  - style     # 只调整格式，不改变内容含义
  - chore     # 维护、清理、配置、杂项
  - test      # 测试、试验、临时验证
  - revert    # 撤销之前的提交
```

推荐格式：

```text
prefix: Summary
```

示例：

```text
docs: Add commit message specification
```

---

## 2. `init`

用于初始化仓库或建立初始结构。

```yaml
init:
  meaning: 初始化
  use_when:
    - 创建仓库初始结构
    - 建立第一版目录
    - 添加初始 README
    - 添加最早的基础文件
  avoid_when:
    - 仓库已经进入正常维护阶段
    - 只是新增普通内容
    - 只是调整已有结构
```

示例：

```text
init: Establish fivsevn-spec repository structure
init: Initialize specification repository
init: Add initial README and directory layout
```

---

## 3. `feat`

用于新增内容、规则、章节、能力或正式材料。

```yaml
feat:
  meaning: 新增
  use_when:
    - 新写一篇正文内容
    - 新增一个内容模块
    - 新增一个规范章节
    - 新增一个正式模板
    - 第一次加入某类材料
  avoid_when:
    - 只是修改说明文档
    - 只是修正错误
    - 只是调整格式
    - 只是移动或重排已有内容
```

示例：

```text
feat: Add initial content structure
feat: Add source classification rules
feat: Add spacetime datetime format specification
feat: Add paleontology reading note
feat: Add translation metadata fields
```

---

## 4. `docs`

用于新增或修改说明性文档。

```yaml
docs:
  meaning: 文档说明
  use_when:
    - 新增 README
    - 修改 README
    - 新增规范说明
    - 修改操作说明
    - 补充字段解释
    - 澄清规则含义
    - 更新示例说明
  avoid_when:
    - 新增正文内容
    - 修正文中事实错误
    - 只调整格式
    - 重命名或拆分文件结构
```

示例：

```text
docs: Add initial README
docs: Update structure overview
docs: Clarify archive status definition
docs: Add commit message guide
docs: Clarify status and visibility distinction
docs: Update frontmatter field explanations
```

---

## 5. `fix`

用于修正错误，不改变原本意图。

```yaml
fix:
  meaning: 修正错误
  use_when:
    - 修正错别字
    - 修正拼写错误
    - 修正错误字段名
    - 修复失效链接
    - 修正错误路径
    - 修正错误示例
    - 修正明显不符合规范的值
  avoid_when:
    - 只是让说明更充分
    - 只是调整结构
    - 只是统一格式
    - 新增内容
```

示例：

```text
fix: Correct typo in spacetime specification
fix: Fix broken internal link
fix: Correct incorrect field name example
fix: Correct source_of_truth value
fix: Fix misspelled translation type
fix: Correct README link target
```

---

## 6. `refactor`

用于重组、拆分、合并、移动或重命名，不改变内容含义。

```yaml
refactor:
  meaning: 结构调整
  use_when:
    - 重排章节顺序
    - 拆分长文档
    - 合并重复章节
    - 重命名文件
    - 调整目录结构
    - 将示例移到单独文件
    - 将枚举移到单独文件
  avoid_when:
    - 新增实质内容
    - 修正事实错误
    - 只调整空格和格式
    - 删除无用文件但没有结构重整
```

示例：

```text
refactor: Reorganize spacetime specifications
refactor: Split content rules into separate files
refactor: Rename files for clarity
refactor: Move commit examples into enum document
refactor: Reorder frontmatter sections
refactor: Split frontmatter spec and enums
```

---

## 7. `style`

用于只改变格式，不改变意思。

```yaml
style:
  meaning: 格式调整
  use_when:
    - 调整空行
    - 调整缩进
    - 统一标题层级
    - 统一列表格式
    - 统一代码块样式
    - 统一表格排版
  avoid_when:
    - 改变文字含义
    - 新增解释
    - 修正错误
    - 调整文件结构
```

示例：

```text
style: Reformat headings and lists
style: Normalize spacing
style: Standardize YAML code blocks
style: Align table formatting
style: Normalize bullet lists
```

---

## 8. `chore`

用于维护性杂项。

```yaml
chore:
  meaning: 维护
  use_when:
    - 删除不用文件
    - 清理过时草稿
    - 调整配置
    - 修改 .gitignore
    - 清理临时资源
    - 更新维护性文件
    - 整理非正文资产
  avoid_when:
    - 新增正式内容
    - 修改规范正文
    - 修正具体错误
    - 结构性重组明显时
```

示例：

```text
chore: Remove unused appendix draft
chore: Clean up obsolete notes
chore: Remove unused images
chore: Update ignore rules
chore: Delete temporary test files
```

---

## 9. `test`

用于测试、试验或临时验证。

```yaml
test:
  meaning: 测试
  use_when:
    - 添加测试样本
    - 试验结构布局
    - 验证 frontmatter 解析
    - 测试页面展示
    - 临时加入示例内容
  avoid_when:
    - 新增正式内容
    - 更新正式说明
    - 修正正式错误
    - 删除测试材料；删除时通常用 chore
```

示例：

```text
test: Try alternative frontmatter layout
test: Add temporary sample for structure testing
test: Add sample note for testing
test: Try image insertion
test: Verify module index generation
```

---

## 10. `revert`

用于撤销之前的提交。

```yaml
revert:
  meaning: 撤销
  use_when:
    - 撤销某次提交
    - 回退错误修改
    - 恢复到旧版本状态
  avoid_when:
    - 只是修正一个小错误
    - 只是重新调整写法
    - 并未实际撤销旧提交
```

示例：

```text
revert: docs: Update README structure overview
revert: fix: Correct boolean value for pin field
revert: feat: Add temporary frontmatter layout
```

---

## 11. 常用动词

### 11.1 新增类

```yaml
verbs_add:
  - Add        # 新增
  - Create     # 创建
  - Introduce  # 引入
  - Establish  # 建立
  - Initialize # 初始化
```

示例：

```text
feat: Add source classification rules
init: Establish repository structure
```

---

### 11.2 更新说明类

```yaml
verbs_docs:
  - Update   # 更新
  - Clarify  # 澄清
  - Explain  # 解释
  - Document # 记录或成文说明
  - Expand   # 扩充
  - Revise   # 修订
```

示例：

```text
docs: Clarify commit message prefix usage
docs: Expand frontmatter enum notes
```

---

### 11.3 修正类

```yaml
verbs_fix:
  - Fix      # 修复
  - Correct  # 纠正
  - Repair   # 修复；较少用
  - Restore  # 恢复
```

示例：

```text
fix: Correct broken internal link
fix: Restore missing heading
```

---

### 11.4 结构调整类

```yaml
verbs_refactor:
  - Split       # 拆分
  - Merge       # 合并
  - Move        # 移动
  - Rename      # 重命名
  - Reorder     # 重排
  - Reorganize  # 重组
  - Restructure # 重构结构
```

示例：

```text
refactor: Split commit rules into spec and enums
refactor: Rename files for clarity
```

---

### 11.5 格式类

```yaml
verbs_style:
  - Format       # 设置格式
  - Reformat     # 重新格式化
  - Normalize    # 统一
  - Standardize  # 标准化
  - Align        # 对齐
```

示例：

```text
style: Normalize spacing
style: Standardize bullet lists
```

---

### 11.6 维护类

```yaml
verbs_chore:
  - Remove  # 移除
  - Delete  # 删除
  - Clean   # 清理
  - Update  # 更新维护性内容
  - Ignore  # 忽略文件或路径
```

示例：

```text
chore: Remove unused draft files
chore: Update ignore rules
```

---

## 12. 判断速查

```yaml
decision_guide:
  new_repository_or_initial_structure: init
  new_content_or_new_rule: feat
  documentation_or_explanation: docs
  error_correction: fix
  structure_change_without_meaning_change: refactor
  formatting_only: style
  maintenance_or_cleanup: chore
  temporary_experiment_or_validation: test
  undo_previous_commit: revert
```

更具体的判断：

```yaml
examples_by_change:
  add_new_note: feat
  add_new_spec_rule: feat
  add_or_update_readme: docs
  clarify_field_meaning: docs
  correct_typo: fix
  fix_broken_link: fix
  split_document: refactor
  rename_file: refactor
  reformat_markdown: style
  normalize_yaml_blocks: style
  remove_unused_file: chore
  update_gitignore: chore
  add_temporary_sample: test
  revert_old_commit: revert
```

---

## 13. 完整示例集

```text
init: Establish fivsevn-spec repository structure
init: Initialize specification repository

feat: Add spacetime datetime format specification
feat: Add source classification rules
feat: Add initial content structure
feat: Add translation metadata fields

docs: Add initial README
docs: Update structure overview
docs: Clarify archive status definition
docs: Add commit message specification
docs: Update commit message examples
docs: Clarify status and visibility distinction

fix: Correct typo in spacetime specification
fix: Fix broken internal link
fix: Correct incorrect field name example
fix: Correct source_of_truth value
fix: Fix misspelled translation type

refactor: Reorganize spacetime specifications
refactor: Split content rules into separate files
refactor: Rename files for clarity
refactor: Split commit rules into spec and enums
refactor: Move examples into enum document

style: Reformat headings and lists
style: Normalize spacing
style: Standardize YAML code blocks
style: Align table formatting

test: Try alternative frontmatter layout
test: Add temporary sample for structure testing
test: Verify module index generation

chore: Remove unused appendix draft
chore: Clean up obsolete notes
chore: Remove unused images
chore: Update ignore rules

revert: docs: Update README structure overview
revert: fix: Correct boolean value for pin field
```

---
