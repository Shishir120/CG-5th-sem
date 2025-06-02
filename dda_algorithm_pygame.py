import pygame
import sys
pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("DDA Line ALgorithm")
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

def dda(x1, y1, x2, y2):

    step = 1

    dx = abs(x2 - x1)    
    dy = abs(y2 - y1)    

    if dx > dy:
        step = dx
    else:
        step = dy

    xinc = dx / step
    yinc = dy / step

    x = x1
    y = y1
    screen.set_at((round(x), round(y)), WHITE)

    for i in range(step+1):

        x = x + xinc
        y = y + yinc
        screen.set_at((round(x), round(y)), WHITE)


def main():
    
    x1 = int(input("Enter value of x1: "))
    y1 = int(input("Enter value of y1: "))
    x2 = int(input("Enter value of x2: "))
    y2 = int(input("Enter value of y2: "))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill(BLACK)

        dda(x1, y1, x2, y2)
        pygame.display.flip()
    
if __name__ == "__main__" :
    main()