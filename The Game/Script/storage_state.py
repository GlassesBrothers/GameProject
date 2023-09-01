import pygame
import os

class StorageState:
    def __init__(self, image_directory, screen_width, screen_height, screen):
        self.image_directory = image_directory
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.game_state = "storage"
        self.screen = screen
        
        self.storage_battery_path = os.path.join(self.image_directory, "storage/storage_bettery.png")
        self.storage_door_path_path = os.path.join(self.image_directory, "storage/storage_door.png")
        self.storage_frame_path = os.path.join(self.image_directory, "storage/storage_frame.png")
        self.storage_gunpowderbox_path = os.path.join(self.image_directory, "storage/storage_gunpowderbox.png")
        self.storage_toolbox_screwdriver_path = os.path.join(self.image_directory, "storage/storage_toolbox_screwdriver.png")
        self.storage_toolbox_path = os.path.join(self.image_directory, "storage/storage_toolbox.png")
        self.storage_keycard_path = os.path.join(self.image_directory, "storage/storage_keycard.png")
        self.storage_closedbox_path = os.path.join(self.image_directory, "storage/storage_closedbox.png")
        self.storage_openbox_path = os.path.join(self.image_directory, "storage/storage_openbox.png")
        self.storage_closedbox = pygame.image.load(self.storage_closedbox_path)
        self.storage_openbox = pygame.image.load(self.storage_openbox_path)
        self.storage_battery = pygame.image.load(self.storage_battery_path)
        self.storage_frame =  pygame.image.load(self.storage_door_path_path)
        self.storage_gunpowderbox =  pygame.image.load(self.storage_gunpowderbox_path)
        self.storage_toolbox = pygame.image.load(self.storage_toolbox)
        self.storage_door = pygame.image.load(self.storage_door)
        self.storage_keycard = pygame.image.load(self.storage_keycard)
        self.storage_toolbox_screwdriver = pygame.image.load(self.storage_toolbox_screwdriver)
        self.storage_toolbox_screwdriver_rect = self.storage_toolbox_screwdriver.get_rect()
        self.storage_battery_rect = self.storage_battery.get_rect()
        self.storage_frame_rect = self.storage_frame.get_rect()
        self.storage_gunpowderbox_rect = self.storage_gunpowderbox.get_rect()
        self.storage_toolbox_rect = self.storage_toolbox.get_rect()
        self.storage_door_rect = self.storage_door.get_rect()
        self.storage_keycard_rect = self.storage_keycard.get_rect()
        self.storage_closedbox_rect = self.storage_closedbox.get_rect()
        self.storage_openbox_rect = self.storage_openbox.get_rect()
        self.storage_battery_rect.center = (screen_width// 1.37, screen_height // 2.1)
        self.storage_frame_rect.center = (screen_width // 2, screen_height // 3.5)
        self.storage_gunpowderbox_rect.center = (screen_width// 1.3, screen_height // 1.8)
        self.storage_toolbox_rect.center = (screen_width// 3.5, screen_height// 1.5)
        self.storage_door_rect.center = (100, screen_height // 1.8)
        
        
        self.inventory = None
        self.inventory_items = []
        self.inventory_visible = False
        self.other_interaction_state = False
        self.storage_frame_state = True
        self.storage_box_state = False
        self.storage_box_text = False
        self.inventory_equipped_item = None
        self.equipped_item = None  # 현재 장착된 아이템을 저장하는 변수
        
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
                if self.storage_toolbox_rect.collidedict(event.pos):
                    self.inventory_items.append(self.storage_toolbox_screwdriver)
                elif self.storage_frame_rect.collidepoint(event.pos):
                    #인벤토리에 "드라이버"있는지 확인하는 if 명령어 ~~~
                    
                    self.inventory_items.remove(self.storage_toolbox_screwdriver)
                    self.storage_frame_state = False
                elif self.storage_closedbox_rect.collidedict(event.pos):
                    #인벤토리에 "부엌 키" 있는지 확인하는 if 명령어 ~~~
                    self.inventory_items.remove(self.restingroom_kitchen_key)
                    self.storage_box_state = True
                    self.storage_box_text = True
                    self.inventory_items.append(self.storage_keycard)
                    
                    
                    
                    
                    
                    
                
            
            
            
            
            
    
    
    
    
    
    
    
    
    
    
    
    
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
        if self.storage_box_state:
            self.screen.blit(self.storage_openbox, self.storage_openbox_rect)
            if self.storage_box_text: 
                self.show_text = True
                if self.text_start_time is None:
                    self.text_start_time = pygame.time.get_ticks()
                self.elapsed_time = pygame.time.get_ticks() - self.text_start_time
                self.show_text_box("보안실 키 카드를(을) 획득했다!", self.elapsed_time)
                
                
                
                
    def draw(self, screen):
        screen.blit(self.storage_battery, self.storage_battery_rect)
        screen.blit(self.storage_gunpowderbox, self.storage_gunpowderbox_rect)
        screen.blit(self.storage_toolbox, self.storage_toolbox_rect)
        screen.blit(self.storage_door, self.storage_door_rect)
        if self.storage_frame_state:
            screen.blit(self.storage_frame, self.storage_frame_rect)
            if not self.storage_box_state:
                screen.blit(self.storage_closedbox, self.storage_closedbox)
                
    def get_inventory_items(self):
        return self.inventory_items