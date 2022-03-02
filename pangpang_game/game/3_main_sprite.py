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

# load character
character = pygame.image.load('C:/Users/ark07/PycharmProjects/game/character.png')

character_size = character.get_rect().size #이미지 크기 구하기
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width - character_width)/2  # 화면 가로축 절반 크기에 두겠다
character_y_pos = screen_height - character_height  # 화면 맨 밑에 두기

#event loop
running = True #game ing?
while running:
    for event in pygame.event.get(): #if event happen
        if event.type == pygame.QUIT: #호출한 이벤트가 창닫기이면
            running = False

    screen.blit(background, (0,0)) # 배경그리기: 어디에다 나타낼지 좌표 설정 필요
    screen.blit(character,(character_x_pos, character_y_pos))
    pygame.display.update() #게임화면 다시 그리기! 반드시 적어야함

# terminate pygame
pygame.quit()