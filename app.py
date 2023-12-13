import pygame
import random


running = True
# coordinates of the bird 
bird_x = 23 
bird_y = 0 

velocity = random.randint(1, 10)

def check_boundaries():
    global bird_y, bird_x
    
    if bird_y > 500 or bird_y < 10:
        bird_y = random.randint(1, 499)
    if bird_x > 500 or bird_x < 10:
        bird_x = random.randint(1, 499)
    

def move():
    global bird_y, bird_x
    if event.key == pygame.K_DOWN:
        bird_y += 10

    if event.key == pygame.K_UP:
        bird_y -= 10

    if event.key == pygame.K_LEFT:
        bird_x -= 10

    if event.key == pygame.K_RIGHT:
        bird_x += 10

    if event.key == pygame.K_SPACE:
        bird_x += 10
        bird_y += 2

pygame.init()

pygame.display.set_caption('bro srxly')

scrn = pygame.display.set_mode((500, 500))

bird = pygame.Rect(bird_x, bird_y, 45, 45)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        if event.type == pygame.KEYDOWN:
            move()
    scrn.fill('pink')
    bird.y = bird_y
    bird.x = bird_x     
    pygame.draw.rect(scrn, 'red', bird)
    check_boundaries()
    pygame.display.update()