'''
Created on 15/11/2012

@author: Andreas M
'''
def do_Plus(X):
    C = X+2
    return(C)


print(do_Plus(5))

def do_Plus2(X):
    C = X+"hello"
    return(C)


print(do_Plus2("cake"))    

print("task done")
#next task

def type123(X):

    if type(X) == type(int()):
        print(do_Plus(X))
        
    elif type(X) == type(str()):    

        print(do_Plus2(X))
    else:
        print("please enter a string")
        
type123(5)
type123("a")
    
type123(5.5)

print("task done")
#task done