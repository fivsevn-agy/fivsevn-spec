---
id: "spec-source-intake-fields-001"
title: "Source Intake Fields 说明"

module: "spec"
submodule: "source"
topic: "spec-source-intake-fields-001"

type: "spec"
status: "active"
canonical: true

summary: "说明Source Intake Fields 说明。"

parents: []
related: []

tags: []

audience: ["self", "internal"]
languages: ["zh"]

maturity: "evolving"
confidence: null

visibility: "public"
source_of_truth: "spec"

note: "未记录原始写作日期；created 为本路径首次 Git 记录日期，无法合理确定时留空。"

created: "2026-06-16"
updated: "2026-10-30"
metadata_updated: "2026-10-30"
---
# Source Intake Fields 说明

本文定义 `intake` 来源条目的字段结构。

具体来源列表维护在：

    fivsevn-devlog/intake/sources.md

本文说明字段意义、来源评估与证据维护规则。字段可使用的枚举值，另见：

    appendix/spec-source-intake-enums-001.md

---

## 1. 标准样本

```yaml
name: Example Source
section: example_section
feed_url: https://example.com/feed.xml
source_cap: 6
site_url: https://example.com/
source_type: specialist_media
authority_level: specialist
reliability_score: 4
professional_value: 4
use_role: baseline
```

---

## 2. 字段说明

### `name`

来源显示名称。

应使用人可以直接识别的名称，不必强行缩写。

示例：

```yaml
name: Example Source
```

---

### `section`

来源所属的二级目录。

该值应对应 `intake/sources.md` 中已有的 section。

示例：

```yaml
section: science_news
```

---

### `feed_url`

RSS 或 Atom 地址。

如果来源有可用 feed，填写完整 URL：

```yaml
feed_url: https://example.com/feed.xml
```

如果没有可用 feed，保留为空字符串：

```yaml
feed_url: ''
```

---

### `source_cap`

该来源每次最多抓取多少条 RSS 内容。

有 feed 的来源通常使用正整数：

```yaml
source_cap: 6
```

没有 feed、只作为网站入口展示的来源使用：

```yaml
source_cap: 0
```

`source_cap` 是逐来源控制字段。不使用全局抓取数量，也不使用 section 级抓取数量。

---

### `site_url`

来源主页或栏目入口。

当 `feed_url` 为空、feed 抓取失败、或返回结果为空时，页面使用 `site_url` 作为网站入口。

示例：

```yaml
site_url: https://example.com/
```

---

### `source_type`

来源类型。

示例：

```yaml
source_type: specialist_media
```

具体枚举见：

    appendix/spec-source-intake-enums-001.md

---

### `authority_level`

来源接近一手信息的程度。

示例：

```yaml
authority_level: specialist
```

具体枚举见：

    appendix/spec-source-intake-enums-001.md

---

### `reliability_score`

事实可靠性评分。

取值为 `1` 到 `5`。

示例：

```yaml
reliability_score: 4
```

分数越高，表示事实可靠性越高。

---

### `professional_value`

该来源在所属 section 中的专业价值评分。

取值为 `1` 到 `5`。

示例：

```yaml
professional_value: 4
```

分数越高，表示对该 section 越有用。

---

### `use_role`

来源在 intake 页面中的使用角色。

示例：

```yaml
use_role: baseline
```

具体枚举见：

    appendix/spec-source-intake-enums-001.md

---

## 3. 网站来源写法

如果来源没有可用 RSS，但仍有参考价值，可以保留为网站来源。

```yaml
name: Example Website
section: example_section
feed_url: ''
source_cap: 0
site_url: https://example.com/
source_type: reference_tool
authority_level: aggregator
reliability_score: 3
professional_value: 4
use_role: reference
```

这种来源不抓取 RSS，只在页面中展示网站入口。

---

## 4. 维护关系

    source/spec-source-intake-fields-001.md
    → 说明字段意义

    appendix/spec-source-intake-enums-001.md
    → 维护字段枚举

    fivsevn-devlog/intake/sources.md
    → 维护实际来源列表

`fivsevn-spec` 保存稳定规则。

`fivsevn-devlog/intake/sources.md` 保存当前选取结果。


## 5. 收录与获取边界

先判断来源是否值得收录，再判断可用的获取渠道。优先使用来源允许的 RSS、Atom 或 API；网页提取须另外核实条款、访问规则和内容使用范围。公开可访问不等于可任意复制。不要绕过登录、付费墙或访问限制。

无 feed、需要未配置的 API 密钥、禁止采集、临时失败或返回空结果，都不构成删除优质网址或降低 R/P 的理由。保留 `site_url`；`source_cap: 0` 只禁用采集，不禁用网址。API 地址不能冒充 RSS 填入 `feed_url`，须先实现并验证对应适配器。

`manual` 包括用户拥有设备的电子说明书，必须保留此类型及现有设备手册入口。型号、版本、语言和官方发布主体是核验重点，不以是否可抓取文章判断价值。

