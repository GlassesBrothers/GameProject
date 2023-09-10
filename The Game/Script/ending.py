import pygame
import os
import time

class Ending:
    def __init__(self, screen_width, screen_height, screen):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.game_state = "ending"
        self.screen = screen

        # 상대경로 만들기
        self.script_directory = os.path.dirname(os.path.abspath(__file__))

        # 텍스트 리스트 설정
        self.text_list = [
            "밖으로 나가니 노을과 함께 망가진 도시가 한눈에 내려다 보였다.",
            "더 이상 내가 알고 있는 세상은 없었다.",
            "하지만 아직 모든 게 끝이 난 게 아니다.",
            "이제부터 시작일 뿐이다.",
            # 추가 텍스트를 필요한 만큼 추가하세요.
        ]
        self.text_index = 0
        self.text_pos = 0  # 현재 텍스트에서 표시된 글자 수
        self.text_delay = 0.1  # 글자 하나가 출력되는 간격 (초 단위)
        self.last_text_update = 0

        # 텍스트 출력에 사용할 폰트 설정
        self.font = pygame.font.SysFont("malgungothic", 36)

        # 이미지 표시 관련 설정
        self.image = pygame.image.load(os.path.join(self.script_directory, "../image/Other/ending_image.png"))
        self.image_rect = self.image.get_rect()
        self.image_rect.center = (self.screen_width // 2, self.screen_height // 2)
        self.image_displayed = False
        self.image_alpha = 0  # 초기 투명도
        self.image_fade_speed = 1  # 페이드 속도 (값을 조절하여 조절 가능)
        self.image_displayed = False

        # 타이머 설정
        self.start_time = pygame.time.get_ticks()
        self.display_duration = 18000  # 5초 (단위: 밀리초)

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_z:
                # 'z' 키를 누를 때마다 다음 텍스트로 이동
                self.text_index += 1
                self.text_pos = 0
                self.last_text_update = time.time()

    def draw(self):
        current_time = pygame.time.get_ticks()
        self.screen.fill((0, 0, 0))  # 화면을 검은색으로 지웁니다.

        # 현재 인덱스의 텍스트를 한 글자씩 출력
        if self.text_index < len(self.text_list):
            current_text = self.text_list[self.text_index]
            if self.text_pos < len(current_text):
                if time.time() - self.last_text_update > self.text_delay:
                    self.text_pos += 1
                    self.last_text_update = time.time()

            # 출력 중인 텍스트 부분만 표시
            displayed_text = current_text[:self.text_pos]
            text_surface = self.font.render(displayed_text, True, (255, 255, 255))
            text_rect = text_surface.get_rect(center=(self.screen_width // 2, self.screen_height // 2))
            self.screen.blit(text_surface, text_rect)
        else:
            # 이미지 페이드 인
            if not self.image_displayed:
                self.screen.blit(self.image, self.image_rect)
                if self.image_alpha < 255:
                    self.image_alpha += self.image_fade_speed
                    self.image.set_alpha(self.image_alpha)
                else:
                    # 이미지가 완전히 나타난 후 5초 후에 game_state 변경
                    if current_time - self.start_time > self.display_duration:
                        self.game_state = "endingcredit"
                        self.image_displayed = True

