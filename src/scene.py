import pygame

class Scene:
    def __init__(self, text, x_pos, y_pos, choices, correct_choice, picture=None):
        """Basis for scenes
        
        """
        self.text = text
        self.x_pos = x_pos
        self.y_pos = y_pos

        self.width, self.height = 600, 150 
        self.scene_rect = pygame.rect.Rect(self.x_pos, self.y_pos, self.width, self.height)  

        if picture: 
            self.picture = pygame.image.load(picture)
        else: 
            self.picture = None

        self.choices = choices
        self.correct_choice = correct_choice

    def draw(self, screen, font):
        """Draws the Scene"""
        scene_text = font.render(self.text, True, 'black')
        scene_rect = scene_text.get_rect(center=self.scene_rect.center)
        pygame.draw.rect(screen, (255,213,128), self.scene_rect, 0, 5)  # Filled rectangle
        pygame.draw.rect(screen, 'black', self.scene_rect, 2, 5)

        screen.blit(scene_text, scene_rect)

        if self.picture:
            picture_rect = self.picture.get_rect(topleft=(self.x_pos, self.y_pos + self.height + 20))
            screen.blit(self.picture, picture_rect)

        for choice in self.choices:
            choice.draw(screen, font)


  

