import pygame

pygame.init()
WINDOW_HEIGHT = 800
WINDOW_WIDTH = 1000
window = pygame.display.set_mode([WINDOW_WIDTH, WINDOW_HEIGHT])


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

        if keys[pygame.K_RIGHT] and self.rect.right <= WINDOW_WIDTH:
            self.rect.x += self.speed

        elif keys[pygame.K_LEFT] and self.rect.left >= 0:
            self.rect.x -= self.speed

    def fire(self):
        if len(self.bullet_group) < 5:
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
        if self.rect.y <= -50 or self.rect.y >= WINDOW_HEIGHT:
            self.kill()

class Ghost(pygame.sprite.Sprite):
    def __init__(self,x,y,speed):
        super().__init__()
        self.image = pygame.image.load("C:\\Users\\hp\\Desktop\\game png\\ghost.png")
        self.image = pygame.transform.scale(self.image,(30,30))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        self.bullet_group = pygame.sprite.Group()

        self.direction = 5
        self.speed = speed

    def update(self):
        self.rect.x += self.direction * self.speed

        if self.rect.x >= WINDOW_WIDTH - 50:
            self.direction = -5
            self.rect.y += 30
        elif self.rect.x <= 0:
            self.direction = 5
            self.rect.y += 30


clock = pygame.time.Clock()
player = Player(pos=(WINDOW_WIDTH // 2, WINDOW_HEIGHT), speed=5)
player_group = pygame.sprite.Group()
player_group.add(player)

y = 3
x = 10

ghosts = []

not_ghosts = 6

ghost = Ghost(x=y, y=x, speed=1)
ghost_group = pygame.sprite.Group()
ghost_group.add(ghost,ghost)

# for i in range(not_ghosts):
#     ghost = Ghost(x=y, y=x, speed=1)
#     ghost_group = pygame.sprite.Group()
#     ghost_group.add(ghost)

while True:
    clock.tick(90)
    window.fill((0, 0, 0))
    player_group.update()
    player_group.draw(window)

    player.bullet_group.update()
    player.bullet_group.draw(window)

    ghost = Ghost(x=y, y=x, speed=1)
    ghost_group.update()
    ghost_group.draw(window)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.fire()

    pygame.display.update()
