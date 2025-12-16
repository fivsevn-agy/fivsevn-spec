# fivsevn-spec

- This repository defines the normative specifications governing content production, versioning, provenance, spacetime semantics, and archival practices within the fivsevn ecosystem.


---
## repository structure-

```
fivsevn-spec/
│
├─ gov/  # 做事时需要遵循的流程和规则
│  ├─ gov-commit-message.md          # 每次提交改动时，用一句话说明这次改动在做什么
│  │                                  （commit message convention）
│  ├─ gov-branch-strategy.md         # 不同分支各自用来做什么，以及在什么情况下使用
│  │                                  （branch strategy）
│  ├─ gov-pull-request.md            # 在什么情况下需要通过 PR 来合并修改
│  ├─ gov-review-process.md          # 修改是否需要他人查看，以及查看时关注什么
│  ├─ gov-content-lifecycle.md       # 一篇内容从开始撰写到正式封存的整个过程
│  └─ gov-experimental-work.md       # 尚未定型的尝试性内容应如何存放，避免影响正式内容
│
├─ ver/  # 与“变化”相关的规则说明
│  ├─ ver-spec-versioning.md         # 规范文件本身在什么情况下需要更新版本号
│  │                                  （spec versioning）
│  ├─ ver-content-versioning.md      # 内容发生变化时，如何区分新旧版本
│  ├─ ver-change-levels.md           # 不同程度的修改分别应当如何理解和标记
│  ├─ ver-updated-vs-rewritten.md    # 是在原内容基础上修订，还是等同于重新写了一份
│  └─ ver-deprecation.md             # 什么时候可以明确标记某条规则或内容不再适用
│
├─ content/  # 内容本身的组织方式
│  ├─ content-frontmatter.md         # 标题、时间、状态等基础信息应如何填写
│  │                                  （frontmatter structure）
│  ├─ content-body-structure.md      # 正文内容在整体上应如何分段和排列
│  ├─ content-section-semantics.md   # 各个内容部分分别承担什么作用
│  │                                  （section semantics）
│  ├─ content-multilang.md           # 同一内容以多种语言呈现时的组织方式
│  └─ content-metadata-optional.md   # 可选但不强制的补充信息说明
│
├─ source/  # 内容所依据的信息来源
│  ├─ source-classification.md       # 不同类型的信息来源应如何区分
│  ├─ source-citation-rules.md       # 引用外部资料时应如何标明出处
│  ├─ source-primary-vs-secondary.md # 在什么情况下需要直接使用原始资料
│  ├─ source-uncertainty-and-disclaimer.md
│  │                                  # 信息存在不确定性时应如何说明
│  └─ source-link-rot-and-loss.md    # 当引用链接失效或来源消失时的处理方式
│
├─ spacetime/  # 与时间和背景相关的说明
│  ├─ spacetime-datetime-format.md   # 时间信息应采用什么格式，以及精确到什么程度
│  │                                  （datetime format）
│  ├─ spacetime-timezone.md          # 时间所对应的时区应如何理解和标注
│  ├─ spacetime-event-time.md        # 这里记录的时间指的是事件发生的时间
│  ├─ spacetime-writing-vs-publish.md
│  │                                  # 写作时间、发布时间与记录时间之间的区别
│  ├─ spacetime-context-validity.md  # 某些判断在特定背景下成立的时间范围
│  └─ spacetime-retroactive-edit.md  # 对历史内容进行事后修改时应遵循的边界
│
├─ archive/  # 与长期保存相关的规则
│  ├─ archive-backup-policy.md       # 是否需要备份，以及备份的方式和频率
│  ├─ archive-archival-criteria.md   # 在什么情况下内容应当进入封存状态
│  ├─ archive-status-archive.md      # 被标记为 archive 后，这篇内容应如何被理解
│  ├─ archive-permalink-policy.md    # 是否需要为内容提供长期有效的访问地址
│  ├─ archive-original-url.md        # 是否保留原始出处链接，以及保留的意义
│  └─ archive-format-migration.md    # 当平台或格式变化时，内容如何迁移
│
├─ appendix/  # 用于理解规范的示例和补充说明
│  ├─ appendix-commit-examples.md    # 各类提交说明的实际写法示例
│  ├─ appendix-frontmatter-examples.md
│  │                                  # frontmatter 的完整填写示例
│  ├─ appendix-content-examples.md   # 一整篇内容从头到尾的结构示例
│  ├─ appendix-migration-notes.md    # 过去规则或结构调整时的记录说明
│  └─ appendix-design-rationale.md   # 这些规则背后的设计考虑
│
└─ README.md  # 本仓库的整体说明与阅读入口
```


