import pygame
from settings import WHITE, BLACK, RED, LIGHT_BLUE, DARK_BLUE


class Button:
    def __init__(self, x, y, width, height, text, action=None):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.action = action
        self.color_idle = RED
        self.color_hover = DARK_BLUE
        self.color_border = BLACK
        self.text_color = BLACK
        
    def draw(self, screen, font):
        mouse_post = pygame.mouse.get_pos()
        color = self.color_hover if self.rect.collidepoint(mouse_post) else self.color_idle
        pygame.draw.rect(screen, color, self.rect)
        pygame.draw.rect(screen, self.color_border, self.rect, 2)
        text_surf = font.render(self.text, True, self.text_color)  
        text_rect = text_surf.get_rect(center=self.rect.center)
        screen.blit(text_surf, text_rect)

    def hable_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos) and self.action:
                self.action()


button1 = Button(0, 0, 100, 50, "")

print(button1.rect)

