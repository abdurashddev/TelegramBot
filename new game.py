import pygame

pygame.init()

screen = pygame.display.set_mode([0,0],pygame.RESIZABLE)

clock = pygame.time.Clock()

word = pygame.image.load("C:\\Users\\hp\\Desktop\\game png\\aa.jpg")
word = pygame.transform.scale(word,(1920,900))
word_rect = word.get_rect(x=0,y=0)

player = pygame.image.load("C:\\Users\\hp\\Desktop\\game png\\player.png")
player = pygame.transform.scale(player,(400,400))
player_rect = word.get_rect(x=100,y=400)

player1 = pygame.image.load("C:\\Users\\hp\\Desktop\\game png\\player1.png")
player1 = pygame.transform.scale(player1,(400,400))
player1_rect = word.get_rect(x=1000,y=400)

mortl_sound = pygame.mixer.Sound("C:\\Users\\hp\\Desktop\\game sound\\combat.mp3")

player_lives = pygame.image.load("C:\\Users\\hp\\Desktop\\game png\\player.png")
player_lives = pygame.transform.scale(player_lives,(400,400))
player_lives_rect = word.get_rect(x=100,y=400)

player1_lives = pygame.image.load("C:\\Users\\hp\\Desktop\\game png\\player1.png")
player1_lives = pygame.transform.scale(player1_lives,(400,400))
player1_lives_rect = word.get_rect(x=1000,y=400)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT] and player_rect.x < 1200:
        player_rect.x += 10
        clock.tick(90)
    elif keys[pygame.K_LEFT] and player_rect.x > 0:
        player_rect.x -= 10
        clock.tick(90)
    elif keys[pygame.K_d] and player1_rect.x < 1100:
        player1_rect.x += 10
        clock.tick(90)
    elif keys[pygame.K_a] and player1_rect.x > 0:
        player1_rect.x -= 10
        clock.tick(90)

    mortl_sound.play()
    screen.blit(word,word_rect)
    screen.blit(player,player_rect)
    screen.blit(player1,player1_rect)
    pygame.display.update()
