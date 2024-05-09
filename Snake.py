from tkinter import *
from Grid import Grid
from Pixel import Pixel
import time
import numpy as np

# written by: 
# cameron kullberg - 34231062
# spencer little 

### complete class Snake

import winsound

class Snake(Grid):
     
#########################################################
############# Main code #################################
#########################################################
    
    def __init__(self, root, n_obstacles, n_fruits, rows=25, cols=25, scale=20):
        """Snake - class representing snake game
        inputs - root: root of the window, n_obstacles: number of obstacles, n_fruits: number of fruits, rows: number of horizontal pixels, cols: number of vertical pixels, scale: size of each pixel
        outputs - none
        """
        super().__init__(root, rows, cols, scale)
        self.n_obstacles = n_obstacles
        self.n_fruits = n_fruits
        self.fruits_eaten = 0
        self.__game_over = False
        self.__pause = False

        snake_dir = [[1, 0], [-1, 0], [0, 1], [0, -1]][np.random.randint(0, 3)]

        self.snake_pixels = [
            Pixel(self.canvas, int(rows/2)-snake_dir[0]*3, int(cols/2)-snake_dir[1]*3, rows, cols, scale, 4, snake_dir),
            Pixel(self.canvas, int(rows/2)-snake_dir[0]*2, int(cols/2)-snake_dir[1]*2, rows, cols, scale, 4, snake_dir),
            Pixel(self.canvas, int(rows/2)-snake_dir[0]*1, int(cols/2)-snake_dir[1]*1, rows, cols, scale, 4, snake_dir),
            Pixel(self.canvas, int(rows/2)-snake_dir[0]*0, int(cols/2)-snake_dir[1]*0, rows, cols, scale, 5, snake_dir)            
        ]

        self.random_pixels(n_obstacles, 1)
        self.random_pixels(n_fruits, 3)

    def pause(self):
        """pause - pauses the game
        inputs - none
        outputs - none
        """
        self.__pause = not self.__pause

    def is_game_over(self):
        """is_game_over - returns true if the game is over
        inputs - none
        outputs - true if game is over
        """
        return self.__game_over

    def is_pause(self):
        """is_pause - returns true if the game is paused
        inputs - none
        outputs - true if game is paused
        """
        return self.__pause

    def up(self):
        """up - move snake up
        inputs - none
        outputs - none
        """
        if self.snake_pixels[-1].vector[0] == 0:
            self.pixarr[self.snake_pixels[-1].i, self.snake_pixels[-1].j] = -2
    
    def down(self):
        """down - move snake down
        inputs - none
        outputs - none
        """
        if self.snake_pixels[-1].vector[0] == 0:
            self.pixarr[self.snake_pixels[-1].i, self.snake_pixels[-1].j] = -4
    
    def left(self):
        """left - move snake left
        inputs - none
        outputs - none
        """
        if self.snake_pixels[-1].vector[1] == 0:
            self.pixarr[self.snake_pixels[-1].i, self.snake_pixels[-1].j] = -1
    
    def right(self):
        """right - move snake right
        inputs - none
        outputs - none
        """
        if self.snake_pixels[-1].vector[1] == 0:
            self.pixarr[self.snake_pixels[-1].i, self.snake_pixels[-1].j] = -3
    
    def next(self):
        """next - iterates the snake one step forward in the simulation
        inputs - none
        outputs - none
        """

        for pix in self.snake_pixels:

            if self.pixarr[pix.i, pix.j] == -1:
                pix.left()
            elif self.pixarr[pix.i, pix.j] == -2:
                pix.up()
            elif self.pixarr[pix.i, pix.j] == -3:
                pix.right()
            elif self.pixarr[pix.i, pix.j] == -4:
                pix.down()

        self.pixarr[self.snake_pixels[0].i, self.snake_pixels[0].j] = 0

        for pix in self.snake_pixels:
            pix.next()
            
        if self.pixarr[self.snake_pixels[-1].i, self.snake_pixels[-1].j] == 1:
            winsound.Beep(300, 500)
            self.__game_over = True
            self.canvas.create_text(int(self.cols*self.scale/2), int(self.rows*self.scale/2), fill='yellow', text="*** GAME OVER ***", font=('Times', 25))
        
        if self.pixarr[self.snake_pixels[-1].i, self.snake_pixels[-1].j] == 3:
            winsound.Beep(800, 100)
            self.fruits_eaten += 1
            self.n_fruits -= 1
            self.snake_pixels.insert(0, Pixel(self.canvas, self.snake_pixels[0].i-self.snake_pixels[0].vector[0], self.snake_pixels[0].j-self.snake_pixels[0].vector[1], self.rows, self.cols, self.scale, 4, self.snake_pixels[0].vector))
            self.delij(self.snake_pixels[-1].i, self.snake_pixels[-1].j)        

        if self.n_fruits == 0:
            winsound.Beep(800, 500)
            self.__game_over = True
            self.canvas.create_text(int(self.cols*self.scale/2), int(self.rows*self.scale/2), fill='yellow', text="*** You Won ***", font=('Times', 25))
  
def main(): 
        
        ##### create a window, canvas 
        root = Tk() # instantiate a tkinter window
        # python = Snake(root,20,20) #20 obstacles, and 20 fruits
        python = Snake(root,5,5,25,25,30) # 5 obstacles/fruits, 25 row, 25 column, 30 scale
        
        ####### Tkinter binding mouse actions
        root.bind("<Right>",lambda e:python.right())
        root.bind("<Left>",lambda e:python.left())
        root.bind("<Up>",lambda e:python.up())
        root.bind("<Down>",lambda e:python.down())
        root.bind("<p>",lambda e:python.pause())
       
        while True:
            if not python.is_pause(): python.next()
            root.update()
            time.sleep(0.15)  # wait few second (simulation)
            if python.is_game_over(): break
            
        
        root.mainloop() # wait until the window is closed
        

if __name__=="__main__":
    main()

