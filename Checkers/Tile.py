import pygame

class Tile:
    def __init__(self, screen, pos, xy):
        self.pos = pos
        self.piece = None
        self.selected = False
        self.screen = screen
        self.xy = xy
        self.highlighted = []
        self.adjacents = [None, None, None, None]
        self.killable = []
        
        self.info = ""

    ### Create and add the tile image on the board 
    def draw(self):
        width = 600/8
        if self.selected: color = (186,202,68)
        else: color = (118,150,86)
        test = pygame.Surface((width, width))
        test.fill(color)

        size = 15
        font1 = pygame.font.SysFont('freesanbold.ttf', size)
        text1 = font1.render(str(self.pos), True, (0, 0, 0))
        textRect1 = text1.get_rect()
        textRect1.center = (width-size/2, width-size/2)
        test.blit(text1, textRect1)
        
        self.screen.blit(test,self.xy)




        
    def has_piece(self):
        return not self.piece == None
    
    
   
    def kill_if_possible(self, tile, Tiles):
        for t, k in self.killable:
            if tile.pos == t: Tiles[k].piece = None
            
    def move_piece_to(self,tile,Tiles):
        tile.piece = self.piece
        tile.piece.pos = tile.pos
        tile.piece.xy = tile.xy
        self.piece = None
        
        self.kill_if_possible(tile, Tiles)
        
    def can_kill(self, tile):
        return not self == None and not tile == None and self.has_piece() and tile.has_piece() and not self.piece.bw == tile.piece.bw




    def select_killable(self, tile, Tiles):    
        self.info = str(tile.pos)            
        for i in range(4):
            t = tile.adjacents[i];
            self.info +=  "    [" + str(i) + "]: " 
            if (not t == None) and t.has_piece() and tile.can_kill(t):
                t2 = t.adjacents[i];
                if t2 == None: self.info += "None"
                if (not t2 == None) and (not t2.has_piece()):
                    self.info += str(t2.pos)
                    t2.selected = True;
                    tile.highlighted.append(t2.pos)
                    tile.killable.append((t2.pos, t.pos))

    def select_moves(self,tile, Tiles):
        bw = tile.piece.bw
        for i in range(2):
            t = tile.adjacents[bw*2+i]
            if not t == None and not t.has_piece(): 
                t.selected = True
                tile.highlighted.append(t.pos)       
        self.info += " ... " + " KILLABLE" + str(self.killable)
                    
    def select_many(self, tile, Tiles):
        tile.selected = True
        self.select_killable(tile,Tiles)
        if len(tile.killable) == 0: self.select_moves(tile,Tiles)






    def deselect_many(self, tile, Tiles):
        if not tile == None:
            tile.selected=False
            for t in tile.highlighted:
                Tiles[t].selected = False
            tile.highlighted.clear()
            tile.killable.clear()


    #def smooth_move(self):
        









