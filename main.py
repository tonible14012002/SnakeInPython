import pygame
from pygame.time import Clock
from SnakeClass import Direction, Snake
from WorldClass import World


#setting up the game
pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
#Create Screen
Screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
IsDone = False

#timer
MyWorld = World(25,SCREEN_WIDTH,SCREEN_HEIGHT)

while not IsDone:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.display.quit()
            IsDone = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and MyWorld.CurrentDir() != Direction.Right:
                MyWorld.SetSnakeDirection(Direction.Left)
            if event.key == pygame.K_RIGHT and MyWorld.CurrentDir() != Direction.Left:
                MyWorld.SetSnakeDirection(Direction.Right)
            if event.key == pygame.K_UP and MyWorld.CurrentDir() != Direction.Down:
                MyWorld.SetSnakeDirection(Direction.Up)
            if event.key == pygame.K_DOWN and MyWorld.CurrentDir() != Direction.Up:
                MyWorld.SetSnakeDirection(Direction.Down)                
            if event.key == pygame.K_ESCAPE:
                MyWorld.SetSnakeDirection(Direction.Stand) 
            if event.key == pygame.K_SPACE:
                MyWorld.Restart()

    MyWorld.Update()

    Screen.fill((0,0,0))
    MyWorld.Render(Screen)
    pygame.display.flip()

    MyWorld.ResetClock()