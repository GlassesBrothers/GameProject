import pygame
import os

class RestingroomState:
    def __init__(self, screen_width, screen_height, screen, inventory_equipped_item):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.game_state = "restingroom"
        self.screen = screen
        self.inventory_equipped_item = inventory_equipped_item

        # 상대경로 만들기
        self.script_directory = os.path.dirname(os.path.abspath(__file__))

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

        # 기본 색 설정
        self.black = (0, 0, 0)
        self.white = (255, 255, 255)
        self.gray = (200, 200, 200)

        # 게임 이미지 경로 및 불러오기 그리고 크기 설정
        # 내가 'RestingRoom_background.png' 로 예시를 들어 볼게.

        # 게임 이미지 경로 설정
        self.RestingRoom_background_path = os.path.join(self.script_directory,
         "../image/RestingRoom/RestingRoom_background.png")
        self.RestingRoom_book_path = os.path.join(self.script_directory,
         "../image/restingroom/RestingRoom_Book.png")
        self.RestingRoom_door_path = os.path.join(self.script_directory,
         "../image/restingroom/RestingRoom_Door.png")
        self.RestingRoom_noplug_path = os.path.join(self.script_directory,
         "../image/restingroom/RestingRoom_NoPlug.png")
        self.RestingRoom_onplug_path = os.path.join(self.script_directory,
         "../image/restingroom/RestingRoom_ONPlug.png")
        self.RestingRoom_plant_path = os.path.join(self.script_directory,
         "../image/restingroom/RestingRoom_Plant.png")
        self.RestingRoom_plantnutrients_path = os.path.join(self.script_directory,
         "../image/restingroom/RestingRoom_plant nutrients.png")
        self.RestingRoom_tablitoff_path = os.path.join(self.script_directory,
         "../image/restingroom/RestingRoom_TablitOff.png")
        self.RestingRoom_tabliton_path = os.path.join(self.script_directory,
         "../image/restingroom/RestingRoom_TablitOn.png")

        # 게임 이미지 불러오기
        self.RestingRoom_background = pygame.image.load(self.RestingRoom_background_path)
        self.RestingRoom_book = pygame.image.load(self.RestingRoom_book_path)
        self.RestingRoom_door = pygame.image.load(self.RestingRoom_door_path)
        self.RestingRoom_noplug = pygame.image.load(self.RestingRoom_noplug_path)
        self.RestingRoom_onplug = pygame.image.load(self.RestingRoom_onplug_path)
        self.RestingRoom_plant = pygame.image.load(self.RestingRoom_plant_path)
        self.RestingRoom_plantnutrients = pygame.image.load(self.RestingRoom_plantnutrients_path)
        self.RestingRoom_tablitoff = pygame.image.load(self.RestingRoom_tablitoff_path)
        self.RestingRoom_tabliton = pygame.image.load(self.RestingRoom_tabliton_path)

        # 게임 이미지 크기 구하기 및 위치 정하기
        self.RestingRoom_background_rect = self.RestingRoom_background.get_rect()
        self.RestingRoom_book_rect = self.RestingRoom_book.get_rect()
        self.RestingRoom_door_rect = self.RestingRoom_door.get_rect()
        self.RestingRoom_noplug_rect = self.RestingRoom_noplug.get_rect()
        self.RestingRoom_plant_rect = self.RestingRoom_plant.get_rect()
        self.RestingRoom_plantnutrients_rect = self.RestingRoom_plantnutrients.get_rect()
        self.RestingRoom_tablitoff_rect = self.RestingRoom_tablitoff.get_rect()
        self.RestingRoom_tabliton_rect = self.RestingRoom_tabliton.get_rect()
        # 여기선 .center를 사용했지만 그것 이외에도
        # 위쪽을 기점으로 하는 .top
        # 왼쪽 위 모서리를 기점으로 하는 .topleft
        # 오른쪽 위 모서리를 기점으로 하는 .topright
        # 아래쪽을 기점으로 하는 .botton
        # 왼쪽 아래 모서리를 기점으로 하는 .bottonleft
        # 오른쪽 아래 모서리를 기점으로 하는 .bottonright 가 있어.
        # 아래 코드는 이미지의 크기의 중심을 기점으로 화면 가로, 세로의 절반 좌표를 설정했어.
        # 이러면 딱 가운데에 맞춰지겠지.
        self.RestingRoom_background_rect.center = (self.screen_width // 2, self.screen_height // 2)
        self.RestingRoom_book_rect.center = (80,80)
        self.RestingRoom_door_rect.center = (200,800)
        self.RestingRoom_noplug_rect.center = (200,50)
        self.RestingRoom_plant_rect.center = (400,100)
        self.RestingRoom_plantnutrients_rect.center = (600,600)
        self.RestingRoom_tablitoff_rect.center = (1000,30)
        self.RestingRoom_tabliton_rect.center = (1000,600)
        

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
                # 여기서부터 상호작용 이벤트를 넣으면 됨
                # 예시를 보여줄게.
                # 상호작용은 무조건 _rect가 들어가야 해.
                # collidepoint는 (event.pos -> 마우스 클릭했을 때의 위치) 감지하는 거야.
                # 이미지 크기 안에서 있는지 없는지 True or False로 나오지.
                if self.RestingRoom_background_rect.collidepoint(event.pos):
                    # 만약 True면?
                    print('정다우 바보')
                else:
                    # 만약 False면?
                    print('정다우 멍청이')
        
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
                # 출력을 중단하게 False로 바꾸고
                self.show_text = False
                # 클릭할 수 있게 False로 설정
                self.noclick = False
                # 그 다음엔 다른 아이템 텍스트 변수를 설정해야 해.
                # ex) self.show_lab_researcher_text = False
    
    # 텍스트 박스를 보여주는 함수
    # 여긴 건드릴 필요없어.
    # 그냥 이런 게 있구나 하고 보면 돼.
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

    # 이 함수는 위에서 네가 설정한 이미지를 화면에 그려주는 함수야.
    def draw(self, screen, event):
        screen.blit(self.RestingRoom_background, self.RestingRoom_background_rect)