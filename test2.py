import numpy as np
import random

def min(input):  
    minInd = 0    #set a minimum number
    for i in range(len(input)):   # set a loop of index
        if input[i] < input[minInd]:  #find the index of the minimum number
            minInd = i
    return minInd #return the index of the minimum number

def sort(input): 
    list = []  #set a list to store the arrary
    for i in range(len(input)):
        minInd = min(input)  #use the function to find the minimum number
        list.append(input[minInd])   #append the minimum number to the list
        input.pop(minInd)  #delete the index of the minimum number
    return list

if __name__== '__main__':
    data = []
    for i in range(10):
        data.append(random.randrange(0,100))   # generate 10 numbers ranging from 0 to 100
    result=sort(data)  #set an array to store the result of sort
    print(result)