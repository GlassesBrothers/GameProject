import pygame
import sys
import os

class StartState:
    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.game_state = "start"
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption('The Game')
        
        self.script_directory = os.path.dirname(os.path.abspath(__file__))

        # 이미지 불러오기
        self.background_image_path = os.path.join(self.script_directory, "../image/Other/startpage.png")
        self.background_image = pygame.image.load(self.background_image_path)
        self.background_rect = self.background_image.get_rect()

        self.option_image_path = os.path.join(self.script_directory, "../image/Other/option.png")
        self.option_image = pygame.image.load(self.option_image_path)
        self.option_image_rect = self.option_image.get_rect()

        # "play", "option", "exit" 영역 정의
        self.play_rect = pygame.Rect(106, 204, 212, 68)
        self.option_rect = pygame.Rect(106, 323, 212, 68)
        self.exit_rect = pygame.Rect(106, 446, 212, 68)
        
        self.play_rect.topleft = (106, 204)
        self.option_rect.topleft = (106, 323)
        self.exit_rect.topleft = (106, 446)

        self.option_flag = False

        # 텍스트 또는 인벤토리 상태일 때 클릭 상호작용 안 되게 만드는 불 변수s
        self.noclick = False

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and not self.noclick:
            print(pygame.mouse.get_pos())
            if self.play_rect.collidepoint(event.pos):
                self.game_state = "lab"
            elif self.option_rect.collidepoint(event.pos):
                self.option_flag = True
                    # Option 버튼을 클릭했을 때 할 동작을 여기에 추가
            elif self.exit_rect.collidepoint(event.pos):
                sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_f:
                self.option_flag = False
                self.noclick = False
        

    def draw(self, screen):
        # 배경 이미지 그리기
        self.screen.blit(self.background_image, self.background_rect)

        if self.option_flag:
            self.noclick = True
            self.option_image_rect.center = (self.screen_width // 2, self.screen_height // 2)
            screen.blit(self.option_image, self.option_image_rect)

            # 폴더 아래에 표시할 텍스트
            folder_text = " 나가기 버튼 : F"

            # 폴더 아래에 텍스트를 그리기 위한 폰트 설정
            font = pygame.font.SysFont("malgungothic", 20, True)
            text_surface = font.render(folder_text, True, (0, 0, 0))

            # 텍스트를 그릴 위치 설정 (이 예제에서는 폴더 이미지 아래 중앙에 위치하도록 설정)
            text_rect = text_surface.get_rect()
            text_rect.bottomleft = (self.option_image_rect.x, self.option_image_rect.bottom - 2)

            # 이미지에 텍스트를 그림
            screen.blit(text_surface, text_rect)