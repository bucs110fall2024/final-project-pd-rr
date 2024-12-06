import pygame

class Choice:
    def __init__(self, text, x_pos, y_pos, enabled):
        """Placeholder"""
        self.text = text
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.enabled = enabled
        self.width, self.height = 150, 25 
        self.choice_rect = pygame.rect.Rect(self.x_pos, self.y_pos, self.width, self.height)  

    def draw(self, screen, font):
        """Placeholder"""
        choice_text = font.render(self.text, True, (0, 0, 0))
        choice_rect = pygame.rect.Rect(self.x_pos, self.y_pos, 150, 25)

        if self.enabled:
            if self.choice_rect.collidepoint(pygame.mouse.get_pos()):
                pygame.draw.rect(screen, (169, 169, 169), choice_rect, 0, 5)
            else:
                pygame.draw.rect(screen, (211, 211, 211), choice_rect, 0, 5)
        else:
                    pygame.draw.rect(screen,(0, 0, 0), choice_rect, 0, 5)

        pygame.draw.rect(screen, (0, 0, 0), choice_rect, 2, 5)
        screen.blit(choice_text, (self.x_pos + 3, self.y_pos + 3))

    def check_click(self):
        """Placeholder"""
        mouse_pos = pygame.mouse.get_pos()
        left_click = pygame.mouse.get_pressed()[0]
        choice_rect = pygame.rect.Rect(self.x_pos, self.y_pos, 150, 25)

        if left_click and choice_rect.collidepoint(mouse_pos) and self.enabled:
            return True
        else:
            return False
