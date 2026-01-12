import pygame
import random
import sys

# Initialize Pygame
pygame.init()  # type: ignore

# Constants
WIDTH = 800
HEIGHT = 600
BLOCK_SIZE = 20
FPS = 10

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Load assets
background = pygame.image.load('Snakes/snakes.jpg')
pygame.mixer.music.load('Snakes/game.mp3')
pygame.mixer.music.play(-1)  # Play background music in loop

# Set up display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Snake Game')
clock = pygame.time.Clock()

# Font
font = pygame.font.SysFont(None, 35)

def draw_snake(snake_body):
    for block in snake_body:
        pygame.draw.rect(screen, GREEN, [block[0], block[1], BLOCK_SIZE, BLOCK_SIZE])

def draw_food(food_pos):
    pygame.draw.rect(screen, RED, [food_pos[0], food_pos[1], BLOCK_SIZE, BLOCK_SIZE])

def draw_score(score):
    text = font.render("Score: " + str(score), True, WHITE)
    screen.blit(text, [10, 10])

def game_over_message():
    text = font.render("Game Over! Press Q to Quit or C to Play Again", True, WHITE)
    screen.blit(text, [WIDTH / 6, HEIGHT / 3])

def main():
    game_over = False
    game_close = False

    # Initial snake position and body
    x = WIDTH / 2
    y = HEIGHT / 2
    x_change = 0
    y_change = 0
    snake_body = []
    length_of_snake = 1

    # Food position
    food_x = round(random.randint(0, WIDTH - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE
    food_y = round(random.randint(0, HEIGHT - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE

    while not game_over:
        while game_close:
            screen.blit(background, (0, 0))
            game_over_message()
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                    game_close = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        main()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and x_change == 0:
                    x_change = -BLOCK_SIZE
                    y_change = 0
                elif event.key == pygame.K_RIGHT and x_change == 0:
                    x_change = BLOCK_SIZE
                    y_change = 0
                elif event.key == pygame.K_UP and y_change == 0:
                    y_change = -BLOCK_SIZE
                    x_change = 0
                elif event.key == pygame.K_DOWN and y_change == 0:
                    y_change = BLOCK_SIZE
                    x_change = 0

        # Check boundaries
        if x >= WIDTH or x < 0 or y >= HEIGHT or y < 0:
            game_close = True

        x += x_change
        y += y_change

        screen.blit(background, (0, 0))

        # Draw food
        draw_food([food_x, food_y])

        # Update snake head
        snake_head = [x, y]
        snake_body.append(snake_head)

        if len(snake_body) > length_of_snake:
            del snake_body[0]

        # Check self collision
        for block in snake_body[:-1]:
            if block == snake_head:
                game_close = True

        draw_snake(snake_body)
        draw_score(length_of_snake - 1)

        pygame.display.update()

        # Check if food eaten
        if x == food_x and y == food_y:
            food_x = round(random.randint(0, WIDTH - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE
            food_y = round(random.randint(0, HEIGHT - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE
            length_of_snake += 1

        # Increase speed as score increases
        current_fps = min(10 + (length_of_snake - 1) // 5, 30)  # Start at 10, increase every 5 points, max 30
        clock.tick(current_fps)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
