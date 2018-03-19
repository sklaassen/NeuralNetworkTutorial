import pygame
import numpy as np
import time
import random

BLACK = 	(0	,	0,	 0)
WHITE =     (255, 255, 255)
BLUE =      (  0,   0, 255)
GREEN =     (  0, 255,   0)
RED =       (255,   0,   0)

(width, height) = (500, 500)

(mapwidth,mapheight)= (20,20)
Map2d = np.zeros((mapwidth,mapheight))

player = [0,0]

running = True

Score = 0

def RandomiseMap():
	global Map2d
	for x in range(mapwidth):
		for y in range(mapheight):
			Map2d[x,y] = random.randint(-1,1)

def main():
	global running, screen, player,Map2d,Score
	RandomiseMap()
	pygame.init()
	screen = pygame.display.set_mode((width, height))
	pygame.display.set_caption("2D World")

	while running:
		ev = pygame.event.get()
		for event in ev:
			if event.type == pygame.QUIT:
				running = False
			if event.type == pygame.KEYDOWN:
				(x,y) = (0,0)
				if event.key == pygame.K_LEFT:
					x = -1
				if event.key == pygame.K_RIGHT:
					x = 1
				if event.key == pygame.K_UP:
					y=-1
				if event.key == pygame.K_DOWN:
					y=1
				movePlayer(x,y)


		screen.fill(BLACK)     
		drawMap(Map2d)
		pygame.draw.circle(screen, BLUE, (int(player[0]/mapwidth*width+width/mapwidth/2),int(player[1]/mapheight*height+height/mapheight/2)), 10)
		pygame.display.update()
def drawMap(mapToDraw):
	mapwidth = len(mapToDraw)
	mapheight = len(mapToDraw)
	for x in range(mapwidth):
		for y in range(mapheight):
			pygame.draw.rect(screen, GREEN, ((x/mapwidth*width,y/mapheight*height),((x+1)/mapwidth*width,(y+1)/mapheight*height)),1)
			if mapToDraw[x,y] > 0:
				pygame.draw.circle(screen, GREEN, (int(x/mapwidth*width+width/mapwidth/4),int(y/mapheight*height+height/mapheight/4)), 5)
			if mapToDraw[x,y] < 0:
				pygame.draw.circle(screen, RED, (int(x/mapwidth*width+width/mapwidth/4),int(y/mapheight*height+height/mapheight/4)), 5)
				

def movePlayer(x,y):
	global Score,player
	player[0] = player[0]+x
	player[1] = player[1]+y
	if player[0] <0:
		player[0] = player[0]+mapwidth
	if player[0] >= mapwidth:
		player[0] = player[0]-mapwidth
	if player[1] <0:
		player[1] = player[1]+mapheight
	if player[1] >= mapheight:
		player[1] = player[1]-mapheight
	Score+=Map2d[player[0],player[1]]
	Map2d[player[0],player[1]] = 0
def mapCordinate(x,y):
	if x<0:
		x += mapwidth
	elif x>= mapwidth:
		x -=mapwidth
	if y<0:
		y += mapheight
	elif y>= mapheight:
		y -=mapheight
	return (x,y)

def getSurounding():
	surounding = np.zeros((5,5))
	for x in range(player[0]-2,player[0]+2,1):
		for y in range(player[1]-2,player[1]+2,1):
			surounding[x,y] = Map2d[mapCordinate(x,y)]
	return surounding
	
if __name__ == '__main__':
	main()
else:
	RandomiseMap()
