import pygame
from random import randint, randrange

pygame.init()
pygame.font.init()
WIN = pygame.display.set_mode((700,700))
pygame.display.set_caption("12am Snake")
BLOCK = 20
font_style = pygame.font.SysFont("Comic Sans", 50)

def screen(snake, apple, score, matrix):
    WIN.fill((0,0,0))
    xx = 40
    yy = 100
    zz = 0
    #Scoreboard
    scoreboard = font_style.render("Score: " + str(score), True, (23, 81, 126))
    WIN.blit(scoreboard, (100,30))
    #Snake
    for i in matrix:
        pygame.draw.rect(WIN, (xx, yy, zz), pygame.Rect(i[0], i[1], BLOCK, BLOCK))
        if zz >= 255:
            zz = 0
        else:
            zz += 5 
    #Apple
    pygame.draw.rect(WIN, (255, 80, 80), pygame.Rect(apple.x, apple.y, BLOCK, BLOCK))
    #Border
    pygame.draw.rect(WIN, (255,105,180), pygame.Rect(90, 90, 500, 500), 1) 


def gameOver():
    WIN.fill((0,0,0))
    display = font_style.render("Press spacebar to play again", True, (0,147,255))
    WIN.blit(display, (300, 350))
    pygame.display.update()
    if pygame.key.get_pressed()[pygame.K_SPACE]:
        run = True
        main()
    if pygame.key.get_pressed()[pygame.K_q]:
        pygame.quit()



def main():
    run = True
    clock = pygame.time.Clock()
    x1_change = 0
    y1_change = 0
    apple = pygame.draw.rect(WIN, (0,255,32), pygame.Rect((randint(0,24) * BLOCK) + 90, (randint(0,24) * BLOCK) + 90, BLOCK, BLOCK))
    snake = pygame.Rect((randint(0,24) * BLOCK) + 90, (randint(0,24) * BLOCK) + 90,  BLOCK, BLOCK)
    score = 0
    matrix = []
    while run:
        clock.tick(10)
        for event in pygame.event.get():
            keys = pygame.key.get_pressed()

            if event.type == pygame.QUIT:
                run = False

        
        if keys[pygame.K_LEFT] or keys[pygame.K_j]:
            x1_change = -BLOCK
            y1_change = 0
        if keys[pygame.K_RIGHT] or keys[pygame.K_l]:
            x1_change = BLOCK 
            y1_change = 0
        if keys[pygame.K_UP] or keys[pygame.K_i]:
            x1_change = 0 
            y1_change = -BLOCK 
        if keys[pygame.K_DOWN] or keys[pygame.K_k]:
            x1_change = 0 
            y1_change = BLOCK 

        snake.x += x1_change
        snake.y += y1_change
        if snake.x <= 80 or snake.x >= 589 or snake.y <= 80 or snake.y >= 589:
            run = False
        
        head = []
        head.append(snake.x)
        head.append(snake.y)
        matrix.append(head)
        if len(matrix) > score + 1:
            del matrix[0]

        for x in matrix[:-1]:
            if x == head:
                run = False

        if snake.colliderect(apple):
            apple.x = (randint(0,24) * BLOCK) + 90
            apple.y = (randint(0,24) * BLOCK) + 90
            #apple.x = round(randrange(0, 700 - BLOCK) / 20) * 20
            #apple.y = round(randrange(0, 700 - BLOCK) / 20) * 20
            score += 1


        screen(snake ,apple, score, matrix)
        pygame.display.update()
                
    gameOver()

if __name__ == "__main__":
    main()






# dont spawn food on blocks snake is already on

# fix gameOver function

# refresh drawing function faster?

