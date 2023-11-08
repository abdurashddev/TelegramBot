import pygame
import random

pygame.init()
WIDTH_WINDOW = 1000
HIGHT_WINDOW = 400
screen = pygame.display.set_mode([WIDTH_WINDOW, HIGHT_WINDOW], pygame.RESIZABLE)
clock = pygame.time.Clock()

dragon_image = pygame.image.load("C:\\Users\\hp\\Desktop\\game png\\2.png")
dragon_image = pygame.transform.scale(dragon_image, (100, 100))
dragon_rect = dragon_image.get_rect()
dragon_rect.left = 32
dragon_rect.centery = HIGHT_WINDOW // 2

money = pygame.image.load("C:\\Users\\hp\\Desktop\\game png\\3.png")
money = pygame.transform.scale(money,(50,50))
money_rect = money.get_rect()
money_rect.x = WIDTH_WINDOW - 50
money_rect.y = random.randint(50,400)

font = pygame.font.SysFont("inkfree", 24)
font_text = font.render(
    "Score:", True,
    (4, 189, 87), (19, 20, 20)
)
font_text_1 = font.render("Lives:", True, (4, 189, 87), (19, 20, 20))

text_rect = font_text.get_rect()
text_rect.topleft = (10, 10)

text_rect1 = font_text.get_rect()
text_rect1.topright = (980, 10)

font_text_2 = font.render("Feed the Dragon", True, (4, 189, 87), (250, 250, 250))

text_rect2 = font_text_2.get_rect()
text_rect2.midtop = (500, 10)

score = 0
lives = 5

money_sound = pygame.mixer.Sound("C:\\Users\\hp\\Desktop\\game sound\\sound 2.wav")
game_sound = pygame.mixer.Sound("C:\\Users\\hp\\Desktop\\game sound\\sound1.wav")
game_over_sound = pygame.mixer.Sound("C:\\Users\\hp\\Desktop\\game sound\\sound.wav")

game_over = pygame.font.SysFont("roboto", 150)
game_over_1 = font.render("Game over"
                          , True, (6, 125, 34), (8, 8, 8))

game_over1 = font_text_1.get_rect()
game_over1.center = (400, 150)

enter = pygame.font.SysFont("roboto", 150)
enter_1 = font.render("Key enter = repley game"
                          , True, (6, 125, 34), (8, 8, 8))

enter1 = font_text_1.get_rect()
enter1.center = (400, 200)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()


    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and dragon_rect.y > 55:
        dragon_rect.y -= 5
    elif keys[pygame.K_s] and dragon_rect.y < 300:
        dragon_rect.y += 5

    if money_rect.x > -50:
        money_rect.x -= 10
        clock.tick(50)
    elif money_rect.x == -50:
        game_sound.play()
        money_rect.x = WIDTH_WINDOW - 100
        money_rect.y = random.randint(50, 350)
        lives -= 1
        clock.tick(50)
    if money_rect.colliderect(dragon_rect):
        pygame.display.update()
        money_sound.play()
        money_rect.x = WIDTH_WINDOW - 100
        money_rect.y = random.randint(50, 350)
        clock.tick(50)
        score += 1
    if lives == 0:
        game_over_sound.play()
        screen.blit(game_over_1,game_over1)
        screen.blit(enter_1,enter1)
        pygame.display.update()

        true = True
        while true:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        game_over_sound.stop()
                        score = 0
                        lives = 5
                        dragon_rect.y = 70
                        true = False
                    if event.type == pygame.QUIT:
                        exit()

    font = pygame.font.SysFont("inkfree", 24)
    font_text = font.render(
        "Score:" + str(score), True,
        (4, 189, 87), (19, 20, 20))
    font_text_1 = font.render("Lives:" + str(lives), True, (4, 189, 87), (19, 20, 20))

    screen.fill((0, 0, 0))
    pygame.draw.line(screen, (199, 150, 16), (0, 50), (1000, 50), width=5)
    screen.blit(font_text, text_rect)
    screen.blit(font_text_1, text_rect1)
    screen.blit(font_text_2, text_rect2)
    screen.blit(money,money_rect)
    screen.blit(dragon_image, dragon_rect)

    pygame.display.update()
    clock.tick(90)

    # for i in pygame.font.get_fonts():
    #     print(i)
