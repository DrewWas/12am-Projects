import pygame

pygame.init()
WIN = pygame.display.set_mode((1000, 800))
pygame.display.set_caption("Worlds Hardest Game")


def draw(player):
    WIN.fill((211,211,211))
    pygame.draw.rect(WIN, (0,147,255), pygame.Rect(player.x, player.y, 20, 20))
    pygame.display.update()


def main():
    run = True
    player = pygame.Rect(20,20, 300,400)
    while run:
        pygame.time.Clock().tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        if pygame.key.get_pressed()[pygame.K_UP]:
            player.y -= 3
        if pygame.key.get_pressed()[pygame.K_DOWN]:
            player.y += 3
        if pygame.key.get_pressed()[pygame.K_RIGHT]:
            player.x += 3
        if pygame.key.get_pressed()[pygame.K_LEFT]:
            player.x -= 3


        draw(player)


    pygame.quit()


if __name__ == "__main__":
    main()
