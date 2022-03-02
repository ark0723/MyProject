import pygame
##################################################
#기본 초기화(반드시 해야하는 것들)
pygame.init() # initialize

# screen size
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

# set title for screen
pygame.display.set_caption("오락실게임") #game name

# load background image
background = pygame.image.load('C:/Users/ark07/PycharmProjects/game/background.png')

# FPS: Frame Per Second
clock = pygame.time.Clock()
##################################################

# 1. 사용자 게임 초기화(배경화면, 게임 이미지, 좌표, 속도, 폰드 설정 등)

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

    pygame.display.update() #게임화면 다시 그리기! 반드시 적어야함

# terminate pygame
pygame.quit()