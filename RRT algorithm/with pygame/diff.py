import pygame
import math

class Envir:
    def __init__(self,dimensions):
        self.grey = (70, 70, 70)
        self.Blue = (0, 0, 255)
        self.Green = (0, 255, 0)
        self.Red = (255, 0, 0)
        self.white = (255, 255, 255)
        self.black = (0,0,0)
        self.yel = (255,255,0)

        self.height = dimensions[0]
        self.width = dimensions[1]

        pygame.display.set_caption("Differential drive robot")
        self.map= pygame.display.set_mode((self.width,self.height))



class Robot:
    def __init__(self,startpos,robotImg, width):
        self.m2p = 3779.52
        self.w= width
        self.x= startpos[0]
        self.y= startpos[1]
        self.theta=0
        self.u = 0.01*self.m2p  #m/s
        self.a=0.01*self.m2p
        self.maxspeed = 0.02*self.m2p
        self.minspeed = 0.02*self.m2p

        self.img =pygame.image.load(robotImg)
        self.rotated= self.img
        self.rect= self.rotated.get_rect(center=(self.x,self.y))

    def draw(self,map):
        map.blit(self.rotated,self.rect)

    def move(self,dt ,event= None):
    
        self.x+=(self.u*math.cos(self.theta) - self.a*math.sin(self.theta)*self.w)*dt
        self.y-=(self.u*math.sin(self.theta) + self.a*math.cos(self.theta)*self.w)*dt
        self.theta+= self.w*dt

        self.rotated = pygame.transform.rotozoom(self.img,math.degrees(-self.theta),1)
        self.rect = self.rotated.get_rect(center=(self.x,self.y))
        self.follow_path()

    def follow_path(self):
        target = self.path[self.waypoint]
        delta_x = target[0] - self.x
        delta_y = target[1] - self.y
        self.u = delta_x * math.sin(self.theta) + delta_y * math.sin(self.theta)
        self.w= (-1/self.a) * math.sin(self.theta) *delta_x + (1/self.a) * math.cos(self.theta)*delta_y
        if self.dist((self.x,self.y).self.path[self.waypoint]) <=35:
            self.waypoint -=1
        if self.waypoint <=0:
            self.waypoint=0

        


pygame.init()

start = (200,200)
dim= (800,1200)
running =True
environment = Envir(dim)

robot= Robot(start, r"C:\Users\Admin\OneDrive\Desktop\python-visualization-of-the-RRT-algorithm-with-pygame-main\vehicle.png",0.01*3779.52)


dt=0
lasttime = pygame.time.get_ticks()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running =False
        robot.move(event)
    
    dt= (pygame.time.get_ticks()- lasttime)/1000
    lasttime = pygame.time.get_ticks()
    pygame.display.update()
    environment.map.fill(environment.black)
    robot.draw(environment.black)
    environment.write_info(int(robot.u),int(robot.a),robot.theta)
        