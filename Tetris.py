from tkinter import *
from Grid import Grid
from Tetrominoes import Tetrominoes
import numpy as np
import time

# written by: 
# cameron kullberg - 34231062
# spencer little 
        
### complete class Tetris


#########################################################
############# Main code #################################
#########################################################
    

class Tetris(Grid):
     
    def __init__(self, canvas, rows, cols, scale):
        """name - 
        inputs - 
        outputs - 
        """
        super().__init__(canvas, rows, cols, scale)
        self.block = None
        self.__gameover = False
        self.__paused = False
        self.block = None
        self.next_is_running = False
    
    def overlapping(self, ii, jj):
        """overlapping - returns true if the current block is overlapping the given coordinate
        inputs - i and j coordinates to test
        outputs - true if there is an overlap
        """

        # check every pixel by iterating through
        for x in range(self.block.w):
            for y in range(self.block.h):
                # if there are pixels in both arrays at this position, then they must be overlapping
                if bool(self.block.get_pattern()[y, x]) and bool(self.pixarr[min(ii+y, self.rows-1), min(jj+x, self.cols-1)]):
                    return True
        
        # if none of the pixels in the loop overlapped, then there was no overlap
        return False

    def next(self):
        """next - iterate the game one step forward in the simulation
        inputs - none
        outputs - none
        """

        self.next_is_running = True

        # instantiate a new block if the old one was deleted         
        if self.block is None:
            self.block = Tetrominoes.random_select(self.canvas, self.rows, self.cols, self.scale)
            self.block.activate()

        # move block down
        self.block.down()

        # check if the block is at the ground level, only if there are pixels on the bottom row (only applies to line piece)
        collision_with_ground = self.block.i > (self.rows - (self.block.h+1) + (np.count_nonzero(self.block.get_pattern()[2,:]) == 0))

        if collision_with_ground or self.overlapping(self.block.i+1, self.block.j):

            # add block to pixel array
            for x in range(self.block.w):
                for y in range(self.block.h):
                    if self.block.get_pattern()[y,x]:
                        self.addij(self.block.i+y, self.block.j+x, self.block.color)

            # iterate over every row the block is touching when it breaks, and check if the row needs to be cleared
            for ii in range(self.block.i, self.block.i + 3):
                if np.count_nonzero(self.pixarr[ii,:]) == self.cols:
                    self.flush_row(ii)

            # check the top two rows for game over
            for ii in range(0, 2):
                if np.count_nonzero(self.pixarr[ii,:]):
                    self.__gameover = True
                    self.canvas.create_text(int(self.cols*self.scale/2), int(self.rows*self.scale/2), fill='yellow', text="*** GAME OVER ***", font=('Times', 25))
            
            # delete the block
            self.block.delete()
            self.block = None
        
        self.next_is_running = False

    def is_game_over(self):
        """is_game_over - check if game is over
        inputs - none
        outputs - true if game is over
        """
        return self.__gameover

    def is_pause(self):
        """is_pause - check if game is paused
        inputs - none
        outputs - true if game is paused
        """
        return self.__paused

    def pause(self):
        """pause - pauses the game
        inputs - none
        outputs - none
        """
        print("pause")
        self.__paused = not self.__paused

    def up(self):
        """up - rotates the current block
        inputs - none
        outputs - none
        """

        if self.next_is_running:
            return

        # rotate forward, then check for a collision
        self.block.rotate()

        # check if the block is at the ground level, only if there are pixels on the bottom row (only applies to line piece)
        collision_with_ground = self.block.i > (self.rows - (self.block.h+1) + (np.count_nonzero(self.block.get_pattern()[2,:]) == 0))

        pixels_overflow = (self.block.j + (np.count_nonzero(self.block.get_pattern()[:,0]) == 0)) < 0 or (self.block.j - (np.count_nonzero(self.block.get_pattern()[:,2]) == 0)) > self.cols-3

        if self.overlapping(self.block.i, self.block.j) or collision_with_ground or pixels_overflow:
            self.block.pattern_idx = (self.block.pattern_idx + (self.block.nbpattern-1)) % self.block.nbpattern
            self.block.clear_pixels()
            self.block.activate(self.block.i, self.block.j)

    def right(self):
        """right - moves the current block right
        inputs - none
        outputs - none
        """

        if self.next_is_running:
            return

        # check if the block is at the ground level, only if there are pixels on the bottom row (only applies to line piece)
        collision_with_ground = self.block.i > (self.rows - (self.block.h+1) + (np.count_nonzero(self.block.get_pattern()[2,:]) == 0))

        if (self.block.j - (np.count_nonzero(self.block.get_pattern()[:,2]) == 0)) < self.cols-self.block.w and not self.overlapping(self.block.i, self.block.j+1) and not collision_with_ground:
            self.block.right()
    
    def left(self):
        """left - moves the current block left
        inputs - none
        outputs - none
        """    
        
        if self.next_is_running:
            return
        # check if the block is at the ground level, only if there are pixels on the bottom row (only applies to line piece)
        collision_with_ground = self.block.i > (self.rows - (self.block.h+1) + (np.count_nonzero(self.block.get_pattern()[2,:]) == 0))

        if (self.block.j + (np.count_nonzero(self.block.get_pattern()[:,0]) == 0)) > 0 and not self.overlapping(self.block.i, self.block.j-1) and not collision_with_ground:
            self.block.left()

    def down(self):
        """down - moves the current block to the lowest possible position
        inputs - none
        outputs - none
        """

        # check to see if the "next" function is currently being run in the main loop of the program so that we don't accidentally delete the block
        # object in the middle of executing code that references it
        if self.next_is_running:
            return

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

