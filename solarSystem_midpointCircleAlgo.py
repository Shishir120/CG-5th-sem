import pygame
import sys
pygame.init()
WIDTH, HEIGHT = 1200, 1000
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

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill(BLACK)
        
        # Neptune
        midpointCicle_algo(600, 500, 450)
        midpointCicle_algo(800, 90, 30)

        # Uranus
        midpointCicle_algo(600, 500, 400)
        midpointCicle_algo(500, 120, 30)

        # Saturn
        midpointCicle_algo(600, 500, 350)
        midpointCicle_algo(800, 210, 30)

        # Jupiter
        midpointCicle_algo(600, 500, 300)
        midpointCicle_algo(400, 280, 30)

        # Mars
        midpointCicle_algo(600, 500, 250)
        midpointCicle_algo(700, 270, 30)

        # Earth
        midpointCicle_algo(600, 500, 200)
        midpointCicle_algo(500, 320, 30)

        # Venus
        midpointCicle_algo(600, 500, 150)
        midpointCicle_algo(500, 600, 30)

        # Mercury
        midpointCicle_algo(600, 500, 100)
        midpointCicle_algo(600, 600, 30)
        pygame.display.flip()   

    
if __name__ == "__main__" :
    main()
