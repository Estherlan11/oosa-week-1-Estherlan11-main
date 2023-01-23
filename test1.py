import numpy as np

def min():
    data=np.random.random((10))  #craete an array of 10 random numbers
    min = data[0]  #set up the minimum number in the array
    for i in data:   #set a loop of the array
        if i < min:  #set a condition of the minimum number
            min = i
    print(min)

if __name__== '__main__':
    min()