---
id: spec-readme
title: fivsevn-spec

module: spec
submodule: guide
topic: null

type: index
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

filename_policy: entrypoint

created: '2025-12-14'
updated: '2026-11-01'
metadata_updated: '2026-11-01'
---

# fivsevn-spec

各内容仓库共用的字段、发布包和媒体命名规则。

- [Frontmatter](content/spec-content-frontmatter-001.md) · [字段取值](appendix/spec-content-frontmatter-enums-001.md)
- [发布包](content/spec-content-site-post-001.md) · [媒体命名](content/spec-content-media-naming-001.md)
- [译文](content/spec-content-translation-001.md) · [来源登记](source/spec-source-intake-fields-001.md)
- [时间格式](spacetime/spec-datetime-format-001.md) · [时间证据](spacetime/spec-datetime-evidence-001.md)
- [提交信息](gov/spec-commit-message-001.md) · [目录](system/spec-system-map-001.md)

`content/` 保存两个 JSON schema，`tools/` 保存校验及命名工具。内容仓库里的副本必须与它们一致，更新时同步修改。Actions 运行文档和工具校验，不部署网站。

```sh
python -m pip install pyyaml jsonschema
python -m unittest discover -s tests -v
python tools/check_metadata.py --repo spec --schema content/content-metadata.schema.json
```
