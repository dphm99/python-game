import pygame

class Car(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("./assets/imgs/blueCar.png")
        self.rect = self.image.get_rect()
        self.rect.center = (50,10)
group = pygame.sprite.Group()
car = Car()
group.add(car)

pygame.init()
screen = pygame.display.set_mode((400,600))
isPlaying = True
clock = pygame.time.Clock()

while isPlaying:
    clock.tick(60)
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            isPlaying = False
    screen.fill((255,255,255))
    group.update()
    group.draw(screen)
pygame.quit()