from tkinter import *
from Pixel import Pixel
import numpy as np
import random, time


class Grid:
    


### To complete

        def __init__(self, root, rows, cols, scale):
                self.canvas = Canvas(root,width=cols*scale,height=rows*scale,bg="black")
                self.canvas.pack()
                self.rows = rows
                self.cols = cols
                self.scale = scale
                self.pixels = []
                self.pixarr = np.zeros((cols, rows), dtype=int)

        def random_pixels(self, npixels, color):
                for i in range(npixels):
                        self.addxy(np.random.randint(low=0, high=self.cols)*self.scale, np.random.randint(low=0, high=self.rows)*self.scale, color)

        def addxy(self, x, y, color=1):
                i = int(x/self.scale)
                j = int(y/self.scale)
                if self.pixarr[i, j] == 0:
                        self.pixels.append(Pixel(self.canvas, i, j, self.rows, self.cols, self.scale, color))
                        self.pixarr[i, j] = 1  
                        self.canvas.update() 

        def delxy(self, x, y):
                i = int(x/self.scale)
                j = int(y/self.scale)
                if self.pixarr[i, j] == 1:
                        for pix in self.pixels:
                                if pix.i == i and pix.j == j:
                                        self.pixels.remove(pix)
                                        pix.delete()
                                        self.pixarr[i, j] = 0 
                                        break
                          




#########################################################
############# Main code #################################
#########################################################

  
def main(): 
        
        ##### create a window, canvas 
        root = Tk()                # instantiate a tkinter window
        mesh = Grid(root,50,30,20) # instantiate a Grid object
        mesh.random_pixels(25,1) # generate 25 random (white) pixels in the Grid

        
        ####### Tkinter binding mouse actions
        root.bind("<Button-1>",lambda e:mesh.addxy(e.x,e.y))
        root.bind("<Button-3>",lambda e:mesh.delxy(e.x,e.y))
        

        root.mainloop() # wait until the window is closed
        

if __name__=="__main__":
    main()

