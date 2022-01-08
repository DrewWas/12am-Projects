import pygame
from pygame import Color, draw
from random import choice


pygame.init()
WIDTH, HEIGHT = 600,700
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
FirstBlocks = [COLOR2, COLOR4]



def drawWindow(score):
    WIN.fill((0,0,0))
    pygame.draw.rect(WIN, (255,255,255), pygame.Rect(20,120,560,560), 3)
    generateBlocks()
    pygame.display.update()
    


def generateBlocks():
    #Generate 2 blocks in at random grid points (grid of 4x4)

    #Grid coordinates
    A = 40
    B = 175
    C = 310
    D = 445
    W = 140
    X = 275
    Y = 410
    Z = 545
    GRID = [[A,W], [B,W], [C,W], [D,W],
            [A,X], [B,X], [C,X], [D,X],
            [A,Y], [B,Y], [C,Y], [D,Y],
            [A,Z], [B,Z], [C,Z], [D,Z]
    ]

    BLOCKSIZE = 115
    pygame.draw.rect(WIN, FirstBlocks[1], pygame.Rect(A,Y, BLOCKSIZE, BLOCKSIZE))
    #LEFT OFF HERE.....    need the block to generate in one random position and stay there until further input
   
    


    #If user swipes up, they blocks go up until they hit another block, the ceiling, or dont move if there is already one above

    #If user swipes down/over, same rules apply

    #While the blocks are moving up, they slowly move (they dont automatically appear)

    #After the swipe, new 2 or 4 valued blocks appear relative to where they swiped (and not where there are already blocks)





def main():
    run = True
    clock = pygame.time.Clock()
    score = 0

    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        drawWindow(score)
        
    
    pygame.quit()


if __name__ ==  "__main__": 
    main()
        




#TO DO 

#Scoreboard that doesnt suck

#Add numbers to the squares