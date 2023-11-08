import pygame

WINDOW_WIDTH = 1920
WINDOW_HEIGHT = 900

screen = pygame.display.set_mode([WINDOW_WIDTH, WINDOW_HEIGHT], pygame.RESIZABLE)
clock = pygame.time.Clock()

word = pygame.image.load("C:\\Users\\hp\\Desktop\\game png\\word.jpg")
word = pygame.transform.scale(word, (1920, 900))

word_rect = word.get_rect()
word_rect.x = 0
word_rect.y = 0

mario = pygame.image.load("C:\\Users\\hp\\Desktop\\game png\\man.png")
mario = pygame.transform.scale(mario, (100, 100))
mario_rect = mario.get_rect(x=0,y=0)

tab = pygame.image.load("C:\\Users\\hp\\Desktop\\game png\\tab.png")
tab = pygame.transform.scale(tab, (80, 70))

tab_rect = tab.get_rect()
tab_rect.x = 950
tab_rect.y = 900

dy = 0
vel_y = 0
GRAVITY = 2

while True:
    clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    keys = pygame.key.get_pressed()
    screen.blit(word, word_rect)

    if keys[pygame.K_w]:
        vel_y = -10
    elif keys[pygame.K_s]:
        vel_y = 10

    vel_y += GRAVITY
    dy += vel_y

    if mario_rect.bottom + dy > WINDOW_HEIGHT - 300:
        vel_y = 0
        dy = WINDOW_HEIGHT - 300 - mario_rect.bottom

    mario_rect.y += dy

    if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
        mario_rect.x += 5

    elif keys[pygame.K_a] or keys[pygame.K_LEFT]:
        mario_rect.x -= 5

    # else:
    #
    # if keys[pygame.K_RIGHT] and mario_rect.x < 1400:
    # elif keys[pygame.K_LEFT] and mario_rect.x > 0:
    #     mario_rect.x -= 10

    screen.blit(mario, mario_rect)
    pygame.display.update()
