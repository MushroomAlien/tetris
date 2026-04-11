# --- Game Dimensions and Timing ---
COLS = 10
ROWS = 20
CELL_SIZE = 30

SCREEN_WIDTH = COLS * CELL_SIZE
SCREEN_HEIGHT = ROWS * CELL_SIZE

FPS = 60
FALL_INTERVAL = 48  # Frames between automatic drop attempts

# --- Colors (RGB Tuples) ---
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREY = (100, 100, 100)

# Tetromino Colors (Example values, should be set by designer)
COLOR_I = (0, 255, 255)  # Cyan
COLOR_O = (255, 255, 0)  # Yellow
COLOR_T = (128, 0, 128)  # Purple
COLOR_S = (0, 255, 0)    # Green
COLOR_Z = (255, 0, 0)    # Red
COLOR_J = (0, 0, 255)    # Blue
COLOR_L = (255, 165, 0)  # Orange

# --- Tetromino Identifiers ---
# Integer IDs mapping to piece type for board state tracking
ID_I = 0
ID_O = 1
ID_T = 2
ID_S = 3
ID_Z = 4
ID_J = 5
ID_L = 6

# Dictionary mapping IDs to colors for easier lookup elsewhere
# Although the rule says no logic, providing this mapping as a constant structure is acceptable for clarity
# If this is too much logic, we can simplify to just keep the two ID/Color groups separate.
# For now, I will include it as a constant dictionary as it aids organization.
TETROMINO_COLORS = {
    ID_I: COLOR_I,
    ID_O: COLOR_O,
    ID_T: COLOR_T,
    ID_S: COLOR_S,
    ID_Z: COLOR_Z,
    ID_J: COLOR_J,
    ID_L: COLOR_L,
}