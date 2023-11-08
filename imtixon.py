import pygame

pygame.init()
screen = pygame.display.set_mode((595,600),pygame.RESIZABLE)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    key = pygame.key.get_pressed()
    if key[pygame.K_w]:

class Player():
    super().()

