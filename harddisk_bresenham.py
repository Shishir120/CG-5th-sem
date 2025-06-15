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
    # x1 = int(input("Enter value of x1: "))
    # y1 = int(input("Enter value of y1: "))
    # x2 = int(input("Enter value of x2: "))
    # y2 = int(input("Enter value of y2: "))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill(BLACK)

        # Hardisk Layout
        bresenham(20, 20, 20, 550)
        bresenham(20, 550, 600, 550)
        bresenham(600, 550, 600, 20)
        bresenham(600, 20, 20, 20)

        bresenham(100, 20, 100, 200)
        bresenham(100, 200, 520, 200)
        bresenham(520, 200, 520, 20)

        bresenham(200, 20, 200, 100)
        bresenham(200, 100, 400, 100)
        bresenham(400, 100, 400, 20)

        bresenham(20, 275, 600, 275)


        bresenham(100, 550, 100, 400)
        bresenham(100, 400, 520, 400)
        bresenham(520, 400, 520, 550)

        bresenham(200, 550, 200, 470)
        bresenham(200, 470, 400, 470)
        bresenham(400, 470, 400, 550)


        pygame.display.flip()   

    
if __name__ == "__main__" :
    main()
