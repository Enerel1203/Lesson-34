import pygame

pygame.init()

WIDTH, HEIGHT = 640, 480
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Two Sprite Game")

# Player controlled sprite (green)
player = pygame.Rect(300, 200, 60, 60)

enemy = pygame.Rect(100, 100, 60, 60)

speed = 5

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_UP]:
        player.y -= speed
    if keys[pygame.K_DOWN]:
        player.y += speed
    if keys[pygame.K_LEFT]:
        player.x -= speed
    if keys[pygame.K_RIGHT]:
        player.x += speed

    screen.fill((255, 255, 255))  # white background

    pygame.draw.rect(screen, (0, 255, 0), player)   
    pygame.draw.rect(screen, (255, 0, 0), enemy)   

    pygame.display.update()

pygame.quit()
