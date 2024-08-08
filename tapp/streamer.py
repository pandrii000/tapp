import cv2
import pygame


class Streamer:
    def __init__(self, width, height):
        pygame.init()
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Tracker")

    def show_frame(self, frame, points=None):
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame_rgb = pygame.surfarray.make_surface(frame_rgb.swapaxes(0, 1))

        if points is not None:
            for point in points:
                pygame.draw.circle(
                    frame_rgb, (255, 0, 0), (int(point[0]), int(point[1])), 5
                )

        self.screen.blit(frame_rgb, (0, 0))
        pygame.display.update()

    def close(self):
        pygame.quit()
