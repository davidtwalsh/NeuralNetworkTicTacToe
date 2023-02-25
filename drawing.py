import pygame
from colors import Color
from boardValues import BoardValues

def draw_grid(screen):
  lineLength = 300
  lineWidth = 10
  offset = 100

  horizontalXStart = 50
  horizontalYStart = 150

  verticalXStart = 150
  verticalYStart = 50

  #draw lines
  for i in range(0,2):
      #horizontal lines
      pygame.draw.line(screen, Color.BLACK, [horizontalXStart,horizontalYStart + offset * i], [horizontalXStart + lineLength, horizontalYStart + offset * i], lineWidth)
      #vertical lines
      pygame.draw.line(screen, Color.BLACK, [verticalXStart + offset * i,verticalYStart], [verticalXStart + offset * i, verticalYStart + lineLength], lineWidth)

def draw_collision_markers(screen):
  squareLength = 95
  factor = 104

  for i in range(0,3):
    for j in range(0,3):
      x, y = 50 + i * factor, 48 + j * factor
      pygame.draw.rect(screen, Color.RED, pygame.Rect(x, y, squareLength, squareLength))

def draw_moveSymbols(screen,grid):
  drawX(screen,40,40)

def drawX(screen,x,y):
  pygame.draw.line(screen, Color.BLACK, [x,y],[x+60,y+60],8)
