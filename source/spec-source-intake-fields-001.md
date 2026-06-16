# Source Intake Fields 说明

本文定义 `intake` 来源条目的字段结构。

具体来源列表维护在：

    fivsevn-devlog/intake/sources.md

本文只说明字段意义。字段可使用的枚举值，另见：

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
