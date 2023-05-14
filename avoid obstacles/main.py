import pygame
import random

####################################################################
# 초기화
pygame.init()

# 화면 크기 설정
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

# 타이틀
pygame.display.set_caption("하늘에서 떨어지는 장애는 피하기 게임")

# FPS
clock = pygame.time.Clock()
####################################################################

####################################################################
# 배경 이미지
background = pygame.image.load("# 이미지 저장 후 경로 복사")

# 캐릭터
character = pygame.image.load("# 이미지 저장 후 경로 복사")
character_size = character.get_rect().size # 이미지 크기
character_width = character_size[0] # 가로
character_height = character_size[1] # 세로
character_x_pos = screen_width / 2 - (character_width / 2)
character_y_pos = screen_height - character_height

# 이동할 좌표
to_x = 0

# 이동 속도
character_speed = 0.2

# 장애물(적)
enemy = pygame.image.load("# 이미지 저장 후 경로 복사")
enemy_size = enemy.get_rect().size # 이미지 크기
enemy_width = enemy_size[0] # 가로
enemy_height = enemy_size[1] # 세로
enemy_x_pos = random.randint(0, screen_width - enemy_width)
enemy_y_pos = 0
enemy_speed = 15

# 폰트
game_font = pygame.font.Font(None, 40) # DEFULT

# 총 게임 시간
total_time = 100

# 시작 시간 정보
start_ticks = pygame.time.get_ticks() # 시작 tick을 받아옴
####################################################################

####################################################################
# 이벤트 루프
running = True # 게임 진행
while running:
    dt = clock.tick(30) # 원하는 초당 프레임 수
    # print("fps: " + str(clock.get_fps()))

    for event in pygame.event.get(): # 이벤트 발생 중
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트
            running = False
        
        if event.type == pygame.KEYDOWN: # 키를 누르는 이벤트
            if event.key == pygame.K_LEFT:
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                to_x += character_speed
        
        if event.type == pygame.KEYUP: # 키를 떼면 멈추는 이벤트
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
    
    character_x_pos += to_x * dt
####################################################################

####################################################################
    # 프레임 안에 위치 시키기(가로 경계값 처리)
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width
    
    # 세로 경계값 처리

    enemy_y_pos += enemy_speed

    if enemy_y_pos > screen_height:
        enemy_y_pos = 0 # 다시 화면 맨 위로
        enemy_x_pos = random.randint(0, screen_width - enemy_width)

    # 충돌 처리
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

    if character_rect.colliderect(enemy_rect):
        print("collision")
        running = False

####################################################################

####################################################################
    screen.blit(background, (0, 0)) # 배경 좌표
    screen.blit(character, (character_x_pos, character_y_pos)) # 캐릭터 좌표
    screen.blit(enemy, (enemy_x_pos, enemy_y_pos)) # 장애물 좌표

    # 타이머
    # 경과 시간 계산
    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000 # 초(s) 단위 표시

    timer = game_font.render(str(int(total_time - elapsed_time)), True, (0, 0, 0)) # 출력될 시간
    screen.blit(timer, (10, 10))

    # 시간이 0초 이하일 때 게임 종료
    if total_time - elapsed_time <= 0:
        print("Timeout")
        running = False
####################################################################

####################################################################
    pygame.display.update() # 게임 화면 다시 그리기

# 잠시 대기
pygame.time.delay(2000) # 2초 대기

# 종료
pygame.quit()
