---
module: system
type: note
status: archived
canonical: false
summary: >
  archived
tags: [archive]
visibility: public
source_of_truth: devlog
updated: 2026-03-01
---
# Markdown 常用语法示范

本模板用于快速回顾 Markdown 基础语法。  
对于新手：存在多种写法的情况下，本示范采取“一种需求仅对应一种最优解”的原则。
  
---

## 1. 换行

Markdown 默认不会自动换行，解决方法如下：

**在行尾加两个空格 + 回车**
  
```markdown
这是第一行（末尾加两个空格）  
这是第二行
```

---

## 2. 缩进
  
Markdown 使用空格控制嵌套层级，推荐每层缩进 2 个空格。**避免使用 Tab 键**，兼容性更好。

**嵌套列表示例：**  

```markdown
- 第一层
  - 第二层（缩进 2 空格）
    - 第三层（缩进 4 空格）
```

---

## 3. 标题

用井号 `#` 表示标题，井号越多表示层级越小：

```markdown
# 一级标题
## 二级标题
### 三级标题
```

---

## 4. 加粗 / 斜体 

```markdown
**加粗**
*斜体*
```

---

## 5. 链接与图片

```markdown
[这是一个链接](https://example.com)
![这是图片](https://example.com/image.png)
```

---

## 6. 列表

### 无序列表

```markdown
- 项目A
  - 子项目A.1
    - 子项目A.1.1
```

### 有序列表

```markdown
1. 第一步
2. 第二步
   1. 子步骤
```

---

## 7. To-Do List

```markdown
- [ ] 未完成事项
  - [ ] 子事项
  - [x] 已完成子事项
- [x] 已完成事项
```

---

## 8. 引用

```markdown
> 这是引用内容
>> 嵌套引用
```
  
---

## 10. 表格

```markdown
| 名称   | 类型   | 备注         |
|--------|--------|--------------|
| 项目A  | 功能型 | 主功能模块   |
| 项目B  | 辅助型 | 可选支持部分 |
```

---

## 11. 分割线

```markdown
---
```

---

## 12. “更多”标记

“更多”用于截断引言 Epigraph 和正文 Essay。本博客主页只会显示 Epigraph 的部分，点击“更多”可以进入展示全部内容的文章页面。Wordpress 可以用模块去编辑，Github 的 md 备份也希望能在结构上体现这一点。

```markdown
<!-- more -->
```

---

## 13. 折叠内容

本博客用于文献等材料的折叠收纳。

```markdown
<details>
<summary>点击展开详细内容</summary>

这里是可以收起的内容。  

> 引用  
  
</details>
```

渲染效果如下：

<details>
<summary>点击展开详细内容</summary>

这里是可以收起的内容。  

> 引用  

</details>

---

## 14. 代码块的显示特性说明

*本节内容已作教程处理，不用回归源码查看。*  
**注意区分“源代码演示”与“渲染效果”。**  

⬇️这是源码

````markdown
```markdown
*斜体*
```
````

⬇️这是代码块

```markdown
*斜体*
```

⬇️这是渲染效果

*斜体*

---

补充：教学代码块展示写法如下：  

`````markdown
````markdown
```markdown
这是第一行（末尾加两个空格）  
这是第二行
```
````
`````

即用四个反引号组包裹三个反引号组。以此类推，教学的教学就是再套一组五个反引号，即本段回归源码可以看到的内容。  

---

## 15. YAML 

这是博客文章的 md 备份文档当中，放在**每篇最前面**的前置信息板块。前后用 `---` 隔开作为独立模块。用户可以根据需求，选择部分项目填写，以准确记录文章的相关信息，方便后续的整理、检索和分析。

```yaml
---
# 文章标题，支持任意语言
title: マイマイカブリ

# 创建日期与时间（发布时间）
date: 2025-04-12 15:36:00

# 最后更新日期与时间
updated: 2025-04-12 15:50:00

# 作者署名，可为昵称或真实姓名
author: 五月七日

# 简短描述，用于搜索引擎摘要、卡片简介等
description: 有关日本食蜗步甲的资料初步收集。

# 可选副标题，不显示在正文，可用作内部标识或模板识别
notes: 副标题

# 主语言，用于 SEO、HTML 标签、字体渲染等（如 zh-CN / ja / en）
lang: zh-CN

# 自定义字段，标记文章涉及的其他语言，供人类或模板辅助识别
multilang: zh / ja

# 分类（单值），用于文章归类导航
category: 旅行香料盒_Zibaldone

# 标签（多值），用于内容筛选、关联推荐等
tags:
  - insect
  - carabidae

# 自定义永久链接，决定文章的 URL 路径
permalink: /zibaldone/maimaikaburi/

# 可选字段，记录原始出处链接（如转载、外部发布）
original_url: （博客原文链接）

# 文章状态：draft（草稿）、published（已发布）、archived（归档/隐藏）
status: published

# 页面布局类型：post（文章）、page（独立页面）、link 等
layout: post

# 是否启用文章目录（需主题支持）
toc: false

# 是否开启评论功能（需集成评论系统）
comments: true

# 是否置顶显示（主题支持时生效）
pin: false

# 是否为草稿，Hugo/Hexo 默认支持，设为 true 时不会被发布
draft: false

# 是否隐藏文章：不会显示在首页、列表、RSS 等位置（适合隐私文）
hidden: false

# SEO 设置：禁止搜索引擎收录该页面（如为私密或测试内容）
robots: noindex, nofollow

# 别名路径（用于旧链接重定向，可写多个）
aliases:
  - /old-url/

# 阅读时间估算（用于前端展示，可自动生成）
reading_time: 4min

# 字数统计（如用于显示“约 xx 字”提示）
word_count: 932

# 最后修改时间（标准格式，部分系统用于排序/同步）
lastmod: 2025-04-12T15:50:00Z

# 封面图 URL，显示在文章顶部或预览卡片
cover: /images/maimai.jpg

# 横幅图 URL，用于页面背景/横幅（主题不同用途不同）
banner: /images/header.png

# 简要摘要，可在文章卡片或社交分享中显示
excerpt: 一句话摘要，适合在卡片中显示

# 授权协议，推荐使用 Creative Commons 格式（如 CC BY-NC-SA 4.0）
license: CC BY-NC-SA 4.0

# 协作者信息，可扩展写多个（适合多人协作项目）
contributor:
  - name: 钱臻
    role: 原图作者
    email: （可省略）

# 翻译者署名，用于注明本文译自他文
translator: 小邓

# 多语言内容绑定的统一标识符（用于语言切换跳转）
translationKey: maimaikaburi

# 该文章的其他语言版本（备用字段，需手动同步）
langAlt:
  - ja
  - en

# 连载系列名，适合整理专题或多篇系列文
series: 日本昆虫记

# 排序权重（适用于某些主题或列表中人工排序）
weight: 5

# 是否为首页精选文章（主题支持时高亮显示）
featured: false

# 置顶权重，一些系统用数字控制置顶优先级（比 pin 更细粒度）
sticky: 0

# 是否允许构建时发布（如设为 false，可用于保留未公开内容）
published: true

# 是否参与构建流程（用于构建脚本筛选）
build: true
---
```

---
