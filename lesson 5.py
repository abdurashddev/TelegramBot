import pygame

pygame.init()
screen = pygame.display.set_mode((600,300),pygame.RESIZABLE)

image = pygame.image.load("C:\\Users\\hp\\Desktop\\game png\\1.png")
image = pygame.transform.scale(image,(100,100))
image_rect = image.get_rect()

image_rect.x = 100
image_rect.y = 100


game_over = pygame.font.SysFont("roboto", 150)
game_over_1 = game_over.render("Game over"
                          , True, (6, 125, 34), (8, 8, 8))

game_over1 = game_over_1.get_rect()
game_over1.center = (400, 150)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w and image_rect.top > 0:
                image_rect.y -= 25
            elif event.key == pygame.K_s and image_rect.bottom < 300:
                image_rect.y += 25
            elif event.key == pygame.K_a and image_rect.left > 0:
                image_rect.x -= 25
            elif event.key == pygame.K_d and image_rect.right < 600:
                image_rect.x += 25

        pygame.display.update()
        screen.fill((250,250,250))
        screen.blit(image,image_rect)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT] and image_rect.right < 600:
        image_rect.x += 5
