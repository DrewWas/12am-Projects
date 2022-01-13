import pygame

pygame.init()
WIN = pygame.display.set_mode((1000, 800))
pygame.display.set_caption("Worlds Hardest Game")


def one():
    #Starting and ending areas
    pygame.draw.rect(WIN, (144,238,144), pygame.Rect(50, 250, 150, 300))
    pygame.draw.rect(WIN, (144,238, 144), pygame.Rect(800, 250, 150, 300))
    #Middle grid
    for i in range(13):
        for j in range(6):
            pygame.draw.rect(WIN, (197,212,250), pygame.Rect((i*2) * 20 + 250, (j*2) * 20 + 285, 20, 20))
    #Borders
    pygame.draw.line(WIN, (0,0,0), (50,250), (50,550), 2)
    pygame.draw.line(WIN, (0,0,0), (50,550), (310,550), 2)
    pygame.draw.line(WIN, (0,0,0), (310,550), (310,505), 2)
    pygame.draw.line(WIN, (0,0,0), (310,505), (750,505), 2)
    pygame.draw.line(WIN, (0,0,0), (750,505), (750,285), 2)
    pygame.draw.line(WIN, (0,0,0), (750,285), (800, 285), 2)
    pygame.draw.line(WIN, (0,0,0), (50,250), (200,250), 2)
    pygame.draw.line(WIN, (0,0,0), (200,250), (200,505), 2)
    pygame.draw.line(WIN, (0,0,0), (200,505), (250,505), 2)
    pygame.draw.line(WIN, (0,0,0), (250,505), (250,285), 2)
    pygame.draw.line(WIN, (0,0,0), (250,285), (690,285), 2)
    pygame.draw.line(WIN, (0,0,0), (690, 285), (690, 250), 2)
    pygame.draw.line(WIN, (0,0,0), (690, 250), (950, 250), 2)
    pygame.draw.line(WIN, (0,0,0), (800, 550), (950, 550), 2)
    pygame.draw.line(WIN, (0,0,0), (950, 250), (950, 550), 2)
    pygame.draw.line(WIN, (0,0,0), (800,550), (800, 285), 2)
     



def draw(player, score, circle1, circle2, circle3, circle4, circle5, circle6):
    WIN.fill((220,220,220))
    if score == 1:
        one()
    pygame.draw.rect(WIN, (0,147,255), pygame.Rect(player.x, player.y, 25, 25))
    pygame.draw.circle(WIN, (255,102,108), (circle1.x, circle1.y), 15)
    pygame.draw.circle(WIN, (255,102,108), (circle2.x, circle2.y), 15)
    pygame.draw.circle(WIN, (255,102,108), (circle3.x, circle3.y), 15)
    pygame.draw.circle(WIN, (255,102,108), (circle4.x, circle4.y), 15)
    pygame.draw.circle(WIN, (255,102,108), (circle5.x, circle5.y), 15)
    pygame.draw.circle(WIN, (255,102,108), (circle6.x, circle6.y), 15)
    pygame.display.update()


def main():
    run = True
    score = 1
    player = pygame.Rect(100,320,25,25)
    circle1 = pygame.Rect(270,375,10,10)
    circle2 = pygame.Rect(270,455,10,10)
    circle3 = pygame.Rect(730,335,10,10)
    circle4 = pygame.Rect(730,490,10,10)
    circle5 = pygame.Rect(270,302,10,10)
    circle6 = pygame.Rect(730,415,10,10)
    circle1Vel = 7
    circle3Vel = -7
    while run:
        pygame.time.Clock().tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        if pygame.key.get_pressed()[pygame.K_UP]:
            player.y -= 5 
        if pygame.key.get_pressed()[pygame.K_DOWN]:
            player.y += 5 
        if pygame.key.get_pressed()[pygame.K_RIGHT]:
            player.x += 5 
        if pygame.key.get_pressed()[pygame.K_LEFT]:
            player.x -= 5 
       
        circle1.x += circle1Vel
        circle2.x += circle1Vel
        circle3.x += circle3Vel
        circle4.x += circle3Vel
        circle5.x += circle1Vel
        circle6.x += circle3Vel

        if circle1.x >= 730:
            circle1Vel = -7
        if circle1.x <= 270:
            circle1Vel = 7
        if circle3.x <= 270:
            circle3Vel = 7
        if circle3.x >= 730:
            circle3Vel = -7

        # check if player touches finish line and increase score so draw
        # function calls next level, may have to fuck around with parameters
        draw(player, score, circle1, circle2, circle3, circle4, circle5, circle6)


    pygame.quit()


if __name__ == "__main__":
    main()
