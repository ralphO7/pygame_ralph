import pygame
import random
from column import Column

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
        bird_y -= 2


pygame.init()

pygame.display.set_caption('bro srxly')


scrn = pygame.display.set_mode((500, 500))

points = 0
font = "JetBrainsMono-Medium.ttf"

bird = pygame.Rect(bird_x, bird_y, 45, 45)
column = pygame.Rect(random.randint(10, 489), 0, 5, 55)
font1 = pygame.font.Font(font, 40)


while True:
    
    #mouse pos 
    mx, my = pygame.mouse.get_pos()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        if event.type == pygame.KEYDOWN:
            move()
    if bird.colliderect(column):
        column.x = random.randint(10, 470)
        column.y = random.randint(10, 470)
        points += 1
    
    #color first
    scrn.fill('pink')
    bird.y = my
    bird.x = mx     
    points_count = font1.render(str(points), True, "white")
    
    check_boundaries()
    
    scrn.blit(points_count, (240, 10))
    pygame.draw.rect(scrn, 'red', column)
    pygame.draw.rect(scrn, 'red', bird)
    
    pygame.display.update()