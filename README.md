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
- en

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

[System map](https://github.com/fivsevn-agy/fivsevn-devlog/blob/main/system-map.md)

Shared contracts for the fivsevn content repositories. Active documents define content metadata, publishing packages, media naming, time records, source attribution, and repository organization.

## Publishing contracts

- [Content frontmatter](content/spec-content-frontmatter-001.md) and [core JSON schema](content/content-metadata.schema.json).
- [Site-post profile](content/spec-content-site-post-001.md) and [profile schema](content/site-post.schema.json) for Flux, Savour, Fieldlog, Stills, Motion, SYS, and CCTV.
- [Publication media naming](content/spec-content-media-naming-001.md).
- [Date and time](spacetime/spec-datetime-format-001.md) and [time evidence](spacetime/spec-datetime-evidence-001.md).
- [Field values](appendix/spec-content-frontmatter-enums-001.md) and [quick reference](appendix/spec-content-frontmatter-enums-quickref-001.md).

## Source layout

| Directory | Responsibility |
|---|---|
| `content/` | Metadata, publication profiles, translation and media rules |
| `tools/` | Offline metadata normalizer, validators and media-name generator |
| `appendix/` | Enumerations and lookup tables |
| `spacetime/` | Dates, times and evidence |
| `source/` | Source and citation conventions |
| `system/`, `gov/` | Repository structure and commit messages |
| `archive/` | Archival policy |
| `tests/` | Contract regression tests |

The site repositories keep identical copies of `site_post_metadata.py`, `media_naming.py`, and both schemas. Their builds validate saved content offline; Actions checks those copies against this repository. Update the authoritative contract and its consumers together. Superseded documents and unused intermediates are removed from the current tree; prior versions remain in Git history.

## Validation

```sh
python -m pip install pyyaml jsonschema
python -m unittest discover -s tests -v
python tools/check_metadata.py --repo spec --schema content/content-metadata.schema.json
```

To check a connected site's saved packages, pass `--profile site-post-v1 --site <board> --content-root <folder>` to `tools/check_metadata.py`. Ordinary documents and saved publication packages have separate validation entry points because fixed directory pages and temporary trigger files are not publication packages.

The `Check shared metadata` workflow runs on pushes and pull requests. It validates the documents and shared helpers; this repository does not deploy a public website.
