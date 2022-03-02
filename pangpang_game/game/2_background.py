import pygame

pygame.init() # initialize

# screen size
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

# set title for screen
pygame.display.set_caption("오락실게임") #game name

# load background image
background = pygame.image.load('C:/Users/ark07/PycharmProjects/game/background.png')

#event loop
running = True #game ing?
while running:
    for event in pygame.event.get(): #if event happen
        if event.type == pygame.QUIT: #호출한 이벤트가 창닫기이면
            running = False

    #screen.fill((0,0,255)) #블루로 채우겠다
    screen.blit(background, (0,0)) # 배경그리기: 어디에다 나타낼지 좌표 설정 필요
    pygame.display.update() #게임화면 다시 그리기! 반드시 적어야함
# terminate pygame
pygame.quit()