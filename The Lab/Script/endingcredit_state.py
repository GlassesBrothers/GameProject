import pygame
import sys
import time

class EndingCredit:
    def __init__(self, screen_width, screen_height, developer_names):
        pygame.init()

        self.screen = pygame.display.set_mode((screen_width, screen_height))
        pygame.display.set_caption('The Game')

        self.font = pygame.font.SysFont("malgungothic", 36)
        self.text_color = (255, 255, 255)

        self.developer_names = developer_names
        self.text_objects = [self.font.render(name, True, self.text_color) for name in self.developer_names]

        self.credit_y = screen_height
        self.scroll_speed = 1

        self.running = True

    def handle_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def draw_credit_screen(self):
        self.screen.fill((0, 0, 0))

        for i, text_surface in enumerate(self.text_objects):
            text_rect = text_surface.get_rect(center=(self.screen.get_width() // 2, self.credit_y + i * 40))
            self.screen.blit(text_surface, text_rect)

    def run(self):
        while self.running:
            self.handle_event()
            self.draw_credit_screen()
            pygame.display.flip()

            self.credit_y -= self.scroll_speed

            if self.credit_y < -len(self.developer_names) * 40:
                self.running = False

            time.sleep(0.03)  # 30ms 딜레이

        pygame.quit()
        sys.exit()


# 개발자 이름 리스트
developer_names = [
    "The End",
    "",
    "제작진",
    "",
    "스토리 및 기획",
    "김현빈, 정다우",
    "",
    "디자인",
    "정다우",
    "",
    "lab, securityroom, restingroom",
    "김현빈",
    "",
    "start, storage, endingcredit", 
    "신강민",
    "",
    "ppt 및 자료 조사",
    "심완기",
    "",
    "Special Thanks",
    "전재민",
    "김희경",
    "·",
    "·",
    "·",
    "·",
    "·",
    "·",
    "",
    "Thank you for playing our Game"
    # 개발자들의 이름을 원하는 만큼 추가할 수 있습니다.
]

# EndingCredit 클래스의 인스턴스 생성
ending_credit = EndingCredit(1280, 720, developer_names)