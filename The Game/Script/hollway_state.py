import pygame
import os

class HollwayState:
    def __init__(self, screen_width, screen_height, screen, inventory_equipped_item):

        self.screen_width = screen_width
        self.screen_height = screen_height
        self.game_state = "hollway"
        self.screen = screen
        self.inventory_equipped_item = inventory_equipped_item

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

        self.show_secret_code = False

        self.storagedoor_flag = False

        self.exitdoor_flag = False

        self.exitdoor_text = False

        self.seciritydoor_key_flag = False
        self.seciritydoor_flag = False
        self.seciritydoor_text = False

        self.rest_wire_flag = False
        self.rest_switch_flag = False
        self.rest_wire_text = False
        self.rest_switch_text = False

        self.rest_gunpowder_flag = False
        self.rest_gunpowder_text = False
        self.retiringdoor_text = False

        self.rest_battary_flag = False

        self.font = pygame.font.Font(None, 36)
        self.code = ""
        self.input_code = ""

        self.noZ = False

        self.restingdoor_flag = False

        self.code_screen = pygame.Surface((800, 600))  # 컴퓨터 화면을 그릴 Surface 생성
        self.code_screen.fill((200, 200, 200))  # 회색 배경으로 초기화
        self.code_screen_rect = self.code_screen.get_rect()
        self.code_screen_rect.center = (screen_width // 2, screen_height // 2)  # 화면 중앙에 위치

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            print(pygame.mouse.get_pos())
            if self.inventory == "inventory" or self.noclick:
                pass
            else:
                if self.exitdoor_rect.collidepoint(event.pos):  # 이미지 위에서 클릭되었는지 확인
                    if self.show_secret_code:
                        pass
                    else:
                        self.exitdoor_flag = True
                        self.exitdoor_text = True
                elif self.labdoor_rect.collidepoint(event.pos):  # 이미지 위에서 클릭되었는지 확인
                    self.game_state = "lab"
                elif self.retiringdoor_rect.collidepoint(event.pos):  # 이미지 위에서 클릭되었는지 확인
                    
                    if self.restingdoor_flag:
                        self.game_state = "restingroom"
                    else:
                        if self.inventory_equipped_item == "lab_wire":
                            self.rest_wire_flag = True
                            self.rest_wire_text = True
                        elif self.inventory_equipped_item == "lab_switch":
                            self.rest_switch_flag = True
                            self.rest_switch_text = True
                        elif self.inventory_equipped_item == "gunpowder":
                            self.rest_gunpowder_flag = True
                            self.rest_gunpowder_text = True
                        elif self.inventory_equipped_item == "battery":
                            self.rest_battary_flag = True
                        self.retiringdoor_text = True
                    # self.game_state = "restingroom"
                elif self.storagedoor_rect.collidepoint(event.pos):  # 이미지 위에서 클릭되었는지 확인
                    self.game_state = "storage"
                elif self.seciritydoor_rect.collidepoint(event.pos):  # 이미지 위에서 클릭되었는지 확인
                    if self.inventory_equipped_item == "storage_keycard":
                        self.seciritydoor_key_flag = True
                    self.seciritydoor_text = True
        if event.type == pygame.KEYDOWN:  # 키보드 이벤트 처리
            if event.key == pygame.K_e :
                if self.inventory != "inventory" and not self.show_text:
                    self.inventory = "inventory"
                else:
                    self.inventory = None  # 인벤토리를 닫을 때는 원래 상태로 돌아가기
            elif event.key == pygame.K_z and not self.noZ:
                if self.exitdoor_text:
                    # 텍스트 출력 시간 초기화
                    self.text_start_time = None
                    # 출력을 중단하게 False로 바꾸고
                    self.show_text = False
                    # 클릭할 수 있게 False로 설정
                    self.noclick = False
                    self.exitdoor_text = False
                else:
                    # 텍스트 출력 시간 초기화
                    self.text_start_time = None
                    # 출력을 중단하게 False로 바꾸고
                    self.show_text = False
                    # 클릭할 수 있게 False로 설정
                    self.noclick = False
                    # 컴퓨터 이미지 불 함수 False로 설정
                    self.exitdoor_flag = False
                    self.storagedoor_flag = False
                    self.seciritydoor_text = False
                    self.retiringdoor_text = False
            if self.exitdoor_flag:
                if not self.show_secret_code:
                    if event.key == pygame.K_BACKSPACE:
                        self.code = self.code[:-1]
                    elif event.key == pygame.K_RETURN:
                        if self.code == "Abaddon":
                            self.show_secret_code = True
                        else:
                            print("잘못된 아이디!")
                            self.code = ""  # 아이디 입력 초기화
                    else:
                        self.code += event.unicode  # event.unicode로 입력된 글자 가져오기
                    if event.key == pygame.K_f:
                        self.exitdoor_flag = False
                        self.noclick = False
                        self.noZ = False


    def show_text_box(self, text, elapsed_time):
        # 출력 변수를 true로 설정하고 클릭할 수 없게 True로 설정
        self.show_text = True
        self.noclick = True

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

    def draw_text(self, text, pos):
        text_surface = self.font.render(text, True, (0, 0, 0))
        text_rect = text_surface.get_rect(center=pos)
        self.screen.blit(text_surface, text_rect)
    
    def draw(self, screen):
        screen.blit(self.Hollway_background, self.Hollway_background_rect)
        screen.blit(self.exitdoor, self.exitdoor_rect)
        screen.blit(self.labdoor, self.labdoor_rect)
        #screen.blit(self.retiringdoor, self.retiringdoor_rect)
        screen.blit(self.storagedoor, self.storagedoor_rect)
        screen.blit(self.seciritydoor, self.seciritydoor_rect)
        if self.exitdoor_flag:
            if self.exitdoor_text:
                self.show_text = True
                if self.text_start_time is None:
                    self.text_start_time = pygame.time.get_ticks()
                self.elapsed_time = pygame.time.get_ticks() - self.text_start_time
                self.show_text_box("문이 잠겨 있다.", self.elapsed_time)
            else:
                if not self.show_secret_code:
                    self.noZ = True
                    self.noclick = True
                    pygame.draw.rect(self.screen, (0, 0, 0), 
                        (self.code_screen_rect.left - 5, self.code_screen_rect.top - 5, 810, 610), 5)
                    screen.blit(self.code_screen, self.code_screen_rect)
                    self.draw_text("Secret Code : " + self.code, (self.screen_width // 2, self.screen_height // 2))
                    # 폴더 아래에 표시할 텍스트
                    folder_text = " 나가기 버튼 : F"

                    # 폴더 아래에 텍스트를 그리기 위한 폰트 설정
                    font = pygame.font.SysFont("malgungothic", 20, True)
                    text_surface = font.render(folder_text, True, (0, 0, 0))

                    # 텍스트를 그릴 위치 설정 (이 예제에서는 폴더 이미지 아래 중앙에 위치하도록 설정)
                    text_rect = text_surface.get_rect()
                    text_rect.bottomleft = (self.code_screen_rect.x, self.code_screen_rect.bottom)

                    # 이미지에 텍스트를 그림
                    screen.blit(text_surface, text_rect)
                else:
                    self.game_state = 'ending'

        if self.storagedoor_flag:
            self.show_text = True
            if self.text_start_time is None:
                self.text_start_time = pygame.time.get_ticks()
            self.elapsed_time = pygame.time.get_ticks() - self.text_start_time
            self.show_text_box("문이 잠겨 있다.", self.elapsed_time)

        if self.seciritydoor_key_flag:
            if self.seciritydoor_text:
                self.show_text = True
                if self.text_start_time is None:
                    self.text_start_time = pygame.time.get_ticks()
                self.elapsed_time = pygame.time.get_ticks() - self.text_start_time
                self.show_text_box("보안실 문이 열렸다.", self.elapsed_time)
            else:
                self.game_state = "securityroom"
                self.seciritydoor_key_flag = False
        else:
            if self.seciritydoor_text:
                self.show_text = True
                if self.text_start_time is None:
                    self.text_start_time = pygame.time.get_ticks()
                self.elapsed_time = pygame.time.get_ticks() - self.text_start_time
                self.show_text_box("보안실 문이 잠겨있다.", self.elapsed_time)
        
        # 와이어, 스위치, 화약, 베터리 모두 o
        if self.rest_wire_flag and self.rest_switch_flag and self.rest_gunpowder_flag and self.rest_battary_flag:
            if self.retiringdoor_text:
                self.show_text = True
                if self.text_start_time is None:
                    self.text_start_time = pygame.time.get_ticks()
                self.elapsed_time = pygame.time.get_ticks() - self.text_start_time
                self.show_text_box("폭탄이 설치됨과 동시에 터지며 열렸다.", self.elapsed_time)
            else:
                self.restingdoor_flag = True
                self.rest_wire_flag = False
                self.rest_switch_flag = False
                self.rest_gunpowder_flag = False
                self.rest_battary_flag = False
        elif self.rest_wire_flag or self.rest_switch_flag or self.rest_gunpowder_flag or self.rest_battary_flag:
            if self.retiringdoor_text:
                self.show_text = True
                if self.text_start_time is None:
                    self.text_start_time = pygame.time.get_ticks()
                self.elapsed_time = pygame.time.get_ticks() - self.text_start_time
                self.show_text_box("폭탄의 재료를 넣었다.", self.elapsed_time)
        else:
            if self.retiringdoor_text:
                self.show_text = True
                if self.text_start_time is None:
                    self.text_start_time = pygame.time.get_ticks()
                self.elapsed_time = pygame.time.get_ticks() - self.text_start_time
                self.show_text_box("문이 열리지 않는다. 폭탄이라면 가능할 수도?", self.elapsed_time)

