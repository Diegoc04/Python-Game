import pygame
import Mapa_Zelda

class Link(pygame.sprite.Sprite):
    def __init__(self, pos, groups, obstaculos):
        super().__init__(groups)

        self.image = pygame.image.load("Link.png")
        self.rect = self.image.get_rect(topleft = pos)

        self.direction = pygame.math.Vector2()
        self.velocity = 5

        self.Obstaculos = obstaculos

    def teclado(self): 
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]:
            self.direction.y = -1

        elif keys[pygame.K_DOWN]:
            self.direction.y = 1

        else:
            self.direction.y = 0

        if keys[pygame.K_RIGHT]:
            self.direction.x = 1

        elif keys[pygame.K_LEFT]:
            self.direction.x = -1

        else:
            self.direction.x = 0 

    def mover(self, velocity):
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()

        self.rect.x += self.direction.x * velocity
        self.coliciones("horizontal")

        self.rect.y += self.direction.y * velocity
        self.coliciones("vertical")

    def coliciones(self, direction):
        if direction == "horizontal":
            for sprite in self.Obstaculos:
                if sprite.rect.colliderect(self.rect):
                    if self.direction.x > 0:
                        self.rect.right = sprite.rect.left

                    if self.direction.x < 0:
                        self.rect.left = sprite.rect.right    

        if direction == "vertical":
            for sprite in self.Obstaculos:
                if sprite.rect.colliderect(self.rect):
                    if self.direction.y > 0:
                        self.rect.bottom = sprite.rect.top

                    if self.direction.y < 0:
                        self.rect.top = sprite.rect.bottom


    def update(self): 
        self.teclado()   
        self.mover(self.velocity)
        