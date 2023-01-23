def loop():
    x=y=8   #set up the range of square 8*8
    for i in range(1,x+1):      #set the loop of x of list
        for j in range(1,y+1):    #set a nested loop of y of list
            print(i,j)       

if __name__== '__main__':
    loop()