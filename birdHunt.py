# I - Import and Initialize
import pygame
import birdHuntSprites
pygame.init()
            
def main():
    '''This function defines the 'mainline logic' for our game.'''
      
    # Display
    screen = pygame.display.set_mode((1000, 1000))    
    pygame.display.set_caption("Bird Hunt")
     
    # Entities
    background = pygame.Surface(screen.get_size())
    background.fill((255, 255, 255))
    screen.blit(background, (0, 0))
    #Create a bird sprite
    bird = birdHuntSprites.Bird(5)
    crossHair = birdHuntSprites.Crosshair() 
    mouseCircle = birdHuntSpirtes.MouseCircle()
    scoreKeeper = birdHuntSprites.Scorekeeper()
    allSprites = pygame.sprite.OrderedUpdates(bird, crossHair, mouseCircle, scoreKeeper)
         
    # ACTION
     
    # Assign 
    clock = pygame.time.Clock()
    keepGoing = True
 
    # Loop
    while keepGoing:
     
        # Time
        clock.tick(30)
     
        # Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if mouseCircle.rect.colliderect(bird):
                    bird.kill()
                    scoreKeeper.addScore(50)

        # Refresh screen
        allSprites.clear(screen, background)
        allSprites.update()
        allSprites.draw(screen)
         
        pygame.display.flip()
 
    # Close the game window
    pygame.quit()    
         
# Call the main function
main()