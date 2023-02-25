from abc import ABC, abstractmethod
import pygame

#-------------------------------------------------#
class Player(ABC):
  def __init__(self,boardValue):
    self.boardValue = boardValue
    
  @abstractmethod
  def makeMove(self,moveInfo=None):
    pass

#-------------------------------------------------#
class Human(Player):
  def makeMove(self,moveInfo=None):
    #check for collisions
    squareLength = 95
    factor = 104

    gridColliders = []
    for j in range(0,3):
      for i in range(0,3):
        x, y = 50 + i * factor, 48 + j * factor
        collider = pygame.Rect(x, y, squareLength, squareLength)
        gridColliders.append(collider)

    if moveInfo.click == True:
        mx,my = pygame.mouse.get_pos()
        for i in range(0,len(gridColliders)):
          collider = gridColliders[i]
          if collider.collidepoint((mx, my)):
                return MoveResults(True,i)
    return MoveResults(False)

#-------------------------------------------------#
class RandomAI(Player):
  def makeMove(self,moveInfo=None):
    return MoveResults(False)

#-------------------------------------------------#
class NeuralNetwork(Player):
  def makeMove(self,moveInfo=None):
    return MoveResults()


#-------------------------------------------------#
class MoveInfo:
  def __init__(self,click):
    self.click = click

#-------------------------------------------------#
class MoveResults:

  def __init__(self,isDoneMoving,moveSpace=-1):
    self.isDoneMoving = isDoneMoving
    self.moveSpace = moveSpace