---
id: spec-content-media-naming-001
title: 发布包媒体命名

module: spec
submodule: content
topic: null

type: spec
status: active
canonical: true

summary: null

parents: []
related: []

tags: []

audience:
- self
- internal
languages:
- zh

maturity: evolving
confidence: null

visibility: public
source_of_truth: spec

created: null
updated: '2026-11-01'
metadata_updated: '2026-11-01'
---

# 发布包媒体命名

## 目录与文件名

普通发布包保留 `栏目/YYYY/MM/<id>/index.md` 与 `assets/`。已有 `id`、目录和文章地址保持稳定；`index.md` 不另行改名。Bygone 独立放在 `stills/bygone/`，不进入年月帖子列表。草稿和共享素材不使用发布包命名规则。

发布包内图片统一为：

```text
YYYYMMDD-HHMMSS-<board>-<package-key>-NNN.ext
20261030-003114-savour-0b4a110839f1-001.webp
```

| 部分 | 规则 |
|---|---|
| `YYYYMMDD-HHMMSS` | `extra.published_at` 转换为 `Asia/Shanghai` 的发布时间；年月目录使用同一时区 |
| `board` | `flux`、`savour`、`fieldlog`、`stills` 或 `motion` |
| `package-key` | UTF-8 字符串 `board + ":" + id` 的 SHA-256 前 12 位，小写十六进制；由工具生成 |
| `NNN` | 本包从 `001` 开始的正整数，至少三位，超过 999 后自然扩展；不复用已分配序号 |
| `ext` | 实际文件格式的小写扩展名；JPEG 使用 `.jpg`，WebP 使用 `.webp` |

稳定标识属于发布包身份，不能使用图片内容摘要替代。图片替换、标题修改或正文调整不重新计算它。即使同一秒发布多个包，文件仍可区分；校验工具拒绝重复名称。同一文件多次展示仍引用同一个文件。

## 分配与修改

1. 先确定稳定 `id` 和带时区的发布时间，再生成图片名。时间缺失时停止，不从文件修改时间、旧文件名或 EXIF 猜测发布时间。
2. 单图帖子使用 `001`。Stills 新影集按上传相对路径排序，依次分配 `001`、`002` 等；一次推送是一组。一次上传多张到 Flux、Savour、Fieldlog 时，每张分别建包，各包从 `001` 开始。
3. 已有包首次整理时，按 `extra.images`、`extra.image` 或正文首次引用顺序分配；未被引用的包内图片排在后面。首次整理完成后，不因页面排序改变文件名。
4. 调整展示顺序只改 `extra.images` 或正文引用。增加图片使用本包已有最大序号加一；删除不重排其余图片，也不复用空号。更换同一位置的文件保持名称，格式变化仅改扩展名并同步引用。
5. 重命名必须同时更新 Markdown、配置、校验清单及发布状态中的文件路径；校验字节摘要保持不变。原文件名不参与页面地址或去重判断。

文件名时间只用于归档排序，不是拍摄时间或证据时间。Bygone 使用集合的保存发布时间命名，历史照片日期仍写在图片说明中；日期未知的原始资料不能补造时间。

## 自动化

[共享工具](../tools/media_naming.py) 提供 `media_filename(board, id, published_at, number, extension)`，各内容仓库在 `scripts/media_naming.py` 保存相同副本。导入器在保存发布包时调用它；常规构建只读校验，不反复重命名。

```sh
python scripts/media_naming.py check --site stills --root stills
```

校验范围包括发布、隐藏和草稿状态的正式发布包。临时上传入口允许手机原文件名；导入完成后按规则保存。未编排原始草稿、头像、横幅、字体、图标等共享素材保留原状。Motion 目前直接嵌入 YouTube，没有本地封面图片；以后增加发布包图片时使用同一规则。

图片格式由各栏目既有保存策略决定：Flux、Savour、Fieldlog 自动上传保存为 WebP，Stills 保留原始字节，显示缩图只在 `_site/` 生成。重命名本身不压缩、转换或改变照片。
