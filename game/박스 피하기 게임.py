import pygame
import random
##################################################################
# 기본 초기화 (반드시 해야 하는 것들)
pygame.init()

#화면 크기 설정
screen_width = 480 #가로크기
screen_height = 640 #세로크기
screen = pygame.display.set_mode((screen_width, screen_height))

#화면타이틀 설정
pygame.display.set_caption("똥 피하기")

#FPS
clock = pygame.time.Clock()
##################################################################

# 1. 사용자 게임 초기화 (배경화면 , 게임 이미지, 좌표, 속도, 폰트 등)
background = pygame.image.load("D:\\파이썬\\game\\background.png")
charactor = pygame.image.load("D:\\파이썬\\game\\charactor.png")
charactor_size = charactor.get_rect().size
charactor_width = charactor_size[0]
charactor_height = charactor_size[1]
charactor_x_pos = (screen_width / 2) - (charactor_width / 2)
charactor_y_pos = screen_height - charactor_height

to_x = 0
to_y = 0

charactor_speed = 0.6

enemy = pygame.image.load("D:\\파이썬\\game\\enemy.png")
enemy_size = enemy.get_rect().size
enemy_width = enemy_size[0]
enemy_height = enemy_size[1]
enemy_x_pos = random.randint(0,screen_width - enemy_width)
enemy_y_pos = 0
enemy_speed = 20

game_font = pygame.font.Font(None,40)

total_time = 20

start_ticks = pygame.time.get_ticks()

running = True 
while running:
    dt = clock.tick(30)
    
    # 2. 이벤트  처리 (키보드, 마우스 등)
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            running = False

    # 3. 게임 캐릭터 위치 정의
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -= charactor_speed
            elif event.key == pygame.K_RIGHT:
                to_x += charactor_speed
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
    charactor_x_pos += to_x * dt
        
    if charactor_x_pos < 0:
        charactor_x_pos = 0
    elif charactor_x_pos > screen_width - charactor_width:
        charactor_x_pos = screen_width - charactor_width

    enemy_y_pos += enemy_speed
    if enemy_y_pos > screen_height:
        enemy_y_pos = 0
        enemy_x_pos = random.randint(0, screen_width - enemy_width)

    charactor_rect = charactor.get_rect()
    charactor_rect.left = charactor_x_pos
    charactor_rect.top = charactor_y_pos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

    if charactor_rect.colliderect(enemy_rect):
        print("충돌했어요")
        running = False

    screen.blit(background, (0,0))
    screen.blit(charactor, (charactor_x_pos, charactor_y_pos))
    screen.blit(enemy, (enemy_x_pos, enemy_y_pos))

    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000

    timer = game_font.render(str(int(total_time - elapsed_time)), True, (255,255,255))

    screen.blit(timer, (10,10))

    if total_time - elapsed_time <= 0:
        print("타임아웃")
        running = False

    pygame.display.update()

pygame.time.delay(2000)

pygame.quit()
