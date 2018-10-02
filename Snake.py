import pygame
pygame.init()

gameSize = (700, 500)
black = (0, 0, 0)

snakeSegment = 50
speed = 50
snakeX = 300
snakeY = 300
direction = "right"

delay = 1000
move_event = pygame.USEREVENT + 1
pygame.time.set_timer(move_event, delay)

run = True

screen = pygame.display.set_mode(gameSize)
pygame.display.set_caption("Snake")

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                snakeX += speed
                direction = "right"
            elif event.key == pygame.K_LEFT:
                snakeX -= speed
                direction = "left"
            elif event.key == pygame.K_DOWN:
                snakeY += speed
                direction = "down"
            elif event.key == pygame.K_UP:
                snakeY -= speed
                direction = "up"
            pygame.event.clear()
            pygame.time.set_timer(move_event, delay)
        elif event.type == move_event:
            if direction == "right":
                snakeX += speed
            elif direction == "left":
                snakeX -= speed
            elif direction == "down":
                snakeY += speed
            elif direction == "up":
                snakeY -= speed

    screen.fill(black)
    pygame.draw.rect(screen, (0,255,0), (snakeX, snakeY, snakeSegment, snakeSegment))
    pygame.display.flip()

pygame.quit()
