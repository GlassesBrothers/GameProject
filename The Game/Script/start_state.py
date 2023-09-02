import pygame
import os

class StartState:
    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.game_state = "start"  # game_state를 멤버 변수로 정의

        self.script_directory = os.path.dirname(os.path.abspath(__file__))

        self.start_button_path = os.path.join(self.script_directory, "../image/Other/startButton.png")
        self.start_button = pygame.image.load(self.start_button_path)
        self.start_button_rect = self.start_button.get_rect()
        self.start_button_rect.center = (100, self.screen_height // 2)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.start_button_rect.collidepoint(event.pos):
                self.game_state = "lab"

    def draw(self, screen):
        screen.blit(self.start_button, self.start_button_rect)
