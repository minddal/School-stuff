'''
Created on 30/11/2012

@author: Andreas M
'''
from tkinter import *

def countdown(n=6):  
    if n<=0:
        print ("Boom!!")
        
    else:
        print (n)
        import time
        time.sleep(1)
        countdown(n-1) 
        
#countdown(5)   

win = Frame()

win.pack()
Label(win, text="Click Add to get the sum or Quit to Exit").pack(side=TOP)
Button(win, text="Start", command=countdown).pack(side=LEFT)
Button(win, text="Quit", command=win.quit).pack(side=RIGHT)
win.mainloop()