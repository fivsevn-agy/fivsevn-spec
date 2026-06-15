# fivsevn-spec

fivsevn-spec 用来保存 fivsevn 体系中的基础规范，包括内容组织、提交信息、来源引用、时间写法、旧文件处理和版本语义等规则。

这个仓库不保存具体内容本身，只说明内容和相关文件应该怎样组织、维护和引用。

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

辅助材料。主要放枚举表、速查表和示例。

- [Commit Message 枚举表](appendix/spec-commit-message-enums-001.md)
- [Content Frontmatter 枚举表](appendix/spec-content-frontmatter-enums-001.md)
- [Content Frontmatter 枚举速查](appendix/spec-content-frontmatter-enums-quickref-001.md)

---

### archive

旧文件和归档的处理规则。

- [Archive and Legacy Policy](archive/spec-archive-policy-001.md)

---

### content

内容文件的组织规则。

- [Content Frontmatter 说明](content/spec-content-frontmatter-001.md)
- [Content Translation Specification 翻译内容规范](content/spec-content-translation-001.md)

---

### gov

做事时使用的规则。当前主要是 commit message。

- [Commit Message 说明](gov/spec-commit-message-001.md)

---

### legacy

旧文件存放区。

这里的文件已经不作为当前规范使用，只保留历史、迁移和对照价值。旧文件移入时，直接在原文件名前加 `legacy-`。

```text
spec-example-001.md
→ legacy-spec-example-001.md
```

---

### source

来源、引用格式和资料类型相关规范。  
这一部分暂时保留现状，后续再单独整理。

- [Citation APA 7](source/spec-source-citation-apa7-001.md)
- [Citation Chicago 17](source/spec-source-citation-chicago17-001.md)
- [Citation GB/T 7714-2015](source/spec-source-citation-gbt7714-2015-001.md)
- [Citation MLA 9](source/spec-source-citation-mla9-001.md)
- [HAM Ecosystem](source/spec-source-ham-ecosystem-001.md)
- [Humanities Sources](source/spec-source-humanities-001.md)
- [Mainstream Media Sources](source/spec-source-mainstream-media-001.md)
- [Source Manual](source/spec-source-manual-001.md)
- [News Aggregators](source/spec-source-news-aggregators-001.md)
- [Reference Pool](source/spec-source-reference-pool-001.md)
- [Science Sources](source/spec-source-science-001.md)

---

### spacetime

日期、时间和严格时间戳相关规范。

- [Date and Time Format Specification](spacetime/spec-datetime-format-001.md)
- [Datetime Evidence Specification](spacetime/spec-datetime-evidence-001.md)

---

### system

仓库结构和目录职责说明。

- [System Map](system/spec-system-map-001.md)

---

### ver

版本变化语义的预留目录。当前只保留轻量说明。

- [Version Semantics](ver/spec-version-semantics-001.md)

---

## 当前整理方式

目前采用一个简单规则：

```text
正式说明    → 放在对应目录
枚举和速查  → 放在 appendix
旧文件      → 放在 legacy
归档规则    → 放在 archive
```

这样做是为了减轻迭代压力。  
新规范可以先放到清楚的位置；旧文件不用马上删除，先移入 `legacy/` 保留对照；辅助材料也不和正文规范混在一起。

---

## 备注

- 本仓库仍在整理中。
- README 只列当前主要入口。
- `legacy/` 里的文件不代表当前规范。
- `source/` 暂时不做大改。
