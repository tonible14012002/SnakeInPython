import pygame
import random
from SnakeClass import Direction, Snake,Point

class World:

    def __init__(self,l_Graphics,Width,Height):
        self.m_Snake = Snake(3,l_Graphics)
        self.m_Graphics = l_Graphics
        self.GridX = int(Width / l_Graphics)
        self.GridY = int(Height / l_Graphics)

        self.Rect = []
        self.Rect.append([0,0,self.m_Graphics,self.m_Graphics*self.GridY])
        self.Rect.append([0,0,self.m_Graphics*self.GridX,self.m_Graphics])
        self.Rect.append([(self.GridX-1)*self.m_Graphics,0,self.m_Graphics,self.m_Graphics*self.GridY])
        self.Rect.append([0,(self.GridY-1)*self.m_Graphics,self.m_Graphics*self.GridX,self.m_Graphics])

        self.Respawn()
        self.m_Clock = pygame.time.Clock()
        self.m_Elapsed = self.m_Clock.tick()
        self.m_Font = pygame.font.Font('font/Poppins-Regular.ttf',int(l_Graphics/2))

    def Update(self):
        Passed = float(1/self.m_Snake.m_Speed)
        if self.m_Elapsed*0.001 >= Passed:
            self.m_Elapsed -= Passed*1000
            self.m_Snake.Tick()
            self.Collision()

    def Collision(self):
        X = self.m_Snake.m_Segment[0].x
        Y = self.m_Snake.m_Segment[0].y
        if X >= self.GridX - 1 or X <= 0 or\
            Y >= self.GridY - 1 or Y <= 0:
            self.m_Snake.HasLost = True
        if self.m_Snake.m_Segment[0].x == self.m_Apple.x and\
            self.m_Snake.m_Segment[0].y == self.m_Apple.y:
            self.Respawn()
            self.m_Snake.Extend()

    def Respawn(self):
        while True:
            self.m_Apple = Point(random.randint(1,self.GridX-2),\
                random.randint(1,self.GridY-2))
            Flag = False
            for Segment in self.m_Snake.m_Segment:
                if self.m_Apple.x == Segment.x and\
                    self.m_Apple.y == Segment.y:
                    Flag = True
            if Flag: 
                continue
            break

    def Render(self,Surface):
        BROWN = (135, 76, 14)
        for Each in self.Rect:
            pygame.draw.rect(Surface,BROWN,Each)
        RED = (191, 57, 42)
        pygame.draw.circle(Surface,RED,((self.m_Apple.x+0.5)*self.m_Graphics,\
            (self.m_Apple.y+0.5)*self.m_Graphics),self.m_Graphics/2)
        self.m_Snake.Render(Surface)
        String = 'Lives: ' + str(self.m_Snake.m_Lives)
        Text = self.m_Font.render(String,True,(255, 255, 255))
        TextRect = Text.get_rect()
        TextRect.center = (self.GridX*self.m_Graphics/2,self.m_Graphics/2)
        Surface.blit(Text,TextRect)

    def SetSnakeDirection(self,l_Direction):
        self.m_Snake.m_Direction = l_Direction
    
    def CurrentDir(self):
        return self.m_Snake.m_Direction
    
    def ResetClock(self):
        self.m_Elapsed += self.m_Clock.tick()
    
    def Restart(self):
        self.m_Snake.Reset(3)
        self.Respawn()
