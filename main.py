import math
import pygame
from pytmx.util_pygame import load_pygame
import csv
import pytmx
from pygame.locals import *
import maploader
from maploader import *


WIN_WIDTH = 640
WIN_HEIGHT = 640

class Sprite(pygame.sprite.Sprite):
    def __init__(self,x,y,image):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Player(pygame.sprite.Sprite):
    def __init__(self,x,y,image):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def checkKeys(self):
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if (event.key == K_LEFT):
                    self.rect.x-=32
                if (event.key == K_RIGHT):
                    self.rect.x+=32
                if (event.key == K_DOWN):
                    self.rect.y+=32
                if (event.key == K_UP):
                    self.rect.y-=32
        
    def update(self):
        self.checkKeys()
       


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
    pygame.display.set_caption("Generic Steampunk Dungeon Crawler")
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((25, 25, 35))
    
    playArea = pygame.Surface((0,0))
    allSprites = pygame.sprite.Group()
    tiled_renderer = TiledRenderer("/acp/data/levels/level.tmx")

    
    
    player = Player(32,32,"data/textures/player.png")
    allSprites.add(player)
    
    map_surf = tiled_renderer.make_map()
    map_rect = map_surf.get_rect()

    

    
    clock = pygame.time.Clock()
    
    keepGoing = True

    while keepGoing:
        
        screen.blit(map_surf,(0,0))
        allSprites.draw(screen)
        clock.tick(60)
        
        player.update()
        
        for event in pygame.event.get():
            if event.type == QUIT:
                return
            
                    
        pygame.display.update()

if __name__ == "__main__":
    main()

pygame.quit() 
    
