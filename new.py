import pygame

pygame.init()
size = (500, 300)
screen = pygame.display.set_mode(size, pygame.RESIZABLE)
url = "C:\\Users\\hp\\Desktop\\game png\\"


class Sprite(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()

        self.images = []

        for num in range(1, 6):
            img = pygame.image.load(url + f"exp{num}.png")
            img = pygame.transform.scale(img, (100, 100))
            self.images.append(img)

        self.index = 0
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]

    def update(self):
        if self.index < len(self.images) - 1:
            self.index += 1
            self.image = self.images[self.index]
        if self.index >= len(self.images) - 1:
            self.kill()


explosion_group = pygame.sprite.Group()
clock = pygame.time.Clock()

while True:
    screen.fill((50, 50, 50))

    clock.tick(30)
    explosion_group.draw(screen)
    explosion_group.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            explosion = Sprite(x=pos[0], y=pos[1])
            explosion_group.add(explosion)


    pygame.display.update()
