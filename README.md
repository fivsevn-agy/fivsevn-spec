# fivsevn-spec

This repository defines the normative specifications governing content production, versioning, provenance, spacetime semantics, and archival practices within the fivsevn ecosystem.

---
## repository structure-

```
fivsevn-spec/
│
├─ gov/  # 做事的流程和规则（怎么操作、先做什么、后做什么）
│  ├─ gov-commit-message.md          # 每次提交代码或文件时，说明文字该怎么写
│  │                                  （程序员常说：commit message 规范）
│  ├─ gov-branch-strategy.md         # 不同分支是干嘛用的，什么时候该用哪一个
│  │                                  （branch strategy）
│  ├─ gov-pull-request.md            # 什么时候需要提 PR，以及 PR 是用来干什么的
│  ├─ gov-review-process.md          # 别人要不要看、怎么看你的修改，哪些情况可以不看
│  ├─ gov-content-lifecycle.md       # 一篇内容从草稿到发布，再到封存的完整过程
│  └─ gov-experimental-work.md       # 试验、尝试、未定型内容放在哪里才不影响整体
│
├─ ver/  # 什么情况算“改了”，改了代表什么
│  ├─ ver-spec-versioning.md         # 这些规范文件本身，版本号应该怎么变
│  │                                  （spec versioning）
│  ├─ ver-content-versioning.md      # 内容版本如何区分新旧，而不是只看时间
│  ├─ ver-change-levels.md           # 小改、大改、重写，分别算哪一种变化
│  ├─ ver-updated-vs-rewritten.md    # 是在原文基础上修改，还是等于重新写了一篇
│  └─ ver-deprecation.md             # 什么时候一条规则或内容可以被正式弃用
│
├─ content/  # 内容本身应该长什么样
│  ├─ content-frontmatter.md         # 标题、时间、状态这些“头部信息”要写哪些
│  │                                  （frontmatter 结构）
│  ├─ content-body-structure.md      # 正文各个部分大致怎么分、怎么排列
│  ├─ content-section-semantics.md   # 每个部分存在的意义是什么，不是随便分的
│  │                                  （section semantics）
│  ├─ content-multilang.md           # 同一内容有多种语言时，应该怎么标记和组织
│  └─ content-metadata-optional.md   # 可以有、但不是必须的附加信息说明
│
├─ source/  # 信息从哪里来，能不能信
│  ├─ source-classification.md       # 不同类型资料怎么区分，比如原始资料和转述资料
│  ├─ source-citation-rules.md       # 引用别人的内容时，应该怎么标明来源
│  ├─ source-primary-vs-secondary.md # 什么时候必须用一手资料，什么时候二手可以
│  ├─ source-uncertainty-and-disclaimer.md
│  │                                  # 信息不确定时，应该如何说明、不该怎么说
│  └─ source-link-rot-and-loss.md    # 链接失效、网页消失后该如何处理
│
├─ spacetime/  # 时间、地点和当时的背景
│  ├─ spacetime-datetime-format.md   # 时间写成什么格式，精确到哪一步
│  │                                  （datetime format）
│  ├─ spacetime-timezone.md          # 时间到底是哪个时区的，默认按什么算
│  ├─ spacetime-event-time.md        # 这里的时间指事情发生的时间，而不是写文章的时间
│  ├─ spacetime-writing-vs-publish.md
│  │                                  # 写作时间、发布时间、记录时间分别代表什么
│  ├─ spacetime-context-validity.md  # 某个判断在什么背景下成立，过了多久可能失效
│  └─ spacetime-retroactive-edit.md  # 事后回头修改旧内容时，允许改到什么程度
│
├─ archive/  # 内容如何长期保存、不被搞丢
│  ├─ archive-backup-policy.md       # 内容要不要备份，多久备份一次，放在哪里
│  ├─ archive-archival-criteria.md   # 什么情况下，一篇内容应该被封存起来
│  ├─ archive-status-archive.md      # 被标记为 archive 后，这篇内容意味着什么
│  ├─ archive-permalink-policy.md    # 固定链接要不要保证长期可用
│  ├─ archive-original-url.md        # 原始出处链接在什么情况下需要保留
│  └─ archive-format-migration.md    # 将来换平台或格式时，内容怎么迁移
│
├─ appendix/  # 示例和补充说明（只用来帮助理解）
│  ├─ appendix-commit-examples.md    # 提交说明的实际示例
│  ├─ appendix-frontmatter-examples.md
│  │                                  # frontmatter 的完整示例
│  ├─ appendix-content-examples.md   # 一整篇内容的示例结构
│  ├─ appendix-migration-notes.md    # 过去调整、迁移时发生过什么
│  └─ appendix-design-rationale.md   # 当初为什么要这样定规则的解释
│
└─ README.md  # 整个规范是干什么的，从这里开始看
```

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


