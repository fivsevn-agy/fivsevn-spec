# Source Intake 枚举表

本文列出 `intake` 来源条目中常用的枚举值。

字段说明见：

    source/spec-source-intake-fields-001.md

实际来源列表维护在：

    fivsevn-devlog/intake/sources.md

---

## 1. `source_type`

`source_type` 表示来源类型。

```yaml
source_type:
  - wire_service
  - public_broadcaster
  - newspaper_magazine
  - institutional
  - journal
  - specialist_media
  - trade_publication
  - culture_magazine
  - reference_tool
  - aggregator
  - community
  - personal_site
  - data_source
```

| value | meaning |
|---|---|
| `wire_service` | 通讯社或新闻社 |
| `public_broadcaster` | 公共广播或公共媒体 |
| `newspaper_magazine` | 综合报纸、杂志或新闻网站 |
| `institutional` | 政府、国际组织、大学、博物馆、实验室或官方机构 |
| `journal` | 学术期刊或期刊平台 |
| `specialist_media` | 专业领域媒体 |
| `trade_publication` | 行业或职业出版物 |
| `culture_magazine` | 文化、思想、评论或长文杂志 |
| `reference_tool` | 查询工具、数据库、索引、目录或参考入口 |
| `aggregator` | 聚合器或发现工具 |
| `community` | 社区、论坛或讨论空间 |
| `personal_site` | 个人网站、博客或独立作者站点 |
| `data_source` | 数据集、统计来源、仪表盘或结构化数据源 |

---

## 2. `authority_level`

`authority_level` 表示来源接近一手信息的程度。

```yaml
authority_level:
  - primary
  - specialist
  - generalist
  - aggregator
  - commentary
  - community
```

| value | meaning |
|---|---|
| `primary` | 一手、官方或原始来源 |
| `specialist` | 专业领域来源 |
| `generalist` | 综合媒体或综合参考来源 |
| `aggregator` | 聚合、索引或转入口 |
| `commentary` | 评论、解释、批评或观点来源 |
| `community` | 社区或用户生成来源 |

---

## 3. `reliability_score`

`reliability_score` 表示事实可靠性评分。

```yaml
reliability_score:
  - 5
  - 4
  - 3
  - 2
  - 1
```

| value | meaning |
|---|---|
| `5` | 高可靠；官方、一手、学术或强编辑来源 |
| `4` | 通常可靠；有清楚编辑、机构或专业责任 |
| `3` | 有用但需要交叉核对 |
| `2` | 可靠性较弱或不稳定 |
| `1` | 通常不适合作为事实来源，只适合观察话语本身 |

---

## 4. `professional_value`

`professional_value` 表示来源在所属 section 中的专业价值。

```yaml
professional_value:
  - 5
  - 4
  - 3
  - 2
  - 1
```

| value | meaning |
|---|---|
| `5` | 该 section 的核心来源 |
| `4` | 强支持来源 |
| `3` | 有用但不是核心 |
| `2` | 偶尔有价值 |
| `1` | 价值较低 |

---

## 5. `use_role`

`use_role` 表示来源在 intake 页面中的用途。

```yaml
use_role:
  - baseline
  - signal
  - reference
  - counterpoint
  - culture_probe
  - archive
  - tool
```

| value | meaning |
|---|---|
| `baseline` | 日常基础来源 |
| `signal` | 早期信号或专业信号来源 |
| `reference` | 查询、索引或参考入口 |
| `counterpoint` | 对照视角或交叉检查来源 |
| `culture_probe` | 文化、审美或思想感知来源 |
| `archive` | 档案、语料库或历史参考 |
| `tool` | 工具性来源 |

---

## 6. 常用组合

### 一手机构来源

```yaml
source_type: institutional
authority_level: primary
reliability_score: 5
professional_value: 4
use_role: baseline
```

### 专业媒体来源

```yaml
source_type: specialist_media
authority_level: specialist
reliability_score: 4
professional_value: 5
use_role: signal
```

### 综合新闻来源

```yaml
source_type: newspaper_magazine
authority_level: generalist
reliability_score: 4
professional_value: 4
use_role: baseline
```

### 参考工具来源

```yaml
source_type: reference_tool
authority_level: aggregator
reliability_score: 3
professional_value: 4
use_role: reference
```

### 学术期刊来源

```yaml
source_type: journal
authority_level: primary
reliability_score: 5
professional_value: 5
use_role: reference
```
