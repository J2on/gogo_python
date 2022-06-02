import pygame
import sys

#define a Main Class
class Gogo:
    def __init__(self):
        # initalize the pygame module
        pygame.init()
        self.running = True

        # screen size 1920X1080
        self.screen = pygame.display.set_mode((1920,1080))

        # set logo and name
        logo = pygame.image.load("logogo.jpg")
        pygame.display.set_icon(logo)
        pygame.display.set_caption("Gogo")

    #define game loop
    def loop(self):
        gameRun = True
        while gameRun:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameRun = False

        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    game = Gogo()
    game.loop()
