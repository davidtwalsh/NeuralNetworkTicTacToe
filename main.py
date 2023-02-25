import pygame
from boardValues import BoardValues
from player import Human, RandomAI, NeuralNetwork, MoveInfo
from colors import Color
import drawing
from mode import Mode


pygame.init()

# Open a new window
size = (960, 540)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Neural Network TicTacToe")

# The loop will carry on until the user exits the game (e.g. clicks the close button).
carryOn = True

# The clock will be used to control how fast the screen updates
clock = pygame.time.Clock()
click = False

grid = [-1 for i in range(0,9)]

gameMode = Mode.HUMANVSRANDOMAI
if gameMode == Mode.HUMANVSRANDOMAI:
  playerOne = Human(BoardValues.Xs)
  playerTwo = RandomAI(BoardValues.Zeros)

currentPlayerMoving = playerOne

# -------- Main Program Loop -----------
while carryOn:
    # --- Main event loop
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
              carryOn = False # Flag that we are done so we can exit the while loop

        if event.type == pygame.MOUSEBUTTONDOWN:
          if event.button == 1:
            click = True


    #conduct player moves
    moveInfo = MoveInfo(click)
    moveResults = currentPlayerMoving.makeMove(moveInfo)
    if moveResults.isDoneMoving == True:
      grid[moveResults.moveSpace] = currentPlayerMoving.boardValue
      if currentPlayerMoving == playerOne:
        currentPlayerMoving = playerTwo
      else:
        currentPlayerMoving = playerOne

    #check win condition


    # --- Drawing code should go here
    # First, clear the screen to white. 
    screen.fill(Color.WHITE)
    #drawing.draw_collision_markers(screen)
    drawing.draw_grid(screen)
    drawing.draw_moveSymbols(screen,grid)


    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    click = False

    # --- Limit to 60 frames per second
    clock.tick(60)

#Once we have exited the main program loop we can stop the game engine:
pygame.quit()