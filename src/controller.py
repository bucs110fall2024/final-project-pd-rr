import pygame

from scene import Scene
from choice import Choice

BGCOLOR = (255, 255, 255)


class Controller: 
    def __init__(self):
        """Initialzes controller, sets up pygame, start screen"""
        pygame.init()
        self.screen = pygame.display.set_mode()
        self.width, self.height = 800, 600
        self.background = pygame.Surface((self.width, self.height))
        self.background_color = BGCOLOR
        self.background.fill(self.background_color)
        pygame.display.set_caption("The Cave of Riddles")

        self.font = pygame.font.Font(None, 18)
        #self.choice = Choice("Testing", 100, 100, enabled = True)
        
        self.scene = Scene("Test", 100, 200)


    def mainloop(self):
        """placeholder"""
        while True: 
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.choice.check_click():
                        print("Mouse clicked")
            
            self.screen.fill(BGCOLOR)
            
            #self.choice.draw(self.screen, self.font)
            self.scene.draw(self.screen, self.font)


            pygame.display.flip()

            clock = pygame.time.Clock()
            clock.tick(60)
