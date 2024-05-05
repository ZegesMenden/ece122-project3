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

        def reset(self):
                for pix in self.pixels:
                        pix.delete()
                        del(pix)

                for i in range(self.cols):
                        for j in range(self.rows):
                                if self.pixarr[i, j] > 0:
                                        self.pixels.append(Pixel(self.canvas, i, j, self.rows, self.cols, self.scale, self.pixarr[i, j]))

        def random_pixels(self, npixels, color):
                if color > 0:
                        for i in range(npixels):
                                self.addij(np.random.randint(low=0, high=self.cols), np.random.randint(low=0, high=self.rows), color)

        def addij(self, i, j, color=1):
                if self.pixarr[i, j] <= 0:
                        self.pixels.append(Pixel(self.canvas, i, j, self.rows, self.cols, self.scale, color))
                        self.pixarr[i, j] = color
                        self.canvas.update() 

        def flush_row(self, i):
                purple_pixels = [
                        Pixel(self.canvas, 0, i, self.rows, self.cols, self.scale, 7, [0, 1]),
                        Pixel(self.canvas, 1, i, self.rows, self.cols, self.scale, 7, [0, 1]),
                        Pixel(self.canvas, 2, i, self.rows, self.cols, self.scale, 7, [0, 1]),
                        Pixel(self.canvas, self.cols-1, i, self.rows, self.cols, self.scale, 7, [0, -1]),
                        Pixel(self.canvas, self.cols-2, i, self.rows, self.cols, self.scale, 7, [0, -1]),
                        Pixel(self.canvas, self.cols-3, i, self.rows, self.cols, self.scale, 7, [0, -1])                        
                ]

                n_iters = int((self.cols-6)/2)
                self.canvas.update()

                for _ in range(n_iters):
                        for pix in purple_pixels:
                                pix.next()
                        self.canvas.update()
                        time.sleep(0.02)

                self.pixarr[:, 1:i+1] = self.pixarr[:, 0:i]
                self.pixarr[:,0] = 0

                for pix in purple_pixels:
                        pix.delete()

                self.reset()

        def delij(self, i, j):
                if self.pixarr[i, j] == 0:
                        print("flushing")
                        self.flush_row(j)
                        return
                
                for pix in self.pixels:
                        if pix.i == i and pix.j == j:
                                # what it seems like you should write for this function, but for some reason not what they want??
                                # for pix in self.pixels:
                                #         if pix.i == i and pix.j == j:
                                #                 self.pixels.remove(pix)
                                #                 pix.delete()
                                #                 self.pixarr[i, j] = 0 
                                #                 break

                                # what they want us to write, for some reason
                                self.pixarr[i, j] = 0
                                self.reset()             

        def addxy(self, x, y):
                i = int(x/self.scale)
                j = int(y/self.scale)
                print(f"insert {x} {y} {i} {j} {self.pixarr[i,j]}")
                self.addij(i, j)

        def delxy(self, x, y):
                print("delxy")
                i = int(x/self.scale)
                j = int(y/self.scale)
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

