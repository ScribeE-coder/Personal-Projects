import pygame 
import random
pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800 
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Rectangle art stuff')
clock = pygame.time.Clock() 

rects = []
colors = [(0, 0, 0), (100, 100, 100), (100, 50, 20), (200, 200, 200), (200, 150, 200), (100, 200, 100), (100, 50, 100), (50, 50, 50), (160, 0, 0)]

class Objects(): 
    def __init__(self, x, y, width, height, collision_rect=False):
        self.x = x 
        self.y = y 
        self.width = width 
        self.height = height
        self.collision_rect = collision_rect 
        num = random.randint(0, len(colors)-1)
        self.color = colors[num]

    def create_laser(self): 
        return None 
    
    def create_rect(self): 
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        rects.append(self.rect) 

    def rect_move(self, keys): 
        if keys[pygame.K_w]: 
            self.y -= 5
        if keys[pygame.K_a]: 
            self.x -= 5
        if keys[pygame.K_s]: 
            self.y += 5  
        if keys[pygame.K_d]: 
            self.x += 5

        if keys[pygame.K_SPACE]: 
            self.create_laser()

        if keys[pygame.K_c]: 
            num = random.randint(0, len(colors)-1)
            self.color = colors[num]           

    def draw(self):
        for rect in rects: 
            pygame.draw.rect(screen, self.color, rect) 
        
rect = Objects(300, 400, 100, 200)
two_rect = Objects(300, 400, 100, 200)
three_rect = Objects(300, 400, 100, 200) 

running = True 
while running:
    keys = pygame.key.get_pressed()  
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            running = False
    
    screen.fill((217, 217, 217))
    rect.create_rect() 
    rect.draw()
    rect.rect_move(keys)   
    pygame.display.update()
    clock.tick(60) 
