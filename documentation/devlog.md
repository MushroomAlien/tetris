# Tetris Dev Log

**Stack:** Python 3 + pygame
**Model under test:** Gemma 4 E4B via Claude Code
**Versioning:** GG.YYMM.rrrr - Odd = WIP, Even = stable

---

## 2026-04-11 22:16 — 01.2604.0001

- Project scaffolded
- Files created: constants.py tetromino.py board.py game.py renderer.py input_handler.py main.py
- Status: WIP (odd revision)

---

## 2026-04-11 — 01.2604.0002

- Created game/constants.py with grid dimensions, screen dimensions, timing, colours, and tetromino IDs
- Syntax verified: python -m py_compile game/constants.py passed with no errors
- No other files modified
- GitHub repo created: https://github.com/MushroomAlien/tetris

Next step: write game/tetromino.py

---
## 2026-04-12 — 01.2604.0004

- Written game/tetromino.py with all 7 piece shapes and rotation logic
- Fixed import from 'from game import constants' to 'import constants'
- Updated CLAUDE.md Gotchas section: read before write rule for pre-created empty files
- Syntax verified: python -m py_compile game/tetromino.py passed
- Committed and pushed to main

Next step: write game/board.py

---
