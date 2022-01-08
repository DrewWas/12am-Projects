import pygame

pygame.init()
WIN = pygame.display.set_mode((700,700))

def main():
    run = True
    clock = pygame.time.Clock()
    x = 100
    y = 100
    while run:
        clock.tick(40)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            WIN.fill((0,0,0))
            pygame.draw.rect(WIN, (255,255,255), pygame.Rect(x, y, 30,30))
            x += 5
            y += 5
            pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    main()
