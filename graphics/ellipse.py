import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the screen
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Implementation of Midpoint Ellipse Algorithm")


BLACK = (0, 0, 0)
RED = (255, 0, 0)

def draw_ellipse(xc, yc, rx, ry):
    x = 0
    y = ry
    p1 = round(ry * ry - rx * rx * ry + 0.25 * rx * rx)

    # First region of the ellipse (ellipse from the top to bottom)
    while (2 * ry * ry * x) <= (2 * rx * rx * y):
        if p1 < 0:
            x += 1
            p1 += (2 * ry * ry * x) + ry * ry
        else:
            x += 1
            y -= 1
            p1 += (2 * ry * ry * x) - (2 * rx * rx * y) + ry * ry

        screen.set_at((xc + x, yc + y), 'YELLOW')
        screen.set_at((xc + x, yc - y), 'GREEN')
        screen.set_at((xc - x, yc + y), 'RED')
        screen.set_at((xc - x, yc - y), 'WHITE')

   
    p2 = round(ry * ry * (x + 0.5) ** 2 + rx * rx * (y - 1) ** 2 - rx * rx * ry * ry)
    while y > 0:
        if p2 > 0:
            y -= 1
            p2 -= (2 * rx * rx * y) + rx * rx
        else:
            x += 1
            y -= 1
            p2 += (2 * ry * ry * x) - (2 * rx * rx * y) + rx * rx

    
        screen.set_at((xc + x, yc + y), RED)
        screen.set_at((xc + x, yc - y), 'GREEN')
        screen.set_at((xc - x, yc + y), 'BLUE')
        screen.set_at((xc - x, yc - y), 'PURPLE')


def get_user_input():
   
    xc = int(input("Enter the center X-coordinate of the ellipse: "))
    yc = int(input("Enter the center Y-coordinate of the ellipse: "))
    rx = int(input("Enter the major axis  of the ellipse: "))
    ry = int(input("Enter the minor axis of the ellipse: "))
    return xc, yc, rx, ry


def main():
    
    xc, yc, rx, ry = get_user_input()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(BLACK)
        draw_ellipse(xc, yc, rx, ry) 
        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
