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
# fivsevn-spec（⚠️ 施工中）

- This repository defines the normative specifications governing content production, versioning, provenance, spacetime semantics, and archival practices within the fivsevn ecosystem.

---
## repository structure

```
fivsevn-spec/
├─ gov/  
├─ ver/
├─ content/
├─ source/
├─ spacetime/
├─ archive/
├─ appendix/
└─ README.md
```

---
## index

### gov

> ⭕️ 做事时需要遵循的流程和规则。保证行为一致、过程可复现。  
> ❌ ~~内容本身的表达~~

- [`commit提交规范`](legacy/legacy-spec-gov-commit-message-001.md) 


### ver

> ⭕️ 变化的语义。区分“更新、修订、重写”。  
> ❌ ~~具体写了什么~~

- [`xxx`](xxx/xxx-xxx-xxx.md) 


### content（施工中）

> ⭕️ 内容本身的组织方式。保证内容可解析、可迁移。  
> ❌ ~~观点质量与深度~~

- [`元数据模版`](content/spec-content-meta-frontmatter-001.md) 
- [`元数据枚举规范`](content/spec-content-meta-enums-001.md)

- [`正文前置元信息规范`](content/spec-content-frontmatter-001.md)
- [`正文规范`](content/content-body.md)
- [`正文后置信息规范`](content/content-backmatter.md)


### source

> ⭕️ 信息来源与证据。明确可信度。  
> ❌ ~~写作风格~~

- [`新闻聚合工具（News Aggregators）`](source/spec-source-news-aggregators-001.md)
- [`主流媒体（Mainstream Media）`](source/spec-source-mainstream-media-001.md)
- [`科学与研究（Science）`](source/spec-source-science-001.md)
- [`人文学科（Humanities）`](source/spec-source-humanities-001.md)
- [`HAM资源汇总`](source/spec-source-ham-ecosystem-001.md)
- [`参考来源暂存`](source/spec-source-reference-pool-001.md)
- [`引用规范（APA 7）`](source/spec-source-citation-apa7-001.md)
- [`引用规范（MLA 9）`](source/spec-source-citation-mla9-001.md)
- [`引用规范（Chicago 17）`](source/spec-source-citation-chicago17-001.md)
- [`引用规范（GB/T 7714-2015）`](source/spec-source-citation-gbt7714-2015-001.md)
- [`使用手册（Manual）`](source/spec-source-manual-001.md)


### spacetime

> ⭕️ 时间、地点、语境。防止语义随时间失真。  
> ❌ ~~事件本身对错~~

- [`日期与时间书写规范`](legacy/legacy-spec-datetime-format-001.md)
- [`时间戳的证据与严格使用规范`](legacy/legacy-spec-datetime-evidence-001.md)


### archive

> ⭕️ 长期保存与可追溯性。保证未来仍可访问与理解。  
> ❌ ~~当前展示效果~~

- [`xxx`](xxx/xxx-xxx-xxx.md) 


### appendix

> ⭕️ 示例与说明。可以用来辅助理解规则。  
> ❌ ~~约束性规则~~

- [`commit示例`](legacy/legacy-spec-gov-commit-message-examples-001.md) 

