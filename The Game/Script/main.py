import pygame
import os
import start_state
import lab_state
import hollway_state

black = (0, 0, 0)
white = (255, 255, 255)
gray = (200, 200, 200)

# 화면 크기
screen_width = 1280
screen_height = 720

inventory_items = []
temp = []
inventory = None

slot_clicked = False  # 슬롯이 클릭되었는지 여부를 나타내는 변수

# 격자 정보
num_rows = 4
num_cols = 4
slot_size = 100  # 슬롯 크기를 늘림
slot_margin = 10
inventory_width = num_cols * (slot_size + slot_margin)
inventory_height = num_rows * (slot_size + slot_margin)

inventory_x = (screen_width - inventory_width) // 2
inventory_y = (screen_height - inventory_height) // 2

inventory_equipped_item = None

def draw_inventory():
    inventory_x = (screen_width - inventory_width) // 2
    inventory_y = (screen_height - inventory_height) // 2

    # 인벤토리 창 배경 그리기 (크기 조정 및 모서리 둥글게 처리)
    border_radius = 20  # 모서리의 둥글기 정도 설정
    pygame.draw.rect(screen, black, (inventory_x-10, inventory_y-10, inventory_width+10, inventory_height+10), border_radius=border_radius)

    slot_index = 0  # 슬롯의 인덱스 초기화
    for row in range(num_rows):
        for col in range(num_cols):
            slot_x = inventory_x + col * (slot_size + slot_margin)
            slot_y = inventory_y + row * (slot_size + slot_margin)
            pygame.draw.rect(screen, gray, (slot_x, slot_y, slot_size, slot_size))

            # 인벤토리 아이템 텍스트를 그리기
            item_index = col + row * num_cols
            if item_index < len(inventory_items):
                item_image = inventory_items[item_index]

                item_image_rect = item_image.get_rect()
                item_image_rect.center = (slot_x + slot_size // 2, slot_y + slot_size // 2)
                screen.blit(item_image, item_image_rect)

    for row in range(num_rows):
        for col in range(num_cols):
            slot_x = inventory_x + col * (slot_size + slot_margin)
            slot_y = inventory_y + row * (slot_size + slot_margin)
            slot_rect = pygame.Rect(slot_x, slot_y, slot_size, slot_size)

            pygame.draw.rect(screen, gray, slot_rect)

            item_index = col + row * num_cols
            if item_index < len(inventory_items):
                item_image = inventory_items[item_index]
                item_image_rect = item_image.get_rect(center=slot_rect.center)
                screen.blit(item_image, item_image_rect)

            slot_index += 1  # 슬롯 인덱스 증가


# 색상 정의
black = (0, 0, 0)
white = (255, 255, 255)

# 게임 초기화
pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('The Game')

# 이미지 디렉토리 설정
image_directory = "The Game/image/"

# 게임 상태 정의
game_state = "start"

# 시작 화면과 연구실 화면 객체 생성
start_state = start_state.StartState(image_directory, screen_width, screen_height)
lab_state = lab_state.LabState(image_directory, screen_width, screen_height, screen, inventory_equipped_item)
hollway_state = hollway_state.HollwayState(image_directory, screen_width, screen_height, screen)

equipped_item = None  # 현재 장착된 아이템을 저장하는 변수

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if game_state == "start":
            start_state.handle_event(event)
            game_state = start_state.game_state
        elif game_state == "lab":
            hollway_state.game_state = "hollway"
            inventory = lab_state.inventory
            new_items = lab_state.inventory_items
            for item in new_items:
                if item not in inventory_items:
                    inventory_items.append(item)
            lab_state.handle_event(event)
            game_state = lab_state.game_state
        elif game_state == "hollway":
            lab_state.game_state = "lab"
            inventory = hollway_state.inventory
            hollway_state.handle_event(event)
            game_state = hollway_state.game_state
        if event.type == pygame.MOUSEBUTTONDOWN:
            if inventory == "inventory":
                for row in range(num_rows):
                    for col in range(num_cols):
                        slot_x = inventory_x + col * (slot_size + slot_margin)
                        slot_y = inventory_y + row * (slot_size + slot_margin)
                        slot_rect = pygame.Rect(slot_x, slot_y, slot_size, slot_size)
                        
                        if slot_rect.collidepoint(event.pos):
                                slot_clicked = True  # 슬롯 클릭되었음을 표시
                        
                        

    screen.fill(white)

    if game_state == "start":
        start_state.draw(screen)
    elif game_state == "lab":
        lab_state.draw(screen)
    elif game_state == "hollway":
        hollway_state.draw(screen)

    if inventory == "inventory":
        draw_inventory()  # 인벤토리 창 그리기

    if slot_clicked:
        for row in range(num_rows):
            for col in range(num_cols):
                slot_x = inventory_x + col * (slot_size + slot_margin)
                slot_y = inventory_y + row * (slot_size + slot_margin)
                slot_rect = pygame.Rect(slot_x, slot_y, slot_size, slot_size)

                if slot_rect.collidepoint(event.pos):
                    clicked_item_index = col + row * num_cols
                    if clicked_item_index < len(inventory_items):
                        equipped_item = inventory_items.pop(clicked_item_index)  # 클릭한 아이템을 장착하고 목록에서 제거
                        slot_clicked = False  # 슬롯 클릭 해제


    equipped_item_rect = pygame.Rect(screen_width - 110, screen_height - 110, 100, 100)

    if equipped_item is not None:
        equipped_item_rect = pygame.Rect(screen_width - 110, screen_height - 110, 100, 100)
        equipped_item_image_rect = equipped_item.get_rect(center=equipped_item_rect.center)
        box_size = 100
        box_surface = pygame.Surface((box_size, box_size), pygame.SRCALPHA)  # 투명한 Surface 생성
        pygame.draw.rect(box_surface, (0, 0, 0), pygame.Rect(0, 0, box_size, box_size), 3)  # 테두리 그리기

        # 박스 배경을 투명하게 설정하고 장착된 아이템 이미지 그리기
        screen.blit(box_surface, (equipped_item_rect.left - (box_size - equipped_item_rect.width) / 2,
                            equipped_item_rect.top - (box_size - equipped_item_rect.height) / 2))
        screen.blit(equipped_item, equipped_item_image_rect)  # 아이템 이미지 표시

        # 아이템 종류에 따라 inventory_equipped_item 설정
        if equipped_item == lab_state.inventory_wire:
            lab_state.inventory_equipped_item = "lab_wire"
        elif equipped_item == lab_state.inventory_switch:
            lab_state.inventory_equipped_item = "lab_switch"
        elif equipped_item == lab_state.keykard:
            lab_state.inventory_equipped_item = "keykard"



    pygame.display.flip()

pygame.quit()