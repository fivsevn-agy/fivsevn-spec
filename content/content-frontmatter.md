# Content Frontmatter Specification
# 正文前置元信息规范

---
Frontmatter模版（参考）
  
```yaml
---
title: 啦啦啦       # 文章主标题
date: 2025-04-12      # 创建日期
updated: 2025-04-18   # 最近一次更新时间
author: 五月七日        # 作者署名
description: 啦啦啦    # 简要描述文章内容
notes: 啦啦啦          # 方法论说明 / 副标题

lang: zh-CN             # 正文主语言
multilang: zh / ja      # 涉及的其他语言

category: 啦啦啦   # 所属文章分类
tags:                  # 自定义标签数组
  - 啦啦啦       # 示例标签
  - 啦啦啦       # 示例标签

permalink: 啦啦啦             # 文章固定链接
original_url: 啦啦啦          # 原始链接

status: draft     # 状态：draft或 published
layout: post          # 页面布局模板标识符
toc: true/false       # 是否启用目录
comments: true/false  # 是否开启评论功能
pin: true/false       # 是否置顶显示文章
---
```
  
---
## 规范要点

- Frontmatter 位于博客最开头
- Frontmatter 必须存在，但字段可为空
- Frontmatter 不属于正文内容
- 正文不应依赖 Frontmatter 才能成立
- 模板为参考实现，不构成强制字段清单


