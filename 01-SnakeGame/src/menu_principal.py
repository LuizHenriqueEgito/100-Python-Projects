import pygame
from pathlib import Path
from typing import Tuple

class MenuInicial:
    def __init__(
            self,
            window_size: Tuple[int],
            window_color: Tuple[int],
            set_display: str
        ) -> None:

        self.window_size = window_size
        self.winddow_color = window_color
        self.set_display = set_display

    def run(self):
        screen = pygame.display.set_mode(self.window_size)
        pygame.display.set_caption(self.set_display)
        screen.fill(self.winddow_color)
        pygame.display.flip()
        # Carregando os botoes de Jogar e Sair
        jogar_path = Path('src/images/jogar_imag.png')
        sair_path = Path('src/images/sair_imag.png')
        jogar_img = pygame.image.load(jogar_path).convert_alpha()
        sair_img = pygame.image.load(sair_path).convert_alpha()
        jogar_button = Button(100, 200, jogar_img, 0.8)
        exit_button = Button(450, 200, sair_img, 0.8)

        image_entrada_path = Path('src/images/img_entrda.png')
        image_entrada = pygame.image.load(image_entrada_path).convert_alpha()
        screen.blit(image_entrada, (150,0))

        running = True
        while running:
            if jogar_button.draw(screen=screen):
                print('START')
                pygame.quit()
                return True
            if exit_button.draw(screen=screen):
                running = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            pygame.display.update()
        pygame.quit()


class Button:
    def __init__(self, x, y, image, scale):
        widht, height = image.get_width(), image.get_height()
        self.image = pygame.transform.scale(image, (int(widht * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False


    def draw(self, screen):
        action = False
        # posição do mouse
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        screen.blit(self.image, (self.rect.x, self.rect.y))
        return action

