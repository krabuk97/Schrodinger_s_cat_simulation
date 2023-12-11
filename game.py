import pygame
import sys
from qbit import run_quantum_simulation

pygame.init()
title = "Schrödinger's cat"
width = 1080
height = 720

class Game:

    def __init__(self, title, width, height):
        self.title = title
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption(self.title)
        self.clock = pygame.time.Clock()
        self.running = True
        self.fps = 60
        self.dt = 0
        self.cat_is_dead = False
        self.cat_is_alive = False
        button_width, button_height = 200, 200
        button_x = self.width // 2 - button_width // 2
        button_y = self.height // 2 - button_height // 8
        self.start_button_rect = pygame.Rect(button_x, button_y, button_width, button_height)
        self.start_button_pressed = False

    def load_images(self):
        self.start_image = pygame.image.load("image/start.jpeg")
        self.start_image = pygame.transform.scale(self.start_image, (self.width, self.height))
        self.cat_dead_image = pygame.image.load("image/cat_dead.jpg")
        self.cat_dead_image = pygame.transform.scale(self.cat_dead_image, (self.width, self.height))
        self.cat_alive_image = pygame.image.load("image/cat_alive.jpg")
        self.cat_alive_image = pygame.transform.scale(self.cat_alive_image, (self.width, self.height))
        self.start_button_image = pygame.image.load("image/start_button.png")
        self.start_button_image = pygame.transform.scale(self.start_button_image, (200, 200))

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if self.start_button_rect.collidepoint(event.pos):
                    self.start_button_pressed = True

    def update(self):
        if self.start_button_pressed:
            qbit_results_0, qbit_results_1, times = run_quantum_simulation()

            print("Wyniki symulacji kwantowej (|0⟩⟨0|):", qbit_results_0)
            print("Wyniki symulacji kwantowej (|1⟩⟨1|):", qbit_results_1)

            # Ustawienie stanu kota na podstawie wyników symulacji
            self.cat_is_dead = qbit_results_0[-1] > qbit_results_1[-1]
            self.cat_is_alive = not self.cat_is_dead

            self.start_button_pressed = False

    def draw(self):
        self.screen.fill((255, 255, 255))

        if not self.cat_is_dead and not self.cat_is_alive:
            self.screen.blit(self.start_image, (0, 0))
            self.screen.blit(self.start_button_image, self.start_button_rect.topleft)
        elif self.cat_is_dead:
            self.screen.blit(self.cat_dead_image, (0, 0))
        elif self.cat_is_alive:
            self.screen.blit(self.cat_alive_image, (0, 0))

        pygame.display.flip()

    def run(self):
        self.load_images()
        while self.running:
            self.dt = self.clock.tick(self.fps)
            self.events()
            self.update()
            self.draw()

        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    game = Game(title, width, height)
    game.run()
