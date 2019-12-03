import pygame, random 
from pygame.locals import *


def on_grid_random():
	x = random.randint(0,590)
	y = random.randint(0,590)
	return (x//10 * 10, y//10 * 10)

def on_grid():
	x = (([-1,+1]))
	y = ([-1,+1])
	return (x, y//10 * 10)

def colision(c1, c2):
	return ((c1[0] == c2[0]) and (c1[1] == c2[1]))

UP = 0
RIGHT = 1
DOWN = 2
LEFT =3

pygame.init()
screen = pygame.display.set_mode((600,600))
pygame.display.set_caption('Snake')

snake = [(200,200), (210,200), (220, 200)]
snake_skin = pygame.Surface((10,10))
snake_skin.fill((255,253,255))

aplle_pos = on_grid_random()
aplle = pygame.Surface((10,10))
aplle.fill((255,0,0))

placar_con = 0
placar_pos = ((10, 10))
placar = pygame.Surface((10,10))
placar.fill((255,255,255))

parede = on_grid()
my_direc = LEFT
clock = pygame.time.Clock()
while True:
	clock.tick(20)
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()

		if event.type == KEYDOWN:
			if event.key == K_UP:
				my_direc = UP
			if event.key == K_LEFT:
				my_direc = LEFT
			if event.key == K_DOWN:
				my_direc = DOWN
			if event.key == K_RIGHT:
				my_direc = RIGHT
	if colision(snake[0],parede):
			pygame.quit()
			print("Placar = " + placar_con)
	if colision(snake[0],aplle_pos):
		aplle_pos = on_grid_random()
		snake.append((0,0)) 
		placar_con = placar_con + 1
	
	for i in range(len(snake) -1,0,-1):
		snake[i] = (snake[i-1][0], snake[i-1][1])
	
	if my_direc == UP:
		snake[0] = (snake[0][0], snake[0][1] -10)
	if my_direc == DOWN:
		snake[0] = (snake[0][0], snake[0][1] +10)
	if my_direc == RIGHT:
		snake[0] = (snake[0][0] +10 , snake[0][1]) 
	if my_direc == LEFT:
		snake[0] = (snake[0][0] -10, snake[0][1])
	
	
	screen.fill((0,0,0))
	screen.blit(aplle, aplle_pos)
	for pos in snake:
		screen.blit(snake_skin,pos)  
	
	pygame.display.update()