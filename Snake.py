import pygame
pygame.init()

def trail(tempHeadX, tempHeadY):
    tempX = 0
    tempY = 0
    for snakeSegment in snake:
        if snakeSegment == snakeHead:
            continue
        else:
            tempX = snakeSegment.x
            tempY = snakeSegment.y
            snakeSegment.x = tempHeadX
            snakeSegment.y = tempHeadY
            tempHeadX = tempX
            tempHeadY = tempY

gameSize = (700, 500)
black = (0, 0, 0)
snakeColour = (0, 255, 0)
red = (255, 0, 0)

snakeSegmentWidth = 50
speed = 50
snakeHeadX = 300
snakeHeadY = 300
direction = "right"

snakeHead = pygame.Rect(snakeHeadX, snakeHeadY, snakeSegmentWidth, snakeSegmentWidth)
snakeBody = snakeHead.copy()
snakeBody.x -= snakeSegmentWidth
snake = [snakeHead, snakeBody]

delay = 250
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
            tempX = snakeHead.x
            tempY = snakeHead.y
            if event.key == pygame.K_RIGHT:
                snakeHead.x += speed
                direction = "right"
            elif event.key == pygame.K_LEFT:
                snakeHead.x -= speed
                direction = "left"
            elif event.key == pygame.K_DOWN:
                snakeHead.y += speed
                direction = "down"
            elif event.key == pygame.K_UP:
                snakeHead.y -= speed
                direction = "up"
            trail(tempX,tempY)
            pygame.event.clear()
            pygame.time.set_timer(move_event, delay)
        elif event.type == move_event:
            tempX = snakeHead.x
            tempY = snakeHead.y
            if direction == "right":
                snakeHead.x += speed
            elif direction == "left":
                snakeHead.x -= speed
            elif direction == "down":
                snakeHead.y += speed
            elif direction == "up":
                snakeHead.y -= speed
            trail(tempX,tempY)

    screen.fill(black)
    for snakeSegment in snake:
        pygame.draw.rect(screen, snakeColour, snakeSegment)
    pygame.display.flip()

pygame.quit()
