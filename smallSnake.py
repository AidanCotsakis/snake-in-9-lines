import pygame, random
while True:
	if 'win' not in globals() or (pygame.display.update() and False) or (clock.tick(10) and False) or snake[-1][0] < 0 or snake[-1][0] > 19 or snake[-1][1] < 0 or snake[-1][1] > 19 or [snake[-1][0], snake[-1][1]] in [[i[0], i[1]] for i in snake[0:-1]]: win, snake, direction, clock, directions, cantGo, apple = (pygame.display.set_mode((1000,1000), pygame.NOFRAME, 0), [[1,10,5,40,(0,230,0)],[1.5,10,5,40,(0,230,0)],[2,10,5,40,(0,230,0)],[2.5,10,5,40,(0,230,0)],[3,10,0,50,(0,255,0)]], [1,0], pygame.time.Clock(), {pygame.K_w : [0,-1], pygame.K_s : [0,1], pygame.K_a : [-1,0], pygame.K_d : [1,0]}, {pygame.K_w : [0,1], pygame.K_s : [0,-1], pygame.K_a : [1,0], pygame.K_d : [-1,0]}, [random.randint(0,19),random.randint(0,19),5,40,(255,0,0)])
	for event in pygame.event.get():
		if (event.type == pygame.QUIT and pygame.quit()) or event.type == pygame.KEYDOWN and (event.key == pygame.K_w or event.key == pygame.K_a or event.key == pygame.K_s or event.key == pygame.K_d) and direction != cantGo[event.key]: direction = directions[event.key]
	if win.fill((0,0,0)) or True: snake = snake[0:-1] + [[snake[-1][0], snake[-1][1], 5,40,(0,230,0)],[snake[-1][0]+direction[0]/2, snake[-1][1]+direction[1]/2, 5,40,(0,230,0)],[snake[-1][0]+direction[0], snake[-1][1]+direction[1], 0,50,(0,255,0)]]
	if [apple[0], apple[1]] in [[i[0], i[1]] for i in snake]: apple = [random.randint(0,19),random.randint(0,19),5,40,(255,0,0)]
	else: snake = snake[2:]
	for box in [apple] + snake: pygame.draw.rect(win, box[4], (box[0]*50+box[2], box[1]*50+box[2], box[3], box[3]))