from tkinter import *
from Pixel import Pixel
import time, random
import numpy as np



class Tetrominoes:

    ## to complete


    def __init__(self, canvas, rows, cols, scale, color = 2, patterns = [np.array([[2, 2, 2],[2, 0, 2],[2, 2, 2]])]):

        self.canavs = canvas
        self.rows = rows
        self.cols = cols
        self.scale = scale
        self.color = color
        self.patterns = patterns
        self.pattern_idx = 0
        self.nbpattern = len(patterns)
        self.w, self.h = patterns[self.pattern_idx].shape
        self.name = "Basic"

        self.i = 0
        self.j = 0
    
        self.pixels = []

    def activate(self, i = 0, j = None):
        if j is None:
            j = np.random.randint(0, self.cols - self.w)

        self.i = i
        self.j = j

        self.clear_pixels()

        for x in range(self.w):
            for y in range(self.h):
                if self.patterns[self.pattern_idx][x, y] > 0:
                    self.pixels.append(
                        Pixel(self.canavs, self.i + x, self.j + y, self.rows, self.cols, self.scale, self.color)
                    )

    def get_pattern(self):
        return np.copy(self.patterns[self.pattern_idx])
        
    def clear_pixels(self):
        for pix in self.pixels:
            pix.delete()
            del(pix)

    def rotate(self):
        self.pattern_idx = (self.pattern_idx + 1) % self.nbpattern
        self.clear_pixels()
        self.activate(self.i, self.j)

    def delete(self):
        self.clear_pixels()

    def up(self):
        self.i = (self.i - 1) % self.rows
        
        for pix in self.pixels:
            pix.up()
            pix.next()
    
    def down(self):
        self.i = (self.i + 1) % self.rows
        
        for pix in self.pixels:
            pix.down()
            pix.next()
    
    def left(self):
        self.j -= 1
        # self.j = (self.j - 1) % self.cols
        
        for pix in self.pixels:
            pix.left()
            pix.next()
    
    def right(self):
        self.j = (self.j + 1) % self.cols
        
        for pix in self.pixels:
            pix.right()
            pix.next()

    @staticmethod
    def random_select(canv,nrow,ncol,scale):
        t1=TShape(canv,nrow,ncol,scale)
        t2=TripodA(canv,nrow,ncol,scale)
        t3=TripodB(canv,nrow,ncol,scale)
        t4=SnakeA(canv,nrow,ncol,scale)
        t5=SnakeB(canv,nrow,ncol,scale)
        t6=Cube(canv,nrow,ncol,scale)
        t7=Pencil(canv,nrow,ncol,scale)        
        return random.choice([t1,t2,t3,t4,t5,t6,t7,t7]) #a bit more change to obtain a pencil shape
        
#########################################################
############# All Child Classes #########################
#########################################################

class TShape(Tetrominoes):
    def __init__(self, canvas, rows, cols, scale):
        super().__init__(canvas, rows, cols, scale, 3, [np.array([[0, 1, 0],
                                                        [0, 1, 0,],
                                                        [1, 1, 1]]),
                                                        np.array([[0, 0, 1,],
                                                        [1, 1, 1,],
                                                        [0, 0, 1,]]),
                                                        np.array([[1, 1, 1,],
                                                        [0, 1, 0,],
                                                        [0, 1, 0,]]),
                                                        np.array([[1, 0, 0,],
                                                        [1, 1, 1,],
                                                        [1, 0, 0,]])])
        self.name="TShape"

class TripodA(Tetrominoes):
    def __init__(self, canvas, rows, cols, scale):
        super().__init__(canvas, rows, cols, scale, 4, [np.array([[0, 1, 0],
                                                        [0, 1, 0],
                                                        [1, 0, 1]]),
                                                        np.array([[0, 0, 1],
                                                        [1, 1, 0],
                                                        [0, 0, 1]]),
                                                        np.array([[1, 0, 1],
                                                        [0, 1, 0],
                                                        [0, 1, 0]]),
                                                        np.array([[1, 0, 0],
                                                        [0, 1, 1],
                                                        [1, 0, 0]])])
        self.name="TripodA"


class TripodB(Tetrominoes):
    def __init__(self, canvas, rows, cols, scale):
            super().__init__(canvas, rows, cols, scale, 5, [np.array([[0, 1, 0],
                                                            [1, 0, 1],
                                                            [1, 0, 1]]),
                                                            np.array([[0, 1, 1],
                                                            [1, 0, 0],
                                                            [0, 1, 1]]),
                                                            np.array([[1, 0, 1],
                                                            [1, 0, 1],
                                                            [0, 1, 0]]),
                                                            np.array([[1, 1, 0],
                                                            [0, 0, 1],
                                                            [1, 1, 0]])])
            self.name="TripodB"

class SnakeA(Tetrominoes):
    def __init__(self, canvas, rows, cols, scale):
            super().__init__(canvas, rows, cols, scale, 6, [np.array([[1, 1, 0],
                                                            [0, 1, 0],
                                                            [0, 1, 1]]),
                                                            np.array([[0, 0, 1],
                                                            [1, 1, 1],
                                                            [1, 0, 0]])])
            self.name="SnakeA"

class SnakeB(Tetrominoes):
    def __init__(self, canvas, rows, cols, scale):
            super().__init__(canvas, rows, cols, scale, 7, [np.array([[0, 1, 1],
                                                            [0, 1, 0],
                                                            [1, 1, 0]]),
                                                            np.array([[1, 0, 0],
                                                            [1, 1, 1],
                                                            [0, 0, 1]])])
            self.name="SnakeB"

