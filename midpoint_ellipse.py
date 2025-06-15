import pygame
import sys

pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Midpoint Ellipse Algorithm")
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

def plot(x, y, xc, yc):
    screen.set_at((round(xc + x), round(yc + y)), WHITE)
    screen.set_at((round(xc - x), round(yc + y)), WHITE)
    screen.set_at((round(xc + x), round(yc - y)), WHITE)
    screen.set_at((round(xc - x), round(yc - y)), WHITE)

def midpoint_ellipse(rx, ry, xc, yc):
    x = 0
    y = ry

    # Region 1
    p1 = ry**2 - rx**2 * ry + 0.25 * rx**2

    while (2 * ry**2 * x) < (2 * rx**2 * y):
        x += 1
        if p1 < 0:
            p1 = p1 + 2 * ry**2 * x + ry**2
        else:
            y -= 1
            p1 = p1 + 2 * ry**2 * x - 2 * rx**2 * y + ry**2

        plot(x, y, xc, yc)


    # Region 2
    p2 = ry**2 * (x + 0.5)**2 + rx**2 * (y - 1)**2 - rx**2 * ry**2

    while y >= 0:
        y -= 1
        if p2 > 0:
            p2 = p2 - 2 * rx**2 * y + rx**2
        else:
            x += 1
            p2 = p2 + 2 * ry**2 * x - 2 * rx**2 * y + rx**2

        plot(x, y, xc, yc)


def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill(BLACK)
        midpoint_ellipse(150, 100, WIDTH // 2, HEIGHT // 2)
        pygame.display.flip()

if __name__ == "__main__":
    main()
