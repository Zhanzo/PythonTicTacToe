from pygame.locals import *
import pygame
from app import App

def main():
    app = App()
    app.on_execute()
    while True:
        message = "Replay: RETURN. Exit: ESC"
        app.on_render(message)
        for event in pygame.event.get():
            if event.type is pygame.KEYDOWN:
                if (event.key is pygame.K_ESCAPE):
                    return
                if (event.key is pygame.K_RETURN):
                    app = App()
                    app.on_execute()

if __name__ == "__main__":
    main()