class Cube(Tetrominoes):
    def __init__(self, canvas, rows, cols, scale):
            super().__init__(canvas, rows, cols, scale, 8, [np.array([[1, 1, 1],
                                                            [1, 1, 1],
                                                            [1, 1, 1]]),
                                                            np.array([[1, 1, 1],
                                                            [1, 1, 1],
                                                            [1, 1, 1]]),
                                                            np.array([[1, 1, 1],
                                                            [1, 1, 1],
                                                            [1, 1, 1]])])
            self.name="Cube"

class Pencil(Tetrominoes):
    def __init__(self, canvas, rows, cols, scale):
            super().__init__(canvas, rows, cols, scale, 9, [np.array([[0, 1, 0],
                                                            [0, 1, 0],
                                                            [0, 1, 0]]),
                                                            np.array([[0, 0, 0],
                                                            [1, 1, 1],
                                                            [0, 0, 0]])])
            self.name="Pencil"

#########################################################
############# Testing Functions #########################
#########################################################
def delete_all(canvas):
    canvas.delete("all")
    print("Delete All")


def test1(canvas,nrow,ncol,scale):
    print("Generate a Tetromino (basic shape)- different options")
    
    tetro1=Tetrominoes(canvas,nrow,ncol,scale) # instantiate
    print("Tetro1",tetro1.name)
    print("  number of patterns:",tetro1.nbpattern)
    print("  current pattern:\n",tetro1.get_pattern()) # retrieve current pattern
    print("  height/width:",tetro1.h,tetro1.w)
    tetro1.activate(nrow//2,ncol//2)        # activate and put in the middle
    print("  i/j coords:  ",tetro1.i,tetro1.j)

    pattern=np.array([[0,3,0],[3,3,3],[0,3,0],[3,0,3],[3,0,3]]) # matrix motif
    tetro2=Tetrominoes(canvas,nrow,ncol,scale,3,[pattern]) # instantiate (list of patterns-- 1 item here)
    print("\nTetro2",tetro2.name)
    print("  number of patterns:",tetro2.nbpattern)
    print("  current pattern:\n",tetro2.get_pattern()) # retrieve current pattern
    print("  height/width:",tetro2.h,tetro2.w)
    tetro2.activate()        # activate and place at random at the top
    print("  i/j coords:  ",tetro2.i,tetro2.j)

    
    
def test2(root,canvas,nrow,ncol,scale):
    print("Generate a 'square' Tetromino (with double shape) and rotate")
    
    print("My Tetro")
    pattern1=np.array([[4,0,0],[0,4,0],[0,0,4]]) # matrix motif
    pattern2=np.array([[0,0,4],[0,4,0],[4,0,0]]) # matrix motif
    tetro=Tetrominoes(canvas,nrow,ncol,scale,4,[pattern1,pattern2]) # instantiate (list of patterns-- 2 items here)
    print("  number of patterns:",tetro.nbpattern)
    print("  height/width:",tetro.h,tetro.w)
    tetro.activate(nrow//2,ncol//2)        # activate and place in the middle
    print("  i/j coords:  ",tetro.i,tetro.j)

    for k in range(10): # make 10 rotations
        tetro.rotate() # rotate (change pattern)
        print("  current pattern:\n",tetro.get_pattern()) # retrieve current pattern
        root.update()
        time.sleep(0.5)
    tetro.delete() # delete tetro (delete every pixels)


def rotate_all(tetros): #auxiliary routine
    for t in tetros:
        t.rotate()
    
       
def test3(root,canvas,nrow,ncol,scale):
    print("Dancing Tetrominoes")

    t0=Tetrominoes(canvas,nrow,ncol,scale)
    t1=TShape(canvas,nrow,ncol,scale)
    t2=TripodA(canvas,nrow,ncol,scale)
    t3=TripodB(canvas,nrow,ncol,scale)
    t4=SnakeA(canvas,nrow,ncol,scale)
    t5=SnakeB(canvas,nrow,ncol,scale)
    t6=Cube(canvas,nrow,ncol,scale)
    t7=Pencil(canvas,nrow,ncol,scale)
    tetros=[t0,t1,t2,t3,t4,t5,t6,t7]

    for t in tetros:
        print(t.name)

    # place the tetrominos
    for i in range(4):
        for j in range(2):
            k=i*2+j
            tetros[k].activate(5+i*10,8+j*10)
            
    ####### Tkinter binding for this test
    root.bind("<space>",lambda e:rotate_all(tetros))     

    
      
def test4(root,canvas,nrow,ncol,scale):
    print("Moving Tetromino")
    tetro=Tetrominoes.random_select(canvas,nrow,ncol,scale) # choose at random
    print(tetro.name)
        
    ####### Tkinter binding for this test
    root.bind("<space>",lambda e:tetro.rotate())
    root.bind("<Up>",lambda e:tetro.up())
    root.bind("<Down>",lambda e:tetro.down())
    root.bind("<Left>",lambda e:tetro.left())
    root.bind("<Right>",lambda e:tetro.right())

    tetro.activate()

    

#########################################################
############# Main code #################################
#########################################################

def main():
    
        ##### create a window, canvas 
        root = Tk() # instantiate a tkinter window
        nrow=45
        ncol=30
        scale=20
        canvas = Canvas(root,width=ncol*scale,height=nrow*scale,bg="black") # create a canvas width*height
        canvas.pack()

        ### general binding events to choose a testing function
        root.bind("1",lambda e:test1(canvas,nrow,ncol,scale))
        root.bind("2",lambda e:test2(root,canvas,nrow,ncol,scale))
        root.bind("3",lambda e:test3(root,canvas,nrow,ncol,scale))
        root.bind("4",lambda e:test4(root,canvas,nrow,ncol,scale))
        root.bind("<d>",lambda e:delete_all(canvas))

        
        root.mainloop() # wait until the window is closed        

if __name__=="__main__":
    main()

