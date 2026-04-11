import pygame
import constants

class Renderer:
    def __init__(self, screen):
        self.screen = screen

    def draw_background(self):
        self.screen.fill(constants.BLACK)

    def draw_board(self, board):
        for row in range(board.rows):
            for col in range(board.cols):
                color = constants.TETROMINO_COLORS.get(board.grid[row][col], constants.BLACK)
                if color != constants.BLACK:
                    pygame.draw.rect(self.screen, color, (col * constants.CELL_SIZE, row * constants.CELL_SIZE, constants.CELL_SIZE, constants.CELL_SIZE), 0)
                    pygame.draw.rect(self.screen, (100, 100, 100), (col * constants.CELL_SIZE, row * constants.CELL_SIZE, constants.CELL_SIZE, constants.CELL_SIZE), 1)

    def draw_piece(self, cells, piece_id):
        # Note: The logic for piece_id usage is assumed to be handled by passing the correct color mapping based on the piece's identity/color.
        # Assuming 'cells' is a list of (row, col) tuples for the piece's current state.
        # We use a placeholder color lookup here as the exact piece_id usage isn't fully defined for color retrieval.
        # For simplicity, we'll draw all points with a consistent color if piece_id isn't directly used for color lookup like in draw_board.
        # Based on the prompt, we'll use the piece_id to look up a color, assuming it maps correctly.
        piece_color = constants.TETROMINO_COLORS.get(piece_id, (255, 255, 255)) # Fallback white
        for row, col in cells:
            pygame.draw.rect(self.screen, piece_color, (col * constants.CELL_SIZE, row * constants.CELL_SIZE, constants.CELL_SIZE, constants.CELL_SIZE))
            pygame.draw.rect(self.screen, (100, 100, 100), (col * constants.CELL_SIZE, row * constants.CELL_SIZE, constants.CELL_SIZE, constants.CELL_SIZE), 1)

    def refresh(self):
        pygame.display.flip()