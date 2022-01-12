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




def draw(player, score):
    WIN.fill((220,220,220))
    if score == 1:
        one()
    pygame.draw.rect(WIN, (0,147,255), pygame.Rect(player.x, player.y, 20, 20))
    pygame.display.update()


def main():
    run = True
    score = 1
    player = pygame.Rect(100, 320, 20, 20)
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
        
        # check if player touches finish line and increase score so draw
        # function calls next level, may have to fuck around with parameters

        draw(player, score)


    pygame.quit()


if __name__ == "__main__":
    main()
