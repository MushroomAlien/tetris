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

# Tetromino Identifiers
ID_I = 0
ID_O = 1
ID_T = 2
ID_S = 3
ID_Z = 4
ID_J = 5
ID_L = 6

# Dictionary mapping IDs to colors for easier lookup elsewhere
TETROMINO_COLORS = {
    ID_I: COLOR_I,
    ID_O: COLOR_O,
    ID_T: COLOR_T,
    ID_S: COLOR_S,
    ID_Z: COLOR_Z,
    ID_J: COLOR_J,
    ID_L: COLOR_L,
}

# --- Input/Action Constants (Copied from input_handler.py) ---
ACTION_NONE = 0
ACTION_MOVE_LEFT = 1
ACTION_MOVE_RIGHT = 2
ACTION_ROTATE = 3
ACTION_SOFT_DROP = 4
ACTION_HARD_DROP = 5
ACTION_QUIT = 6