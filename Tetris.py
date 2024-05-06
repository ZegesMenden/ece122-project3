from tkinter import *
from Grid import Grid
from Tetrominoes import Tetrominoes
import numpy as np
import time

        
### complete class Tetris


#########################################################
############# Main code #################################
#########################################################
    

class Tetris(Grid):
     
    def __init__(self, canvas, rows, cols, scale):
        super().__init__(canvas, rows, cols, scale)
        self.block = None
        self.__gameover = False
        self.__paused = False
        self.block = None
    
    def overlapping(self, ii, jj):
        collision_mat = self.block.get_pattern() * self.pixarr[ii:ii+3,jj:jj+3]
        any_colision = np.count_nonzero(collision_mat)
        if any_colision:
            return True
        return False

    def next(self):
         
        if self.block is None:
            self.block = Tetrominoes.random_select(self.canvas, self.rows, self.cols, self.scale)
            self.block.activate()
                    
        self.block.down()

        if self.block.i >= (self.rows - (self.block.h*2)) or self.overlapping(self.block.i+1, self.block.j):
            for x in range(self.block.w):
                for y in range(self.block.h):
                    if self.block.get_pattern()[y,x]:
                        self.addij(self.block.i+y, self.block.j+x, self.block.color)

            for ii in range(self.block.i, self.block.i + 2):
                print(np.count_nonzero(self.pixarr[ii,:]))
                if np.count_nonzero(self.pixarr[ii,:]) == self.cols:
                    self.flush_row(ii)

            for ii in range(0, 2):
                if np.count_nonzero(self.pixarr[ii,:]):
                    self.__gameover = True
                    
            self.block.delete()
            self.block = None

    def is_game_over(self):
        return self.__gameover

    def is_pause(self):
        return self.__paused

    def pause(self):
        self.__paused = not self.__paused

    def up(self):
        self.block.rotate()
    
    def right(self):
        if self.block.j < self.cols-self.block.w:
            self.block.right()
    
    def left(self):
        if self.block.j > 0:
            self.block.left()

    def down(self):
        while self.block is not None:
            self.next()
            

def main():
    ##### create a window, canvas 
        root = Tk() # instantiate a tkinter window
        game=Tetris(root,36,12,25) 
        
        ####### Tkinter binding mouse actions
        root.bind("<Up>",lambda e:game.up())
        root.bind("<Left>",lambda e:game.left())
        root.bind("<Right>",lambda e:game.right())
        root.bind("<Down>",lambda e:game.down())
        root.bind("<p>",lambda e:game.pause())        

        while True:
            if not game.is_pause(): game.next()
            root.update()   # update the graphic
            time.sleep(0.25)  # wait few second (simulation)
            if game.is_game_over(): break
        
        root.mainloop() # wait until the window is closed


        

if __name__=="__main__":
    main()

