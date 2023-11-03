import pygame
import pygame.freetype
 
pygame.init()
screen = pygame.display.set_mode((900, 500))
pygame.display.set_caption('My game')
clock = pygame.time.Clock()
font = pygame.freetype.Font(None, 30)
player = pygame.rect.Rect(10, 200, 20, 100)
bot = pygame.rect.Rect(870, 200, 20, 100)
ball = pygame.rect.Rect(445, 245, 10, 10)
running = True
game_status = 'game'
player_speed_y = 0
ball_speed_x = -2
ball_speed_y = 2
max_score = 1
score = [0, 0]
 
 
def move_bot():
    if ball.centery > bot.centery and ball.centerx > 450:
        bot.y += 1
    if ball.centery < bot.centery and ball.centerx > 450:
        bot.y -= 1
 
 
def ball_respawn():
    global game_status
    ball.center = (450, 250)
    if score[0] >= max_score or score[1] >= max_score:
        game_status = 'menu'
 
 
def ball_check():
    global ball_speed_y
    global ball_speed_x
    if ball.top <= 0:
        ball_speed_y = -ball_speed_y
    if ball.bottom >= 500:
        ball_speed_y = - ball_speed_y
    if ball.colliderect(bot) or ball.colliderect(player):
        ball_speed_x = -ball_speed_x
    if ball.right < 0:
        score[1] += 1
        ball_respawn()
    if ball.left > 900:
        score[0] += 1
        ball_respawn()
 
 
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if game_status == 'menu':
                game_status = 'game'
            score = [0, 0]
            if event.key == pygame.K_UP:
                player_speed_y -= 1
            if event.key == pygame.K_DOWN:
                player_speed_y += 1
 
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                player_speed_y += 1
            if event.key == pygame.K_DOWN:
                player_speed_y -= 1
    if game_status == 'game':
        player.y += player_speed_y
        ball.x += ball_speed_x
        ball.y += ball_speed_y
        ball_check()
        move_bot()
    screen.fill((0, 0, 0))
    font.render_to(screen, (440, 20), str(score[0]) + ':' + str(score[1]), (255, 255, 255))
    pygame.draw.rect(screen, (20, 200, 20), player)
    pygame.draw.rect(screen, (200, 20, 20), bot)
    pygame.draw.ellipse(screen, (255, 255, 255), ball)
    if game_status == 'menu':
        if score[0] >= max_score:
            font.render_to(screen, (200, 20), 'You win!', (255, 255, 255))
        else:
            font.render_to(screen, (200, 20), 'Computer win', (255, 255, 255))
    pygame.display.flip()
    clock.tick(60)