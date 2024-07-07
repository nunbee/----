import pygame
import sys
import random

### pygame 초기화 ###
pygame.init()

### 1000*600 게임 창 설정 ###
screen_width = 1000
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("킹받는 게임")

### 색상 설정 ###
white = (255, 255, 255)         # 배경 색상
black = (0, 0, 0)               # 땅, 장애물 색상
player_color = (255, 0, 0)      # 플레이어 색상 (빨간색)

# 땅의 높이
ground_height = 50

### 플레이어 설정 ###
player_width = 15
player_height = 20
# 플레이어 시작 위치 좌표
player_x = 50  
player_y = screen_height - ground_height - player_height
# 플레이어 속도
player_speed = 8
# 점프 설정
is_jumping = False
gravity = 2         # 중력
jump_height = 15    # 점프 속도
jump_velocity = jump_height

# 장애물 설정 (삼각형) =============================
obstacle_width = 10  
obstacle_height = 20 
obstacle_color = black

# 장애물 3개 설정 (연달아 붙어있도록)
obstacle1_x_start = screen_width // 2 - (3 * obstacle_width) // 2 - 100
obstacle2_x_start = screen_width // 2 + 200
obstacles = []
for i, obstacle_x_start in enumerate([obstacle1_x_start, obstacle2_x_start]):
    for j in range(3):
        obstacle_x = obstacle_x_start + j * obstacle_width
        obstacle_y = screen_height - ground_height - obstacle_height
        points = [(obstacle_x, obstacle_y + obstacle_height),
                  (obstacle_x + obstacle_width // 2, obstacle_y),
                  (obstacle_x + obstacle_width, obstacle_y + obstacle_height)]
        obstacles.append(points)

# 조각난 플레이어 설정 ==========================================================
pieces = []
fragment_time = 0

def create_pieces():
    global pieces, fragment_time
    pieces = []
    for _ in range(20):
        piece_x = player_x + random.randint(-10, 10)
        piece_y = player_y + random.randint(-10, 10)
        piece_dx = random.choice([-1, 1]) * random.random() * 5
        piece_dy = random.choice([-1, 1]) * random.random() * 5
        pieces.append([piece_x, piece_y, piece_dx, piece_dy])
    fragment_time = pygame.time.get_ticks()
    
# 게임 루프 ==================================================================
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 키 입력 처리
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_x += player_speed
    if keys[pygame.K_SPACE] and not is_jumping and not pieces:
        is_jumping = True
        jump_velocity = -jump_height

    # 점프 로직
    if is_jumping:
        player_y += jump_velocity
        jump_velocity += gravity
        if player_y >= screen_height - ground_height - player_height:
            player_y = screen_height - ground_height - player_height
            is_jumping = False

    # 플레이어가 창 밖으로 나가지 않도록 경계 검사
    if player_x < 0:
        player_x = 0
    if player_x + player_width > screen_width:
        player_x = screen_width - player_width

    # 충돌 감지
    for obstacle_points in obstacles:
        obstacle_x = obstacle_points[0][0]
        obstacle_y = obstacle_points[1][1]
        if player_x < obstacle_x + obstacle_width and player_x + player_width > obstacle_x and \
           player_y < obstacle_y + obstacle_height and player_y + player_height > obstacle_y and not pieces:
            create_pieces()  # 플레이어 조각 생성
            player_x = 50  # 플레이어 초기 위치 재설정
            player_y = screen_height - ground_height - player_height

    # 배경 그리기
    screen.fill(white)

    # 땅 그리기
    pygame.draw.rect(screen, black, (0, screen_height - ground_height, screen_width, ground_height))

    # 장애물 그리기 (삼각형 3개)
    for obstacle_points in obstacles:
        pygame.draw.polygon(screen, obstacle_color, obstacle_points)

    # 플레이어 그리기
    if pieces:
        for piece in pieces:
            piece[0] += piece[2]
            piece[1] += piece[3]
            pygame.draw.rect(screen, player_color, (piece[0], piece[1], 5, 5))
        
        # 1초 후 플레이어 초기화 (산산조각나고 1초 뒤 초기화)
        if pygame.time.get_ticks() - fragment_time > 1000:
            pieces = []
            player_x = 50
            player_y = screen_height - ground_height - player_height
    else:
        pygame.draw.rect(screen, player_color, (player_x, player_y, player_width, player_height))

    # 화면 업데이트
    pygame.display.flip()

    # 프레임 속도 설정
    pygame.time.Clock().tick(30)

# pygame 종료
pygame.quit()
sys.exit()



