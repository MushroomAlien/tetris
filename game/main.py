import pygame
import constants
import game
import renderer
import input_handler

def main():
    """
    Entry point for the Tetris game. Initializes Pygame, sets up components,
    and runs the main game loop according to module separation rules.
    """
    pygame.init()

    # 3. Create the screen
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    pygame.display.set_caption("Tetris Clone")

    # 4. Create one instance each of Game, Renderer, and InputHandler
    game_instance = game.Game()
    renderer_instance = renderer.Renderer(screen)
    # No instantiation for input_handler, we call the module function directly.

    # 5. Create one pygame.time.Clock instance before the loop
    clock = pygame.time.Clock()

    print("--- Game loop starting ---")

    running = True
    while running:
        # 6.a. Gets actions from InputHandler (Corrected: calling the module function)
        actions = input_handler.handle_events()

        # Check for quit signal first (Using the constant reference)
        if constants.ACTION_QUIT in actions:
            running = False
            continue

        # 6.b. Passes each action to game.handle_action(action)
        for action in actions:
            game_instance.handle_action(action)

        # 6.c. Calls game.update()
        game_instance.update()

        # 6.d. Calls the renderer draw methods
        renderer_instance.draw_background()
        renderer_instance.draw_board(game_instance.board)
        renderer_instance.draw_piece(game_instance.get_current_cells(), game_instance.piece_id)

        # 6.e. Calls renderer.refresh()
        renderer_instance.refresh()

        # 6.f. Calls clock.tick(constants.FPS)
        clock.tick(constants.FPS)

    # 7. Call pygame.quit() when the loop ends
    pygame.quit()
    print("--- Game loop ended and Pygame quit ---")

if __name__ == "__main__":
    main()