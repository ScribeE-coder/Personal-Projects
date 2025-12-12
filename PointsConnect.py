import pygame 

pygame.init()

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600 

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

class Point: 
    def __init__(self, x, y): 
        self.x = x 
        self.y = y 
        self.color = (0, 0, 0)
        self.radius = 10 

    def plot(self): 
        point = pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)
        return point
    
    def get_pos(self): 
        return (self.x, self.y) 

 # take all points made and draw a line connecting all of them  
def connect(points: list, color=(0, 0, 0), thickness=2): 
    for i in range(len(points) - 1): 
        start_point = points[i]
        end_point = points[i+1] 
        start_pos = start_point.get_pos()
        end_pos = end_point.get_pos()
        pygame.draw.line(screen, color, start_pos, end_pos, thickness)
        
        first_point = points[0].get_pos()
        last_point = points[-1].get_pos()
        pygame.draw.line(screen, color, first_point, last_point, thickness) 

points = []       

point1 = Point(300, 300)
point2 = Point(100, 100)
point3 = Point(100, 500)
point4 = Point(100, 400) 
point5 = Point(500, 500)

points.append(point1) 
points.append(point2)
points.append(point3) 
points.append(point4) 
points.append(point5) 

running = True 
while running: 
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            running = False 
    
    screen.fill((217, 217, 217))
    for point in points: 
        point.plot()
    connect(points)
    pygame.display.update()