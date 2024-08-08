import pygame


class KeyboardInput:
    def __init__(self):
        self.track = False

    def check_key(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    self.track = True
                elif event.key == pygame.K_0:
                    self.track = False
                elif event.key == pygame.K_ESCAPE:
                    return False
        return True

    def is_tracking(self):
        return self.track
