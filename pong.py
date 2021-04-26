import pygame
import random

pygame.init()
clock=pygame.time.Clock()
screen=pygame.display.set_mode((4,8))
def ball_animation():
	global velocity_bx,velocity_by,player_score,opponent_score
	ball.x=ball.x+velocity_bx
	ball.y=ball.y+velocity_by
	if ball.top<=0 or ball.bottom>=800:
		velocity_by=(velocity_by*(-1))
	if ball.left<=0:
		ball.center=(525,400)
		velocity_by=velocity_by*random.choice((-1,1))
		player_score+=1
	if ball.right>=1080:
		ball.center=(525,400)
		opponent_score+=1
	if ball.colliderect(player) or ball.colliderect(opponent):
		velocity_bx=(velocity_bx*(-1))
		
def opponent_ai():
	if opponent.top<ball.y:
		opponent.top+=opponent_speeddown
	if opponent.bottom>ball.y:
		opponent.bottom-=opponent_speedup
	if opponent.top<0:
		opponent.top=0
	if opponent.bottom>800:
		opponent.bottom=800

font=pygame.font.SysFont(None,80)
def text_screen(text,color,x,y):
	screen_text=font.render(text,True,color)
	screen.blit(screen_text,[x,y])
	
player_velocity=0
opponent_speedup=10
opponent_speeddown=13
velocity_bx=4
velocity_by=4
player_score=0
opponent_score=0
ball=pygame.Rect(525,400,30,30)
player=pygame.Rect(1050,400,20,150)
opponent=pygame.Rect(5,400,20,150)
game_exit=False
	
while not game_exit:
	screen.fill((0,0,0))
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			game_exit=True
			
		if event.type==pygame.KEYDOWN:
			if event.key==pygame.K_UP:
				player_velocity-=10
			if event.key==pygame.K_DOWN:
				player_velocity+=10
				
	ball_animation()
	opponent_ai()
	player.y+=player_velocity
	if player.top<0:
		player.top=0
	if player.bottom>800:
		player.bottom=800
	
	pygame.draw.rect(screen,(255,255,255),player)
	pygame.draw.rect(screen,(255,255,255),opponent)
	pygame.draw.ellipse(screen,(255,255,255),ball)
	pygame.draw.rect(screen,(255,255,255),(0,800,1080,50))
	text_screen(f"{player_score}",(255,255,255),1000,10)
	text_screen(f"{opponent_score}",(255,255,255),10,10)
	pygame.display.update()
	clock.tick(60)
pygame.quit()
quit()