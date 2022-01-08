import pygame
from random import randint 


pygame.init()
pygame.font.init()
WIN = pygame.display.set_mode((700,700))
pygame.display.set_caption("12am Snake")
BLOCK = 30


def screen(snake, apple, score):
    WIN.fill((0,0,0))
    #Scoreboard
    scoreboard = pygame.font.SysFont("Comic Sans", 75)
    textsurface = scoreboard.render("Score: " + str(score), 1, (80, 104, 235))
    WIN.blit(textsurface, (250, 50))
    #Border
    pygame.draw.rect(WIN, (255,105,180), pygame.Rect(95, 95, 510, 510), 1)
    #Snake
    pygame.draw.rect(WIN, (0,147,255), pygame.Rect(snake.x, snake.y, BLOCK, BLOCK))
    #Apple
    pygame.draw.rect(WIN, (102, 255, 102), pygame.Rect(apple.x, apple.y, BLOCK, BLOCK))
    pygame.display.update()






def main():
    run = True
    clock = pygame.time.Clock()
    snake = pygame.Rect(randint(97,573), randint(97,573), BLOCK, BLOCK)
    apple = pygame.Rect(randint(97, 573), randint(97, 573), BLOCK, BLOCK)
    score = 0
    while run:
        clock.tick(120)
        for event in pygame.event.get():
            keys = pygame.key.get_pressed()
            eat = snake.colliderect(apple)
            if event.type == pygame.QUIT:
                run = False
            if keys[pygame.K_w] and snake.y >= 103:
                snake.y -= 10
            if keys[pygame.K_s] and snake.y <= 568:
                snake.y += 10
            if keys[pygame.K_d] and snake.x <= 568:
                snake.x += 20
            if keys[pygame.K_a] and snake.x >= 103:
                snake.x -= 20
            if eat: 
                apple.x = randint(97, 573)
                apple.y = randint(97, 573)
                score += 1
                print(score)

            screen(snake, apple, score)
                
    pygame.quit()


if __name__ == "__main__":
    main()




# fix git

# scoreboard

# make blocks run smoother (and makes blocks smaller)

# put everything in grid 

# snake gets longer

# fix border stuff

