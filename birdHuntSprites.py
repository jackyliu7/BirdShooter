""" 
Name : Jacky
Date : May 14, 2019
Description : This program creates the classes needed for birdHunt game.
""" 

import pygame
import random

class Bird(pygame.sprite.Sprite):
    """This class defines the sprite for birds"""
    def __init__(self, points):
        """This initializer method takes screen and points as parameters and instantiates a bird, points, centerx, centery, and direction"""
        pygame.sprite.Sprite.__init__(self)
        
        self.points = points
        
        if points == 1:
            self.image = self.image.load("pelipper.png")
            self.image = self.image.convert()
        if points == 2:
            self.image = self.image.load("charizard.png")
            self.image = self.image.convert()
        if points == 3:
            self.image = self.image.load("golbat.png")
            self.image = self.image.convert()
        if points == 4:
            self.image = self.image.load("pidgeot.png")
            self.image = self.image.convert()
        if points == 5:
            self.image = self.image.load("zapdos.png")
            self.image = self.image.convert()
            
        self.rect = self.image.get_rect()
     
        if random.randint(1, 2) == 1:
            self.rect.center = (random.randint(100, 900), 0)
        else:
            self.rect.center = (0, random.randint(100, 900))
        #set the direction of the bird    
        self.dx = random.randint(3, 8)
        self.dy = random.randint(3, 8)
        
    def update(self):
        """This method will automatically be called to reposition the bird on the screen"""
        # Check if we have reached the left or right end of the screen.
        # If not, then keep moving the ball in the same x direction.
        if ((self.rect.left > 0) and (self.dx < 0)) or\
           ((self.rect.right < self.window.get_width()) and (self.dx > 0)):
            self.rect.left += self.dx
        #If yes, kill the sprite
        else:
            self.kill()
            
        # Check if we have reached the top or bottom of the court.
        # If not, then keep moving the ball in the same y direction.
        if ((self.rect.top-40 > 0) and (self.dy > 0)) or\
           ((self.rect.bottom+40 < self.window.get_height()) and (self.dy < 0)):
            self.rect.top += self.dy
        # If yes, kill the sprite
        else:
            self.kill()         
        
class Crosshair(pygame.sprite.Sprite):
    """A mouse following crosshair sprite"""
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = self.image.load("crosshair.png")
        self.rect = self.image.get_rect()
        
    def update(self, xy):
        """This method repositions the crosshair onto the mouse"""
        self.rect.center = mouse.postion.get_pos()
        
class MouseCircle(pygame.sprite.Sprite):
    """A mouse following circle sprite subclass to accurately detect sprite collisions"""
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((1, 1))
        self.image.fill(0, 0, 0)
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect()
        
    def update(self):
        """Moves the center of the circle to where the mouse is pointing."""
        self.rect.center = pygame.mouse.get_pos()
    
class Scorekeeper(pygame.sprite.Sprite):
    def __init__(self, screen):
        pygame.sprite.Sprite.__init__(self)
        self.points = 0
        
    def addScore(self, points):
        self.points += points
        
    def loseScore(self, points):
        self.points -= points
        
    def getScore(self):
        '''This method returns the total score of the player'''
        return self.points
            
    def update(self):
        '''This method will consistently update and display the score and lives that the player has.'''        
        mySystemFont = pygame.font.SysFont("Arial", 30)
        self.image = mySystemFont.render("Score: " + str(self.points), 1, (0, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.center = (500, 15)
            
        