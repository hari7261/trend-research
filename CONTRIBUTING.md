# Contributing

Trend Research accepts contributions for research requests, article revisions, source improvements, visual assets, and publishing infrastructure.

## What Good Contributions Look Like

- Narrow, well-scoped pull requests
- Claims supported by primary or authoritative secondary sources
- Writing that is precise, grammatical, and easy to audit
- Diagrams that clarify system behavior rather than decorate the page
- Stable, topic-based slugs with no dates in directory names

## Research Writing Standard

Each article should read like a professional technical paper:

- Use an abstract or introduction that states the problem clearly
- Separate evidence, synthesis, and design recommendations
- Define terminology before using it heavily
- Prefer references to papers, official documentation, standards, and benchmark reports
- Include direct reference links in the article
- Update the `updated` field whenever substantial content changes

## Structure

Create new research under:

```text
research/<topic-slug>/
  index.md
  assets/
```

## Figures and Tables

- Prefer transparent SVG for architecture diagrams and flow charts
- Keep labels short and technically accurate
- Use tables when comparisons or tradeoffs matter
- Do not embed screenshots when a vector diagram communicates the point more clearly

## Validation

Run the repository checks before opening a pull request:

```bash
python scripts/validate_links.py
cd website
hugo --minify
```

## Licensing

By contributing:

- code and infrastructure contributions are licensed under MIT
- research content under `research/` is licensed under CC BY 4.0 unless a file states otherwise

## Review Expectations

- Summarize the change in one paragraph
- List any new references added
- Call out unresolved claims or assumptions
- Confirm local validation was completed