分类保持两级：一级覆盖广泛领域，二级满足实际检索用途。优先复用已有二级分类，跨分类收录允许，不为单个来源增设过细分类。

## 6. R 与 P 的评估方法

R 是**所述适用范围内事实陈述的可信程度**；P 是**该来源在当前 section 中的专业用途**。两者独立判断，不取平均，不因来源名气、流量、语言、视觉包装、是否免费、能否抓取或与自身观点一致而自动加减分。

评估顺序：

1. 核实机构/作者身份、具体栏目、原始材料与转载关系；同一域名不必然是同一来源。
2. 写明适用领域和产出种类。新闻、研究、观点、社区回答、工具和手册分别评价。
3. 查验责任主体、编辑或同行评审过程、引用/数据/方法可追溯性、公开更正机制、资金与利益关系。能取得时抽查代表性产出；不能取得时明确缺口。
4. 按下列锚点给 R，并记录支持和限制；按分类需求给 P，说明补足什么知识或工具用途。
5. 同一具体来源跨分类比对身份和 R。若 R 不同，逐项给出领域/栏目差异与证据；P 和 use_role 可因用途不同而变化。检查只能提示冲突，不能自动统一分数。

| R | 判断锚点 |
|---|---|
| 5 | 在明确领域内，责任、方法或原始材料、审查/纠错机制均有充分可查证据，并有产出核验支持；不等于零错误。 |
| 4 | 责任主体和专业审查/编辑流程清楚，事实或原始记录可追溯；仍需核对具体主张及边界。 |
| 3 | 有可用信息，但审查、方法、纠错或出处不均，使用事实需交叉核验。 |
| 2 | 已有证据表明事实质量明显不稳、出处薄弱或错误处理不足；应写明证据。 |
| 1 | 已有证据表明通常不适合作事实依据；可因话语观察价值保留，须说明用途。 |

证据不足是“待复核”，不是 R1/R2，也不应为了填齐字段默认给 R5。既有来源保留历史评分并标记未复核；新来源先完成有范围、有依据的评估。只核实身份时用 `partial`，不宣称完成评分复核。

| P | 判断锚点 |
|---|---|
| 5 | 当前分类中具有不可轻易替代的核心资料、深度方法或持续专业产出；说明核心用途。 |
| 4 | 对当前分类提供强支持、重要补充或直接可用的专业工具。 |
| 3 | 有明确用途，但深度、覆盖或适配度有限。 |
| 2 | 偶发相关，专业支撑较弱。 |
| 1 | 当前分类用途很有限；重新核对分类与收录理由。 |

领域边界：学术期刊的同行评审不把每篇论文变成定论；预印本不等于已同行评审；官方机构对自有记录是一手来源，但宣传与政策主张仍需核验；观点和批评中的论证不按立场赞同程度打分；社区内容按具体作者、出处和治理机制评估；工具/素材库的 P 可高于事实可靠性 R；设备手册的高 R 仅覆盖对应型号、版本的官方操作说明。

## 7. 可选的说明与复核字段

新增来源及修改身份、评分时，应在原 `source` 块加入 `review`。既有条目逐步补充；缺失表示未按本标准复核，不表示质量低。为便于审查，`checked` 使用带引号的日期字符串。

```yaml
description: 简短、准确的来源用途说明；网址卡片可使用它作为摘要。
review:
  status: reviewed
  checked: '2026-10-30'
  scope: 本次评估适用的领域、栏目与内容种类
  identity: 来源身份和类型的依据
  reliability: R 分数的理由；变更时注明原值及变更原因
  professional_value: 当前 section 中 P 分数与用途的理由
  evidence:
    - https://example.com/about
    - https://example.com/editorial-policy
  limitations: 尚未核验的部分、利益关系和不适用范围
  access: 允许的获取方式、限制或仅保留网址的原因
```

`status` 为 `reviewed`（上述范围内完成本轮评估）或 `partial`（如只核实身份）。`reviewed` 不是对全部历史内容的保证。证据优先采用官方介绍、编辑/纠错政策、论文/数据及可定位的实际产出；自我宣传不能独立证明最高评级。记录核验日期，所有者、栏目、政策或内容质量发生变化时复核。

## 8. 生成数据的准确性

- 原文发布时间、更新时间、抓取时间和页面生成时间分开保存。Atom/RSS 的已解析日期优先，支持有时区的 ISO 8601 和 RFC 日期；无法确认发布时间时明确为未知，不能使用抓取时间替代。仅有更新时间不能冒充发布时间。
- 同篇文章以保守规范化 URL 识别，只移除已知跟踪参数；保留未知参数、内容 ID、版本、语言及片段，不以标题相同就合并。跨域转载没有明确证据不自动合并。
- 同分类重复条目合并时保留全部来源、原始链接与分类评分；跨分类归属继续可见。网址卡片和文章不得互相吞并。
- 标题与摘要使用同一文本清洗结果生成 HTML 和 LLM context；输出时分别正确转义，不二次破坏 URL 参数或实体。页面与 context 使用同一构建时刻和同一条目集合。
