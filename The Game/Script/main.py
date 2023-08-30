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

    screen.fill(white)

    if game_state == "start":
        start_state.draw(screen)
    elif game_state == "lab":
        lab_state.draw(screen)
    elif game_state == "hollway":
        hollway_state.draw(screen)

    pygame.display.flip()

pygame.quit()
