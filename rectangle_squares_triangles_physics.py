import pygame
import sys
import pymunk
import random    

pygame.init()

SCREEN_WIDTH = 640 
SCREEN_HEIGHT = 640 

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
space = pymunk.Space() 
space.gravity = (0, 300)

clock = None 

shapes = [] 

class Laser(): 
    def __init__(self, x, y, width, height): 
        self.x = x 
        self.y = y 
        self.width = width 
        self.height = height 
        self.color = (100, 100, 100)
        self.mass = 3 

    def create_laser(self, space, size): 
        body = pymunk.Body(self.mass, 0, pymunk.Body.DYNAMIC)
        body.position = (self.x, self.y)
        self.shape = pymunk.Poly.create_box(body, (size, 3))
        self.elasticity = 0.01 
        space.add(body, self.shape)

    def laser_move(self, keys): 
        for event in event.type: 
            if event == pygame.KEYDOWN:
                return None 
            
    def laser_draw(self): 
        return None               
            

class Rectangle(): 
    def __init__(self, x, y, width, height): 
        self.x = x 
        self.y = y 
        self.width = width 
        self.height = height
        self.color = (0, 0, 0)
        self.shape = None 
        self.right = True 

    def create_rect(self, space, size): 
        # rectangles should be static objects 
        body = pymunk.Body(body_type=pymunk.Body.STATIC) 
        body.position = (self.x, self.y)
        self.shape = pymunk.Poly.create_box(body, (size, 5))
        self.elasticity  = 0.01 
        space.add(body, self.shape) 

    def rect_move(self): # movement will be independent of player controls don't yell at me for a static object moving
       # move right until rectangle hits the right edge of the screen
       if self.x < SCREEN_WIDTH - self.width and self.right:
        self.x += 0.3

        # once we hit the right edge, move to the left 
       elif self.x >= SCREEN_WIDTH - self.width:
           self.x -= 0.3
           self.right = False 

        # move left until rectangle hits the left edge of the screen
       elif self.x > 0 and not self.right:
           self.x -= 0.3

        # once we hit left edge, move to the right
       elif self.x <=0: 
           self.x += 0.3 
           self.right = True 
       
       self.shape.body.position = (self.x, self.y)

    def draw(self): 
        pos_x = int(self.shape.body.position.x) 
        pos_y = int(self.shape.body.position.y)
        rect = pygame.Rect(pos_x, pos_y, self.width, self.height) 
        pygame.draw.rect(screen, self.color, rect)

class Square(): 
    def __init__(self, x, y, width, height, mass):
        self.x = x 
        self.y = y
        self.width = width 
        self.height = height
        self.mass = mass 
        self.color = (0, 0, 0)
        self.shape = None 

        if self.width != self.height: 
            print("This is not a square smh")
            raise TypeError
    
    def create_square(self, space, size): 
        # square objects should be kinematic --> don't respond to gravity 
        body = pymunk.Body(self.mass, 1, pymunk.Body.KINEMATIC) 
        body.position = (self.x, self.y)
        self.shape = pymunk.Poly.create_box(body, (size, 5))
        self.shape.elasticity = 0.05 

    def collision_check(self): 
        return None  

    def boundary_check(self): 
       if self.y < 0:
           return False
       else: 
           return True
    
    def move(self):
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_w]:
            if self.boundary_check():
                self.y -= 1

        if keys[pygame.K_a]:
            self.boundary_check() 
            self.x -= 1 

        if keys[pygame.K_s]: 
            self.boundary_check()
            self.y += 1 

        if keys[pygame.K_d]: 
            self.boundary_check() 
            self.x += 1 

        self.shape.body.position = (self.x, self.y) 
        self.collision_check()         

    def draw(self): 
        pos_x = int(self.shape.body.position.x)
        pos_y = int(self.shape.body.position.y)
        square = pygame.Rect(pos_x, pos_y, self.width, self.height)
        pygame.draw.rect(screen, self.color, square)
        

class Triangle(): 
    def __init__(self, x, y , width, height):
        self.x = x 
        self.y = y 
        self.width = width 
        self.height = height
        self.color = (0, 0, 0)
        self.shape = None
        self.mass = None 

    def create_triangles(self):
        # triangle objects should be dynamic  
        body = pymunk.Body(self.mass, 1, pymunk.Body.DYNAMIC)
        body.position = (self.x, self.y)
        self.shape = None 

    def draw(): 
        pos_x = None 
        pos_y = None
        triangle = None 

class Circle(): 
    def __init__(self, x, y, width, height): 
        self.x = x
        self.y = y 
        self.width = width 
        self.height = height 
        self.color = (0, 0, 0)
        self.shape = None 

    def create_circles(self):
        return None 
    
    def draw(): 
        pos_x = None 
        pos_y = None 
        circle = None 

def draw(shapes):
    screen.fill((255, 255, 255))
    
    for shape in shapes: 
        shape.draw()

rectangle = Rectangle(320, 320, 100, 150) 
rect_space = rectangle.create_rect(space, 25) 

square = Square(310, 310, 150, 150, 5)
square.color = (100, 100, 100)
square_space = square.create_square(space, 25) 

shapes.append(rectangle)
shapes.append(square) 

running = True 

while running: 
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            running = False 
            pygame.quit()
            sys.exit()
    
    draw(shapes) 
    square.move()
    rectangle.rect_move() 
    space.step(1/60)
    pygame.display.update() 