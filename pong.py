import pygame ##probleem met versie van python via VS-code, opgelost via versiecontrole onderaan lint
pygame.init()

width, height = 700, 500
win = pygame.display.set_mode((width,height))
pygame.display.set_caption("PONG")

def main():
    run = True

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
    pygame.quit()

if __name__ == '__main__':
    main()