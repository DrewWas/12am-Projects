import pygame
from pygame import Color, draw, key
from random import choice, randint


pygame.init()
WIDTH, HEIGHT = 700,750
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
FPS = 60
COLOR2 = (255,0,0)
COLOR4 = (252,84,0)
COLOR8 = (209,146,0)
COLOR16 = (65,186,0)
COLOR32 = (0,199,119)
COLOR64 = (0,199,199)
COLOR128 = (0,136,199)
COLOR256 = (0,36,199) 
COLOR512 = (86,0, 199)
COLOR1024 = (143, 0, 199)
COLOR2048 = (199,0,169)
COLOR_PLUS = (199,0,86)
pygame.display.set_caption("2048")



x1 = (randint(0,3) * 19) * 7.7 + 62
x2 = (randint(0,3) * 19) * 7.7 + 62
y1 = (randint(0,3) * 19) * 7.7 + 110
y2 = (randint(0,3) * 19) * 7.7 + 110

def drawWindow():
    WIN.fill((250,248,239))
    # Border(s)
    border_vert_x = 205
    border_horz_y = 255 
    pygame.draw.rect(WIN, (187,173,160), pygame.Rect(50,100,600,600), 15, 10)
    for i in range(3):
        pygame.draw.line(WIN, (187, 173, 160), (border_vert_x,100), (border_vert_x,690), width=15)
        border_vert_x += 145
    for i in range(3):
        pygame.draw.line(WIN, (187, 173, 160), (50, border_horz_y), (640, border_horz_y), width=15)
        border_horz_y += 145

    # Blank/filler squares
    for i in range(4):
        for j in range(4):
            pygame.draw.rect(WIN, (205,192,180), pygame.Rect((i * 19) * 7.7 + 62, (j * 19) * 7.7 + 110, 140, 140), 0, 8)

    # Scoreboard
    
    cubes()

    pygame.display.update()
    




def cubes():
    # get two squares to spawn in random positions with each reload
    pygame.draw.rect(WIN, (0,138,255), pygame.Rect(x1, y1, 140, 140), 0, 8)
    pygame.draw.rect(WIN, (0,138,255), pygame.Rect(x2, y2, 140, 140), 0, 8)
    
    # with every move a new cube spawns in  

    # cubes only spawn in open squares

    # they stop if they hit the borders or another cube (of a different type)

    # if it hits a cube of the same color/type, they combine

    # Put numbers on the cubes

    # Add a scoreboard



def main():
    global x1, y1
    run = True
    clock = pygame.time.Clock()
    score = 0

    xchange = 0
    ychange = 0

    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False


        # get them to only move within the grid
        if pygame.key.get_pressed()[pygame.K_UP]:    # end of this line will be implementation of how to stop it from colliding
            y1 = y1 - 10
        if pygame.key.get_pressed()[pygame.K_DOWN]:
            y1 = y1 + 10
        if pygame.key.get_pressed()[pygame.K_RIGHT]:
            x1 = x1 + 10
        if pygame.key.get_pressed()[pygame.K_LEFT]:
            x1 = x1 - 10


        # This is where game functionality goes
        drawWindow()
    pygame.quit()


if __name__ ==  "__main__": 
    main()
        
