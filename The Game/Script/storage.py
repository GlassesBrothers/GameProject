import pygame

screen_height = 720
screen_width = 1280

screen = pygame.display.set_mode((screen_width, screen_height))

storage_battery = pygame.image.load("The Game\image\storage\storage_battery.png")
storage_frame =  pygame.image.load("The Game\image\storage\storage_frame.png")
storage_gunpowderbox =  pygame.image.load("The Game\image\storage\storage_gunpowderbox.png")
storage_toolbox = pygame.image.load("The Game\image\storage\storage_toolbox.png")
storage_door = pygame.image.load("The Game\image\storage\storage_door.png")
storage_battery_rect = storage_battery.get_rect()
storage_frame_rect = storage_frame.get_rect()
storage_gunpowderbox_rect = storage_gunpowderbox.get_rect()
storage_toolbox_rect = storage_toolbox.get_rect()
storage_door_rect = storage_door.get_rect()
storage_battery_rect.center = (screen_width// 1.37, screen_height // 2.1)
storage_frame_rect.center = (screen_width // 2, screen_height // 3.5)
storage_gunpowderbox_rect.center = (screen_width// 1.3, screen_height // 1.8)
storage_toolbox_rect.center = (screen_width// 3.5, screen_height// 1.5)
storage_door_rect.center = (100, screen_height // 1.8)




def storage_info():
    screen.blit(storage_battery, storage_battery_rect)
    screen.blit(storage_frame, storage_frame_rect)
    screen.blit(storage_gunpowderbox, storage_gunpowderbox_rect)
    screen.blit(storage_toolbox, storage_toolbox_rect)
    screen.blit(storage_door, storage_door_rect)
    
    
    
    
    




