import pygame

# Action Constants
ACTION_NONE = 0
ACTION_MOVE_LEFT = 1
ACTION_MOVE_RIGHT = 2
ACTION_ROTATE = 3
ACTION_SOFT_DROP = 4
ACTION_HARD_DROP = 5
ACTION_QUIT = 6

def handle_events():
    """
    Processes Pygame events and translates them into abstract game actions.
    Reads events directly from pygame.event.get().
    Returns a list of action constants.
    """
    events = pygame.event.get()
    actions = []
    for event in events:
        if event.type == pygame.QUIT:
            actions.append(ACTION_QUIT)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                actions.append(ACTION_MOVE_LEFT)
            elif event.key == pygame.K_RIGHT:
                actions.append(ACTION_MOVE_RIGHT)
            elif event.key == pygame.K_UP:
                actions.append(ACTION_ROTATE)
            elif event.key == pygame.K_DOWN:
                actions.append(ACTION_SOFT_DROP)
            elif event.key == pygame.K_SPACE:
                actions.append(ACTION_HARD_DROP)
    return actions