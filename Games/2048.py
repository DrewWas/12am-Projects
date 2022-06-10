import pygame
from pygame import Color, draw
from random import choice


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

    pygame.display.update()
    

def main():
    run = True
    clock = pygame.time.Clock()
    score = 0

    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        # This is where game functionality goes
        
        drawWindow()
        
    
    pygame.quit()


if __name__ ==  "__main__": 
    main()
        
