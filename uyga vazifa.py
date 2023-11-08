import pygame

pygame.init()
size = (600, 600)
screen = pygame.display.set_mode(size, pygame.RESIZABLE)
pygame.display.set_caption("Pdp Junior")
red = (238, 255, 5)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        pygame.display.update()
        screen.fill((5, 5, 5))
        pygame.draw.rect(screen,(23, 156, 166),(250,150,100,150))
        pygame.draw.rect(screen, (22, 4, 135), (250, 300, 100, 150))
        pygame.draw.rect(screen, (23, 156, 166), (200, 150, 50, 50))
        pygame.draw.rect(screen, (23, 156, 166), (350, 150, 50, 50))
        pygame.draw.rect(screen, (232, 148, 88), (200, 200, 50, 100))
        pygame.draw.rect(screen, (232, 148, 88), (350, 200, 50, 100))
        pygame.draw.rect(screen, (232, 148, 88), (250, 50, 100, 100))
        pygame.draw.rect(screen, (94, 44, 8), (250, 50, 100, 20))
        pygame.draw.rect(screen, (94, 44, 8), (250, 70, 20, 20))
        pygame.draw.rect(screen, (94, 44, 8), (330, 70, 20, 20))
        pygame.draw.rect(screen, (255, 255, 255), (265, 100, 25, 15))
        pygame.draw.rect(screen, (255, 255, 255), (310, 100, 25, 15))
        pygame.draw.rect(screen, (94, 44, 8), (280, 140, 40, 10))
        pygame.draw.rect(screen, (94, 44, 8), (280, 130, 10, 10))
        pygame.draw.rect(screen, (94, 44, 8), (310, 130, 10, 10))

      # elif event.type == pygame.MOUSEBUTTONDOWN:
        #     image_rect.centerx = event.pos[0]
        #     image_rect.centery = event.pos[1]
        #
        # elif event.type == pygame.MOUSEMOTION and event.buttons[0] == 1:
        #     image_rect.centerx = event.pos[0]
        #     image_rect.centery = event.pos[1]
