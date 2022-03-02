import pygame

pygame.init() # initialize

# screen size
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

# set title for screen
pygame.display.set_caption("오락실게임") #game name

#event loop
running = True #game ing?
while running:
    for event in pygame.event.get(): #if event happen
        if event.type == pygame.QUIT: #호출한 이벤트가 창닫기이면
            running = False

# terminate pygame
pygame.quit()



