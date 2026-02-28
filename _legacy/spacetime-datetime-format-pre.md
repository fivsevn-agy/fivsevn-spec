---
id: module-submodule-topic-001   # 全仓唯一主键，不随文件名变化

title: 标题                         # 给人读的标题

module: module-name               # 一级模块（natsci / netcom / posts / blogops / system / narrative）
submodule: submodule-name         # 二级分类（如 rf / lora / taxonomy）
topic: specific-topic             # 具体对象或主题（如 meshtastic / coleoptera）

type: note                        # 内容类型（note / article / index / log / spec / release 等）
status: active                    # 当前状态（draft / active / archived）
canonical: true                   # 是否权威版本

summary: >                        # 1–2 句摘要，供 AI 快速扫描
  简要说明这篇内容解决什么问题。

parents: []                       # 上级节点（通常只 1 个 index）
related: []                       # 相关内容 id 列表

tags: []                          # 关键词标签（3–8 个为宜）

audience: [self]                  # 目标读者（self / public / tutorial / collaborator）
languages: [zh]                   # 内容语言（zh / en / jp 等）

maturity: evolving                # 认知成熟度（draft / evolving / stable / deprecated）
confidence: 0.70                  # 主观确定度（0–1）

visibility: public                # 可见性（public / private）
source_of_truth: devlog           # 权威来源（devlog / site / other）

created: 2026-01-01               # 创建日期（YYYY-MM-DD）
updated: 2026-01-01               # 最近修改日期
---
> Status: legacy  
> Validity: expired  
> Replaced by: [spacetime-datetime-format.md](../spacetime/system-spec-datetime-format-001.md) & [spacetime-datetime-evidence.md](../spacetime/system-spec-datetime-evidence-001.md) 
> Note: retained for historical reference only

---

# 日期与时间格式说明标准（Date & Time Format Specification）

为确保文档、文件、接口等系统中的时间信息统一、清晰且具可读性，特制定如下日期与时间格式标准说明，涵盖年月日的常见格式、用途建议、示例参考等内容。

---

## 一、基本格式定义

| 标记        | 含义             | 范围或说明       | 示例     |
|-------------|------------------|------------------|----------|
| `YYYY`      | 年（四位）       | 0000–9999        | `2025`   |
| `MM`        | 月（两位）       | 01–12            | `04`     |
| `DD`        | 日（两位）       | 01–31            | `09`     |
| `HH`        | 小时（24小时制） | 00–23            | `08`     |
| `mm`        | 分钟             | 00–59            | `05`     |
| `ss`        | 秒               | 00–59            | `32`     |

---

## 二、推荐格式组合与说明

| 格式样式             | 示例               | 推荐用途                             |
|----------------------|--------------------|--------------------------------------|
| `YYYY`               | `2025`             | 仅表示年份，如报告标题年份等         |
| `YYYYMM`             | `202504`           | 用于文件夹/归档命名，便于排序        |
| `YYYY-MM`            | `2025-04`          | 显示用年月格式，较友好               |
| `YYYYMMDD`           | `20250409`         | 用于文件名、日志、排序               |
| `YYYY-MM-DD`         | `2025-04-09`       | 页面展示、接口文档字段标准           |
| `YYYY-MM-DD HH:mm`   | `2025-04-09 08:05` | 简洁的时间戳，日志中常用             |
| `YYYY-MM-DD HH:mm:ss`| `2025-04-09 08:05:32` | 精确时间戳，用于日志、数据库记录 |
| `Y-m-d\TH:i:sP`（PHP 格式） | `2025-04-09T03:31:31+08:00` | PHP 中生成 ISO 8601 标准时间戳（含时区）的格式化写法 |

---

## 三、用途建议

| 使用场景           | 推荐格式               | 示例                 | 理由说明                       |
|--------------------|------------------------|----------------------|--------------------------------|
| **文件夹命名**     | `YYYYMM`               | `202504`             | 简洁、可按时间自动排序         |
| **文件名嵌入时间** | `YYYYMMDD`             | `post-20250409.md`   | 精确到日，避免重复             |
| **日志文件记录**   | `YYYY-MM-DD HH:mm:ss`  | `2025-04-09 08:05:32`| 精确定位问题                   |
| **页面显示/文档**  | `YYYY-MM-DD`           | `2025-04-09`         | 国际标准，用户友好             |
| **数据库时间字段** | `DATE` / `DATETIME`    | -                    | 支持查询、排序、索引           |
| **API 接口字段**   | `YYYY-MM-DD` 或 ISO 8601 | `2025-04-09T08:05:32Z` | 保证时区、格式一致性           |

---

## 四、书写规范建议

- 所有年月日格式应统一为 ISO 标准（`YYYY-MM-DD`）。
- 文件系统中建议使用无分隔符格式（如 `YYYYMMDD`）以方便排序与命名。
- 命名中嵌入时间建议放在开头或末尾，并使用中划线分隔，如：`log-20250409.md`。
- 如需带时间戳的文件名，应统一格式如：`log-20250409-080532.txt`。
- 避免使用不明确的缩写格式如 `YYMMDD`，防止年份混淆。

---

## 五、特殊格式说明（如需）

| 格式                 | 用途                 | 示例                        |
|----------------------|----------------------|-----------------------------|
| `YYYY/`              | 年份目录             | `2025/`                     |
| `YYYY/MM/`           | 年月层级目录         | `2025/04/`                  |
| `YYYY-MM-DD.md`      | 每日日志文件         | `2025-04-09.md`             |
| `YYYYMMDD_HHmmss`    | 精确时间文件命名     | `20250409_080532.log`       |
| `2025年4月9日`       | 中文日期显示         | 页面展示、用户界面          |

---

如需与时间有关的字段统一命名规范，可根据此模板做项目级调整。推荐在 README 或 CONTRIBUTING 文档中说明此规范，以便团队协作保持一致。