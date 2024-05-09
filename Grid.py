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
                self.pixarr = np.zeros((rows, cols), dtype=int)

                # create the vertical lines of the grid
                for i in range(self.cols - 1):
                        self.canvas.create_line((i+1)*self.scale, 0, (i+1)*self.scale, self.scale*self.rows, fill='white')
                
                # create the horizontal lines of the grid
                for j in range(self.rows - 1):
                        self.canvas.create_line(0, (j+1)*self.scale, self.scale*self.cols, (j+1)*self.scale, fill='white')

        def reset(self):

                # delete every pixel
                for pix in self.pixels:
                        pix.delete()
                        del(pix)

                # recreate the pixels
                for i in range(self.rows):
                        for j in range(self.cols):
                                if self.pixarr[i, j] > 0:
                                        self.pixels.append(Pixel(self.canvas, i, j, self.rows, self.cols, self.scale, self.pixarr[i, j]))

        def random_pixels(self, npixels, color):
                # dont do anything if the pixels are black
                if color == 0:
                        return

                for i in range(npixels):
                        self.addij(np.random.randint(low=0, high=self.rows), np.random.randint(low=0, high=self.cols), color)

        def addij(self, i, j, color=1):
                if self.pixarr[i, j] <= 0:
                        self.pixels.append(Pixel(self.canvas, i, j, self.rows, self.cols, self.scale, color))
                        self.pixarr[i, j] = color
                        self.canvas.update() 

        def flush_row(self, i):
                purple_pixels = [
                        Pixel(self.canvas, i, 0, self.rows, self.cols, self.scale, 7, [0, 1]),
                        Pixel(self.canvas, i, 1, self.rows, self.cols, self.scale, 7, [0, 1]),
                        Pixel(self.canvas, i, 2, self.rows, self.cols, self.scale, 7, [0, 1]),
                        Pixel(self.canvas, i, self.cols-1, self.rows, self.cols, self.scale, 7, [0, -1]),
                        Pixel(self.canvas, i, self.cols-2, self.rows, self.cols, self.scale, 7, [0, -1]),
                        Pixel(self.canvas, i, self.cols-3, self.rows, self.cols, self.scale, 7, [0, -1])                        
                ]

                n_iters = int((self.cols-6)/2)
                self.canvas.update()

                for _ in range(n_iters):
                        for pix in purple_pixels:
                                pix.next()
                        self.canvas.update()
                        time.sleep(0.02)

                self.pixarr[1:i+1] = self.pixarr[0:i]
                self.pixarr[0,:] = 0

                for pix in purple_pixels:
                        pix.delete()

                self.reset()

        def delij(self, i, j):
                if self.pixarr[i, j] == 0:
                        print("flushing")
                        self.flush_row(i)
                        return
                
                for pix in self.pixels:
                        if pix.i == i and pix.j == j:
                                self.pixarr[i, j] = 0
                                self.reset()             

        def addxy(self, x, y):
                j = int(x/self.scale)
                i = int(y/self.scale)
                print(f"insert {x} {y} {i} {j} {self.pixarr[i,j]}")
                self.addij(i, j)

        def delxy(self, x, y):
                j = int(x/self.scale)
                i = int(y/self.scale)
                print(f"delete {x} {y} {i} {j} {self.pixarr[i,j]}")
                self.delij(i, j)




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

