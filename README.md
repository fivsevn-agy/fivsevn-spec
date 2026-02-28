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
# fivsevn-spec

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

- [`元数据模版`](gov/gov-meta-frontmatter.md) 
- [`元数据枚举规范`](gov/gov-meta-enums.md)
- [`commit提交规范`](gov/gov-commit-message.md) 


### ver

> ⭕️ 变化的语义。区分“更新、修订、重写”。  
> ❌ ~~具体写了什么~~

- [`xxx`](xxx/xxx-xxx-xxx.md) 


### content

> ⭕️ 内容本身的组织方式。保证内容可解析、可迁移。  
> ❌ ~~观点质量与深度~~

- [`正文前置元信息规范`](content/content-frontmatter.md)
- [`正文规范`](content/content-body.md)
- [`正文后置信息规范`](content/content-backmatter.md)


### source

> ⭕️ 信息来源与证据。明确可信度。  
> ❌ ~~写作风格~~

- [`新闻聚合工具（News Aggregators）`](source/source-news-aggregators.md)
- [`主流媒体（Mainstream Media）`](source/source-mainstream-media.md)
- [`科学与研究（Science）`](source/source-science.md)
- [`人文学科（Humanities）`](source/source-humanities.md)
- [`HAM资源汇总`](source/source-ham-ecosystem.md)
- [`参考来源暂存`](source/source-reference-pool.md)
- [`引用规范（APA 7）`](source/source-citation-apa7.md)
- [`引用规范（MLA 9）`](source/source-citation-mla9.md)
- [`引用规范（Chicago 17）`](source/source-citation-chicago17.md)
- [`引用规范（GB/T 7714-2015）`](source/source-citation-gbt7714-2015.md)
- [`使用手册（Manual）`](source/source-manual.md)


### spacetime

> ⭕️ 时间、地点、语境。防止语义随时间失真。  
> ❌ ~~事件本身对错~~

- [`日期与时间书写规范`](spacetime/spacetime-datetime-format.md)
- [`时间戳的证据与严格使用规范`](spacetime/spacetime-datetime-evidence.md)


### archive

> ⭕️ 长期保存与可追溯性。保证未来仍可访问与理解。  
> ❌ ~~当前展示效果~~

- [`xxx`](xxx/xxx-xxx-xxx.md) 


### appendix

> ⭕️ 示例与说明。可以用来辅助理解规则。  
> ❌ ~~约束性规则~~

- [`commit示例`](appendix/appendix-commit-message-examples.md) 


