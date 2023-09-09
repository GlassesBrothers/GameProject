import pygame
import os

class SecurityroomState:
    def __init__(self, screen_width, screen_height, screen, inventory_equipped_item):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.game_state = "securityroom"
        self.screen = screen
        self.inventory_equipped_item = inventory_equipped_item

        # 상대경로 만들기
        self.script_directory = os.path.dirname(os.path.abspath(__file__))

        # 텍스트 시작 시간 변수
        self.text_start_time = None

        # 텍스트 바가 있는지 없는지 나타냄(True -> o, False -> x)
        self.show_text = False
        
        # 텍스트 또는 인벤토리 상태일 때 클릭 상호작용 안 되게 만드는 불 변수s
        self.noclick = False

        # Z키를 누르면 안될 때 사용해야 하는 불 변수
        self.noZ = False

        # 인벤토리 아이템 목록 & 인벤토리 작동 or 비작동 함수
        self.inventory_items = []
        self.inventory = None

        # 현재 장착된 아이템을 저장하는 변수
        self.equipped_item = None  

        # 상호작용 이벤트 작동 여부
        
        # 컴퓨터 상호작용 글씨 불 변수
        self.secroom_computer_off_text = False

        # 파워 공급기 상호작용 글씨 불 변수
        self.secroom_power_supply_text = False

        # 파워 공급기 상호작용 글씨 불 변수
        self.secroom_power_supply_text = False

        # 기본 색 설정
        self.black = (0, 0, 0)
        self.white = (255, 255, 255)
        self.gray = (200, 200, 200)

        # 게임 이미지 경로 설정
        
        # 배경 - off 버전
        self.secroom_background_off_path = os.path.join(self.script_directory,
            "../image/InformationSecurityRoom/InformationSecurityRoom_background_PowerOff.png")
        
        # 컴퓨터 이미지 - off 버전
        self.secroom_computer_off_path = os.path.join(self.script_directory,
            "../image/InformationSecurityRoom/InformationSecurityRoom_ComputerOff.png")
        
        # 출구 문 이미지
        self.secroom_door_path = os.path.join(self.script_directory,
            "../image/InformationSecurityRoom/InformationSecurityRoom_Door.png")
        
        # 파워 전력 공급기 이미지
        self.secroom_power_supply_path = os.path.join(self.script_directory,
            "../image/InformationSecurityRoom/InformationSecurityRoom_PowerSupply.png")
    

        # 게임 이미지 불러오기

        # 배경 - off 버전
        self.secroom_background_off = pygame.image.load(self.secroom_background_off_path)

        # 컴퓨터 이미지 - off 버전
        self.secroom_computer_off = pygame.image.load(self.secroom_computer_off_path)

        # 출구 문 이미지
        self.secroom_door = pygame.image.load(self.secroom_door_path)

        # 파워 전력 공급기 이미지
        self.secroom_power_supply = pygame.image.load(self.secroom_power_supply_path)
        

        # 게임 이미지 크기 구하기 및 위치 정하기

        # 배경 - off 버전
        self.secroom_background_off_rect = self.secroom_background_off.get_rect()
        self.secroom_background_off_rect.center = (self.screen_width // 2, self.screen_height // 2)

        # 컴퓨터 이미지 - off 버전
        self.secroom_computer_off_rect = self.secroom_computer_off.get_rect()
        self.secroom_computer_off_rect.topleft = (387, 326)

        # 출구 문 이미지
        self.secroom_door_rect = self.secroom_door.get_rect()
        self.secroom_door_rect.topleft = (1205, 150)

        # 파워 전력 공급기 이미지
        self.secroom_power_supply_rect = self.secroom_power_supply.get_rect()
        self.secroom_power_supply_rect.topleft = (813, 195)

    # 상호작용 및 다양한 게임 이벤트 함수
    def handle_event(self, event):
        # 파이게임 안에 마우스가 눌러졌을 때의 이벤트가 참인지 거짓인지 판단
        if event.type == pygame.MOUSEBUTTONDOWN:
            print(pygame.mouse.get_pos())
            # 인벤토리가 켜져 있을 때 또는 클릭 불가가 켜져 있다면 상호작용이 안 되게 판단
            if self.inventory == "inventory" or self.noclick:
                # 이건 건드릴 필요 없음
                pass
            else:
                if self.secroom_computer_off_rect.collidepoint(event.pos):
                    self.secroom_computer_off_text = True
                if self.secroom_power_supply_rect.collidepoint(event.pos):
                    self.secroom_power_supply_text = True
        
        # 키보드 이벤트 처리
        if event.type == pygame.KEYDOWN:  
            # 만약 키보드의 e를 눌렀을 때를 판단
            if event.key == pygame.K_e :
                # True면 inventory가 "inventory" 가 아니고 텍스트가 출력 중이 아닌지 다시 판단
                if self.inventory != "inventory" and not self.show_text:
                    # True면 inventory를 "inventory" 로 바꾸고 main.py에서 값을 받아서 인벤토리를 그려줘.
                    self.inventory = "inventory"
                else:
                    # inventory = "inventory" 인 상태, 즉 켜져 있다면?
                    # 인벤토리를 원래 상태로 돌아가기
                    self.inventory = None
            
            # 만약 키보드의 z를 눌렀을 때 그리고 Z를 누를 수 있을 때 판단
            elif event.key == pygame.K_z and not self.noZ:
                # 텍스트 출력 시간 초기화
                self.text_start_time = None
                # 출력을 중단하게 False로 바꾸고
                self.show_text = False
                # 클릭할 수 있게 False로 설정
                self.noclick = False
                # 컴퓨터 이미지 불 함수 False로 설정
                self.secroom_computer_off_text = False
    
    def show_text_box(self, text, elapsed_time):
        # 출력 변수를 true로 설정하고 클릭할 수 없게 True로 설정
        self.show_text = True
        self.noclick = True

        # 이건 텍스트 박스의 크기를 설정하는 거야
        text_box_rect = pygame.Rect(50, self.screen_height - 220, self.screen_width - 100, 200)
        
        # 이게 설정한 텍스트 박스를 그려주는 코드.
        pygame.draw.rect(self.screen, (0,0,0), text_box_rect)
        pygame.draw.rect(self.screen, (255,255,255), text_box_rect.inflate(-5, -5))

        # 폰트 설정
        font = pygame.font.SysFont("malgungothic", 36)
        
        # 입력 내용을 받기 위한 변수 설정
        visible_text = ""

        # 네가 설정한 내용을 아까 전에 visible_text 안에 넣어주는 작업
        # 이렇게 하면 텍스트가 100ms씩 차례대로 출력될 거야.
        for i in range(len(text)):
            if elapsed_time > i * 100:  # 글자마다 100ms씩 지연
                visible_text += text[i]
        
        # 기본적으로 폰트는 blit로 그릴 수 없어.
        # 그래서 폰트를 blit로 그릴 수 있는 surface로 렌더링하는 작업이야.
        # 변수 이름 = font.render(텍스트 변수, True, 색깔)
        text_surface = font.render(visible_text, True, (0,0,0))
        
        # 이건 텍스트 크기를 구하고 위치를 한번에 설정하는 작업 
        text_rect = text_surface.get_rect(center=text_box_rect.center)

        # 화면에 글씨를 그리는 작업
        self.screen.blit(text_surface, text_rect)

    def draw(self, screen, event):
        screen.blit(self.secroom_background_off, self.secroom_background_off_rect)
        screen.blit(self.secroom_computer_off, self.secroom_computer_off_rect)
        screen.blit(self.secroom_door, self.secroom_door_rect)
        screen.blit(self.secroom_power_supply, self.secroom_power_supply_rect)

        # 컴퓨터 이미지 - off 버전 텍스트 출력
        if self.secroom_computer_off_text:
            self.show_text = True
            if self.text_start_time is None:
                self.text_start_time = pygame.time.get_ticks()
            self.elapsed_time = pygame.time.get_ticks() - self.text_start_time
            self.show_text_box("컴퓨터 전원이 켜지지 않는다.", self.elapsed_time)
