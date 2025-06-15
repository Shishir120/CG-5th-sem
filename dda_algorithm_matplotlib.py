import pygame
import matplotlib.pyplot as plt

def dda(x1, y1, x2, y2):
    xPoints = []
    yPoints = []
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

    for i in range(step):

        xPoints.append(round(x))
        yPoints.append(round(y))

        x = x + xinc
        y = y + yinc

    plt.title("Line using DDA Algorithm")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.plot(xPoints, yPoints, marker='o', color='blue')
    plt.show()


x1 = int(input("Enter value of x1: "))
y1 = int(input("Enter value of y1: "))
x2 = int(input("Enter value of x2: "))
y2 = int(input("Enter value of y2: "))


dda(x1, y1, x2, y2)