import random
import constants
import board
import tetromino

class Game:
    def __init__(self):
        self.board = board.Board()
        self.frame_counter = 0
        self.score = 0
        self.running = True
        self.spawn_piece()

    def spawn_piece(self):
        piece_ids = [constants.ID_I, constants.ID_O, constants.ID_T, constants.ID_S, constants.ID_Z, constants.ID_J, constants.ID_L]
        self.piece_id = random.choice(piece_ids)
        self.rotation = 0
        self.col = constants.COLS // 2 - 1
        self.row = 0

    def get_current_cells(self):
        return [(self.row + dr, self.col + dc) for dr, dc in tetromino.get_shape(self.piece_id, self.rotation)]

    def update(self):
        self.frame_counter += 1
        if self.frame_counter >= constants.FALL_INTERVAL:
            self.frame_counter = 0
            self.row += 1