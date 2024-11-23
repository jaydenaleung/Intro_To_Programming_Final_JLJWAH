import pygame


class Entity:
    def __init__(self,x,y,imagePath,speed):
        self.x = x
        self.y = y
        self.image = pygame.image.load(imagePath)
        self.speed = speed
        self.movingLeft = False
        self.movingRight = False
        self.movingUp = False
        self.movingDown = False

class Player(Entity):
    def __init__(self,x,y,imagePath):
        super().__init__(x,y,imagePath,5.0)
        
    def update(self,surface):
        surface.blit(self.image, (self.x, self.y))

class Enemy(Entity):
    def __init__(self,x,y,imagePath):
        super().__init__(x,y,imagePath,2.5)
        
    def update(self,surface):
        surface.blit(self.image, (self.x, self.y))

class Scene:
    def __init__(self, imagePath, *coords: tuple[int,int,int,int]):
        self.image = pygame.image.load(imagePath)
        
        for index in coords:
            self.x1 = coords[0]
            self.y1 = coords[1]
            self.x2 = coords[2]
            self.y2 = coords[3]