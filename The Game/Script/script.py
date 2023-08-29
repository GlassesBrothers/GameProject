import pygame
import time
import sys
import storage
import os

#화면 크기
screen_height = 720
screen_width = 1280

black = (0, 0, 0)
white = (255, 255, 255)
gray = (200, 200, 200)

# 격자 정보
num_rows = 4
num_cols = 4
slot_size = 100  # 슬롯 크기를 늘림
slot_margin = 10
inventory_width = num_cols * (slot_size + slot_margin)
inventory_height = num_rows * (slot_size + slot_margin)

pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('The Game')

inventory_items = []

def draw_inventory():
    inventory_x = (screen_width - inventory_width) // 2
    inventory_y = (screen_height - inventory_height) // 2

    # 인벤토리 창 배경 그리기 (크기 조정 및 모서리 둥글게 처리)
    border_radius = 20  # 모서리의 둥글기 정도 설정
    pygame.draw.rect(screen, black, (inventory_x-10, inventory_y-10, inventory_width+10, inventory_height+10), border_radius=border_radius)

    for row in range(num_rows):
        for col in range(num_cols):
            slot_x = inventory_x + col * (slot_size + slot_margin)
            slot_y = inventory_y + row * (slot_size + slot_margin)
            pygame.draw.rect(screen, gray, (slot_x, slot_y, slot_size, slot_size))

            # 인벤토리 아이템 텍스트를 그리기
            item_index = col + row * num_cols
            if item_index < len(inventory_items):
                item_image = inventory_items[item_index]
                font = pygame.font.Font(None, 24)

                item_image_rect = item_image.get_rect()
                item_image_rect.center = (slot_x + slot_size // 2, slot_y + slot_size // 2)
                screen.blit(item_image, item_image_rect)

game_state = "start"  # 현재 게임 상태
inventory = None


# 입력된 비밀번호를 저장할 변수를 생성합니다.
password = ""

login_pass = False

computer_screen_text = [
    "K_HyBin's Pc",
    "login",
    "Please enter your password"
]

# 이미지 파일이 있는 디렉토리를 기준으로 상대 경로 설정
image_directory = "The Game/image/"

# 이미지 파일들의 상대 경로를 계산하여 불러오기


# 나머지 이미지들도 동일한 방식으로 계산

# 이미지 파일 불러오기
# game_state = start
start_button_path = os.path.join(image_directory, "Other/startButton.png")
start_button = pygame.image.load(start_button_path)
start_button_rect = start_button.get_rect()
start_button_rect.center = (100, screen_height // 2)

# game_state = hollway
exitdoor_path = os.path.join(image_directory, "hollway/hollway_exit.png")
labdoor_path = os.path.join(image_directory, "hollway/hollway_lab_door.png")
retiringdoor_path = os.path.join(image_directory, "hollway/hollway_retiringroom_door.png")
storagedoor_path = os.path.join(image_directory, "hollway/hollway_storage_door.png")
seciritydoor_path = os.path.join(image_directory, "hollway/hollway_securityroom_door.png")
exitdoor = pygame.image.load(exitdoor_path)
labdoor = pygame.image.load(labdoor_path)
retiringdoor = pygame.image.load(retiringdoor_path)
storagedoor = pygame.image.load(storagedoor_path)
seciritydoor = pygame.image.load(seciritydoor_path)
exitdoor_rect = exitdoor.get_rect()
labdoor_rect = labdoor.get_rect()
retiringdoor_rect = retiringdoor.get_rect()
storagedoor_rect = storagedoor.get_rect()
seciritydoor_rect = seciritydoor.get_rect()
exitdoor_rect.center = (screen_width // 2, screen_height // 2)
labdoor_rect.center = (screen_width // 5.0, screen_height // 2)
retiringdoor_rect.center = (screen_width // 2.6, screen_height // 2)
storagedoor_rect.center = (screen_width // 1.6, screen_height // 2)
seciritydoor_rect.center = (screen_width // 1.3 , screen_height // 2)

# game_state = lab
lab_clock_path = os.path.join(image_directory, "lab/lab_clock.png")
lab_computer_path = os.path.join(image_directory, "lab/lab_computer.png")
lab_door_path = os.path.join(image_directory, "lab/lab_door.png")
lab_researcher_path = os.path.join(image_directory, "lab/lab_researcher.png")
lab_profile_path = os.path.join(image_directory, "lab/lab_profile.png")
lab_switch_path = os.path.join(image_directory, "lab/lab_switch.png")
lab_wire_path = os.path.join(image_directory, "lab/lab_wire.png")
lab_profile_image_path = os.path.join(image_directory, "Other/Profile.png")
lab_clock = pygame.image.load(lab_clock_path)
lab_computer = pygame.image.load(lab_computer_path)
lab_door = pygame.image.load(lab_door_path)
lab_researcher = pygame.image.load(lab_researcher_path)
lab_profile = pygame.image.load(lab_profile_path)
lab_switch = pygame.image.load(lab_switch_path)
lab_wire = pygame.image.load(lab_wire_path)
lab_profile_image = pygame.image.load(lab_profile_image_path)
lab_clock_rect = lab_clock.get_rect()
lab_computer_rect = lab_computer.get_rect()
lab_door_rect = lab_door.get_rect()
lab_researcher_rect = lab_researcher.get_rect()
lab_profile_rect = lab_profile.get_rect()
lab_switch_rect = lab_switch.get_rect()
lab_wire_rect = lab_wire.get_rect()
lab_profile_image_rect = lab_profile_image.get_rect()
lab_clock_rect.center = (screen_width // 1.3, 100)
lab_computer_rect.center = (screen_width // 2.5, screen_height // 2)
lab_door_rect.center = (100, screen_height // 1.8)
lab_researcher_rect.center = (screen_width - 100, screen_height // 1.5)
lab_profile_rect.center = (screen_width // 1.3, screen_height // 2)
lab_switch_rect.center = (screen_width // 1.7, screen_height // 2)
lab_wire_rect.center = (screen_width // 1.5, screen_height // 2)
lab_profile_image_rect.center = (screen_width // 2, screen_height // 2)

# inventory
inventory_switch_path = os.path.join(image_directory, "inventory_items/inventory_switch.png")
inventory_wire_path = os.path.join(image_directory, "inventory_items/inventory_wire.png")
inventory_switch = pygame.image.load(inventory_switch_path)
inventory_wire = pygame.image.load(inventory_wire_path)

# computer screen
folder_path = os.path.join(image_directory, "Other/folder.png")
folder = pygame.image.load(folder_path)
folder_rect = folder.get_rect()
folder_rect.center = (50, 50)

# Click flag
lab_switch_flag = True
lab_wire_flag = True
lab_profile_flag = True
lab_computer_flag = False

# text flag
show_lab_switch_text = False  # lab_switch에 대한 텍스트 표시 플래그
show_lab_wire_text = False    # lab_wire에 대한 텍스트 표시 플래그
show_lab_profile_text = False
text_start_time = None

# lab_switch를 눌렀을 때 텍스트를 표시하는 플래그
show_text = False
noclick = False

# 텍스트 창 상태와 내용을 저장하는 변수
text_box_content = ""

def show_text_box(text, elapsed_time):
    text_box_rect = pygame.Rect(50, screen_height - 220, screen_width - 100, 200)
    pygame.draw.rect(screen, black, text_box_rect)
    pygame.draw.rect(screen, white, text_box_rect.inflate(-5, -5))

    font = pygame.font.SysFont("malgungothic", 36)
    visible_text = ""
    for i in range(len(text)):
        if elapsed_time > i * 100:  # 글자마다 100ms씩 지연
            visible_text += text[i]
    text_surface = font.render(visible_text, True, black)
    text_rect = text_surface.get_rect(center=text_box_rect.center)
    screen.blit(text_surface, text_rect)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:  # 마우스 클릭 이벤트 처리
            if inventory == "inventory" or show_text or noclick:
                # 인벤토리가 열려있는 동안에는 다른 오브젝트 클릭 무시
                pass
            else:
                if game_state == "start":
                    # 시작 버튼을 클릭하면 게임 상태를 "lab"로 변경
                    if start_button_rect.collidepoint(event.pos):
                        game_state = "lab"
                elif game_state == "hollway" :
                    if exitdoor_rect.collidepoint(event.pos):  # 이미지 위에서 클릭되었는지 확인
                        print('exitdoor') 
                    elif labdoor_rect.collidepoint(event.pos):  # 이미지 위에서 클릭되었는지 확인
                        game_state = "lab"
                    elif retiringdoor_rect.collidepoint(event.pos):  # 이미지 위에서 클릭되었는지 확인
                        print('retiringdoor')
                    elif storagedoor_rect.collidepoint(event.pos):  # 이미지 위에서 클릭되었는지 확인
                        game_state = 'storage'
                    elif seciritydoor_rect.collidepoint(event.pos):  # 이미지 위에서 클릭되었는지 확인
                        print('seciritydoor')
                elif game_state == "lab" :
                    if lab_clock_rect.collidepoint(event.pos):
                        print("시계다")
                    elif lab_computer_rect.collidepoint(event.pos):
                        lab_computer_flag = True
                    elif lab_door_rect.collidepoint(event.pos):
                        game_state = "hollway"
                    elif lab_researcher_rect.collidepoint(event.pos):
                        print("시체다.")
                    elif lab_profile_rect.collidepoint(event.pos):
                        lab_profile_flag = False
                        show_lab_profile_text = True
                    elif lab_switch_rect.collidepoint(event.pos) and lab_switch_flag :
                        lab_switch_flag = False
                        show_lab_switch_text = True  # 텍스트 표시 플래그 활성화
                        inventory_items.append(inventory_switch)
                    elif lab_wire_rect.collidepoint(event.pos) and lab_wire_flag :
                        lab_wire_flag = False
                        show_lab_wire_text = True
                        inventory_items.append(inventory_wire)
                elif game_state == 'storage':
                    if storage.storage_battery_rect.collidepoint(event.pos):
                        print('베터리다.')
        elif event.type == pygame.KEYDOWN:  # 키보드 이벤트 처리
            if event.key == pygame.K_e and not game_state == 'start':
                if inventory != "inventory":
                    inventory = "inventory"
                else:
                    inventory = None  # 인벤토리를 닫을 때는 원래 상태로 돌아가기
            elif event.key == pygame.K_z:
                # 'Z' 키를 눌렀을 때 텍스트 창을 숨기도록 처리
                if show_lab_profile_text:
                    # "z" 키를 누르면 텍스트 창을 숨깁니다.
                    show_lab_profile_text = False
                    text_start_time = None
                elif not show_lab_profile_text and not lab_profile_flag:
                    # 이미지가 보여지고, 텍스트 창이 숨겨진 경우에는 "z" 키로 이미지를 지웁니다.
                    lab_profile_flag = True
                    noclick = False
                else :
                    show_lab_switch_text = False
                    show_lab_wire_text = False
                    text_start_time = None  # 텍스트 시작 시간 초기화
                    if lab_computer_flag:
                        lab_computer_flag = False
                        noclick = False
            if lab_computer_flag :
                if event.key == pygame.K_BACKSPACE:  # 백스페이스 키 처리
                    password = password[:-1]  # 마지막 문자 제거
                elif event.key == pygame.K_RETURN:  # 엔터 키 처리
                    if password == "0415":  # 입력한 비밀번호가 올바른지 확인
                        login_pass = True
                    elif not login_pass:
                        print("잘못된 비밀번호!")
                    password = ""  # 비밀번호 입력 초기화
                else:
                    password += event.unicode  # 눌린 키를 비밀번호에 추가
                        

    
    screen.fill(white)  # 화면을 흰색으로 지우기

    if game_state == "start":
        screen.blit(start_button, start_button_rect)

    if game_state == "hollway":
        screen.blit(exitdoor, exitdoor_rect)
        screen.blit(labdoor, labdoor_rect)
        screen.blit(retiringdoor, retiringdoor_rect)
        screen.blit(storagedoor, storagedoor_rect)
        screen.blit(seciritydoor, seciritydoor_rect)
    
    if game_state == "lab":
        screen.blit(lab_clock, lab_clock_rect)
        screen.blit(lab_computer, lab_computer_rect)
        screen.blit(lab_door, lab_door_rect)
        screen.blit(lab_researcher, lab_researcher_rect)
        screen.blit(lab_profile, lab_profile_rect)
        if lab_wire_flag :
            screen.blit(lab_wire, lab_wire_rect)
        else :
            if show_lab_wire_text:
                if text_start_time is None:
                    text_start_time = pygame.time.get_ticks()
                elapsed_time = pygame.time.get_ticks() - text_start_time
                show_text_box("전선을 눌러서 텍스트를 표시합니다.", elapsed_time)
                pygame.display.flip()
        if lab_switch_flag :
            screen.blit(lab_switch, lab_switch_rect)
        else :   
            if show_lab_switch_text:
                if text_start_time is None:
                    text_start_time = pygame.time.get_ticks()
                elapsed_time = pygame.time.get_ticks() - text_start_time
                show_text_box("스위치를 눌러서 텍스트를 표시합니다.", elapsed_time)
                pygame.display.flip()
        if not lab_profile_flag :
            screen.blit(lab_profile_image, lab_profile_image_rect)
            noclick = True
            if show_lab_profile_text:
                if text_start_time is None:
                    text_start_time = pygame.time.get_ticks()
                elapsed_time = pygame.time.get_ticks() - text_start_time
                show_text_box("내 사진과 함께 내 정보가 적혀 있는 프로필이다.", elapsed_time)
                pygame.display.flip()
        if lab_computer_flag :
            noclick = True
            # 컴퓨터 화면 배경을 직접 그립니다.
            computer_width = 800
            computer_height = 450
            computer_size_x = 240
            computer_size_y = 135
            pygame.draw.rect(screen, (0, 0, 0), (240, 135, computer_width, computer_height))  # 배경 그리기
            pygame.draw.rect(screen, (255, 0, 0), (240 + computer_width - 20, 135, 20, 20))  # X 표시 그리기
        
            # 컴퓨터 화면 텍스트 렌더링
            if not login_pass:
                text_y = screen_height // 3  # 화면의 중앙에 텍스트를 렌더링하기 위한 y 좌표
                for line in computer_screen_text:
                    font = pygame.font.Font(None, 36)  # 폰트와 크기 설정
                    text_surface = font.render(line, True, white)  # 텍스트 렌더링
                    text_rect = text_surface.get_rect(center=(screen_width // 2, text_y))
                    screen.blit(text_surface, text_rect)  # 텍스트 화면에 렌더링
                    text_y += 50  # 다음 텍스트 줄을 그리기 위해 y 좌표 증가
                
                # 비밀번호 입력 상자 그리기
                password_input_rect = pygame.Rect(screen_width // 2 - 150, text_y + 300, 300, 50)
                pygame.draw.rect(screen, (255, 255, 255), password_input_rect)
                font = pygame.font.Font(None, 36)
                password_name = font.render("password : ", True, white)
                screen.blit(password_name, (screen_width // 2 - 150, text_y))
                password_surface = font.render(password, True, white)
                screen.blit(password_surface, (screen_width // 2, text_y))
            else :
                folder_rect.center = (computer_size_x + 50, computer_size_y + 50)
                screen.blit(folder, folder_rect)
                pygame.draw.rect(screen, (255, 0, 0), (240 + computer_width - 20, 135, 20, 20))  # X 표시 그리기
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if folder_rect.collidepoint(event.pos):
                        pygame.draw.rect(screen, (255, 255, 255), (290, 185, 200, 100))
                if event.type == pygame.MOUSEBUTTONDOWN:  # 마우스 클릭 이벤트 처리
                    if pygame.Rect(240 + computer_width - 20, 135, 20, 20).collidepoint(event.pos):  # X 표시를 눌렀는지 확인
                        lab_computer_flag = False
                        noclick = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.Rect(240 + computer_width - 20, 135, 20, 20).collidepoint(event.pos):  # X 표시를 눌렀는지 확인
                    lab_computer_flag = False
                    noclick = False

    if game_state == "storage":
        storage.storage_info()
            
    if inventory == "inventory":
        draw_inventory()  # 인벤토리 창 그리기
            
    
    pygame.display.flip()  # 화면 업데이트

pygame.quit()