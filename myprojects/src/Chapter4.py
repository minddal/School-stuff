'''
Created on 15/11/2012

@author: Andreas M
'''
fridge = {"milk" : "goat", "Beer" : "Refreshing" , "Cheese" : "Stinky"}

try:
    wrongkey = fridge["Book"]

except KeyError:
    print("We have no books")
    
try:
    goodkey = fridge["Beer"]
except KeyError:
    print("We have no beer")           