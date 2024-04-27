from tkinter import *
from Grid import Grid
from Pixel import Pixel
import time


### complete class Snake
            
        
class Snake:
     

#########################################################
############# Main code #################################
#########################################################
    

  
def main(): 
        
        ##### create a window, canvas 
        root = Tk() # instantiate a tkinter window
        python = Snake(root,20,20) #20 obstacles, and 20 fruits
        #python = Snake(root,5,5,25,25,30) # 5 obstacles/fruits, 25 row, 25 column, 30 scale
        
        
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

