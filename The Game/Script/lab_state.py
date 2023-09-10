import pygame
import os

class LabState:
    def __init__(self, screen_width, screen_height, screen, inventory_equipped_item):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.game_state = "lab"
        self.screen = screen
        self.inventory_equipped_item = inventory_equipped_item

        self.script_directory = os.path.dirname(os.path.abspath(__file__))

        # lab_state에 필요한 초기화 코드 작성
        self.font = pygame.font.Font(None, 36)
        self.lab_computer_flag = False
        self.password = ""
        self.username = ""
        self.input_username = ""
        self.input_password = ""
        self.username_entered = False  # 아이디 입력이 완료되었는지 여부를 나타내는 변수
        self.computer_screen_text = [
            "K_HyBin's Pc",
            "login",
            "Please enter your password"
        ]
        # PIN 입력에 필요한 초기화 코드 추가
        self.pin = ""  # 빈 문자열로 초기화
        self.pin_input_active = False  # PIN 입력 활성화 여부
        self.pin_entered = False
        self.buttons_visible = False  # 버튼 표시 여부
        self.button1_rect = pygame.Rect(535, 295, 200, 50)  # 첫 번째 버튼 위치와 크기
        self.button2_rect = pygame.Rect(535, 395, 200, 50)  # 두 번째 버튼 위치와 크기
        self.button_font = pygame.font.Font(None, 36)  # 버튼 폰트 설정
        self.button1_text = self.button_font.render("Open", True, (0, 0, 0))  # 첫 번째 버튼 텍스트 렌더링
        self.button2_text = self.button_font.render("Lock", True, (0, 0, 0))  # 두 번째 버튼 텍스트 렌더링
        self.door_state = "Lock"
        self.noZ = False
        self.computer_Lock_flag = False
        self.folder_flag = False
        self.folder2_flag = False
        self.folder3_flag = False
        self.txt_flag = False
        self.txt2_flag = False
        self.txt3_flag = False
        self.login_pass = False
        self.lab_door_flag = False
        self.lab_switch_flag = True
        self.lab_wire_flag = True
        self.lab_profile_flag = True
        self.lab_profile_image_path = os.path.join(self.script_directory, "../image/Other/Profile.png")
        self.lab_profile_image = pygame.image.load(self.lab_profile_image_path)
        self.lab_profile_image_rect = self.lab_profile_image.get_rect()
        self.lab_profile_image_rect.center = (self.screen_width // 2, self.screen_height // 2)
        self.show_lab_switch_text = False
        self.show_lab_wire_text = False
        self.show_lab_profile_text = False
        self.text_start_time = None
        self.show_lab_door_text = False
        self.show_lab_researcher_text = False
        self.lab_clock_text = False
        self.one_time = True
        self.keydoor_flag = False
        self.keykard_flag = True
        # lab_switch를 눌렀을 때 텍스트를 표시하는 플래그s
        self.show_text = False
        self.noclick = False
        self.inventory_items = []
        self.inventory = None


        # 다른 상호작용 요소에 대한 초기화 코드 작성
        self.keyCard_path = os.path.join(self.script_directory, "../image/Lab/Lab_KeyCard.png")
        self.keyCard = pygame.image.load(self.keyCard_path)
        
        
        # ... (다른 이미지들 로드 및 Rect 설정)
        self.computer_Lock_path = os.path.join(self.script_directory, "../image/Other/computer_Lock.png")
        self.computer_Lock = pygame.image.load(self.computer_Lock_path)
        self.computer_Lock_rect = self.computer_Lock.get_rect()
        self.folder_path = os.path.join(self.script_directory, "../image/Other/folder.png")
        self.folder = pygame.image.load(self.folder_path)
        self.folder_rect = self.folder.get_rect()
        self.txt_path = os.path.join(self.script_directory, "../image/Other/txt.png")
        self.txt = pygame.image.load(self.txt_path)
        self.txt_rect = self.txt.get_rect()
        self.ID_txt_path = os.path.join(self.script_directory, "../image/Other/ID_txt.png")
        self.ID_txt = pygame.image.load(self.ID_txt_path)
        self.ID_txt_rect = self.ID_txt.get_rect()
        self.folder2 = pygame.image.load(self.folder_path)
        self.folder2_rect = self.folder2.get_rect()
        self.txt2 = pygame.image.load(self.txt_path)
        self.txt2_rect = self.txt2.get_rect()
        self.instruction_path = os.path.join(self.script_directory, "../image/Other/instruction.png")
        self.instruction = pygame.image.load(self.instruction_path)
        self.instruction_rect = self.instruction.get_rect()
        self.folder3 = pygame.image.load(self.folder_path)
        self.folder3_rect = self.folder3.get_rect()
        self.txt3 = pygame.image.load(self.txt_path)
        self.txt3_rect = self.txt3.get_rect()
        self.mybrith_path = os.path.join(self.script_directory, "../image/Other/mybrith.png")
        self.mybrith = pygame.image.load(self.mybrith_path)
        self.mybrith_rect = self.mybrith.get_rect()
        self.lab_background_path = os.path.join(self.script_directory, "../image/lab/Lab_background.png")
        self.lab_clock_path = os.path.join(self.script_directory, "../image/Lab/lab_clock.png")
        self.lab_computer_path = os.path.join(self.script_directory, "../image/Lab/Lab_Computer.png")
        self.lab_door_path = os.path.join(self.script_directory, "../image/Lab/Lab_Door.png")
        self.lab_researcher_path = os.path.join(self.script_directory, "../image/Lab/Lab_Researcher.png")
        self.lab_profile_path = os.path.join(self.script_directory, "../image/Lab/Lab_Prlfile.png")
        self.lab_switch_path = os.path.join(self.script_directory, "../image/Lab/Lab_Switch.png")
        self.lab_wire_path = os.path.join(self.script_directory, "../image/Lab/Lab_Wire.png")
        self.lab_background = pygame.image.load(self.lab_background_path)
        self.lab_clock = pygame.image.load(self.lab_clock_path)
        self.lab_computer = pygame.image.load(self.lab_computer_path)
        self.lab_door = pygame.image.load(self.lab_door_path)
        self.lab_researcher = pygame.image.load(self.lab_researcher_path)
        self.lab_profile = pygame.image.load(self.lab_profile_path)
        self.lab_switch = pygame.image.load(self.lab_switch_path)
        self.lab_wire = pygame.image.load(self.lab_wire_path)
        self.lab_background_rect = self.lab_background.get_rect()
        self.lab_clock_rect = self.lab_clock.get_rect()
        self.lab_computer_rect = self.lab_computer.get_rect()
        self.lab_door_rect = self.lab_door.get_rect()
        self.lab_researcher_rect = self.lab_researcher.get_rect()
        self.lab_profile_rect = self.lab_profile.get_rect()
        self.lab_switch_rect = self.lab_switch.get_rect()
        self.lab_wire_rect = self.lab_wire.get_rect()
        self.lab_background_rect.center = (screen_width // 2, screen_height // 2)
        self.lab_clock_rect.topleft = (673, 55)
        self.lab_computer_rect.topleft = (389, 347)
        self.lab_door_rect.topleft = (0, 154)
        self.lab_researcher_rect.topleft = (955, 370)
        self.lab_profile_rect.topleft = (146, 438)
        self.lab_switch_rect.topleft = (350, 441)
        self.lab_wire_rect.topleft = (702, 464)

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

        self.equipped_item = None  # 현재 장착된 아이템을 저장하는 변수

        self.computer_width = 920  # 컴퓨터 화면 너비
        self.computer_height = 480  # 컴퓨터 화면 높이

        self.computer_background_path = os.path.join(self.script_directory, "../image/Other/computer_background.png")
        self.computer_background = pygame.image.load(self.computer_background_path)
        self.computer_background_rect = self.computer_background.get_rect()
        self.computer_background_rect.center = (screen_width // 2, screen_height // 2)

        self.lab_computer_screen = pygame.Surface((self.computer_width, self.computer_height))  # 컴퓨터 화면을 그릴 Surface 생성
        self.lab_computer_screen.fill((200, 200, 200))  # 회색 배경으로 초기화
        self.lab_computer_screen_rect = self.lab_computer_screen.get_rect()
        self.lab_computer_screen_rect.center = (screen_width // 2, screen_height // 2)  # 화면 중앙에 위치

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            print(pygame.mouse.get_pos())
            if self.inventory == "inventory" or self.noclick:
                pass
            else:
                if self.lab_clock_rect.collidepoint(event.pos):
                    self.lab_clock_text = True
                elif self.lab_computer_rect.collidepoint(event.pos):
                    self.lab_computer_flag = True
                    self.noclick = True
                elif self.lab_door_rect.collidepoint(event.pos):
                    if self.lab_door_flag:
                        self.game_state = "hollway"
                    else:
                        self.show_lab_door_text = True
                        self.keydoor_flag = True
                elif self.lab_researcher_rect.collidepoint(event.pos):
                    if self.keykard_flag:
                        self.inventory_items.append(self.keyCard)
                        self.keykard_flag = False
                    self.show_lab_researcher_text = True
                elif self.lab_profile_rect.collidepoint(event.pos):
                    self.lab_profile_flag = False
                    self.show_lab_profile_text = True
                elif self.lab_switch_rect.collidepoint(event.pos) and self.lab_switch_flag :
                    self.lab_switch_flag = False
                    self.show_lab_switch_text = True  # 텍스트 표시 플래그 활성화
                    self.inventory_items.append(self.lab_switch)
                elif self.lab_wire_rect.collidepoint(event.pos) and self.lab_wire_flag :
                    self.lab_wire_flag = False
                    self.show_lab_wire_text = True
                    self.inventory_items.append(self.lab_wire)
        if event.type == pygame.KEYDOWN:  # 키보드 이벤트 처리
            if event.key == pygame.K_e :
                if self.inventory != "inventory" and not self.show_text and not self.lab_computer_flag:
                    self.inventory = "inventory"
                else:
                    self.inventory = None  # 인벤토리를 닫을 때는 원래 상태로 돌아가기
            elif event.key == pygame.K_z and not self.noZ:
                if self.show_lab_profile_text:
                        # "z" 키를 누르면 텍스트 창을 숨깁니다.
                        self.show_lab_profile_text = False
                        self.text_start_time = None
                        self.show_text = False
                        self.noclick = False
                elif not self.show_lab_profile_text and not self.lab_profile_flag:
                        # 이미지가 보여지고, 텍스트 창이 숨겨진 경우에는 "z" 키로 이미지를 지웁니다.
                        self.lab_profile_flag = True
                        self.noclick = False
                elif self.show_lab_researcher_text and self.one_time:
                        self.text_start_time = None  # 텍스트 시작 시간 초기화
                        self.show_text = False
                        self.one_time = False
                        self.show_lab_researcher_text = False
                        self.noclick = False
                else :
                        self.lab_clock_text = False
                        self.show_lab_switch_text = False
                        self.show_lab_wire_text = False
                        self.text_start_time = None  # 텍스트 시작 시간 초기화
                        self.show_text = False
                        self.show_lab_door_text = False
                        self.show_lab_researcher_text = False
                        self.noclick = False
                if self.keydoor_flag:
                        self.text_start_time = None  # 텍스트 시작 시간 초기화
                        self.show_text = False
                        self.show_lab_door_text = False
                        self.keydoor_flag = False
                        self.noclick = False
                if self.lab_computer_flag and not self.noZ:
                        self.lab_computer_flag = False
                        self.noclick = False
            if self.lab_computer_flag:
                if self.pin_input_active and not self.pin_entered:
                    if event.key == pygame.K_BACKSPACE:
                        self.pin = self.pin[:-1]  # 마지막 문자를 삭제
                    elif event.key == pygame.K_RETURN:
                        if len(self.pin) == 4:  # 4자리 PIN이 입력되었는지 확인
                            # 여기에 PIN 검증 로직을 추가하세요.
                            # 예를 들어, 올바른 PIN인지 확인하는 조건문을 작성하세요.
                            if self.pin == "0412":
                                self.pin_entered = True
                                self.buttons_visible = True
                            else:
                                print('no')
                                self.pin = ""
                        else:
                            print('no')
                            self.pin = ""  # 입력한 PIN 초기화
                    elif event.key >= pygame.K_0 and event.key <= pygame.K_9 and len(self.pin) < 4:
                        self.pin += event.unicode  # 입력된 숫자를 PIN에 추가
                    # 더 많은 키 이벤트 처리를 추가할 수 있습니다.
                if not self.login_pass and not self.username_entered:
                    if event.key == pygame.K_BACKSPACE:
                        self.username = self.username[:-1]
                    elif event.key == pygame.K_RETURN:
                        if self.username == "Dawoo":
                            self.username_entered = True
                        else:
                            print("잘못된 아이디!")
                            self.username = ""  # 아이디 입력 초기화
                    else:
                        self.username += event.unicode  # event.unicode로 입력된 글자 가져오기
                elif not self.login_pass:
                    if event.key == pygame.K_BACKSPACE:
                        self.password = self.password[:-1]
                    elif event.key == pygame.K_RETURN:
                        if self.username == "Dawoo" and self.password == "20514":
                            self.login_pass = True
                        elif not self.login_pass:
                            print("잘못된 비밀번호!")
                        self.password = ""  # 비밀번호 입력 초기화
                    else:
                        self.password += event.unicode  # event.unicode로 입력된 글자 가져오기

    def show_text_box(self, text, elapsed_time):
        self.show_text = True
        self.noclick = True
        text_box_rect = pygame.Rect(50, self.screen_height - 220, self.screen_width - 100, 200)
        pygame.draw.rect(self.screen, (0,0,0), text_box_rect)
        pygame.draw.rect(self.screen, (255,255,255), text_box_rect.inflate(-5, -5))

        font = pygame.font.SysFont("malgungothic", 36)
        visible_text = ""
        for i in range(len(text)):
            if elapsed_time > i * 100:  # 글자마다 100ms씩 지연6
                visible_text += text[i]
        text_surface = font.render(visible_text, True, (0,0,0))
        text_rect = text_surface.get_rect(center=text_box_rect.center)
        self.screen.blit(text_surface, text_rect)

    def get_inventory_items(self):
        return self.inventory_items
    
    # 화면에 텍스트 렌더링 함수
    def draw_text(self, text, pos):
        text_surface = self.font.render(text, True, (0, 0, 0))
        text_rect = text_surface.get_rect(center=pos)
        self.screen.blit(text_surface, text_rect)

    def draw_pin_input(self, screen):
            # PIN 입력 창 그리기
            pin_box_rect = pygame.Rect(self.lab_computer_screen_rect.centerx - 100, self.lab_computer_screen_rect.centery - 50, 200, 40)
            pygame.draw.rect(screen, (255, 255, 255), pin_box_rect)
            pygame.draw.rect(screen, (0, 0, 0), pin_box_rect, 2)

            font = pygame.font.Font(None, 36)
            pin_text = font.render(self.pin, True, (0, 0, 0))
            pin_text_rect = pin_text.get_rect(center=pin_box_rect.center)
            screen.blit(pin_text, pin_text_rect)

    def draw(self, screen, event):
        screen.blit(self.lab_background, self.lab_background_rect)
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
        if self.lab_clock_text:
            self.show_text = True
            if self.text_start_time is None:
                self.text_start_time = pygame.time.get_ticks()
            self.elapsed_time = pygame.time.get_ticks() - self.text_start_time
            self.show_text_box("이상하게 시침과 분침이 고정되어 있다.", self.elapsed_time)
        if not self.lab_profile_flag :
            screen.blit(self.lab_profile_image, self.lab_profile_image_rect)
            self.noclick = True
            if self.show_lab_profile_text:
                if self.text_start_time is None:
                    self.text_start_time = pygame.time.get_ticks()
                self.elapsed_time = pygame.time.get_ticks() - self.text_start_time
                self.show_text_box("내 사진과 함께 내 정보가 적혀 있는 프로필이다.", self.elapsed_time)
                pygame.display.flip()
        if self.show_lab_door_text and not self.inventory_equipped_item == "keykard":
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
            self.show_text_box("뒷면에는 Dawoo라는 글자와 20514이라는 숫자가 적혀 있다.", self.elapsed_time)
            pygame.display.flip()
        
        if self.inventory_equipped_item == "keykard" and self.keydoor_flag:
                print('1')
                self.show_text = True
                if self.text_start_time is None:
                    self.text_start_time = pygame.time.get_ticks()
                self.elapsed_time = pygame.time.get_ticks() - self.text_start_time
                self.show_text_box("ID카드가 망가졌는지 열리지 않는다.", self.elapsed_time)
                pygame.display.flip()
        if self.lab_computer_flag:
            # 검은 테두리를 그립니다.
            self.x_button_x = self.lab_computer_screen_rect.right - 20
            self.x_button_y = self.lab_computer_screen_rect.top
            pygame.draw.rect(self.screen, (0, 0, 0), (self.lab_computer_screen_rect.left - 5, self.lab_computer_screen_rect.top - 5, self.computer_width + 10, self.computer_height + 10), 5)            
            
            # 흰색 내부를 그립니다.
            pygame.draw.rect(self.screen, (255, 255, 255), (self.lab_computer_screen_rect.left, self.lab_computer_screen_rect.top, self.computer_width, self.computer_height))

            # X 표시 그리기
            pygame.draw.rect(screen, (255, 0, 0), (self.x_button_x, self.x_button_y, 20, 20))
            
            # 컴퓨터 화면 텍스트 렌더링
            if not self.login_pass:
                screen.blit(self.lab_computer_screen, self.lab_computer_screen_rect)
                text_y = self.screen_height // 3  # 화면의 중앙에 텍스트를 렌더링하기 위한 y 좌표
                for i, line in enumerate(self.computer_screen_text):
                    text_y += 80  # 다음 텍스트 줄을 그리기 위해 y 좌표 증가 (50에서 80으로 변경)
                if i == 2:
                    self.draw_text("ID : " + self.username, (self.screen_width // 2, text_y - 50))
                    # 비밀번호 입력 중에는 마스킹 처리 (e.g., '*****')
                    masked_password = '*' * len(self.password)
                    self.draw_text("Password : " + masked_password, (self.screen_width // 2, text_y))
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if pygame.Rect(self.x_button_x, self.x_button_y, 20, 20).collidepoint(event.pos):  # X 표시를 눌렀는지 확인
                        self.lab_computer_flag = False
                        self.noclick = False
                        self.noZ = False
            else:
                screen.blit(self.computer_background, self.computer_background_rect)
                pygame.draw.rect(screen, (255, 0, 0), (self.x_button_x, self.x_button_y, 20, 20))
                self.x_button_x = self.lab_computer_screen_rect.right - 20
                self.x_button_y = self.lab_computer_screen_rect.top
                self.folder_rect.center = (230, 150)
                screen.blit(self.folder, self.folder_rect)
                self.computer_Lock_rect.topleft = (205, 190)
                screen.blit(self.computer_Lock, self.computer_Lock_rect)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.folder_rect.collidepoint(event.pos) and not self.computer_Lock_flag:
                        self.folder_flag = True
                        self.noZ = True
                    if self.computer_Lock_rect.collidepoint(event.pos) and not self.folder_flag:
                        self.computer_Lock_flag = True
                        self.pin_input_active = True
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if pygame.Rect(self.x_button_x, self.x_button_y, 20, 20).collidepoint(event.pos):  # X 표시를 눌렀는지 확인
                        self.lab_computer_flag = False
                        self.noclick = False
                        self.noZ = False
                        self.folder_flag = False
                        self.folder2_flag = False
                        self.folder3_flag = False
                        self.computer_Lock_flag = False
                if self.computer_Lock_flag:
                    pygame.draw.rect(self.screen, (0, 0, 0), (483, 189, 300, 350), 5)
                    pygame.draw.rect(self.screen, (255, 255, 255), (488, 194, 290, 340))
                    pygame.draw.rect(screen, (255, 0, 0), (759, 194, 20, 20))
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if pygame.Rect(759, 194, 20, 20).collidepoint(event.pos):  # X 표시를 눌렀는지 확인
                            self.computer_Lock_flag = False
                    if self.pin_input_active and not self.pin_entered:
                        # PIN 입력 창 그리기
                        self.draw_pin_input(screen)
                        # 여기에 더 많은 PIN 입력 창 관련 코드를 추가하세요.
                    
                    elif self.buttons_visible:
                        if self.lab_door_flag:
                            self.door_state = "Open"
                            self.draw_text("Door System : ", (592, 237))
                            self.door_state_surface = self.font.render(self.door_state, True, (0, 255, 0))
                            self.door_state_rect = self.door_state_surface.get_rect(topleft=(682, 227))
                            screen.blit(self.door_state_surface, self.door_state_rect)
                        else:
                            self.door_state = "Lock"
                            self.draw_text("Door System : ", (592, 237))
                            self.door_state_surface = self.font.render(self.door_state, True, (255, 0, 0))
                            self.door_state_rect = self.door_state_surface.get_rect(topleft=(682, 227))
                            screen.blit(self.door_state_surface, self.door_state_rect)
                        # 버튼 표시
                        pygame.draw.rect(screen, (0, 0, 0), self.button1_rect, 2)
                        pygame.draw.rect(screen, (0, 0, 0), self.button2_rect, 2)
                        # 버튼 텍스트 중앙 정렬
                        button1_text_rect = self.button1_text.get_rect(center=self.button1_rect.center)
                        button2_text_rect = self.button2_text.get_rect(center=self.button2_rect.center)

                        # 버튼 텍스트 그리기
                        screen.blit(self.button1_text, button1_text_rect.topleft)
                        screen.blit(self.button2_text, button2_text_rect.topleft)
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            if self.button1_rect.collidepoint(event.pos):
                                # 첫 번째 버튼을 클릭했을 때 수행할 동작 추가
                                self.lab_door_flag = True
                            elif self.button2_rect.collidepoint(event.pos):
                                # 두 번째 버튼을 클릭했을 때 수행할 동작 추가
                                self.lab_door_flag = False
                if self.folder_flag:
                    pygame.draw.rect(self.screen, (0, 0, 0), (235, 160, 210, 110), 5)
                    pygame.draw.rect(screen, (255, 255, 255), (240, 165, 200, 100))
                    pygame.draw.rect(screen, (255, 0, 0), (420, 165, 20, 20))
                    self.txt_rect.center = (300, 210)
                    screen.blit(self.txt, self.txt_rect)
                    self.folder2_rect.center = (375, 210)
                    screen.blit(self.folder2, self.folder2_rect)
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if self.txt_rect.collidepoint(event.pos) and not self.folder2_flag:
                            self.txt_flag = True
                            self.folder2_flag = False
                        if self.folder2_rect.collidepoint(event.pos) and not self.txt_flag:
                            self.folder2_flag = True
                            self.txt_flag = False
                        if pygame.Rect(420, 165, 20, 20).collidepoint(event.pos):  # X 표시를 눌렀는지 확인
                            self.folder_flag = False
                            self.noZ = False
                    if self.txt_flag and not self.folder2_flag:
                        self.ID_txt_rect.center = (self.screen_width // 2, self.screen_height // 2)
                        screen.blit(self.ID_txt, self.ID_txt_rect)
                        pygame.draw.rect(self.screen, (0, 0, 0), (246, 141, 790, 434), 5)
                        pygame.draw.rect(screen, (255, 0, 0), (1012, 146, 20, 20))
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            if pygame.Rect(1012, 146, 20, 20).collidepoint(event.pos):  # X 표시를 눌렀는지 확인
                                self.txt_flag = False
                    if self.folder2_flag and not self.txt_flag:
                        pygame.draw.rect(self.screen, (0, 0, 0), (380, 220, 210, 110), 5)
                        pygame.draw.rect(screen, (255, 255, 255), (385, 225, 200, 100))
                        pygame.draw.rect(screen, (255, 0, 0), (565, 225, 20, 20))
                        self.txt2_rect.center = (445, 270)
                        screen.blit(self.txt2, self.txt2_rect)
                        self.folder3_rect.center = (520, 270)
                        screen.blit(self.folder3, self.folder3_rect)
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            if self.txt2_rect.collidepoint(event.pos) and not self.folder3_flag:
                                self.txt2_flag = True
                            if self.folder3_rect.collidepoint(event.pos) and not self.txt2_flag:
                                self.folder3_flag = True
                            if pygame.Rect(565, 225, 20, 20).collidepoint(event.pos):  # X 표시를 눌렀는지 확인
                                self.folder2_flag = False
                        if self.txt2_flag:
                            self.instruction_rect.center = (self.screen_width // 2, self.screen_height // 2)
                            screen.blit(self.instruction, self.instruction_rect)
                            pygame.draw.rect(self.screen, (0, 0, 0), (23, 27, 1239, 667), 5)
                            pygame.draw.rect(screen, (255, 0, 0), (1237, 32, 20, 20))
                            if event.type == pygame.MOUSEBUTTONDOWN:
                                if pygame.Rect(1237, 32, 20, 20).collidepoint(event.pos):  # X 표시를 눌렀는지 확인
                                    self.txt2_flag = False
                        if self.folder3_flag:
                            pygame.draw.rect(self.screen, (0, 0, 0), (525, 280, 210, 110), 5)
                            pygame.draw.rect(screen, (255, 255, 255), (530, 285, 200, 100))
                            pygame.draw.rect(screen, (255, 0, 0), (710, 285, 20, 20))
                            self.txt3_rect.center = (590, 330)
                            screen.blit(self.txt3, self.txt3_rect)
                            if event.type == pygame.MOUSEBUTTONDOWN:
                                if self.txt3_rect.collidepoint(event.pos):
                                    self.txt3_flag = True
                                if pygame.Rect(710, 285, 20, 20).collidepoint(event.pos):  # X 표시를 눌렀는지 확인
                                    self.folder3_flag = False
                            if self.txt3_flag:
                                self.mybrith_rect.center = (self.screen_width // 2, self.screen_height // 2)
                                screen.blit(self.mybrith, self.mybrith_rect)
                                pygame.draw.rect(self.screen, (0, 0, 0), (49, 234, 1182, 255), 5)
                                pygame.draw.rect(screen, (255, 0, 0), (1206, 239, 20, 20))
                                if event.type == pygame.MOUSEBUTTONDOWN:
                                    if pygame.Rect(1206, 239, 20, 20).collidepoint(event.pos):  # X 표시를 눌렀는지 확인
                                        self.txt3_flag = False
                        
                        
        else:
            pass