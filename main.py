import pygame,time
import random
pygame.init()

display_width = 1024
display_height = 800

FPS = 20

DISPLAY = pygame.display.set_mode((display_width,display_height))

pygame.display.set_caption("Slithher")

blue = (200,30,200)
red = (255,0,0)
white =  (255,255,255)
black = (0,0,0)
green = (0,180,0)

apple = pygame.image.load("apple3.png")
snakeimg = pygame.image.load("snake.png")

direction = "right"

blocksize = 20
applesize = 30


clock = pygame.time.Clock()

smallfont = pygame.font.SysFont("Sawasdee", 25)
medfont = pygame.font.SysFont("Sawasdee", 40)
largefont = pygame.font.SysFont("purisa", 75)

def introgame():
	
	intro = True
	DISPLAY.fill(white)
	message ("Welcome to Slithher",green,-100,largefont)
	message ("The objective of the game is to eat apples",black,-40)
	message ("If you run into the edges you die !",black,10)
	message ("Press C to play or Q to quit ",black,60)
	
	while intro:
		for event in pygame.event.get():
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_q:
						pygame.quit()
						quit()
					elif event.key == pygame.K_c:
						intro = False
				elif event.type == pygame.QUIT:
						pygame.quit()
						quit()
	
def randappleGen():
	randAppleX = round(random.randrange(0,display_width-applesize))
	randAppleY = round(random.randrange(0,display_height-applesize))
	return randAppleX,randAppleY
	
	

def message(msg,color,y_displace=0,Font_type=smallfont,x_displace=0):
	
	textSurf=  Font_type.render(msg,True,color)
	
	rect = textSurf.get_rect()
	rect.center = (display_width/2)+x_displace,(display_height/2)+ y_displace
	
	DISPLAY.blit(textSurf,rect)
	pygame.display.update()	

def pauseGame():
	pause = True
	
	message("Paused",black,-70,largefont)
	message("Press C to continue or Q to quit",black,15,medfont)
	while pause:
		for event in pygame.event.get():
						if event.type == pygame.KEYDOWN:
							if event.key == pygame.K_q:
								pygame.quit()
								quit()
							elif event.key == pygame.K_c:
								pause = False
						
						elif event.type == pygame.QUIT:
								pygame.quit()
								quit()
				
		
	




def snake(blocksize,snakelist,direction):
	
	if direction == "right":
		head = pygame.transform.rotate(snakeimg,270)
	elif direction == "left":
		head = pygame.transform.rotate(snakeimg,90)
	elif direction == "up":
		head = snakeimg
	elif direction == "down":
		head = pygame.transform.rotate(snakeimg,180)
	
	
	DISPLAY.blit(head,(snakelist[-1][0],snakelist[-1][1]))
	
	for XnY in snakelist[:-1]:
		pygame.draw.rect(DISPLAY,green,[XnY[0],XnY[1],blocksize,blocksize])
		
	



def gameloop():
	
	global direction
	
	
	
	gamexit = False
	gameover = False
	lead_x = display_width/2
	lead_y = display_height/2
	
	lead_x_change = blocksize
	lead_y_change = 0
	
	snakeList = []
	snakeLength = 1
	score = snakeLength-1
	randAppleX , randAppleY = randappleGen()
	
	while not gamexit:
		if gameover:
			
			message("Game over !",blue,-50,largefont)
			message("Press C to play again or Q to quit",black,50,medfont)
			
		while gameover:		
			for event in pygame.event.get():
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_q:
						gameover = False
						gamexit = True
					elif event.key == pygame.K_c:
						gameloop()
				elif event.type == pygame.QUIT:
						gamexit = True 
						gameover = False		


		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				gamexit = True 
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					lead_x_change = -blocksize
					lead_y_change = 0
					direction = "left"
				elif event.key == pygame.K_RIGHT:
					lead_x_change = blocksize
					lead_y_change = 0
					direction = "right"
				elif event.key == pygame.K_UP:
					lead_y_change = -blocksize
					lead_x_change = 0
					direction = "up"
				elif event.key == pygame.K_DOWN:
					lead_y_change = blocksize
					lead_x_change = 0
					direction = "down"
				elif event.key == pygame.K_p:
					pauseGame()
				

		if lead_x >= display_width or lead_x < 0 or lead_y >= display_height or lead_y < 0:
			gameover = True 
		
		lead_x +=lead_x_change
		lead_y += lead_y_change			
			
		DISPLAY.fill(white)
		
		DISPLAY.blit(apple,(randAppleX,randAppleY))
		
		
		snakeHead = []
		snakeHead.append(lead_x)
		snakeHead.append(lead_y)
		snakeList.append(snakeHead)
		
		if len(snakeList) > snakeLength:
			del snakeList[0]
		
		snake(blocksize,snakeList,direction)
		
		for segment in snakeList[:-1]:
			if segment == snakeHead:
				gameover = True
		
		score = snakeLength-1
		 
		message("Score: " + str(score),black,-display_height/2+20,smallfont,-display_width/2+60)
		
		pygame.display.update()
		
			
		if lead_x >= randAppleX and lead_x <= randAppleX+applesize or lead_x + blocksize >= randAppleX and lead_x + blocksize <= randAppleX + applesize:
			if lead_y >= randAppleY and lead_y <= randAppleY+applesize or lead_y + blocksize >= randAppleY and lead_y + blocksize <= randAppleY + applesize:
				randAppleX , randAppleY = randappleGen()
				snakeLength+=1
			
		
		
		
		clock.tick(FPS)	
		
	DISPLAY.fill(white)
	message("Good Bye !!",red)
	
	time.sleep(1)

	pygame.quit()

	quit()
introgame()
gameloop()
