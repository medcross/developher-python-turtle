import game

BLOCK_SIZE = 50
SELECTED_MAZE = 0
(player, screen) = game.setup_maze(BLOCK_SIZE, SELECTED_MAZE)

# LIST OF POSSIBLE COMMANDS:
#
# player.turn_left()
# player.turn_right()
# player.move_forward()
# player.is_wall_ahead()
#
# WRITE CODE BELOW


# (Zur Ausführung auf dem eigenen Rechner, damit sich das Fenster nicht gleich wieder schließt)
screen.main_loop()
