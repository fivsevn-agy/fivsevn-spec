---
id: "spec-content-translation-001"
title: "翻译内容规范"

module: "spec"
submodule: "content"
topic: "spec-content-translation-001"

type: "spec"
status: "active"
canonical: true

summary: "说明翻译内容规范。"

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
updated: '2026-11-01'
metadata_updated: '2026-11-01'
---

# 译文

译文使用 `type: translation`、`languages: [zh]` 和[完整核心字段](spec-content-frontmatter-001.md)。原作信息写在 `original_title`、`original_source`、`original_publisher`、`original_url`，翻译说明写在 `translation_note`。不明的字段留空，不编造作者、日期或授权。

## 正文

```markdown
## 文章翻译

### source

[原文标题](原文网址) · 原作者或出版方

### note

翻译用途、原作版权与许可说明。

## 正文

# 中文译文标题

逐段译文……
```

- 忠实传达原意，保留段落顺序、事实、时间、数量、语气及不确定性；不以总结、评论或扩写替代翻译。
- 保留标题、列表、表格、引用、代码、脚注、图片说明和链接。技术术语准确处理，必要时保留原词；不确定的含义使用保守译法。
- 删除网页导航、广告、Cookie 提示、评论、分享按钮及无关推荐；保留与正文有关的来源、注释和附录。

## 图片与附件

已获准保存的原图、附件放在本篇发布包的 `assets/`，正文改用包内路径。保留原始字节、alt、说明和出处；图片说明正常翻译。保留远程引用时使用原网址，并简短说明未本地保存，无需在每张图片下重复提示。

原作的署名、版权、许可和使用限制继续保留。公开可访问或添加用途说明不等于取得转载、翻译或图片转存授权。公开发布须符合来源许可；不绕过登录、付费墙或其他访问限制。`rights` 记录明确的许可条件及核对情况。

文件按 `年/月/文章编号/index.md` 保存。正文和素材在同一发布包中维护，原文网址继续作为出处保留。日期、字段值及媒体格式分别见[时间规则](../spacetime/spec-datetime-format-001.md)、[枚举速查](../appendix/spec-content-frontmatter-enums-quickref-001.md)和[媒体规则](spec-content-media-naming-001.md)。
