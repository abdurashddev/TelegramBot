import pygame

pygame.init()

screen = pygame.display.set_mode([800, 800])

url = "C:\\Users\\hp\\Desktop\\game png\\"


class Explosion(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.images = []

        for i in range(1, 6):
            image = pygame.image.load(url + f"exp{i}.png")
            image = pygame.transform.scale(image, (100, 100))
            self.images.append(image)

        self.index = 0
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def update(self):
        if self.index < len(self.images):
            self.index += 1
            self.image = self.images[self.index]
        if self.index >= len(self.images) - 1:
            self.kill()


sprite_group = pygame.sprite.Group()
clock = pygame.time.Clock()

while True:
    screen.fill((0, 0, 0))
    sprite_group.draw(screen)
    sprite_group.update()
    clock.tick(10)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            exp = Explosion(x=pos[0], y=pos[1])
            sprite_group.add(exp)

    pygame.display.update()