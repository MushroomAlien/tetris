import constants

class Board:
    """
    Manages the 2D grid state for a Tetris game.
    Grid format: 0 = empty, non-zero = piece ID colour.
    """

    def __init__(self):
        """Initialises the board grid."""
        self.rows = constants.ROWS
        self.cols = constants.COLS
        self.grid = [[0 for _ in range(constants.COLS)] for _ in range(constants.ROWS)]

    def is_valid_position(self, cells):
        """
        Checks if all given (row, col) cell coordinates are within bounds
        and currently empty on the board.
        :param cells: List of (row, col) tuples.
        :return: bool indicating validity.
        """
        for r, c in cells:
            # Check bounds
            if not (0 <= r < constants.ROWS and 0 <= c < constants.COLS):
                return False
            # Check if empty (0)
            if self.grid[r][c] != 0:
                return False
        return True

    def place_piece(self, cells, piece_id):
        """
        Sets each cell in the provided coordinates to the given piece_id.
        :param cells: List of (row, col) tuples.
        :param piece_id: The ID/colour to place in the cells.
        """
        for r, c in cells:
            self.grid[r][c] = piece_id

    def get_cell(self, row, col):
        """
        Returns the value at the specified row and column.
        :param row: The row index.
        :param col: The column index.
        :return: The cell value (0 if empty).
        """
        return self.grid[row][col]

    def clear_lines(self):
        """
        Removes any completely filled rows, shifts everything above down,
        and returns the count of lines cleared.
        :return: int count of lines cleared.
        """
        lines_cleared = 0
        new_grid = []

        # Check for filled rows (row by row)
        temp_grid = []
        for row in self.grid:
            if all(row):
                # This row is full, it will be cleared
                temp_grid.append(False)
            else:
                temp_grid.append(True)

        # Count lines cleared
        lines_cleared = sum(1 for is_cleared in temp_grid if not is_cleared)

        # Rebuild the grid: keep lines that are not cleared, and pad the top with new empty rows
        rows_to_keep = [row for i, row in enumerate(self.grid) if temp_grid[i]]
        rows_cleared_count = lines_cleared

        # The number of empty rows needed at the top is the number of cleared lines
        empty_row = [0] * constants.COLS

        # New grid is: [empty_row] * lines_cleared + rows_to_keep
        self.grid = [empty_row[:] for _ in range(rows_cleared_count)] + rows_to_keep

        return lines_cleared

# Example usage (for testing purposes, should be removed for final library file):
# if __name__ == '__main__':
#     board = Board()
#     print(f"Initial grid state:")
#     for row in board.grid:
#         print(row)
#
#     # Test placing a piece (assuming constants are available)
#     # print(f"Is valid position for (0, 0) to (2, 2)?: {board.is_valid_position([(0, 0), (1, 0), (2, 0)])}")
#     # board.place_piece([(0, 0), (1, 0), (2, 0)], 1)
#     # print(f"Grid after placement:")
#     # for row in board.grid:
#     #     print(row)
#
#     # Test line clearing (this requires manual setup or mocking constants)
#     pass