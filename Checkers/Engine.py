import matplotlib.pyplot as plt
import numpy as np

class Node:
    def __init__(self, elem):
        self.elem = elem
        self.value = 0 
        self.neighbors = []

        
class Engine:
    def __init__(self):
        self.position = None
        self.current_player = 0
        self.info = ""
    
    def is_proper_turn(self, bw):
        return self.current_player == bw

    def print_board(self,Tiles):
        temp_blacks = []
        temp_whites = []
        for t in Tiles:
            if t.has_piece(): 
                if t.piece.bw == 0: temp_blacks.append(t.pos)
                if t.piece.bw == 1: temp_whites.append(t.pos)
        
        blacks, whites = [], []
        for e in temp_whites:
            row = int(e/4)
            col = 2*(e%4)+(row)%2
            whites.append([row, col])
        for e in temp_blacks:
            row = int(e/4)
            col = 2*(e%4)+(row)%2
            blacks.append([row, col])
        
        for i in range(8):
            print("| ", end = "")
            for j in range(8):
                if [7-i,j] in blacks: print("T|", end = "")
                elif [7-i,j] in whites: print("X|", end = "")
                else: print("  |",end = "")
            print("")
        print("_____________________")
        print()
        
    #def next_possible_boards(self, Tiles):
    #    res = []
    #    for t in Tiles:
    #        if t.bw == self.current_player:
                
            