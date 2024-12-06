import pygame

from scene import Scene
from choice import Choice

WHITE = (251, 166, 58)


class Controller: 
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode()
        self.width, self.height = 1920, 1080
        self.background = pygame.Surface((self.width, self.height))
        self.background_color = WHITE
        self.background.fill(self.background_color)
        pygame.display.set_caption("The Cave of Riddles")
        self.font = pygame.font.Font(None, 32)        

        self.wrong_choices = 0

        self.background_image = pygame.image.load("assets/background.jpg")
        self.background_image = pygame.transform.scale(self.background_image, (self.width, self.height))

        self.transition_image = pygame.image.load("assets/transitionscreen.jpg")
        self.transition_image = pygame.transform.scale(self.background_image, (self.width, self.height))

        self.font = pygame.font.Font(None, 20)  
        self.current_scene = 0
        self.make_scenes()

    def start_screen(self):
        self.screen.blit(self.transition_image, (0, 0))  
        title_font = pygame.font.Font(None, 64)
        context_font = pygame.font.Font(None, 32)

        title_text = "The Cave of Riddles"
        title = title_font.render(title_text, True, WHITE)
        self.screen.blit(title, (500, 100))

        context_text = "Test your Knowledge, answer these riddles. Press any key."
        context = context_font.render(context_text, True, WHITE)
        self.screen.blit(context, (450, 500))

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
            Choice("The Moon", 650, 400, enabled=True),
            Choice("The Sun", 650, 450, enabled=True),
            Choice("A Torch", 650, 500, enabled=True)
        ]
        scene_1 = Scene("I rise in the morning but set at night. I guide the lost with my light. What am I?", 420, 200, choice_scene_1, "The Sun") 

        choice_scene_2 = [ 
            Choice("A River", 650, 400, enabled=True),
            Choice("A Clock", 650, 450, enabled=True),
            Choice("A Shadow", 650, 500, enabled=True)
        ]
        scene_2 = Scene("I am always running but never move. I have a mouth but no voice. What am I?", 420, 200, choice_scene_2, "A Clock" ) 

        choice_scene_3 = [ 
            Choice("An Echo", 650, 400, enabled=True),
            Choice("A Whisper", 650, 450, enabled=True),
            Choice("A Ghost", 650, 500, enabled=True)
        ]
        scene_3 = Scene("Speaking without a mouth, born from a cave, I can be heard but never seen. What am I?", 420, 200, choice_scene_3, "An Echo" ) 

        choice_scene_4 = [ 
            Choice("Footsteps", 650, 400, enabled=True),
            Choice("Time", 650, 450, enabled=True),
            Choice("Shadows", 650, 500, enabled=True)
        ]
        scene_4 = Scene("The more of me you take, the more you leave behind. What am I?", 420, 200, choice_scene_4, "Footsteps") 

        choice_scene_5 = [ 
            Choice("Fire", 650, 400, enabled=True),
            Choice("A Plant", 650, 450, enabled=True),
            Choice("Water", 650, 500, enabled=True)
        ]
        scene_5 = Scene("I am not alive, but I grow. I don’t have lungs, but I need air. What am I?", 420, 200, choice_scene_5, "Fire" ) 

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
        self.screen.blit(self.transition_image, (0, 0))  
        end_text = f"You have passed, having made {self.wrong_choices} wrong choices."
        end_font = pygame.font.Font(None, 48)
        end_surface = end_font.render(end_text, True, WHITE)
        self.screen.blit(end_surface, (400 ,450 ))
    
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
                        
            
            self.screen.blit(self.background_image, (0, 0))
            self.scene = self.scenes[self.current_scene]
            self.scene.draw(self.screen, self.font)

            pygame.display.flip()

            clock = pygame.time.Clock()
            clock.tick(60)
