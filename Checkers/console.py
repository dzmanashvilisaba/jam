import pygame

class Console:
    def __init__(self, screen, width, height, xy):
        self.screen = screen
        self.w = width
        self.h = height
        self.xy = xy
        self.size = 20
        
        self.sep = pygame.font.SysFont("couriernew.ttf", self.size).get_height()  
        self.commands = []
        
    def write_commands(self):
        for c, xy in self.commands:
            self.screen.blit(c,xy)

    def shift_commands_down(self):
        if len(self.commands) != 0:
            for i in range(len(self.commands)):
                t, xy = self.commands[i]
                xy = (xy[0],xy[1]+self.sep)
                self.commands[i] = (t,xy)
        
    def exec(self, s):  
        xy = (self.xy[0]+10,self.xy[1]+10)

        text = pygame.font.SysFont("couriernew.ttf", self.size)
        t = text.render(s, True, (0,0,0))
        self.shift_commands_down()
        self.commands.insert(0, (t, xy) )
        

    def draw_console(self):    
        console = pygame.Surface((self.w, self.h))
        console.fill((255,255,255))
        
        self.screen.blit(console,self.xy)

        self.write_commands()