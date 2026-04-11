# Tetris Clone — Project CLAUDE.md

## What We Are Building
Standard Tetris clone. Python 3 + pygame. No novel mechanics. Small scope.
Core gameplay first. Optional features only after core is solid and tested.

## File Locations
- Game source: `game/`
- Documentation: `documentation/`
- Devlog: `documentation/devlog.md`

## Commands
- Run game: `python game/main.py`
- Check syntax: `python -m py_compile game/<file>.py`
- Install deps: `pip install pygame`

## Architecture — Read This First
```
main.py → game.py → board.py
                  → tetromino.py
                  → input_handler.py
                  → renderer.py
                  → constants.py (imported by everything)
```
- `constants.py` — magic numbers only, no logic
- `board.py` — grid state and line clears only, no pygame
- `tetromino.py` — piece shapes and rotation only
- `renderer.py` — all pygame drawing, no game logic
- `input_handler.py` — pygame events to actions only
- `game.py` — coordinator only, no drawing
- `main.py` — entry point only, under 30 lines

## Conventions
- Files stay under 100 lines. Flag if approaching limit.
- One job per file. Do not let responsibilities bleed across files.
- All magic numbers go in constants.py. Never hardcode values elsewhere.
- No pygame imports outside renderer.py and main.py.
- No game logic in renderer.py.

## Do Not
- DO NOT add features that were not requested
- DO NOT modify more than one file per task unless explicitly told to
- DO NOT delete or overwrite anything in documentation/devlog.md — append only
- DO NOT add new files without asking first
- DO NOT over-engineer. Match the simplest solution that works.
- DO NOT import across layers (e.g. renderer must not import from board directly)

## End of Every Session — Mandatory Steps
Do these in order. Do not skip. Do not combine into one message.

### 1. Append to devlog
Open `documentation/devlog.md` and append a new entry at the bottom:

```
## YYYY-MM-DD HH:MM — <version>

- What was built or changed
- What was tested and result
- Any known issues
- Next step

---
```

Rules:
- APPEND ONLY. Never edit, delete, or rewrite existing devlog content.
- If the file does not exist, create it. If it exists, only add to the end.

### 2. Git commit and push
Run these commands in order:

```bash
git add .
git commit -m "<short description of what was done this session>"
git push
```

Commit message should be specific. Not "update" or "changes". Example:
`"Add board.py with grid state and line clear logic"`

## Compact Instructions
Preserve: current task, which file is being worked on, any failing errors,
architecture decisions made this session.

## Gotchas
- Work on one file at a time. Ask for the file content if you need it.
- If a task spans two files, do them in separate steps.
- python -m py_compile is your friend. Run it after every file change.
- pygame.init() only in main.py. Never call it elsewhere.
- All project files are pre-created empty. Always read a file before writing to it,
  even if you expect it to be empty. The Write tool requires a prior Read on any
  existing file or it will error.
