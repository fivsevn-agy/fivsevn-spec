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
# Date and Time Format Specification
# 日期与时间书写规范

---
## 1. 目的

- 用于约定不同使用场景下的日期与时间书写方式，以避免含义混淆和格式滥用。

---
## 2. 时间写法层级

- 时间相关写法按用途分为三层，层级之间互不替代。

### 2.1 Level 1：日期记录（个人记录）

> 用途：手写笔记、日常记录、更新说明  
> 是否为时间戳：否  
> 是否参与系统计算：否  

- 规范格式：

```
YYYY.MM.DD
```

- 示例：

```
2025.12.13
```

- 规则：

  - 仅表示“某一天”
  - 不表达具体时间
  - 不要求时区信息
  - 作为个人记录习惯长期保持稳定

```
Notes（参考，不作为规范要求）

以下写法在不同地区或个人习惯中广泛存在，仅作参考：

美式日期顺序：
MM/DD/YYYY
12/13/2025

欧式日期顺序：
DD/MM/YYYY
13/12/2025

短年份写法：
YY.MM.DD
25.12.13

其他分隔符号示例：
2025-12-13

说明：
- 上述写法不在本规范推荐范围内
- 容易在跨地区、跨语境时产生歧义
- 仅用于理解他人记录或历史资料
- 不要求、也不建议在本规范体系内使用
```


### 2.2 Level 2：日期标记（文档 / 内容命名）

> 用途：文档标题、内容分组、资料归档  
> 是否为时间戳：否  
> 是否表达具体时刻：否  

- 规范格式：

```
YYYYMMDD
```

- 示例：

```
20251213
```

- 规则：

  - 使用纯数字
  - 不使用任何分隔符
  - 固定宽度，天然支持排序
  - 适用于文档命名与内容组织


### 2.3 Level 3：严格时间点（系统时间戳）

> 用途：系统字段、发布时间、事件时间  
> 是否为时间戳：是  
> 是否具备唯一性：是  

- 唯一推荐格式（ISO 8601，含时区）：

```
YYYY-MM-DDTHH:mm:ss±HH:MM
```

- PHP 输出格式：

```
Y-m-d\TH:i:sP
```

- 示例：

```
2025-04-09T03:31:31+08:00
```

- 规则：

  - 必须包含时区信息
  - 禁止使用不含时区的时间字符串
  - 推荐由系统自动生成


---
## 3. 使用对照表

|  场景  | 使用层级 | 示例 |
|-------|---------|-----|
|笔记/手写记录|Level 1|2025.12.13|
|文档命名/内容归档|Level 2|20251213|
|发布/系统记录|Level 3|2025-04-09T03:31:31+08:00|


---
## 4. 规范立场

- 不强求统一为一种格式
- 每一层级只解决自身问题
- 禁止跨层级滥用


