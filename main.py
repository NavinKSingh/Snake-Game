import pygame
import random
import os

# Initialize Pygame
pygame.mixer.init()
pygame.init()

# Constants
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
SCREEN_WIDTH = 900
SCREEN_HEIGHT = 600
SNAKE_SIZE = 30
INIT_VELOCITY = 4
FPS = 60
HI_SCORE_FILE = "hiscore.txt"
BG_IMAGE_PATH = "image.jpg"
BG_IMAGE_PATH1 = "image2.webp"
BG_IMAGE_PATH2 = "image3.jpg"
MUSIC_START = 'music1.mp3'
MUSIC_INTRO = 'music4.mp3'
MUSIC_GAME_OVER = 'music2.mp3'
MUSIC_HIT_WALL = 'music2.mp3'
MUSIC_EAT_FRUIT = 'music3.mp3'
FOOD_IMAGE_PATH = "apple.png"    # Add your food image path

# Creating window
gameWindow = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("SNAKES WITH KN")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 55)

# Load background images
bgimg = pygame.image.load(BG_IMAGE_PATH)
bgimg = pygame.transform.scale(bgimg, (SCREEN_WIDTH, SCREEN_HEIGHT)).convert_alpha()

bgimg1 = pygame.image.load(BG_IMAGE_PATH1)
bgimg1 = pygame.transform.scale(bgimg1, (SCREEN_WIDTH, SCREEN_HEIGHT)).convert_alpha()

bgimg2 = pygame.image.load(BG_IMAGE_PATH2)
bgimg2 = pygame.transform.scale(bgimg2, (SCREEN_WIDTH, SCREEN_HEIGHT)).convert_alpha()

# Load images for food
food_img = pygame.image.load(FOOD_IMAGE_PATH)
food_img = pygame.transform.scale(food_img, (SNAKE_SIZE, SNAKE_SIZE))

# Load sound effects
sound_eat_fruit = pygame.mixer.Sound(MUSIC_EAT_FRUIT)

def welcome():
    exit_game = False
    pygame.mixer.music.load(MUSIC_INTRO)
    pygame.mixer.music.play(loops=-1)

    while not exit_game:
        gameWindow.blit(bgimg1, (0, 0))
        text_screen("WELCOME TO SNAKE GAME WITH KN!", "#C04018", 80, 120)
        text_screen("PRESS SPACE BAR TO START...", "#7BAF44", 160, 240)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pygame.mixer.music.load(MUSIC_START)
                    pygame.mixer.music.play(loops=-1)
                    gameloop()
        pygame.display.update()
        clock.tick(FPS)

def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text, [x, y])

def plot_snake(snk_list):
    for x, y in snk_list:
        pygame.draw.rect(gameWindow, BLACK, [x, y, SNAKE_SIZE, SNAKE_SIZE])

def load_highscore():
    if not os.path.exists(HI_SCORE_FILE):
        with open(HI_SCORE_FILE, "w") as f:
            f.write("0")
    with open(HI_SCORE_FILE, "r") as f:
        return int(f.read())

def save_highscore(score):
    with open(HI_SCORE_FILE, "w") as f:
        f.write(str(score))

def gameloop():
    exit_game = False
    game_over = False
    snake_x = 45
    snake_y = 45
    velocity_x = 0
    velocity_y = 0
    current_direction = None  
    snk_list = []
    snk_length = 1
    food_x = random.randint(20, int(SCREEN_WIDTH / 2))
    food_y = random.randint(20, int(SCREEN_HEIGHT / 2))
    score = 0
    hiscore = load_highscore()

    while not exit_game:
        if game_over:
            save_highscore(hiscore)
            gameWindow.blit(bgimg2, (0, 0))
            text_screen("Game Over! Press Enter To Continue", "#F0E057", 100, 250)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        welcome()
        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT and current_direction != "LEFT":
                        velocity_x = INIT_VELOCITY
                        velocity_y = 0
                        current_direction = "RIGHT"
                    elif event.key == pygame.K_LEFT and current_direction != "RIGHT":
                        velocity_x = -INIT_VELOCITY
                        velocity_y = 0
                        current_direction = "LEFT"
                    elif event.key == pygame.K_UP and current_direction != "DOWN":
                        velocity_y = -INIT_VELOCITY
                        velocity_x = 0
                        current_direction = "UP"
                    elif event.key == pygame.K_DOWN and current_direction != "UP":
                        velocity_y = INIT_VELOCITY
                        velocity_x = 0
                        current_direction = "DOWN"
                    elif event.key == pygame.K_q:
                        score += 10

            snake_x += velocity_x
            snake_y += velocity_y

            # Define head here before checking for collisions
            head = [snake_x, snake_y]

            if abs(snake_x - food_x) < 10 and abs(snake_y - food_y) < 10:
                score += 10
                food_x = random.randint(20, int(SCREEN_WIDTH / 2))
                food_y = random.randint(20, int(SCREEN_HEIGHT / 2))
                snk_length += 10
                sound_eat_fruit.play()  # Play sound when eating fruit
                if score > hiscore:
                    hiscore = score

            if snake_x < 0 or snake_x > SCREEN_WIDTH or snake_y < 0 or snake_y > SCREEN_HEIGHT or \
                head in snk_list[:-1]:
                game_over = True
                pygame.mixer.music.load(MUSIC_HIT_WALL if snake_x < 0 or snake_x > SCREEN_WIDTH or snake_y < 0 or snake_y > SCREEN_HEIGHT else MUSIC_GAME_OVER)
                pygame.mixer.music.play()

            gameWindow.fill(WHITE)
            gameWindow.blit(bgimg, (0, 0))
            text_screen(f"Score: {score}  Hiscore: {hiscore}", RED, 5, 5)
            gameWindow.blit(food_img, (food_x, food_y))

            snk_list.append(head)
            if len(snk_list) > snk_length:
                del snk_list[0]

            plot_snake(snk_list)

        pygame.display.update()
        clock.tick(FPS)

    pygame.quit()
    quit()

welcome()
