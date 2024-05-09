from tkinter import *
import time
import random

# written by: 
# cameron kullberg - 34231062
# spencer little 

class Pixel:
    color=['black','white','yellow','red','blue','green','orange','purple','brown','cyan']
    
    ### to complete       

    def __init__(self, canvas, i, j, rows, cols, size, color_px, vector=[0,0]):
        """Pixel - instantiate pixel class
        inputs - canvas: canvas object, i: i coordinate, j: j coordinate, rows: number of rows, cols: number of cols, size: size of pixel, color_px, color of pixel, vector: pixel direction vector
        outputs - none
        """
        self.canvas = canvas
        self.i = i % rows
        self.j = j % cols
        self.rows = rows
        self.cols = cols
        self.size = size
        self.color = color_px
        self.vector = vector
        self.canvas_obj = self.canvas.create_rectangle(self.j*self.size, self.i*self.size, self.j*self.size+self.size, self.i*self.size+self.size, fill=Pixel.color[self.color])

    def __str__(self):
        """__str__ - returns string representation of the pixel
        inputs - none
        outputs - string representation
        """
        return f"[{self.i}, {self.j}] {Pixel.color[self.color]}"

    def next(self):
        """next - iterates the pixel one step forward
        inputs - none
        outputs - none
        """
        self.i = (self.i + self.vector[0]) % self.rows
        self.j = (self.j + self.vector[1]) % self.cols
        self.canvas.coords(self.canvas_obj, self.j*self.size, self.i*self.size, self.j*self.size+self.size, self.i*self.size+self.size)

    def up(self):
        """up - sets the pixels direction to up
        inputs - none
        outputs - none
        """
        self.vector = [-1, 0]
    
    def down(self):
        """down - sets the pixels direction to down
        inputs - none
        outputs - none
        """
        self.vector = [1, 0]
    
    def left(self):
        """left - sets the pixels direction to left
        inputs - none
        outputs - none
        """
        self.vector = [0, -1]
    
    def right(self):
        """right - sets the pixels direction to right
        inputs - none
        outputs - none
        """
        self.vector = [0, 1]

    def delete(self):
        """delete - deletes pixel from the display
        inputs - none
        outputs - none
        """
        self.canvas.delete(self.canvas_obj)

        
#################################################################
########## TESTING FUNCTION
#################################################################
def delete_all(canvas):
    canvas.delete("all")
    print("Delete All")


def test1(canvas,nrow,ncol,scale):
    print("Generate 10 points at random")
    random.seed(4) # for reproducibility
    for k in range(10):
        i=random.randint(0,nrow-1) 
        j=random.randint(0,ncol-1)
        c=random.randint(1,9)    # color number
        pix=Pixel(canvas,i,j,nrow,ncol,scale,c)
        print(pix)

def test2(canvas,nrow,ncol,scale):
    print("Generate 10 points at random (using modulo)")
    random.seed(5) # for reproducibility
    for k in range(10):
        i=random.randint(0,nrow-1)*34
        j=random.randint(0,ncol-1)*13
        ij=str(i)+","+str(j)
        c=random.randint(1,9)    # color number
        pix=Pixel(canvas,i,j,nrow,ncol,scale,c)
        print(ij,"->",pix)

        
def test3(root,canvas,nrow,ncol,scale):
    print("Move one point along a square")

    pix=Pixel(canvas,35,35,nrow,ncol,scale,3)
    pix.vector=[-1,0] # set up direction (up)
    for i in range(30):
        pix.next()       # next move in the simulation 
        root.update()    # update the graphic
        time.sleep(0.05) # wait in second (simulation)
        
    pix.vector=[0,-1] # set up new direction (left)
    for i in range(30):
        pix.next()       # next move in the simulation 
        root.update()    # update the graphic
        time.sleep(0.05) # wait in second (simulation)
        
    pix.vector=[1,0]   # set up new direction (down)
    for i in range(30):
        pix.next()       # next move in the simulation 
        root.update()    # update the graphic
        time.sleep(0.05) # wait in second (simulation)
        
    pix.vector=[0,1]    # set up new direction (right)
    for i in range(30):
        pix.next()       # next move in the simulation 
        root.update()    # update the graphic
        time.sleep(0.05) # wait in second (simulation)

    #delete point
    pix.delete()


  
def test4(root,canvas,nrow,ncol,scale):
    print("Move four point along a square")

    pixs=[]
    pixs.append(Pixel(canvas,35,35,nrow,ncol,scale,3,[-1,0]))
    pixs.append(Pixel(canvas,5,35,nrow,ncol,scale,4,[0,-1]))
    pixs.append(Pixel(canvas,5,5,nrow,ncol,scale,5,[1,0]))
    pixs.append(Pixel(canvas,35,5,nrow,ncol,scale,6,[0,1]))
    
    print("Starting coords")
    for p in pixs: print(p)

    for i in range(30):
        for p in pixs:
            p.next()       # next move in the simulation     
        root.update()      # update the graphic
        time.sleep(0.05)   # wait in second (simulation)

    print("Ending coords")
    for p in pixs:
        print(p)
        p.delete()


        
def test5(root,canvas,nrow,ncol,scale):
    print("Move one point any direction -use arrow commands")

    pix=Pixel(canvas,20,20,nrow,ncol,scale,2)

    ### binding used by test5
    root.bind("<Right>",lambda e:pix.right())
    root.bind("<Left>",lambda e:pix.left())
    root.bind("<Up>",lambda e:pix.up())
    root.bind("<Down>",lambda e:pix.down())

    ### simulation
    while True:
        pix.next()
        root.update()     # update the graphic
        time.sleep(0.05)  # wait in second (simulation)



        

###################################################
#################### Main method ##################
###################################################


def main():
       
        ##### create a window, canvas
        root = Tk() # instantiate a tkinter window
        nrow=40
        ncol=40
        scale=20
        canvas = Canvas(root,width=ncol*scale,height=nrow*scale,bg="black") # create a canvas width*height
        canvas.pack()

        ### general binding events to choose a testing function
        root.bind("1",lambda e:test1(canvas,nrow,ncol,scale))
        root.bind("2",lambda e:test2(canvas,nrow,ncol,scale))
        root.bind("3",lambda e:test3(root,canvas,nrow,ncol,scale))
        root.bind("4",lambda e:test4(root,canvas,nrow,ncol,scale))
        root.bind("5",lambda e:test5(root,canvas,nrow,ncol,scale))
        root.bind("<d>",lambda e:delete_all(canvas))
        
       
        
        root.mainloop() # wait until the window is closed
        
if __name__=="__main__":
    main()

