import pygame, random
from random import choice
from pygame.locals import *
import logging
logging.basicConfig(level=logging.INFO)


    

def game():
    logging.info('iniciando o jogo ...')
    snake_game = SnakeGame()
    logging.info('fechadno o jogo.')
    return snake_game.run()


class SnakeGame:
    def __init__(self):
        self.UP = 0
        self.RIGHT = 1
        self.DOWN = 2
        self.LEFT = 3

    # Gera a fruta no mapa aleatóriamente
    # TODO: Coloque conforme o score aumenta uma probabilidade de cair nas beiradas maior
    def on_grid_random(self):
        x = random.randint(0,59)
        y = random.randint(0,59)
        return (x * 10, y * 10)

    def collision(self, c1, c2):
        return (c1[0] == c2[0]) and (c1[1] == c2[1])

    def run(self):
        pygame.init()
        screen = pygame.display.set_mode((600, 600))
        pygame.display.set_caption('Snake')

        snake = [(200, 200), (210, 200), (220,200)]
        snake_skin = pygame.Surface((10, 10))
        snake_skin.fill((175, 225, 175))

        apple_pos = self.on_grid_random()
        apple = pygame.Surface((10,10))
        apple.fill((255,87,51))

        my_direction = choice(
            [
                self.LEFT,
                self.UP,
                self.DOWN,
                self.RIGHT
            ]
        )

        clock = pygame.time.Clock()

        font = pygame.font.Font('freesansbold.ttf', 18)
        score = 0
        dificult = 5
        game_over = False
        while not game_over:
            clock.tick(dificult)  # vai aumentando a velocidade do jogo
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()

                if event.type == KEYDOWN:
                    if event.key == K_UP and my_direction != self.DOWN:
                        my_direction = self.UP
                    if event.key == K_DOWN and my_direction != self.UP:
                        my_direction = self.DOWN
                    if event.key == K_LEFT and my_direction != self.RIGHT:
                        my_direction = self.LEFT
                    if event.key == K_RIGHT and my_direction != self.LEFT:
                        my_direction = self.RIGHT

            if self.collision(snake[0], apple_pos):
                apple_pos = self.on_grid_random()
                snake.append((0,0))
                score += 1
                dificult += 3
                
            # Check if snake collided with boundaries
            if snake[0][0] == 600 or snake[0][1] == 600 or snake[0][0] < 0 or snake[0][1] < 0:
                game_over = True
                break
            
            # Check if the snake has hit itself
            for i in range(1, len(snake) - 1):
                if snake[0][0] == snake[i][0] and snake[0][1] == snake[i][1]:
                    game_over = True
                    break

            if game_over:
                break
            
            # cria o movimento da cobra
            for i in range(len(snake) - 1, 0, -1):
                snake[i] = (snake[i-1][0], snake[i-1][1])
                
            # Actually make the snake move.
            if my_direction == self.UP:
                snake[0] = (snake[0][0], snake[0][1] - 10)
            if my_direction == self.DOWN:
                snake[0] = (snake[0][0], snake[0][1] + 10)
            if my_direction == self.RIGHT:
                snake[0] = (snake[0][0] + 10, snake[0][1])
            if my_direction == self.LEFT:
                snake[0] = (snake[0][0] - 10, snake[0][1])
            
            screen.fill((0,0,0))
            screen.blit(apple, apple_pos)
            
            for x in range(0, 600, 10): # Draw vertical lines
                pygame.draw.line(screen, (40, 40, 40), (x, 0), (x, 600))
            for y in range(0, 600, 10): # Draw vertical lines
                pygame.draw.line(screen, (40, 40, 40), (0, y), (600, y))
            
            score_font = font.render('Score: %s' % (score), True, (255, 255, 255))
            score_rect = score_font.get_rect()
            score_rect.topleft = (600 - 120, 10)
            screen.blit(score_font, score_rect)
            
            for pos in snake:
                screen.blit(snake_skin,pos)

            pygame.display.update()

        while True:
            game_over_font = pygame.font.Font('freesansbold.ttf', 75)
            game_over_screen = game_over_font.render('Game Over', True, (255, 255, 255))
            game_over_rect = game_over_screen.get_rect()
            game_over_rect.midtop = (600 / 2, 10)
            screen.blit(game_over_screen, game_over_rect)
            pygame.display.update()
            pygame.time.wait(500)
            while True:
                for event in pygame.event.get():
                    if event.type == QUIT:
                        pygame.quit()
                        exit()
