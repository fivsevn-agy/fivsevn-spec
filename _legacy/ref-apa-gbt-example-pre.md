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
> Status: archived  
> Validity: expired  
> Replaced by: source/
> Note: retained for historical reference only

---

# 常见文献类型及引用规范

- 示例 APA 7th 与 GB/T 7714-2015 对照
## 一、期刊文章 Journal Article

### APA 7th
> Author, A. A., & Author, B. B. (Year). Title of the article. *Title of the Journal*, *Volume*(Issue), page range. https://doi.org/xxx

**示例**：  
> Smith, J., & Lee, K. (2020). Innovation in education. *Journal of Educational Research*, *45*(2), 123–135. https://doi.org/10.1234/edu.2020.045

### GB/T 7714
> 作者. 文章标题[J]. 刊名, 出版年, 卷号(期号): 起止页码.

**示例**：  
> 张三. 高等教育质量评价体系研究[J]. 教育理论与实践, 2020, 40(6): 58–62.

---

## 二、专著 / 图书 Book

### APA 7th
> Author, A. A. (Year). *Title of the book*. Publisher.

**示例**：  
> Brown, D. (2015). *Principles of Language Learning and Teaching*. Pearson Education.

### GB/T 7714
> 作者. 书名[M]. 出版地: 出版社, 出版年.

**示例**：  
> 王五. 教育学导论[M]. 北京: 高等教育出版社, 2018.

---

## 三、图书章节 Chapter in an Edited Book

### APA 7th
> Author, A. A. (Year). Title of chapter. In E. E. Editor (Ed.), *Title of book* (pp. xxx–xxx). Publisher.

**示例**：  
> King, A. (2012). Cooperative learning. In R. Mayer (Ed.), *Learning theories in education* (pp. 75–98). Academic Press.

### GB/T 7714
> 章节作者. 章节题名[A]. 见：主编. 书名[M]. 出版地: 出版社, 出版年: 页码.

**示例**：  
> 李强. 课堂管理策略研究[A]. 见：张伟主编. 教育心理学新进展[M]. 上海: 华东师范大学出版社, 2017: 112–128.

---

## 四、学位论文 Thesis / Dissertation

### APA 7th
> Author, A. A. (Year). *Title of thesis* (Master’s thesis or Doctoral dissertation). Institution. URL

**示例**：  
> Miller, T. (2019). *Teacher perceptions of inclusive education* (Doctoral dissertation). University of Michigan. https://deepblue.lib.umich.edu/handle/2027.42/147639

### GB/T 7714
> 作者. 论文题目[D]. 所在城市: 学校名称, 出版年.

**示例**：  
> 刘洋. 初中生学习动机的影响因素研究[D]. 北京: 北京师范大学, 2021.

---

## 五、会议论文 Conference Paper

### APA 7th
> Author, A. A. (Year, Month). Title of presentation. *Conference Name*, Location.

**示例**：  
> Lin, M. (2022, July). Smart learning environments in China. *International Conference on Education Innovation*, Shanghai, China.

### GB/T 7714
> 作者. 论文题目[A]. 见：会议名称, 会议地点, 出版地: 出版社, 出版年: 页码.

**示例**：  
> 陈立. 网络学习行为研究[A]. 见：全国教育技术大会论文集, 北京, 北京: 高教出版社, 2019: 85–92.

---

## 六、报纸文章 Newspaper Article

### APA 7th
> Author, A. A. (Year, Month Day). Title of article. *Title of Newspaper*, page.

**示例**：  
> Roberts, S. (2020, May 5). Online learning gains momentum. *The New York Times*, p. A3.

### GB/T 7714
> 作者. 文章题目[N]. 报纸名称, 出版日期(版次).

**示例**：  
> 张晓. 教育公平亟待突破[N]. 中国教育报, 2021-04-15(7).

---

## 七、网页 / 在线文章 Web Page

### APA 7th
> Author, A. A. (Year, Month Day). Title of page. Website Name. URL

**示例**：  
> World Health Organization. (2020, March 20). Coronavirus advice. WHO. https://www.who.int/emergencies/diseases/novel-coronavirus-2019

### GB/T 7714
> 作者. 文章标题[EB/OL]. 网站名称, 发布日期[引用日期]. 链接地址.

**示例**：  
> 李明. 在线教学的挑战与对策[EB/OL]. 教育在线, 2022-03-15[2025-04-10]. https://www.jyzx.com.cn/article/20220315

---

## 八、标准 / 法规 Standards / Legal Documents

### APA 7th
> Organization. (Year). *Title of standard* (Standard No.). Publisher.

**示例**：  
> International Organization for Standardization. (2018). *Quality management systems – Requirements* (ISO 9001:2015). ISO.

### GB/T 7714
> 标准编号. 标准名称[S].

**示例**：  
> GB/T 7714—2015. 信息与文献 参考文献著录规则[S].

---

## 九、专利 Patent

### APA 7th
> Inventor, A. A. (Year). *Title of patent* (Patent No.). Issuing Agency.

**示例**：  
> Zhang, H. (2020). *Wireless education terminal* (CN202010123456.0). China National Intellectual Property Administration.

### GB/T 7714
> 专利申请人. 专利名称[P]. 专利国别及专利号, 出版日期.

**示例**：  
> 王磊. 一种智能教学设备[P]. 中国专利: CN201911234567.0, 2020-06-12.