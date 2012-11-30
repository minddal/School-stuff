'''
Created on 01/11/2012

@author: Andreas M
'''
def countdown(n):  
    if n<=0:
        print ("Boom!!")
        
    else:
        print (n)
        import time
        time.sleep(1)
        countdown(n-1) 
        
countdown(5)     
      
