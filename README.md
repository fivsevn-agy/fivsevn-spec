# fivsevn-spec

fivsevn-spec 保存 fivsevn 体系的基础规范，约定内容、来源、引用、时间、提交、归档和版本语义。

---

## 目录结构

```text
fivsevn-spec/
├─ appendix/
├─ archive/
├─ content/
├─ gov/
├─ legacy/
├─ source/
├─ spacetime/
├─ system/
├─ ver/
└─ README.md
```

---

## 索引

### appendix

枚举表、速查表和示例。

- [Commit Message 枚举表](appendix/spec-commit-message-enums-001.md)
- [Content Frontmatter 枚举表](appendix/spec-content-frontmatter-enums-001.md)
- [Content Frontmatter 枚举速查](appendix/spec-content-frontmatter-enums-quickref-001.md)
- [Source Intake 枚举表](appendix/spec-source-intake-enums-001.md)

### archive

旧文件和归档处理规则。

- [Archive and Legacy Policy](archive/spec-archive-policy-001.md)

### content

内容文件的组织规则。

- [Content Frontmatter 说明](content/spec-content-frontmatter-001.md)
- [Content Translation Specification 翻译内容规范](content/spec-content-translation-001.md)

### gov

规范执行过程中的操作规则。

- [Commit Message 说明](gov/spec-commit-message-001.md)

### legacy

删除前的缓存区。这里的文件不作为当前规范使用，只保留历史、迁移和对照价值。

### source

来源、引用格式和资料类型相关规范。

- [Source Intake Fields 说明](source/spec-source-intake-fields-001.md)
- [Citation APA 7](source/spec-source-citation-apa7-001.md)
- [Citation Chicago 17](source/spec-source-citation-chicago17-001.md)
- [Citation GB/T 7714-2015](source/spec-source-citation-gbt7714-2015-001.md)
- [Citation MLA 9](source/spec-source-citation-mla9-001.md)

### spacetime

日期、时间和严格时间戳相关规范。

- [Date and Time Format Specification](spacetime/spec-datetime-format-001.md)
- [Datetime Evidence Specification](spacetime/spec-datetime-evidence-001.md)

### system

仓库结构和目录职责说明。

- [System Map](system/spec-system-map-001.md)

### ver

版本变化语义的预留目录。

- [Version Semantics](ver/spec-version-semantics-001.md)

---

## 整理规则

```text
正式说明    → 放在对应目录
枚举和速查  → 放在 appendix
旧文件      → 放在 legacy
归档规则    → 放在 archive
```

新规范先放到职责清楚的位置。旧文件不用马上删除，先移入 `legacy/` 保留对照。

---

## 备注

- 本仓库仍在整理中。
- README 只列当前主要入口。
- `legacy/` 里的文件不代表当前规范。
