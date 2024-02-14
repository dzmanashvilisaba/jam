import pygame
import random
import numpy as np
from Engine import Engine
from Tile import Tile
from Piece import Piece
from console import Console

####################################################
###   INIT VARIABLES, ARRAYS AND CONSTANTS       ###
FPS = 60
WIDTH = 600  
HEIGHT = 600  
x_offset,y_offset = 0,0
bg_color = (238,238,210)
dark_color = (118,150,86)
selected_color = (105,25,0)

###   Initialize graphics and background   
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
screen.fill(bg_color)
sq_len = WIDTH/8

###     INITIALIZE CONSOLE
c = Console(screen, WIDTH, HEIGHT-WIDTH, (0,HEIGHT+y_offset))
e = Engine()

###   Initialize arrays   
Coordinates = []
Position = []
Tiles = []
############################################################
############################################################


#############################################
###      INIT COORDINATES AND POSITION    ###  
def get_xy(n: int):
    row = int(n/4)
    temp = int(n%8)
    col = int((temp*2 + temp/4)%8)
    # temp=0 ==> col=0
    # temp=1 ==> col=2
    # temp=2 ==> col=4
    # temp=3 ==> col=6
    # temp=4 ==> col=1
    # temp=5 ==> col=3
    # temp=6 ==> col=5
    # temp=7 ==> col=7
    y = HEIGHT - (row+1)*sq_len
    x = col*sq_len
    return(x+x_offset,y+y_offset)

### Get position in [0:31] from given tuple of (y,x) coordinates
def get_pos(yx):
    row = 7-int(yx[1]/sq_len)
    col = int(yx[0]/sq_len)
    if row%2 != col%2: return 
    return 4*row + int(col/2)
    
###     Generate Coordinates list      
def init_coords():
    result = []
    for i in range(32):
        result.append(get_xy(i))
    return result
Coordinates = init_coords() 

### Initializez starting position ###
def init_pos():
    res = []
    for i in range(12):
        res.append( i*10 )
    for i in range(20,32):
        res.append( i*10+1 )
    return res
Position = init_pos()


### Initialize Random Position ###
def make_pos(a,b):
    temp1, temp2 = [],[]
    for var in a:
        temp1.append(var*10)
    for var in b:
        temp2.append(var*10+1)
    return temp1 + temp2

def gen_pos():
    blacks, whites = [],[]
    for i in range(12):
        s = random.randrange(0,31)
        if s not in blacks+whites: blacks.append(s)
        s = random.randrange(0,31)
        if s not in blacks+whites: whites.append(s)
    return make_pos(blacks,whites)
# Position = gen_pos()
print(Position)
#########################################################
#########################################################



###########################################
###         INIT TILES AND PIECES       ###
def init_Tiles():
    tiles = []
    for i in range(32):
        tiles.append(Tile(screen, i, Coordinates[i]))
    ### Add impossible neigbhors
    for i in range(32):
        if i==0: tiles[i].adjacents[1] = tiles[i+4]
        elif i==31: tiles[i].adjacents[3] = tiles[i-4]
        elif i<4: 
            tiles[i].adjacents[0]=tiles[i+3]
            tiles[i].adjacents[1]=tiles[i+4]
        elif i%8==0:
            tiles[i].adjacents[1]=tiles[i+4]
            tiles[i].adjacents[2]=tiles[i-4]
        elif i%8==7:
            tiles[i].adjacents[0]=tiles[i+4]
            tiles[i].adjacents[3]=tiles[i-4]
        elif i>27: 
            tiles[i].adjacents[2] = tiles[i-3]
            tiles[i].adjacents[3] = tiles[i-4]
        elif int((i/4))%2==0:
            tiles[i].adjacents = (tiles[i+3],tiles[i+4],tiles[i-4],tiles[i-5])
        elif int((i/4))%2==1:   
            tiles[i].adjacents = (tiles[i+4],tiles[i+5],tiles[i-3],tiles[i-4])
    return tiles
Tiles = init_Tiles()

def init_Pieces():
    pieces = []
    for p in Position:
        pos = int(p/10)
        piece = Piece(screen, Coordinates[pos], pos, int(p%10))
        pieces.append(piece)
        Tiles[pos].piece = piece
    return pieces
Pieces = init_Pieces()



def draw_Pieces():
    for p in Pieces:
        p.draw()
################################################################
################################################################

def draw_board():
    for t in Tiles:
        t.draw()
        if t.has_piece(): t.piece.draw()


def main():
    ###################################
    ###             GAME            ###
    ###################################
    game_active = True
    last = None
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_active = False
                break
            elif event.type == pygame.MOUSEBUTTONDOWN:
                ### After mouse is clicked, check, whether position is selectable
                p = get_pos(pygame.mouse.get_pos())
                if p != None: 
                    temp = Tiles[p]
                    ### Clicked again on the same piece
                    if temp.selected and temp.has_piece(): temp.deselect_many(temp, Tiles)
                    ### Moving the piece and kill
                    elif temp.selected and not temp.has_piece(): 
                        if not last == None: last.move_piece_to(temp, Tiles)
                        temp.deselect_many(last, Tiles)
                        
                        e.current_player = (e.current_player + 1)%2
                        e.print_board(Tiles)
                    ### Selecting other piece
                    elif temp.has_piece() and e.is_proper_turn(temp.piece.bw): 
                        temp.deselect_many(last, Tiles)
                        temp.select_many(temp, Tiles)
                        last = temp

                    #c.exec(temp.info)
                    c.exec(e.info)
                    
        if not game_active:
            break
            
        draw_board()
        c.draw_console()


     


        pygame.display.update()
        pygame.display.set_caption("Game Demo [{} fps]".format(int(clock.get_fps())))

        clock.tick(FPS)
        
        
        
main()        
        
        
    
    
    
    