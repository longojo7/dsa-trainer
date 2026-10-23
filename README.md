# DSA Trainer

A study tool for data-structures-and-algorithms interviews, built around **recognizing the pattern**
and then writing the solution yourself.

**Milestone 1 (done):** a static cheat sheet of 20 core patterns. Each one has recognition signals,
the key idea, pitfalls, a **pytest-verified Python template**, and practice problems ordered easy → hard.

**Coming next:** flashcards with saved progress (spaced repetition), a hint-ladder AI tutor
(FastAPI + Claude API), Docker Compose, then cloud deployment.

## Project layout

```
content/                 ← the cheat sheet itself — edit this, not the frontend
  patterns/<slug>/
    pattern.md           frontmatter (title, signals, complexity, problems) + Markdown body
    template.py          real Python, imported by the tests
  guides/*.md            "How to Pick a Pattern", "Python Interview Toolkit"
  tests/                 pytest suite — every template must pass
frontend/                React + TypeScript + Vite site that renders /content at build time
```

## Run it locally

```bash
cd frontend
npm install
npm run dev          # http://localhost:5173 (hot-reloads when you edit /content)
```

## Tests

```bash
pip install pytest
pytest content/tests          # are the Python templates correct?
cd frontend && npm test       # is every pattern.md complete and well-formed?
```

Both run in GitHub Actions on every push (`.github/workflows/ci.yml`).

## Adding a pattern

1. Create `content/patterns/<new-slug>/pattern.md` — copy an existing one for the frontmatter shape.
   `category` must be one of `CATEGORY_ORDER` in `frontend/src/lib/content.ts`.
   Must include a `## Key idea` section.
2. Write `content/patterns/<new-slug>/template.py`.
3. Add `test_<new_slug>` in `content/tests/test_templates.py` (a test fails if you forget).
4. Run both test suites. The site picks the pattern up automatically — no frontend changes.

> YAML tip: if a list item **starts** with a quote but has more text after it, wrap the whole line
> in single quotes: `- '"At most K" distinct'`.
