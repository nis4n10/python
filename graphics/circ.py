import pygame
import sys

pygame.init()

width = 800
height = 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Midpoint Circle Algorithm")

white = (255, 255, 255)
black = (0, 0, 0)

# Midpoint Circle Drawing Algorithm
def circle(x1, y1, r):
    x = 0
    y = r
    d = 1 - r  
   
    
    
    while x < y:
        x += 1
        if d < 0:
            d += 2 * x + 1  
        else:
            y -= 1
            d += 2 * (x - y) + 1 

        
        screen.set_at((x1 + x, y1 + y), "WHITE")
        screen.set_at((x1 - x, y1 + y), "RED")
        screen.set_at((x1 + x, y1 - y), "GREEN")
        screen.set_at((x1 - x, y1 - y), "BLUE")
        screen.set_at((x1 + y, y1 + x), "PURPLE")
        screen.set_at((x1 - y, y1 + x), "ORANGE")
        screen.set_at((x1 + y, y1 - x), "YELLOW")
        screen.set_at((x1 - y, y1 - x), "CYAN")

def main():
    screen.fill(black)
    
    circle(400, 300, 100)
    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

if __name__ == "__main__":
    main()
