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
        self.font = pygame.font.Font(None, 32)        

        self.wrong_choices = 0


        self.font = pygame.font.Font(None, 18)  
        self.current_scene = 0
        self.make_scenes()

    def start_screen(self):
        self.screen.fill(BGCOLOR)
        title_font = pygame.font.Font(None, 64)
        context_font = pygame.font.Font(None, 32)

        title_text = "The Cave of Riddles"
        title = title_font.render(title_text, True, (0, 0, 0))
        self.screen.blit(title, (self.width // 2 - title.get_width() // 2, 100))

        context_text = "Test your Knowledge, answer these riddles. Press any key."
        context = context_font.render(context_text, True, (0, 0, 0))
        self.screen.blit(context, (self.width // 2 - context.get_width() // 2, 500))

        pygame.display.flip()

        wait = True
        while wait:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                elif event.type == pygame.KEYDOWN:
                    wait = False

    def make_scenes(self):
        """Placeholder"""
        choice_scene_1 = [ 
            Choice("Choice 1", 100, 400, enabled=True),
            Choice("Choice 2", 100, 450, enabled=True),
            Choice("Choice 3", 100, 500, enabled=True)
        ]
        scene_1 = Scene("Riddle 1?", 100, 200, choice_scene_1, "Choice 1") 

        choice_scene_2 = [ 
            Choice("Choice 1", 100, 400, enabled=True),
            Choice("Choice 2", 100, 450, enabled=True),
            Choice("Choice 3", 100, 500, enabled=True)
        ]
        scene_2 = Scene("Riddle 2?", 100, 200, choice_scene_2, "Choice 3" ) 

        choice_scene_3 = [ 
            Choice("Choice 1", 100, 400, enabled=True),
            Choice("Choice 2", 100, 450, enabled=True),
            Choice("Choice 3", 100, 500, enabled=True)
        ]
        scene_3 = Scene("Riddle 3?", 100, 200, choice_scene_3, "Choice 2" ) 

        choice_scene_4 = [ 
            Choice("Choice 1", 100, 400, enabled=True),
            Choice("Choice 2", 100, 450, enabled=True),
            Choice("Choice 3", 100, 500, enabled=True)
        ]
        scene_4 = Scene("Riddle 4?", 100, 200, choice_scene_4, "Choice 2") 

        choice_scene_5 = [ 
            Choice("Choice 1", 100, 400, enabled=True),
            Choice("Choice 2", 100, 450, enabled=True),
            Choice("Choice 3", 100, 500, enabled=True)
        ]
        scene_5 = Scene("Riddle 5?", 100, 200, choice_scene_5, "Choice 1" ) 

        self.scenes = [scene_1, scene_2, scene_3, scene_4, scene_5]  
     

    def check_choice(self, click):
        if click.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            for choice in self.scene.choices:
                if choice.check_click():
                    if choice.text == self.scene.correct_choice:
                        print("correct")
                        self.current_scene += 1
                        if self.current_scene >= len(self.scenes):
                            self.end_scene()
                    else:
                        print("Try again")
                        self.wrong_choices += 1

    def end_scene(self):
        self.screen.fill(BGCOLOR)
        end_text = f"You have passed, having made {self.wrong_choices} wrong choices."
        end_font = pygame.font.Font(None, 36)
        end_surface = end_font.render(end_text, True, (0, 0, 0))
        self.screen.blit(end_surface, (self.width // 2 - end_surface.get_width() // 2, self.height // 2))

        pygame.display.flip()
        pygame.time.wait(6000)
        pygame.quit()
        exit()


    def mainloop(self):
        """placeholder"""
        self.start_screen()
        
        while True: 
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.check_choice(event)
                        
            
            self.screen.fill(BGCOLOR)
            self.scene = self.scenes[self.current_scene]
            self.scene.draw(self.screen, self.font)

            pygame.display.flip()

            clock = pygame.time.Clock()
            clock.tick(60)
