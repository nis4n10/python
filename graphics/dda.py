import pygame
import sys

# Initialize pygame
pygame.init()

# Screen size
width = 800
height = 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("DDA Algorithm")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Taking values from user
print("Enter the first point:")
x1 = int(input())
y1 = int(input())

print("Enter the second point:")
x2 = int(input())
y2 = int(input())


def line_generation(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1

    steps = max(abs(dx), abs(dy))

    x_inc = dx / steps
    y_inc = dy / steps

    x = x1
    y = y1

    for i in range(steps):
        screen.set_at((round(x), round(y)), WHITE)
        x += x_inc
        y += y_inc

def main():
    screen.fill(BLACK)
    line_generation(x1, y1, x2, y2)
    pygame.display.flip()


# Event loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


# Display the line
if __name__=="__main__":
    main()