from time import sleep
import pygame
pygame.init()
pygame.display.set_caption("Монстрики")
class Area():
    def __init__(self, x, y, width, height,filename):
        self.rect = pygame.Rect(x, y, width, height)
        self.image = pygame.image.load(filename)
    
    def draw(self,boarder = (50,50,200)):
        window.blit(self.image,(self.rect.x,self.rect.y))
    
    def fill(self,boarder = (50,50,200)):
        pygame.draw.rect(window, self.color, self.rect)
        pygame.draw.rect(window, boarder, self.rect,10)

    def collide(self, other):
        return self.rect.colliderect(other.rect)

window = pygame.display.set_mode((500,500))
color = (215,155,162)
clock = pygame.time.Clock()

platform = Area(200, 300, 100, 23, 'platform.png')
platform.move_left = False
platform.move_right = False
ball = Area(220,200,50,50,'ball.png')
ball.speed_x = 3
ball.speed_y = 3

enemies = list()
for i in range(3):
    x = 5 + 25 * i
    y = 5 + 50 * i
    for j in range(9-i):
        enemy = Area(x+55*j,y,50,45, 'enemy.png')
        enemies.append(enemy)

sleep(3)
finish = False
while True:
    if not finish:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    platform.move_right = True
                elif event.key == pygame.K_LEFT:
                    platform.move_left = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    platform.move_right = False
                elif event.key == pygame.K_LEFT:
                    platform.move_left = False 
        if platform.move_right and platform.rect.right < 500:
            platform.rect.x += 5
        if platform.move_left and platform.rect.left > 0:
            platform.rect.x -= 5
        ball.rect.x += ball.speed_x
        ball.rect.y += ball.speed_y
        if ball.collide(platform):
            ball.speed_y = -1 * abs(ball.speed_y)
        if ball.rect.top < 0:
            ball.speed_y = abs(ball.speed_y)
        if ball.rect.left < 0 or ball.rect.right > 500:
            ball.speed_x *= -1

        window.fill(color)
        platform.draw()
        ball.draw()
        for enemy in enemies:
            if ball.collide(enemy):
                enemies.remove(enemy)
                ball.speed_y = abs(ball.speed_y)
            else:
                enemy.draw()
        if not enemies:
            image = pygame.font.SysFont('verdana', 70).render('WIN WIN', True, (255, 255, 255))
            window.blit(image, (150, 150))
            finish = True
        elif ball.rect.top > platform.rect.bottom:
            image = pygame.font.SysFont('verdana', 70).render('LOOSE', True, (255, 255, 255))
            window.blit(image, (150, 150))
            finish = True
    
    pygame.display.update()
    clock.tick(40)


