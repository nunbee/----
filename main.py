import pygame
import sys
from game_components.player import Player
from game_components.obstacles import create_obstacles, draw_obstacles
from game_components.fragments import Fragments

### pygame 초기화 ###
pygame.init()

### 1000*600 게임 창 설정 ###
screen_width = 1000
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("킹받는 게임")

### 색상 설정 ###
white = (255, 255, 255)  # 배경 색상
black = (0, 0, 0)  # 땅, 장애물 색상

# 땅의 높이
ground_height = 50

# 플레이어 설정
player = Player(screen_width, screen_height, ground_height)

# 장애물 설정 (삼각형)
obstacles = create_obstacles(screen_width, screen_height, ground_height)

# 조각난 플레이어 설정
fragments = Fragments()

# 게임 루프
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 키 입력 처리
    keys = pygame.key.get_pressed()
    player.update(keys, fragments)

    # 충돌 감지
    if player.check_collision(obstacles) and not fragments.is_active:
        fragments.create_pieces(player.x, player.y)
        player.reset()

    # 배경 그리기
    screen.fill(white)

    # 땅 그리기
    pygame.draw.rect(screen, black, (0, screen_height - ground_height, screen_width, ground_height))

    # 장애물 그리기 (삼각형 3개)
    draw_obstacles(screen, obstacles)

    # 플레이어 그리기
    if fragments.is_active:
        fragments.update_and_draw(screen)
    else:
        player.draw(screen)

    # 화면 업데이트
    pygame.display.flip()

    # 프레임 속도 설정
    pygame.time.Clock().tick(30)

# pygame 종료
pygame.quit()
sys.exit()
