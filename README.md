# marimo Hello World — Starter Template

> **New to marimo?** This is the right place to start. Fork this repo, run one command, and you'll have an interactive Python notebook running in your browser in under a minute.

## What is marimo?

[marimo](https://marimo.io) is a modern Python notebook where:

- Cells **re-execute automatically** when their inputs change — no stale output, no manual re-runs
- UI widgets (sliders, dropdowns, tables) are **plain Python objects** — bind them to variables and everything just works
- The notebook is stored as a **`.py` file** — works with git, diffs cleanly, and opens in any editor
- Execution follows **data flow**, not cell position — hidden state is impossible

## Step 1 — Fork this repository

Click **Fork** in the top-right corner of this page on GitHub. This creates your own copy where you can freely experiment.

Then clone your fork:

```bash
git clone https://github.com/<your-username>/marimo-uv-starter-template
cd marimo-uv-starter-template
```

## Step 2 — Install uv

[uv](https://docs.astral.sh/uv/) is a fast Python package manager. It handles the Python version and all dependencies for you — no `pip install`, no virtual environment setup.

**macOS / Linux:**

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

**Windows (PowerShell):**

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

Verify the installation:

```bash
uv --version
```

## Step 3 — Run the Hello World notebook

```bash
cd notebooks
uv run marimo edit altair-demo.py
```

That's it. `uv` installs all required packages automatically on first run, then opens the notebook in your browser.

### What you will see

The notebook walks through three core marimo concepts:

| Section | What it shows |
|---|---|
| **1 · Markdown cells** | Render formatted text, lists, and LaTeX with `mo.md()` |
| **2 · Reactive UI elements** | A slider whose value is instantly reflected in another cell |
| **3 · Interactive Altair charts** | Click-and-drag selection on a scatter plot that filters a table and histograms in real time |

> **Tip:** Try editing a cell directly in the browser editor. marimo re-runs only the cells affected by your change.

## Project structure

```
notebooks/
    altair-demo.py   ← Hello World notebook (start here)
    notebook.py      ← Blank notebook template
    app.py           ← Example app layout
src/
    utils.py         ← Shared Python helpers
tests/
    test_sample.py   ← pytest test suite
pyproject.toml       ← Project config & dependencies
```

## Running the notebook as a read-only app

```bash
cd notebooks
uv run marimo run altair-demo.py
```

Use `run` instead of `edit` to launch a clean, non-editable view — useful for sharing with others.

## Development commands

```bash
# Run all tests
uv run pytest tests

# Lint and format
uv run ruff check .
uv run ruff format .
```

## Next steps

- Edit `notebooks/altair-demo.py` to experiment with your own data
- Add new notebooks to the `notebooks/` folder
- Put reusable Python functions in `src/utils.py` and import them in your notebooks
- Read the [marimo docs](https://docs.marimo.io) to explore more UI elements and layouts

## License

MIT
