import input_handler
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

    def update(self, actions):
        # 1. Process each action
        for action in actions:
            if action == "ACTION_MOVE_LEFT":
                self.col -= 1
                if not self.board.is_valid_position(self.get_current_cells()):
                    self.col += 1
            elif action == "ACTION_MOVE_RIGHT":
                self.col += 1
                if not self.board.is_valid_position(self.get_current_cells()):
                    self.col -= 1
            elif action == "ACTION_ROTATE":
                old = self.rotation
                self.rotation = tetromino.next_rotation(self.rotation, self.piece_id)
                if not self.board.is_valid_position(self.get_current_cells()):
                    self.rotation = old
            elif action == "ACTION_SOFT_DROP":
                self.row += 1
                if not self.board.is_valid_position(self.get_current_cells()):
                    self.row -= 1
            elif action == "ACTION_HARD_DROP":
                while self.board.is_valid_position(self.get_current_cells()):
                    self.row += 1
                self.row -= 1
            elif action == "ACTION_QUIT":
                self.running = False

        # 2. Handle gravity
        self.frame_counter += 1
        if self.frame_counter >= constants.FALL_INTERVAL:
            self.frame_counter = 0
            self.row += 1
            if not self.board.is_valid_position(self.get_current_cells()):
                self.row -= 1
                self.board.place_piece(self.get_current_cells(), self.piece_id)
                cleared = self.board.clear_lines()
                self.score += cleared * 10
                self.spawn_piece()
                if not self.board.is_valid_position(self.get_current_cells()):
                    self.running = False

    def get_current_cells(self):
        return [(self.row + dr, self.col + dc) for dr, dc in tetromino.get_shape(self.piece_id, self.rotation)]