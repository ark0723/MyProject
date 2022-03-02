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
character = pygame.image.load(os.path.join(image_path, "rabbit.png"))
character_size = character.get_rect().size
character_width, character_height = character_size[0], character_size[1]
character_x_pos = (screen_width - character_width)/2
character_y_pos = screen_height - (stage_height + character_height)

#캐릭터 이동방향
character_to_x = 0
#캐릭터 스피드
character_speed = 5

# 무기 만들기
weapon = pygame.image.load(os.path.join(image_path, "bullet.png"))
weapon_size = weapon.get_rect().size
weapon_width, weapon_height = weapon_size[0], weapon_size[1]

# 한번에 여러발 발사 가능
weapons = []
# 무기 이동 속도
weapon_speed = 10

# 공 만들기 (ball size: 4가지)
ball_images = [pygame.image.load(os.path.join(image_path, "ball1.png")), \
               pygame.image.load(os.path.join(image_path, "ball2.png")), \
               pygame.image.load(os.path.join(image_path, "ball3.png")), \
               pygame.image.load(os.path.join(image_path, "ball4.png"))]

# 공의 크기에 따라 속도가 다르다:  클수록 빠름
ball_speed_y = [- 18, -15, -12, -9] # ball1, ball2, ball3, ball4

# balls
balls = []

#최초의 큰 공 추가
balls.append({
    "pos_x": 50, # 공의 시작 x 좌표
    "pos_y": 50, # 공의 시작 y 좌표
    "img_idx" : 0, # 공의 인덱스
    "to_x": 3, # 공의 x축 이동방향, -3이면 왼쪽으로, +3이면 오른쪽 이동
    "to_y": -6, # 공의 y축 이동방향, -6이면 위쪽으로 +6이면 아래로 이동
    "init_speed_y": ball_speed_y[0] # y 최초 속도
})



#event loop
running = True #game ing?
while running:
    dt = clock.tick(60)  # fps=60으로 설정 - 높은 값일수록 동작이 부드러움

    # 2. 이벤트 처리(키보드, 마우스 등)
    for event in pygame.event.get(): #if event happen
        if event.type == pygame.QUIT: #호출한 이벤트가 창닫기면
            running = False

        if event.type == pygame.KEYDOWN: #키보드를 눌렀을 때
            if event.key == pygame.K_LEFT:
                character_to_x -= character_speed

            elif event.key == pygame.K_RIGHT:
                character_to_x += character_speed

            elif event.key == pygame.K_SPACE: #스페이스바를 누르면 무기발사
                weapon_x_pos = character_x_pos #+ (character_width/2) - (weapon_width/2)
                weapon_y_pos = character_y_pos
                weapons.append([weapon_x_pos, weapon_y_pos])

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                character_to_x = 0

    # 3. 게임 캐릭터 위치 정의
    character_x_pos += character_to_x
    # 경계값 설정
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    # 무기 위치 조정
    weapons = [[w[0], w[1] - weapon_speed] for w in weapons]

    # 천장에 무기 닿으면 없앤다
    weapons = [[w[0], w[1]] for w in weapons if w[1] > 0]

    # 공 위치 정의
    for ball_idx, ball_val in enumerate(balls):
        ball_pos_x = ball_val['pos_x']
        ball_pos_y = ball_val['pos_y']
        ball_img_idx = ball_val['img_idx']

        ball_size = ball_images[ball_img_idx].get_rect().size
        ball_width, ball_height = ball_size[0], ball_size[1]

        # ball 경계값 처리
        # 모서리에 닿으면 반대방향으로 튕겨야한다
        if ball_pos_x < 0 or ball_pos_x > screen_width - ball_width:
            ball_val['to_x'] = ball_val['to_x'] * (-1)

        # 세로 위치: stage에 닿으면 튕긴다
        if ball_pos_y >= screen_height - stage_height - ball_height:
            ball_val['to_y'] = ball_val['init_speed_y']
        # 공이 튕긴후 올라갈때는 속도가 계속 감속 -> 0 -> 내려오면서 다시 속도 증가
        else: # 그 외
            ball_val['to_y'] += 0.5

        ball_val['pos_x'] += ball_val['to_x']
        ball_val['pos_y'] += ball_val['to_y']

    # 4. 충돌 처리
    # 총알이 공에 맞았을 때

    # 캐릭터가 공과 충돌했을 때

    # 5. 화면에 그리기
    screen.blit(background, (0, 0))

    # 총알(weapon) 그리기
    for weapon_x_pos, weapon_y_pos in weapons:
        screen.blit(weapon, (weapon_x_pos, weapon_y_pos))
    # 공 그리기
    for idx, val in enumerate(balls):
        ball_pos_x = val["pos_x"]
        ball_pos_y = val['pos_y']
        ball_img_idx = val['img_idx']
        screen.blit(ball_images[ball_img_idx], (ball_pos_x, ball_pos_y))

    screen.blit(stage, (0, screen_height - stage_height))
    screen.blit(character, (character_x_pos, character_y_pos))

    pygame.display.update() #게임화면 다시 그리기! 반드시 적어야함

# terminate pygame
pygame.quit()