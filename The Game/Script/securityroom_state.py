import pygame
import os

class SecurityState:
    def __init__(self, image_directory, screen_width, screen_height, screen):
        self.image_directory = image_directory
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.game_state = "lab"
        self.screen = screen

        self.show_text = False
        self.noclick = False
        self.inventory_items = []
        self.inventory = None
        self.text_start_time = None

        #이미지 파일 경로
        pass

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.inventory == "inventory" or self.noclick:
                pass
            else:
                if self.lab_clock_rect.collidepoint(event.pos):
                    print("시계다")
        if event.type == pygame.KEYDOWN:  # 키보드 이벤트 처리
            if event.key == pygame.K_e :
                if self.inventory != "inventory" and not self.show_text:
                    self.inventory = "inventory"
                else:
                    self.inventory = None  # 인벤토리를 닫을 때는 원래 상태로 돌아가기
            elif event.key == pygame.K_z:
                pass
        
    def draw(self, screen):
        pass
