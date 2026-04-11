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

## 2026-04-12 — 01.2604.0006

- Written game/board.py with Board class
- Methods: __init__, is_valid_position, place_piece, clear_lines, get_cell
- No pygame imports, no game logic, grid state only
- Syntax verified: python -m py_compile game/board.py passed
- Committed and pushed to main

Next step: write game/input_handler.py

---

## 2026-04-12 — 01.2604.0008

- Written game/input_handler.py with InputHandler class
- Translates pygame events to abstract actions (MOVE_LEFT, MOVE_RIGHT, MOVE_DOWN, ROTATE, QUIT)
- Syntax verified: python -m py_compile game/input_handler.py passed
- Committed and pushed to main

Next step: write game/renderer.py

---