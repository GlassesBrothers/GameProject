import pygame
import os


class StorageState:
    def __init__(self, screen_width, screen_height, screen, inventory_equipped_item):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.game_state = "storage"
        self.screen = screen
        self.inventory_equipped_item = inventory_equipped_item
        
        self.script_directory = os.path.dirname(os.path.abspath(__file__))
        
        
        self.storage_background_path = os.path.join(self.script_directory, "../image/storage/Storage_background.png")
        self.storage_battery_path = os.path.join(self.script_directory, "../image/storage/Storage_Battery.png")
        self.storage_door_path = os.path.join(self.script_directory, "../image/storage/Storage_Door.png")
        self.storage_frame_path = os.path.join(self.script_directory, "../image/storage/Storage_Frame.png")
        self.storage_gunpowderbox_path = os.path.join(self.script_directory, "../image/storage/Storage_Gunpowder.png")
        self.storage_toolbox_screwdriver_path = os.path.join(self.script_directory, "../image/InventoryItems/Inventory_Driver.png")
        self.storage_toolbox_path = os.path.join(self.script_directory, "../image/storage/Storage_ToolBox.png")
        self.storage_keycard_path = os.path.join(self.script_directory, "../image/InventoryItems/Inventory_Storage_KeyCard.png")
        self.ClosedBox_path = os.path.join(self.script_directory, "../image/storage/Storage_SafeClosed.png")
        self.OpenBox_path = os.path.join(self.script_directory, "../image/storage/Storage_SafeOpen.png")
        self.OpenBoxLess_path = os.path.join(self.script_directory, "../image/storage/Storage_SafeOpenLess.png")
        self.OpenStorage_toolbox_path = os.path.join(self.script_directory, "../image/storage/Storage_ToolBox.png")
        self.safekey_path = os.path.join(self.script_directory, "../image/InventoryItems/Inventory_Key.png")
        self.OpenBoxLess = pygame.image.load(self.OpenBoxLess_path)
        self.storage_background = pygame.image.load(self.storage_background_path)
        self.ClosedBox = pygame.image.load(self.ClosedBox_path)
        self.OpenBox = pygame.image.load(self.OpenBox_path)
        self.storage_battery = pygame.image.load(self.storage_battery_path)
        self.storage_frame =  pygame.image.load(self.storage_frame_path)
        self.storage_gunpowderbox =  pygame.image.load(self.storage_gunpowderbox_path)
        self.storage_toolbox = pygame.image.load(self.storage_toolbox_path)
        self.storage_door = pygame.image.load(self.storage_door_path)
        self.storage_keycard = pygame.image.load(self.storage_keycard_path)
        self.OpenStorage_toolbox = pygame.image.load(self.OpenStorage_toolbox_path)
        self.safekey = pygame.image.load(self.safekey_path)
        self.storage_toolbox_screwdriver = pygame.image.load(self.storage_toolbox_screwdriver_path)
        self.storage_background_rect = self.storage_background.get_rect()
        self.OpenBoxLess_rect = self.OpenBoxLess.get_rect()
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
        
        self.storage_background_rect.center = (self.screen_width // 2, self.screen_height // 2)
        self.storage_battery_rect.center = (310, 328)
        self.storage_frame_rect.center = (screen_width // 2, screen_height // 3.5)
        self.storage_gunpowderbox_rect.center = (250, 174)
        self.storage_toolbox_rect.center = (1020, 550)
        self.storage_door_rect.center = (40, 421)
        self.OpenStorage_toolbox_rect.center = (screen_width// 3.5, screen_height// 1.5)
        self.ClosedBox_rect.center = (screen_width // 2, screen_height // 3.5)
        self.OpenBox_rect.center = (screen_width // 2, screen_height // 3.5)
        self.OpenBoxLess_rect.center = (screen_width // 2, screen_height // 3.5)
        
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
        self.storage_battery_state = True
        self.storage_battery_text = False
        self.storage_gunpowderbox_state = True
        self.storage_gunpowderbox_text = False
        self.OpenBox_state = False
        
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
        if event.type == pygame.MOUSEBUTTONDOWN and not self.inventory == "inventory":
            if self.inventory == "storage" or self.noclick:
                pass
            else:
                print(pygame.mouse.get_pos())
                
                if self.storage_toolbox_rect.collidepoint(event.pos):
                    if self.storage_toolbox_screwdriver not in self.inventory_items:
                        self.inventory_items.append(self.storage_toolbox_screwdriver)
                        print("드라이버 추가됨")
                    self.storage_toolbox_text = True
                    self.storage_toolbox_state = True
                elif self.storage_door_rect.collidepoint(event.pos):
                    self.game_state = "hollway"
                    
                elif self.storage_frame_rect.collidepoint(event.pos):
                    if self.inventory_equipped_item == "storage_toolbox_screwdriver":
                        print("액자")
                        if self.storage_toolbox_screwdriver in self.inventory_items:
                            self.storage_frame_state = False
                            self.storage_frame_rect.center = (-100, -100)
                elif self.storage_gunpowderbox_rect.collidepoint(event.pos):
                    self.storage_gunpowderbox_state = False
                    self.storage_gunpowderbox_text = True
                    self.inventory_items.append(self.storage_gunpowderbox)
                    
                elif self.ClosedBox_rect.collidepoint(event.pos):
                    #if self.equipped_item == "safekey":
                        #if self.safekey in self.inventory_items:
                    print("닫힌 상자")
                    if self.inventory_equipped_item == "key":
                        self.storage_box_state = True
                        self.ClosedBox_rect.center = (-100, -100)
                    
                elif self.storage_battery_rect.collidepoint(event.pos):
                    self.storage_battery_state = False
                    self.storage_battery_text = True
                    self.inventory_items.append(self.storage_battery)
                elif self.OpenBox_rect.collidepoint(event.pos):
                    print("열린 상자")
                    self.inventory_items.append(self.storage_keycard)
                    self.storage_box_state = False
                    self.OpenBox_state = True
                    self.storage_box_text = True
                        
                    
                
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
                    self.noclick = False
                    
                else:
                    self.text_start_time = None  # 텍스트 시작 시간 초기화
                    self.show_text = False
                    self.storage_box_text = False
                    self.storage_toolbox_text = False
                    self.noclick = False
                
                
                if self.storage_box_text and self.one_time:
                    self.text_start_time = None  # 텍스트 시작 시간 초기화
                    self.show_text = False
                    self.storage_box_text = False
                    self.one_time = False
                    self.noclick = False

                else:
                    self.text_start_time = None  # 텍스트 시작 시간 초기화
                    self.show_text = False
                    self.storage_box_text = False
                    self.noclick = False
                
                if self.storage_battery_text:
                    self.text_start_time = None 
                    self.show_text = False
                    self.storage_battery_text = False
                    self.noclick = False
                else:
                    self.text_start_time = None  # 텍스트 시작 시간 초기화
                    self.show_text = False
                    self.storage_battery_text = False
                    self.noclick = False
                    
                if self.storage_gunpowderbox_text:
                    self.text_start_time = None 
                    self.show_text = False
                    self.storage_gunpowderbox_text = False
                    self.noclick = False
                else:
                    self.text_start_time = None  # 텍스트 시작 시간 초기화
                    self.show_text = False
                    self.storage_gunpowderbox_text = False
                    self.noclick = False
    
    def show_text_box(self, text, elapsed_time):
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
        

    def get_inventory_items(self):
        return self.inventory_items
                
    def draw(self, screen):
        screen.blit(self.storage_background, self.storage_background_rect)
        screen.blit(self.storage_door, self.storage_door_rect)
        if self.storage_gunpowderbox_state:
            screen.blit(self.storage_gunpowderbox, self.storage_gunpowderbox_rect)
        if self.storage_gunpowderbox_text:
            self.show_text = True
            if self.text_start_time is None:
                self.text_start_time = pygame.time.get_ticks()
            self.elapsed_time = pygame.time.get_ticks() - self.text_start_time
            self.show_text_box("화약(을)를 획득했다!", self.elapsed_time)
            pygame.display.flip()
        if self.storage_battery_state:
            screen.blit(self.storage_battery, self.storage_battery_rect)
        if self.storage_battery_text:
            self.show_text = True
            if self.text_start_time is None:
                self.text_start_time = pygame.time.get_ticks()
            self.elapsed_time = pygame.time.get_ticks() - self.text_start_time
            self.show_text_box("배터리(을)를 획득했다!", self.elapsed_time)
            pygame.display.flip()
        
        if self.storage_toolbox_state:
            # screen.blit(self.OpenStorage_toolbox, self.OpenStorage_toolbox_rect)
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
            elif self.OpenBox_state:
                self.screen.blit(self.OpenBoxLess, self.OpenBoxLess_rect)   
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