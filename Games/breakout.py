import pygame
from random import randint

pygame.init()
pygame.font.init()
WIDTH, HEIGHT = 1120, 700
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("12am Breakout")
DIFF = 0

player_pos = randint(100,700)


def homescreen():
    WIN.fill((0,0,0))
    global DIFF

    my_font = pygame.font.SysFont("Arial", 50)
    title_surface = my_font.render("Select Difficulty", False, (255, 255, 255))
    
    pygame.draw.rect(WIN, (0,136,255), pygame.Rect(150, 250, 200, 200), 1, 0)
    easy_surface = my_font.render("Easy", False, (0,136,255))
    easy1_surface = my_font.render("Press 1", False, (0,136,255))

    pygame.draw.rect(WIN, (0,136,25), pygame.Rect(450, 250, 200, 200), 1, 0)
    med_surface = my_font.render("Medium", False, (0,136,25))
    med1_surface = my_font.render("Press 2", False, (0,136,25))

    pygame.draw.rect(WIN, (200,36,25), pygame.Rect(750, 250, 200, 200), 1, 0)
    hard_surface = my_font.render("Hard", False, (200,36,25))
    hard1_surface = my_font.render("Press 3", False, (200,36,25))



    WIN.blit(title_surface, (375,100))

    WIN.blit(easy_surface, (200, 270))
    WIN.blit(easy1_surface, (170, 350))
    WIN.blit(med_surface, (460, 270))
    WIN.blit(med1_surface, (470, 350))
    WIN.blit(hard_surface, (800, 270))
    WIN.blit(hard1_surface, (770, 350))

    #DIFF = int(input())




    pygame.display.update()




def draw():
    WIN.fill((0,0,0))
    red = 250
    global player_pos
    global DIFF

    #player
    pygame.draw.rect(WIN, (0,136,255), pygame.Rect(player_pos, 675, 100,20 ))

    #blocks 
    for i in range(3):
        for j in range(8):
            pygame.draw.rect(WIN, (red,36, 189), pygame.Rect(140 * j + 5,50 * i + 50, 130, 40))
        red -= 40

    print(DIFF)
            

    pygame.display.update()


def main():
    run = True
    clock = pygame.time.Clock()
    global player_pos

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

        draw()

    pygame.quit()


def gameover():
    return 0



if __name__ == "__main__":
    homescreen()



