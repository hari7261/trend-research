# Trend Research

Trend Research is an open research publishing repository built for premium, citation-backed technical articles. Research is authored in Markdown, rendered with Hugo, optimized for discoverability, and deployed automatically through GitHub Actions.

## Editorial Direction

- Topic-first research publishing with stable slugs
- Reference-based technical writing rather than marketing summaries
- Professional presentation with diagrams, tables, and structured sections
- Public contribution workflow for requests, revisions, and peer improvement
- Automated static publishing with clean permalinks and machine-readable outputs

## Current Research

- `latency-aware-multimodal-agent-orchestration`

## Repository Layout

```text
trend-research/
|-- research/
|   `-- latency-aware-multimodal-agent-orchestration/
|       |-- index.md
|       `-- assets/
|           |-- architecture.svg
|           `-- latency-pipeline.svg
|-- website/
|   |-- config.toml
|   |-- assets/
|   |   `-- css/extended/brand.css
|   |-- content/
|   |   `-- _index.md
|   |-- layouts/
|   |   `-- partials/extend_head.html
|   |-- static/
|   `-- themes/
|-- scripts/
|   `-- validate_links.py
|-- .github/
|   |-- ISSUE_TEMPLATE/
|   |   `-- research_request.yml
|   |-- PULL_REQUEST_TEMPLATE.md
|   `-- workflows/deploy.yml
|-- LICENSE
|-- README.md
`-- CONTRIBUTING.md
```

## Local Preview

```bash
python scripts/validate_links.py
cd website
hugo server --disableFastRender
```

## Publishing Model

1. Create a new topic folder in `research/`
2. Write the paper in `index.md`
3. Keep figures in the article-local `assets/` directory
4. Cite authoritative sources directly in the article
5. Open a pull request
6. Merge to publish

## Licensing

- Code, automation, and site infrastructure: MIT
- Original research content under `research/`: CC BY 4.0

Contribution guidance is available in [CONTRIBUTING.md](./CONTRIBUTING.md).
