'''
Quiz) 하늘에서 떨어지는 똥 피하기 게임을 만드시오

[게임조건]
1. 캐릭터는 화면 가장 아래에 위치, 좌우로만 이동 가능
2. 똥은 화면 가장 위에서 떨어짐, x 좌표는 매번 랜덤으로 설정
3. 캐릭터가 똥을 피하면 다음 똥이 다시 떨어짐
4. 캐릭터가 똥과 충돌하면 게임 종료
5. FPS는 30으로 고정

[게임 이미지]
1. 배경: 640 * 480 (세로 가로) - background.png
2. 캐릭터: 48*48 - ryan.png
3. 똥: 48 * 48 - poo.png
'''

import pygame
from random import randint
##################################################
#기본 초기화(반드시 해야하는 것들)
pygame.init() # initialize

# screen size
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

# set title for screen
pygame.display.set_caption("똥 떨어지는 게임") #game name

# load background image
background = pygame.image.load('C:/Users/ark07/PycharmProjects/game/background.png')

# FPS: Frame Per Second
clock = pygame.time.Clock()
##################################################

# 1. 사용자 게임 초기화(배경화면, 게임 이미지, 좌표, 속도, 폰드 설정 등)
# load character
character = pygame.image.load('C:/Users/ark07/PycharmProjects/game/ryan.png')

character_size = character.get_rect().size
character_width, character_height = character_size[0], character_size[1]
#초기 위치
character_x_pos = (screen_width - character_width)/2 # x축 가운데 위치
character_y_pos = screen_height - character_height # 화면 맨 아래

# load obstacle(Poo)
poo = pygame.image.load('C:/Users/ark07/PycharmProjects/game/poo.png')

poo_size = poo.get_rect().size
poo_width, poo_height = poo_size[0], poo_size[1]
# 똥 초기 위치
poo_x_pos = randint(0, screen_width - poo_width)  # random한 위치
poo_y_pos = 0  # 화면 맨 위에서 떨어짐

#이동할 좌표
to_x = 0
#moving speed
character_speed = 0.6
poo_speed = randint(10,20) # 똥 떨어지는 속도

#event loop
running = True #game ing?
while running:
    dt = clock.tick(30)  # fps=30으로 설정

    # 2. 이벤트 처리(키보드, 마우스 등)
    for event in pygame.event.get(): #if event happen
        if event.type == pygame.QUIT: #호출한 이벤트가 창닫기면
            running = False

        if event.type == pygame.KEYDOWN: #키를 눌렀는지 체크
            if event.key == pygame.K_LEFT:
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                to_x += character_speed
            else:
                pass

        if event.type == pygame.KEYUP: #키를 떼면
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            else:
                pass
    # 3. 게임 캐릭터 위치 정의
    character_x_pos += to_x * dt
    poo_y_pos += poo_speed

    # x 경계값 설정 : 캐릭터가 화면 밖을 나가지 못하도록
    if character_x_pos < 0:
        character_x_pos =0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    if poo_y_pos > screen_height:
        poo_y_pos = 0
        poo_x_pos = randint(0, (screen_width) - (poo_width))

    # 4. 충돌 처리
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    poo_rect = poo.get_rect()
    poo_rect.left = poo_x_pos
    poo_rect.top = poo_y_pos

    #충돌이 있는지 체크
    if character_rect.colliderect(poo_rect):
        print("collision!")
        running = False

    # 5. 화면에 그리기
    screen.blit(background, (0, 0))  # 배경그리기: 어디에다 나타낼지 좌표 설정 필요
    screen.blit(character, (character_x_pos, character_y_pos))
    screen.blit(poo, (poo_x_pos, poo_y_pos))
    pygame.display.update() #게임화면 다시 그리기! 반드시 적어야함

#잠시 대기
pygame.time.delay(1000) #1초 정도 대기
# terminate pygame
pygame.quit()