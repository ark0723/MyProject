'''
<오락실 팡게임 만들기>
[게임 조건]
1. 캐릭터는 화면 아래에 위치, 좌우로만 이동 가능
2. 스페이스를 누르면 무기를 쏘아 올림
3. 큰 공 1개가 나타나서 바운스
4. 무기에 닿으면 공은 작은 크기 2개로 분할, 가장 작은 크기의 공은 사라짐
5. 모든 공을 없애면 게임 종료 (success)
6. 캐릭터가 공에 닿으면 게임 종료 (fail)
7. 시간 제한 100초 초과시 게임종료 (fail)
8. FPS = 30

[게임 이미지]
1. 배경: 640 * 480 - background.png
backgound image: <a href="https://www.freepik.com/vectors/vintage">Vintage vector created by stockgiu - www.freepik.com</a>
2. 무대: 640 * 50 - stage.png
3. 캐릭터: 33 * 60 - character.png
4. 무기: 20 * 430 - weapon.png
5. 공: 160 * 160, 80*80, 40*40, 20*20 - ball1.png, ball2.png, ..
'''
import os
import pygame
from random import randint

##################################################
#기본 초기화(반드시 해야하는 것들)
pygame.init() # initialize

# screen size
screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))

# set title for screen
pygame.display.set_caption("PangPang") #game name

# FPS: Frame Per Second
clock = pygame.time.Clock()
##################################################

# 1. 사용자 게임 초기화(배경화면, 게임 이미지, 좌표, 속도, 폰드 설정 등)

cur_path = os.path.dirname(__file__) #현재 파일의 위치 반환
image_path = os.path.join(cur_path, "image") # 이미지 폴더 위치

# load background image
background = pygame.image.load(os.path.join(image_path, "city_background.png"))

# load stage image
stage = pygame.image.load(os.path.join(image_path, "stage.png"))
stage_size = stage.get_rect().size
stage_height = stage_size[1] # 스테이지의 높이 위에 캐릭터를 두기 위해 사용

# load character
character = pygame.image.load(os.path.join(image_path, "character.png"))
character_size = character.get_rect().size
character_width, character_height = character_size[0], character_size[1]
character_x_pos = (screen_width - character_width)/2
character_y_pos = screen_height - (stage_height + character_height)


#event loop
running = True #game ing?
while running:
    dt = clock.tick(60)  # fps=60으로 설정 - 높은 값일수록 동작이 부드러움

    # 2. 이벤트 처리(키보드, 마우스 등)
    for event in pygame.event.get(): #if event happen
        if event.type == pygame.QUIT: #호출한 이벤트가 창닫기면
            running = False


    # 3. 게임 캐릭터 위치 정의

    # 4. 충돌 처리

    # 5. 화면에 그리기
    screen.blit(background, (0, 0))
    screen.blit(stage, (0, screen_height - stage_height))
    screen.blit(character, (character_x_pos, character_y_pos))
    pygame.display.update() #게임화면 다시 그리기! 반드시 적어야함

# terminate pygame
pygame.quit()
