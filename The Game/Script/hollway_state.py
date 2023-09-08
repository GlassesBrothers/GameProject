import pygame
import os

class HollwayState:
    def __init__(self, screen_width, screen_height, screen):

        self.screen_width = screen_width
        self.screen_height = screen_height
        self.game_state = "hollway"
        self.screen = screen

        self.script_directory = os.path.dirname(os.path.abspath(__file__))

        self.Hollway_background_path = os.path.join(self.script_directory, "../image/Hollway/Hollway_background.png")
        self.exitdoor_path = os.path.join(self.script_directory, "../image/Hollway/Hollway_Exit.png")
        self.labdoor_path = os.path.join(self.script_directory, "../image/Hollway/Hollway_Lab_Door.png")
        self.retiringdoor_path = os.path.join(self.script_directory, "../image/Hollway/Hollway_RestingRoom_Door.png")
        self.storagedoor_path = os.path.join(self.script_directory, "../image/Hollway/Hollway_Storage_Door.png")
        self.seciritydoor_path = os.path.join(self.script_directory, "../image/Hollway/Hollway_InformationSecurityRoom_Door.png")
        self.Hollway_background = pygame.image.load(self.Hollway_background_path)
        self.exitdoor = pygame.image.load(self.exitdoor_path)
        self.labdoor = pygame.image.load(self.labdoor_path)
        self.retiringdoor = pygame.image.load(self.retiringdoor_path)
        self.storagedoor = pygame.image.load(self.storagedoor_path)
        self.seciritydoor = pygame.image.load(self.seciritydoor_path)
        self.Hollway_background_rect = self.Hollway_background.get_rect()
        self.exitdoor_rect = self.exitdoor.get_rect()
        self.labdoor_rect = self.labdoor.get_rect()
        self.retiringdoor_rect = self.retiringdoor.get_rect()
        self.storagedoor_rect = self.storagedoor.get_rect()
        self.seciritydoor_rect = self.seciritydoor.get_rect()
        self.Hollway_background_rect.center = (screen_width // 2, screen_height // 2)
        self.exitdoor_rect.topleft = (609, 224)
        self.labdoor_rect.topright = (1240, 125)
        self.retiringdoor_rect.topleft = (59, 140)
        self.storagedoor_rect.topleft = (929, 172)
        self.seciritydoor_rect.topleft = (309, 175)

        self.text_start_time = None
        self.show_text = False
        self.noclick = False
        self.inventory_items = []
        self.inventory = None

        # 다른 상호작용 요소의 상태
        self.inventory_items = []
        self.inventory_visible = False
        self.other_interaction_state = False

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            print(pygame.mouse.get_pos())
            if self.inventory == "inventory" or self.noclick:
                pass
            else:
                if self.exitdoor_rect.collidepoint(event.pos):  # 이미지 위에서 클릭되었는지 확인
                    print('exitdoor') 
                elif self.labdoor_rect.collidepoint(event.pos):  # 이미지 위에서 클릭되었는지 확인
                    self.game_state = "lab"
                elif self.retiringdoor_rect.collidepoint(event.pos):  # 이미지 위에서 클릭되었는지 확인
                    self.game_state = "restingroom"
                elif self.storagedoor_rect.collidepoint(event.pos):  # 이미지 위에서 클릭되었는지 확인
                    self.game_state = 'storage'
                elif self.seciritydoor_rect.collidepoint(event.pos):  # 이미지 위에서 클릭되었는지 확인
                    self.game_state = "securityroom"
        if event.type == pygame.KEYDOWN:  # 키보드 이벤트 처리
            if event.key == pygame.K_e :
                if self.inventory != "inventory" and not self.show_text:
                    self.inventory = "inventory"
                else:
                    self.inventory = None  # 인벤토리를 닫을 때는 원래 상태로 돌아가기
            elif event.key == pygame.K_z:
                pass

    def show_text_box(self, text, elapsed_time):
        text_box_rect = pygame.Rect(50, self.screen_height - 220, self.screen_width - 100, 200)
        pygame.draw.rect(self.screen, (0,0,0), text_box_rect)
        pygame.draw.rect(self.screen, (255,255,255), text_box_rect.inflate(-5, -5))

        font = pygame.font.SysFont("malgungothic", 36)
        visible_text = ""
        for i in range(len(text)):
            if elapsed_time > i * 100:  # 글자마다 100ms씩 지연
                visible_text += text[i]
        text_surface = font.render(visible_text, True, (0,0,0))
        text_rect = text_surface.get_rect(center=text_box_rect.center)
        self.screen.blit(text_surface, text_rect)
    
    def draw(self, screen):
        screen.blit(self.Hollway_background, self.Hollway_background_rect)
        screen.blit(self.exitdoor, self.exitdoor_rect)
        screen.blit(self.labdoor, self.labdoor_rect)
        #screen.blit(self.retiringdoor, self.retiringdoor_rect)
        screen.blit(self.storagedoor, self.storagedoor_rect)
        screen.blit(self.seciritydoor, self.seciritydoor_rect)