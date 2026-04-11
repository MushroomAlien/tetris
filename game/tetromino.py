"""
Defines the shapes and rotations for all 7 Tetromino pieces.

This module contains only static data and pure geometric functions.
It must not contain any game logic, Pygame imports, or state management.
"""
from typing import List, Tuple, Dict

# Import piece IDs from constants.py to ensure consistency
import constants

# Type alias for clarity
Shape = List[Tuple[int, int]] # List of (row, col) offsets

# --- SHAPE DEFINITIONS ---
# Each piece_id maps to a list of all its unique rotation states.
# Each rotation state is a list of (row, col) offsets relative to the pivot point.
# The order in the list defines the rotations (0, 1, 2, ...).

TETROMINO_SHAPES: Dict[int, List[Shape]] = {
    constants.ID_I: [
        [(0, 0), (0, 1), (0, 2), (0, 3)], # Rotation 0: Horizontal
        [(0, 0), (1, 0), (2, 0), (3, 0)], # Rotation 1: Vertical
    ],
    constants.ID_O: [
        # Always a 2x2 square, only one unique rotation
        [(0, 0), (0, 1), (1, 0), (1, 1)],
    ],
    constants.ID_T: [
        # Rotation 0: T-shape upright
        [(0, 1), (1, 0), (1, 1), (1, 2)],
        # Rotation 1: T-shape rotated 90 degrees
        [(0, 0), (1, 0), (2, 0), (1, 1)],
    ],
    constants.ID_S: [
        # Rotation 0
        [(0, 1), (0, 2), (1, 0), (1, 1)],
        # Rotation 1
        [(0, 0), (1, 0), (1, 1), (2, 1)],
    ],
    constants.ID_Z: [
        # Rotation 0
        [(0, 0), (0, 1), (1, 1), (1, 2)],
        # Rotation 1
        [(0, 1), (1, 0), (1, 1), (2, 0)],
    ],
    constants.ID_J: [
        # Rotation 0 (Left hook base)
        [(0, 0), (1, 0), (2, 0), (2, 1)],
        # Rotation 1 (L-shape pointing right/down)
        [(0, 1), (1, 1), (2, 1), (2, 0)],
    ],
    constants.ID_L: [
        # Rotation 0 (Horizontal bar base)
        [(0, 0), (0, 1), (0, 2), (1, 2)],
        # Rotation 1 (Vertical bar base)
        [(0, 2), (1, 2), (2, 2), (2, 1)]
    ],
}

# --- FUNCTIONS ---

def get_shape(piece_id: int, rotation: int) -> Shape:
    """
    Retrieves the (row, col) coordinates for a specific tetromino shape.

    Args:
        piece_id: The ID of the tetromino (from constants.py).
        rotation: The rotation index (0, 1, 2, ...).

    Returns:
        A list of (row, col) tuples representing the shape, or an empty list
        if the piece_id or rotation is invalid.
    """
    if piece_id not in TETROMINO_SHAPES:
        return []

    shapes = TETROMINO_SHAPES[piece_id]
    if 0 <= rotation < len(shapes):
        return shapes[rotation]
    return []

def next_rotation(rotation: int, piece_id: int) -> int:
    """
    Calculates the next rotation index for a given piece.

    Args:
        rotation: The current rotation index.
        piece_id: The ID of the tetromino.

    Returns:
        The next rotation index, wrapping around to 0 if at the end.
    """
    if piece_id not in TETROMINO_SHAPES:
        return -1

    shapes = TETROMINO_SHAPES[piece_id]
    num_rotations = len(shapes)
    if num_rotations == 0:
        return -1

    return (rotation + 1) % num_rotations

# Example usage check (purely for validation, should not be run by users)
# print(f"I shape, rotation 0: {get_shape(constants.ID_I, 0)}")
# print(f"T shape next rotation: {next_rotation(0, constants.ID_T)}")
