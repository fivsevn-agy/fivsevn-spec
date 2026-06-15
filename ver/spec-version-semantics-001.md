# Version Semantics
# 版本语义说明

本文说明 `ver/` 目录的预留用途。  
当前阶段，本目录不定义复杂版本规则，只保留未来扩展位置。

---

## 1. 目的

`ver/` 用于未来说明内容变化在版本层面的意义。

它可能用于区分：

```text
update     小幅更新
revision   修订
rewrite    重写
migration  迁移
deprecate  废弃
archive    归档
```

这些语义用于说明“一个内容单元发生了什么层级的变化”。

---

## 2. 当前状态

当前阶段，fivsevn-spec 暂不启用独立版本语义规范。

日常提交分类仍以以下文件为准：

```text
gov/spec-commit-message-001.md
```

归档和旧文件处理以以下文件为准：

```text
archive/spec-archive-policy-001.md
```

---

## 3. 暂不展开的原因

版本语义容易与 commit message、archive policy 和内容维护流程重叠。

因此，在规则尚未稳定前，`ver/` 只作为预留目录，避免过早引入额外维护负担。

---

## 4. 后续可能扩展

未来如果需要，可以在本目录中增加：

```text
spec-version-semantics-001.md
spec-version-lifecycle-001.md
spec-version-migration-001.md
```

在正式启用前，README 中可将 `ver/` 标记为预留目录。

---
