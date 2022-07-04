import pygame
from random import randint

pygame.init()
pygame.font.init()
WIDTH, HEIGHT = 1120, 700
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("12am Breakout")
player_pos = randint(100,700)
ballx = randint(100,1000)
bally = 400 
player = None
ball = None

def draw():
    WIN.fill((0,0,0))
    red = 250
    global player_pos, player
    global ball, ballx, bally

    #player
    player = pygame.draw.rect(WIN, (0,136,255), pygame.Rect(player_pos, 675, 100,20 ))

    #blocks 
    for i in range(6):
        for j in range(8):
            pygame.draw.rect(WIN, (red,36, 189), pygame.Rect(140 * j + 5,50 * i + 50, 130, 40))
        red -= 40

    #ball
    ball = pygame.draw.circle(WIN, (255,255,255), (ballx, bally), 12)


    pygame.display.update()


def gameOver():
    print("Game over")

def main():
    run = True
    clock = pygame.time.Clock()
    global player_pos, player
    global ball, ballx, bally

    VEL = [-6,6]

    while run:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] and player_pos > 10:
            player_pos -= 8
        if keys[pygame.K_RIGHT] and player_pos < 990:
            player_pos += 8 


        ballx += VEL[0]
        bally += VEL[1] 

        #logic
        if bally > 700:
            run = False
            gameOver()

        if ballx > 1090 or ballx < 5:
            VEL[0] = -VEL[0]


        #code below will change
        if bally > 680 or bally < 5:
            VEL[1] = -VEL[1]

        """
        if ball.colliderect(player) == True:
            VEL[0] = -VEL[0]
        """
        draw()

    pygame.quit()


if __name__ == "__main__":
    main()



