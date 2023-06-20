import pygame
import random

# 初始化 Pygame
pygame.init()

# 視窗寬度和高度
window_width = 800
window_height = 600

# 定義顏色
white = (255, 255, 255)
blue = (0, 0, 255)
yellow = (255, 255, 0)

# 定義主角尺寸和移動速度
player_size = 50
player_speed = 10

# 定義金幣尺寸和移動速度
coin_size = 30
coin_speed = 5

# 初始化視窗
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("吃金幣遊戲")

# 初始化遊戲時的位置和分數
player_x = window_width // 2
player_y = window_height // 2
score = 0

# 創建字體
font = pygame.font.Font(None, 36)

def generate_coin():
    """隨機生成金幣的位置"""
    coin_x = random.randint(0, window_width - coin_size)
    coin_y = random.randint(0, window_height - coin_size)
    return coin_x, coin_y

def draw_player(x, y):
    """繪製主角"""
    player_image = pygame.image.load('charactor.png')
    window.blit(player_image, (x, y))

def draw_coin(x, y):
    """繪製金幣"""
    coin_image = pygame.image.load('coin.png')  
    window.blit(coin_image, (x, y))

def display_score(score):
    """顯示分數"""
    score_text = font.render("分數: " + str(score), True, white)
    window.blit(score_text, (10, 10))

def collision_detection(player_x, player_y, coin_x, coin_y):
    """碰撞檢測"""
    if player_x < coin_x + coin_size and player_x + player_size > coin_x and \
       player_y < coin_y + coin_size and player_y + player_size > coin_y:
        return True
    return False

# 初始化金幣位置
coin_x, coin_y = generate_coin()

# 遊戲迴圈
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 取得鍵盤輸入
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_x += player_speed
    if keys[pygame.K_UP]:
        player_y -= player_speed
    if keys[pygame.K_DOWN]:
        player_y += player_speed

    # 碰撞檢測
    if collision_detection(player_x, player_y, coin_x, coin_y):
        coin_x, coin_y = generate_coin()
        score += 1

    # 清空視窗
    window.fill((0, 0, 0))

    # 繪製主角和金幣
    draw_player(player_x, player_y)
    draw_coin(coin_x, coin_y)

    # 顯示分數
    display_score(score)

    # 更新視窗
    pygame.display.update()
    clock.tick(30)

# 結束遊戲
pygame.quit()
