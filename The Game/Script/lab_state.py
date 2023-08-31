import pygame
import os

class LabState:
    def __init__(self, image_directory, screen_width, screen_height, screen, inventory_equipped_item):
        self.image_directory = image_directory
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.game_state = "lab"
        self.screen = screen
        self.inventory_equipped_item = inventory_equipped_item

        # lab_state에 필요한 초기화 코드 작성
        self.lab_computer_flag = False
        self.password = ""
        self.login_pass = False
        self.lab_switch_flag = True
        self.lab_wire_flag = True
        self.lab_profile_flag = True
        self.lab_profile_image_path = os.path.join(self.image_directory, "./../image/Other/Profile.png")
        self.lab_profile_image = pygame.image.load(self.lab_profile_image_path)
        self.lab_profile_image_rect = self.lab_profile_image.get_rect()
        self.lab_profile_image_rect.center = (self.screen_width // 2, self.screen_height // 2)
        self.show_lab_switch_text = False
        self.show_lab_wire_text = False
        self.show_lab_profile_text = False
        self.text_start_time = None
        self.show_lab_door_text = False
        self.show_lab_researcher_text = False
        self.one_time = True
        self.keydoor_flag = False
        self.keykard_flag = True
        # lab_switch를 눌렀을 때 텍스트를 표시하는 플래그
        self.show_text = False
        self.noclick = False
        self.inventory_items = []
        self.inventory = None


        # 다른 상호작용 요소에 대한 초기화 코드 작성
        self.inventory_switch_path = os.path.join(self.image_directory, "./../image/inventory_items/inventory_switch.png")
        self.inventory_wire_path = os.path.join(self.image_directory, "./../image/inventory_items/inventory_wire.png")
        self.inventory_switch = pygame.image.load(self.inventory_switch_path)
        self.inventory_wire = pygame.image.load(self.inventory_wire_path)
        self.keykard_path = os.path.join(self.image_directory, "./../image/lab/keykard.png")
        self.keykard = pygame.image.load(self.keykard_path)
        
        
        # ... (다른 이미지들 로드 및 Rect 설정)
        self.lab_path = os.path.join(self.image_directory, "./../image/lab/lab.png")
        self.lab_clock_path = os.path.join(self.image_directory, "./../image/lab/lab_clock.png")
        self.lab_computer_path = os.path.join(self.image_directory, "./../image/lab/lab_computer.png")
        self.lab_door_path = os.path.join(self.image_directory, "./../image/lab/lab_door.png")
        self.lab_researcher_path = os.path.join(self.image_directory, "./../image/lab/lab_researcher.png")
        self.lab_profile_path = os.path.join(self.image_directory, "./../image/lab/lab_profile.png")
        self.lab_switch_path = os.path.join(self.image_directory, "./../image/lab/lab_switch.png")
        self.lab_wire_path = os.path.join(self.image_directory, "./../image/lab/lab_wire.png")
        self.lab = pygame.image.load(self.lab_path)
        self.lab_clock = pygame.image.load(self.lab_clock_path)
        self.lab_computer = pygame.image.load(self.lab_computer_path)
        self.lab_door = pygame.image.load(self.lab_door_path)
        self.lab_researcher = pygame.image.load(self.lab_researcher_path)
        self.lab_profile = pygame.image.load(self.lab_profile_path)
        self.lab_switch = pygame.image.load(self.lab_switch_path)
        self.lab_wire = pygame.image.load(self.lab_wire_path)
        self.lab_rect = self.lab.get_rect()
        self.lab_clock_rect = self.lab_clock.get_rect()
        self.lab_computer_rect = self.lab_computer.get_rect()
        self.lab_door_rect = self.lab_door.get_rect()
        self.lab_researcher_rect = self.lab_researcher.get_rect()
        self.lab_profile_rect = self.lab_profile.get_rect()
        self.lab_switch_rect = self.lab_switch.get_rect()
        self.lab_wire_rect = self.lab_wire.get_rect()
        self.lab_rect.center = (screen_width // 2, screen_height // 2)
        self.lab_clock_rect.center = (screen_width // 1.3, 100)
        self.lab_computer_rect.center = (screen_width // 2.5, screen_height // 2)
        self.lab_door_rect.center = (100, screen_height // 1.8)
        self.lab_researcher_rect.center = (screen_width - 100, screen_height // 1.5)
        self.lab_profile_rect.center = (screen_width // 1.3, screen_height // 2)
        self.lab_switch_rect.center = (screen_width // 1.7, screen_height // 2)
        self.lab_wire_rect.center = (screen_width // 1.5, screen_height // 2)

        # 다른 상호작용 요소의 상태
        self.inventory_items = []
        self.inventory_visible = False
        self.other_interaction_state = False

        self.slot_clicked = False  # 슬롯이 클릭되었는지 여부를 나타내는 변수

        # 격자 정보
        self.num_rows = 4
        self.num_cols = 4
        self.slot_size = 100  # 슬롯 크기를 늘림
        self.slot_margin = 10
        self.inventory_width = self.num_cols * (self.slot_size + self.slot_margin)
        self.inventory_height = self.num_rows * (self.slot_size + self.slot_margin)

        self.inventory_x = (self.screen_width - self.inventory_width) // 2
        self.inventory_y = (self.screen_height - self.inventory_height) // 2

        self.black = (0, 0, 0)
        self.white = (255, 255, 255)
        self.gray = (200, 200, 200)

        self.inventory_equipped_item = None
        self.equipped_item = None  # 현재 장착된 아이템을 저장하는 변수

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.inventory == "inventory" or self.noclick:
                for row in range(self.num_rows):
                    for col in range(self.num_cols):
                        slot_x = self.inventory_x + col * (self.slot_size + self.slot_margin)
                        slot_y = self.inventory_y + row * (self.slot_size + self.slot_margin)
                        slot_rect = pygame.Rect(slot_x, slot_y, self.slot_size, self.slot_size)
                        
                        if slot_rect.collidepoint(event.pos):
                                self.slot_clicked = True  # 슬롯 클릭되었음을 표시
                        if self.slot_clicked:
                            for row in range(self.num_rows):
                                for col in range(self.num_cols):
                                    slot_x = self.inventory_x + col * (self.slot_size + self.slot_margin)
                                    slot_y = self.inventory_y + row * (self.slot_size + self.slot_margin)
                                    slot_rect = pygame.Rect(slot_x, slot_y, self.slot_size, self.slot_size)

                                    if slot_rect.collidepoint(event.pos):
                                        clicked_item_index = col + row * self.num_cols
                                        if clicked_item_index < len(self.inventory_items):
                                            self.equipped_item = self.inventory_items[clicked_item_index]  # 클릭한 아이템을 장착
                                            self.slot_clicked = False  # 슬롯 클릭 해제
            else:
                if self.lab_clock_rect.collidepoint(event.pos):
                    print("시계다")
                elif self.lab_computer_rect.collidepoint(event.pos):
                    self.lab_computer_flag = True
                elif self.lab_door_rect.collidepoint(event.pos):
                    #self.game_state = "hollway"  
                    self.show_lab_door_text = True
                    self.keydoor_flag = True

                elif self.lab_researcher_rect.collidepoint(event.pos):
                    #print("시체다.")
                    if self.keykard_flag:
                        self.inventory_items.append(self.keykard)
                        self.keykard_flag = False
                    self.show_lab_researcher_text = True
                elif self.lab_profile_rect.collidepoint(event.pos):
                    self.lab_profile_flag = False
                    self.show_lab_profile_text = True
                elif self.lab_switch_rect.collidepoint(event.pos) and self.lab_switch_flag :
                    self.lab_switch_flag = False
                    self.show_lab_switch_text = True  # 텍스트 표시 플래그 활성화
                    self.inventory_items.append(self.inventory_switch)
                elif self.lab_wire_rect.collidepoint(event.pos) and self.lab_wire_flag :
                    self.lab_wire_flag = False
                    self.show_lab_wire_text = True
                    self.inventory_items.append(self.inventory_wire)
        if event.type == pygame.KEYDOWN:  # 키보드 이벤트 처리
            if event.key == pygame.K_e :
                if self.inventory != "inventory" and not self.show_text:
                    self.inventory = "inventory"
                else:
                    self.inventory = None  # 인벤토리를 닫을 때는 원래 상태로 돌아가기
            elif event.key == pygame.K_z:
                if self.show_lab_profile_text:
                        # "z" 키를 누르면 텍스트 창을 숨깁니다.
                        self.show_lab_profile_text = False
                        self.text_start_time = None
                        self.show_text = False
                elif not self.show_lab_profile_text and not self.lab_profile_flag:
                        # 이미지가 보여지고, 텍스트 창이 숨겨진 경우에는 "z" 키로 이미지를 지웁니다.
                        self.lab_profile_flag = True
                        self.noclick = False
                elif self.show_lab_researcher_text and self.one_time:
                        self.text_start_time = None  # 텍스트 시작 시간 초기화
                        self.show_text = False
                        self.one_time = False
                        self.show_lab_researcher_text = False
                        print('1')
                else :
                        self.show_lab_switch_text = False
                        self.show_lab_wire_text = False
                        self.text_start_time = None  # 텍스트 시작 시간 초기화
                        self.show_text = False
                        self.show_lab_door_text = False
                        self.show_lab_researcher_text = False
                if self.keydoor_flag:
                        self.text_start_time = None  # 텍스트 시작 시간 초기화
                        self.show_text = False
                        self.show_lab_door_text = False
                        self.keydoor_flag = False

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

    def get_inventory_items(self):
        return self.inventory_items
    
    def draw_inventory(self):
        inventory_x = (self.screen_width - self.inventory_width) // 2
        inventory_y = (self.screen_height - self.inventory_height) // 2

        # 인벤토리 창 배경 그리기 (크기 조정 및 모서리 둥글게 처리)
        border_radius = 20  # 모서리의 둥글기 정도 설정
        pygame.draw.rect(self.screen, self.black, (inventory_x-10, inventory_y-10, self.inventory_width+10, self.inventory_height+10), border_radius=border_radius)

        slot_index = 0  # 슬롯의 인덱스 초기화
        for row in range(self.num_rows):
            for col in range(self.num_cols):
                slot_x = inventory_x + col * (self.slot_size + self.slot_margin)
                slot_y = inventory_y + row * (self.slot_size + self.slot_margin)
                pygame.draw.rect(self.screen, self.gray, (slot_x, slot_y, self.slot_size, self.slot_size))

                # 인벤토리 아이템 텍스트를 그리기
                item_index = col + row * self.num_cols
                if item_index < len(self.inventory_items):
                    item_image = self.inventory_items[item_index]

                    item_image_rect = item_image.get_rect()
                    item_image_rect.center = (slot_x + self.slot_size // 2, slot_y + self.slot_size // 2)
                    self.screen.blit(item_image, item_image_rect)

        for row in range(self.num_rows):
            for col in range(self.num_cols):
                slot_x = inventory_x + col * (self.slot_size + self.slot_margin)
                slot_y = inventory_y + row * (self.slot_size + self.slot_margin)
                slot_rect = pygame.Rect(slot_x, slot_y, self.slot_size, self.slot_size)

                pygame.draw.rect(self.screen, self.gray, slot_rect)

                item_index = col + row * self.num_cols
                if item_index < len(self.inventory_items):
                    item_image = self.inventory_items[item_index]
                    item_image_rect = item_image.get_rect(center=slot_rect.center)
                    self.screen.blit(item_image, item_image_rect)

                slot_index += 1  # 슬롯 인덱스 증가

    def draw(self, screen):
        screen.blit(self.lab, self.lab_rect)
        screen.blit(self.lab_clock, self.lab_clock_rect)
        screen.blit(self.lab_computer, self.lab_computer_rect)
        screen.blit(self.lab_door, self.lab_door_rect)
        screen.blit(self.lab_researcher, self.lab_researcher_rect)
        screen.blit(self.lab_profile, self.lab_profile_rect)
        if self.lab_wire_flag :
            screen.blit(self.lab_wire, self.lab_wire_rect)
        else :
            if self.show_lab_wire_text:
                self.show_text = True
                if self.text_start_time is None:
                    self.text_start_time = pygame.time.get_ticks()
                self.elapsed_time = pygame.time.get_ticks() - self.text_start_time
                self.show_text_box("전선을 흭득했다.", self.elapsed_time)
                pygame.display.flip()
        if self.lab_switch_flag :
            screen.blit(self.lab_switch, self.lab_switch_rect)
        else :   
            if self.show_lab_switch_text:
                self.show_text = True
                if self.text_start_time is None:
                    self.text_start_time = pygame.time.get_ticks()
                self.elapsed_time = pygame.time.get_ticks() - self.text_start_time
                self.show_text_box("낡은 스위치를 흭득했다.", self.elapsed_time)
                pygame.display.flip()
        if not self.lab_profile_flag :
            screen.blit(self.lab_profile_image, self.lab_profile_image_rect)
            self.noclick = True
            if self.show_lab_profile_text:
                if self.text_start_time is None:
                    self.text_start_time = pygame.time.get_ticks()
                self.elapsed_time = pygame.time.get_ticks() - self.text_start_time
                self.show_text_box("내 사진과 함께 내 정보가 적혀 있는 프로필이다.", self.elapsed_time)
                pygame.display.flip()
        if self.show_lab_door_text:
            self.show_text = True
            if self.text_start_time is None:
                self.text_start_time = pygame.time.get_ticks()
            self.elapsed_time = pygame.time.get_ticks() - self.text_start_time
            self.show_text_box("문이 잠겨 있다.", self.elapsed_time)
        if self.show_lab_researcher_text and self.one_time:
            self.show_text = True
            if self.text_start_time is None:
                self.text_start_time = pygame.time.get_ticks()
            self.elapsed_time = pygame.time.get_ticks() - self.text_start_time
            self.show_text_box("부패한 시체 속에서 ID카드를 발견했다.", self.elapsed_time)
            pygame.display.flip()
        elif self.show_lab_researcher_text and not self.one_time:
            self.show_text = True
            if self.text_start_time is None:
                self.text_start_time = pygame.time.get_ticks()
            self.elapsed_time = pygame.time.get_ticks() - self.text_start_time
            self.show_text_box("뒷면에는 Dawoo라는 글자와 0412이라는 숫자가 적혀 있다.", self.elapsed_time)
            pygame.display.flip()

        if self.inventory == "inventory":
            self.draw_inventory()  # 인벤토리 창 그리기

        equipped_item_rect = pygame.Rect(self.screen_width - 110, self.screen_height - 110, 100, 100)

        if self.equipped_item is not None:
            equipped_item_rect = pygame.Rect(self.screen_width - 110, self.screen_height - 110, 100, 100)
            equipped_item_image_rect = self.equipped_item.get_rect(center=equipped_item_rect.center)
            box_size = 100
            box_surface = pygame.Surface((box_size, box_size), pygame.SRCALPHA)  # 투명한 Surface 생성
            pygame.draw.rect(box_surface, (0, 0, 0), pygame.Rect(0, 0, box_size, box_size), 3)  # 테두리 그리기

            # 박스 배경을 투명하게 설정하고 장착된 아이템 이미지 그리기
            screen.blit(box_surface, (equipped_item_rect.left - (box_size - equipped_item_rect.width) / 2,
                                equipped_item_rect.top - (box_size - equipped_item_rect.height) / 2))
            screen.blit(self.equipped_item, equipped_item_image_rect)  # 아이템 이미지 표시

            # 아이템 종류에 따라 inventory_equipped_item 설정
            if self.equipped_item == self.inventory_wire:
                self.inventory_equipped_item = "lab_wire"
            elif self.equipped_item == self.inventory_switch:
                self.inventory_equipped_item = "lab_switch"
            elif self.equipped_item == self.keykard:
                self.inventory_equipped_item = "keykard"

            if self.inventory_equipped_item == "keykard" and self.keydoor_flag:
                self.show_text = True
                if self.text_start_time is None:
                    self.text_start_time = pygame.time.get_ticks()
                self.elapsed_time = pygame.time.get_ticks() - self.text_start_time
                self.show_text_box("ID카드가 망가졌는지 열리지 않는다.", self.elapsed_time)
                pygame.display.flip()
