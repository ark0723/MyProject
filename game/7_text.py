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

# FPS: Frame Per Second
clock = pygame.time.Clock()


# load character
character = pygame.image.load('C:/Users/ark07/PycharmProjects/game/character.png')

character_size = character.get_rect().size #이미지 크기 구하기
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width - character_width)/2  # 화면 가로축 절반 크기에 두겠다
character_y_pos = screen_height - character_height  # 화면 맨 밑에 두기

# 이동할 좌표
to_x, to_y = 0, 0

# 이동속도(moving speed)
character_speed = 0.6

# enemy character
enemy = pygame.image.load('C:/Users/ark07/PycharmProjects/game/enemy.png')

enemy_size = enemy.get_rect().size #이미지 크기 구하기
enemy_width = enemy_size[0]
enemy_height = enemy_size[1]
enemy_x_pos = (screen_width - enemy_width)/2  # 화면 가로축 절반 크기에 두겠다
enemy_y_pos = (screen_height - enemy_height)/2  # 화면 맨 밑에 두기


# font
game_font = pygame.font.Font(None, 40) #폰트 객체 생성(폰트이름, 크기)

#총 시간
total_time = 10

# 시작시간
start_ticks = pygame.time.get_ticks() # 시작 tick을 받아옴


#event loop
running = True #game ing?
while running:
    dt = clock.tick(60)  # fps=60으로 설정 - 높은 값일수록 동작이 부드러움

    #캐릭터가 1초 동안에 100만큼 이동을 해야한다고 가정
    # 10 fps: 1초 동안에 10번 동작 -> 1번에 몇만큼 이동? 10만큼! 10 * 10 = 100
    # 20 fps: 1초 동안에 20번 동작 -> 1번에 5만큼! 5*20 = 100
    #print("fps: "+str(clock.get_fps()))
    for event in pygame.event.get(): #if event happen
        if event.type == pygame.QUIT: #호출한 이벤트가 창닫기면
            running = False

        if event.type == pygame.KEYDOWN: #keyboard를 눌렀는지 체크
            if event.key == pygame.K_LEFT: #캐릭터를 왼쪽으로
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT: #캐릭터를 오른쪽으로
                to_x += character_speed
            elif event.key == pygame.K_UP:
                to_y -= character_speed
            elif event.key == pygame.K_DOWN:
                to_y += character_speed
            else:
                pass

        if event.type == pygame.KEYUP: #키보드에서 손을 떼면 멈춤
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0

    character_x_pos += to_x * dt
    character_y_pos += to_y * dt

    # x 경계값 설정
    if character_x_pos < 0 :
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    # y 경계값 설정
    if character_y_pos < 0 :
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height

    # 충돌처리(collision)를 위한 rect정보 업데이트
    character_rect = character.get_rect() #좌표, width, height 포함:  rect(0,0,70,70)
    #print(character_rect)
    character_rect.left = character_x_pos
    character_rect.top =  character_y_pos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

    # 충돌체크
    if character_rect.colliderect(enemy_rect): #캐릭터가 적과 충돌했는지 체크
        print("Collision!")
        running = False # terminate game

    screen.blit(background, (0,0)) # 배경그리기: 어디에다 나타낼지 좌표 설정 필요
    screen.blit(character,(character_x_pos, character_y_pos)) #캐릭터
    screen.blit(enemy, (enemy_x_pos, enemy_y_pos)) #적

    # timer
    # 경과시간: ms를 1000으로 나누어서 초(second) 단위로 표시
    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000
    # timer: 출력할 글자, True, 폰트 색깔
    timer = game_font.render(str(int(total_time - elapsed_time)), True, (255,255,255)) #10, 9, 8, 7, ...
    screen.blit(timer, (10,10))

    #만약 시간이 0이하이면 게임 종료
    if total_time - elapsed_time <= 0:
        print("타임아웃")
        running = False

    pygame.display.update() #게임화면 다시 그리기! 반드시 적어야함

#잠시 대기
pygame.time.delay(2000) #2초 정도 대기

# terminate pygame
pygame.quit()