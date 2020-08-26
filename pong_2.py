import pygame as pg
import sys
import winsound

def main():
	# COLORS:
	BLACK = (0, 0, 0)
	WHITE = (255, 255, 255)
	RED = (255, 0, 0)
	YELLOW = (255, 255, 0)
	GREEN = (0, 255, 0)
	BLUE = (0, 0, 255)

	# PARAMETERS:
	PLAYER_WIDTH = 15
	PLAYER_HEIGHT = 90
	NET_WIDTH = 5
	GAP = 50
	SPEED = 3
	FPS = 60
	LEVEL = 1

	# SCREEN N CLOCK
	screen_size = (800, 600)
	screen = pg.display.set_mode(screen_size)
	pg.display.set_caption("Ping Pong RETRO")
	clock = pg.time.Clock()

	# PARAMETERS PLAYER 1
	player1_x_coord = GAP
	player1_y_coord = (screen_size[1]/2) - (PLAYER_HEIGHT/2)
	player1_y_speed = 0
	score_p1 = 0

	# PARAMETERS PLAYER 2
	player2_x_coord = screen_size[0] - GAP - PLAYER_WIDTH
	player2_y_coord = (screen_size[1]/2) - (PLAYER_HEIGHT/2)
	player2_y_speed = 0
	score_p2 = 0

	# PARAMETER BALL
	ball_x = screen_size[0]//2 
	ball_y = screen_size[1]//2
	ball_speed_x = SPEED
	ball_speed_y = SPEED
	BALL_RADIUS = 10

	game_over = False

	while not game_over:

		if LEVEL == 100:
			game_over = True

		for event in pg.event.get():
			if event.type == pg.QUIT:
				game_over = True
		
			if event.type == pg.KEYDOWN:
				# PLAYER 1
				if event.key == pg.K_w:
					player1_y_speed = -1*SPEED
				if event.key == pg.K_s:
					player1_y_speed = SPEED
				# PLAYER 2
				if event.key == pg.K_UP:
					player2_y_speed = -1*SPEED
				if event.key == pg.K_DOWN:
					player2_y_speed = SPEED

			if event.type == pg.KEYUP:
				# PLAYER 1
				if event.key == pg.K_w:
					player1_y_speed = 0
				if event.key == pg.K_s:
					player1_y_speed = 0
				# PLAYER 2
				if event.key == pg.K_UP:
					player2_y_speed = 0
				if event.key == pg.K_DOWN:
					player2_y_speed = 0

		# GIVE MOVEMENT TO PLAYERS
		if player1_y_coord > (screen_size[1] - PLAYER_HEIGHT) or player1_y_coord < 0:
			player1_y_speed *= -1
		player1_y_coord += player1_y_speed
		if player2_y_coord > (screen_size[1] - PLAYER_HEIGHT) or player2_y_coord < 0:
			player2_y_speed *= -1
		player2_y_coord += player2_y_speed

		# GIVE MOVEMENT TO BALL
		if (ball_y > screen_size[1] - BALL_RADIUS) or ball_y < BALL_RADIUS:
			ball_speed_y *= -1
		# POINT: vertical wall
		if (ball_x > screen_size[0] - BALL_RADIUS) or ball_x < BALL_RADIUS:
			ball_x = screen_size[0]//2
			ball_y = screen_size[1]//2
			ball_speed_x *= -1	
			LEVEL += 1
			#SPEED += 1
			ball_speed_x = SPEED
			ball_speed_y = SPEED
			winsound.Beep(2000, 50)

		ball_x += ball_speed_x
		ball_y += ball_speed_y

		screen.fill(BLACK)

			# TITLE N TEXT	
		font = pg.font.Font('freesansbold.ttf', 32) 
		textT = font.render('PING PONG RETRO. Nivel: ' + str(LEVEL), True, GREEN, BLUE)
		textRect = textT.get_rect()
		textRect.center = (screen_size[0]//2, 25)
		screen.blit(textT, textRect)

		# NET
		for net in range(NET_WIDTH, screen_size[1], NET_WIDTH*2):
			pg.draw.rect(screen, WHITE, (screen_size[0]//2, net, NET_WIDTH, NET_WIDTH))

		# ZONA DE DIBUJO:
		player1 = pg.draw.rect(screen, WHITE, (player1_x_coord, player1_y_coord, PLAYER_WIDTH, PLAYER_HEIGHT))
		player2 = pg.draw.rect(screen, WHITE, (player2_x_coord, player2_y_coord, PLAYER_WIDTH, PLAYER_HEIGHT))
		ball    = pg.draw.circle(screen, YELLOW, (ball_x, ball_y), BALL_RADIUS)

		# COLLIDES
		if ball.colliderect(player1) or ball.colliderect(player2):
			ball_speed_x *= -1
			winsound.Beep(1000, 50)

		# SCORES:
		if ball_x < BALL_RADIUS:
			# Point to player 2
			score_p2 += 1
			pg.draw.line(screen, RED, [0, 0], [0, screen_size[1]], BALL_RADIUS)

		if ball_x > screen_size[0] - BALL_RADIUS: 
			# Point to player 1
		    score_p1 += 1
		    pg.draw.line(screen, RED, [screen_size[0], 0], [screen_size[0], screen_size[1]], BALL_RADIUS)
		
		# PRINT THE SCORE
		font = pg.font.Font('freesansbold.ttf', 64) 
		textT1 = font.render(str(score_p1), True, BLACK, WHITE)
		textRect1 = textT1.get_rect()
		textRect1.center = (screen_size[0]//2 - 100, 100)
		screen.blit(textT1, textRect1)
		textT2 = font.render(str(score_p2), True, BLACK, WHITE)
		textRect2 = textT2.get_rect()
		textRect2.center = (screen_size[0]//2 + 100, 100)
		screen.blit(textT2, textRect2)

		pg.display.update()
		clock.tick(FPS)

if __name__ == '__main__':
	pg.init()
	main()
	pg.quit()