---
## index

### gov

- [`commit提交规范`](gov/gov-commit-message.md) 
- gov-branch-strategy.md
- gov-pull-request.md
- gov-review-process.md
- gov-content-lifecycle.md
- gov-experimental-work.md


### ver

- ver-spec-versioning.md
- ver-content-versioning.md
- ver-change-levels.md
- ver-updated-vs-rewritten.md
- ver-deprecation.md


### content

- [`正文前置元信息规范`](content/content-frontmatter.md)
- [`正文规范`](content/content-body.md)
- [`正文后置信息规范`](content/content-backmatter.md)
- content-section-semantics.md
- content-multilang.md
- content-metadata-optional.md


### source

- source-classification.md
- source-citation-rules.md
- source-primary-vs-secondary.md
- source-uncertainty-and-disclaimer.md
- source-link-rot-and-loss.md
- [`引用规范（APA 7）`](source/source-citation-apa7.md)
- [`引用规范（MLA 9）`](source/source-citation-mla9.md)
- [`引用规范（Chicago 17）`](source/source-citation-chicago17.md)
- [`引用规范（GB/T 7714-2015）`](source/source-citation-gbt7714-2015.md)
- [`HAM资源汇总`](source/source-ham-ecosystem.md)
- [`参考来源暂存`](source/source-reference-pool.md)

### spacetime

- [`日期与时间书写规范`](spacetime/spacetime-datetime-format.md)
- [`时间戳的证据与严格使用规范`](spacetime/spacetime-datetime-evidence.md)
- spacetime-timezone.md
- spacetime-event-time.md
- spacetime-writing-vs-publish.md
- spacetime-context-validity.md
- spacetime-retroactive-edit.md


### archive

- archive-backup-policy.md
- archive-archival-criteria.md
- archive-status-archive.md
- archive-permalink-policy.md
- archive-original-url.md
- archive-format-migration.md


### appendix

- [`commit示例`](appendix/appendix-commit-message-examples.md) 
- appendix-frontmatter-examples.md
- appendix-content-examples.md
- appendix-migration-notes.md
- appendix-design-rationale.md


---
## note

### 1. Governance & Workflow Spec

- ⭕️协作与操作流程
- ❌~~内容本身的表达~~
- 目的：保证行为一致、过程可复现

```
e.g.
commit message 规则
branch / PR 约定
draft → published → archive 流程
```
  
### 2. Versioning & Change Spec

- ⭕️变化的语义
- ❌~~具体写了什么~~
- 目的：区分“更新、修订、重写”

``` 
spec 版本号
content 的 updated 规则
变更级别划分
```

### 3. Content Representation Spec

- ⭕️内容的数据结构
- ❌~~观点质量与深度~~
- 目的：保证内容可解析、可迁移

```
frontmatter 字段
正文结构
多语言标记
```

### 4. Source & Reference Spec

- ⭕️信息来源与证据
- ❌~~写作风格~~
- 目的：明确可信度与引用边界

``` 
来源分类
引用规则
不确定性标注
```

### 5. Spacetime & Context Spec

- ⭕️时间、地点、语境
- ❌~~事件本身对错~~
- 目的：防止语义随时间失真

``` 
时间戳格式
时区
事件时间 / 写作时间 / 发布时间区分
语境有效期
```

### 6. Preservation & Archival Spec

- ⭕️长期保存与可追溯性
- ❌~~当前展示效果~~
- 目的：保证未来仍可访问与理解

```
备份规则
archive 条件
permalink / original_url
```

### 7. Appendix (Informative)

- ⭕️示例与说明
- ❌~~约束性规则~~
- 目的：辅助理解，不产生规范

``` 
templates
examples
non-normative notes
```


