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
# Content Backmatter Specification
# 正文后置信息规范

---
Backmatter模版（参考）

```yaml
---
references: 

  people: # 文章中提到的历史人物或真实人物
    - id: christie  # 内部引用 ID
      name: Agatha Christie  # 人物原名
      zh_name: 阿加莎·克里斯蒂  # 人物中文译名
      role: author  # 人物角色（如 author / translator / director / subject 等）
      lifespan: ”1890–1976“  # 生卒年

  works_discussed:  # 正文中重点分析的文学作品
    - id: poirot  # 文本引用 ID
      title: Poirot Investigates  # 作品原文名称
      zh_title: 《首相绑架案》  # 中文译名
      author: Agatha Christie  # 作者名称
      year: 1924  # 首次出版年份（原作）
      editions:  # 该作品涉及的主要版本（如中译版/重印版等）
        - lang: zh  # 语言代码
          citation: 阿加莎克里斯蒂. 首相绑架案[M]. 王占一 译. 北京: 新星出版社, 2018.
          # 中文引用格式，可直接用于 GB/T 样式呈现

        - lang: en
          citation: Christie, A. (1924). *Poirot Investigates*. The Bodley Head.
          # 英文原作引用格式，适用于 APA/MLA 风格渲染

  sources:  # 本文引用或提及的文献资料
    - id: zhang2021  # 唯一引用标识符，供正文 [cite:zhang2021] 使用
      type: journal  # 来源类型：book / journal / thesis / report / chapter 等
      author: 张三  # 作者姓名
      title: 波洛侦探形象的文化演变  # 文献标题
      journal: 外国文学评论  # 期刊名称
      year: 2021  # 出版年份
      volume: 45  # 卷号（如期刊）
      issue: 3  # 期号（如期刊）
      pages: 112–128  # 页码范围
      lang: zh  # 文献语言，用于风格判断与格式选择

    - id: smith2019
      type: book
      author: John Smith
      title: *Detective Fiction and Modernity*  # 支持渲染为斜体书名
      publisher: Oxford University Press
      year: 2019
      lang: en
---
```
  
---
## 规范要点

- Backmatter 主要集中存放正文的参考资料来源等
- Backmatter 位于正文（Body）之后
- Backmatter 不属于正文内容
- Backmatter 用于存放结构化参考信息
- Backmatter 不参与正文叙事与论证
- 正文可引用 Backmatter 中的条目
- Backmatter 的存在不影响正文成立


