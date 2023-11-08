import pygame

pygame.init()
screen = pygame.display.set_mode((595,600),pygame.RESIZABLE)

image = pygame.image.load("C:\\Users\\hp\\Desktop\\game png\\1.png")
image = pygame.transform.scale(image,(70,70))
image_rect = image.get_rect()

image_rect.x = 100
image_rect.y = 100

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w and image_rect.top > 50 and image_rect.top > 150:
                image_rect.y -= 10
            elif event.key == pygame.K_s and image_rect.bottom < 550 and image_rect.bottom < 450:
                image_rect.y += 10
            elif event.key == pygame.K_a and image_rect.left > 80:
                image_rect.x -= 10
            elif event.key == pygame.K_d and image_rect.right < 600:
                image_rect.x += 10
            elif event.key == pygame.K_q and pygame.K_w and image_rect.top > 50:
                image_rect.y -= 10

        screen.blit(image, image_rect)
        pygame.display.update()
        screen.fill((89, 89, 89))

        pygame.draw.rect(screen,(4, 207, 58),(0,0,800,50))
        pygame.draw.rect(screen, (4, 207, 58), (0, 20, 100, 100))
        pygame.draw.rect(screen, (4, 207, 58), (0, 550, 800, 50))
        pygame.draw.rect(screen, (4, 207, 58), (0, 480, 100, 100))

        pygame.draw.rect(screen,(250,250,250),(170,50,5,100))
        pygame.draw.rect(screen, (250, 250, 250), (240, 50, 5, 100))
        pygame.draw.rect(screen, (250, 250, 250), (310, 50, 5, 100))
        pygame.draw.rect(screen, (250, 250, 250), (380, 50, 5, 100))
        pygame.draw.rect(screen, (250, 250, 250), (450, 50, 5, 100))
        pygame.draw.rect(screen, (250, 250, 250), (520, 50, 5, 100))
        pygame.draw.rect(screen, (250, 250, 250), (590, 50, 5, 100))

        pygame.draw.rect(screen, (250, 250, 250), (170, 450, 5, 100))
        pygame.draw.rect(screen, (250, 250, 250), (240, 450, 5, 100))
        pygame.draw.rect(screen, (250, 250, 250), (310, 450, 5, 100))
        pygame.draw.rect(screen, (250, 250, 250), (380, 450, 5, 100))
        pygame.draw.rect(screen, (250, 250, 250), (450, 450, 5, 100))
        pygame.draw.rect(screen, (250, 250, 250), (520, 450, 5, 100))
        pygame.draw.rect(screen, (250, 250, 250), (590, 450, 5, 100))

        pygame.draw.rect(screen, (250,250,250), (463, 480, 50, 50),width=5)
        pygame.draw.rect(screen, (250, 250, 250), (480, 490, 5, 30))
        pygame.draw.circle(screen,(250,250,250),(485, 500),
                           radius=10,width=5,draw_top_right=True,draw_bottom_right=True)

        pygame.draw.rect(screen, (250, 250, 250), (323, 70, 50, 50), width=5)
        pygame.draw.rect(screen, (250, 250, 250), (340, 80, 5, 30))
        pygame.draw.circle(screen, (250, 250, 250), (345, 90),
                           radius=10, width=5, draw_bottom_right=True, draw_top_right=True)