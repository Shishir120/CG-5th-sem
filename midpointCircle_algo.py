import pygame
import sys
pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("DDA Line ALgorithm")
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

def plot(x, y, xc, yc):
    screen.set_at((xc + x, yc + y), WHITE)
    screen.set_at((xc - x, yc + y), WHITE)
    screen.set_at((xc + x, yc - y), WHITE)
    screen.set_at((xc - x, yc - y), WHITE)
    screen.set_at((xc + y, yc + x), WHITE)
    screen.set_at((xc - y, yc + x), WHITE)
    screen.set_at((xc + y, yc - x), WHITE)
    screen.set_at((xc - y, yc - x), WHITE)

def midpointCicle_algo(xc, yc, r):

    # Calculate initial decision parameter
    d = 1 - r 
    x = 0
    y = r
    plot(x, y, xc, yc)

    while(x <= y):
        if d < 0:
            x = x + 1
            y = y
            d = d + 2*x + 1

        else:
            x = x + 1
            y = y - 1
            d = d + 2*x - 2*y + 1

        plot(x, y, xc, yc)



def main():
    xc = int(input("Enter x-coordinate of centre: "))
    yc = int(input("Enter y-coordinate of centre: "))
    r = int(input("Enter radius of circle: "))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill(BLACK)

        midpointCicle_algo(xc, yc, r)
        pygame.display.flip()   

    
if __name__ == "__main__" :
    main()
