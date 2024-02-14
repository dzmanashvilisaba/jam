import pygame

class Piece:
    
    def __init__(self, screen, xy, pos, bw):
        self.pos = pos
        self.bw = bw
        self.screen = screen
        self.xy = xy
        self.queen = False
        
        global width, col
        width = 600/8
        

        
    def draw(self):
        rad = width/2.5 
        if self.bw == 0: r,g,b = 30,30,30
        elif self.bw == 1: r,g,b = 225,225,225

        x = self.xy[0]+width/2
        y = self.xy[1]+width/2

        screen = self.screen
        circleTopShade = pygame.draw.circle(screen,(r-30,g-30,b-30),(x,y+4),rad, draw_bottom_left=True, draw_bottom_right=True)
        circleTop = pygame.draw.circle(screen,(r,g,b),(x,y),rad)
        circleBotShade = pygame.draw.circle(screen,(r-20,g-20,b-20),(x,y-3),rad*0.75,  draw_top_right=True, draw_top_left=True)
        circleBot = pygame.draw.circle(screen,(r+30,g+30,b+30),(x,y),rad*0.75)
    
    