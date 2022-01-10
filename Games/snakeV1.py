import pygame
from random import randint 

pygame.init()
pygame.font.init()
WIN = pygame.display.set_mode((700,700))
pygame.display.set_caption("12am Snake")
BLOCK = 20
font_style = pygame.font.SysFont("Comic Sans", 50)

def screen(snake, apple, score, matrix, lives):
    WIN.fill((0,0,0))
    #Scoreboard
    scoreboard = font_style.render("Score: " + str(score), True, (23, 81, 126))
    livesDisplay = font_style.render("Lives left: " + str(lives), True, (23, 81, 126))
    WIN.blit(scoreboard, (100,30))
    WIN.blit(livesDisplay, (350, 30))
    #GRID 
    for i in range(25):
        for j in range(25):
            pygame.draw.rect(WIN, (255,255,255), pygame.Rect(i * BLOCK + 90, j * BLOCK + 90, BLOCK, BLOCK), 1)
    #Snake
    for i in matrix:
        pygame.draw.rect(WIN, (0,147,255), pygame.Rect(i[0], i[1], BLOCK, BLOCK))
    #Apple
    pygame.draw.rect(WIN, (102, 255, 102), pygame.Rect(apple.x, apple.y, BLOCK, BLOCK))
    #Border
    pygame.draw.rect(WIN, (255,105,180), pygame.Rect(90, 90, 500, 500), 1) 





def main():
    run = True
    clock = pygame.time.Clock()
    x1_change = 0
    y1_change = 0
    apple = pygame.draw.rect(WIN, (0,255,32), pygame.Rect((randint(0,24) * BLOCK) + 90, (randint(0,24) * BLOCK) + 90, BLOCK, BLOCK))
    snake = pygame.Rect((randint(0,24) * BLOCK) + 90, (randint(0,24) * BLOCK) + 90,  BLOCK, BLOCK)
    score = 0
    lives = 3
    matrix = []
    while run:
        clock.tick(120)
        for event in pygame.event.get():
            keys = pygame.key.get_pressed()

            if event.type == pygame.QUIT:
                run = False


        if keys[pygame.K_UP]:
            x1_change = 0
            y1_change = -2
        if keys[pygame.K_DOWN]:
            x1_change = 0
            y1_change = 2
        if keys[pygame.K_RIGHT]:
            x1_change = 2
            y1_change = 0
        if keys[pygame.K_LEFT]:
            x1_change = -2
            y1_change = 0
        snake.x += x1_change
        snake.y += y1_change
        
        if snake.x <= 95 or snake.x >= 589 or snake.y <= 95 or snake.y >= 589:
            lives -= 1
        
        head = []
        head.append(snake.x)
        head.append(snake.y)
        matrix.append(head)
        if len(matrix) > score + 1:
            del matrix[0]

        if snake.colliderect(apple):
            apple.x = (randint(0,24) * BLOCK) + 90
            apple.y = (randint(0,24) * BLOCK) + 90
            score += 1

        screen(snake ,apple, score, matrix, lives)
        pygame.display.update()
                
    pygame.quit()


if __name__ == "__main__":
    main()




# put snake in  grid 

# implement lives (3 lives) and game over screeen
#^ game over screen includes restart button... this means we may have to also make a homescreeen

# fix border stuff
# lives border may need to be updated to accomodate new grid

# snake grows by 20px (original size) when it eats an apple
# as of rn snake only grows by 2pxs and program redraws squares on top of each other
# should draw sqaures side by side, not on top of each other

# dont spawn food on blocks snake is already on

# game over if snake hits border or itself
