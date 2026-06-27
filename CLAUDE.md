# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

**Spendly** is a Flask-based expense tracking web application. It is a student learning project with placeholder routes that students implement in steps.

## Commands

```bash
# Run the development server
python app.py

# Run tests
pytest

# Run a single test file
pytest tests/test_filename.py

# Run tests with verbose output
pytest -v
```

The app runs on port 5001 with `debug=True` by default.

## Architecture

- **app.py**: Main Flask application with all routes. Routes marked as "Placeholder routes — students will implement these" are the exercises.
- **database/db.py**: Empty placeholder where students implement database functions (`get_db()`, `init_db()`, `seed_db()`).
- **templates/**: Jinja2 HTML templates extending `base.html`
- **static/css/style.css**: Single CSS file with design system variables and all component styles
- **static/js/main.js**: Client-side JavaScript

## Database Structure

SQLite is used. The `database/db.py` file should export:
- `get_db()` — returns SQLite connection with row_factory and foreign keys enabled
- `init_db()` — creates tables with `CREATE TABLE IF NOT EXISTS`
- `seed_db()` — inserts sample development data

## Routes

| Route | Status |
|-------|--------|
| `/` | Landing page |
| `/register` | Registration page |
| `/login` | Login page |
| `/terms` | Terms and conditions |
| `/logout`, `/profile`, `/expenses/add`, `/expenses/<id>/edit`, `/expenses/<id>/delete` | Placeholder routes for student implementation |

## Design System

The CSS uses CSS custom properties for theming:
- `--ink-*`: Text colors (dark to light)
- `--paper-*`: Background colors
- `--accent`: Primary green (#1a472a)
- `--accent-2`: Secondary gold (#c17f24)
- `--font-display`: DM Serif Display (headings)
- `--font-body`: DM Sans (body text)