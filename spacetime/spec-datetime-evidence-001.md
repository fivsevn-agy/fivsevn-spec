---
id: "spec-datetime-evidence-001"
title: "时间戳的证据与严格使用规范"

module: "spec"
submodule: "spacetime"
topic: "spec-datetime-evidence-001"

type: "spec"
status: "active"
canonical: true

summary: "说明时间戳的证据与严格使用规范。"

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

created: "2025-12-16"
updated: '2026-11-01'
metadata_updated: '2026-11-01'
---

# 时间证据

严格时间戳包含日期、时分秒和明确时区，例如 `2026-11-01T18:30:00+08:00`。记录发布时间、事件顺序和系统日志时，优先保存来源系统产生的原始值，并注明来源。

- 发布时间、更新时间、采集时间和构建时间分别记录，不能相互代替。
- 文件名、手填日期、EXIF、文件修改时间和 Git 首次记录时间有各自含义，不自动证明实际创作或事件发生时间。
- 缺少可靠时间或时区时，标为未知，不补造精确值。
- 跨系统核对时保留原值和时区，必要时比较 UTC 对应时刻，并说明已知的时钟偏差。
- 格式正确只表示可定位和比较，不单独证明真实性、权属或法律效力。涉及核验时保留来源记录及其上下文。

显示与归档格式见[日期与时间](spec-datetime-format-001.md)。
