import pygame
import os


# 야 강민아 지금 내가 Box 상호작용 이벤트랑 처음에 누르면 아이템 먹어지고 
# 상자가 열린 모습으로 바뀌고 다시 클릭하면 다른 메세지가 출력되게 만들었어.

# 네가 해야 할 게 이제 toolbox를 클릭하면 지금은 드라이버만 인벤토리에 들어가는데 
# 여기서 클릭하면 열린 모습으로 바뀌게 만들면 돼.

# 만약 궁금한 거 있으면 물어봐

#remove()메소드를 써도 인벤토리에서 screw드라이버가 지워지지 않아
#그리고 toolbox를 누를때 다른 액자나 상자가 깜빡거려 100ms 저거 때문인거같은데 인벤토리랑 장착된 아이템도 깜빡거리더라 이거 해결 방법 없냐


class StorageState:
    def __init__(self, screen_width, screen_height, screen, inventory_equipped_item):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.game_state = "storage"
        self.screen = screen
        self.inventory_equipped_item = inventory_equipped_item
        
        self.script_directory = os.path.dirname(os.path.abspath(__file__))
        
        self.storage_battery_path = os.path.join(self.script_directory, "../image/storage/storage_battery.png")
        self.storage_door_path = os.path.join(self.script_directory, "../image/storage/storage_door.png")
        self.storage_frame_path = os.path.join(self.script_directory, "../image/storage/storage_frame.png")
        self.storage_gunpowderbox_path = os.path.join(self.script_directory, "../image/storage/storage_gunpowderbox.png")
        self.storage_toolbox_screwdriver_path = os.path.join(self.script_directory, "../image/storage/storage_toolbox_screwdriver.png")
        self.storage_toolbox_path = os.path.join(self.script_directory, "../image/storage/storage_toolbox.png")
        self.storage_keycard_path = os.path.join(self.script_directory, "../image/storage/KeyKard.png")
        self.ClosedBox_path = os.path.join(self.script_directory, "../image/storage/ClosedBox.png")
        self.OpenBox_path = os.path.join(self.script_directory, "../image/storage/OpenBox.png")
        self.OpenStorage_toolbox_path = os.path.join(self.script_directory, "../image/storage/OpenStorage_toolbox.png")
        self.restingroom_kitchen_key_path = os.path.join(self.script_directory, "../image/restingroom/kitchen/restingroom_kitchen_key.png")
        self.ClosedBox = pygame.image.load(self.ClosedBox_path)
        self.OpenBox = pygame.image.load(self.OpenBox_path)
        self.storage_battery = pygame.image.load(self.storage_battery_path)
        self.storage_frame =  pygame.image.load(self.storage_frame_path)
        self.storage_gunpowderbox =  pygame.image.load(self.storage_gunpowderbox_path)
        self.storage_toolbox = pygame.image.load(self.storage_toolbox_path)
        self.storage_door = pygame.image.load(self.storage_door_path)
        self.storage_keycard = pygame.image.load(self.storage_keycard_path)
        self.OpenStorage_toolbox = pygame.image.load(self.OpenStorage_toolbox_path)
        self.restingroom_kitchen_key = pygame.image.load(self.restingroom_kitchen_key_path)
        self.storage_toolbox_screwdriver = pygame.image.load(self.storage_toolbox_screwdriver_path)
        self.storage_toolbox_screwdriver_rect = self.storage_toolbox_screwdriver.get_rect()
        self.storage_battery_rect = self.storage_battery.get_rect()
        self.storage_frame_rect = self.storage_frame.get_rect()
        self.storage_gunpowderbox_rect = self.storage_gunpowderbox.get_rect()
        self.storage_toolbox_rect = self.storage_toolbox.get_rect()
        self.storage_door_rect = self.storage_door.get_rect()
        self.storage_keycard_rect = self.storage_keycard.get_rect()
        self.OpenBox_rect = self.OpenBox.get_rect()
        self.ClosedBox_rect = self.ClosedBox.get_rect()
        
        self.OpenStorage_toolbox_rect = self.OpenStorage_toolbox.get_rect()
        self.storage_battery_rect.center = (screen_width// 1.37, screen_height // 2.1)
        self.storage_frame_rect.center = (screen_width // 2, screen_height // 3.5)
        self.storage_gunpowderbox_rect.center = (screen_width// 1.3, screen_height // 1.8)
        self.storage_toolbox_rect.center = (screen_width// 3.5, screen_height// 1.5)
        self.storage_door_rect.center = (100, screen_height // 1.8)
        self.OpenStorage_toolbox_rect.center = (screen_width// 3.5, screen_height// 1.5)
        self.ClosedBox_rect.center = (screen_width // 2, screen_height // 3.5+10)
        self.OpenBox_rect.center = (screen_width // 2, screen_height // 3.5)
        
        
        self.show_text = False
        self.noclick = False
        self.inventory = None
        self.inventory_items = []
        self.inventory_visible = False
        self.other_interaction_state = False
        self.storage_frame_state = True
        self.storage_box_state = False
        self.storage_box_text = False
        self.inventory_equipped_item = None
        self.equipped_item = None  # 현재 장착된 아이템을 저장하는 변수
        self.text_start_time = None
        self.one_time = True
        self.storage_toolbox_state = False
        self.storage_toolbox_text = False
        
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
            if self.inventory == "storage":
                pass
            else:
                if self.storage_toolbox_rect.collidepoint(event.pos):
                    if self.storage_toolbox_screwdriver not in self.inventory_items:
                        self.inventory_items.append(self.storage_toolbox_screwdriver)
                        print("드라이버 추가됨")
                    self.storage_toolbox_text = True
                    self.storage_toolbox_state = True
                    
                elif self.storage_frame_rect.collidepoint(event.pos):
                    print("액자")
                    #if self.equipped_item == self.storage_toolbox_screwdriver:
                    if self.storage_toolbox_screwdriver in self.inventory_items:
                        self.inventory_items.remove(self.storage_toolbox_screwdriver)
                        print("드라이버 사라짐")
                        self.storage_frame_state = False
                        self.storage_frame_rect.center = (-100, -100)
                elif self.ClosedBox_rect.collidepoint(event.pos):
                    print("닫힌 상자")
                    self.storage_box_state = True
                    self.storage_box_text = True
                    #if self.equipped_item == self.restingroom_kitchen_key:
                    #인벤토리에 "부엌 키" 있는지 확인하는 if 명령어 ~~~
                    #if self.restingroom_kitchen_key in self.inventory_items:
                        #self.inventory_items.remove(self.restingroom_kitchen_key)
                        
                    self.inventory_items.append(self.storage_keycard)
        if event.type == pygame.KEYDOWN:  # 키보드 이벤트 처리
            if event.key == pygame.K_e :
                if self.inventory != "inventory" and not self.show_text:
                    self.inventory = "inventory"
                else:
                    self.inventory = None  # 인벤토리를 닫을 때는 원래 상태로 돌아가기
            elif event.key == pygame.K_z:
                if self.storage_toolbox_text and self.one_time:
                    self.text_start_time = None  # 텍스트 시작 시간 초기화
                    self.show_text = False
                    self.storage_toolbox_text = False
                    self.one_time = False
                    
                else:
                    self.text_start_time = None  # 텍스트 시작 시간 초기화
                    self.show_text = False
                    self.storage_box_text = False
                    self.storage_toolbox_text = False
                
                
                if self.storage_box_text and self.one_time:
                    self.text_start_time = None  # 텍스트 시작 시간 초기화
                    self.show_text = False
                    self.storage_box_text = False
                    self.one_time = False

                else:
                    self.text_start_time = None  # 텍스트 시작 시간 초기화
                    self.show_text = False
                    self.storage_box_text = False
    
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
                
    def draw(self, screen):
        screen.blit(self.storage_battery, self.storage_battery_rect)
        screen.blit(self.storage_gunpowderbox, self.storage_gunpowderbox_rect)
        screen.blit(self.storage_door, self.storage_door_rect)
        
        if self.storage_toolbox_state:
            screen.blit(self.OpenStorage_toolbox, self.OpenStorage_toolbox_rect)
            if self.storage_toolbox_text and self.one_time: 
                    self.show_text = True
                    if self.text_start_time is None:
                        self.text_start_time = pygame.time.get_ticks()
                    self.elapsed_time = pygame.time.get_ticks() - self.text_start_time
                    self.show_text_box("드라비어를(을) 획득했다!", self.elapsed_time)
                    pygame.display.flip()
            elif  self.storage_toolbox_text and not self.one_time: 
                    self.show_text = True
                    if self.text_start_time is None:
                        self.text_start_time = pygame.time.get_ticks()
                    self.elapsed_time = pygame.time.get_ticks() - self.text_start_time
                    self.show_text_box("상자는(은) 비어있다", self.elapsed_time)
                    pygame.display.flip()
        else:
            screen.blit(self.storage_toolbox, self.storage_toolbox_rect)
            
            
            
            
        if self.storage_frame_state:
            screen.blit(self.storage_frame, self.storage_frame_rect)
        else:
            if self.storage_box_state:
                self.screen.blit(self.OpenBox, self.OpenBox_rect)
                if self.storage_box_text and self.one_time: 
                    self.show_text = True
                    if self.text_start_time is None:
                        self.text_start_time = pygame.time.get_ticks()
                    self.elapsed_time = pygame.time.get_ticks() - self.text_start_time
                    self.show_text_box("보안실 키 카드를(을) 획득했다!", self.elapsed_time)
                    pygame.display.flip()
                elif self.storage_box_text and not self.one_time:
                    self.show_text = True
                    if self.text_start_time is None:
                        self.text_start_time = pygame.time.get_ticks()
                    self.elapsed_time = pygame.time.get_ticks() - self.text_start_time
                    self.show_text_box("상자는(은) 비어있다.", self.elapsed_time)
                    pygame.display.flip()
            else:
                screen.blit(self.ClosedBox, self.ClosedBox_rect)
