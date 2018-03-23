import pygame
import sys
import random
import numpy as np

tile = np.dtype([('terrain',np.uint8),('item',np.uint16),('player',np.bool)])

class Player(object):

	def __init__(self, hp,viewrange):
		self.maxhp = hp
		self.viewrange = viewrange
		self.position = np.array([5,5])
		
		
class map(object):
	def __init__(self, size):
		self.grid = np.empty((size,size), dtype=tile)
		self.player = Player(10,3)
		for x in range(size):
			for y in range(size):
				self.grid[x,y]['player']= False
				self.grid[x,y]['player']= 0
				if x<self.player.viewrange or y<self.player.viewrange or x>=size-self.player.viewrange or y>=size-self.player.viewrange:
					self.grid[x,y]['terrain']= 0
				else:
					self.grid[x,y]['terrain'] = random.randint(2,4)

		
	def getMap(self):
		grid2 = np.copy(self.grid)
		grid2[self.player.position[0],self.player.position[1]]['player'] = True
		grid2 = grid2[max(self.player.position[0]-self.player.viewrange,0):self.player.position[0]+self.player.viewrange+1,self.player.position[1]-self.player.viewrange:self.player.position[1]+self.player.viewrange+1]
		return grid2
	def move(self,direction):
		position = self.player.position+direction
		position[0] = max(min(self.grid.shape[0]-1,position[0]),1)
		position[1] = max(min(self.grid.shape[1]-1,position[1]),1)
		
		if self.grid[position[0],position[1]]['terrain']!=0:
			print("Position: " + str(position) + " grid: " + str(self.grid[position[0],position[1]]))
			self.player.position = position
		
def main():
	pygame.init()
	clock = pygame.time.Clock()
	fps = 50
	bg = [0, 0, 0]
	size =[700, 700]
	screen = pygame.display.set_mode(size)
	Map = map(20)

	print(str(Map.getMap()))
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return False

			elif event.type == pygame.KEYDOWN:
				direction = [0,0]
				if event.key == pygame.K_LEFT:
					direction[0] = -1
				elif event.key ==pygame.K_RIGHT:
					direction[0] = 1
				elif event.key ==pygame.K_UP:
					direction[1] = -1	
				elif event.key ==pygame.K_DOWN:
					direction[1] = 1	
				Map.move(direction)
				print(str(Map.getMap()))

		screen.fill(bg)
		drawMap = Map.getMap()

		for x in range(drawMap.shape[0]):
			for y in range(drawMap.shape[1]):
				if drawMap[x,y]['terrain'] == 0:
					screen.fill([0, 0, 0],rect=[x*100,y*100,100,100])
				elif drawMap[x,y]['terrain'] == 2:
					screen.fill([0, 100, 0],rect=[x*100,y*100,100,100])
				elif drawMap[x,y]['terrain'] == 3:
					screen.fill([0, 50, 200],rect=[x*100,y*100,100,100])
				elif drawMap[x,y]['terrain'] == 4:
					screen.fill([0, 50, 200],rect=[x*100,y*100,100,100])
				if drawMap[x,y]['player']:
					pygame.draw.circle(screen,[200, 200, 0],[x*100+50,y*100+50],20,20)

		pygame.display.update()
		clock.tick(fps)
	pygame.quit()
	sys.exit


if __name__ == '__main__':
	main()