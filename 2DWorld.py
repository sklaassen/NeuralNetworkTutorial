import pygame
import sys
import random
import numpy as np

class Sprite(pygame.sprite.Sprite):
    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([20, 20])
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.center = pos

class Tank(object):
	moveSpeed = [3,3]
	teamColors = [(255,0,0),(0,0,255)]
	def __init__(self, team,group):
		print("Initialising Tank")
		self.sprite = Sprite([random.randint(0,200),random.randint(0,200) ])
		self.sprite.image.fill(self.teamColors[team])
		group.add(self.sprite)

	def shoot(self,targetPos,projectileGroup):
		proj = Sprite(self.sprite.rect)

	def move(self,direction):
		self.sprite.rect.x += direction[0]*self.moveSpeed[0]
		self.sprite.rect.y += direction[1]*self.moveSpeed[1]
		self.sprite.rect.x = max(0, min(self.sprite.rect.x, 500))
		self.sprite.rect.y = max(0, min(self.sprite.rect.y, 500))

def main():
	pygame.init()
	clock = pygame.time.Clock()
	fps = 50
	bg = [255, 255, 255]
	size =[500, 500]
	screen = pygame.display.set_mode(size)
	players = []
	obstacles = []
	projectile = []
	playersGroup = pygame.sprite.Group()
	for teams in range(2):
		for player in range(1):
			players.append(Tank(teams,playersGroup))
	projectileGroup = pygame.sprite.Group()
	obstacleGroup = pygame.sprite.Group()

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return False

		key = pygame.key.get_pressed()
		direction = [0,0]
		if key[pygame.K_LEFT]:
			direction[0] = -1
		elif key[pygame.K_RIGHT]:
			direction[0] = 1
		if key[pygame.K_UP]:
			direction[1] = -1
		elif key[pygame.K_DOWN]:
			direction[1] = 1
		players[0].move(direction)
		#pressed1, pressed2, pressed3 = pygame.mouse.get_pressed()
		if key[pygame.MOUSEBUTTONDOWN]:
			players[0].shoot(pygame.mouse.get_pos(),projectileGroup)

		screen.fill(bg)
		playersGroup.draw(screen)
		projectileGroup.draw(screen)


        #hit = pygame.sprite.spritecollide(player, wall_group, False)

        #if hit:

            #player.image.fill((0, 0, 0))

		pygame.display.update()
		clock.tick(fps)

	pygame.quit()
	sys.exit


if __name__ == '__main__':
	main()