import pygame
import sys
pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("DDA Line ALgorithm")
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

def bresenham(x1, y1, x2, y2):
    dx = abs(x2-x1)
    dy = abs(y2-y1)

    x = x1
    y = y1

    if x2 > x1:
        lx = 1
    else:
        lx = -1

    if y2 > y1:
        ly = 1
    else:
        ly = -1

    if dx > dy:
        p = 2 * dy - dx

        while(x != x2):
            if p < 0 :
                x = x + lx
                y = y
                p = p + 2 * dy
            else:
                x = x + lx
                y = y + ly
                p = p + 2 * dy - 2 * dx

            screen.set_at((round(x), round(y)), WHITE)

    else:
        p = 2 * dx - dy

        while(y != y2):
            if p < 0 :
                x = x 
                y = y + ly
                p = p + 2 * dx
            else:
                x = x + lx
                y = y + ly
                p = p + 2 * dx - 2 * dy

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

        bresenham(x1, y1, x2, y2)
        pygame.display.flip()   

    
if __name__ == "__main__" :
    main()

