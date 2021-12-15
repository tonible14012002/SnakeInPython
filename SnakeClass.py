import pygame
from enum import Enum

class Direction(Enum):
    Up = 1
    Down = 2
    Left = 3
    Right = 4
    Stand = 5


class Point:

    def __init__(self,x = 0,y = 0):
        self.x = x
        self.y = y

class Snake:

    def __init__(self,Len = 7,l_GraphicSize = 20,l_Speed = 10,l_Lives = 5):
        #Graphic Size initialization
        self.m_GraphicSize = l_GraphicSize
        self.Reset(Len,l_Speed,l_Lives)

    def Reset(self,Len=3,l_Speed=10,l_Lives=5):

        self.m_Segment = []
        for i in range(Len,0,-1):
            self.m_Segment.append(Point(i,1))
        #Initialize Direction
        self.m_Direction = Direction.Stand
        self.m_Speed = l_Speed
        self.m_Lives = l_Lives
        self.HasLost = False

    def Extend(self):

        Tail = len(self.m_Segment)-1
        Spain = Tail - 1
        NewSegment = Point(self.m_Segment[Tail].x, self.m_Segment[Tail].y)
        if (self.m_Segment[Spain].x - self.m_Segment[Tail].x) > 0:
            NewSegment.x = self.m_Segment[Tail].x-1
        elif (self.m_Segment[Spain].x - self.m_Segment[Tail].x) < 0:
            NewSegment.x =  self.m_Segment[Tail].x+1
        elif (self.m_Segment[Spain].y - self.m_Segment[Tail].y) < 0:
            NewSegment.y = self.m_Segment[Tail].y + 1
        elif (self.m_Segment[Spain].y - self.m_Segment[Tail].y) > 0:
            NewSegment.y = self.m_Segment[Tail].y - 1
        self.m_Segment.append(NewSegment)

    def Move(self):

        if self.m_Direction == Direction.Stand:
            return
            
        n = len(self.m_Segment) - 1
        for i in range(n,0,-1):
            self.m_Segment[i].x = self.m_Segment[i-1].x
            self.m_Segment[i].y = self.m_Segment[i-1].y

        if self.m_Direction == Direction.Right:
            self.m_Segment[0].x += 1
        elif self.m_Direction == Direction.Up:
            self.m_Segment[0].y -= 1
        elif self.m_Direction == Direction.Left:
            self.m_Segment[0].x -= 1
        elif self.m_Direction == Direction.Down:
            self.m_Segment[0].y += 1

    def Render(self, Surface):

        Graphic = self.m_GraphicSize
        GREEN = (47, 168, 77)
        YELLOW = (226, 232, 102)
        for Segment in self.m_Segment:    
            Rect = [Segment.x*Graphic, Segment.y*Graphic,Graphic,Graphic]
            pygame.draw.rect(Surface,GREEN,Rect)
        Rect = [self.m_Segment[0].x*Graphic, self.m_Segment[0].y*Graphic,Graphic,Graphic]
        pygame.draw.rect(Surface,YELLOW,Rect)

    def Tick(self):
        if self.HasLost == True:
            self.m_Direction = Direction.Stand
        self.Move()
        self.CheckCollision()

    def CheckCollision(self):
        n = len(self.m_Segment)
        for i in range(3,n):
            if self.m_Segment[i].x == self.m_Segment[0].x and\
                self.m_Segment[i].y == self.m_Segment[0].y:
                self.m_Lives -= 1
                self.Cut(i,n)
                break
        if self.m_Lives == 0:
            self.HasLost = True

    def Cut(self,Colli_Pos,len):
        #Cut the Snake, --Lives
        for i in range(Colli_Pos,len):
            self.m_Segment.pop(Colli_Pos)
        

