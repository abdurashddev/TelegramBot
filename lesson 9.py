import pygame

screen = pygame.display.set_mode([1000, 800])
clock = pygame.time.Clock()


class Player(pygame.sprite.Sprite):
    def __init__(self, pos, speed):
        super().__init__()
        self.image = pygame.image.load("C:\\Users\\hp\\Desktop\\game png\\ship.png")
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect(midbottom=pos)
        self.speed = speed
        self.bullet_group = pygame.sprite.Group()

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.x >= 0:
            self.rect.x -= self.speed

        elif keys[pygame.K_RIGHT] and self.rect.x <= 900:
            self.rect.x += 10

        if keys[pygame.K_UP]:
            self.fire()

    def fire(self):
        if len(self.bullet_group) < 4:
            bullet = Laser((self.rect.centerx, self.rect.top), speed=-8)
            self.bullet_group.add(bullet)


class Laser(pygame.sprite.Sprite):
    def __init__(self, pos, speed):
        super().__init__()
        self.image = pygame.image.load("C:\\Users\\hp\\Desktop\\game png\\as.jpg")
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.rect = self.image.get_rect(center=pos)
        self.speed = speed

    def update(self):
        self.rect.y += self.speed
        if self.rect.y <= -50 or self.rect.y >= 800:
            self.kill()


player = Player(pos=(800, 780), speed=5)
player_group = pygame.sprite.Group()
player_group.add(player)

while True:

    clock.tick(90)
    screen.fill((0, 0, 0))

    player_group.update()
    player_group.draw(screen)

    player.bullet_group.update()
    player.bullet_group.draw(screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.fire()

    pygame.display.update()
