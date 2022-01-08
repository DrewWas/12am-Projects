import pygame
from random import randint 


pygame.init()
pygame.font.init()
WIN = pygame.display.set_mode((700,700))
pygame.display.set_caption("12am Snake")
BLOCK = 20
font_style = pygame.font.SysFont("Comic Sans", 70)


def screen(snake, apple, score):
    WIN.fill((0,0,0))
    #Scoreboard
    scoreboard = font_style.render("Score: " + str(score), True, (23, 81, 126))
    WIN.blit(scoreboard, (240,30))
    #Border
    pygame.draw.rect(WIN, (255,105,180), pygame.Rect(95, 95, 510, 510), 1)
    #Snake
    pygame.draw.rect(WIN, (0,147,255), pygame.Rect(snake.x, snake.y, BLOCK, BLOCK))
    #Apple
    pygame.draw.rect(WIN, (102, 255, 102), pygame.Rect(apple.x, apple.y, BLOCK, BLOCK))
    





def main():
    run = True
    clock = pygame.time.Clock()
    x1_change = 0
    y1_change = 0
    snake = pygame.Rect(randint(97, 573), randint(97, 573), BLOCK, BLOCK)
    apple = pygame.Rect(randint(97, 573), randint(97, 573), BLOCK, BLOCK)
    score = 0
    while run:
        clock.tick(120)
        for event in pygame.event.get():
            keys = pygame.key.get_pressed()
            eat = snake.colliderect(apple)

            if event.type == pygame.QUIT:
                run = False
            
            if eat: 
                apple.x = randint(97, 573)
                apple.y = randint(97, 573)
                score += 1


        if keys[pygame.K_UP]:
            x1_change = 0
            y1_change = -3
        if keys[pygame.K_DOWN]:
            x1_change = 0
            y1_change = 3
        if keys[pygame.K_RIGHT]:
            x1_change = 3
            y1_change = 0
        if keys[pygame.K_LEFT]:
            x1_change = -3
            y1_change = 0
        snake.x += x1_change
        snake.y += y1_change 

        screen(snake, apple, score)
        pygame.display.update()
                
    pygame.quit()


if __name__ == "__main__":
    main()





# put everything in grid 

# snake gets longer

# implement lives (3 lives) and game over screeen
#^ game over screen includes restart button... this means we may have to also make a homescreeen

# fix border stuff

# fix the fact that sometimes the apple/score doesnt update when the snake touches it 
#^ (probably has to do with plavement of the if statement 

# game over if snake hits border or itself
