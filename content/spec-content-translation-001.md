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
updated: "2026-06-16"
metadata_updated: "2026-10-13"
---
# Content Translation Specification
# 翻译内容规范

本文定义 fivsevn 内容体系中翻译类文件的基本要求。  
本规范适用于从网页、文章、说明文档或其他外部材料生成的中文翻译稿。

翻译内容应同时遵循：

```text
content/spec-content-frontmatter-001.md
appendix/spec-content-frontmatter-enums-001.md
appendix/spec-content-frontmatter-enums-quickref-001.md
```

---

## 目录

- [1. 目的](#1-目的)
- [2. 适用范围](#2-适用范围)
- [3. 基本原则](#3-基本原则)
- [4. Frontmatter 要求](#4-frontmatter-要求)
- [5. 原文信息字段](#5-原文信息字段)
- [6. 正文结构](#6-正文结构)
- [7. 翻译要求](#7-翻译要求)
- [8. 图片与远程资源](#8-图片与远程资源)
- [9. 网页内容清理](#9-网页内容清理)
- [10. 版权与公开发布说明](#10-版权与公开发布说明)
- [11. 自动化生成要求](#11-自动化生成要求)
- [12. 推荐输出结构](#12-推荐输出结构)

---

## 1. 目的

翻译内容规范用于统一翻译稿的保存方式，使翻译文件能够直接进入 fivsevn devlog / site 内容体系。

本规范主要解决以下问题：

- 翻译文件如何填写 frontmatter；
- 原文信息如何记录；
- 翻译正文应保留哪些内容；
- 网页抓取内容中哪些部分应删除；
- 图片、链接和远程资源如何处理；
- 快捷指令或 AI 辅助生成时应遵守哪些边界。

---

## 2. 适用范围

本规范适用于以下内容：

- 外部网页文章的中文翻译；
- 技术文档、博客文章、新闻材料的中文翻译；
- 通过快捷指令抓取网页 Markdown 后生成的译文；
- 需要保留原文链接和出处信息的翻译稿。

本规范不适用于：

- 原创文章；
- 摘要笔记；
- 评论文章；
- 读后感；
- 只保留观点、不保留原文结构的改写内容。

如果内容已经脱离原文结构，变成整理、评论或再创作，则不应使用 `type: translation`。

---

## 3. 基本原则

翻译文件应遵循以下原则：

1. **忠实原文**  
   翻译应准确传达原意，不删减、不扩写，不把翻译改写成评论或解读。

2. **结构可对照**  
   尽量保留原文段落顺序、标题层级、列表、表格、引用和代码块，方便与原文对照。

3. **来源清楚**  
   必须记录原文标题、来源名称、发布方和原文链接。

4. **格式稳定**  
   frontmatter 使用统一字段，并按字段组保留空行。

5. **资源按许可保存**  
   普通引用链接保留原目标；图片和附件在来源许可允许时归入文章发布包，否则保留原始远程引用及必要的使用说明。

---

## 4. Frontmatter 要求

翻译内容必须使用：

```yaml
type: translation
source_of_truth: translation
```

推荐基础设置：

```yaml
type: translation
status: active
canonical: true
audience: [self, public]
languages: [zh]
maturity: stable
confidence: 0.9
visibility: public
source_of_truth: translation
```

如果译文只是暂存、尚未检查，才使用：

```yaml
status: hidden
audience: [self]
maturity: draft
confidence: 0.0
visibility: private
```

frontmatter 字段必须按分组保留空行。推荐结构如下：

```yaml
---
id: module-submodule-topic-001
title: 中文标题

module: module-name
submodule: submodule-name
topic: specific-topic

type: translation
status: active
canonical: true

summary: >
  一到两句中文摘要。

parents: []
related: []

tags: []

audience: [self, public]
languages: [zh]

maturity: stable
confidence: 0.9

visibility: public
source_of_truth: translation

original_title:
original_source:
original_publisher:
original_url:
translation_note: >
  本文为原文内容的中文翻译，仅用于学习与知识整理。
  原文版权归原作者及出版方所有。若权利人认为本文不宜公开保留，请联系后删除或调整。

created: YYYY-MM-DD
updated: YYYY-MM-DD
---
```

要求：

- 不保留占位符；
- 不在 YAML 中保留 `#` 注释；
- `summary: >` 和 `translation_note: >` 的正文换行并缩进两个空格；
- `created` 与 `updated` 使用 `YYYY-MM-DD`；
- frontmatter 结束后空一行，再进入正文。

---

## 5. 原文信息字段

翻译内容必须使用以下原文信息字段：

```yaml
original_title:
original_source:
original_publisher:
original_url:
translation_note:
```

字段含义如下：

| 字段 | 含义 |
|---|---|
| `original_title` | 原文标题 |
| `original_source` | 原文来源名称，例如栏目名、站点名、项目名 |
| `original_publisher` | 原文发布方，例如网站、机构、媒体或作者所属主体 |
| `original_url` | 原文 URL |
| `translation_note` | 翻译说明 |

注意：

- 原文 URL 应填写在 `original_url`，不应填入 `original_source`；
- 如果无法判断 `original_source` 和 `original_publisher` 的区别，可以都填写网站名；
- 如果原文没有明确标题，应根据页面标题或正文主标题保守填写；
- `translation_note` 不应写成长篇译者说明。

推荐翻译说明：

```yaml
translation_note: >
  本文为原文内容的中文翻译，仅用于学习与知识整理。
  原文版权归原作者及出版方所有。若权利人认为本文不宜公开保留，请联系后删除或调整。
```

---

## 6. 正文结构

翻译文件正文推荐使用以下结构：

```markdown
## 文章翻译

### source

- [原文链接](原文链接)

### note

本文为原文内容的中文翻译，仅用于学习与知识整理。原文版权归原作者及出版方所有。若权利人认为本文不宜公开保留，请联系后删除或调整。

---

## 正文

# 中文译文标题

完整中文翻译正文
```

说明：

- `source` 部分用于人工快速回到原文；
- `note` 部分用于说明翻译用途、原文权利归属和删除调整请求；
- `正文` 部分应先写中文译文标题，再放完整中文译文；
- 不需要在正文后附上完整英文原文；
- 除非原文中的代码、链接、专有名词或必要格式需要保留，否则正文应以中文译文为主。

---

## 7. 翻译要求

翻译正文应遵守以下要求：

1. 忠实传达原意，不删减、不扩写。
2. 不用总结替代翻译。
3. 不改写为评论、解读或二次创作。
4. 保留原文段落顺序，尽量逐段翻译。
5. 保留 Markdown 标题、列表、表格、引用块、代码块和链接结构。
6. 原文入口和普通引用链接保持原目标；获准本地保存的图片、附件按发布包路径更新。
7. 专有名词、技术术语、人名、机构名和产品名应准确处理。
8. 常见技术术语使用自然中文译法；必要时保留英文原词。
9. 语言应自然流畅，符合中文阅读习惯。保持良好的中文水平。
10. 不改变事实、时间、数量、因果关系或语气。
11. 原文中的幽默、口语、引号和括号说明，应尽量保留表达效果。
12. 原文中的明显拼写、语法或标点问题，翻译时可自然化处理，但不得改变含义。
13. 不遗漏标题、图片说明、列表、引用、括号内容或脚注式信息。
14. 无法确定含义时，采用保守译法，不自行发挥。

---

## 8. 图片与远程资源

翻译稿保留原文中的图片、图片说明、alt 文本和附件信息。资源的保存方式取决于来源许可：

- 已获准保存的图片和附件，放在本篇文章发布包的 `assets/`，正文更新为对应的包内资源路径；
- 未获准转存的资源保留原始远程引用，不擅自下载、重新分发或转换格式；
- 图片获准本地保存时保留原始字节、文件身份和出处，不能因迁移而移除署名或使用限制；
- 原作的普通引用链接、原文入口与外部文章链接保持原目标。

### 8.1 本地发布包

```text
posts/YYYY/MM/<文章编号>/
├── index.md
└── assets/
    └── image-01.jpg
```

公开路径须与发布包和站点构建一致。文章使用固定 `permalink` 时，图片采用完整站内路径，避免浏览器按旧文章网址寻找附件：

```markdown
![原 alt 文本](/posts/2026/06/posts-example/assets/image-01.jpg)

翻译后的原图片说明。
```

保存原文入口、原始图片出处及必要的版权或许可记录。发布包归档本身不产生新的转载、翻译或媒体保存许可。

### 8.2 远程引用

普通图片保留：

```markdown
![Image](URL)
```

图片缩略图包裹链接时保留：

```markdown
[![Image](URL)](LINK)
```

保留远程引用时，可在文中一次说明：

```markdown
> 部分图片引用原文远程资源；若无法显示，请访问原文。
```

要求：

- 不删除原文中与正文有关的图片；
- 保留远程引用的原图片 URL 和外层链接目标；
- 图片 alt 文本保持原样，不翻译、不改写；
- 原文自带图片说明仍应保留并翻译；
- 不在没有远程图片的地方添加远程资源提示；
- 有特殊署名或许可要求的图片按其条件标明，不以统一提示替代。

---

## 9. 网页内容清理

从网页抓取 Markdown 时，正文中可能混入非正文网页元素。  
翻译稿应只保留文章主体和与正文直接相关的扩展阅读内容。

应删除：

- 网页导航；
- Cookie 提示；
- 菜单；
- 搜索框；
- 作者页脚；
- 分类列表；
- 归档列表；
- 评论区；
- 分享按钮；
- 广告；
- 站点说明；
- 与正文无关的推荐内容。

可酌情保留：

- 与正文直接相关的参考链接；
- 原文中的相关阅读；
- 文章内部的脚注、注释和来源说明；
- 对理解正文有必要的附录材料。

---

## 10. 版权与公开发布说明

翻译内容公开发布前应核实来源许可，保留来源信息，并避免把译文伪装为原创内容。用途说明不代替转载、翻译或媒体保存授权。

每篇译文正文中应在 `source` 之后加入固定说明：

```markdown
### note

本文为原文内容的中文翻译，仅用于学习与知识整理。原文版权归原作者及出版方所有。若权利人认为本文不宜公开保留，请联系后删除或调整。
```

frontmatter 中的 `translation_note` 应使用同一含义的说明：

```yaml
translation_note: >
  本文为原文内容的中文翻译，仅用于学习与知识整理。
  原文版权归原作者及出版方所有。若权利人认为本文不宜公开保留，请联系后删除或调整。
```

公开发布时应遵守以下原则：

- 必须保留原文链接；
- 必须记录原文标题、来源和发布方；
- 不删除原文自带的作者、来源、版权或许可说明；
- 不声称译文为原创文章；
- 不将译文包装为商业发布内容；
- 如果原文明确禁止转载、复制或翻译，应优先不公开发布；
- 如果原文来自付费墙、会员区、未公开材料或受限访问内容，不应公开发布完整译文；
- 如果权利人提出删除或调整请求，应及时删除或调整。

不同来源可按以下方式处理：

| 原文状态 | 建议处理 |
|---|---|
| 明确开放许可 | 可公开发布，保留署名、来源和许可信息 |
| 普通公开网页，无明确开放许可 | 先核实转载、翻译及媒体保存许可；公开可访问不等于授权 |
| 明确禁止转载、复制或翻译 | 不建议公开发布 |
| 付费墙、会员内容、未公开内容 | 不公开发布完整译文 |
| 新闻短讯、官方公告、技术说明 | 保留来源后谨慎公开 |

本说明不等同于授权，也不保证某篇译文一定没有版权风险。  
其作用是明确译文用途、保留来源、降低误认和方便权利人联系处理。

---

## 11. 自动化生成要求

通过快捷指令或 AI 自动生成翻译稿时，应遵守以下要求：

- 只输出完整 Markdown 文件内容；
- 不输出解释过程；
- 不输出“我将如何处理”；
- 不把规则说明写入最终文件；
- 不把英文原文整段附在译文后面；
- 不保留模板占位符；
- 不在 frontmatter 中保留注释；
- frontmatter 字段组之间必须保留空行；
- 原文 URL 必须写入 `original_url`；
- 正文 `source` 后必须加入 `note` 版权与公开发布说明；
- `source_of_truth` 必须为 `translation`；
- 文件名可由自动化工具决定，但推荐使用 frontmatter 中的 `id`。
- 本规范默认生成可公开发布的译文；如只是暂存或未检查，应手动改为 `status: hidden` 与 `visibility: private`。

如果自动化工具无法直接生成文件附件，则应输出纯 Markdown 文本，供后续步骤保存为 `.md` 文件。

---

## 12. 推荐输出结构

最终文件推荐结构如下：

```markdown
---
id: module-submodule-topic-001
title: 中文标题

module: module-name
submodule: submodule-name
topic: specific-topic

type: translation
status: active
canonical: true

summary: >
  一到两句中文摘要。

parents: []
related: []

tags: []

audience: [self, public]
languages: [zh]

maturity: stable
confidence: 0.9

visibility: public
source_of_truth: translation

original_title:
original_source:
original_publisher:
original_url:
translation_note: >
  本文为原文内容的中文翻译，仅用于学习与知识整理。
  原文版权归原作者及出版方所有。若权利人认为本文不宜公开保留，请联系后删除或调整。

created: YYYY-MM-DD
updated: YYYY-MM-DD
---

## 文章翻译

### source

- [原文链接](原文链接)

### note

本文为原文内容的中文翻译，仅用于学习与知识整理。原文版权归原作者及出版方所有。若权利人认为本文不宜公开保留，请联系后删除或调整。

---

## 正文

# 中文译文标题

完整中文翻译正文
```

---
