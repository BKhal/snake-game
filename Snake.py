import pygame
pygame.init()

# Causes segments in snake body to follow movement of leading segment
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

# Game properties
gameSize = (700, 500)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)

# Snake default properties
snakeColour = green
snakeSegmentWidth = 50
speed = 50
snakeHeadX = 300
snakeHeadY = 300
direction = "right"
outlineWidth = 2

# Building snake
snakeHead = pygame.Rect(snakeHeadX, snakeHeadY, snakeSegmentWidth, snakeSegmentWidth)
snakeBody = snakeHead.copy()
snakeBody.x -= snakeSegmentWidth
snake = [snakeHead, snakeBody]

# Timer event properties
delay = 250
move_event = pygame.USEREVENT + 1
pygame.time.set_timer(move_event, delay)

run = True

screen = pygame.display.set_mode(gameSize)
pygame.display.set_caption("Snake")



# Main game
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        
        tempX = snakeHead.x
        tempY = snakeHead.y

        # Arrow key events
        if event.type == pygame.KEYDOWN:

            # Right key
            if event.key == pygame.K_RIGHT and (direction == "up" or direction == "down"):
                snakeHead.x += speed
                direction = "right"
                trail(tempX,tempY)
                pygame.time.set_timer(move_event, delay)
            
            # Left key
            elif event.key == pygame.K_LEFT and (direction == "up" or direction == "down"):
                snakeHead.x -= speed
                direction = "left"
                trail(tempX,tempY)
                pygame.time.set_timer(move_event, delay)
            
            # Down key
            elif event.key == pygame.K_DOWN and (direction == "right" or direction == "left"):
                snakeHead.y += speed
                direction = "down"
                trail(tempX,tempY)
                pygame.time.set_timer(move_event, delay)

            # Up key
            elif event.key == pygame.K_UP and (direction == "right" or direction == "left"):
                snakeHead.y -= speed
                direction = "up"
                trail(tempX,tempY)
                pygame.time.set_timer(move_event, delay)

            pygame.event.clear()

        # Timer based movement
        elif event.type == move_event:
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

    # Rebuilding snake after movement
    for snakeSegment in snake:
        pygame.draw.rect(screen, black, snakeSegment)
        pygame.draw.rect(screen, snakeColour, (snakeSegment.x + outlineWidth, snakeSegment.y + outlineWidth, snakeSegmentWidth - outlineWidth * 2, snakeSegmentWidth - outlineWidth * 2))
    pygame.display.flip()

pygame.quit()
