import pygame ##probleem met versie van python via VS-code, opgelost via versiecontrole onderaan lint
pygame.init()

width, height = 700, 500
win = pygame.display.set_mode((width,height))
pygame.display.set_caption("PONG")

FPS = 60

white = (255,255,255)
black = (0,0,0)

PADDLE_WIDTH, PADDLE_HEIGHT= 20,100


class Paddle:
    color = white

    def __init__(self,x,y,width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def draw (self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height))

def draw(win, paddles):
    win.fill(black)

    for paddle in paddles:
        paddle.draw(win)

    pygame.display.update()

def main():
    run = True
    clock = pygame.time.Clock()

    left_paddle = Paddle(10, height//2 - PADDLE_HEIGHT//2, PADDLE_WIDTH, PADDLE_HEIGHT )
    right_paddle = Paddle(width - 10 - PADDLE_WIDTH, height //2 - PADDLE_HEIGHT //2,  PADDLE_WIDTH, PADDLE_HEIGHT)

    while run:
        clock.tick(FPS) ##regulate speed
        draw(win, [left_paddle, right_paddle])


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break


    pygame.quit()

if __name__ == '__main__':
    main()