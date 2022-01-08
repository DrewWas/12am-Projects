import pygame
from random import randint, choice
from pygame import draw, key

pygame.init()
pygame.font.init()
WIDTH, HEIGHT = 1400,700
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
FPS = 120
PLAYER1COLOR = (0,136,255)
PLAYER2COLOR = (255,0,0)
BALLCOLOR = (255,20,147)
VELOCITY = [-6,6]
pygame.display.set_caption("12am pong")


def draw_window(p1, p2, score1, score2, ball):
    WIN.fill((0,0,0))
    scoreboard0 = pygame.font.SysFont('Comic Sans', 100)
    textsurface = scoreboard0.render(str(score1), 1, PLAYER1COLOR)
    WIN.blit(textsurface, (365,25))
    scoreboard1 = pygame.font.SysFont('Comic Sans', 100)
    textsurface = scoreboard1.render(str(score2), 1, PLAYER2COLOR)
    WIN.blit(textsurface, (975,25))
    ball = pygame.draw.circle(WIN, (255,20,147), (ball.x, ball.y), 10)
    pygame.draw.rect(WIN, PLAYER1COLOR, pygame.Rect(p1.x, p1.y,10,120))
    pygame.draw.rect(WIN, PLAYER2COLOR, pygame.Rect(p2.x, p2.y, 10, 120))
    pygame.display.update()

def ballgo(ball, p1, p2):
    ball.x += VELOCITY[0]
    ball.y += VELOCITY[1]

    if ball.x - 10 > 1400 or ball.x < 0:
        VELOCITY[0] = -VELOCITY[0]
    if ball.y + 10 > 700 or ball.y < 0:
        VELOCITY[1] = -VELOCITY[1]
    if ball.colliderect(p1) == True:
        VELOCITY[0] = -VELOCITY[0]
    if ball.colliderect(p2) == True:
        VELOCITY[0] = - VELOCITY[0]


def main():
    score1 = 0
    score2 = 0
    p1 = pygame.Rect(15, randint(120,550), 10, 120)
    p2 = pygame.Rect(1375, randint(120,550), 10, 120)
    ball = pygame.Rect(randint(550,850), randint(250,450),10, 10)  
    clock = pygame.time.Clock()
    run = True
     
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_w] and p1.y > 10:
            p1.y -= 8
        if keys_pressed[pygame.K_s] and p1.y < 570:
            p1.y += 8
        if keys_pressed[pygame.K_UP] and p2.y > 10:
            p2.y -= 8
        if keys_pressed[pygame.K_DOWN] and p2.y < 570:
            p2.y += 8

        ballgo(ball, p1, p2)
        
        if ball.x < 0:
            score2 += 1
            ball.x = randint(550,850)
            ball.y = randint(120,550)
            VELOCITY[1] = VELOCITY[0]
        if ball.x > 1400:
            score1 += 1
            ball.x = randint(550,850)
            ball.y = randint(120,550)
            VELOCITY[0] = VELOCITY[1]

        draw_window(p1,p2,score1,score2, ball) 
        if score1 >= 11:
            winner = "Blue"
            winnercolor = PLAYER1COLOR
            gameOver(winner,winnercolor)        
        if score2 >= 11:
            winner = "Red"
            winnercolor = PLAYER2COLOR
            gameOver(winner, winnercolor)
    pygame.quit()





def homescreen():
    run = True
    while run:
        myfont = pygame.font.SysFont('Comic Sans', 50)
        textsurface = myfont.render("Press SpaceBar to Start", False, PLAYER1COLOR)
        WIN.blit(textsurface, (WIDTH/2 - 200,HEIGHT/2 - 30))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if pygame.key.get_pressed()[pygame.K_SPACE]:
                main()
    pygame.quit()


def gameOver(winner, winnercolor):
    run = True
    WIN.fill((0,0,0))
    while run:
        myfont = pygame.font.SysFont('Comic Sans', 60)
        textsurface0 = myfont.render(winner + " is the winner!!!", False, winnercolor)
        textsurface1 = myfont.render("Thanks for playing!!!", False, (255,20,147))
        textsurface2 = myfont.render("Hold [CTRL] + Q to Quit or tap Spacebar to Play Again", False, (255,255,255))
        WIN.blit(textsurface0, (WIDTH/2 - 270, HEIGHT/2 - 100))
        WIN.blit(textsurface1, (WIDTH/2 - 250,HEIGHT/2))
        WIN.blit(textsurface2, (WIDTH/2 - 525, HEIGHT/2 +100))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if pygame.key.get_pressed()[pygame.K_SPACE]:
                main()
    pygame.quit()

if __name__ == "__main__":
    homescreen()
